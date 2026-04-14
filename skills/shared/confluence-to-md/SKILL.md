---
name: confluence-to-md
description: |
  Convert Confluence pages to clean GitHub-Flavored Markdown files. Use this skill whenever the user
  wants to pull a Confluence page into the local repo, convert Confluence content to markdown, download
  a spec from Confluence, or batch-convert multiple pages. Also triggers on Confluence URLs, page IDs,
  or phrases like "pull this page", "download this spec", "confluence to md". Use this even if the user
  just pastes a Confluence URL and says something vague like "get this" or "convert this".
created_by: Aman Parmar
last_modified: 14-04-2026
---

# Confluence to Markdown

Pull Confluence pages into the local repo as clean markdown. The bundled script handles all the messy
Confluence storage format edge cases (user mentions, complex tables, images, status badges) so you
don't have to. Zero LLM tokens spent on the actual conversion.

## Quick start

```bash
# Single page
python3 .claude/skills/confluence-to-md/scripts/confluence-to-md.py <page_id> <output_path>

# Batch (write a Python loop - don't run CLI commands one by one)
python3 .claude/skills/confluence-to-md/scripts/batch-convert.py
```

The script auto-loads credentials from `.env` at the project root.

## Workflow

### Step 1: Get the page ID

Extract from the Confluence URL - it's the number in the path:
```
https://[your-instance].atlassian.net/wiki/spaces/[SPACE]/pages/123456789/Page+Title
                                                              ^^^^^^^^^ this
```

If the user gives a title instead of URL, search via API:
```bash
curl -s -u "$CONFLUENCE_EMAIL:$CONFLUENCE_TOKEN" \
  "https://$CONFLUENCE_BASE_URL/wiki/rest/api/content?spaceKey=[SPACE_KEY]&title=$(python3 -c 'import urllib.parse; print(urllib.parse.quote("Page Title"))')"
```

### Step 2: Pick the output path

Follow your project's naming conventions. General guidelines:
- Use descriptive, kebab-case folder and file names
- Strip redundant prefixes from Confluence titles (e.g., "SPEC |", "PRD |")
- Use the feature/product concept name, not the full page description

### Step 3: Run the script

```bash
python3 .claude/skills/confluence-to-md/scripts/confluence-to-md.py 123456789 docs/feature-name/feature-name.md
```

### Step 4: Post-conversion check

1. Scan for raw HTML `<a>` tags with `data-*` attributes (embedded media) - replace with markdown links
2. Verify image references work (script downloads to `images/` subfolder automatically)
3. Check for excessive blank lines or formatting artifacts

## Batch conversion

Write a Python driver script for multiple pages:
```python
import subprocess
pages = {
    "123456789": "docs/feature-a/feature-a.md",
    "234567890": "docs/feature-b/feature-b.md",
}
for page_id, output_path in pages.items():
    subprocess.run(["python3", ".claude/skills/confluence-to-md/scripts/confluence-to-md.py", page_id, output_path], check=True)
```

## Index files (zero LLM tokens)

For overview pages, don't convert - parse programmatically:
1. Fetch page HTML via REST API (`body.storage`)
2. Parse `<ac:link>` tags with regex
3. Resolve titles to URLs via API
4. Write structured markdown

## What the script handles

The script automatically resolves these Confluence storage format quirks:
- `<time datetime="..."/>` self-closing tags
- `<ri:user>` mentions (resolves display names via API, cached)
- Bare `<ac:link>` without URLs (resolves from `body.view`)
- Complex tables with `numberingColumn`, `colgroup`, highlights
- Lists inside table cells (flattened to inline)
- Status macros -> `[Yes]`/`[No]` text
- Single-cell layout tables (unwrapped)
- `<ac:image>` attachments (downloaded to `images/`, handles CDN 302 redirects)

If something looks wrong in the output, read `references/storage-format-gotchas.md` for the full
list of 13 known issues and their fixes.

## Post-conversion evals

After conversion, automatically verify:
1. **No raw `<ac:` tags** — grep output for `<ac:` to catch unconverted Confluence macros
2. **No broken image refs** — if `images/` folder exists, verify every `![](images/...)` ref has a matching file
3. **Source header present** — first non-blank line after `# Title` should be `> Source: [Confluence](...)`
4. **No excessive blank lines** — no more than 2 consecutive blank lines anywhere in the file

## Anti-patterns

- Running CLI commands one-by-one for batch conversion (write a Python loop instead)
- Sending full page content through an LLM for conversion (use REST API + pandoc — zero LLM tokens)
- Using symlinks for skill scripts (break when target moves) — always copy actual Python files
- Not caching user lookups (each `ri:user` triggers an API call without caching)
- Converting index/overview pages through the full pipeline (parse HTML programmatically instead)

## Quality checklist

- [ ] Output contains no raw `<ac:` tags
- [ ] All image files downloaded to `images/` subfolder
- [ ] Source header links back to original Confluence page
- [ ] No more than 2 consecutive blank lines
- [ ] Tables render correctly in GitHub-Flavored Markdown
- [ ] User mentions resolved to display names (not account IDs)

## Dependencies

- Python 3 (standard library only)
- Pandoc (`brew install pandoc`)
- `.env` with: `CONFLUENCE_EMAIL`, `CONFLUENCE_TOKEN`, `CONFLUENCE_BASE_URL`
