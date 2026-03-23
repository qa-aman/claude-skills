# Requirements Attributes Reference

Use this reference in Step 3 when writing individual requirements. Every requirement should carry these attributes to be traceable, testable, and manageable.

---

## Standard Attributes

| Attribute | Description | Example |
|-----------|-------------|---------|
| **ID** | Unique identifier: FR-[area]-[number] | FR-AUTH-001 |
| **Description** | "The system shall [action] when [condition] so that [rationale]" | The system shall lock the account after 5 failed login attempts so that brute-force attacks are mitigated |
| **Type** | Functional / Non-Functional / Business Rule / Constraint | Functional |
| **Priority** | MoSCoW: Must / Should / Could / Won't | Must |
| **Status** | Proposed / Approved / Implemented / Verified / Deferred | Proposed |
| **Source** | Who requested it or what regulation mandates it | Security team, ISO 27001 |
| **Rationale** | Why this requirement exists - the business reason | Prevent unauthorized access via brute-force |
| **Fit Criterion** | Measurable condition proving the requirement is met (Robertson's Volere) | Account locked within 1s of 5th failure; cannot auth until admin unlock or 30 min timeout |
| **Dependencies** | Other requirements this depends on or conflicts with | FR-AUTH-003 (unlock process) |
| **Version** | When this requirement was last changed | v1.2, [date] |
| **Stability** | How likely this requirement is to change (High / Medium / Low) | High |

## Requirement Types

| Type | What It Defines | Example |
|------|-----------------|---------|
| **Functional** | What the system does (behavior) | The system shall send an email notification when an order ships |
| **Non-Functional** | How well the system performs (quality) | Response time < 2 seconds under 1000 concurrent users |
| **Business Rule** | Policy or decision logic the system enforces | Orders over [amount] require manager approval |
| **Constraint** | Fixed limitation on the solution | Must integrate with [existing system] via REST API |
| **Transition** | What's needed to move from current to future state | Historical data migrated with 99.9% accuracy |

## Writing Good Fit Criteria (Volere)

A fit criterion makes a requirement testable. If you cannot write a fit criterion, the requirement is too vague.

| Vague Requirement | Fit Criterion |
|-------------------|---------------|
| "The system shall be easy to use" | 80% of new users complete [task] without help within 5 minutes |
| "The system shall be fast" | 95th percentile response time < 500ms for [operation] |
| "The system shall be secure" | All PII encrypted at rest (AES-256) and in transit (TLS 1.2+); passes [standard] audit |
| "The system shall be reliable" | 99.9% uptime measured monthly; MTTR < 4 hours |
