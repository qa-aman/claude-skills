---
name: delivery-risk-review
description: >
  Identify, score, and mitigate delivery risks for a program or release. Use when
  the user says "risk review", "what could go wrong", "risk register", "delivery
  risks for this release", "program risk assessment", "identify blockers before they
  hit", or wants to pressure-test a plan before committing - even if they don't say
  "risk review". Based on "The Phoenix Project" by Kim, Behr & Spafford (unplanned
  work, fragile systems, single points of failure) and "The Art of Project
  Management" by Scott Berkun (scoping risk, milestone pressure, hidden assumptions).
---

## Overview

Based on "The Phoenix Project" (Kim, Behr & Spafford) and "The Art of Project Management" (Scott Berkun). The core insight from Phoenix Project: most delivery failures are not surprise events - they are predictable patterns (unplanned work, single points of failure, technical debt accumulation) that were visible before the crisis but ignored. A risk review forces you to name these patterns before they explode. Berkun adds: the highest-risk part of any project is not the work - it is the assumptions baked into the plan.

## Workflow

### Step 1: Gather program context
Ask the user for:
- Program/release name and target date
- Team size and structure (how many teams, any new team members?)
- Key dependencies (external vendors, other teams, regulatory approvals)
- Known hotspots (legacy systems, areas of high technical debt, frequently changed code)

### Step 2: Run the risk identification sweep
Work through five risk categories (drawn from Phoenix Project patterns and Berkun's scoping risk model):

**Category 1: Unplanned Work Risk**
Questions to surface:
- What percentage of past sprint capacity went to unplanned work (bugs, incidents, support)?
- Are there any live production incidents or instability issues currently?
- Is the team on an on-call rotation that competes with feature delivery?

Phoenix Project signal: if unplanned work consumed > 20% of capacity in recent sprints, it will consume more during the release crunch.

**Category 2: Dependency Risk**
Questions to surface:
- Are there external teams or vendors whose deliverables are on your critical path?
- Have any dependencies been verbally confirmed but not formally committed?
- Is there a shared resource (DBA, security review, legal) that serves multiple teams?

**Category 3: Scope Risk**
Questions to surface:
- Has the scope changed since the release was planned?
- Are there features with open design questions or unsettled technical approach?
- Are any P0 items estimated with low confidence?

Berkun signal: any feature where the team has not done this type of work before carries a 2x estimation risk.

**Category 4: People Risk**
Questions to surface:
- Is any critical knowledge concentrated in one person (single point of failure)?
- Are there planned vacations, hiring gaps, or new team members ramping up during the release window?
- Is team morale or engagement a concern?

**Category 5: Technical Risk**
Questions to surface:
- Is the release touching legacy systems, high-complexity code, or areas with low test coverage?
- Are there infrastructure changes (migrations, new services, third-party integrations) in scope?
- Has this area of the codebase caused incidents in the past 90 days?

### Step 3: Score each risk
For each identified risk, assign:
- **Likelihood**: Low (unlikely in this release) / Med (has happened before) / High (currently happening or happened in last release)
- **Impact**: Low (minor delay, < 1 sprint) / Med (1-2 sprint delay or scope cut) / High (release date at risk or launch criteria not met)
- **Priority**: High × High = P0 (escalate now), else use the matrix below

```
           | Impact Low | Impact Med | Impact High
-----------|------------|------------|------------
Likelihood High | P2 | P1 | P0
Likelihood Med  | P3 | P2 | P1
Likelihood Low  | P3 | P3 | P2
```

### Step 4: Generate the risk register
```
DELIVERY RISK REGISTER - [your program] - [date]
=================================================

P0 - ESCALATE NOW
| # | Risk | Category | Likelihood | Impact | Owner | Mitigation | Due |
|---|------|----------|-----------|--------|-------|------------|-----|
| 1 | [risk description] | [type] | High | High | [name] | [action] | [date] |

P1 - MONITOR WEEKLY
[same format]

P2/P3 - TRACK AND ACCEPT
[same format]
```

### Step 5: Write mitigations (not just monitoring)
For each P0 and P1 risk, the mitigation must be one of:
- **Avoid**: change the plan to eliminate the risk (re-sequence, reduce scope)
- **Transfer**: make it someone else's problem with a formal commitment (SLA, contract, escalation to leadership)
- **Reduce**: take specific action to lower likelihood or impact (add test coverage, cross-train a second engineer, get written confirmation from vendor)
- **Accept**: explicitly acknowledge it and define the trigger that would escalate it

"We'll keep an eye on it" is not a mitigation. Name the action, the owner, and the date.

### Step 6: Set risk review cadence
Recommend a standing cadence based on program phase:
- More than 6 weeks from release: review risk register every 2 weeks
- 3-6 weeks from release: weekly review, P0 risks reviewed in every program sync
- Less than 3 weeks from release: daily standup includes P0 risk status

## Anti-Patterns

**1. Identifying risks without owners**
Bad: "Technical debt in the auth service is a risk."
Good: "[Name] will assess auth service test coverage by [date] and recommend if it needs a dedicated spike."

**2. Only listing obvious risks**
Bad: Risk register with "API might be slow" and "team might be busy."
Good: Surface non-obvious risks: knowledge concentration, unplanned work patterns, verbally-confirmed-but-not-written dependencies.

**3. All risks rated the same**
Bad: 15 risks all rated "medium."
Good: Force a distribution. If everything is medium, you have not done the analysis.

**4. Risk review as a one-time event**
Bad: Risk register created at kickoff, never updated.
Good: Risk register is a living document. Reviewed at program sync, statuses updated weekly.

**5. Mitigation = monitoring**
Bad: "We will watch this closely."
Good: A specific action that reduces likelihood or impact, with a named owner and due date.

## Quality Checklist

- [ ] All five risk categories are covered (unplanned work, dependency, scope, people, technical)
- [ ] Every risk has a likelihood, impact, and priority score
- [ ] P0 and P1 risks each have a named owner and specific mitigation action
- [ ] Mitigation is one of: avoid / transfer / reduce / accept - not "monitor"
- [ ] Risk review cadence is set and scheduled
- [ ] Register is scoped to program-level risks, not every possible task failure
