---
name: gap-analysis
description: >
  Identify gaps between current and desired state. Use when the user says "gap analysis",
  "what's missing", "current vs future state", "where are the gaps", "capability gap",
  "maturity assessment", "fit-gap analysis", "what needs to change", "compare current to target",
  "readiness assessment" - even if they don't explicitly say "gap analysis".
---

## Overview

Based on the **BABOK Guide v3 (IIBA)** - Strategy Analysis knowledge area, which defines gap analysis as the comparison between current state and desired future state to identify changes needed. Also draws on **Mastering the Requirements Process** by Suzanne & James Robertson for the Brown Cow Model - a 2x2 matrix (What/How x Now/Future) that prevents teams from jumping to solutions before understanding the problem space. The key insight: gap analysis must cover all four quadrants of the Brown Cow Model. Teams that skip "What-Now" (current business requirements) and jump straight to "How-Future" (new system design) build the wrong thing.

## Workflow

### Step 1: Define the desired future state
Document what success looks like using measurable targets:
```
FUTURE STATE OBJECTIVE: [what capability or performance level is needed]
BUSINESS DRIVER: [why this change is needed now]
SUCCESS METRIC: [how we will know we've arrived]
TARGET DATE: [when this must be achieved]
```

### Step 2: Document the current state using Brown Cow Model
Map all four quadrants:
```
|           | WHAT (requirements)        | HOW (implementation)         |
|-----------|----------------------------|------------------------------|
| NOW       | Current business needs     | Current systems & processes  |
| FUTURE    | Future business needs      | Future systems & processes   |
```
- **What-Now**: What does the business need today? (Often undocumented)
- **How-Now**: How is it currently delivered? (Systems, processes, people)
- **What-Future**: What will the business need? (New requirements)
- **How-Future**: How should it be delivered? (Design this last, not first)

### Step 3: Identify gaps across 4 dimensions
For each dimension, compare current to desired:

| Dimension | Current State | Desired State | Gap |
|-----------|--------------|---------------|-----|
| **Process** | [how work flows today] | [how it should flow] | [what's missing or broken] |
| **Technology** | [current systems] | [needed capabilities] | [what's missing or inadequate] |
| **People** | [current skills/capacity] | [needed skills/capacity] | [training, hiring, restructuring] |
| **Policy** | [current rules/governance] | [needed rules/governance] | [policy changes required] |

### Step 4: Categorize each gap
- **Missing capability**: Does not exist today, must be built or acquired
- **Underperforming capability**: Exists but doesn't meet the target
- **Unnecessary capability**: Exists but is not needed in the future state (candidate for removal)

### Step 5: Prioritize gaps using Force-Field Analysis
For each gap, assess:
- **Driving forces**: factors pushing toward closing the gap (business need, regulation, competition)
- **Restraining forces**: factors resisting change (cost, complexity, organizational resistance)
- **Net priority**: driving forces minus restraining forces

Rank gaps by net priority to determine which to address first.

### Step 6: Recommend actions
For each gap:
```
GAP: [description]
SEVERITY: [High / Medium / Low]
ACTION: [Build / Buy / Partner / Defer / Accept]
OWNER: [who is responsible]
EFFORT: [estimated complexity]
DEPENDENCIES: [what must happen first]
```

### Step 7: Output the gap register
Deliver a consolidated gap register with all gaps, their categorization, priority, and recommended actions. Include the Brown Cow Model diagram and Force-Field Analysis summary.

## Anti-Patterns

**1. Jumping to solutions before documenting current state**
Bad: "We need a new CRM system." (Without analyzing what the current state is or what specific gaps exist.)
Good: Document What-Now and How-Now first, then identify specific gaps, then evaluate solutions.

**2. Only identifying technology gaps**
Bad: Gap analysis that lists missing software features but ignores process, people, and policy.
Good: Cover all 4 dimensions - often the biggest gaps are in process and people, not technology.

**3. No prioritization - all gaps treated equally**
Bad: A flat list of 30 gaps with no ranking.
Good: Force-Field Analysis or severity scoring to identify the vital few gaps that matter most.

**4. Vague gap descriptions**
Bad: "Improve reporting capabilities."
Good: "Current reporting requires 4 hours of manual Excel compilation; future state requires automated dashboards refreshed every 15 minutes."

**5. Future state without success metrics**
Bad: "We want to be best in class."
Good: "Reduce order fulfillment cycle time from 5 days to 1 day, measured by average across all orders."

## Quality Checklist

- [ ] Future state has measurable targets with deadlines
- [ ] Current state documented with evidence (not assumed)
- [ ] Brown Cow Model completed (all 4 quadrants)
- [ ] All 4 dimensions covered (Process, Technology, People, Policy)
- [ ] Each gap categorized (missing / underperforming / unnecessary)
- [ ] Gaps prioritized using Force-Field Analysis or severity scoring
- [ ] Each gap has an owner and recommended action
- [ ] Recommendations are actionable (Build / Buy / Partner / Defer / Accept)
- [ ] Dependencies between gaps identified
