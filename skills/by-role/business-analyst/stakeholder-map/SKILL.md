---
name: stakeholder-map
description: >
  Map stakeholders by influence, interest, and communication needs. Use when the user says
  "stakeholder analysis", "stakeholder map", "power interest grid", "who are the stakeholders",
  "RACI matrix", "stakeholder engagement plan", "who needs to be involved",
  "communication plan for stakeholders", "influence mapping" - even if they don't explicitly
  say "stakeholder map".
---

## Reference Files

- `references/stakeholder-strategies.md` - Engagement strategy lookup for each Power/Interest Grid quadrant: communication frequency, channels, typical concerns, and engagement actions. Read this in Step 4 when building the engagement plan.

## Overview

Based on **Business Analysis Techniques** by James Cadle, Debra Paul, and Paul Turner - the Power/Interest Grid, Stakeholder Wheel, and Onion Model for systematically classifying stakeholders. Also draws on **The Business Analysis Handbook** by Helen Winter for Stakeholder Engagement Planning with influence strategies per stakeholder type. The key insight from Cadle: stakeholder mapping is not a list of names. It is a strategic tool that determines who to engage, how deeply, and how often. Misclassifying a high-power stakeholder as low-interest guarantees project risk.

## Workflow

### Step 1: Identify all stakeholders
Cast a wide net using BABOK's categories:
- **Sponsor**: Funds and champions the initiative
- **End users**: People who will use the solution daily
- **Domain experts**: Subject matter experts with deep knowledge
- **Regulators**: External bodies with compliance authority
- **Implementation team**: Developers, testers, operations
- **Affected parties**: People whose work changes even if they don't use the system

Also use the Onion Model - concentric rings from solution outward:
- Ring 1: The solution itself
- Ring 2: The system (users and operators)
- Ring 3: The containing organization
- Ring 4: External environment (regulators, partners, customers)

### Step 2: Classify using the Power/Interest Grid
Place each stakeholder on the 2x2 matrix:
```
                    HIGH INTEREST
                    |
    Keep Satisfied  |  Manage Closely
    (High Power,    |  (High Power,
     Low Interest)  |   High Interest)
                    |
--------------------+--------------------
                    |
    Monitor         |  Keep Informed
    (Low Power,     |  (Low Power,
     Low Interest)  |   High Interest)
                    |
                    LOW INTEREST
    LOW POWER                    HIGH POWER
```

### Step 3: Build the RACI matrix
For key decisions and deliverables, assign:
- **R** - Responsible: Does the work
- **A** - Accountable: Has final authority (exactly one per item)
- **C** - Consulted: Provides input before the decision
- **I** - Informed: Told after the decision

```
| Decision/Deliverable | [Stakeholder 1] | [Stakeholder 2] | [Stakeholder 3] |
|----------------------|-----------------|-----------------|-----------------|
| Requirements sign-off | C | A | I |
| Solution design | R | C | I |
| UAT approval | I | A | R |
```

### Step 4: Create the engagement plan
For each stakeholder (see `references/stakeholder-strategies.md`):
```
STAKEHOLDER: [name / role]
QUADRANT: [Manage Closely / Keep Satisfied / Keep Informed / Monitor]
COMMUNICATION: [frequency and channel]
KEY CONCERNS: [what they care about most]
ENGAGEMENT ACTION: [specific actions to maintain their support]
RISK IF NEGLECTED: [what happens if we don't engage them properly]
```

### Step 5: Identify influence dynamics
Map who influences whom:
- Who can block the project?
- Who can champion it to others?
- Where are there conflicts between stakeholders?
- Who is a hidden influencer (low formal power but high informal influence)?

### Step 6: Output the stakeholder map
Deliver: Power/Interest Grid visual, RACI matrix, engagement plan table, and a stakeholder register with all fields populated.

## Anti-Patterns

**1. List of names instead of a map**
Bad: "Stakeholders: CEO, CTO, Product Manager, Users."
Good: Each stakeholder classified by power, interest, RACI role, and engagement strategy.

**2. Ignoring low-power, high-interest stakeholders**
Bad: Only engaging executives and ignoring end users.
Good: End users are in "Keep Informed" - they may lack decision power but their adoption determines success.

**3. Multiple Accountable people in RACI**
Bad: Two people marked as "A" for the same decision.
Good: Exactly one Accountable person per row. If unclear, that's a governance gap to resolve.

**4. Static stakeholder map**
Bad: Creating the map once at project start and never updating it.
Good: Review and update the map at each phase boundary - stakeholder power and interest shift over time.

**5. No engagement strategy - just classification**
Bad: Power/Interest Grid with no action plan.
Good: Each quadrant drives a specific engagement frequency, channel, and approach.

## Quality Checklist

- [ ] All stakeholder categories covered (sponsors, users, domain experts, regulators, implementers, affected parties)
- [ ] Onion Model used to check for missed external stakeholders
- [ ] Every stakeholder placed on the Power/Interest Grid
- [ ] RACI matrix has exactly one "A" per row
- [ ] Engagement plan defines frequency, channel, and approach per stakeholder
- [ ] Hidden influencers identified
- [ ] Conflicts between stakeholders flagged
- [ ] Risk of neglect documented for key stakeholders
