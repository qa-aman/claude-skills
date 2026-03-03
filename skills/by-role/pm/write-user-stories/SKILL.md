---
name: write-user-stories
description: >
  Write user stories with acceptance criteria. Use when the user says "write user stories",
  "convert this to stories", "create acceptance criteria", "break this into tickets",
  "story for this feature", or wants to translate a feature idea into sprint-ready items
  - even if they don't explicitly say "user stories".
---

## Overview

A user story is a unit of work from the user's perspective. It forces the team to think about value before implementation. Acceptance criteria define "done" - without them, stories are ambiguous and sprints are unpredictable.

## Workflow

### Step 1: Identify the users
List the distinct user types affected by the feature. Each user type may need separate stories.

### Step 2: Write the story headline
Format: `As a [user type], I want [goal], so that [benefit].`

The "so that" clause is critical - it ties the story to user value. If you can't write it, the story may not be worth building.

### Step 3: Write Acceptance Criteria
Use Given/When/Then format for each criterion:
```
Given [precondition]
When [action]
Then [expected outcome]
```

Write 3-7 criteria per story. Fewer means incomplete; more means the story is too large.

### Step 4: Add edge cases
List edge cases as additional AC items:
- What happens on error?
- What happens with empty state?
- What happens at limits (0 items, max items)?

### Step 5: Estimate complexity (optional)
Flag stories as Small / Medium / Large based on AC complexity. Stories larger than Medium should be split.

### Step 6: Link dependencies
Note any stories that must complete before this one. Untracked dependencies cause sprint failures.

## Anti-Patterns

**1. Technical stories written as user stories**
Bad: "As a developer, I want to refactor the auth module so that code is cleaner."
Good: Technical work goes in a tech debt ticket, not a user story. If there's no user value, say so explicitly.

**2. Missing "so that" clause**
Bad: "As a user, I want to reset my password."
Good: "As a user, I want to reset my password so that I can regain access to my account without contacting support."

**3. Acceptance criteria that describe implementation**
Bad: "Given the user clicks the button, when the API call returns 200, then..."
Good: AC describes behavior, not implementation. "Given the user is logged out, when they request a password reset, then they receive an email within 2 minutes."

**4. One mega-story**
Bad: "As a user, I want to manage my account settings."
Good: Split into separate stories for each setting type. Each story is independently deployable.

## Quality Checklist

- [ ] Each story follows "As a [user], I want [goal], so that [benefit]"
- [ ] "So that" clause ties to real user value
- [ ] Each story has 3-7 acceptance criteria
- [ ] AC uses Given/When/Then format
- [ ] Edge cases (empty state, errors, limits) are covered
- [ ] Stories are independently deployable
- [ ] No implementation details in AC
