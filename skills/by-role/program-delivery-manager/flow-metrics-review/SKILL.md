---
name: flow-metrics-review
description: >
  Analyze flow metrics to identify delivery bottlenecks and improve throughput. Use
  when the user says "flow metrics", "why is delivery slow", "cycle time analysis",
  "WIP analysis", "throughput review", "what's our lead time", "DORA metrics",
  "where is work getting stuck", "Kanban metrics", or wants to diagnose delivery
  performance using data - even if they don't explicitly say "flow metrics review".
  Based on "Making Work Visible" by Dominica DeGrandis (WIP limits, flow blockers,
  time thieves) and "Accelerate" by Forsgren, Humble & Kim (DORA metrics, delivery
  performance indicators).
---

## Overview

Based on "Making Work Visible" by Dominica DeGrandis and "Accelerate" by Forsgren, Humble & Kim. The core insight from both books: you cannot improve what you cannot see. Flow metrics make the invisible queue visible. DeGrandis identifies five time thieves that destroy flow (too much WIP, unknown dependencies, unplanned work, conflicting priorities, neglected work). Accelerate adds four DORA metrics that distinguish high-performing from low-performing delivery organizations. Together, these give a complete picture of where work is slowing down and why.

## Workflow

### Step 1: Identify available data
Ask the user what metrics data they have access to. Common sources:
- Jira / Linear / GitHub: cycle time, lead time, WIP count, throughput
- DORA dashboard or CI/CD pipeline: deployment frequency, change failure rate, MTTR
- Manual export or spreadsheet

Minimum viable dataset for this review:
- Cycle time (time from "in progress" to "done") for the last 10-20 items
- Current WIP count (items actively being worked on)
- Throughput (items completed per sprint or week)

If the user has no data, recommend: "Start by instrumenting your board. At minimum, track when each item moves to 'in progress' and 'done'. After 2-3 sprints you will have enough data for a meaningful review."

### Step 2: Benchmark against DORA performance levels
If deployment/delivery frequency data is available, map to DORA tiers:

| Metric | Elite | High | Medium | Low |
|--------|-------|------|--------|-----|
| Deployment frequency | Multiple/day | 1/week-1/day | 1/month-1/week | < 1/month |
| Lead time for changes | < 1 hour | 1 day-1 week | 1 week-1 month | > 1 month |
| Change failure rate | 0-5% | 5-10% | 10-15% | > 15% |
| MTTR (mean time to restore) | < 1 hour | < 1 day | 1 day-1 week | > 1 week |

State clearly which tier the team is in and what the next tier requires.

### Step 3: Analyze the five time thieves (DeGrandis)
For each thief, ask the user targeted questions and assess its presence:

**Thief 1: Too much WIP**
- How many items are "in progress" right now?
- WIP limit rule of thumb: WIP should not exceed 1.5x the number of people on the team. If a team of 6 has 15 items in progress, WIP is too high.
- Signal: cycle time is long but throughput is low. Items are waiting more than they are being worked on.

**Thief 2: Unknown dependencies**
- Are any in-progress items waiting on another team, system, or approval?
- Count the number of items with "waiting" or "blocked" tags.
- Signal: items spend time in in-progress state without moving, but the team is not idle.

**Thief 3: Unplanned work**
- What percentage of completed work in the last sprint was unplanned (bugs, incidents, ad-hoc requests)?
- Signal: planned throughput is consistently lower than expected. Team appears busy but planned features are not shipping.

**Thief 4: Conflicting priorities**
- Are team members pulled between multiple products, programs, or workstreams?
- Does the team have a single prioritized backlog or multiple competing queues?
- Signal: context switching - items start, pause, restart. High WIP but low flow.

**Thief 5: Neglected work**
- Are there items that have been "in progress" for more than 2x the average cycle time?
- These are the silent queue - work that is started but not finishing.
- Signal: aging items. Run an aging report (how long each item has been in its current state).

### Step 4: Calculate key flow metrics
Using the data the user provides:

**Cycle time** = average time from "in progress" to "done"
- Calculate average, p50 (median), and p85 (85th percentile)
- p85 is your service level agreement - 85% of items complete within this time
- A healthy cycle time has low variance. High variance means unpredictable delivery.

