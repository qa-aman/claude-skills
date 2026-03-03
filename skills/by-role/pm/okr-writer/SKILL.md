---
name: okr-writer
description: >
  Write OKRs (Objectives and Key Results). Use when the user says "write OKRs",
  "help me set goals", "create objectives and key results", "quarterly goals",
  "team OKRs", "I need to define success for this quarter", or wants to translate
  a strategic direction into measurable targets - even if they don't say "OKRs".
---

## Overview

An Objective answers "where do we want to go?" It is aspirational and qualitative. Key Results answer "how will we know we got there?" They are measurable and binary at quarter end - either you hit them or you didn't.

Bad OKRs are activity-based ("launch feature X"). Good OKRs are outcome-based ("reduce churn by 15%").

## Workflow

### Step 1: Extract the strategic intent
Ask or infer: what is the team trying to achieve this quarter? What problem are they solving or opportunity are they capturing?

### Step 2: Write the Objective
- 1 sentence, aspirational, qualitative
- Should be memorable and motivating
- Answers: "what do we want to be true at the end of the quarter?"

Example: "Become the fastest onboarding experience in [your industry]."

### Step 3: Write 3-5 Key Results per Objective
Each KR must:
- Be measurable with a specific number
- Be outcome-based, not task-based
- Be achievable but ambitious (70% confidence is ideal)
- Have a clear baseline and target

Format: `[Metric] from [baseline] to [target] by [date]`

Example:
- Reduce time-to-first-value from 14 days to 3 days
- Increase onboarding completion rate from 45% to 70%
- Decrease onboarding support tickets by 50%

### Step 4: Check alignment
Do the KRs actually measure the Objective? If all KRs are hit but the Objective still feels unachieved, the KRs are wrong.

### Step 5: Flag missing baselines
If the user doesn't know current metrics, flag this: "You'll need a baseline for this KR before you can track it. Who owns this data?"

## Anti-Patterns

**1. Activity-based Key Results**
Bad: "Launch new onboarding flow by March 31"
Good: "Increase onboarding completion rate from 45% to 70%"
Shipping is not success. Outcomes are success.

**2. Too many Objectives**
Bad: 5+ Objectives per team per quarter.
Good: 1-3 Objectives. Focus is the point of OKRs.

**3. KRs that are always 100% achievable**
Bad: "Maintain NPS above 40" when NPS is already 55.
Good: KRs should have ~70% confidence. Too easy means no stretch; too hard means teams game the system.

**4. No baseline**
Bad: "Improve conversion rate to 10%"
Good: "Improve conversion rate from 6% to 10%"
Without a baseline, you can't measure progress or claim success.

## Quality Checklist

- [ ] Objective is aspirational and qualitative (not a task)
- [ ] 3-5 Key Results per Objective
- [ ] Each KR is measurable with a specific number
- [ ] Each KR has a baseline and a target
- [ ] KRs are outcome-based, not output-based
- [ ] No more than 3 Objectives per team
- [ ] Missing baselines are flagged with owners
