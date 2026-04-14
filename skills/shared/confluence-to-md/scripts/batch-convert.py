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
   - Strips common prefixes (configurable in TITLE_PREFIXES)
   - Converts to lowercase kebab-case
   - NOTE: Review and rename folders after conversion — auto-generated names
     are a starting point

4. Creates a numbered folder for each page (e.g., 003-feature-name/)
   and plans the output file path (e.g., 003-feature-name/feature-name.md)
   - Numbering starts from START_NUM (set below) to continue after existing folders

5. Shows the planned folder structure before starting conversion

6. Converts each page using the single-page converter script (confluence-to-md.py)

7. Tracks which pages succeeded and which failed, and prints a summary

How to use:
-----------
1. Update the PAGE_IDS list below with the Confluence page IDs you want to convert
   (the page ID is the number at the end of a Confluence page URL)

2. Update OUTPUT_BASE if your output folder is different

3. Update START_NUM to the next number after your last existing folder

4. Optionally update TITLE_PREFIXES with prefixes to strip from page titles

5. Run: python3 batch-convert.py

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
HOST = BASE_URL.replace("https://", "")
AUTH = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()

# --- CONFIGURATION: Edit these for your project ---

# Prefixes to strip from Confluence page titles when generating folder names.
# Add your project-specific prefixes here.
TITLE_PREFIXES = [
    # "ProjectName | Spec | ",
    # "ProjectName | ",
    # "SPEC | ",
]

# Page IDs to convert — replace with your actual page IDs
PAGE_IDS = [
    # "123456789",
    # "234567890",
]

# Base output directory for converted files
OUTPUT_BASE = "docs"

# Starting number for folder numbering (continue after existing folders)
START_NUM = 1

# --- END CONFIGURATION ---


def api_get(path):
    ctx = ssl.create_default_context()
    conn = http.client.HTTPSConnection(HOST, context=ctx)
    conn.request("GET", path, headers={"Authorization": f"Basic {AUTH}", "Accept": "application/json"})
    resp = conn.getresponse()
    data = json.loads(resp.read().decode())
    conn.close()
    return data


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


if not PAGE_IDS:
    print("No page IDs configured. Edit the PAGE_IDS list in this script.")
    sys.exit(0)

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
