# Requirements Traceability Matrix Template

Use this template in Step 2 when setting up the matrix structure. Copy and adapt the tables below for your project.

---

## V-Model: Requirement Level to Test Level Mapping

```
Requirements Side                    Testing Side
==================                   =============

Business Requirements  <-----------> Acceptance Tests (UAT)
  |                                        |
  v                                        v
Stakeholder Requirements <---------> System Tests
  |                                        |
  v                                        v
Functional Requirements <----------> Integration Tests
  |                                        |
  v                                        v
Technical / Component Specs <------> Unit Tests
```

Each requirement level has a corresponding test level. Traceability ensures every requirement is tested at the appropriate level.

---

## Full RTM Template

```
| Req ID | Req Description | Priority | Source (Backward) | Business Req | Design Ref | Test Case ID(s) | Test Result | Status | Owner | Notes |
|--------|----------------|----------|-------------------|-------------|-----------|----------------|-------------|--------|-------|-------|
| FR-XXX-001 | [description] | Must | [stakeholder, regulation, BRD ref] | [BO-X] | [DD-X.Y] | [TC-XXX-001, TC-XXX-002] | [Pass/Fail/Not Run] | [Proposed/Approved/Verified] | [name] | [any notes] |
```

### Column Definitions

| Column | Description | Who Fills It | When |
|--------|-------------|-------------|------|
| **Req ID** | Unique identifier (FR-[area]-[number]) | BA | At requirements definition |
| **Req Description** | Brief description of the requirement | BA | At requirements definition |
| **Priority** | MoSCoW: Must / Should / Could / Won't | BA + Stakeholders | At prioritization |
| **Source (Backward)** | Why this requirement exists - stakeholder, regulation, or BRD reference | BA | At requirements definition |
| **Business Req** | Link to the business objective this supports | BA | At requirements definition |
| **Design Ref** | Link to design document or component | Developer / Architect | At design |
| **Test Case ID(s)** | Link to test case(s) that verify this requirement | QA / BA | At test planning |
| **Test Result** | Pass / Fail / Not Run / Blocked | QA | At test execution |
| **Status** | Lifecycle state (see states below) | BA | Ongoing |
| **Owner** | Person responsible for this requirement | BA | At requirements definition |
| **Notes** | Change history, exceptions, deferral reasons | Anyone | Ongoing |

---

## Coverage Metrics Template

```
TRACEABILITY COVERAGE REPORT
Project: [name]
Date: [date]
Total Requirements: [N]

FORWARD COVERAGE (Requirements -> Tests):
  Must requirements with tests:    [X] / [Y] = [Z]%
  Should requirements with tests:  [X] / [Y] = [Z]%
  Could requirements with tests:   [X] / [Y] = [Z]%
  Overall forward coverage:        [X] / [Y] = [Z]%

BACKWARD COVERAGE (Requirements -> Source):
  Requirements with source:        [X] / [Y] = [Z]%
  Requirements without source:     [list IDs - these need investigation]

GOLD PLATING CHECK:
  Orphan test cases (no linked req): [list TC IDs]
  Orphan design elements (no linked req): [list DD refs]

TEST EXECUTION STATUS:
  Tests passed:    [X] / [Y] = [Z]%
  Tests failed:    [X] (linked defects: [list])
  Tests not run:   [X]
  Tests blocked:   [X]
```

---

## Requirement Lifecycle States

```
Proposed --> Approved --> Designed --> Implemented --> Tested --> Verified
    |            |                                                  |
    v            v                                                  v
  Rejected    Deferred ----------------------------------------> Deferred
```

| State | Definition | Exit Criteria |
|-------|-----------|---------------|
| **Proposed** | Identified but not yet reviewed | Stakeholder review completed |
| **Approved** | Accepted for implementation in this release | Prioritized and baselined |
| **Designed** | Design artifact exists | Design review passed |
| **Implemented** | Code complete | Code review passed |
| **Tested** | Test cases executed | All test cases have results |
| **Verified** | All tests pass, stakeholder accepts | UAT sign-off |
| **Deferred** | Postponed to a future release | Deferral approved, target release assigned |
| **Rejected** | Will not be implemented | Rejection rationale documented |
