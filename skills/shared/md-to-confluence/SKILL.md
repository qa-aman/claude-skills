---
name: md-to-confluence
description: |
  Push markdown files to Confluence - update existing pages or create new ones under a parent page.
  Use this skill whenever the user wants to publish markdown to Confluence, update a Confluence page
  from a local .md file, create new Confluence pages, or batch-create pages. Also triggers on "push
  to confluence", "update confluence page", "create confluence page", "publish to confluence",
  "sync to confluence", or any mention of uploading/pushing markdown content to Confluence. Use this
  even when the user says "put this on confluence" or "make a confluence page for this".
created_by: Aman Parmar
last_modified: 14-04-2026
---

# Markdown to Confluence

Push local markdown to Confluence - update existing pages or create new ones. The bundled script
handles pandoc conversion, image uploads, Confluence macro formatting, and wide mode. It avoids
the many pitfalls of Confluence's storage format so you don't have to build HTML manually.

## Quick start

```bash
# Update existing page
python3 .claude/skills/md-to-confluence/scripts/md-to-confluence.py <page_id> <markdown_file>

# Create new page under a parent
python3 .claude/skills/md-to-confluence/scripts/md-to-confluence.py --create --parent-id <parent_id> --space <SPACE_KEY> <markdown_file> --wide

# Batch create
python3 .claude/skills/md-to-confluence/scripts/md-to-confluence.py --create --parent-id <parent_id> --space <SPACE_KEY> file1.md file2.md --wide
```

The script auto-loads credentials from `.env` at the project root.

## Workflow

### Step 1: Determine the mode

**Update** - user has an existing page URL:
```
https://[your-instance].atlassian.net/wiki/spaces/[SPACE]/pages/1234567890/Page+Title
                                                             ^^^^^^^^^^ page ID
```

**Create** - user wants a new page. You need:
- `--parent-id` (from the parent page URL)
- `--space` key (the Confluence space key for your project)

### Step 2: Run the script

```bash
# Update with title change and wide mode
python3 .claude/skills/md-to-confluence/scripts/md-to-confluence.py 1234567890 my-doc.md --title "New Title" --wide

# Create under parent with auto-title (extracted from first H1)
python3 .claude/skills/md-to-confluence/scripts/md-to-confluence.py --create --parent-id 9876543210 --space [SPACE_KEY] guide.md --wide

# Dry run first
python3 .claude/skills/md-to-confluence/scripts/md-to-confluence.py 1234567890 my-doc.md --dry-run
```

### Step 3: Post-push verification

After every push, verify these automatically:

1. **No duplicate H1** — Confluence page title IS the H1. If the markdown starts with `# Title`, the
   script strips it. Verify: fetch `body.storage` and confirm no `<h1>` tag exists.
2. **No Source callout** — The `> Source: [Confluence](...)` line in markdown is a local-only reference.
   The script strips it. Verify: fetch `body.storage` and confirm no "Source:" info panel or blockquote.
3. **Numbering columns present** — All tables should have auto-numbering. Verify: fetch `body.storage`
   and confirm `<th class="numberingColumn">` exists in every `<table>`.
4. **Wide tables** — Verify: `data-table-width="1800"` and `data-layout="wide"` on every `<table>`.
5. **No broken images** — For pages with images, verify all `<ri:attachment ri:filename="...">` have
   matching attachments on the page.
6. **@mentions** — The script auto-converts `@Name` to `<ac:link><ri:user>` macros by looking up
   account IDs from a team directory file. Verify: no `@Name` plain text or `class="citation"` remains.
7. **TOC macro** — Auto-added at the top (H1-H3). Verify: `ac:name="toc"` present.
8. **Date macros** — DD-MM-YYYY dates become `<time datetime="YYYY-MM-DD" />` macros (styled date pill).
   Verify: `<time datetime=` in HTML.

```bash
# Quick eval: fetch page and check for common issues
python3 -c "
import http.client, json, os, base64
email = os.environ.get('CONFLUENCE_EMAIL', '')
token = os.environ.get('CONFLUENCE_TOKEN', '')
auth = base64.b64encode(f'{email}:{token}'.encode()).decode()
base_url = os.environ.get('CONFLUENCE_BASE_URL', '').replace('https://', '')
conn = http.client.HTTPSConnection(base_url)
conn.request('GET', '/wiki/rest/api/content/PAGE_ID?expand=body.storage',
             headers={'Authorization': f'Basic {auth}'})
html = json.loads(conn.getresponse().read())['body']['storage']['value']
checks = []
checks.append(('No duplicate H1', '<h1' not in html))
checks.append(('Numbering columns', 'numberingColumn' in html))
checks.append(('Wide tables', 'data-table-width' in html))
checks.append(('No plain @mentions', 'citation' not in html))
checks.append(('TOC macro', 'ac:name=\"toc\"' in html))
checks.append(('Date macros', '<time datetime' in html))
checks.append(('No broken images', 'UNKNOWN_ATTACHMENT' not in html))
for name, passed in checks:
    print(f'{\"PASS\" if passed else \"FAIL\"}: {name}')
print(f'{sum(1 for _,p in checks if p)}/{len(checks)} checks passed')
"
```

## What the script handles

