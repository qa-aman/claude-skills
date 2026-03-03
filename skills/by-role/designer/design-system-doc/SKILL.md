---
name: design-system-doc
description: >
  Document a design system component. Use when the user says "design system docs",
  "document this for the design system", "add this to the design system",
  "design token", "component library docs", "style guide", "design system entry",
  or wants to formally document a pattern, component, or token for team-wide use
  - even if they don't explicitly say "design system".
---

## Overview

Based on **"Atomic Design"** by Brad Frost. A design system is not a component library - it's a shared language. Frost's insight: components without documentation are just code. Documentation is what transforms a component library into a system that a whole team can use consistently without needing to ask the original designer.

Design system documentation has two audiences: designers who need to use the pattern correctly, and engineers who need to implement it accurately. Write for both.

## Workflow

### Step 1: Establish the entry structure
Every design system entry should follow the same structure so team members can predict where to find information:

```
1. Overview (what this is, one paragraph)
2. When to use / when not to use
3. Anatomy (labeled diagram of all parts)
4. Variants
5. States
6. Design tokens used
7. Usage examples (correct and incorrect)
8. Accessibility
9. Related components
10. Changelog
```

### Step 2: Write the overview
One paragraph: what is this component/pattern? What job does it do in the UI?

Include a simple visual (or Figma embed) showing the component in its default state.

### Step 3: When to use / when not to use
This is the most important section. Design systems fail when components are used outside their intended context.

```
Use when:
- [specific context 1]
- [specific context 2]

Don't use when:
- [anti-context 1] - use [alternative] instead
- [anti-context 2] - use [alternative] instead
```

### Step 4: Document the anatomy
Label every part of the component. Each part should have:
- A name (used consistently in code and design)
- Whether it's required or optional
- Constraints (max length, image dimensions, etc.)

### Step 5: Document design tokens
List every token the component uses:

| Token | Value | Role |
|-------|-------|------|
| `color.interactive.primary` | `#0066CC` | Background color |
| `spacing.md` | `16px` | Internal padding |
| `radius.sm` | `4px` | Border radius |
| `typography.body.md` | `16px / 24px` | Label text |

Using tokens (not hardcoded values) ensures the component responds correctly to theme changes in [your design system].

### Step 6: Add usage examples
Show correct and incorrect usage with visual examples:

Correct: [example with explanation of why it's correct]
Incorrect: [example with explanation of why it's wrong and what to do instead]

At least 2-3 of each. Real examples beat abstract rules.

### Step 7: Document accessibility
- Keyboard interactions
- Screen reader behavior
- Required ARIA attributes
- Color contrast compliance (WCAG AA)
- Touch target size compliance

### Step 8: Add a changelog
Every time the component changes, log it:

```
v1.2 - [date] - Added loading state. [your team]
v1.1 - [date] - Updated border radius to match new tokens. [your team]
v1.0 - [date] - Initial release. [your team]
```

## Anti-Patterns

**1. Documentation written only for designers**
Bad: Docs describe visual design but no tokens, props, or accessibility.
Good: Document at both design and implementation level. Engineers should be able to build from the doc alone.

**2. No "when not to use" section**
Bad: Only positive usage guidance.
Good: "When not to use" prevents misuse and is often more valuable than "when to use."

**3. Hardcoded values instead of tokens**
Bad: Component documented with hex codes and pixel values.
Good: Everything references a named token. Tokens are the vocabulary of [your design system].

**4. No changelog**
Bad: Component updated silently.
Good: Every change logged with version, date, and author. [Your team] can see what changed and when.

## Quality Checklist

- [ ] Standard entry structure followed (overview through changelog)
- [ ] When to use AND when not to use documented
- [ ] Anatomy labeled with names used in both design and code
- [ ] All design tokens documented (not hardcoded values)
- [ ] Correct and incorrect usage examples included
- [ ] Accessibility: keyboard, screen reader, ARIA, contrast
- [ ] Changelog entry added for this version
- [ ] Related components cross-referenced
