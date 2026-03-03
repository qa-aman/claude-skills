---
name: write-prd
description: >
  Write a Product Requirements Document (PRD). Use when the user says "write a PRD",
  "document this feature", "product requirements for X", "write requirements",
  "I need a PRD", or wants to formalize a feature or product idea into a structured doc
  - even if they don't explicitly say "PRD".
---

## Overview

A PRD defines the problem, the solution, and the success criteria. It is the contract between product and engineering. A good PRD eliminates ambiguity before it becomes a bug.

## Workflow

### Step 1: Clarify scope
If the user hasn't provided enough context, ask:
- What problem does this solve for the user?
- Who is the target user?
- What's the MVP scope vs. future iterations?

### Step 2: Write the PRD header
```
# PRD: [Feature Name]
**Author:** [your name]
**Status:** Draft
**Last Updated:** [date]
**Stakeholders:** [your team]
```

### Step 3: Write the Problem Statement
One paragraph. Answer: what is broken or missing today, who is affected, and what is the cost of not solving it.

### Step 4: Define Goals and Non-Goals
**Goals:** 2-4 bullet points of what success looks like.
**Non-Goals:** Explicit list of what this PRD does NOT cover. Non-goals prevent scope creep.

### Step 5: Define Success Metrics
Quantify success. Examples:
- "Reduce support tickets related to X by 30%"
- "90% of users complete onboarding in under 5 minutes"
- "Feature adopted by 60% of active users within 30 days"

### Step 6: Write Functional Requirements
Number each requirement. Use "The system shall..." or "Users can..." format.
Group by user flow or component.

### Step 7: Write Open Questions
List unresolved decisions with owners and due dates. Unresolved questions become blockers - surface them early.

### Step 8: Add Appendix (optional)
Link to mocks, research, analytics, or related tickets.

## Anti-Patterns

**1. Solutioning in the problem statement**
Bad: "We need to add a modal because users don't see the CTA."
Good: "30% of users drop off at the checkout step. Research suggests the CTA is not visible enough."

**2. Vague requirements**
Bad: "The system should be fast."
Good: "Page load time should be under 2 seconds for 95th percentile users on 4G."

**3. No non-goals**
Bad: PRD with only goals listed.
Good: Explicit "Out of Scope" section that prevents engineering from over-building.

**4. Missing success metrics**
Bad: "The feature is successful when users like it."
Good: Quantified metric tied to a business or user outcome.

## Quality Checklist

- [ ] Problem statement explains the "why", not the "what"
- [ ] Goals are outcome-based, not output-based
- [ ] Non-goals are explicit
- [ ] Success metrics are measurable and time-bound
- [ ] Each functional requirement is unambiguous
- [ ] Open questions have owners
- [ ] PRD is readable by an engineer with no prior context
