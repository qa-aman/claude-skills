---
name: figma-copy-rewriter
description: |
  Rewrite UI copy directly on Figma files to be simpler, jargon-free, and terminologically consistent.
  Trigger when: user says "rewrite copy", "simplify copy", "fix the text", "copy audit",
  "UX copy review", "clean up the wording", shares a Figma URL and mentions copy/text/wording,
  or asks to make text simpler/clearer/more consistent on a Figma file.
created_by: Aman Parmar
last_modified: 20-04-2026
---

# Figma Copy Rewriter

Rewrite interface copy on Figma screens to be simple, jargon-free, and terminologically consistent. Works on any Figma file.

**Prerequisites**: Load the `figma:figma-use` skill before calling `use_figma`. Load [ux-copy-guidelines.md](references/ux-copy-guidelines.md) before auditing.

## Workflow

### Phase 1 -- Extract

Read all text nodes from the target Figma file or specific page/frame.

```
Step 1: Get the fileKey from the user (extract from Figma URL if provided).
Step 2: Run use_figma to list all pages and identify target scope (full file, specific page, or specific frame).
Step 3: Run use_figma to extract every text node: { nodeId, characters, parentFrameName, textType }.
```

**Text type classification** (infer from context):
1. `heading` -- h1-h3 sized text, section titles
2. `subheading` -- h4-h6 sized text, card titles
3. `body` -- paragraph text, descriptions
4. `label` -- form field labels
5. `placeholder` -- greyed-out input text
6. `helper` -- small text below fields
7. `button` -- text inside button-shaped frames
8. `error` -- red/orange text near form fields
9. `badge` -- small tag/chip text
10. `footer` -- bottom-of-screen text

**Extraction script pattern:**

```js
// Switch to target page first
const targetPage = figma.root.children.find(p => p.name === "PAGE_NAME");
if (targetPage) await figma.setCurrentPageAsync(targetPage);

const textNodes = [];
const root = targetPage || figma.currentPage;

root.findAll(node => {
  if (node.type === 'TEXT' && node.characters.trim().length > 0) {
    // Walk up to find parent frame name
    let parentName = '';
    let parent = node.parent;
    while (parent && parent.type !== 'PAGE') {
      if (parent.type === 'FRAME' || parent.type === 'COMPONENT') {
        parentName = parent.name;
        break;
      }
      parent = parent.parent;
    }

    textNodes.push({
      id: node.id,
      text: node.characters,
      fontSize: typeof node.fontSize === 'number' ? node.fontSize : 'mixed',
      parentFrame: parentName
    });
  }
  return false;
});

return { count: textNodes.length, nodes: textNodes };
```

### Phase 2 -- Audit

Load [references/ux-copy-guidelines.md](references/ux-copy-guidelines.md). For each extracted text node, check against the 14 guideline sections:

1. **Reading level**: Would a 12-year-old understand this?
2. **Jargon**: Any terms from the Forbidden Jargon table (section 4)?
3. **Terminology**: Cross-check against the Glossary (section 3). Flag inconsistencies across screens.
4. **Voice**: Active, direct, "you/your"?
5. **Button pattern**: Verb + noun, max 3 words, sentence case?
6. **Error pattern**: What happened + what to do?
7. **Label pattern**: Noun phrase, sentence case, no colon?
8. **Inclusive language**: Gender-neutral, no idioms?
9. **Number formatting**: Correct per section 11?
10. **Punctuation**: Correct per context?

**Terminology consistency check**: Build a term-usage map across ALL extracted text. Flag when the same concept uses different words (e.g., "Phone number" on one screen, "Mobile number" on another).

### Phase 3 -- Rewrite

For every flagged text node, generate improved copy following the guidelines. Group rewrites by screen/frame.

### Phase 4 -- Review (MANDATORY)

Present a before/after diff table to the user. Group by screen/frame for easy scanning.

```
## Screen: 03 - OTP Verification

| # | Node | Before | After | Reason |
|---|------|--------|-------|--------|
| 1 | header title | "Verify Your Number" | "Verify your number" | Sentence case (section 12) |
| 2 | subtitle | "We'll send a one-time password to your WhatsApp" | "We'll send a verification code to your WhatsApp" | Terminology: "verification code" not "one-time password" (section 3) |
| 3 | button | "Send OTP →" | "Send code →" | Jargon: "OTP" → "code" (section 4) |
```

**Ask the user to approve, edit, or reject each change.** Do NOT proceed to Phase 5 until the user explicitly approves.

### Phase 5 -- Push

Write approved changes back to Figma using `use_figma`. Process in batches of 10-15 nodes per call.

```js
// Load font BEFORE changing text
const node = await figma.getNodeByIdAsync("NODE_ID");
if (node && node.type === 'TEXT') {
  // Load all fonts used in this text node
  const fonts = node.getRangeAllFontNames(0, node.characters.length);
  for (const font of fonts) {
    await figma.loadFontAsync(font);
  }
  node.characters = "NEW TEXT HERE";
}
```

**Critical rules for push:**
1. Always `loadFontAsync` before changing `node.characters` -- will throw otherwise.
2. Use `getRangeAllFontNames` to discover exact fonts (not hardcoded).
3. Return all mutated node IDs.
4. Batch max 15 nodes per `use_figma` call to avoid timeouts.
5. After push, take a `get_screenshot` to verify changes look correct.

## Input

The user provides ONE of:
1. **Figma URL**: Extract fileKey and optional nodeId. Audit that scope.
2. **Figma fileKey**: Audit the entire file (all pages).
3. **Figma fileKey + page name**: Audit only that page.

If no Figma URL/fileKey is provided, ask for it.

## Output

1. **Audit table**: Before/after diff grouped by screen (Phase 4).
2. **Term consistency report**: Flagged terminology inconsistencies across screens.
3. **Updated Figma file**: Approved changes pushed directly (Phase 5).

## Examples

**Input**: "Rewrite the copy on this Figma file to be simpler: https://figma.com/design/abc123/MyApp"

**Output flow**:
1. Extract 47 text nodes across 5 pages
2. Flag 12 issues: 3 jargon, 4 inconsistent terms, 2 passive voice, 3 wrong capitalisation
3. Present diff table grouped by page
4. User approves 10, edits 1, rejects 1
5. Push 11 changes to Figma
6. Screenshot verification

**Input**: "Audit the copy on page 'Registration Form' for terminology consistency"

**Output flow**:
1. Extract 23 text nodes from that page only
2. Cross-check terms against glossary and other pages in the file
3. Flag "Email ID" (should be "Email address"), "Phone number" (should be "Mobile number")
4. Present diff table, get approval, push
