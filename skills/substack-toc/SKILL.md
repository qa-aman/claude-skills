---
name: substack-toc
description: Creates numbered table of contents for Substack articles with working internal anchor links using the /i/POST_ID/section-slug format. Use when user asks to add navigation, TOC, table of contents, anchor links, jump links, article navigation, or improve article structure. Also trigger when user has a long Substack post and wants readers to navigate between sections - even if they don't explicitly ask for a "TOC".
---

# Substack Table of Contents Generator

Generate professional, numbered table of contents for Substack newsletter articles with working internal anchor links.

## How Substack Anchor Links Work

Substack auto-generates anchor links for every heading using this format:
```
https://domain.substack.com/i/POST_ID/heading-in-kebab-case
```

Components:
- `POST_ID` = unique numerical identifier (e.g., 176830635)
- `heading-in-kebab-case` = heading text converted to lowercase with hyphens

## Required Information

Before creating a TOC, collect:
1. **Post ID** - The numerical ID from the published Substack URL
2. **Section headings** - All main headings to include in TOC
3. **Substack domain** - Full domain (e.g., username.substack.com or custom domain)

If missing, ask the user for these details.

## Workflow

### Step 1: Extract Section Headings

Identify all H2 or H3 headings from the article that should appear in the TOC.

Skip these headings:
- Intro paragraphs before the TOC
- "Table of Contents" itself
- Closing signatures

### Step 2: Convert Headings to Anchor Slugs

For each heading, create kebab-case slug:
- Convert to lowercase
- Replace spaces with hyphens
- Remove special characters except hyphens
- Remove trailing/leading hyphens

Examples:
- "Email Triage and Response" > `email-triage-and-response`
- "Run Your Own Audit" > `run-your-own-audit`
- "What These Patterns Reveal" > `what-these-patterns-reveal`

### Step 3: Build TOC

Create numbered list with full anchor URLs:

```markdown
**Table of Contents:**

1. [First Section](https://[your-domain]/i/POST_ID/first-section)
2. [Second Section](https://[your-domain]/i/POST_ID/second-section)
3. [Third Section](https://[your-domain]/i/POST_ID/third-section)
```

### Step 4: Number Section Headings

Update all section headings to match TOC numbering:

```markdown
### 1. First Section

Content here...

---

### 2. Second Section

Content here...

---

### 3. Third Section

Content here...
```

### Step 5: Format Complete Article

Structure the final output:

```markdown
[Opening paragraphs before TOC]

---

**Table of Contents:**

1. [Section One](https://[your-domain]/i/POST_ID/section-one)
2. [Section Two](https://[your-domain]/i/POST_ID/section-two)
[... all sections ...]

---

[Optional: Brief transition sentence]

*Note: [Any article-specific disclaimers]*

---

### 1. Section One

[Content]

---

### 2. Section Two

[Content]

---

[Continue for all sections...]

---

[Closing]
```

## Best Practices

**Clean separation**: Use `---` horizontal rules to separate:
- TOC from content
- Each major section

**Consistent heading level**: Use H3 (`###`) for all numbered sections

**Exact matching**: TOC link text must exactly match section heading text (except for the number prefix)

**No back-to-top links**: Avoid cluttering sections with "Back to top" links after every section

**Brief transitions**: Add one short paragraph between TOC and first section if helpful for flow

## Common Issues and Solutions

**Links don't work after publishing:**
- Verify POST_ID matches the published URL
- Check heading text in links exactly matches actual headings
- Confirm kebab-case conversion is correct (lowercase, hyphens only, no special chars)

**TOC numbers don't match section numbers:**
- Audit both TOC and section headings
- Ensure sequential numbering with no gaps

**Wrong anchors generated:**
- Remember: Substack auto-generates anchors from heading text
- Cannot use custom anchor IDs
- Heading text determines the anchor slug

## Example Transformation

**Input article:**
```markdown
Hey Reader,

Intro paragraph here.

### Email triage and response prioritization

Content...

### Client presentation assembly

Content...

### Prompt optimization

Content...
```

**Output with TOC:**
```markdown
Hey Reader,

Intro paragraph here.

---

**Table of Contents:**

1. [Email triage and response prioritization](https://[your-domain]/i/POST_ID/email-triage-and-response-prioritization)
2. [Client presentation assembly](https://[your-domain]/i/POST_ID/client-presentation-assembly)
3. [Prompt optimization](https://[your-domain]/i/POST_ID/prompt-optimization)

---

### 1. Email triage and response prioritization

Content...

---

### 2. Client presentation assembly

Content...

---

### 3. Prompt optimization

Content...
```

## Output Instructions

After generating the TOC-enhanced article:

1. Provide the complete formatted article
2. Tell the user: "Copy this article and paste it into your Substack editor. The TOC links will work once published at the URL with POST_ID [ID]."
3. If POST_ID was not provided, remind user to get it from their published post and update all links

## Limitations

This skill cannot:
- Automatically fetch POST_ID from Substack (must be provided by user)
- Create custom anchor IDs (Substack generates them automatically)
- Add styling or custom formatting beyond standard markdown
- Verify links work (links only function after publishing)
