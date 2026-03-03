---
name: release-planning
description: >
  Build a velocity-based release roadmap with risk buffers. Use when the user says
  "release plan", "when will we ship", "plan the next release", "map sprints to
  milestones", "estimate our release date", "how many sprints until done", or wants
  to translate a backlog into a delivery timeline - even if they don't say "release
  planning". Based on "Agile Estimating and Planning" by Mike Cohn (velocity,
  story points, cone of uncertainty, risk buffers).
---

## Overview

Based on "Agile Estimating and Planning" by Mike Cohn. The core insight: release dates are not commitments - they are probabilistic forecasts. Velocity is a lagging indicator that gets more reliable over time (the cone of uncertainty narrows). A good release plan gives a date range, not a single date, and explicitly buffers for unknowns. Single-date commitments made from a backlog on day one are fiction.

## Workflow

### Step 1: Establish velocity baseline
Ask the user for sprint velocity data. You need at least 3 sprints of history for a meaningful average.

```
Sprint | Story Points Completed
-------|----------------------
S-1    | [number]
S-2    | [number]
S-3    | [number]
```

Calculate:
- **Average velocity**: sum / number of sprints
- **Velocity range**: min to max (this defines your planning range)

If no historical data exists, flag this: "No velocity history means your first release plan has a high cone of uncertainty. Revisit after 2-3 sprints."

### Step 2: Size the remaining backlog
Ask for the current backlog in story points. If the backlog is not estimated, do not attempt to generate a plan - ask the user to size the top items first.

Group the backlog:
- **Must have** (P0): work required for the release to ship
- **Should have** (P1): high-value, included if time permits
- **Nice to have** (P2): deferred if velocity is lower than expected

### Step 3: Calculate the release forecast

Using the velocity range from Step 1:

```
Optimistic date:  P0 points / max velocity = [N] sprints
Realistic date:   P0 points / avg velocity = [N] sprints
Conservative date: (P0 + P1 points) / min velocity = [N] sprints
```

Convert sprints to calendar dates using sprint length (ask user: 1-week, 2-week, or 3-week sprints?).

Output format:
```
RELEASE FORECAST - [your program]
==================================
Optimistic:   Ship by [date] (P0 scope only, best-case velocity)
Realistic:    Ship by [date] (P0 scope, average velocity)
Conservative: Ship by [date] (P0+P1 scope, worst-case velocity)

Recommended commitment: [realistic date] with [conservative date] as contingency
```

### Step 4: Apply risk buffers
Cohn's rule: buffer 20% for unknowns if the team is mature and the codebase is known. Buffer up to 50% for:
- New team (< 3 sprints together)
- Greenfield build with no precedent
- External dependencies not yet confirmed
- Compliance, security, or legal review required

Add the buffer to the realistic estimate:
```
Buffered release date = realistic date + (realistic duration × buffer %)
```

Explicitly state what the buffer covers:
- "[X]% buffer for [integration risk with third-party API / new team ramp-up / unknown legacy behavior]"

### Step 5: Identify sprint-by-sprint milestones
Break the release into checkpoints. Use Cohn's planning horizon principle: plan in detail for the next 1-2 sprints, rough milestones for the rest.

```
SPRINT MILESTONES
Sprint 1-2: [specific deliverables - detailed]
Sprint 3-4: [milestone checkpoint - e.g., "core feature complete, integration testing starts"]
Sprint 5:   [scope decision point - P1 items in or out based on velocity trend]
Sprint 6:   [release candidate, regression, final go/no-go]
```

### Step 6: Define the go/no-go criteria
State explicitly what must be true on the release date for the team to ship:
- P0 stories: all accepted
- Critical defects: zero Sev 1, fewer than [N] Sev 2
- Performance: [metric] meets [threshold]
- External dependencies: [list] confirmed resolved

## Anti-Patterns

**1. Committing to a single date from day one**
Bad: "We will ship on March 15th" based on a rough backlog estimate.
Good: "Our realistic forecast is March 15th ± 2 sprints. We will tighten this after Sprint 3."

**2. Planning without velocity data**
Bad: Generating a release date when the team has never shipped together.
Good: Flag the uncertainty, provide a range 2x wider than normal, revisit after 3 sprints.

**3. Forgetting to account for interrupt work**
Bad: Planning every story point of velocity for feature work.
Good: Reserve 15-20% of velocity for bugs, support escalations, and unplanned work - especially for teams with external customers.

**4. No scope buffer - only time buffer**
Bad: Fixed scope + fixed date with only a time buffer.
Good: Designate P1 items as scope buffer. If velocity is low, cut P1 - don't extend the date.

**5. Milestones too far apart**
Bad: "Done by Q3" with no intermediate checkpoints.
Good: A milestone every 2-3 sprints so you detect drift early, not at the end.

## Quality Checklist

- [ ] Velocity baseline uses at least 3 sprints of data (or uncertainty is flagged)
- [ ] Forecast includes optimistic, realistic, and conservative dates - not a single date
- [ ] Risk buffer is sized and labeled (what it covers, not just a percentage)
- [ ] Backlog is divided into P0 / P1 / P2 for scope flexibility
- [ ] Sprint-by-sprint milestones defined for at least the first half of the release
- [ ] Go/no-go criteria are explicit and measurable
