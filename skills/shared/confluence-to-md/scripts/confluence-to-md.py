#!/usr/bin/env python3
"""
Confluence to Markdown Converter
================================

What this script does (step by step):
-------------------------------------
1. Reads your Confluence login credentials from a .env file automatically
   (no need to type them every time)

2. Connects to Confluence and downloads the page content in two formats:
   - "storage" format (the raw HTML that Confluence saves internally)
   - "view" format (the rendered HTML that you see in your browser)
   Both are needed because some information only exists in one format.

3. Fixes Confluence-specific formatting issues that would break the markdown:
   - Dates: Confluence stores dates in a special tag — this extracts the actual date
   - People's names: Confluence only stores user IDs, not names — this looks up
     each person's real name via the Confluence API
   - Broken links: Some links in Confluence have no URL in the raw format —
     this finds the real URL by checking the rendered version of the page

4. Handles tables separately (Confluence tables are too complex for standard tools):
   - Removes auto-numbering columns that Confluence adds
   - Converts lists inside table cells into a single-line format
     (markdown tables can't have multi-line content)
   - Detects "fake" tables (1 row, 1 column) that Confluence uses just for
     visual indentation — unwraps the content instead of making a table

5. Cleans up Confluence-only elements:
   - Status badges (colored labels like [Yes]/[No]) -> plain text
   - Info/warning/note panels -> blockquotes
   - Table of contents macros -> removed (not useful in markdown)
   - Colored text and background highlights -> simplified

6. Downloads any images attached to the page:
   - Detects <ac:image> tags that reference Confluence attachments
   - Downloads each image file from the Confluence API
   - Saves images to an "images/" subfolder next to the output .md file
   - Replaces the Confluence image tags with standard markdown image syntax

7. Converts the cleaned HTML to GitHub-Flavored Markdown using Pandoc

8. Puts the converted tables back into the markdown (they were set aside in step 4)

9. Adds a header with the page title and a link back to the original Confluence page

10. Saves the final .md file to the specified output path
    (creates any missing folders automatically)

Usage:
    python3 confluence-to-md.py <page_id> <output_path>

    The page_id is the number at the end of a Confluence page URL.
    Example URL: https://[your-instance].atlassian.net/wiki/spaces/[SPACE]/pages/123456789
    The page_id here is: 123456789

Examples:
    # Credentials auto-loaded from .env file in project root (recommended)
    python3 confluence-to-md.py 123456789 docs/feature-name/feature-name.md

    # Or with explicit env vars
    export CONFLUENCE_EMAIL="your-email@company.com"
    export CONFLUENCE_TOKEN="your-api-token"
    python3 confluence-to-md.py 123456789 output.md

Prerequisites:
    - Python 3 (no extra packages needed — uses only built-in libraries)
    - Pandoc installed (brew install pandoc)
    - A .env file at the project root with:
        CONFLUENCE_EMAIL=your-email@company.com
        CONFLUENCE_TOKEN=your-atlassian-api-token
        CONFLUENCE_BASE_URL=https://your-instance.atlassian.net
"""

import argparse
import base64
import http.client
import json
import os
import re
import ssl
import subprocess
import sys
import urllib.parse
from datetime import datetime


