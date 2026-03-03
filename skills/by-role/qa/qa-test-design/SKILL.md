---
name: qa-test-design
description: Design and write QA test artifacts - test cases, test plans, acceptance criteria, API test specs, and PR testability reviews. Use this skill whenever a QA engineer or SDET needs to translate requirements, user stories, or feature specs into structured test documentation. Trigger on phrases like "write test cases", "create a test plan", "define acceptance criteria", "review this PR for testability", "write API test specs", "test coverage for this feature", "what should we test", "how do we test this", or any request to structure what and how to test before execution begins. Also trigger when a developer asks "is this testable?" or a PM asks "what are the edge cases?".
---

## Overview

Based on **"The Art of Software Testing"** by Glenford Myers. Myers established three systematic techniques that catch the most defects per test written: equivalence partitioning, boundary value analysis, and decision table testing. Applied together, they replace ad-hoc test design with a method that maximizes defect detection within a fixed time budget.

# QA Test Design

Turn requirements, user stories, and feature specs into structured, executable test documentation.

## Context Personalization

At the start of every invocation, read `~/.claude/skills/skill-context.md` if it exists. Use the values there to replace generic placeholders in your output:
- `[your industry]` → actual industry (e.g. Fintech, HealthTech)
- `[your stack]` → actual tech stack (e.g. React + Node.js)
- `[your compliance]` → actual compliance requirements (e.g. PCI-DSS, HIPAA, none)
- `[your test framework]` → actual framework (e.g. Jest, Cypress, Playwright)

If the file does not exist, use generic placeholders and proceed normally.

## When to Use

- Translating a user story or spec into test cases
- Writing acceptance criteria before a feature is built
- Reviewing a PR for testability gaps
- Drafting an API test spec from endpoint documentation
- Producing a test plan for a sprint or release

## Inputs to Gather

Before writing anything, collect:
1. **Feature/scope** - what is being built or changed?
2. **User story or spec** - the requirements source
3. **Tech context** - frontend, API, mobile, or all of the above?
4. **Test management tool** - Jira, TestRail, Notion, or plain markdown?
5. **Risk level** - new feature, regression area, or critical path?

If inputs are missing, ask for the user story or spec before proceeding.

## Workflow

### Step 1: Analyze Requirements

Read the spec or story. Identify:
- The happy path (what should work)
- Negative paths (what should fail gracefully)
- Edge cases (boundary values, empty states, large data, concurrent users)
- Integration points (APIs called, DB writes, external services)
- Non-functional requirements (performance thresholds, accessibility, security)

**Apply Myers' three techniques:**

- **Equivalence Partitioning** - Divide inputs into classes where any value in the class is equally likely to reveal a bug. Test one value per class (not all). Example: age input - classes are negative, 0-17, 18-120, >120. Test one from each.
- **Boundary Value Analysis** - Bugs cluster at boundaries. For each equivalence class, test the boundary values (min, min+1, max-1, max). Example: a form accepting 1-255 characters → test 0, 1, 2, 254, 255, 256.
- **Decision Table Testing** - For features with complex logic (multiple conditions → multiple outcomes), build a table mapping all condition combinations to expected actions. Catches combinations that informal testing misses.

### Step 2: Write Test Cases

Use this structure for each test case:

```
ID: TC-[feature]-[number]
Title: [brief action + expected result]
Preconditions: [system state before test runs]
Steps:
  1. [action]
  2. [action]
Expected Result: [observable outcome]
Priority: P1 / P2 / P3
Type: Positive / Negative / Edge / Regression
```

Aim for coverage across:
- **P1** - critical path, blocks release if broken
- **P2** - important, degrades experience
- **P3** - nice to have, low risk

### Step 3: Write Acceptance Criteria (if requested)

Use Given/When/Then format:

```
Given [precondition]
When [action]
Then [expected outcome]
```

Each criterion must be:
- Observable - can be verified by a tester or automated check
- Specific - no ambiguity about pass/fail
- Independent - does not depend on another AC to make sense

### Step 4: API Test Spec (if requested)

For each endpoint, document:

```
Endpoint: [METHOD] /path
Description: [what it does]
Auth: [required / not required / scope needed]

Test Cases:
  Happy path: [valid payload → expected response + status]
  Missing required field: [payload → 400 + error message]
  Invalid auth: [payload → 401/403]
  Edge: [boundary value → expected behavior]

Contract checks:
  - Response schema matches documented spec
  - Required fields always present
  - Error messages are human-readable
```

### Step 5: PR Testability Review (if requested)

Evaluate the diff for:
- Are new code paths covered by existing or new tests?
- Are error branches tested, not just the happy path?
- Are there hardcoded values that should be parameterized for testing?
- Is the code structured to be testable (dependencies injectable, side effects isolated)?
- Are there missing logging/observability that would make failures hard to diagnose?

Output as a short checklist with specific line references.

## Output Formats

**Test cases** - table or numbered list, depending on test management tool
**Acceptance criteria** - Given/When/Then bullets in the ticket
**API test spec** - markdown doc or Postman collection outline
**PR testability review** - bullet checklist with file:line references

## Anti-Patterns

**Only testing the happy path**
Every feature has edge cases. Empty inputs, max limits, concurrent operations, network failures. If you only test what should work, you miss what will break in production.

**Vague steps**
"Click the button" is not a test step. "Click the Submit button on the /checkout page with a valid Visa card number" is. Steps must be reproducible by someone who has never seen the feature.

**No expected result**
A test case without a specific expected result is not a test case. It is a script. State exactly what the system should do - status codes, UI messages, DB state, side effects.

**Writing tests after the feature is built**
Test design before implementation surfaces ambiguity in requirements while it is cheap to fix. Do test design during sprint planning or alongside spec review, not after code review.

**Ignoring non-functional requirements**
Performance, accessibility, and security are test cases too. A login flow that passes functional tests but is inaccessible to screen readers is a bug.

## Quality Checklist

Before finalizing any test artifact:

- [ ] Every happy path has a corresponding negative path
- [ ] Edge cases include: empty, null, max value, min value, special characters
- [ ] Each test case has a unique ID, clear steps, and a specific expected result
- [ ] Priority is assigned (P1/P2/P3) with rationale
- [ ] Integration points and external dependencies are called out
- [ ] Acceptance criteria are observable and unambiguous
- [ ] API specs include auth, error, and schema checks
- [ ] No test depends on execution order (each is independent)
