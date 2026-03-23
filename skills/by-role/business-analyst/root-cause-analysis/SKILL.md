---
name: root-cause-analysis
description: >
  Find the root cause of a problem, not just symptoms. Use when the user says "root cause",
  "why does this keep happening", "5 whys", "fishbone diagram", "cause analysis",
  "problem investigation", "defect analysis", "incident analysis", "A3 problem solving",
  "what's causing this", "ishikawa" - even if they don't explicitly say "root cause analysis".
---

## Reference Files

- `references/fishbone-categories.md` - Six fishbone categories adapted for BA context (People, Process, Technology, Policy, Environment, Data) with example causes for each. Read this in Step 4 when building the Ishikawa diagram.

## Overview

Based on **Business Process Change** by Paul Harmon - integrating Six Sigma DMAIC root cause methodology into business process improvement. Also draws on **Lean Business Analysis** by Mark Sherrington for the A3 Problem Solving technique - a one-page structured format that forces clarity by constraining the entire analysis to a single sheet. The key insight: most "root causes" identified in practice are actually symptoms. True root cause analysis requires asking "why" until you reach a systemic cause you can change - something in the process, policy, or system design, never an individual person.

## Workflow

### Step 1: Write the problem statement
Be specific and measurable. A good problem statement answers: what, where, when, and how much.
```
BAD:  "The system is slow."
GOOD: "Order processing takes 4.2 hours on average, exceeding the 2-hour SLA.
       This has occurred for 67% of orders in the past 30 days, primarily
       affecting [region/segment]. Impact: $[X] in late delivery penalties."
```

### Step 2: Gather data
Before hypothesizing causes, collect evidence:
- Timeline of when the problem started and any changes that preceded it
- Frequency and pattern (constant, intermittent, time-based, load-based)
- Scope of impact (which users, processes, or systems are affected)
- Prior attempts to fix and their outcomes

### Step 3: Run 5 Whys analysis
Start with the problem statement and ask "why" iteratively:
```
Problem: Order processing exceeds 2-hour SLA
Why 1?  Manual validation step takes 90 minutes
Why 2?  Validator must cross-reference 3 systems manually
Why 3?  Systems don't share a common order ID
Why 4?  Each system was built independently without integration design
Why 5?  No enterprise data architecture was defined when systems were procured
ROOT CAUSE: Absence of enterprise data architecture standards for procurement
```

Rules for 5 Whys:
- Branch when multiple causes exist at a level
- Stop when you reach a cause that is systemic and actionable
- If a "why" answer is a person's name, go deeper - root causes are systemic

### Step 4: Build a Fishbone (Ishikawa) diagram
Use 6 BA-specific categories (see `references/fishbone-categories.md`):
- **People**: skills, capacity, roles, communication
- **Process**: steps, handoffs, bottlenecks, documentation
- **Technology**: systems, integrations, performance, functionality
- **Policy**: rules, approvals, compliance, SLAs
- **Environment**: organizational context, budget, competing priorities
- **Data**: quality, availability, accuracy, access

Place the problem at the head. Add potential causes along each bone. Circle the causes that appear across multiple categories - these are systemic.

### Step 5: Apply Pareto analysis
Rank causes by frequency or impact. The 80/20 rule: typically 20% of causes drive 80% of the problem. Focus countermeasures on the vital few, not the trivial many.

### Step 6: Validate the root cause
Before declaring a root cause, test it:
- Can you reproduce the problem by triggering this cause?
- Does removing this cause prevent recurrence?
- Does the causal chain from root to symptom hold under scrutiny?
- Is this cause actionable (you can change it)?

### Step 7: Document using A3 format
```
| A3 Section | Content |
|------------|---------|
| Background | Why this problem matters |
| Current Condition | Problem statement with data |
| Goal | Target state after fix |
| Root Cause Analysis | 5 Whys + Fishbone summary |
| Countermeasures | Actions to address root cause |
| Implementation Plan | Who, what, when |
| Follow-up | How to verify the fix worked |
| Expected Results | Measurable improvement target |
```

## Anti-Patterns

**1. Stopping at symptoms**
Bad: "Users didn't follow the process." (Why didn't they? That's a symptom.)
Good: "The process requires 12 steps across 3 systems with no integrated view, so users created workarounds."

**2. Root cause is a person's name**
Bad: "John made an error."
Good: "The process has no validation check at step 5, allowing data entry errors to propagate."

**3. 5 Whys that go in circles**
Bad: Why? Because X. Why X? Because Y. Why Y? Because X again.
Good: If you loop back, you've missed a branch. Split and explore both causal paths.

**4. Fishbone with only technology causes**
Bad: All causes listed under "Technology" - ignoring process, people, and policy.
Good: Populate at least 4 of the 6 categories before concluding.

**5. No validation of the root cause**
Bad: "We think the root cause is X, so let's fix it."
Good: Test the hypothesis - can you reproduce the problem? Does the fix address it?

## Quality Checklist

- [ ] Problem statement is specific, measurable, and time-bounded
- [ ] Data gathered before hypothesizing (not after)
- [ ] 5 Whys reaches a systemic cause (not an individual)
- [ ] Fishbone covers at least 4 of 6 categories
- [ ] Pareto analysis identifies the vital few causes
- [ ] Root cause is validated (reproducible, removable, actionable)
- [ ] Countermeasures address root cause, not symptoms
- [ ] A3 document is complete with follow-up plan and expected results
