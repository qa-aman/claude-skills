---
name: brd-writer
description: >
  Write a Business Requirements Document. Use when the user says "write a BRD",
  "business requirements", "document the business need", "vision and scope document",
  "business case for this feature", "what does the business need", "strategic requirements",
  "document why we need this" - even if they don't explicitly say "BRD".
---

## Overview

Based on **Software Requirements** by Karl Wiegers & Joy Beatty - the Vision & Scope Document template that separates business objectives from product scope before any solution is discussed. Also draws on the **BABOK Guide v3 (IIBA)** and its BACCM model - 6 core concepts (Change, Need, Solution, Stakeholder, Value, Context) that frame every business analysis effort. The key insight from Wiegers: a BRD is not a feature list. It defines why the organization needs a change and what success looks like, leaving how to the solution team.

## Workflow

### Step 1: Define the business context (BACCM)
Frame the initiative using BABOK's 6 core concepts:
- **Change**: What is changing and why now?
- **Need**: What problem or opportunity exists?
- **Stakeholder**: Who is affected and who decides?
- **Value**: What business value will this deliver?
- **Context**: What constraints, regulations, or dependencies exist?
- **Solution**: What type of solution is envisioned (not the detailed design)?

### Step 2: Write business objectives
Each objective must be measurable. Format:
```
BO-1: [Verb] [measurable outcome] by [timeframe]
Example: Reduce customer onboarding time from 14 days to 3 days by Q4 [year]
```
Link each objective to an organizational goal or KPI.

### Step 3: Identify stakeholders and their needs
For each stakeholder group:
```
STAKEHOLDER: [Role / Group]
NEEDS: [What they need from this initiative]
SUCCESS CRITERIA: [How they will judge success]
CONSTRAINTS: [Limitations they impose]
```

### Step 4: Define the scope boundary
Use Wiegers' scope definition approach:
- **In scope**: Capabilities this initiative will deliver
- **Out of scope**: Explicitly excluded items (prevents scope creep)
- **Assumptions**: What you are taking as given
- **Dependencies**: External factors that must be true

### Step 5: Document constraints and risks
- **Business constraints**: budget, timeline, regulatory deadlines
- **Technical constraints**: existing systems, integration requirements, data limitations
- **Risks**: what could prevent success, with likelihood and impact

### Step 6: Define success criteria
Quantified metrics that determine whether the initiative achieved its objectives:
```
SC-1: [Metric] moves from [current baseline] to [target] within [timeframe]
Measurement method: [how it will be measured]
```

### Step 7: Assemble the BRD
```
# Business Requirements Document: [Initiative Name]
**Version:** [X.X]  **Status:** [Draft / Review / Approved]
**Author:** [your name]  **Date:** [date]

## 1. Business Context (BACCM)
## 2. Business Objectives
## 3. Stakeholders and Needs
## 4. Scope (In / Out / Assumptions / Dependencies)
## 5. Constraints and Risks
## 6. Success Criteria
## 7. Approval and Sign-off
```

## Anti-Patterns

**1. Writing a feature list instead of a BRD**
Bad: "The system shall have a dashboard with charts and filters."
Good: "Operations managers need real-time visibility into order fulfillment to reduce late shipments by 40%."

**2. Unmeasurable business objectives**
Bad: "Improve the customer experience."
Good: "Increase NPS from 32 to 50 within 6 months of launch."

**3. No scope boundary**
Bad: BRD that lists what's included but never says what's excluded.
Good: Explicit "Out of Scope" section that prevents scope creep during delivery.

**4. Stakeholders listed without needs**
Bad: "Stakeholders: Finance, Operations, IT."
Good: Each stakeholder has documented needs, success criteria, and constraints.

## Quality Checklist

- [ ] Business context framed using all 6 BACCM concepts
- [ ] Every business objective is measurable with a target and timeframe
- [ ] All stakeholder groups identified with needs and success criteria
- [ ] Scope has both "in scope" and "out of scope" sections
- [ ] Assumptions and dependencies are explicit
- [ ] Risks documented with likelihood and impact
- [ ] Success criteria are quantified with measurement methods
- [ ] BRD explains "why" without prescribing "how"
