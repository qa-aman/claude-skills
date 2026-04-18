#!/usr/bin/env python3
"""
Markdown → Confluence Page Updater & Creator
==============================================

What this script does (in plain language):
1. Reads a markdown (.md) file from your computer
2. Converts it to HTML that Confluence can understand
3. Finds all image references in the markdown (like ![alt](path/to/image.png))
4. Checks which images are already uploaded to the Confluence page
5. Uploads any missing images as attachments
6. Converts image references to Confluence's special <ac:image> format
7. Converts blockquotes starting with **bold label:** to Confluence info/note panels
8. Converts @Name mentions to Confluence <ac:link><ri:user> macros (lookup from .local/team/users.md)
9. Adds Table of Contents macro (H1-H3) at the top of the page
10. Converts DD-MM-YYYY dates in the Versioning table to Confluence <time> date macros
11. Formats the Versioning table with grey subtext and dark grey header row background
12. Updates (or creates) the Confluence page with the new HTML content

How to use:

  UPDATE an existing page:
    python3 .claude/scripts/md-to-confluence.py <page_id> <markdown_file>
    python3 .claude/scripts/md-to-confluence.py <page_id> <markdown_file> --title "New Page Title"
    python3 .claude/scripts/md-to-confluence.py <page_id> <markdown_file> --message "What changed"
    python3 .claude/scripts/md-to-confluence.py <page_id> <markdown_file> --dry-run
    python3 .claude/scripts/md-to-confluence.py <page_id> <markdown_file> --image-dir path/to/images

  CREATE a new page under a parent:
    python3 .claude/scripts/md-to-confluence.py --create --parent-id <parent_id> --space <SPACE_KEY> --title "My Page" <markdown_file>
    python3 .claude/scripts/md-to-confluence.py --create --parent-id <parent_id> --space <SPACE_KEY> --title "My Page" <markdown_file> --wide

  BATCH CREATE multiple pages under a parent:
    python3 .claude/scripts/md-to-confluence.py --create --parent-id <parent_id> --space <SPACE_KEY> file1.md file2.md file3.md --wide

Prerequisites:
    - .env file at the project root with CONFLUENCE_EMAIL, CONFLUENCE_TOKEN, CONFLUENCE_BASE_URL
    - pandoc installed (brew install pandoc)

Examples:
    # Update an existing page
    python3 .claude/scripts/md-to-confluence.py 1234567890 my-doc.md

    # Dry run - see what would be uploaded without making changes
    python3 .claude/scripts/md-to-confluence.py 1234567890 my-doc.md --dry-run

    # Create a new page under a parent page
    python3 .claude/scripts/md-to-confluence.py --create --parent-id 9876543210 --space <SPACE_KEY> --title "My Guide" guide.md --wide

    # Batch create multiple pages (titles auto-derived from the first H1 heading in each file)
    python3 .claude/scripts/md-to-confluence.py --create --parent-id 9876543210 --space <SPACE_KEY> *.md --wide
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


def get_auth_header():
    """Build Basic auth header from env vars."""
    email = os.environ.get('CONFLUENCE_EMAIL', '')
    token = os.environ.get('CONFLUENCE_TOKEN', '')
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    return f'Basic {auth}'


def get_host():
    """Get Confluence host (without scheme) from CONFLUENCE_BASE_URL env var."""
    base_url = os.environ.get('CONFLUENCE_BASE_URL', '')
    if not base_url:
        print("ERROR: CONFLUENCE_BASE_URL not set in .env or environment")
        sys.exit(1)
    return base_url.replace("https://", "").replace("http://", "").rstrip('/')


def get_base_url():
    """Get full Confluence base URL (with scheme) from env var."""
    base_url = os.environ.get('CONFLUENCE_BASE_URL', '')
    if not base_url:
        print("ERROR: CONFLUENCE_BASE_URL not set in .env or environment")
        sys.exit(1)
    return base_url.rstrip('/')


def get_space_id(space_key):
    """Get the numeric space ID from a space key (e.g., 'DOCS' -> '12345678')."""
    conn = http.client.HTTPSConnection(get_host())
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
    conn = http.client.HTTPSConnection(get_host())
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
    """Extract the first H1 heading from markdown content to use as page title.
    Falls back to None if no H1 found."""
    match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        # Clean up any trailing markdown artifacts
        title = re.sub(r'\s*[-]+\s*$', '', title)
        return title
    return None


def get_page_info(page_id):
    """Fetch current page version and title."""
    conn = http.client.HTTPSConnection(get_host())
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
    conn = http.client.HTTPSConnection(get_host())
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

    conn = http.client.HTTPSConnection(get_host())
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
    """Extract all image references from markdown content.
    Returns list of (alt_text, image_path) tuples.
    """
    return re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', md_content)


def transform_html_for_confluence(html, image_map):
    """Transform pandoc HTML to Confluence storage format.

    - Replace <img> tags with <ac:image> macros
    - Convert blockquotes with bold labels to info/note panels
    """
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

    # Strip id attributes from headings — pandoc generates id="slug-of-heading" which
    # Confluence renders as visible text instead of an anchor attribute
    html = re.sub(r'(<h[1-6])\s+id="[^"]*"', r'\1', html)

    # Strip <figure>/<figcaption> wrappers that pandoc adds around images
    # These cause alt text to appear as visible captions on Confluence
    html = re.sub(r'<figure[^>]*>', '', html)
    html = re.sub(r'</figure>', '', html)
    html = re.sub(r'<figcaption[^>]*>.*?</figcaption>', '', html, flags=re.DOTALL)

    # Convert blockquotes with bold labels to Confluence panels
    # Pattern: <blockquote><p><strong>Label:</strong> text</p></blockquote>
    def replace_blockquote(match):
        content = match.group(1)
        # Determine panel type based on label
        note_keywords = ['pre-requisite', 'pre-condition', 'important', 'note', 'when to do',
                         'पूर्व शर्त', 'महत्वपूर्ण', 'नोट', 'कब करें']
        info_keywords = ['why this is needed', 'when to use', 'यह क्यों जरूरी है', 'कब उपयोग करें']

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
    # When multiple "> **Key:** value" lines are in a blockquote, pandoc merges them
    # into a single <p>. This splits them so each key-value pair is on its own line.
    def split_metadata_keys(match):
        content = match.group(1)
        # Add <br/> before each <strong>Key:</strong> except the first one
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
        # Remove any class attributes
        code_content = re.sub(r'<code[^>]*>', '', code_content).replace('</code>', '')
        return f'<ac:structured-macro ac:name="code"><ac:plain-text-body><![CDATA[{code_content}]]></ac:plain-text-body></ac:structured-macro>'

    html = re.sub(
        r'<pre><code[^>]*>(.*?)</code></pre>',
        replace_code,
        html,
        flags=re.DOTALL
    )

    return html


def resolve_local_spec_paths(html):
    """Replace local spec folder paths with Confluence page links.

    Why: Local paths like '001-student-onboarding/' or '002-level-check-test/level-check-test.md'
    are meaningless on Confluence. End users cannot navigate to local repo folders.
    This function scans all spec .md files for their '> Source: [Confluence](url)' line,
    builds a folder-number-to-URL mapping, and replaces any local folder references in the HTML.
    """
    # Find project root
    current = Path(__file__).resolve().parent
    spec_dir = None
    for _ in range(10):
        candidate = current / '01-product-spec-zone' / 'outputs' / '05-product-features'
        if candidate.exists():
            spec_dir = candidate
            break
        current = current.parent

    if not spec_dir:
        return html

    # Build mapping: folder pattern -> (page title, confluence URL)
    folder_map = {}
    for spec_folder in sorted(spec_dir.iterdir()):
        if not spec_folder.is_dir() or not re.match(r'\d{3}-', spec_folder.name):
            continue
        # Find main spec .md file and extract Source URL
        for md_file in spec_folder.glob('*.md'):
            if md_file.name in ('change.md', 'decisions.md'):
                continue
            try:
                with open(md_file) as f:
                    for line in f:
                        m = re.search(r'>\s*Source:\s*\[Confluence\]\((https://[^)]+)\)', line)
                        if m:
                            url = m.group(1)
                            # Extract a readable title from the folder name
                            title = spec_folder.name.split('-', 1)[1].replace('-', ' ').title()
                            folder_map[spec_folder.name] = (title, url)
                            break
            except Exception:
                continue

    if not folder_map:
        return html

    # Replace patterns like: NNN-feature-name/ or NNN-feature-name/filename.md
    # These appear as <code>NNN-feature-name/</code> or plain text in the HTML
    for folder_name, (title, url) in sorted(folder_map.items(), key=lambda x: len(x[0]), reverse=True):
        # Pattern 1: <code>NNN-feature-name/</code> or <code>NNN-feature-name/file.md</code>
        html = re.sub(
            rf'<code>{re.escape(folder_name)}[^<]*</code>',
            f'<a href="{url}">{title}</a>',
            html
        )
        # Pattern 2: plain text NNN-feature-name/ (not already in a link)
        html = re.sub(
            rf'(?<!href=")(?<!/">){re.escape(folder_name)}/?\w*\.?m?d?',
            f'<a href="{url}">{title}</a>',
            html
        )

    return html


def load_users_map():
    """Load user name -> Jira account ID map from .local/team/users.md.

    Why: Confluence @mentions require account IDs. This file is the canonical
    source for name-to-ID mapping in the project.

    Returns dict like {'Jane Doe': '6267ace0a32183006f23a09e', ...}
    """
    users = {}
    # Walk up from script to find project root (has .env)
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
            # Parse table rows: | Short Name | Full Name | Email | Jira Account ID | Role |
            parts = [p.strip() for p in line.strip().split('|')]
            if len(parts) >= 6:
                full_name = parts[2]
                account_id = parts[4]
                # Skip header, separator, empty, and placeholder rows
                if (full_name and account_id and
                    full_name != 'Full Name' and
                    not full_name.startswith('--') and
                    account_id != 'Jira Account ID' and
                    account_id != '—'):
                    users[full_name] = account_id
    return users


def convert_at_mentions(html):
    """Convert @Name references to Confluence <ac:link><ri:user> macros.

    Why: Pandoc outputs @Name as plain text. Confluence needs <ac:link> macros
    with account IDs for proper @mention rendering (blue pill badges).
    Looks up account IDs from .local/team/users.md.
    """
    users = load_users_map()
    if not users:
        return html

    # Sort by name length descending to match longer names first
    # (e.g., "Jane Doe" before "Jane")
    for name in sorted(users.keys(), key=len, reverse=True):
        account_id = users[name]
        first_name = name.split()[0]
        last_parts = name.split()[1:]
        replacement = f'<ac:link><ri:user ri:account-id="{account_id}" /></ac:link>'

        # Pattern 1: Pandoc wraps @FirstName in <span class="citation" data-cites="FirstName">@FirstName</span> LastName
        # This is pandoc's citation syntax kicking in on the @ symbol
        if last_parts:
            last_name = ' '.join(last_parts)
            citation_pattern = (
                f'<span class="citation"[^>]*>@{re.escape(first_name)}</span>'
                f'\\s*{re.escape(last_name)}'
            )
            html = re.sub(citation_pattern, replacement, html)

        # Pattern 2: Plain text @Name (in case pandoc doesn't wrap it)
        pattern = f'@{re.escape(name)}'
        html = re.sub(pattern, replacement, html)

    return html


def convert_versioning_dates(html):
    """Convert DD-MM-YYYY date strings in the Versioning table to Confluence <time> macros.

    Why: Confluence has a native date component (<time datetime="YYYY-MM-DD" />)
    that renders as a styled date pill. Plain text dates look unprofessional in
    versioning tables.

    Only converts dates in the first column after the numberingColumn in tables
    that follow a 'Versioning' heading.
    """
    # Find the versioning table — it follows <strong>Versioning</strong>
    versioning_pos = html.find('<strong>Versioning</strong>')
    if versioning_pos == -1:
        versioning_pos = html.find('>Versioning<')
    if versioning_pos == -1:
        return html

    # Find the next table after the Versioning heading
    table_start = html.find('<table', versioning_pos)
    if table_start == -1:
        return html
    table_end = html.find('</table>', table_start)
    if table_end == -1:
        return html
    table_end += len('</table>')

    table_html = html[table_start:table_end]

    # Convert DD-MM-YYYY dates in <td> cells to <time> macros
    def replace_date(m):
        day, month, year = m.group(1), m.group(2), m.group(3)
        iso_date = f'{year}-{month}-{day}'
        return f'<time datetime="{iso_date}" />'

    table_html = re.sub(
        r'(\b\d{2})-(\d{2})-(\d{4})\b',
        replace_date,
        table_html
    )

    html = html[:table_start] + table_html + html[table_end:]
    return html


def convert_all_dates(html):
    """Convert DD-MM-YYYY date strings anywhere in the page to Confluence <time> macros.

    Why: Markdown uses plain text dates (e.g., "30-03-2026") for local readability.
    Confluence has a native date component that renders as a styled date pill.
    This converts ALL DD-MM-YYYY dates — not just those in the Versioning table.

    Skips dates already inside <time> macros (from convert_versioning_dates).
    """
    def replace_date(m):
        # Skip if already inside a <time> macro
        prefix = html[:m.start()]
        if prefix.rstrip().endswith('datetime="'):
            return m.group(0)
        day, month, year = m.group(1), m.group(2), m.group(3)
        # Basic validation: month 01-12, day 01-31
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
    """Remove manual '#' or 'Sr' first columns from HTML tables before adding numberingColumn.

    Why: Markdown tables often have a manual '| # |' first column for local readability.
    The script auto-adds Confluence's built-in numberingColumn, so keeping the manual
    column creates DUPLICATE row numbers on the pushed page.

    This strips the first column from tables where the header is '#', 'Sr', 'Sr.', or 'S#'.
    """
    def process_table(match):
        table_html = match.group(0)

        # Check if the first <th> content (stripped of <strong>) is a numbering header
        first_th = re.search(r'<th[^>]*>(?:<strong>)?\s*(.*?)\s*(?:</strong>)?</th>', table_html)
        if not first_th:
            return table_html

        header_text = first_th.group(1).strip()
        if header_text not in ('#', 'Sr', 'Sr.', 'S#', 'S.No', 'S.No.', 'No', 'No.'):
            return table_html

        # Remove the first <th> in the header row
        table_html = re.sub(
            r'(<tr[^>]*>)\s*<th[^>]*>(?:<strong>)?\s*(?:#|Sr\.?|S#|S\.No\.?|No\.?)\s*(?:</strong>)?</th>',
            r'\1',
            table_html, count=1)

        # Remove the first <td> in each data row (the manual number cell)
        table_html = re.sub(
            r'(<tr[^>]*>)\s*<td[^>]*>(?:<strong>)?\s*\d+\s*(?:</strong>)?</td>',
            r'\1',
            table_html)

        return table_html

    html = re.sub(r'<table[^>]*>.*?</table>', process_table, html, flags=re.DOTALL)
    return html


def add_toc_macro(html):
    """Add a Table of Contents macro at the top of the page.

    Why: Confluence's TOC macro generates a clickable, auto-updating outline
    from headings. All SPEC pages should have one for easy navigation.
    Adds TOC for heading levels 1-3.
    """
    toc_macro = (
        '<ac:structured-macro ac:name="toc">'
        '<ac:parameter ac:name="maxLevel">3</ac:parameter>'
        '</ac:structured-macro>'
    )

    # Don't add if already present
    if 'ac:name="toc"' in html:
        return html

    # Insert TOC at the very beginning of the content
    return toc_macro + html


def format_versioning_table(html):
    """Apply Confluence-native formatting to the Versioning table.

    Adds:
    1. Grey italic subtext below the 'Versioning' heading (matching the 10x SPEC template)
    2. Dark grey background (data-highlight-colour="#b3bac5") on header cells

    Why: The 10x SPEC template has a standard versioning section with styled headers
    and descriptive subtext. Pandoc can't produce these Confluence-specific styles.
    """
    # 1. Add versioning subtext after the Versioning heading (if not already present)
    versioning_subtext = (
        '<p><em><span style="color: rgb(151,160,175);">'
        'This section describes the version control and releases management process '
        'for the system or application being developed. This section outlines how '
        'different versions of the system will be identified, how changes will be '
        'tracked and documented, and how new versions will be released.'
        '</span></em></p>'
    )

    if 'version control and releases management' not in html:
        # Find the Versioning paragraph and add subtext after it
        # Pattern: <p><strong>Versioning</strong></p> or <p ...><strong>Versioning</strong></p>
        html = re.sub(
            r'(<p[^>]*><strong>Versioning</strong></p>)',
            r'\1' + versioning_subtext,
            html
        )

    # 2. Add grey background to Versioning table header cells
    versioning_pos = html.find('<strong>Versioning</strong>')
    if versioning_pos == -1:
        return html

    table_start = html.find('<table', versioning_pos)
    if table_start == -1:
        return html
    table_end = html.find('</table>', table_start)
    if table_end == -1:
        return html
    table_end += len('</table>')

    table_html = html[table_start:table_end]

    # Add data-highlight-colour to <th> cells (skip numberingColumn and <thead>)
    table_html = re.sub(
        r'<th(?!ead)(?!\s+class="numberingColumn")([^>]*)(?<!data-highlight-colour="#b3bac5")>',
        r'<th data-highlight-colour="#b3bac5"\1>',
        table_html
    )

    html = html[:table_start] + table_html + html[table_end:]
    return html


def strip_h1_and_source(html):
    """Remove the first H1 heading and the Source callout from HTML.

    Why: Confluence already shows the page title — having it in the body creates
    a duplicate. The 'Source: Confluence' callout is only useful in the local .md
    file, not when viewing the page on Confluence itself.
    """
    # Remove first H1 tag (the page title duplicated in body)
    html = re.sub(r'<h1[^>]*>.*?</h1>\s*', '', html, count=1)

    # Remove the Source callout (info panel or blockquote containing "Source:")
    # Pattern 1: Confluence info panel with Source link
    html = re.sub(
        r'<ac:structured-macro ac:name="info"[^>]*>\s*<ac:rich-text-body>\s*<p>\s*Source:.*?</p>\s*</ac:rich-text-body>\s*</ac:structured-macro>\s*',
        '', html, flags=re.DOTALL)
    # Pattern 2: blockquote with Source link (before pandoc converts to panel)
    html = re.sub(
        r'<blockquote>\s*<p>\s*Source:.*?</p>\s*</blockquote>\s*',
        '', html, flags=re.DOTALL)

    # Remove leading <hr> tags that were separators after the removed header
    html = re.sub(r'^(\s*<hr\s*/?>\s*)+', '', html)

    return html


def make_tables_wide(html):
    """Add data-layout='wide' and data-table-width='1800' to all tables.
    This makes tables span the full page width in Confluence Cloud wide mode,
    matching the pattern used by landing plan pages."""
    html = re.sub(
        r'<table(?![^>]*data-layout)([^>]*)>',
        r'<table data-table-width="1800" data-layout="wide"\1>',
        html
    )
    return html


def add_numbering_columns(html):
    """Add Confluence auto-numbering columns to all tables.

    Why: Confluence has a built-in row numbering feature that adds a '#' column.
    This is done by adding a <th class="numberingColumn"></th> to the header row
    and <td class="numberingColumn">N</td> to each data row.
    """
    def process_table(match):
        table_html = match.group(0)

        # Add numberingColumn header to the header row
        table_html = re.sub(
            r'(<tr[^>]*>)\s*(<th)',
            r'\1<th class="numberingColumn"></th>\2',
            table_html, count=1)

        # Add numberingColumn cells to each data row
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
    """Wrap <th> text content in <strong> tags so header rows render bold.

    Why: Pandoc does NOT bold table headers by default. Confluence renders <th>
    with slightly different styling, but bold makes headers visually distinct.
    Only wraps plain text content — skips already-bold, empty, and numberingColumn headers.
    """
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
    """Replace pandoc's equal-percentage colgroup with proportional pixel widths.

    Why: Pandoc generates equal-width columns (e.g., 7 cols = 14% each), making all
    columns the same width regardless of content. A 'Type' column (3-5 chars) gets the
    same space as 'Rationale' (100+ chars). Confluence uses pixel-based <col style="width: Npx;">
    inside <colgroup> for proper proportional column sizing.

    Heuristic: Assign widths based on header text length and known content patterns.
    Wide columns: Rationale, Summary, Description, Reason, Theme, Meaning, Key Tickets, Focus Area
    Narrow columns: #, Type, Count, Direction, Priority (headers < 10 chars)
    """
    # Known wide-content column names (need more space)
    WIDE_COLS = {'rationale', 'summary', 'description', 'reason', 'theme', 'meaning',
                 'key tickets', 'focus area', 'details', 'notes', 'comment', 'context',
                 'acceptance criteria', 'steps to reproduce', 'expected behaviour'}
    # Known narrow-content column names
    NARROW_COLS = {'#', 'type', 'count', 'direction', 'p', 'status', 'sr', 'sr.'}

    def process_table(match):
        table_html = match.group(0)

        # Extract header texts (skip numberingColumn which is self-closing or empty)
        headers = re.findall(r'<th(?:(?!numberingColumn)[^>])*>(?:<strong>)?(.*?)(?:</strong>)?</th>',
                             table_html, re.DOTALL)
        header_texts = [re.sub(r'<[^>]+>', '', h).strip() for h in headers if h.strip()]

        if not header_texts:
            return table_html

        # Check if table has numberingColumn
        has_numbering = 'numberingColumn' in table_html

        # Calculate proportional widths
        total_width = 1800  # match data-table-width
        numbering_width = 40 if has_numbering else 0
        available = total_width - numbering_width

        # Assign weight to each column based on header name
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

        # Build new colgroup
        cols = ['<col />'] if has_numbering else []
        for w in widths:
            cols.append(f'<col style="width: {w}.0px;" />')
        new_colgroup = f'<colgroup>{"".join(cols)}</colgroup>'

        # Replace existing colgroup or insert after <table> tag
        existing_cg = re.search(r'<colgroup>.*?</colgroup>', table_html, re.DOTALL)
        if existing_cg:
            table_html = table_html.replace(existing_cg.group(0), new_colgroup)
        else:
            table_html = re.sub(r'(<table[^>]*>)', r'\1' + new_colgroup, table_html)

        return table_html

    html = re.sub(r'<table[^>]*>.*?</table>', process_table, html, flags=re.DOTALL)
    return html


def set_wide_mode(page_id):
    """Set the Confluence page to full-width (wide) mode.
    Sets both draft and published appearance properties.
    Value must be a plain string "full-width", NOT an object."""
    headers = {
        'Authorization': get_auth_header(),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    for prop_key in ['content-appearance-draft', 'content-appearance-published']:
        # Check if property exists
        conn = http.client.HTTPSConnection(get_host())
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

        conn2 = http.client.HTTPSConnection(get_host())
        conn2.request(method, url, body=body, headers=headers)
        resp2 = conn2.getresponse()
        resp2.read()
        conn2.close()

    print("  Wide mode: enabled (full-width)")


def process_single_file(md_path, image_dir=None):
    """Read a markdown file and prepare HTML + image data for Confluence.
    Returns (html, image_map, image_files, md_content)."""
    md_content = md_path.read_text()
    md_dir = md_path.parent

    # Extract image references
    image_refs = extract_image_refs(md_content)
    print(f"  Images found in markdown: {len(image_refs)}")

    # Build image map: markdown path -> attachment filename
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

    # Convert markdown to HTML and transform for Confluence
    html = convert_md_to_html(md_path)
    html = transform_html_for_confluence(html, image_map)
    html = strip_h1_and_source(html)
    html = add_toc_macro(html)
    html = convert_at_mentions(html)
    html = resolve_local_spec_paths(html)
    html = make_tables_wide(html)
    html = strip_manual_number_column(html)
    html = add_numbering_columns(html)
    html = bold_header_cells(html)
    html = fix_column_widths(html)
    html = format_versioning_table(html)
    html = convert_versioning_dates(html)
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


def post_process_page(page_id):
    """Post-push processing: convert plain team names to @mentions and D-NNN-XXX to hyperlinks.

    Why: Pandoc cannot produce Confluence @mention macros or decision cross-reference links.
    The script's pre-push pipeline handles @Name patterns but NOT plain "Full Name" text.
    This step runs AFTER the page is created/updated and does a fetch → replace → PUT cycle.

    Handles:
    1. Plain team member names → <ac:link><ri:user> macros (loaded from .local/team/users.md)
    2. D-NNN-XXX decision references → <a href="..."> links (resolved from epic-to-spec-map.yaml)
    """
    # Fetch current page content + version
    conn = http.client.HTTPSConnection(get_host())
    conn.request('GET', f'/wiki/rest/api/content/{page_id}?expand=body.storage,version',
                 headers={'Authorization': get_auth_header(), 'Accept': 'application/json'})
    resp = conn.getresponse()
    if resp.status != 200:
        resp.read()
        conn.close()
        return
    data = json.loads(resp.read())
    conn.close()

    html = data['body']['storage']['value']
    version = data['version']['number']
    title = data['title']
    original_html = html

    # --- Step 1: Plain names → @mentions ---
    users = load_users_map()
    if users:
        # Sort by name length descending to match longer names first
        for name in sorted(users.keys(), key=len, reverse=True):
            account_id = users[name]
            mention_macro = f'<ac:link><ri:user ri:account-id="{account_id}" /></ac:link>'
            # Only replace plain text names — skip if already inside an ac:link or ri:user tag
            # Simple approach: replace all, then the already-converted ones will have nested macros
            # which we avoid by checking if the name appears outside of ac:link tags
            if name in html and f'ri:account-id="{account_id}"' not in html:
                html = html.replace(name, mention_macro)
            elif name in html:
                # Account ID already present — but name might appear in other places (e.g., headings, body text)
                # Replace only occurrences NOT already inside <ac:link> blocks
                # Split by the mention macro and only replace in non-macro segments
                parts = html.split(mention_macro)
                parts = [p.replace(name, mention_macro) if name in p else p for p in parts]
                html = mention_macro.join(parts)

    # --- Step 2: D-NNN-XXX → hyperlinks ---
    # Find all D-NNN-XXX patterns in the HTML
    decision_refs = set(re.findall(r'D-\d{3}-\d{3}', html))

    if decision_refs:
        # Build spec-number → Confluence page URL mapping
        decisions_pages = _load_decisions_page_map()
        for ref in decision_refs:
            spec_num = ref.split('-')[1]  # e.g., '007' from 'D-007-002'
            if spec_num not in decisions_pages:
                continue
            url = decisions_pages[spec_num]
            link = f'<a href="{url}">{ref}</a>'
            # Skip if already linked (contains the ref inside an <a> tag)
            if f'>{ref}</a>' in html:
                continue
            # Replace plain text occurrences in common positions
            html = html.replace(f'>{ref}<', f'><a href="{url}">{ref}</a><')
            html = html.replace(f'>{ref}.<', f'><a href="{url}">{ref}</a>.<')
            html = html.replace(f'>{ref})</', f'><a href="{url}">{ref}</a>)<')
            html = html.replace(f' {ref}.', f' <a href="{url}">{ref}</a>.')
            html = html.replace(f' {ref})', f' <a href="{url}">{ref}</a>)')
            html = html.replace(f'({ref}', f'(<a href="{url}">{ref}</a>')

    # Only push if something changed
    if html == original_html:
        return

    # PUT updated content
    conn = http.client.HTTPSConnection(get_host())
    payload = json.dumps({
        'version': {'number': version + 1},
        'title': title,
        'type': 'page',
        'body': {'storage': {'value': html, 'representation': 'storage'}}
    })
    conn.request('PUT', f'/wiki/rest/api/content/{page_id}', body=payload,
                 headers={'Authorization': get_auth_header(), 'Content-Type': 'application/json'})
    resp = conn.getresponse()
    resp_body = resp.read().decode()
    conn.close()

    if resp.status == 200:
        changes = []
        if users:
            changes.append('@mentions')
        if decision_refs:
            changes.append('decision cross-refs')
        print(f"  Post-process: {', '.join(changes)} applied (v{version+1})")
    else:
        print(f"  Post-process: ERROR {resp.status}")


def _load_decisions_page_map():
    """Load a mapping of spec number → Confluence decisions page URL.

    Reads from epic-to-spec-map.yaml (looks for decisions_confluence_url field)
    and falls back to scanning decisions.md files for Confluence (decisions) URLs.
    Returns dict like {'007': 'https://...', '011': 'https://...'}
    """
    mapping = {}

    # Strategy: scan all decisions.md files for their Confluence (decisions) URLs
    base = Path.cwd() / '01-product-spec-zone' / 'outputs' / '05-product-features'
    if not base.exists():
        # Try parent directories
        for parent in [Path.cwd()] + list(Path.cwd().parents):
            candidate = parent / '01-product-spec-zone' / 'outputs' / '05-product-features'
            if candidate.exists():
                base = candidate
                break

    if base.exists():
        for decisions_file in base.glob('*/decisions.md'):
            folder_name = decisions_file.parent.name
            # Extract spec number from folder name (e.g., '007' from '007-sync-dashboard')
            spec_match = re.match(r'^(\d{3})-', folder_name)
            if not spec_match:
                continue
            spec_num = spec_match.group(1)

            # Read the file and extract the Confluence (decisions) URL
            with open(decisions_file) as f:
                for line in f:
                    if 'Confluence (decisions):' in line:
                        url_match = re.search(r'\((https://[^)]+)\)', line)
                        if url_match:
                            mapping[spec_num] = url_match.group(1)
                        break

    return mapping


def save_snapshot(page_id, md_path):
    """Save a copy of the just-pushed .md as the new baseline for preflight checks.

    Why: The confluence-preflight.py script diffs local vs this snapshot vs
    Confluence to detect whether anyone edited the page on Confluence since the
    last sync. Without a snapshot, it can only do a 2-way diff and cannot
    distinguish "your changes" from "their changes".

    Auto-creates .local/confluence-snapshots/ if missing.
    """
    current = Path(md_path).resolve()
    if current.is_file():
        current = current.parent
    project_root = None
    for _ in range(10):
        if (current / '.env').exists() or (current / '.git').exists():
            project_root = current
            break
        if current.parent == current:
            break
        current = current.parent
    if not project_root:
        project_root = Path.cwd()

    snap_dir = project_root / '.local' / 'confluence-snapshots'
    snap_dir.mkdir(parents=True, exist_ok=True)
    snap_path = snap_dir / f'{page_id}.md'
    snap_path.write_text(Path(md_path).read_text())
    print(f"  Snapshot saved: {snap_path.relative_to(project_root)}")


def verify_push(page_id):
    """Fetch the pushed page from Confluence and run 9 quality checks.

    Why: The md-to-confluence pipeline applies many transformations (TOC, mentions,
    date macros, versioning formatting, wide tables, numbering columns, H1 stripping).
    This verifies all transformations landed correctly on the live page.

    Returns (passed_count, total_count).
    """
    conn = http.client.HTTPSConnection(get_host())
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
    has_versioning = 'Versioning' in html

    checks = [
        ('No duplicate H1',       '<h1' not in html),
        ('Numbering columns',     'numberingColumn' in html if has_tables else True),
        ('Wide tables',           'data-table-width' in html if has_tables else True),
        ('No plain @mentions',    'class="citation"' not in html),
        ('TOC macro',             'ac:name="toc"' in html),
        ('Versioning subtext',    'version control and releases management' in html
                                  if has_versioning else True),
        ('Grey header bg',        'data-highlight-colour' in html
                                  if has_versioning else True),
        ('Date macros',           '<time datetime' in html
                                  if (has_versioning or re.search(r'\b\d{2}-\d{2}-\d{4}\b', html)) else True),
        ('No source callout',     'Source:' not in html or 'Confluence' not in html),
        ('No broken images',     'UNKNOWN_ATTACHMENT' not in html),
    ]

    passed = sum(1 for _, ok in checks if ok)
    total = len(checks)

    print(f"\n  Verify: {passed}/{total} checks passed")
    for name, ok in checks:
        if not ok:
            print(f"    \033[91mFAIL\033[0m: {name}")

    if passed == total:
        print("    \033[92mAll checks passed!\033[0m")

    return passed, total


def main():
    parser = argparse.ArgumentParser(
        description='Push markdown to Confluence - update existing pages or create new ones',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Mode: create or update
    parser.add_argument('--create', action='store_true',
                        help='Create new page(s) under a parent instead of updating an existing page')
    parser.add_argument('--parent-id',
                        help='Parent page ID (required with --create)')
    parser.add_argument('--space',
                        help='Confluence space key (required with --create)')

    # Positional args: page_id (for update) or markdown files
    parser.add_argument('args', nargs='+',
                        help='For update mode: <page_id> <markdown_file>. For create mode: <markdown_file> [<markdown_file> ...]')

    # Common options
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

        # Get space ID
        print(f"Getting space ID for {parsed.space}...")
        space_id = get_space_id(parsed.space)
        print(f"Space ID: {space_id}")
        base_url = get_base_url()

        results = []
        for md_path in md_files:
            print(f"\nProcessing: {md_path}")

            html, image_map, image_files, md_content = process_single_file(md_path, parsed.image_dir)

            # Determine title: --title flag (only for single file), or extract from H1
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

            # Create the page
            page_id, web_url = create_page(space_id, parsed.parent_id, title, html)
            if page_id:
                full_url = f"{base_url}/wiki{web_url}" if web_url else f"{base_url}/wiki/spaces/{parsed.space}/pages/{page_id}"
                print(f"  Created! Page ID: {page_id}")
                print(f"  URL: {full_url}")

                # Upload attachments if any, then re-push HTML so image
                # references point to already-uploaded files (Confluence
                # can replace filenames with UNKNOWN_ATTACHMENT if the
                # page is created before the attachments exist).
                if image_files:
                    handle_attachments(page_id, image_files)

                    # Re-push HTML body so image refs resolve correctly
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
                    conn_rp = http.client.HTTPSConnection(get_host())
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

                # Set wide mode if requested
                if parsed.wide:
                    set_wide_mode(page_id)

                # Post-process: convert plain names to @mentions and D-NNN-XXX to hyperlinks
                post_process_page(page_id)

                # Verify the push
                verify_push(page_id)

                # Save snapshot as baseline for future preflight checks
                save_snapshot(page_id, md_path)

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

        # Get page info
        page_info = get_page_info(page_id)
        print(f"  Page: '{page_info['title']}', version: {page_info['version']}")

        # Handle attachments
        missing = handle_attachments(page_id, image_files, parsed.dry_run)

        if parsed.dry_run:
            print("\n[DRY RUN] Would perform:")
            print(f"  - Upload {len(missing)} attachments")
            print(f"  - Update page to version {page_info['version'] + 1}")
            if parsed.title:
                print(f"  - Change title to: {parsed.title}")
            return

        # Update page
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

        conn = http.client.HTTPSConnection(get_host())
        headers = {
            'Authorization': get_auth_header(),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        conn.request('PUT', f'/wiki/api/v2/pages/{page_id}', body=json.dumps(update_body), headers=headers)
        resp = conn.getresponse()
        resp_body = resp.read().decode()
        conn.close()

        if resp.status == 200:
            result = json.loads(resp_body)
            new_version = result['version']['number']
            print(f"\nSUCCESS - Page updated to version {new_version}")
            print(f"URL: {get_base_url()}/wiki/spaces/{result.get('spaceId', '...')}/pages/{page_id}")

            # Set wide mode if requested
            if parsed.wide:
                set_wide_mode(page_id)

            # Post-process: convert plain names to @mentions and D-NNN-XXX to hyperlinks
            post_process_page(page_id)

            # Verify the push
            verify_push(page_id)

            # Save snapshot as baseline for future preflight checks
            save_snapshot(page_id, md_path)
        else:
            print(f"\nERROR {resp.status}: {resp_body[:500]}")
            sys.exit(1)


if __name__ == '__main__':
    main()
