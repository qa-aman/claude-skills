---
name: prioritization
description: >
  Prioritize a feature backlog or list of ideas. Use when the user says "help me prioritize",
  "prioritize this backlog", "RICE score these", "MoSCoW", "what should we build first",
  "rank these features", or has a list of items and needs to decide order
  - even if they don't explicitly say "prioritization framework".
---

## Overview

Prioritization removes the loudest-voice problem. A framework forces explicit tradeoffs. Use RICE when you need a defensible numeric score. Use MoSCoW when you need fast stakeholder alignment.

## Workflow

### Step 1: Identify the framework
Ask the user which framework they want, or recommend based on context:
- **RICE** - when you need data-driven scoring and can estimate reach/impact
- **MoSCoW** - when you need fast consensus across stakeholders
- **Both** - when you want RICE to inform MoSCoW buckets

### Step 2a: RICE Scoring

Score each item on:
- **Reach** - How many users affected per period? (number)
- **Impact** - How much does it move the needle per user? (0.25 / 0.5 / 1 / 2 / 3)
- **Confidence** - How sure are you? (100% / 80% / 50%)
- **Effort** - Person-weeks to build (number)

Formula: `RICE = (Reach x Impact x Confidence) / Effort`

Present as a table:
| Feature | Reach | Impact | Confidence | Effort | RICE Score |
|---------|-------|--------|------------|--------|------------|

### Step 2b: MoSCoW Bucketing

Assign each item to:
- **Must Have** - Without this, the release fails
- **Should Have** - High value, not critical for launch
- **Could Have** - Nice to have, cut if pressed
- **Won't Have** - Explicitly out of scope this cycle

### Step 3: Identify conflicts
Flag items where stakeholders are likely to disagree. Surface these explicitly rather than burying them in a ranked list.

### Step 4: Recommend top 3
Summarize with a clear recommendation: "Based on this scoring, focus on X, Y, Z in this cycle. Consider A next cycle."

## Anti-Patterns

**1. Scoring without data**
Bad: Assigning RICE scores based on gut feel without stating the assumptions.
Good: State assumptions explicitly. "Reach = 500 assumes 20% of MAU hits this flow - validate with analytics."

**2. Everything is "Must Have"**
Bad: Stakeholders label every item Must Have to protect their work.
Good: Force a constraint: "You have 3 Must Have slots. Which 3?" Scarcity forces honest prioritization.

**3. Prioritizing solutions instead of problems**
Bad: "Build a dashboard" vs "Build export feature" - these are solutions.
Good: Reframe as problems first: "Users can't track progress over time" - then prioritize the problem, then pick the solution.

**4. Never revisiting**
Bad: RICE score set once, never updated.
Good: Scores are estimates. Flag items for re-scoring when new data arrives.

## Quality Checklist

- [ ] Framework choice is explained (why RICE or MoSCoW for this situation)
- [ ] RICE: all four factors scored with stated assumptions
- [ ] MoSCoW: no more than 40% of items in Must Have
- [ ] Conflicts and disagreements are surfaced, not hidden
- [ ] Clear recommendation at the end
- [ ] Scores are labeled as estimates, not facts