- **Pandoc with `--wrap=none`** - prevents premature line breaks that Confluence renders literally
- **Images** - detects `![](path)` refs, uploads missing attachments, converts to `<ac:image>` macros at `ac:width="1350"` (fills the wide content area). After creating a page, re-pushes HTML so image refs resolve against uploaded attachments (prevents `UNKNOWN_ATTACHMENT` bug).
- **Callout panels** - blockquotes with `**bold label:**` become Confluence info/note panels
- **Code blocks** - `<pre><code>` becomes Confluence code macro with CDATA
- **Wide tables** - all tables get `data-table-width="1800" data-layout="wide"` and `data-number-column="true"` for full width with numbered rows
- **Manual `#` column stripping** - auto-strips manual `| # |`, `| Sr |`, `| S# |` first columns from tables before adding Confluence numbering (prevents duplicate row numbers). Keep `#` columns in markdown for local readability — the script handles it.
- **Numbering columns** - auto-adds Confluence numbering column (`numberingColumn` class) to all tables
- **H1 stripping** - removes the first `<h1>` from HTML output since Confluence uses the page title as H1 (avoids duplicate heading)
- **Source callout stripping** - removes `> Source: [Confluence](...)` info panels/blockquotes that are only meaningful in local markdown
- **Bold headers** - `<th>` content is wrapped in `<strong>` so header row text renders bold
- **Figure stripping** - removes pandoc's figure/figcaption wrappers that cause visible caption boxes
- **Wide mode** - `--wide` flag sets both draft and published content appearance properties
- **@mentions** - converts `@Name` to Confluence user mention macros using a team directory file lookup. Handles pandoc's citation span wrapping automatically.
- **TOC macro** - auto-adds Table of Contents (H1-H3) at the top of every page
- **Date macros** - converts ALL DD-MM-YYYY dates (anywhere on the page) to Confluence native `<time>` date pills. Keep plain dates in markdown for local readability — the script converts them on push.

## Key things to know

**Pandoc column widths are the #1 table gotcha.** Pandoc generates equal-percentage `<col>` widths
(e.g., 7 columns = 14% each). This makes ALL columns the same width regardless of content. The script
replaces pandoc's `<colgroup>` with proportional pixel-based widths using a heuristic: columns with
short header names (< 10 chars) get narrow widths; columns with known long-content names like
"Rationale", "Summary", "Description" get wide widths.

**Manual `#` columns are auto-stripped.** The script detects manual numbering columns (`| # |`,
`| Sr |`, `| S# |`, `| S.No |`) and removes them before adding Confluence's built-in
`numberingColumn`. Keep `#` columns in your markdown for local readability.

**Pandoc line wrapping is the #2 gotcha.** Without `--wrap=none`, pandoc breaks lines at ~72 chars
and Confluence renders those as actual line breaks. The script already handles this, but if you ever
call pandoc directly, always include `--wrap=none`.

**Paragraph width is a Confluence design decision.** Even in wide mode, paragraph text constrains to
~740px readable width. Only tables expand with `data-layout="wide"`. This is how Confluence works.

**Single newlines in markdown merge into one paragraph.** Pandoc treats a single newline as a space.
Always use **blank lines** between elements that should be separate paragraphs.

**Duplicate titles cause errors.** Confluence rejects creating a page if another page with the same
title exists in the space.

For the full list of Confluence storage format details, read `references/confluence-format-guide.md`.

## @mentions setup

To enable @mention conversion, create a team directory file at `.local/team/users.md` with this format:

```markdown
| Short Name | Full Name | Email | Jira Account ID | Role |
|---|---|---|---|---|
| Alice | Alice Smith | alice@company.com | 6267ace0a32183006f23a09e | Engineer |
```

The script looks up names in this file to resolve Confluence account IDs. Sort names by length
(longest first) to avoid partial matches.

## STOP: Check before full-page push (MANDATORY)

This script does a **full page replacement**. Pandoc CANNOT preserve Confluence-native macros:
- Jira smart links (`<ac:structured-macro ac:name="jira">`) become broken UUID text
- Images (`<ac:image>`) are lost
- Status badges (`<ac:structured-macro ac:name="status">`) become plain text
- Expand macros, @mentions, and other Confluence macros are destroyed

**Before pushing to ANY existing page, check:**
1. Does the page have Jira smart links, images, status badges, or macros? If YES, **do NOT use this script**
2. Instead, use surgical update tools for targeted changes

**This script is ONLY safe for:**
- Brand new pages being created for the first time (`--create`)
- Pages where the local .md is the SOLE source of truth (never edited on Confluence)

## Overwriting user's manual Confluence edits

If someone has edited the Confluence page directly, pushing from local markdown will OVERWRITE those changes. Before pushing:
1. Check the page version number via `GET /wiki/rest/api/content/{id}?expand=version`
2. If version > what you last pushed, fetch the latest `body.storage` and diff against your local
3. Apply their manual changes to the local markdown FIRST, then push

## Anti-patterns

- Pushing to a page with Jira smart links or status badges (destroys them)
- Running without `--dry-run` first on an unfamiliar page
- Not checking page version before pushing (overwrites manual edits)
- Hardcoding Confluence hostnames instead of reading from `.env`
- Using symlinks for skill scripts (break when target moves) — always copy files

## Quality checklist

- [ ] Ran `--dry-run` before actual push
- [ ] Checked page version for manual edits
- [ ] Verified no Confluence-native macros on target page
- [ ] Post-push eval: all checks passed
- [ ] Images render correctly (no UNKNOWN_ATTACHMENT)
- [ ] @mentions render as blue pills, not plain text
- [ ] TOC macro present at top of page

## Dependencies

- Python 3 (standard library only)
- Pandoc (`brew install pandoc`)
- `.env` with: `CONFLUENCE_EMAIL`, `CONFLUENCE_TOKEN`, `CONFLUENCE_BASE_URL`
