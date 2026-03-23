---
name: frd-writer
description: >
  Write a Functional Requirements Document. Use when the user says "write an FRD",
  "functional requirements", "system requirements", "SRS", "what should the system do",
  "document the functional specs", "software requirements specification",
  "detailed requirements for engineering", "functional spec" - even if they don't
  explicitly say "FRD".
---

## Reference Files

- `references/requirements-attributes.md` - Standard attributes for each requirement (ID, type, priority, status, source, rationale, fit criterion, dependencies). Read this in Step 3 when writing individual requirements.

## Overview

Based on **Software Requirements** by Karl Wiegers & Joy Beatty - the modernized IEEE 830 SRS structure that organizes functional requirements by feature or use case, not by system component. Also draws on **User Stories Applied** by Mike Cohn for agile-format FRDs using the INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable). The key insight from Wiegers: every functional requirement must have a rationale (why it exists) and a fit criterion (how you know it's satisfied). Requirements without these two attributes are wishes, not requirements.

## Workflow

### Step 1: Define the system context
Before writing requirements, establish what the system is:
```
SYSTEM NAME: [name]
PURPOSE: [one sentence]
USERS: [user roles and their primary goals]
ADJACENT SYSTEMS: [systems this integrates with]
SCOPE REFERENCE: [link to BRD or scope document]
```

### Step 2: Organize by functional area
Group requirements by user-facing capability, not by technical layer:
```
FA-1: User Registration and Authentication
FA-2: Order Management
FA-3: Reporting and Analytics
FA-4: Notifications
```

### Step 3: Write individual requirements
For each requirement, use the attributes from `references/requirements-attributes.md`:
```
ID: FR-[area]-[number] (e.g., FR-AUTH-001)
DESCRIPTION: The system shall [action] when [condition] so that [rationale].
PRIORITY: [Must / Should / Could - MoSCoW]
SOURCE: [stakeholder, BRD reference, or regulation]
FIT CRITERION: [measurable condition that proves this requirement is met]
DEPENDENCIES: [other requirements this depends on]
```

Example:
```
ID: FR-AUTH-001
DESCRIPTION: The system shall lock the account after 5 consecutive failed
login attempts so that brute-force attacks are mitigated.
PRIORITY: Must
SOURCE: Security team, ISO 27001 requirement
FIT CRITERION: Account is locked within 1 second of the 5th failed attempt.
Locked account cannot authenticate until unlocked by admin or timeout (30 min).
DEPENDENCIES: FR-AUTH-003 (account unlock process)
```

### Step 4: Define non-functional requirements
For each quality attribute:
```
NFR-PERF-001: Page load time shall not exceed 2 seconds under 1000 concurrent users.
NFR-SEC-001: All PII shall be encrypted at rest (AES-256) and in transit (TLS 1.2+).
NFR-AVAIL-001: System uptime shall be 99.9% measured monthly, excluding planned maintenance.
```

### Step 5: Document business rules
Rules that govern system behavior:
```
BR-001: [If condition, then action]
Example: If order total exceeds [threshold], require manager approval before processing.
Source: [policy document or stakeholder]
```

### Step 6: Add a data requirements summary
List key data entities, their attributes, and CRUD operations (which functions create, read, update, or delete each entity).

### Step 7: Assemble the FRD
```
# Functional Requirements Document: [System Name]
**Version:** [X.X]  **Status:** [Draft / Review / Approved]

## 1. System Context
## 2. Functional Requirements (by area)
## 3. Non-Functional Requirements
## 4. Business Rules
## 5. Data Requirements
## 6. Assumptions and Constraints
## 7. Traceability (to BRD objectives)
## 8. Approval
```

## Anti-Patterns

**1. Requirements without fit criteria**
Bad: "The system shall be fast." (How fast? For whom? Under what conditions?)
Good: "Search results shall return within 500ms for queries against up to 1M records."

**2. Solution-specific language in requirements**
Bad: "Use a PostgreSQL stored procedure to calculate totals."
Good: "The system shall calculate order totals including tax and discount rules."

**3. Compound requirements**
Bad: "The system shall allow users to search orders, filter by date, and export to CSV."
Good: Split into FR-ORD-010 (search), FR-ORD-011 (filter), FR-ORD-012 (export). Each independently testable.

**4. Missing rationale**
Bad: "FR-AUTH-005: The system shall require passwords of at least 12 characters."
Good: Same requirement with "so that [rationale]" - why 12? Policy? Regulation? Risk assessment?

## Quality Checklist

- [ ] System context defined (purpose, users, adjacent systems)
- [ ] Requirements organized by functional area, not technical layer
- [ ] Every requirement has ID, description, priority, source, and fit criterion
- [ ] No compound requirements - each is independently testable (INVEST: Small, Testable)
- [ ] Non-functional requirements are quantified
- [ ] Business rules documented with source
- [ ] Each requirement traces back to a BRD objective
- [ ] Assumptions and constraints listed
