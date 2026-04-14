#!/usr/bin/env python3
"""
Markdown to Confluence Page Updater & Creator
==============================================

What this script does (in plain language):
1. Reads a markdown (.md) file from your computer
2. Converts it to HTML that Confluence can understand
3. Finds all image references in the markdown (like ![alt](path/to/image.png))
4. Checks which images are already uploaded to the Confluence page
5. Uploads any missing images as attachments
6. Converts image references to Confluence's special <ac:image> format
7. Converts blockquotes starting with **bold label:** to Confluence info/note panels
8. Converts @Name mentions to Confluence <ac:link><ri:user> macros (lookup from team directory)
9. Adds Table of Contents macro (H1-H3) at the top of the page
10. Converts DD-MM-YYYY dates to Confluence <time> date macros
11. Updates (or creates) the Confluence page with the new HTML content

How to use:

  UPDATE an existing page:
    python3 md-to-confluence.py <page_id> <markdown_file>
    python3 md-to-confluence.py <page_id> <markdown_file> --title "New Page Title"
    python3 md-to-confluence.py <page_id> <markdown_file> --message "What changed"
    python3 md-to-confluence.py <page_id> <markdown_file> --dry-run
    python3 md-to-confluence.py <page_id> <markdown_file> --image-dir path/to/images

  CREATE a new page under a parent:
    python3 md-to-confluence.py --create --parent-id <parent_id> --space [SPACE_KEY] --title "My Page" <markdown_file>
    python3 md-to-confluence.py --create --parent-id <parent_id> --space [SPACE_KEY] --title "My Page" <markdown_file> --wide

  BATCH CREATE multiple pages under a parent:
    python3 md-to-confluence.py --create --parent-id <parent_id> --space [SPACE_KEY] file1.md file2.md file3.md --wide

Prerequisites:
    - .env file at the project root with CONFLUENCE_EMAIL, CONFLUENCE_TOKEN, CONFLUENCE_BASE_URL
    - pandoc installed (brew install pandoc)
    - Optional: team directory file at .local/team/users.md for @mention conversion
"""

import http.client
import json
import base64
import os
import re
import sys
import subprocess
import argparse
import urllib.parse
from pathlib import Path


def load_env():
    """Load .env file from project root (walk up from script location)."""
    current = Path(__file__).resolve().parent
    for _ in range(10):
        env_file = current / '.env'
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, _, value = line.partition('=')
                        os.environ.setdefault(key.strip(), value.strip())
            print(f"Loaded credentials from: {env_file}")
            return
        current = current.parent
    print("WARNING: No .env file found")


def get_confluence_host():
    """Get the Confluence hostname from environment."""
    base_url = os.environ.get('CONFLUENCE_BASE_URL', '')
    if not base_url:
        print("ERROR: CONFLUENCE_BASE_URL not set in .env or environment")
        sys.exit(1)
    return base_url.replace("https://", "").replace("http://", "")


def get_auth_header():
    """Build Basic auth header from env vars."""
    email = os.environ.get('CONFLUENCE_EMAIL', '')
    token = os.environ.get('CONFLUENCE_TOKEN', '')
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    return f'Basic {auth}'


def get_space_id(space_key):
    """Get the numeric space ID from a space key."""
    host = get_confluence_host()
    conn = http.client.HTTPSConnection(host)
    conn.request('GET', f'/wiki/api/v2/spaces?keys={urllib.parse.quote(space_key)}', headers={
        'Authorization': get_auth_header(),
        'Accept': 'application/json'
    })
    resp = conn.getresponse()
    data = json.loads(resp.read().decode())
    conn.close()
    if 'results' in data and len(data['results']) > 0:
        return data['results'][0]['id']
    print(f"ERROR: Could not find space ID for '{space_key}': {data}")
    sys.exit(1)


def create_page(space_id, parent_id, title, html_body):
    """Create a new Confluence page under a parent using the v2 API.
    Returns (page_id, web_url) on success."""
    host = get_confluence_host()
    conn = http.client.HTTPSConnection(host)
    payload = json.dumps({
        'spaceId': space_id,
        'parentId': parent_id,
        'status': 'current',
        'title': title,
        'body': {
            'representation': 'storage',
            'value': html_body
        }
    })
    conn.request('POST', '/wiki/api/v2/pages', body=payload, headers={
        'Authorization': get_auth_header(),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    })
    resp = conn.getresponse()
    resp_body = resp.read().decode()
    conn.close()

    if resp.status in (200, 201):
        result = json.loads(resp_body)
        page_id = result.get('id')
        web_url = result.get('_links', {}).get('webui', '')
        return page_id, web_url
    else:
        print(f"ERROR creating page '{title}': {resp.status} - {resp_body[:500]}")
        return None, None


