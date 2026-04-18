# Confluence Storage Format Guide for Pushing Markdown

Read this reference when building or debugging Confluence page content pushed from markdown.

## Table of Contents
1. Pandoc line wrapping
2. Markdown paragraph spacing
3. Image format
4. Callout panels (info/note/warning)
5. Code blocks
6. Wide tables
7. Wide mode property
8. Figure/figcaption stripping
9. Attachment upload
10. Page creation (v2 API)
11. Deep links to sections
12. Complex page elements (programmatic HTML)
13. H1 stripping (duplicate heading prevention)
14. Source callout stripping
15. Numbering columns (auto-row-numbers)
16. @mentions limitation and workaround
17. Overwriting manual Confluence edits

---

## 1. Pandoc line wrapping (critical)
Pandoc defaults to wrapping output at ~72 characters. Confluence interprets those newlines as actual line breaks - headings split across lines, paragraphs break mid-sentence.
**Fix**: Always use `pandoc --wrap=none` when converting markdown to HTML for Confluence.

## 2. Markdown paragraph spacing (critical for FAQ/list formatting)
Pandoc treats a single newline as a space within the same paragraph. Two consecutive lines like:
```
**Q: "Question?"**
A: Answer here.
```
will render as **one line** on Confluence: `Q: "Question?" A: Answer here.`

Similarly, intro text immediately followed by a numbered list (no blank line) merges into one paragraph:
```
Note down:
1. Item one
2. Item two
```
renders as: `Note down: 1. Item one 2. Item two`

**Fix**: Always insert a **blank line** between elements that should be separate paragraphs:
```
**Q: "Question?"**

A: Answer here.
```
This applies to: Q&A pairs, intro text before lists, any two blocks that should be visually separate.

## 3. Image format
Raw `<img>` tags don't work in Confluence. Use the attachment macro:
```html
<ac:image ac:width="1350"><ri:attachment ri:filename="image.png" /></ac:image>
```
Missing attachments cause silently broken images - always verify attachments exist before pushing HTML.

## 4. Callout panels
Use Confluence structured macros, NOT HTML `<blockquote>`:
```html
<ac:structured-macro ac:name="info">
  <ac:rich-text-body><p>Content here</p></ac:rich-text-body>
</ac:structured-macro>
```
Types: `info` (blue), `note` (yellow), `warning` (red), `tip` (green).

## 5. Code blocks
```html
<ac:structured-macro ac:name="code">
  <ac:plain-text-body><![CDATA[code content here]]></ac:plain-text-body>
</ac:structured-macro>
```

## 6. Wide tables with header row and numbered rows
Tables need explicit attributes for full width, header row, and numbered rows:
```html
<table data-table-width="1800" data-layout="wide" data-number-column="true">
```
- `data-number-column="true"` enables the auto-numbering column (Confluence "Numbered rows" option)
- Header row uses `<th>` tags (pandoc does this automatically from markdown table headers)
- Wrap `<th>` content in `<strong>` for bold headers - Confluence doesn't bold `<th>` by default in storage format:
```html
<th><strong>Column Name</strong></th>
```
Without these, tables render at default narrow width with non-bold headers and no row numbers.

## 7. Wide mode property
Set via content properties API:
```
PUT /wiki/rest/api/content/{pageId}/property/content-appearance-published
PUT /wiki/rest/api/content/{pageId}/property/content-appearance-draft
```
- Value must be the **plain string** `"full-width"`, NOT an object `{"appearance": "full-width"}`
- Both properties (draft and published) must be set
- Paragraph text still constrains to ~740px readable width (Confluence design decision) - only tables expand with wide mode

## 8. Figure/figcaption stripping
Pandoc wraps images in `<figure>` with `<figcaption>` containing alt text. On Confluence, the figcaption renders as a visible text box below the image.
**Fix**: Strip `<figure>`, `</figure>`, and `<figcaption>...</figcaption>` during HTML transformation.

## 9. Attachment upload
```
PUT /wiki/rest/api/content/{pageId}/child/attachment
```
- Header: `X-Atlassian-Token: nocheck`
- Content-Type: `multipart/form-data`
- Returns 200 (existing) or 201 (new)

## 10. Page creation (v2 API)
```
POST /wiki/api/v2/pages
```
Requires `spaceId` (numeric, not space key), `parentId`, `body.representation: "storage"`.
Get spaceId from: `GET /wiki/api/v2/spaces?keys=[SPACE_KEY]`

