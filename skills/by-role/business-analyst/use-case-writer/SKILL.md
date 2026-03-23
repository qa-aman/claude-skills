---
name: use-case-writer
description: >
  Write structured use cases with main and alternate flows. Use when the user says
  "write a use case", "document the user flow", "use case diagram", "actor goal list",
  "main success scenario", "fully dressed use case", "what does the user do step by step",
  "system behavior for this feature", "interaction flow" - even if they don't explicitly
  say "use case".
---

## Reference Files

- `references/use-case-template.md` - Cockburn's Fully Dressed Use Case template with field descriptions and a worked example. Read this in Step 3 when writing individual use cases.

## Overview

Based on **Writing Effective Use Cases** by Alistair Cockburn - the definitive reference on use case methodology. Cockburn's key insight is the goal level altitude metaphor: most use cases should be written at "sea level" (one user, one sitting, one goal). Writing too high (kite/cloud) produces vague summaries; too low (fish/clam) produces implementation detail disguised as requirements. The Actor-Goal List is the starting point, not the use case itself.

## Workflow

### Step 1: Build the Actor-Goal List
Before writing any use case, list every actor and their goals:
```
| Actor | Goal | Level |
|-------|------|-------|
| Customer | Place an order | Sea level (user goal) |
| Customer | Track shipment | Sea level |
| Warehouse clerk | Pick and pack order | Sea level |
| System (scheduler) | Generate daily reports | Sea level |
| Finance manager | Review quarterly revenue | Kite (summary) |
```
This list is the master index. Every sea-level goal becomes one use case.

### Step 2: Set the scope and level
For each use case, declare:
- **Scope**: System under design (black-box) or component (white-box)?
- **Level**: Cloud (very high summary), Kite (summary), Sea level (user goal), Fish (subfunction), Clam (too low - avoid)

Most use cases should be sea level. If you find yourself writing fish-level steps, extract them into a sub-use case referenced via "includes."

### Step 3: Write the Fully Dressed Use Case
Use Cockburn's template (see `references/use-case-template.md`):
```
USE CASE: [UC-number]: [Title - verb phrase]
PRIMARY ACTOR: [who triggers this]
GOAL: [what the actor is trying to achieve]
SCOPE: [system name]
LEVEL: [sea level / summary / subfunction]
PRECONDITIONS: [what must be true before this starts]
SUCCESS GUARANTEE: [what is true when this succeeds - this becomes acceptance criteria]

MAIN SUCCESS SCENARIO:
1. [Actor] [action]
2. [System] [response]
3. [Actor] [next action]
...

EXTENSIONS:
3a. [Condition]: [what happens instead]
    3a1. [System] [alternate response]
    3a2. Return to step [N] / Use case fails
```

### Step 4: Write extensions for every branch
Extensions are where the real requirements live. For each step in the main scenario, ask:
- What could go wrong? (error extensions)
- What alternatives exist? (alternate flow extensions)
- What if the data is missing or invalid? (validation extensions)

Use the numbered branching notation: 3a, 3b, 3c for branches off step 3.

### Step 5: Identify relationships between use cases
- **Includes**: Shared subfunctions (e.g., "Authenticate User" included by multiple use cases)
- **Extends**: Optional behavior that adds to the base use case
- **Generalizes**: Actor inheritance (e.g., "Premium Customer" generalizes "Customer")

### Step 6: Validate with stakeholders
Walk through each use case with the primary actor or their representative. The main success scenario should sound like their description of a successful interaction.

## Anti-Patterns

**1. Writing at the wrong altitude**
Bad: "The user clicks the Submit button" (clam level - too low, implementation detail).
Good: "The customer submits the order" (sea level - the goal, not the UI).

**2. Extensions only for error cases**
Bad: Only writing extensions for system failures.
Good: Extensions cover errors, alternatives, business rule variations, and edge cases.

**3. Actor is "The User"**
Bad: "The User performs actions." (Which user? What role?)
Good: Name the specific actor role: Customer, Warehouse Clerk, System Administrator.

**4. Missing success guarantee**
Bad: Use case with preconditions but no postconditions.
Good: Success guarantee states what is true after the use case completes - this directly becomes the acceptance criterion.

**5. Monolithic use cases**
Bad: A single use case that covers an entire workflow spanning 30+ steps.
Good: Break into sea-level use cases connected by includes/extends. Each should be 3-9 main steps.

## Quality Checklist

- [ ] Actor-Goal List created before writing individual use cases
- [ ] Every use case has a named actor (not "the user")
- [ ] Level is declared (sea level for most)
- [ ] Main success scenario is 3-9 steps
- [ ] Extensions cover errors, alternatives, and validation failures
- [ ] Success guarantee (postcondition) is defined
- [ ] Preconditions are testable
- [ ] Sub-use cases extracted for shared behavior (includes)
- [ ] Stakeholders have validated the main success scenario