class ConfluenceToMarkdown:
    def __init__(self, email, token, base_url):
        self.email = email
        self.token = token
        self.base_url = base_url
        self.host = base_url.replace("https://", "").replace("http://", "")
        self.auth = base64.b64encode(f"{email}:{token}".encode()).decode()
        self.user_cache = {}

    def _connect(self):
        ctx = ssl.create_default_context()
        return http.client.HTTPSConnection(self.host, context=ctx)

    def _api_get(self, path):
        conn = self._connect()
        headers = {"Authorization": f"Basic {self.auth}", "Accept": "application/json"}
        conn.request("GET", path, headers=headers)
        resp = conn.getresponse()
        data = json.loads(resp.read().decode())
        conn.close()
        return data

    def fetch_page(self, page_id):
        """Fetch page with both storage and view body formats."""
        data = self._api_get(f"/wiki/rest/api/content/{page_id}?expand=body.storage,body.view,version")
        return {
            "title": data["title"],
            "storage_html": data["body"]["storage"]["value"],
            "view_html": data["body"]["view"]["value"],
            "version": data["version"]["number"],
            "url": f"{self.base_url}/wiki{data['_links']['webui']}",
        }

    def resolve_user(self, account_id):
        """Resolve Confluence user account ID to display name."""
        if account_id in self.user_cache:
            return self.user_cache[account_id]
        try:
            data = self._api_get(f"/wiki/rest/api/user?accountId={account_id}")
            name = data.get("displayName", data.get("publicName", "Unknown"))
        except Exception:
            name = "Unknown"
        self.user_cache[account_id] = name
        return name

    def fetch_attachment_urls(self, page_id):
        """Fetch attachment download URLs for a page. Returns {filename: download_path}."""
        data = self._api_get(f"/wiki/rest/api/content/{page_id}/child/attachment")
        urls = {}
        for a in data.get("results", []):
            filename = a.get("title", "")
            dl_path = a.get("_links", {}).get("download", "")
            if filename and dl_path:
                urls[filename] = f"/wiki{dl_path}"
        return urls

    def download_attachment(self, download_path, output_dir, filename):
        """Download a Confluence attachment using its full download path.
        Follows redirects (Atlassian Cloud returns 302 to media CDN)."""
        img_dir = os.path.join(output_dir, "images")
        os.makedirs(img_dir, exist_ok=True)
        filepath = os.path.join(img_dir, filename)
        conn = self._connect()
        headers = {"Authorization": f"Basic {self.auth}"}
        conn.request("GET", download_path, headers=headers)
        resp = conn.getresponse()
        # Follow redirects (302 to Atlassian media CDN)
        if resp.status in (301, 302, 303, 307):
            resp.read()  # drain
            conn.close()
            redirect_url = resp.getheader("Location")
            if redirect_url:
                parsed = urllib.parse.urlparse(redirect_url)
                ctx = ssl.create_default_context()
                conn2 = http.client.HTTPSConnection(parsed.hostname, context=ctx)
                redirect_path = parsed.path
                if parsed.query:
                    redirect_path += f"?{parsed.query}"
                conn2.request("GET", redirect_path)
                resp = conn2.getresponse()
                data = resp.read()
                conn2.close()
                if resp.status == 200:
                    with open(filepath, 'wb') as f:
                        f.write(data)
                    return True
                return False
        data = resp.read()
        conn.close()
        if resp.status == 200:
            with open(filepath, 'wb') as f:
                f.write(data)
            return True
        return False

    def process_images(self, html, page_id, output_dir):
        """Find <ac:image> tags, download attachments, replace with <img> tags."""
        attachment_urls = self.fetch_attachment_urls(page_id)
        image_count = 0
        # Match both wrapping and self-closing <ac:image> tags
        image_tags = re.findall(r'<ac:image[^>]*>.*?</ac:image>', html, re.DOTALL)
        image_tags += re.findall(r'<ac:image[^/]*/>', html)
        # Deduplicate while preserving order
        seen = set()
        unique_tags = []
        for tag in image_tags:
            if tag not in seen:
                seen.add(tag)
                unique_tags.append(tag)
        for tag in unique_tags:
            fn_match = re.search(r'ri:filename="([^"]+)"', tag)
            if not fn_match:
                continue
            filename = fn_match.group(1)
            alt_match = re.search(r'ac:alt="([^"]*)"', tag)
            alt_text = alt_match.group(1) if alt_match else filename
            caption_match = re.search(r'<ac:caption[^>]*>.*?<p[^>]*>(.*?)</p>.*?</ac:caption>', tag, re.DOTALL)
            caption_text = caption_match.group(1).strip() if caption_match else ''
            dl_path = attachment_urls.get(filename)
            if dl_path and self.download_attachment(dl_path, output_dir, filename):
                image_count += 1
                img_tag = f'<img src="images/{filename}" alt="{alt_text}" />'
                if caption_text:
                    img_tag += f'<br><em>{caption_text}</em>'
                html = html.replace(tag, img_tag)
                print(f"  Downloaded: {filename}")
            else:
                print(f"  WARNING: Failed to download {filename}")
                html = html.replace(tag, f'<!-- Image not found: {filename} -->')
        return html, image_count

    def resolve_bare_ac_links(self, storage_html, view_html):
        """
        Find ac:link tags in storage format that have no ri:page/href,
        and resolve their actual URLs from the view format.
        """
        bare_links = re.findall(
            r'<ac:link>(?:(?!ri:page).)*?<ac:link-body>(.*?)</ac:link-body>\s*</ac:link>',
            storage_html, re.DOTALL
        )
        link_map = {}
        for link_text in bare_links:
            clean_text = re.sub(r'<[^>]+>', '', link_text).strip()
            pattern = re.escape(clean_text)
            match = re.search(rf'<a\s+href="([^"]*)"[^>]*>{pattern}</a>', view_html)
            if match:
                href = match.group(1)
                if href.startswith("/"):
                    href = f"{self.base_url}{href}"
                link_map[clean_text] = href
        return link_map

    def preprocess_html(self, storage_html, view_html):
        """Pre-process Confluence storage HTML before conversion."""
        html = storage_html

        # 1. Convert <time datetime="..."/> to readable date
        def time_to_text(m):
            try:
                dt = datetime.strptime(m.group(1), "%Y-%m-%d")
                return dt.strftime("%b %d, %Y")
            except Exception:
                return m.group(1)
        html = re.sub(r'<time\s+datetime="([^"]+)"\s*/>', time_to_text, html)

        # 2. Resolve user mentions -> @DisplayName
        user_ids = set(re.findall(r'ri:account-id="([^"]+)"', html))
        for uid in user_ids:
            name = self.resolve_user(uid)
            print(f"  Resolved user: {uid} => {name}")
        def user_mention(m):
            return f'@{self.resolve_user(m.group(1))}'
        html = re.sub(
            r'<ac:link[^>]*>\s*<ri:user\s+ri:account-id="([^"]+)"[^/]*/>\s*</ac:link>',
            user_mention, html
        )

        # 3. Resolve bare ac:links (no ri:page) using view HTML
        link_map = self.resolve_bare_ac_links(storage_html, view_html)
        for text, url in link_map.items():
            pattern = rf'<ac:link>(?:(?!ri:page).)*?<ac:link-body>{re.escape(text)}</ac:link-body>\s*</ac:link>'
            replacement = f'<a href="{url}">{text}</a>'
            html = re.sub(pattern, replacement, html, flags=re.DOTALL)

        return html

    def clean_cell_text(self, text):
        """Clean HTML from a table cell to plain text."""
        # Status macros
        text = re.sub(
            r'<ac:structured-macro[^>]*ac:name="status"[^>]*>.*?<ac:parameter ac:name="title">(.*?)</ac:parameter>.*?</ac:structured-macro>',
            r'[\1]', text, flags=re.DOTALL
        )
        # ac:link with ri:page -> extract body text
        def ac_link(m):
            body = re.search(r'<ac:link-body>(.*?)</ac:link-body>', m.group(0), re.DOTALL)
            return re.sub(r'<[^>]+>', '', body.group(1)).strip() if body else ''
        text = re.sub(r'<ac:link[^>]*>.*?</ac:link>', ac_link, text, flags=re.DOTALL)
        # <a href> -> markdown link
        def a_link(m):
            href = m.group(1).replace('&amp;', '&')
            inner = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            if inner and inner != href:
                return f'[{inner}]({href})'
            return href
        text = re.sub(r'<a\s+href="([^"]*)"[^>]*>(.*?)</a>', a_link, text, flags=re.DOTALL)
        # Bold / italic
        text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
        text = re.sub(r'<em>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
        # Ordered list -> inline numbered format
        def format_ol(m):
            items = re.findall(r'<li[^>]*>(.*?)</li>', m.group(0), re.DOTALL)
            start_match = re.search(r'start="(\d+)"', m.group(0))
            start = int(start_match.group(1)) if start_match else 1
            parts = []
            for i, item in enumerate(items, start):
                clean = re.sub(r'<(?!img\s|/img|em>|/em>|br>)[^>]+>', '', item).strip()
                if clean:
                    parts.append(f'{i}. {clean}')
            return '<br>'.join(parts)
        text = re.sub(r'<ol[^>]*>.*?</ol>', format_ol, text, flags=re.DOTALL)
        # Unordered list -> inline
        def format_ul(m):
            items = re.findall(r'<li[^>]*>(.*?)</li>', m.group(0), re.DOTALL)
            parts = []
            for item in items:
                clean = re.sub(r'<(?!img\s|/img|em>|/em>|br>)[^>]+>', '', item).strip()
                if clean:
                    parts.append(f'- {clean}')
            return '<br>'.join(parts)
        text = re.sub(r'<ul[^>]*>.*?</ul>', format_ul, text, flags=re.DOTALL)
        # <img> tags -> markdown image syntax
        def img_to_md(m):
            attrs = m.group(0)
            src_match = re.search(r'src="([^"]*)"', attrs)
            alt_match = re.search(r'alt="([^"]*)"', attrs)
            src = src_match.group(1) if src_match else ''
            alt = alt_match.group(1) if alt_match else ''
            return f'![{alt}]({src})'
        text = re.sub(r'<img\s[^>]*/?>', img_to_md, text)
        # br -> <br> for markdown table cells
        text = re.sub(r'<br\s*/?>', '<br>', text)
        # Strip remaining tags (but NOT <br>)
        text = re.sub(r'<(?!br>)[^>]+>', '', text)
        # HTML entities
        for old, new in [('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&nbsp;', ' '),
                         ('&ndash;', '\u2013'), ('&mdash;', '\u2014'), ('&rsquo;', "'"), ('&lsquo;', "'"),
                         ('&ldquo;', '\u201c'), ('&rdquo;', '\u201d')]:
            text = text.replace(old, new)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def table_to_md(self, table_html):
        """Convert an HTML table to a markdown table."""
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        if not rows:
            return ''
        md_rows = []
        for row_html in rows:
            # Remove numbering column
            row_clean = re.sub(r'<th\s+class="numberingColumn"\s*/>', '', row_html)
            row_clean = re.sub(r'<td\s+class="numberingColumn"[^>]*>.*?</td>', '', row_clean, flags=re.DOTALL)
            cell_matches = re.findall(r'<(th|td)[^>]*>(.*?)</\1>', row_clean, re.DOTALL)
            cells = []
            for tag, cell_html in cell_matches:
                cell_text = self.clean_cell_text(cell_html).replace('|', '\\|')
                cells.append((cell_text, tag == 'th'))
            if cells:
                md_rows.append(cells)
        if not md_rows:
            return ''
        max_cols = max(len(r) for r in md_rows)
        lines = []
        first_row = md_rows[0]
        is_header = any(c[1] for c in first_row)
        hdr = [c[0] for c in first_row]
        while len(hdr) < max_cols:
            hdr.append('')
        lines.append('| ' + ' | '.join(hdr) + ' |')
        lines.append('|' + '|'.join(['---' for _ in range(max_cols)]) + '|')
        for row in md_rows[1:] if is_header else md_rows:
            cells = [c[0] for c in row]
            while len(cells) < max_cols:
                cells.append('')
            lines.append('| ' + ' | '.join(cells) + ' |')
        return '\n'.join(lines)

    def convert(self, page_id, output_path):
        """Main conversion: fetch page, pre-process, convert, write."""
        print(f"Fetching page {page_id}...")
        page = self.fetch_page(page_id)
        print(f"  Title: {page['title']}")
        print(f"  Version: {page['version']}")
        print(f"  URL: {page['url']}")

        print("Pre-processing HTML...")
        html = self.preprocess_html(page["storage_html"], page["view_html"])

        # Download images and replace <ac:image> tags with <img> tags
        print("Processing images...")
        output_dir = os.path.dirname(os.path.abspath(output_path))
        html, image_count = self.process_images(html, page_id, output_dir)
        print(f"  Images downloaded: {image_count}")

        # Replace tables with placeholders
        # First: unwrap single-cell layout tables (used for styling, not data)
        print("Unwrapping layout tables...")
        def unwrap_layout_table(m):
            table_html = m.group(0)
            rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
            if len(rows) == 1:
                cells = re.findall(r'<td[^>]*>(.*?)</td>', rows[0], re.DOTALL)
                if len(cells) == 1:
                    print(f"  Unwrapped single-cell layout table")
                    return cells[0]
            return m.group(0)
        html = re.sub(r'<table[^>]*>.*?</table>', unwrap_layout_table, html, flags=re.DOTALL)

        print("Converting tables...")
        table_counter = [0]
        table_map = {}
        def replace_table(m):
            table_counter[0] += 1
            key = f'MDTBL{table_counter[0]}MDTBL'
            md = self.table_to_md(m.group(0))
            table_map[key] = md
            return f'<p>{key}</p>'
        html = re.sub(r'<table[^>]*>.*?</table>', replace_table, html, flags=re.DOTALL)
        print(f"  Tables found: {table_counter[0]}")

        # Clean remaining Confluence markup
        print("Cleaning Confluence markup...")
        # Status macros
        html = re.sub(
            r'<ac:structured-macro[^>]*ac:name="status"[^>]*>.*?<ac:parameter ac:name="title">(.*?)</ac:parameter>.*?</ac:structured-macro>',
            r'<strong>[\1]</strong>', html, flags=re.DOTALL
        )
        # TOC / view-file macros
        html = re.sub(r'<ac:structured-macro[^>]*ac:name="(toc|view-file)"[^>]*>.*?</ac:structured-macro>', '', html, flags=re.DOTALL)
        # Note/info/warning panels -> blockquote
        def panel_to_bq(m):
            body = re.search(r'<ac:rich-text-body>(.*?)</ac:rich-text-body>', m.group(0), re.DOTALL)
            if body:
                return f'<blockquote><p><strong>Note:</strong> {body.group(1)}</p></blockquote>'
            return ''
        html = re.sub(
            r'<ac:structured-macro[^>]*ac:name="(note|info|warning|tip|panel)"[^>]*>.*?</ac:structured-macro>',
            panel_to_bq, html, flags=re.DOTALL
        )
        # Remaining ac:link -> extract body text
        def ac_to_a(m):
            body = re.search(r'<ac:link-body>(.*?)</ac:link-body>', m.group(0), re.DOTALL)
            return body.group(1) if body else ''
        html = re.sub(r'<ac:link[^>]*>.*?</ac:link>', ac_to_a, html, flags=re.DOTALL)
        # Inline color/bg spans
        html = re.sub(r'<span[^>]*style="color:[^"]*"[^>]*>(.*?)</span>', r'<em>\1</em>', html, flags=re.DOTALL)
        html = re.sub(r'<span[^>]*style="background-color:[^"]*"[^>]*>(.*?)</span>', r'\1', html, flags=re.DOTALL)
        # Panel divs
        html = re.sub(
            r'<div[^>]*class="panel[^"]*"[^>]*>.*?<div[^>]*class="panelContent"[^>]*>(.*?)</div>\s*</div>',
            r'<blockquote>\1</blockquote>', html, flags=re.DOTALL
        )
        # Confluence-specific attributes
        html = re.sub(
            r'\s*(data-table-width|data-layout|ac:local-id|local-id|data-card-appearance|data-highlight-colour)="[^"]*"',
            '', html
        )

        # Pandoc conversion
        print("Running pandoc...")
        tmp_file = f'/tmp/confluence-{page_id}.html'
        with open(tmp_file, 'w') as f:
            f.write(html)
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'gfm', '--wrap=none', tmp_file],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  Pandoc error: {result.stderr}")
            sys.exit(1)
        md = result.stdout

        # Replace table placeholders
        for key, table_md in table_map.items():
            md = md.replace(key, f'\n{table_md}\n')

        # Add header
        header = f"""# {page['title']}

> Source: [Confluence]({page['url']})

---

"""
        md = header + md
        md = re.sub(r'\n{4,}', '\n\n\n', md)

        # Write output
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(md)

        lines = md.split('\n')
        table_lines = sum(1 for l in lines if l.startswith('|'))
        print(f"\nDone! Written to: {output_path}")
        print(f"  Lines: {len(lines)}")
        print(f"  Table rows: {table_lines}")
        print(f"  Tables converted: {table_counter[0]}")
        print(f"  Images downloaded: {image_count}")
        print(f"  Users resolved: {len(self.user_cache)}")


