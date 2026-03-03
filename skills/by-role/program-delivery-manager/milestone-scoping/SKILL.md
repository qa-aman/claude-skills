---
name: milestone-scoping
description: >
  Scope a milestone to a fixed time window with variable scope. Use when the user
  says "scope this milestone", "what fits in the sprint", "cut scope for the
  release", "define the MVP for this milestone", "we need to ship by [date] what
  do we cut", "shape the work to fit the cycle", or needs to make hard scope
  decisions under a time constraint - even if they don't explicitly say "milestone
  scoping". Based on "Shape Up" by Ryan Singer (appetite, shaping, betting table)
  and "The Art of Project Management" by Scott Berkun (milestones as forcing
  functions, scope as a variable).
---

## Overview

Based on "Shape Up" by Ryan Singer and "The Art of Project Management" by Scott Berkun. The key insight both books share: time is fixed, scope is the variable. Most delivery failures come from treating scope as fixed and time as the flex - which produces the worst outcome (late delivery of bloated scope). A milestone scoped correctly defines what "done enough to ship" looks like within a fixed window, and explicitly names what is deferred.

## Workflow

### Step 1: Lock the time boundary
Before touching scope, get the time constraint on the table. Ask:
- What is the milestone date or sprint end date?
- Is this date moveable? (If yes, scope discussion changes. If no, proceed.)
- What is the sprint or cycle length?

Shape Up rule: appetite is decided before scope. If the team is willing to spend 6 weeks on this, that is different from 2 weeks - and the solution should change accordingly, not the timeline.

### Step 2: Identify the core job to be done
Ask: "What is the one thing this milestone must accomplish for it to be worth shipping?"

This is not a feature list. It is a user or business outcome:
- "Users can complete checkout without calling support"
- "The migration is live with zero data loss"
- "Engineering team has a working CI pipeline"

If the user gives a list of features instead of an outcome, push back: "Which of these features, if not shipped, would make the milestone not worth shipping?"

### Step 3: Sort everything into Must / Should / Cut
Take the full feature list or backlog for this milestone and classify each item:

| Category | Criteria | Action |
|----------|---------|--------|
| **Must** | The milestone does not achieve its core job without this | In scope, non-negotiable |
| **Should** | Valuable, improves the outcome, but the milestone ships without it | In scope if capacity allows |
| **Cut** | Nice to have, or solvable with a workaround for now | Explicitly deferred to next cycle |

Berkun's forcing function test for each item: "If we cut this, does the milestone still meet its core job?" If yes, it is a Should or Cut - not a Must.

### Step 4: Apply the fat marker sketch
For each Must item, describe it at the right altitude using Shape Up's fat marker principle:
- Write what the user can do, not how it is built
- Leave room for engineers to make implementation decisions
- Flag the rabbit holes: specific traps or complexity that would blow the scope

```
MUST: [feature/capability]
User can: [what they can do in 1 sentence]
Rabbit holes to avoid: [specific traps - e.g., "don't rebuild the notification system, use existing email infra"]
Complexity signal: [anything here that could expand scope unexpectedly]
```

### Step 5: Generate the milestone scope document
```
MILESTONE SCOPE - [milestone name]
Cycle: [start date] to [end date]
Core job: [outcome this milestone achieves]

IN SCOPE (Must)
1. [Feature/capability] - [one-sentence user-facing description]
   Rabbit holes: [traps to avoid]

2. [Feature/capability] - [description]
   Rabbit holes: [traps to avoid]

IN SCOPE IF CAPACITY ALLOWS (Should)
- [Feature] - [description]
- [Feature] - [description]

OUT OF SCOPE (explicitly deferred)
- [Feature]: [why deferred, when it will be revisited]
- [Feature]: [rationale]

OPEN QUESTIONS (must resolve in first half of cycle)
- [Question] - Owner: [name] - Due: [date]

DONE CRITERIA
The milestone is complete when:
- [Specific, measurable condition 1]
- [Specific, measurable condition 2]
- [No Sev 1 defects / performance threshold / user acceptance criteria]
```

### Step 6: Run the scope pressure test
Before locking the scope, ask these three questions:

1. "If the team discovers this takes 30% longer than expected, what gets cut first?" - The answer should be the Should list. If there is no answer, the scope is under-specified.

2. "Is there anything on the Must list that a team member might reasonably interpret as 10x bigger than we intend?" - If yes, add a rabbit hole note to that item.

3. "Is there a workaround that satisfies the core job without building this feature?" - If yes, move it to Should or Cut.

## Anti-Patterns

**1. Treating the feature list as the milestone**
Bad: "Milestone 2 = [list of 15 features]"
Good: "Milestone 2 = users can complete onboarding without contacting support. These 4 features make that possible."

**2. No explicit Cut list**
Bad: Scope document with only what is included.
Good: Out of scope section is as important as in scope. It prevents scope creep during build and manages stakeholder expectations.

**3. Must list too large**
Bad: 12 items in the Must category.
Good: Must items should be completable in 70% of the cycle window, leaving buffer for Should and unexpected work. If Must is too large, the real Must list is not yet defined.

**4. Rabbit holes not named**
Bad: "Build the reporting dashboard" with no caveats.
Good: "Build the reporting dashboard. Rabbit hole: don't build custom chart library - use existing components. Don't add export to PDF in v1."

**5. Done criteria are vague**
Bad: "Milestone is done when features are built."
Good: "Done when: all P0 user stories are accepted, no Sev 1 defects, performance under 200ms on target hardware, stakeholder sign-off received."

## Quality Checklist

- [ ] Time boundary is fixed and stated at the top
- [ ] Core job is one outcome statement, not a feature list
- [ ] Every item is classified as Must / Should / Cut
- [ ] Must items have fat marker descriptions with rabbit holes named
- [ ] Out of scope section is explicit with rationale for each deferred item
- [ ] Done criteria are measurable, not subjective
- [ ] Scope pressure test has been run (what gets cut if capacity is short?)
