---
name: health-scorecard
description: >
  Build a customer health scorecard across usage, engagement, adoption, NPS, support load,
  and financial risk. Use when user says "health score", "customer health", "build a scorecard",
  "how healthy is this account", "customer scoring model", "green yellow red", "health dashboard",
  or "account health framework" - even if they don't say "scorecard" explicitly.
  Applies to CSMs building account health models or CS leaders standardizing health tracking
  across the team.
---

## Overview

Based on "Customer Success" by Mehta, Steinman & Murphy, a health score is the single most
important operational tool in CS. It converts diverse signals - usage, support, sentiment,
financial - into one composite view that tells a CSM where to focus time.

The core insight: a health score is only as useful as the action it triggers. A score without
a corresponding playbook is a dashboard that collects dust. Build the score and the response
together.

## Workflow

### Step 1: Define the six scoring dimensions

Score each dimension 1 (at risk) to 5 (healthy). Weight dimensions based on what predicts
churn or expansion in your product. Defaults shown below - adjust weights to your context.

**Dimension 1 - Product Usage (default weight: 25%)**
Measures whether the customer is actually using the product.

| Score | Signal |
|-------|--------|
| 5 | MAU >85% of licensed seats, logins growing MoM |
| 4 | MAU 70-85%, stable |
| 3 | MAU 50-70%, flat |
| 2 | MAU 30-50% or declining >10% MoM |
| 1 | MAU <30% or no logins in 30+ days |

**Dimension 2 - Feature Adoption (default weight: 20%)**
Measures depth of product use, not just login frequency.

| Score | Signal |
|-------|--------|
| 5 | >75% of core features adopted, exploring advanced features |
| 4 | 60-75% core features adopted |
| 3 | 40-60% adopted, stuck in basic workflows |
| 2 | <40% adopted, avoiding key features |
| 1 | Using only 1-2 surface features, product barely embedded |

**Dimension 3 - Engagement with CSM/Support (default weight: 15%)**
Measures relationship health and responsiveness.

| Score | Signal |
|-------|--------|
| 5 | Regular cadence calls, champion responsive within 24h, exec engaged |
| 4 | Monthly calls, reasonable responsiveness |
| 3 | Sporadic calls, 2-3 day response lag |
| 2 | Skipping calls, slow to respond, champion hard to reach |
| 1 | Gone dark - no response in 3+ weeks, declined last meeting |

**Dimension 4 - NPS / Sentiment (default weight: 15%)**
Measures subjective satisfaction and advocacy likelihood.

| Score | Signal |
|-------|--------|
| 5 | NPS 9-10, reference willing, positive qualitative feedback |
| 4 | NPS 7-8, satisfied, no active complaints |
| 3 | NPS 6-7, neutral, minor grumbles |
| 2 | NPS 4-6, frustrated, expressing dissatisfaction in calls |
| 1 | NPS 0-3, actively unhappy, escalations or threats to leave |

**Dimension 5 - Support Load (default weight: 15%)**
Measures whether the product is causing operational pain.

| Score | Signal |
|-------|--------|
| 5 | <2 tickets/month, all resolved promptly |
| 4 | 2-4 tickets/month, normal resolution time |
| 3 | 5-7 tickets/month or 1 lingering unresolved issue |
| 2 | 8-12 tickets/month or critical open issue >2 weeks |
| 1 | >12 tickets/month or multiple unresolved critical issues |

**Dimension 6 - Financial Risk (default weight: 10%)**
Measures exposure at renewal and expansion potential.

| Score | Signal |
|-------|--------|
| 5 | Renewal >6 months, expansion conversation active, budget secured |
| 4 | Renewal 4-6 months, no red flags |
| 3 | Renewal 2-4 months, no expansion discussion started |
| 2 | Renewal <2 months, budget uncertainty, no expansion |
| 1 | Renewal <2 months, active budget scrutiny or downsell risk |

### Step 2: Calculate the composite health score

Weighted score = sum of (dimension score x dimension weight)
Maximum possible score = 5.0

Example calculation:
- Usage: 3 x 0.25 = 0.75
- Feature Adoption: 4 x 0.20 = 0.80
- Engagement: 2 x 0.15 = 0.30
- NPS/Sentiment: 3 x 0.15 = 0.45
- Support Load: 4 x 0.15 = 0.60
- Financial Risk: 3 x 0.10 = 0.30
- **Composite: 3.20 / 5.0 - Yellow**

**Score ranges**:
- 4.0-5.0: Green - healthy, standard cadence
- 2.5-3.9: Yellow - watch, increase touchpoints
- 1.0-2.4: Red - at risk, immediate intervention

### Step 3: Apply dimension-level overrides (Red Flag Rule)

A single dimension scoring 1 can override a composite Green. Apply Red Flag Rule:

If any single dimension scores 1, the account is automatically Yellow regardless of composite.
If two or more dimensions score 1, the account is automatically Red.

This prevents a high-usage account with a gone-dark champion from being masked by a good composite.

### Step 4: Document the scorecard

Produce a scorecard entry for each account:

**[Customer name] - Health Score**
Scoring date: [date]
CSM: [name]

| Dimension | Weight | Score (1-5) | Weighted | Notes |
|-----------|--------|-------------|----------|-------|
| Product Usage | 25% | | | |
| Feature Adoption | 20% | | | |
| Engagement | 15% | | | |
| NPS / Sentiment | 15% | | | |
| Support Load | 15% | | | |
| Financial Risk | 10% | | | |
| **Composite** | | | | |

Status: Green / Yellow / Red
Red Flag Rule applied: Yes / No

**Top risk signal**: [the dimension with the lowest score and why it matters]
**Recommended next action**: [1 specific intervention with a date]

### Step 5: Set review cadence

Health scores must be refreshed regularly. Stale scores are worse than no scores because they
create false confidence.

- Green accounts: Review monthly
- Yellow accounts: Review bi-weekly
- Red accounts: Review weekly until score improves

## Anti-Patterns

**1. Composite score only, no dimension breakdown**
Bad: "Health score is 3.2." CSM doesn't know where to intervene.
Good: Show composite plus all six dimensions. The breakdown tells the CSM where to act.

**2. Static score never updated**
Bad: Setting a health score at onboarding and never refreshing it.
Good: Mandatory refresh cadence. Green = monthly, Yellow = bi-weekly, Red = weekly.

**3. No action linked to the score**
Bad: Health dashboard exists but no playbook triggers based on tier.
Good: Every tier (Green, Yellow, Red) maps to a specific cadence and intervention type.

**4. Ignoring single-dimension red flags**
Bad: Account with 85% MAU rated Green even though champion went dark 6 weeks ago.
Good: Apply Red Flag Rule. A gone-dark champion is a churn signal regardless of usage.

**5. Using only quantitative signals**
Bad: Scoring only usage and support tickets because they're easy to measure.
Good: Include sentiment and engagement even if they require CSM judgment to score. Hard-to-measure
signals are often the earliest churn indicators.

## Quality Checklist

- [ ] All six dimensions scored individually before calculating composite
- [ ] Weights adjusted to reflect what actually predicts churn in your context
- [ ] Red Flag Rule applied - single dimension scoring 1 escalates the tier
- [ ] Composite score assigned to Green / Yellow / Red tier
- [ ] Top risk signal identified with a specific recommended action
- [ ] Review cadence set based on tier
- [ ] Scorecard entry dated - staleness is tracked
- [ ] No personal names, internal tool names, or company-specific references in template