Duplicate title error: Confluence rejects creating a page if another page with the same title exists in the space. Check first or handle the 400 error.

## 11. Deep links to sections
Heading IDs are UUIDs in the `id` attribute of `<h*>` tags in storage format. Link format:
```
https://[your-instance].atlassian.net/wiki/spaces/[SPACE]/pages/PAGE_ID/Title#heading-uuid
```

## 12. Complex page elements (programmatic HTML)
For pages that need features pandoc can't produce, build storage HTML directly:

**@mentions:**
```html
<ac:link><ri:user ri:account-id="6267ace0a32183006f23a09e" /></ac:link>
```

**Status badges:**
```html
<ac:structured-macro ac:name="status">
  <ac:parameter ac:name="title">Done</ac:parameter>
  <ac:parameter ac:name="colour">Green</ac:parameter>
</ac:structured-macro>
```
Colors: Grey, Blue, Green, Yellow, Red.

**Colored table cells:**
```html
<td data-highlight-colour="#f4f5f7"><p>Content</p></td>
```

**TOC macro:**
```html
<ac:structured-macro ac:name="toc">
  <ac:parameter ac:name="minLevel">1</ac:parameter>
  <ac:parameter ac:name="maxLevel">7</ac:parameter>
  <ac:parameter ac:name="outline">true</ac:parameter>
</ac:structured-macro>
```

**Wide tables with column widths:**
```html
<table data-table-width="1800" data-layout="wide">
  <colgroup>
    <col style="width: 235.0px;" />
    <col style="width: 725.0px;" />
  </colgroup>
```

## 13. H1 stripping (duplicate heading prevention)
Confluence uses the **page title** as the H1 heading. If your markdown starts with `# Title`, pandoc converts it to `<h1>Title</h1>`, which creates a duplicate heading on the rendered page.
**Fix**: The script auto-strips the first `<h1>` tag from the HTML output before pushing. If you're building HTML manually, never include an `<h1>`.
**Eval**: After pushing, fetch `body.storage` and verify no `<h1>` tag exists.

## 14. Source callout stripping
Local markdown files often start with a `> Source: [Confluence](...)` callout as a back-reference. This is meaningless on Confluence itself (it would link to the page you're already on).
**Fix**: The script auto-strips:
- `<ac:structured-macro ac:name="info">` panels containing "Source:"
- `<blockquote>` elements containing "Source:"
- Leading `<hr>` tags left behind after stripping
**Eval**: After pushing, fetch `body.storage` and verify no "Source:" text exists in the first 500 chars.

## 15. Numbering columns (auto-row-numbers)
Confluence tables support an auto-numbering column via CSS classes. The script adds these automatically:
```html
<!-- Header row: empty th with numberingColumn class -->
<tr><th class="numberingColumn"></th><th>Column 1</th>...</tr>

<!-- Data rows: td with numberingColumn class and sequential number -->
<tr><td class="numberingColumn">1</td><td>Data</td>...</tr>
<tr><td class="numberingColumn">2</td><td>Data</td>...</tr>
```
This is separate from `data-number-column="true"` on the `<table>` tag (which the script also sets). Both are needed for proper rendering.
**Eval**: After pushing, fetch `body.storage` and verify `numberingColumn` class exists in every `<table>`.

## 16. @mentions limitation and workaround
Pandoc and the md-to-confluence script **CANNOT** produce Confluence @mention macros. The `@Name` text in markdown is pushed as plain text.
**Workaround** (2-step process):
1. Push the page with the script (plain `@Name` text appears)
2. After push, use the Confluence REST API directly to find-replace plain `@Name` with the proper macro:
```html
<ac:link><ri:user ri:account-id="ACCOUNT_ID" /></ac:link>
```
Resolve account IDs from `.local/team/users.md` or via `GET /wiki/rest/api/user?accountId={id}`.

Common use case: **Sign-off tables** where team members need to be tagged/notified.

## 17. Overwriting manual Confluence edits
When pushing from local markdown, the script replaces the entire page body. If anyone has edited the Confluence page directly since the last push, their changes will be **silently overwritten**.
**Fix** (pre-push check):
1. Fetch current page version: `GET /wiki/rest/api/content/{id}?expand=version`
2. If version > what you last pushed, someone edited it
3. Fetch the latest `body.storage` and diff against your local version
4. Apply their changes to the local markdown FIRST, then push
5. For version history: `GET /wiki/rest/api/content/{id}?expand=body.storage&status=historical&version=N`
