---
name: cost-benefit-analysis
description: >
  Build a business case with costs, benefits, and ROI. Use when the user says "cost-benefit analysis",
  "business case", "ROI calculation", "is this worth it", "justify the investment",
  "payback period", "benefits realization", "financial justification", "total cost of ownership",
  "should we build or buy", "investment appraisal" - even if they don't explicitly say "CBA".
---

## Overview

Based on **The Business Analysis Handbook** by Helen Winter - the Benefits Realization Framework that traces every requirement through output to benefit to business objective, ensuring nothing is built without a measurable business outcome. Also draws on **Business Process Change** by Paul Harmon for Activity-Based Costing in process improvements, and **Business Analysis Techniques** by James Cadle for the structured CBA technique with worked examples. The key insight from Winter: a cost-benefit analysis that only counts costs and tangible revenue misses the point. Benefits must be mapped to business objectives, and intangible benefits need proxy metrics.

## Workflow

### Step 1: Define the decision
State what is being evaluated:
```
DECISION: [What are we comparing?]
OPTIONS: [Build vs. Buy / Option A vs. B / Do vs. Don't]
TIME HORIZON: [3-5 years is standard]
DISCOUNT RATE: [organization's cost of capital or hurdle rate]
```

### Step 2: Identify all costs
Categorize into one-time and recurring:
```
ONE-TIME COSTS:
- Development / procurement: $[amount]
- Data migration: $[amount]
- Training and change management: $[amount]
- Infrastructure setup: $[amount]

RECURRING COSTS (annual):
- Licensing / subscription: $[amount]
- Maintenance and support: $[amount]
- Operations and infrastructure: $[amount]
- Ongoing training: $[amount]
```
Use Harmon's Activity-Based Costing to trace costs to specific process activities rather than lumping into categories.

### Step 3: Identify benefits using Winter's Benefits Map
Trace each benefit to a business objective:
```
Requirement --> Output --> Benefit --> Business Objective

Example:
"Automated order validation" --> "Orders validated in < 1 min"
--> "Reduced processing cost by $50K/year" --> "Improve operational efficiency (BO-2)"
```

Classify benefits:
- **Tangible (financial)**: Revenue increase, cost reduction - quantify in currency
- **Tangible (non-financial)**: Time saved, error reduction - quantify in units
- **Intangible**: User satisfaction, brand perception - define a proxy metric

### Step 4: Quantify over the time horizon
Build a year-by-year table:
```
| Year | Costs | Benefits | Net | Cumulative |
|------|-------|----------|-----|------------|
| 0    | -$[X] | $0       | -$[X] | -$[X]  |
| 1    | -$[X] | +$[X]   | +$[X] | -$[X]  |
| 2    | -$[X] | +$[X]   | +$[X] | +$[X]  |  <-- Payback
| ...  | ...   | ...      | ...   | ...     |
```

Calculate:
- **NPV** = Sum of (Benefit_t - Cost_t) / (1 + r)^t for each year
- **ROI** = (Total Benefits - Total Costs) / Total Costs x 100%
- **Payback Period** = Year when cumulative net benefits turn positive

### Step 5: Apply risk adjustment
For each major benefit and cost, assess:
```
ITEM: [benefit or cost]
BASE ESTIMATE: $[amount]
PROBABILITY: [% likelihood of realization]
RISK-ADJUSTED VALUE: $[base x probability]
KEY ASSUMPTION: [what must be true for this estimate to hold]
```

Run sensitivity analysis on the top 3 assumptions: what happens to NPV if each assumption is 20% worse?

### Step 6: Build the comparison and recommend
For each option, present: total cost, total benefit, NPV, ROI, payback period, and key risks. Recommend the option with the best risk-adjusted NPV, not just the lowest cost or highest ROI.

### Step 7: Output the CBA document
```
# Cost-Benefit Analysis: [Decision Name]

## 1. Executive Summary (recommendation + key numbers)
## 2. Decision and Options
## 3. Cost Breakdown (one-time + recurring)
## 4. Benefits Map (Winter's chain: requirement -> output -> benefit -> objective)
## 5. Financial Summary (NPV, ROI, Payback table)
## 6. Risk and Sensitivity Analysis
## 7. Recommendation
## 8. Assumptions Register
```

## Anti-Patterns

**1. Counting only tangible benefits**
Bad: CBA that shows $200K in development cost vs. $0 in quantified benefits because "it's hard to measure."
Good: Use proxy metrics for intangibles: "Reduce manual effort by 20 hours/week = $52K/year at fully loaded cost."

**2. Ignoring ongoing costs (TCO)**
Bad: Comparing $100K build cost to $80K buy cost (year 1 only).
Good: Total Cost of Ownership over the full time horizon including maintenance, licensing, and operations.

**3. Benefits without a realization owner**
Bad: "$500K in efficiency gains" with no one accountable for realizing them.
Good: Each benefit has an owner who is responsible for tracking realization post-implementation.

**4. No sensitivity analysis**
Bad: Single-point estimates presented as certain.
Good: Show what happens if key assumptions change by +/- 20%. If NPV goes negative, the decision is fragile.

**5. Comparing apples to oranges**
Bad: Comparing undiscounted future benefits to present-day costs.
Good: All values discounted to present value using the same rate and time horizon.

## Quality Checklist

- [ ] Decision and options clearly stated
- [ ] All cost categories covered (one-time + recurring = TCO)
- [ ] Benefits traced to business objectives using Winter's Benefits Map
- [ ] Tangible benefits quantified in currency
- [ ] Intangible benefits have proxy metrics
- [ ] NPV, ROI, and Payback Period calculated
- [ ] Key assumptions listed explicitly
- [ ] Sensitivity analysis on top 3 assumptions
- [ ] Each benefit has a realization owner
- [ ] Recommendation based on risk-adjusted NPV
