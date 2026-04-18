#!/usr/bin/env python3
"""
Batch Confluence to Markdown Converter
=======================================

What this script does (step by step):
-------------------------------------
1. Reads Confluence credentials from the .env file automatically
   (same as the single-page converter — no manual setup needed)

2. Takes a list of Confluence page IDs (defined in the PAGE_IDS list below)
   and fetches the title of each page from Confluence

3. Generates a clean folder name from each page title:
   - Strips common doc-type prefixes (configure TITLE_PREFIXES below for your project,
     e.g., "SPEC |", "PRD |") so folder names aren't redundant
   - Converts to lowercase kebab-case (e.g., "Control Panel UI Localisation"
     becomes "control-panel-ui-localisation")
   - NOTE: Review and rename folders after conversion — the auto-generated names
     are a starting point and may not match your feature/product naming.

4. Creates a numbered folder for each page (e.g., 003-language-adaptive-logic/)
   and plans the output file path (e.g., 003-language-adaptive-logic/language-adaptive-logic.md)
   - Numbering starts from START_NUM (set below) to continue after existing folders

5. Shows you the full planned folder structure before starting conversion
   so you can review what will be created

6. Converts each page one by one using the single-page converter script
   (confluence-to-md.py) — which handles all the Confluence formatting edge cases

7. Tracks which pages succeeded and which failed, and prints a summary at the end

How to use:
-----------
1. Update the PAGE_IDS list below with the Confluence page IDs you want to convert
   (the page ID is the number at the end of a Confluence page URL)

2. Update OUTPUT_BASE if your output folder is different

3. Update START_NUM to the next number after your last existing folder
   (e.g., if you have 001 and 002 already, set START_NUM = 3)

4. Run: python3 scripts/batch-convert.py

Prerequisites:
    - The single-page converter script (confluence-to-md.py) must be in the same folder
    - Python 3 (no extra packages needed)
    - Pandoc installed (brew install pandoc)
    - A .env file at the project root with Confluence credentials
"""
import base64
import http.client
import json
import os
import re
import ssl
import subprocess
import sys

# Auto-load .env
def load_env():
    for base in [os.getcwd(), os.path.dirname(os.path.dirname(os.path.abspath(__file__)))]:
        env_path = os.path.join(base, '.env')
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        k, _, v = line.partition('=')
                        if k.strip() not in os.environ:
                            os.environ[k.strip()] = v.strip()
            return

load_env()

EMAIL = os.environ.get("CONFLUENCE_EMAIL")
TOKEN = os.environ.get("CONFLUENCE_TOKEN")
BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "")
if not BASE_URL:
    print("ERROR: CONFLUENCE_BASE_URL not set in .env or environment")
    sys.exit(1)
HOST = BASE_URL.replace("https://", "").replace("http://", "").rstrip('/')
AUTH = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()

def api_get(path):
    ctx = ssl.create_default_context()
    conn = http.client.HTTPSConnection(HOST, context=ctx)
    conn.request("GET", path, headers={"Authorization": f"Basic {AUTH}", "Accept": "application/json"})
    resp = conn.getresponse()
    data = json.loads(resp.read().decode())
    conn.close()
    return data

TITLE_PREFIXES = [
    # Add doc-type prefixes to strip from page titles, e.g., "SPEC | ", "PRD | "
    "SPEC ", "PRD ", "DOC | ", "SPEC | ", "PRD | ",
]


def slugify(title):
    """Convert title to kebab-case slug."""
    s = title
    for prefix in TITLE_PREFIXES:
        if s.startswith(prefix):
            s = s[len(prefix):]
            break
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s

# Page IDs to convert. Replace with your own Confluence page IDs
# (the number at the end of a Confluence page URL).
PAGE_IDS = [
    # "1234567890",
    # "9876543210",
]

OUTPUT_BASE = "outputs"  # Base folder for converted markdown files
START_NUM = 1  # Starting number for folder prefix (e.g., 001-, 002-, ...)

print(f"Fetching titles for {len(PAGE_IDS)} pages...\n")

pages = []
for pid in PAGE_IDS:
    data = api_get(f"/wiki/rest/api/content/{pid}?expand=version")
    title = data["title"]
    slug = slugify(title)
    pages.append({"id": pid, "title": title, "slug": slug})
    print(f"  {pid}: {title} -> {slug}")

print(f"\n{'='*60}")
print("Planned folder structure:")
print(f"{'='*60}\n")

conversions = []
for i, p in enumerate(pages):
    num = f"{START_NUM + i:03d}"
    folder = f"{num}-{p['slug']}"
    filename = f"{p['slug']}.md"
    output_path = f"{OUTPUT_BASE}/{folder}/{filename}"
    conversions.append({"id": p["id"], "title": p["title"], "output": output_path, "folder": folder})
    print(f"  {folder}/{filename}")

print(f"\n{'='*60}")
print(f"Starting conversion of {len(conversions)} pages...")
print(f"{'='*60}\n")

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "confluence-to-md.py")

succeeded = []
failed = []

for c in conversions:
    print(f"\n>>> Converting: {c['title']}")
    print(f"    Output: {c['output']}")
    result = subprocess.run(
        [sys.executable, script_path, c["id"], c["output"]],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        succeeded.append(c)
        print(f"    OK")
    else:
        failed.append({"conv": c, "error": result.stderr or result.stdout})
        print(f"    FAILED: {result.stderr[:200] if result.stderr else result.stdout[:200]}")

print(f"\n{'='*60}")
print(f"RESULTS: {len(succeeded)} succeeded, {len(failed)} failed out of {len(conversions)}")
print(f"{'='*60}")

if failed:
    print("\nFailed pages:")
    for f in failed:
        print(f"  - {f['conv']['title']} (ID: {f['conv']['id']})")
        print(f"    Error: {f['error'][:300]}")