def load_env_file():
    """Auto-load .env file from project root (walks up from script location)."""
    search_dirs = [os.getcwd()]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    search_dirs.append(os.path.dirname(script_dir))

    for base in search_dirs:
        env_path = os.path.join(base, '.env')
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, _, value = line.partition('=')
                        key, value = key.strip(), value.strip()
                        if key not in os.environ:
                            os.environ[key] = value
            print(f"Loaded credentials from: {env_path}")
            return
    print("No .env file found — using environment variables or CLI args")


def main():
    load_env_file()

    parser = argparse.ArgumentParser(description="Convert Confluence page to Markdown")
    parser.add_argument("page_id", help="Confluence page ID (from URL)")
    parser.add_argument("output", help="Output .md file path")
    parser.add_argument("--email", default=os.environ.get("CONFLUENCE_EMAIL"), help="Atlassian email (or set CONFLUENCE_EMAIL)")
    parser.add_argument("--token", default=os.environ.get("CONFLUENCE_TOKEN"), help="Atlassian API token (or set CONFLUENCE_TOKEN)")
    parser.add_argument("--base-url", default=os.environ.get("CONFLUENCE_BASE_URL", ""), help="Confluence base URL (or set CONFLUENCE_BASE_URL)")
    args = parser.parse_args()

    if not args.email or not args.token:
        print("Error: Email and token required.")
        print("Options: 1) Add to .env file  2) Set CONFLUENCE_EMAIL/CONFLUENCE_TOKEN env vars  3) Use --email/--token flags")
        sys.exit(1)

    if not args.base_url:
        print("Error: Base URL required. Set CONFLUENCE_BASE_URL in .env or use --base-url flag.")
        sys.exit(1)

    converter = ConfluenceToMarkdown(args.email, args.token, args.base_url)
    converter.convert(args.page_id, args.output)


if __name__ == "__main__":
    main()
