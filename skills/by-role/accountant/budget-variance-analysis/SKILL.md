---
name: budget-variance-analysis
description: >
  Analyze budget vs. actual variances, identify root causes, and recommend corrective
  actions. Use when an accountant or finance professional says "explain this variance",
  "budget vs. actual analysis", "why did we miss budget", "favorable / unfavorable
  variance", "price volume variance", "management reporting commentary", "explain
  the P&L variance to the CFO", "what drove the cost overrun", "revenue shortfall
  analysis", or needs to write the narrative behind a financial result.
  Also trigger when someone shares a table of actuals vs. budget and needs to explain
  the gaps - even if they don't use the word "variance".
---

## Overview

Based on **"Cost Accounting: A Managerial Emphasis"** by Horngren, Datar, and Rajan - the standard reference for management accounting and variance analysis. Variance analysis is not about flagging numbers that are off; it is about explaining *why* they are off in a way that leads to a decision.

Horngren's principle: decompose variances into their components (price, volume, mix, efficiency) before drawing conclusions. A single unfavorable revenue variance could be caused by lower prices, lower volume, or a worse product mix - and each cause has a completely different corrective action.

## Workflow

### Step 1: Establish the variance summary

Before decomposing, calculate the total variance for each line and flag direction.

```
VARIANCE SUMMARY - [Period]

                     Actual      Budget      Variance    %       F / U
Revenue              $[X]        $[X]        $[X]        [%]     [F/U]
Cost of Goods Sold   $[X]        $[X]        $[X]        [%]     [F/U]
Gross Profit         $[X]        $[X]        $[X]        [%]     [F/U]
  Gross Margin %     [%]         [%]         [%pts]              [F/U]
Operating Expenses   $[X]        $[X]        $[X]        [%]     [F/U]
Operating Income     $[X]        $[X]        $[X]        [%]     [F/U]
```

F = Favorable (better than budget). U = Unfavorable (worse than budget).
Apply F/U correctly: higher-than-budget revenue is F; higher-than-budget expense is U.

Focus investigation on variances that are:
- More than [materiality threshold] in absolute dollars
- More than 5-10% of the budgeted line
- Unexpected directionally (e.g., revenue up but gross margin down)

### Step 2: Decompose revenue variances

Revenue variance has three components: price, volume, and mix.

**Price variance** - Did we sell at the price we planned?
```
Revenue Price Variance = (Actual Price - Budget Price) x Actual Volume
Favorable if actual price > budget price
```

**Volume variance** - Did we sell the quantity we planned?
```
Revenue Volume Variance = (Actual Volume - Budget Volume) x Budget Price
Favorable if actual volume > budget volume
```

**Mix variance** (multi-product businesses) - Did we sell the right mix of products?
```
Revenue Mix Variance = (Actual Mix % - Budget Mix %) x Total Actual Volume x (Product Margin - Avg Margin)
Favorable if actual mix skewed toward higher-margin products
```

After decomposing, write a one-paragraph explanation:
```
Revenue was [F/U] by $[X] vs. budget.
- Price: [favorable/unfavorable] by $[X] - [explanation: discounting, pricing change, FX, etc.]
- Volume: [favorable/unfavorable] by $[X] - [explanation: market demand, sales execution, etc.]
- Mix: [favorable/unfavorable] by $[X] - [explanation: product mix shift, channel mix, etc.]
Net: $[X] [F/U]
```

### Step 3: Decompose cost variances

For COGS and direct costs, decompose into spending (price) and efficiency (usage) components.

**Spending variance (price effect)** - Did inputs cost more or less per unit than planned?
```
Spending Variance = (Actual Rate - Budget Rate) x Actual Quantity
```

**Efficiency variance (usage effect)** - Did we use more or fewer inputs per unit of output than planned?
```
Efficiency Variance = (Actual Quantity - Budget Quantity) x Budget Rate
```