**Throughput** = items completed per sprint or week
- Calculate average throughput over the last 4-6 sprints
- Throughput trend: increasing, stable, or declining?

**WIP age distribution**
- How many items have been in progress 0-3 days / 4-7 days / 8-14 days / 14+ days?
- Items in the 14+ day bucket are flow blockers requiring immediate attention.

**Flow efficiency** (if data allows)
- Flow efficiency = active work time / total cycle time
- Industry average is 15-40%. Below 15% means the work is waiting more than it is being worked on.

### Step 5: Generate the flow metrics report
```
FLOW METRICS REVIEW - [your team/program]
Period: [date range]
Data source: [Jira / Linear / manual]

DORA PERFORMANCE TIER: [Elite / High / Medium / Low]
- Deployment frequency: [value] ([tier])
- Lead time: [value] ([tier])
- Change failure rate: [value] ([tier])
- MTTR: [value] ([tier])

FLOW HEALTH SUMMARY
Cycle time (p50): [N] days
Cycle time (p85): [N] days  <- your de facto SLA
Throughput: [N] items/sprint (trend: [up/stable/down])
Current WIP: [N] items (team size: [N], recommended max: [1.5x team size])
Flow efficiency: [N]% [if calculable]

TIME THIEF ANALYSIS
[Thief]: [Present / Not detected] - [1-sentence evidence]
[Thief]: [Present / Not detected] - [1-sentence evidence]
[Thief]: [Present / Not detected] - [1-sentence evidence]
[Thief]: [Present / Not detected] - [1-sentence evidence]
[Thief]: [Present / Not detected] - [1-sentence evidence]

TOP 3 BOTTLENECKS
1. [Bottleneck]: [evidence] - Recommended action: [specific action]
2. [Bottleneck]: [evidence] - Recommended action: [specific action]
3. [Bottleneck]: [evidence] - Recommended action: [specific action]

RECOMMENDED EXPERIMENTS (pick one to try next sprint)
- [Specific change]: expected impact on [metric]
```

### Step 6: Recommend one experiment
Do not give a list of 10 improvements. Pick one experiment based on the biggest bottleneck identified. Format:

```
EXPERIMENT: [name]
Hypothesis: If we [action], then [metric] will improve by [amount] because [reasoning].
How to measure: Track [metric] before and after for [N] sprints.
Owner: [name]
Start: [date]
Review: [date]
```

## Anti-Patterns

**1. Reporting metrics without interpreting them**
Bad: "Cycle time is 8.3 days."
Good: "Cycle time is 8.3 days (p85: 14 days). The spread between p50 and p85 is high - it signals that a subset of items are regularly getting stuck. Likely cause: unknown dependencies."

**2. Focusing on velocity instead of flow**
Bad: "Our velocity dropped from 42 to 38 story points this sprint."
Good: Velocity measures effort, not flow. Cycle time and throughput measure whether work is actually moving. Use flow metrics to diagnose, velocity to plan.

**3. Too many WIP items treated as a productivity signal**
Bad: "The team has 18 items in progress - they are really busy."
Good: 18 items in progress for a team of 8 is 2.25x the recommended limit. High WIP is the cause of slow cycle time, not a sign of productivity.

**4. Ignoring aging work**
Bad: Status report that only shows items completed this sprint.
Good: Flag any item that has been in-progress for more than 2x the average cycle time. These are hidden blockers.

**5. Recommending many improvements at once**
Bad: 8-point action plan to improve flow.
Good: One focused experiment. Changing too many variables at once makes it impossible to know what worked.

## Quality Checklist

- [ ] DORA tier is assessed for all four metrics (or gaps noted)
- [ ] All five time thieves are assessed - presence or absence stated with evidence
- [ ] Cycle time is reported as p50 and p85, not just average
- [ ] WIP count is compared to team size (1.5x rule)
- [ ] Aging items (14+ days in-progress) are called out specifically
- [ ] One specific experiment is recommended with a hypothesis and measurement plan
- [ ] Report distinguishes diagnosis (what the data shows) from prescription (what to do)