def extract_title_from_md(md_content):
    """Extract the first H1 heading from markdown content to use as page title."""
    match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        title = re.sub(r'\s*[-]+\s*$', '', title)
        return title
    return None


def get_page_info(page_id):
    """Fetch current page version and title."""
    host = get_confluence_host()
    conn = http.client.HTTPSConnection(host)
    headers = {
        'Authorization': get_auth_header(),
        'Accept': 'application/json'
    }
    conn.request('GET', f'/wiki/api/v2/pages/{page_id}', headers=headers)
    resp = conn.getresponse()
    data = json.loads(resp.read().decode())
    conn.close()

    if resp.status != 200:
        print(f"ERROR: Could not fetch page {page_id}: {resp.status}")
        sys.exit(1)

    return {
        'version': data['version']['number'],
        'title': data['title'],
        'id': page_id
    }


def list_attachments(page_id):
    """List all existing attachments on the page."""
    host = get_confluence_host()
    conn = http.client.HTTPSConnection(host)
    headers = {
        'Authorization': get_auth_header(),
        'Accept': 'application/json'
    }
    conn.request('GET', f'/wiki/rest/api/content/{page_id}/child/attachment?limit=100', headers=headers)
    resp = conn.getresponse()
    data = json.loads(resp.read().decode())
    conn.close()

    existing = set()
    for att in data.get('results', []):
        existing.add(att['title'])
    return existing


def upload_attachment(page_id, filepath, filename):
    """Upload a single file as an attachment to the page."""
    with open(filepath, 'rb') as f:
        file_data = f.read()

    boundary = '----FormBoundary7MA4YWxkTrZu0gW'
    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f'Content-Type: image/png\r\n\r\n'
    ).encode() + file_data + f'\r\n--{boundary}--\r\n'.encode()

    headers = {
        'Authorization': get_auth_header(),
        'X-Atlassian-Token': 'nocheck',
        'Content-Type': f'multipart/form-data; boundary={boundary}',
    }

    host = get_confluence_host()
    conn = http.client.HTTPSConnection(host)
    conn.request('PUT', f'/wiki/rest/api/content/{page_id}/child/attachment', body=body, headers=headers)
    resp = conn.getresponse()
    resp.read()
    status = resp.status
    conn.close()
    return status in (200, 201)


