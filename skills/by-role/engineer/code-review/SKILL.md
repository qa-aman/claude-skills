---
name: code-review
description: "Review code for quality, bugs, security vulnerabilities, naming conventions, performance issues, and design patterns. Provides structured feedback without modifying code directly. Use when the user says 'review this code', 'do a code review', 'check this PR', 'review this diff', 'is this code good', 'what's wrong with this code', 'code quality check', or pastes code and wants feedback - even if they don't explicitly say 'code review'."
---

## Overview

Review code for intent clarity, correctness, and maintainability. A code review is not just a bug hunt - it checks that the code communicates its intent clearly to the next developer who reads it.

## Workflow

### Step 1: Read for intent first
Before looking for bugs, read the code as a whole. Can you understand what it does without reading comments or documentation? If not, that's the first finding.

### Step 2: Check naming
Review every variable, function, and class name for intent clarity.
- Does the name tell you what it does, not how it does it?
- Would a new team member understand this name without context?
- Are booleans named as predicates? (`isValid`, `hasPermission`, not `flag`, `check`)

Bad: `d = datetime.now() - start`
Good: `elapsed_time = datetime.now() - start`

### Step 3: Check function size and responsibility
Each function should do one thing and do it well.
- Functions longer than 20 lines are candidates for extraction
- If a function needs a comment to explain what each section does, split it
- If a function has multiple levels of abstraction mixed together, extract

### Step 4: Check error handling
- Are errors handled explicitly or silently swallowed?
- Do error messages help the caller understand what went wrong and how to fix it?
- Are exceptions used for exceptional cases only - not flow control?

### Step 5: Check for duplication
- Is this logic duplicated elsewhere in the codebase?
- Could this be extracted to a shared utility?
- Are magic numbers duplicated? (extract to named constants)

### Step 6: Check tests
- Are there tests for the new or changed behavior?
- Do tests cover the happy path AND failure cases?
- Are test names descriptive? (`test_login_fails_with_invalid_password` not `test_login_2`)

### Step 7: Write the review
Structure feedback as:
- **Must fix** - bugs, security issues, broken contracts
- **Should fix** - violations that will cause maintenance pain
- **Consider** - style suggestions, optional improvements
- **Praise** - what was done well (important for team morale and learning)

### Example Review Output

Given this code:
```python
def process(d, u):
    if d:
        for i in d:
            if i['status'] == 'active':
                send_email(u, i)
                update_db(i)
                log(i)
```

Review:
- **Must fix:** No error handling around `send_email` or `update_db` - a failure in one skips the rest of the list. Wrap in try/except per item or use a batch-safe approach.
- **Should fix:** `d`, `u`, `i` reveal no intent. Rename to `documents`, `user`, `document`. `process` should describe what it does: `notify_user_of_active_documents`.
- **Consider:** Extract the filter (`status == 'active'`) into a list comprehension or generator to separate filtering from action.
- **Praise:** The operation order (email → DB → log) is correct - notifies the user before persisting state.

## Anti-Patterns

**1. Nitpicking style without flagging real issues**
Bad: 10 comments about variable naming, zero comments about a missing null check.
Good: Prioritize by impact. Fix correctness first, then clarity, then style.

**2. No positive feedback**
Bad: Only listing problems.
Good: Note what was done well. Reviewers who only criticize produce defensive engineers.

**3. Vague feedback**
Bad: "This function is too complex."
Good: "This function does 3 things: validates input, transforms data, and saves to DB. Extract each into its own function so each can be read and tested independently."

**4. Reviewing without running the code**
Bad: Approving a PR without checking it builds and tests pass.
Good: CI should enforce this automatically. If CI is absent, run tests locally before approving.

## Quality Checklist

- [ ] Intent is clear - code reads without needing to decode it
- [ ] Names reveal intent at every level (variables, functions, classes)
- [ ] Functions have single responsibility and fit in one screen
- [ ] Error handling is explicit - no silent failures
- [ ] No unnecessary duplication
- [ ] Tests cover happy path and failure cases
- [ ] Must fix / should fix / consider clearly separated
- [ ] At least one specific piece of positive feedback included
