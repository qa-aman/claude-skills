---
name: feature-spec
description: >
  Write a feature spec for engineering handoff. Use when the user says "write a spec",
  "feature spec", "one-pager for eng", "spec this out", "write up this feature",
  "I need to hand this off to engineering", or wants a concise technical brief
  for a feature - even if they don't say "feature spec".
---

## Overview

A feature spec is not a PRD. A PRD justifies building something. A spec tells engineers exactly what to build. It is a contract: ambiguity in the spec becomes a bug in production.

Keep it to one page. If it needs more than one page, the feature is too large and should be split.

## Workflow

### Step 1: Write the header
```
# Feature Spec: [Feature Name]
**PM:** [your name]
**Eng Lead:** [engineer name]
**Status:** Draft | In Review | Approved
**Target Sprint:** [sprint or date]
**Related PRD / Ticket:** [link]
```

### Step 2: Write the Problem (2-3 sentences)
What is broken or missing? Who is affected? What is the measurable cost?

### Step 3: Write the Proposed Solution (3-5 sentences)
What are we building? How does it solve the problem? What does it NOT do?

### Step 4: Write Functional Requirements
Number each requirement. Be exhaustive. Engineers should not need to ask "what happens when X?" if X is a realistic scenario.

Structure:
- Happy path first
- Error states second
- Edge cases third

### Step 5: Write Non-Functional Requirements
- Performance targets (load time, response time)
- Accessibility requirements
- Browser / device support
- Security or compliance constraints

Only include what's relevant. Don't pad.

### Step 6: Define Out of Scope
Explicit list of things this spec does NOT cover. This prevents engineers from over-building or making assumptions about future phases.

### Step 7: Add Open Questions
Format:
```
Q: [question]
Owner: [name]
Due: [date]
```

Unresolved questions block engineering. Assign owners and deadlines.

### Step 8: Link to assets
Mockups, Figma files, API specs, data models. A spec without visuals is incomplete for any UI work.

## Anti-Patterns

**1. Specs that describe the UI instead of the behavior**
Bad: "There is a blue button in the top right corner."
Good: "Users can trigger X from the [feature area]. Exact placement per Figma [link]."

**2. Missing error states**
Bad: "User submits the form and sees a confirmation."
Good: Cover success, validation error, server error, empty state, and loading state.

**3. Assumptions instead of requirements**
Bad: "This should work on mobile." (assumes engineer knows what "work" means)
Good: "Feature is fully functional on iOS Safari and Chrome Android at 375px width."

**4. Spec approved with open questions unresolved**
Bad: Moving to engineering with "TBD" items.
Good: All open questions resolved or explicitly deferred to a named owner with a date before approval.

## Quality Checklist

- [ ] Header has PM, eng lead, status, target sprint
- [ ] Problem is 2-3 sentences, outcome-focused
- [ ] Requirements cover happy path, error states, and edge cases
- [ ] Out of scope section exists
- [ ] Open questions have owners and due dates
- [ ] Figma / mockup links included for any UI work
- [ ] Spec fits on one page (split if it doesn't)