def convert_md_to_html(md_file):
    """Convert markdown to HTML using pandoc."""
    result = subprocess.run(
        ['pandoc', str(md_file), '-f', 'markdown', '-t', 'html', '--wrap=none'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"ERROR: pandoc failed: {result.stderr}")
        sys.exit(1)
    return result.stdout


def extract_image_refs(md_content):
    """Extract all image references from markdown content."""
    return re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', md_content)


def transform_html_for_confluence(html, image_map):
    """Transform pandoc HTML to Confluence storage format."""
    # Replace <img> tags with ac:image macros
    def replace_img(match):
        full_tag = match.group(0)
        src_match = re.search(r'src="([^"]+)"', full_tag)
        if not src_match:
            return full_tag
        src = src_match.group(1)
        filename = image_map.get(src, os.path.basename(src))
        return f'<ac:image ac:width="1350"><ri:attachment ri:filename="{filename}" /></ac:image>'

    html = re.sub(r'<img[^>]+/?>', replace_img, html)

    # Strip id attributes from headings
    html = re.sub(r'(<h[1-6])\s+id="[^"]*"', r'\1', html)

    # Strip <figure>/<figcaption> wrappers
    html = re.sub(r'<figure[^>]*>', '', html)
    html = re.sub(r'</figure>', '', html)
    html = re.sub(r'<figcaption[^>]*>.*?</figcaption>', '', html, flags=re.DOTALL)

    # Convert blockquotes with bold labels to Confluence panels
    def replace_blockquote(match):
        content = match.group(1)
        note_keywords = ['pre-requisite', 'pre-condition', 'important', 'note', 'when to do']
        info_keywords = ['why this is needed', 'when to use']

        content_lower = content.lower()
        panel_type = 'info'
        for kw in note_keywords:
            if kw in content_lower:
                panel_type = 'note'
                break
        for kw in info_keywords:
            if kw in content_lower:
                panel_type = 'info'
                break

        return f'<ac:structured-macro ac:name="{panel_type}"><ac:rich-text-body>{content}</ac:rich-text-body></ac:structured-macro>'

    html = re.sub(
        r'<blockquote>\s*(.*?)\s*</blockquote>',
        replace_blockquote,
        html,
        flags=re.DOTALL
    )

    # Add line breaks between metadata keys in info/note panels
    def split_metadata_keys(match):
        content = match.group(1)
        content = re.sub(r'(?<!^)\s+(<strong>[^<]+:</strong>)', r'<br/>\1', content)
        return f'<ac:rich-text-body>{content}</ac:rich-text-body>'

    html = re.sub(
        r'<ac:rich-text-body>(.*?)</ac:rich-text-body>',
        split_metadata_keys,
        html,
        flags=re.DOTALL
    )

    # Convert <pre><code> to Confluence code macro
    def replace_code(match):
        code_content = match.group(1)
        code_content = re.sub(r'<code[^>]*>', '', code_content).replace('</code>', '')
        return f'<ac:structured-macro ac:name="code"><ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body></ac:structured-macro>'

    html = re.sub(
        r'<pre><code[^>]*>(.*?)</code></pre>',
        replace_code,
        html,
        flags=re.DOTALL
    )

    return html


def load_users_map():
    """Load user name -> Jira account ID map from a team directory file.

    Looks for .local/team/users.md in the project root.
    Expected format: | Short Name | Full Name | Email | Jira Account ID | Role |

    Returns dict like {'Alice Smith': '6267ace0a32183006f23a09e', ...}
    """
    users = {}
    current = Path(__file__).resolve().parent
    users_file = None
    for _ in range(10):
        candidate = current / '.local' / 'team' / 'users.md'
        if candidate.exists():
            users_file = candidate
            break
        current = current.parent

    if not users_file:
        return users

    with open(users_file) as f:
        for line in f:
            parts = [p.strip() for p in line.strip().split('|')]
            if len(parts) >= 6:
                full_name = parts[2]
                account_id = parts[4]
                if (full_name and account_id and
                    full_name != 'Full Name' and
                    not full_name.startswith('--') and
                    account_id != 'Jira Account ID' and
                    account_id != '\u2014'):
                    users[full_name] = account_id
    return users


def convert_at_mentions(html):
    """Convert @Name references to Confluence <ac:link><ri:user> macros."""
    users = load_users_map()
    if not users:
        return html

    for name in sorted(users.keys(), key=len, reverse=True):
        account_id = users[name]
        first_name = name.split()[0]
        last_parts = name.split()[1:]
        replacement = f'<ac:link><ri:user ri:account-id="{account_id}" /></ac:link>'

        # Handle pandoc's citation span wrapping
        if last_parts:
            last_name = ' '.join(last_parts)
            citation_pattern = (
                f'<span class="citation"[^>]*>@{re.escape(first_name)}</span>'
                f'\\s*{re.escape(last_name)}'
            )
            html = re.sub(citation_pattern, replacement, html)

        pattern = f'@{re.escape(name)}'
        html = re.sub(pattern, replacement, html)

    return html


def convert_all_dates(html):
    """Convert DD-MM-YYYY date strings anywhere in the page to Confluence <time> macros."""
    def replace_date(m):
        prefix = html[:m.start()]
        if prefix.rstrip().endswith('datetime="'):
            return m.group(0)
        day, month, year = m.group(1), m.group(2), m.group(3)
        if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
            return m.group(0)
        iso_date = f'{year}-{month}-{day}'
        return f'<time datetime="{iso_date}" />'

    html = re.sub(
        r'(?<!datetime=")\b(\d{2})-(\d{2})-(\d{4})\b',
        replace_date,
        html
    )
    return html


def strip_manual_number_column(html):
    """Remove manual '#' or 'Sr' first columns from HTML tables before adding numberingColumn."""
    def process_table(match):
        table_html = match.group(0)

        first_th = re.search(r'<th[^>]*>(?:<strong>)?\s*(.*?)\s*(?:</strong>)?</th>', table_html)
        if not first_th:
            return table_html

        header_text = first_th.group(1).strip()
        if header_text not in ('#', 'Sr', 'Sr.', 'S#', 'S.No', 'S.No.', 'No', 'No.'):
            return table_html

        table_html = re.sub(
            r'(<tr[^>]*>)\s*<th[^>]*>(?:<strong>)?\s*(?:#|Sr\.?|S#|S\.No\.?|No\.?)\s*(?:</strong>)?</th>',
            r'\1',
            table_html, count=1)

        table_html = re.sub(
            r'(<tr[^>]*>)\s*<td[^>]*>(?:<strong>)?\s*\d+\s*(?:</strong>)?</td>',
            r'\1',
            table_html)

        return table_html

    html = re.sub(r'<table[^>]*>.*?</table>', process_table, html, flags=re.DOTALL)
    return html


def add_toc_macro(html):
    """Add a Table of Contents macro at the top of the page."""
    toc_macro = (
        '<ac:structured-macro ac:name="toc">'
        '<ac:parameter ac:name="maxLevel">3</ac:parameter>'
        '</ac:structured-macro>'
    )

    if 'ac:name="toc"' in html:
        return html

    return toc_macro + html


def strip_h1_and_source(html):
    """Remove the first H1 heading and the Source callout from HTML."""
    html = re.sub(r'<h1[^>]*>.*?</h1>\s*', '', html, count=1)

    html = re.sub(
        r'<ac:structured-macro ac:name="info"[^>]*>\s*<ac:rich-text-body>\s*<p>\s*Source:.*?</p>\s*</ac:rich-text-body>\s*</ac:structured-macro>\s*',
        '', html, flags=re.DOTALL)
    html = re.sub(
        r'<blockquote>\s*<p>\s*Source:.*?</p>\s*</blockquote>\s*',
        '', html, flags=re.DOTALL)

    html = re.sub(r'^(\s*<hr\s*/?>\s*)+', '', html)

    return html


def make_tables_wide(html):
    """Add data-layout='wide' and data-table-width='1800' to all tables."""
    html = re.sub(
        r'<table(?![^>]*data-layout)([^>]*)>',
        r'<table data-table-width="1800" data-layout="wide"\1>',
        html
    )
    return html


def add_numbering_columns(html):
    """Add Confluence auto-numbering columns to all tables."""
    def process_table(match):
        table_html = match.group(0)

        table_html = re.sub(
            r'(<tr[^>]*>)\s*(<th)',
            r'\1<th class="numberingColumn"></th>\2',
            table_html, count=1)

        row_num = [0]
        def add_row_number(m):
            row_num[0] += 1
            return f'{m.group(1)}<td class="numberingColumn">{row_num[0]}</td>{m.group(2)}'

        table_html = re.sub(
            r'(<tr[^>]*>)\s*(<td)',
            add_row_number,
            table_html)

        return table_html

    html = re.sub(r'<table[^>]*>.*?</table>', process_table, html, flags=re.DOTALL)
    return html


def bold_header_cells(html):
    """Wrap <th> text content in <strong> tags so header rows render bold."""
    def bold_th(match):
        attrs = match.group(1)
        content = match.group(2)
        if not content.strip():
            return match.group(0)
        if 'numberingColumn' in attrs:
            return match.group(0)
        if '<strong>' in content:
            return match.group(0)
        return f'<th{attrs}><strong>{content}</strong></th>'

    html = re.sub(r'<th([^>/]*)>([^<]+)</th>', bold_th, html)
    return html


def fix_column_widths(html):
    """Replace pandoc's equal-percentage colgroup with proportional pixel widths."""
    WIDE_COLS = {'rationale', 'summary', 'description', 'reason', 'theme', 'meaning',
                 'details', 'notes', 'comment', 'context',
                 'acceptance criteria', 'steps to reproduce', 'expected behaviour'}
    NARROW_COLS = {'#', 'type', 'count', 'direction', 'p', 'status', 'sr', 'sr.'}

    def process_table(match):
        table_html = match.group(0)

        headers = re.findall(r'<th(?:(?!numberingColumn)[^>])*>(?:<strong>)?(.*?)(?:</strong>)?</th>',
                             table_html, re.DOTALL)
        header_texts = [re.sub(r'<[^>]+>', '', h).strip() for h in headers if h.strip()]

        if not header_texts:
            return table_html

        has_numbering = 'numberingColumn' in table_html

        total_width = 1800
        numbering_width = 40 if has_numbering else 0
        available = total_width - numbering_width

        weights = []
        for h in header_texts:
            h_lower = h.lower()
            if h_lower in NARROW_COLS or len(h) <= 4:
                weights.append(1)
            elif h_lower in WIDE_COLS:
                weights.append(6)
            elif len(h) <= 10:
                weights.append(2)
            else:
                weights.append(3)

        total_weight = sum(weights)
        widths = [round(available * w / total_weight) for w in weights]

        cols = ['<col />'] if has_numbering else []
        for w in widths:
            cols.append(f'<col style="width: {w}.0px;" />')
        new_colgroup = f'<colgroup>{"".join(cols)}</colgroup>'

        existing_cg = re.search(r'<colgroup>.*?</colgroup>', table_html, re.DOTALL)
        if existing_cg:
            table_html = table_html.replace(existing_cg.group(0), new_colgroup)
        else:
            table_html = re.sub(r'(<table[^>]*>)', r'\1' + new_colgroup, table_html)

        return table_html

    html = re.sub(r'<table[^>]*>.*?</table>', process_table, html, flags=re.DOTALL)
    return html


def set_wide_mode(page_id):
    """Set the Confluence page to full-width (wide) mode."""
    host = get_confluence_host()
    headers = {
        'Authorization': get_auth_header(),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    for prop_key in ['content-appearance-draft', 'content-appearance-published']:
        conn = http.client.HTTPSConnection(host)
        conn.request('GET', f'/wiki/rest/api/content/{page_id}/property/{prop_key}', headers=headers)
        resp = conn.getresponse()
        resp_body = resp.read().decode()
        conn.close()

        if resp.status == 200:
            current_version = json.loads(resp_body)['version']['number']
            method = 'PUT'
            url = f'/wiki/rest/api/content/{page_id}/property/{prop_key}'
            body = json.dumps({
                "key": prop_key,
                "value": "full-width",
                "version": {"number": current_version + 1}
            })
        else:
            method = 'POST'
            url = f'/wiki/rest/api/content/{page_id}/property'
            body = json.dumps({
                "key": prop_key,
                "value": "full-width",
                "version": {"number": 1}
            })

        conn2 = http.client.HTTPSConnection(host)
        conn2.request(method, url, body=body, headers=headers)
        resp2 = conn2.getresponse()
        resp2.read()
        conn2.close()

    print("  Wide mode: enabled (full-width)")


def process_single_file(md_path, image_dir=None):
    """Read a markdown file and prepare HTML + image data for Confluence."""
    md_content = md_path.read_text()
    md_dir = md_path.parent

    image_refs = extract_image_refs(md_content)
    print(f"  Images found in markdown: {len(image_refs)}")

    image_map = {}
    image_files = {}
    for alt_text, img_path in image_refs:
        filename = os.path.basename(img_path)
        image_map[img_path] = filename
        full_path = md_dir / img_path
        if image_dir:
            alt_path = Path(image_dir) / filename
            if alt_path.exists():
                full_path = alt_path
        if full_path.exists():
            image_files[filename] = str(full_path)

    html = convert_md_to_html(md_path)
    html = transform_html_for_confluence(html, image_map)
    html = strip_h1_and_source(html)
    html = add_toc_macro(html)
    html = convert_at_mentions(html)
    html = make_tables_wide(html)
    html = strip_manual_number_column(html)
    html = add_numbering_columns(html)
    html = bold_header_cells(html)
    html = fix_column_widths(html)
    html = convert_all_dates(html)

    return html, image_map, image_files, md_content


def handle_attachments(page_id, image_files, dry_run=False):
    """Check and upload missing attachments for a page."""
    existing_attachments = list_attachments(page_id)
    print(f"  Existing attachments: {len(existing_attachments)}")

    missing = []
    for filename, filepath in image_files.items():
        if filename not in existing_attachments:
            missing.append((filename, filepath))

    if missing:
        print(f"  Missing attachments to upload: {len(missing)}")
        for fn, _ in missing:
            print(f"    - {fn}")

    if not dry_run:
        for filename, filepath in missing:
            ok = upload_attachment(page_id, filepath, filename)
            status = "UPLOADED" if ok else "FAILED"
            print(f"  {status}: {filename}")

    return missing


def verify_push(page_id):
    """Fetch the pushed page from Confluence and run quality checks."""
    host = get_confluence_host()
    conn = http.client.HTTPSConnection(host)
    conn.request('GET', f'/wiki/rest/api/content/{page_id}?expand=body.storage',
                 headers={'Authorization': get_auth_header()})
    resp = conn.getresponse()
    if resp.status != 200:
        print(f"  Verify: could not fetch page (HTTP {resp.status})")
        resp.read()
        conn.close()
        return 0, 0
    html = json.loads(resp.read())['body']['storage']['value']
    conn.close()

    has_tables = '<table' in html

    checks = [
        ('No duplicate H1',       '<h1' not in html),
        ('Numbering columns',     'numberingColumn' in html if has_tables else True),
        ('Wide tables',           'data-table-width' in html if has_tables else True),
        ('No plain @mentions',    'class="citation"' not in html),
        ('TOC macro',             'ac:name="toc"' in html),
        ('Date macros',           '<time datetime' in html
                                  if re.search(r'\b\d{2}-\d{2}-\d{4}\b', html) else True),
        ('No source callout',     'Source:' not in html or 'Confluence' not in html),
        ('No broken images',     'UNKNOWN_ATTACHMENT' not in html),
    ]

    passed = sum(1 for _, ok in checks if ok)
    total = len(checks)

    print(f"\n  Verify: {passed}/{total} checks passed")
    for name, ok in checks:
        if not ok:
            print(f"    FAIL: {name}")

    if passed == total:
        print("    All checks passed!")

    return passed, total


def main():
    parser = argparse.ArgumentParser(
        description='Push markdown to Confluence - update existing pages or create new ones',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--create', action='store_true',
                        help='Create new page(s) under a parent instead of updating an existing page')
    parser.add_argument('--parent-id',
                        help='Parent page ID (required with --create)')
    parser.add_argument('--space',
                        help='Confluence space key (required with --create)')

    parser.add_argument('args', nargs='+',
                        help='For update mode: <page_id> <markdown_file>. For create mode: <markdown_file> [...]')

    parser.add_argument('--title',
                        help='Page title (default: first H1 heading from the markdown file)')
    parser.add_argument('--message',
                        help='Version message (default: auto-generated)')
    parser.add_argument('--image-dir',
                        help='Directory containing images (default: auto-detect from markdown)')
    parser.add_argument('--wide', action='store_true',
                        help='Set page to full-width (wide) mode')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would happen without making changes')

    parsed = parser.parse_args()
    load_env()

    if parsed.create:
        # --- CREATE MODE ---
        if not parsed.parent_id:
            print("ERROR: --parent-id is required with --create")
            sys.exit(1)
        if not parsed.space:
            print("ERROR: --space is required with --create")
            sys.exit(1)

        md_files = [Path(f) for f in parsed.args]
        for f in md_files:
            if not f.exists():
                print(f"ERROR: File not found: {f}")
                sys.exit(1)

        print(f"Getting space ID for {parsed.space}...")
        space_id = get_space_id(parsed.space)
        print(f"Space ID: {space_id}")

        host = get_confluence_host()
        base_url = os.environ.get('CONFLUENCE_BASE_URL', '')
        results = []
        for md_path in md_files:
            print(f"\nProcessing: {md_path}")

            html, image_map, image_files, md_content = process_single_file(md_path, parsed.image_dir)

            if parsed.title and len(md_files) == 1:
                title = parsed.title
            else:
                title = extract_title_from_md(md_content)
                if not title:
                    title = md_path.stem.replace('-', ' ').title()
            print(f"  Title: {title}")
            print(f"  HTML size: {len(html)} chars")

            if parsed.dry_run:
                print(f"  [DRY RUN] Would create page '{title}' under parent {parsed.parent_id}")
                results.append({'file': md_path.name, 'status': 'dry-run', 'title': title})
                continue

            page_id, web_url = create_page(space_id, parsed.parent_id, title, html)
            if page_id:
                full_url = f"{base_url}/wiki{web_url}" if web_url else f"{base_url}/wiki/spaces/{parsed.space}/pages/{page_id}"
                print(f"  Created! Page ID: {page_id}")
                print(f"  URL: {full_url}")

                if image_files:
                    handle_attachments(page_id, image_files)

                    page_info = get_page_info(page_id)
                    repush_body = {
                        "id": page_id,
                        "status": "current",
                        "title": title,
                        "body": {
                            "representation": "storage",
                            "value": html
                        },
                        "version": {
                            "number": page_info['version'] + 1,
                            "message": "Re-push after attachment upload"
                        }
                    }
                    conn_rp = http.client.HTTPSConnection(host)
                    conn_rp.request('PUT', f'/wiki/api/v2/pages/{page_id}',
                                    body=json.dumps(repush_body),
                                    headers={
                                        'Authorization': get_auth_header(),
                                        'Content-Type': 'application/json',
                                        'Accept': 'application/json'
                                    })
                    rp_resp = conn_rp.getresponse()
                    rp_resp.read()
                    conn_rp.close()
                    if rp_resp.status == 200:
                        print("  Re-pushed HTML after attachment upload")
                    else:
                        print(f"  WARNING: Re-push failed ({rp_resp.status}) - images may show as UNKNOWN_ATTACHMENT")

                if parsed.wide:
                    set_wide_mode(page_id)

                verify_push(page_id)

                results.append({'file': md_path.name, 'status': 'success', 'page_id': page_id, 'url': full_url})
            else:
                results.append({'file': md_path.name, 'status': 'error'})

        # Summary
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        success = [r for r in results if r['status'] == 'success']
        errors = [r for r in results if r['status'] == 'error']
        print(f"Created: {len(success)} / {len(results)} pages")
        if errors:
            print(f"Errors: {len(errors)}")
            for e in errors:
                print(f"  - {e['file']}")
        for r in success:
            print(f"  {r['file']} -> {r['url']}")

    else:
        # --- UPDATE MODE ---
        if len(parsed.args) < 2:
            print("ERROR: Update mode requires <page_id> <markdown_file>")
            print("  Use --create for creating new pages")
            sys.exit(1)

        page_id = parsed.args[0]
        md_path = Path(parsed.args[1])

        if not md_path.exists():
            print(f"ERROR: File not found: {md_path}")
            sys.exit(1)

        print(f"Reading: {md_path}")

        html, image_map, image_files, md_content = process_single_file(md_path, parsed.image_dir)

        page_info = get_page_info(page_id)
        print(f"  Page: '{page_info['title']}', version: {page_info['version']}")

        missing = handle_attachments(page_id, image_files, parsed.dry_run)

        if parsed.dry_run:
            print("\n[DRY RUN] Would perform:")
            print(f"  - Upload {len(missing)} attachments")
            print(f"  - Update page to version {page_info['version'] + 1}")
            if parsed.title:
                print(f"  - Change title to: {parsed.title}")
            return

        title = parsed.title or page_info['title']
        message = parsed.message or f"Updated from {md_path.name}"

        update_body = {
            "id": page_id,
            "status": "current",
            "title": title,
            "body": {
                "representation": "storage",
                "value": html
            },
            "version": {
                "number": page_info['version'] + 1,
                "message": message
            }
        }

        host = get_confluence_host()
        conn = http.client.HTTPSConnection(host)
        headers = {
            'Authorization': get_auth_header(),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        conn.request('PUT', f'/wiki/api/v2/pages/{page_id}', body=json.dumps(update_body), headers=headers)
        resp = conn.getresponse()
        resp_body = resp.read().decode()
        conn.close()

        base_url = os.environ.get('CONFLUENCE_BASE_URL', '')
        if resp.status == 200:
            result = json.loads(resp_body)
            new_version = result['version']['number']
            print(f"\nSUCCESS - Page updated to version {new_version}")
            print(f"URL: {base_url}/wiki/spaces/{result.get('spaceId', '...')}/pages/{page_id}")

            if parsed.wide:
                set_wide_mode(page_id)

            verify_push(page_id)
        else:
            print(f"\nERROR {resp.status}: {resp_body[:500]}")
            sys.exit(1)


if __name__ == '__main__':
    main()
