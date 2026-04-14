# Confluence Storage Format Gotchas

Read this reference when troubleshooting conversion issues or when the script produces unexpected output.

## Table of Contents
1. Self-closing time tags
2. User mentions (no display name)
3. Bare ac:link tags (no URL)
4. Complex table markup
5. Lists inside table cells
6. Status macros
7. Pandoc placeholder escaping
8. Single-cell layout tables
9. URL encoding for title lookups
10. Base64 auth for special-char tokens
11. Image attachments and CDN redirects
12. Raw HTML a tags surviving pandoc
13. Script location and symlink prohibition

---

## 1. Self-closing `<time>` tags
```html
<time datetime="2025-01-23" />
```
Content is in the `datetime` **attribute**, not between tags. Standard regex `<time>(.*?)</time>` won't capture it.
**Fix**: `re.sub(r'<time\s+datetime="([^"]+)"\s*/>', format_date, html)`

## 2. User mentions (no display name in storage)
```html
<ac:link><ri:user ri:account-id="62e7a9c0b5b801a9afee58f6" /></ac:link>
```
Only the account-id is stored. Must call `GET /wiki/rest/api/user?accountId={id}` to get displayName. Cache user lookups to avoid repeated API calls.

## 3. Bare `<ac:link>` tags (no ri:page, no href)
```html
<ac:link><ac:link-body>v.12</ac:link-body></ac:link>
```
In storage format, there's no URL. In view format (`body.view`), Confluence renders it as `<a href="/wiki/spaces/...">v.12</a>`.
**Fix**: Fetch BOTH `body.storage` and `body.view`, match link text, extract href from view.

## 4. Complex table markup
```html
<table data-table-width="1800" data-layout="center">
  <colgroup><col /></colgroup>
  <tr><th class="numberingColumn" /><th data-highlight-colour="#b3bac5">...</th></tr>
  <td class="numberingColumn">1</td>
```
- `numberingColumn` - auto-numbering column, strip it
- `colgroup` - confuses pandoc, strip it
- `data-highlight-colour` - styling only, strip it
- **Pandoc CANNOT convert these tables** - must extract and convert manually

## 5. Lists inside table cells
```html
<td><ol start="1"><li><p>Item 1</p></li><li><p>Item 2</p></li></ol></td>
```
Markdown tables don't support multi-line content. Flatten to: `1. Item 1 2. Item 2` (inline numbered).

## 6. Status macros
```html
<ac:structured-macro ac:name="status">
  <ac:parameter ac:name="title">Yes</ac:parameter>
  <ac:parameter ac:name="colour">Green</ac:parameter>
</ac:structured-macro>
```
Extract `title` parameter, render as `[Yes]`.

## 7. Pandoc placeholder escaping
Pandoc escapes underscores: `__TABLE_1__` becomes `\_\_TABLE_1\_\_`.
**Fix**: Use alpha-only placeholders like `MDTBL1MDTBL`.

## 8. Single-cell layout tables
```html
<table><tr><td>
  <h3>Key Concepts</h3>
  <p>Content here...</p>
</td></tr></table>
```
Confluence uses 1-row, 1-col tables for visual layout/indentation. Detect by counting rows and cells; if exactly 1 row with 1 cell, unwrap the inner content and discard the table wrapper.

## 9. URL encoding for title lookups
Page titles often contain `|` (pipe), `&`, special chars. Bash `curl` mangles these even with quoting.
**Fix**: Always use Python `urllib.parse.quote()` for title encoding.

## 10. Base64 auth for tokens with special characters
API tokens contain `=`, `+`, `/` which break bash `-u user:token` flag.
**Fix**: Compute auth header in Python: `base64.b64encode(f"{email}:{token}".encode()).decode()`

## 11. Image attachments and CDN redirects
`<ac:image>` with `<ri:attachment ri:filename="...">` - embedded images in Confluence storage format.
- Script auto-downloads attachments to `images/` subfolder
- Replaces with `![](images/filename.png)`
- Confluence Cloud returns 302 redirect to `api.media.atlassian.com` CDN
- `http.client` doesn't auto-follow redirects - must manually parse Location header

## 12. Raw HTML `<a>` tags surviving pandoc
Embedded media links (e.g., YouTube `<a>` tags with `data-*` attributes) may survive pandoc as raw HTML.
**Fix**: Post-conversion cleanup to replace with proper markdown `[text](url)` links.

## 13. Script location and symlink prohibition
The conversion script lives inside the skill folder at `.claude/skills/confluence-to-md/scripts/confluence-to-md.py`.
- **NEVER use symlinks** for skill scripts — they break when the symlink target moves or is deleted. Always copy the actual Python file.
- If the project-local script is missing or broken, copy from global: `~/.claude/skills/confluence-to-md/scripts/confluence-to-md.py`
