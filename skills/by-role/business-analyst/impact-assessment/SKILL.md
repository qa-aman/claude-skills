---
name: impact-assessment
description: >
  Assess business impact of a proposed change. Use when the user says "impact assessment",
  "impact analysis", "what will this change affect", "change impact", "who is impacted",
  "ripple effects", "downstream impact", "impact mapping", "what breaks if we change this",
  "readiness for change" - even if they don't explicitly say "impact assessment".
---

## Overview

Based on **The Business Analysis Handbook** by Helen Winter - the Impact Mapping framework (Goal to Actors to Impacts to Deliverables) that connects every change to measurable outcomes. Also draws on **Requirements Engineering** by Hull, Jackson, and Dick for Change Impact Analysis methodology, and **Business Process Change** by Paul Harmon for process change impact assessment across Rummler-Brache's 3 levels. The key insight from Winter: impact assessment is not about listing what changes. It is about tracing the chain from a proposed change through every actor it touches, every process it disrupts, and every system it modifies - then quantifying the disruption.

## Workflow

### Step 1: Define the proposed change
```
CHANGE: [What is being proposed]
TRIGGER: [Why this change is happening - business driver, regulation, incident]
SCOPE: [What areas, systems, or processes are affected]
TIMELINE: [When the change will occur]
```

### Step 2: Build the Impact Map (Winter's framework)
Trace the chain:
```
GOAL: [Business objective this change serves]
  |
  --> ACTOR: [Who is affected?]
        |
        --> IMPACT: [How does this change their work?]
              |
              --> DELIVERABLE: [What must be built/changed to enable this?]
```

Example:
```
GOAL: Reduce order processing time by 50%
  --> ACTOR: Warehouse staff
        --> IMPACT: Manual pick list replaced by automated routing
              --> DELIVERABLE: Warehouse management system integration
  --> ACTOR: Customer service team
        --> IMPACT: Fewer "where is my order" calls
              --> DELIVERABLE: Real-time tracking dashboard
```

### Step 3: Assess impact across 4 dimensions
For each affected area:

| Dimension | Questions to Answer |
|-----------|-------------------|
| **People** | Who needs retraining? New roles created/eliminated? Resistance expected? |
| **Process** | Which processes change? New handoffs? Steps added/removed? |
| **Technology** | Which systems modified? Integrations affected? Data migration needed? |
| **Policy** | Which policies need updating? Compliance implications? Approval changes? |

### Step 4: Score impact severity
For each impact:
```
| Impact | Severity | Likelihood | Score | Mitigation |
|--------|----------|------------|-------|------------|
| [description] | High/Med/Low | High/Med/Low | [SxL] | [action to reduce] |
```

Severity scale:
- **High**: Stops work, regulatory risk, data loss, or affects > 50% of users
- **Medium**: Degrades performance, requires workaround, affects 10-50% of users
- **Low**: Minor inconvenience, affects < 10% of users

### Step 5: Map dependencies
Identify what must happen in what order:
- Which impacts are prerequisites for others?
- Which systems must be changed before others?
- What is the critical path?
- What can be done in parallel?

### Step 6: Assess change readiness
For each affected group:
```
GROUP: [team or role]
AWARENESS: [Do they know the change is coming?] High/Med/Low
DESIRE: [Do they want the change?] High/Med/Low
KNOWLEDGE: [Do they know how to work in the new way?] High/Med/Low
ABILITY: [Can they actually do it?] High/Med/Low
REINFORCEMENT: [Will the change stick?] High/Med/Low
READINESS: [Overall assessment and actions needed]
```

### Step 7: Output the impact assessment
```
# Impact Assessment: [Change Name]

## 1. Change Definition
## 2. Impact Map (Goal -> Actors -> Impacts -> Deliverables)
## 3. 4-Dimension Impact Table (People, Process, Technology, Policy)
## 4. Severity Scoring and Mitigation
## 5. Dependency Map
## 6. Change Readiness Assessment
## 7. Recommended Sequencing
```

## Anti-Patterns

**1. Only assessing technology impact**
Bad: "We need to update the database schema and deploy a new API endpoint."
Good: Also assess: who needs retraining, which processes change, which policies need updating.

**2. Impact without severity scoring**
Bad: A flat list of 20 impacts with no ranking.
Good: Each impact scored by severity x likelihood; high-score items get mitigation plans.

**3. Missing downstream effects**
Bad: Assessing only the team making the change.
Good: Trace through Impact Map to find second and third-order effects on downstream actors.

**4. No change readiness assessment**
Bad: Assuming people will adopt the change because it was communicated.
Good: Assess awareness, desire, knowledge, ability, and reinforcement for each affected group.

## Quality Checklist

- [ ] Change definition includes trigger, scope, and timeline
- [ ] Impact Map traces Goal to Actors to Impacts to Deliverables
- [ ] All 4 dimensions assessed (People, Process, Technology, Policy)
- [ ] Each impact scored by severity and likelihood
- [ ] High-severity impacts have mitigation plans
- [ ] Dependencies mapped with critical path identified
- [ ] Change readiness assessed for each affected group
- [ ] Recommended sequencing accounts for dependencies and readiness