For labor:
```
Labor Rate Variance = (Actual Hourly Rate - Budget Hourly Rate) x Actual Hours
Labor Efficiency Variance = (Actual Hours - Budget Hours) x Budget Hourly Rate
```

For materials:
```
Material Price Variance = (Actual Unit Cost - Budget Unit Cost) x Actual Quantity
Material Usage Variance = (Actual Quantity - Budget Quantity) x Budget Unit Cost
```

### Step 4: Explain operating expense variances

For fixed and discretionary costs (SG&A, R&D, headcount), the decomposition is simpler:

```
Expense Variance = Actual Expense - Budget Expense

Explain by category:
- Headcount: [actual HC vs. budget HC] x [avg cost per head]
- Timing: expenses budgeted in this period but shifted (or pulled forward)
- One-time items: [legal, severance, project costs not in budget]
- Inflation / rate: [vendor price increases above budget assumption]
- Volume-driven: [variable costs that moved with revenue]
```

### Step 5: Write the management commentary

Translate the numbers into narrative for leadership:

```
BUDGET VARIANCE COMMENTARY - [Period]

HEADLINE
[One sentence: net result and whether it was above or below budget, by how much]

REVENUE: [F/U $X vs. budget]
[2-3 sentences: what drove it, broken into price/volume/mix where relevant]

GROSS MARGIN: [F/U $X / [X]pts vs. budget]
[2-3 sentences: COGS drivers - materials, labor, overhead absorption, mix]

OPERATING EXPENSES: [F/U $X vs. budget]
[2-3 sentences: key lines that moved, timing vs. structural, headcount context]

KEY RISKS / OPPORTUNITIES
- [Forward-looking risk or opportunity suggested by the variance analysis]
- [Forward-looking risk or opportunity]

CORRECTIVE ACTIONS (where applicable)
- [Specific action, owner, timeline]
- [Specific action, owner, timeline]
```

## Anti-Patterns

**1. Describing variances without decomposing them**
Bad: "Revenue was $500K unfavorable vs. budget due to lower sales."
Good: "Revenue was $500K unfavorable: $200K price (average selling price declined 3% due to competitive discounting), $300K volume (unit sales 8% below budget in the SMB segment, offset partially by enterprise outperformance of +$150K)."

**2. Calling everything "timing"**
Bad: Labeling every unfavorable expense variance as "timing" without evidence.
Good: Timing means a specific expense was budgeted in one period and shifted to another. Identify the specific item, the budgeted period, and when it will now be incurred.

**3. No corrective action for unfavorable variances**
Bad: Documenting a $300K unfavorable COGS variance and stopping there.
Good: Variances that repeat need a root cause and an owner. "Material costs exceeded budget by $300K due to supplier price increases. Procurement is renegotiating the contract with [vendor] - revised pricing expected by [date]."

**4. Favorable variance treated as no investigation needed**
Bad: Ignoring favorable variances.
Good: A favorable variance can hide a problem. Revenue $500K favorable on $300K lower expenses might mean volume was lower but headcount and overhead are under-absorbed. Investigate favorable variances where the cause is not obvious.

**5. Mixing actuals from different accounting bases**
Bad: Comparing cash-basis actuals to accrual-basis budgets.
Good: Confirm both actuals and budget use the same accounting basis before calculating variances. If they differ, restate before analysis.

## Quality Checklist

- [ ] Variance summary table complete with F/U designation for every line
- [ ] Material variances identified using absolute dollar and % thresholds
- [ ] Revenue variance decomposed into price, volume, and mix where applicable
- [ ] Cost variances decomposed into spending (rate) and efficiency (usage) where applicable
- [ ] Management commentary written in plain language, not accounting jargon
- [ ] Every "timing" explanation has a specific item, original period, and new expected period
- [ ] Corrective actions include owner and timeline for unfavorable variances
- [ ] Forward-looking risks or opportunities flagged where variance suggests a trend
- [ ] No favorable variance left unexplained if the cause is not obvious
