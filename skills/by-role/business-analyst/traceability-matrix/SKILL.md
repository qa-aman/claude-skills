---
name: traceability-matrix
description: >
  Create a requirements traceability matrix linking requirements to design, test, and delivery.
  Use when the user says "traceability matrix", "RTM", "requirements traceability",
  "link requirements to tests", "trace requirements", "coverage matrix",
  "are all requirements tested", "requirements coverage", "forward traceability",
  "backward traceability" - even if they don't explicitly say "traceability matrix".
---

## Reference Files

- `references/traceability-template.md` - Template table for the RTM with all standard columns plus a V-Model diagram showing the requirement-to-test level mapping. Read this in Step 2 when setting up the matrix structure.

## Overview

Based on **Requirements Engineering** by Elizabeth Hull, Ken Jackson, and Jeremy Dick - the most thorough treatment of pre-RS traceability (source to requirement) and post-RS traceability (requirement to design to test to delivery). Also draws on the **BABOK Guide v3 (IIBA)** Requirements Life Cycle Management knowledge area, and **Mastering the Requirements Process** by Robertson & Robertson where each Volere Snow Card links requirement to event, source, and rationale. The key insight from Hull: traceability is not a bureaucratic checkbox. It answers three critical questions: "Why does this requirement exist?" (backward), "Is this requirement implemented?" (forward), and "Is anything implemented that wasn't required?" (coverage).

## Workflow

### Step 1: Define the traceability scope
```
PROJECT: [name]
TRACEABILITY DIRECTION:
  - Backward (pre-RS): Source -> Business Req -> Stakeholder Req -> Functional Req
  - Forward (post-RS): Functional Req -> Design -> Code -> Test Case -> Test Result
DEPTH: [How many levels of tracing? Minimum: requirement -> test case]
TOOL: [spreadsheet, requirements management tool, or issue tracker]
```

### Step 2: Set up the matrix structure
Use the template from `references/traceability-template.md`. The V-Model determines which requirement level maps to which test level:
```
Business Requirements  <------>  Acceptance Tests (UAT)
  Stakeholder Requirements  <------>  System Tests
    Functional Requirements  <------>  Integration Tests
      Component/Technical Specs  <------>  Unit Tests
```

### Step 3: Populate backward traceability (source to requirement)
For each requirement, trace backward:
```
| Req ID | Source | Business Req | Stakeholder Req | Notes |
|--------|--------|-------------|-----------------|-------|
| FR-AUTH-001 | ISO 27001, Security team | BO-3: Reduce security incidents | SR-12: Lock after failed attempts | |
| FR-ORD-005 | Customer feedback Q3 | BO-1: Improve order experience | SR-04: Real-time order tracking | |
```

This answers: "Why does this requirement exist?" and "What happens if we remove it?"

### Step 4: Populate forward traceability (requirement to delivery)
For each requirement, trace forward:
```
| Req ID | Design Ref | Test Case ID | Test Result | Status |
|--------|-----------|-------------|-------------|--------|
| FR-AUTH-001 | DD-Auth-3.2 | TC-AUTH-001, TC-AUTH-002 | Pass | Verified |
| FR-ORD-005 | DD-Ord-5.1 | TC-ORD-012 | Fail (defect #234) | Open |
```

This answers: "Is this requirement implemented and tested?"

### Step 5: Analyze coverage gaps
Run three coverage checks:

**Forward coverage**: % of requirements with at least one test case
```
Forward coverage = (Requirements with test cases / Total requirements) x 100%
Target: 100% for Must requirements, 90%+ for Should requirements
```

**Backward coverage**: % of requirements traceable to a business source
```
Backward coverage = (Requirements with source / Total requirements) x 100%
Target: 100% - any requirement without a source is suspect
```

**Gold plating check**: Test cases or design elements that don't trace to any requirement
```
Orphan tests = Test cases with no linked requirement
Orphan design = Design components with no linked requirement
```
These indicate scope creep or unnecessary work.

### Step 6: Track requirement states
Monitor each requirement through its lifecycle:
```
| State | Definition |
|-------|-----------|
| Proposed | Identified but not yet approved |
| Approved | Accepted for implementation |
| Designed | Design artifact created |
| Implemented | Code complete |
| Tested | Test cases executed |
| Verified | All tests pass, accepted |
| Deferred | Postponed to a future release |
```

### Step 7: Output and maintain the RTM
Deliver the traceability matrix with coverage metrics. Update it as requirements change - the matrix is a living document, not a one-time artifact.

## Anti-Patterns

**1. Traceability as a checkbox exercise**
Bad: Filling in the matrix after everything is built, just to satisfy an audit.
Good: Building the matrix as requirements are written and maintaining it through delivery.

**2. Forward-only traceability**
Bad: Linking requirements to tests but not back to business sources.
Good: Both directions - backward (why) and forward (is it done).

**3. No coverage analysis**
Bad: A complete-looking matrix that's never analyzed for gaps.
Good: Run coverage metrics regularly - forward, backward, and gold plating checks.

**4. One-to-one assumption**
Bad: Expecting every requirement maps to exactly one test.
Good: Many-to-many is normal - one requirement may need multiple tests; one test may verify multiple requirements.

**5. Stale matrix**
Bad: Matrix created in month 1, never updated when requirements changed.
Good: Update the matrix whenever a requirement is added, changed, deferred, or removed.

## Quality Checklist

- [ ] Traceability direction defined (backward and forward)
- [ ] V-Model mapping established (requirement level to test level)
- [ ] Every requirement has backward traceability to a source
- [ ] Every Must requirement has forward traceability to at least one test case
- [ ] Forward coverage calculated and meets target (100% for Must)
- [ ] Backward coverage calculated (100% target)
- [ ] Gold plating check done (orphan tests and design elements identified)
- [ ] Requirement states tracked through lifecycle
- [ ] Matrix is maintained as a living document, not a snapshot
