---
name: acceptance-criteria-writer
description: >
  Write measurable acceptance criteria for requirements or user stories. Use when the user says
  "write acceptance criteria", "definition of done", "how do we test this", "fit criteria",
  "given when then", "Gherkin scenarios", "what does done look like", "testable conditions",
  "how will we know this works" - even if they don't explicitly say "acceptance criteria".
---

## Overview

Based on **Mastering the Requirements Process** by Suzanne & James Robertson - the Fit Criteria concept, where every requirement gets a quantified, measurable condition that proves it has been satisfied. Also draws on **User Stories Applied** by Mike Cohn for the 3 C's (Card, Conversation, Confirmation) where Confirmation = acceptance criteria, and **Writing Effective Use Cases** by Alistair Cockburn where the Success Guarantee (postcondition) is the use case's acceptance criterion. The key insight from Robertson: if you cannot write a fit criterion for a requirement, the requirement is too vague to implement.

## Workflow

### Step 1: Identify the requirement or story to test
Start from a documented requirement (FR-XXX), user story, or use case. Extract:
- **What** the system should do (the behavior)
- **Why** it matters (the rationale - drives which edge cases to cover)
- **Who** is the actor (drives the perspective of the criteria)

### Step 2: Write the primary acceptance criterion (happy path)
Use Robertson's Fit Criterion format for precision:
```
FIT CRITERION: [Measurable condition that proves the requirement is met]
MEASUREMENT: [How to verify - manual test, automated check, metric threshold]
```

Or Gherkin format for scenario-based criteria:
```
GIVEN [precondition / context]
WHEN [action / trigger]
THEN [expected outcome / observable result]
```

### Step 3: Write criteria for the four paths
Every requirement needs criteria covering:
- **Happy path**: The expected successful flow
- **Edge cases**: Boundary conditions, empty states, maximum values
- **Error path**: Invalid input, system failures, timeout scenarios
- **Empty/null path**: No data, first-time use, zero results

Example for a search feature:
```
Happy: GIVEN products exist WHEN user searches "laptop" THEN matching results display within 500ms
Edge: GIVEN 10,000+ results WHEN user searches THEN first page loads with pagination controls
Error: GIVEN search service is unavailable WHEN user searches THEN error message displays with retry option
Empty: GIVEN no products match WHEN user searches "xyznonexistent" THEN "no results" message displays with suggestions
```

### Step 4: Quantify vague criteria (Robertson's Fit Criteria)
Convert subjective requirements into measurable conditions:

| Vague | Fit Criterion |
|-------|---------------|
| "Easy to use" | 80% of new users complete [task] within 5 minutes without assistance |
| "Fast" | 95th percentile response time < 500ms under [load condition] |
| "Secure" | Passes [standard] penetration test with zero critical findings |
| "Reliable" | 99.9% uptime measured monthly; mean time to recovery < 4 hours |
| "Scalable" | Supports [N] concurrent users with < 10% performance degradation |

### Step 5: Link criteria to test type
For each criterion, specify how it will be verified:
```
AC-001: [criterion]
TEST TYPE: [unit / integration / E2E / manual / performance / security]
AUTOMATION: [yes / no - with justification if no]
```

### Step 6: Review with the "three amigos"
Walk through criteria with: the BA (requirements perspective), a developer (feasibility), and a tester (completeness). Criteria that the tester cannot execute or the developer cannot implement need revision.

## Anti-Patterns

**1. Vague criteria that cannot be tested**
Bad: "The system should be user-friendly."
Good: "80% of users complete the checkout flow in under 3 minutes on first attempt."

**2. Only happy-path criteria**
Bad: Acceptance criteria that only describe the successful flow.
Good: Criteria covering happy, edge, error, and empty paths for every requirement.

**3. Implementation-specific criteria**
Bad: "The React component renders a dropdown with CSS class .select-primary."
Good: "The user can select a value from a constrained list of options."

**4. Criteria without a measurement method**
Bad: "The system loads quickly." (How will you measure this?)
Good: "Page load < 2 seconds measured at the 95th percentile using [monitoring tool]."

**5. Copy-paste criteria across stories**
Bad: Same generic acceptance criteria on every story ("meets coding standards").
Good: Each story has criteria specific to its behavior and business logic.

## Quality Checklist

- [ ] Every requirement or story has at least one acceptance criterion
- [ ] Happy path, edge case, error path, and empty/null path covered
- [ ] All criteria are measurable (Robertson's Fit Criteria test)
- [ ] No subjective language without a quantified proxy metric
- [ ] Criteria are written from the user's perspective, not the developer's
- [ ] Each criterion specifies how it will be verified (test type)
- [ ] Three amigos review completed (BA, dev, tester)
- [ ] Criteria are independent of implementation technology
