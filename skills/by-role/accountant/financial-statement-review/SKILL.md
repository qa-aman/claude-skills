---
name: financial-statement-review
description: >
  Analyze and interpret financial statements to surface performance signals, quality
  concerns, and red flags. Use when an accountant says "review these financials",
  "analyze the income statement", "look at the balance sheet", "what does the cash
  flow statement tell us", "check the financial health", "ratio analysis", "are the
  earnings real", "working capital review", "does this company have liquidity issues",
  or needs to interpret any of the three core financial statements - even if they
  don't explicitly say "financial statement review". Also trigger when someone shares
  P&L, balance sheet, or cash flow data and asks what it means.
---

## Reference Files

- `references/industry-benchmarks.md` - Ratio benchmarks by industry (SaaS, manufacturing, retail, professional services, healthcare). Read this in Step 4 when calculating ratios and when you need industry-specific thresholds to compare against.

## Overview

Based on **"Financial Intelligence"** by Karen Berman & Joe Knight and **"The Interpretation of Financial Statements"** by Benjamin Graham. Financial statements are not just numbers - they are a compressed story of business decisions. The goal of a review is not to recite figures but to answer three questions: Is this business profitable in a way that will last? Is it financially stable? Is the reported profit converting to real cash?

Graham's core principle: always read all three statements together. The income statement shows profit; the balance sheet shows what was built with it; the cash flow statement shows whether the profit is real.

## Workflow

### Step 1: Read the Income Statement for quality of earnings

Start with the income statement and look beyond the headline net income number.

```
Revenue: [amount] - Is it growing? At what rate? Is growth organic or acquisition-driven?
Gross Margin: [%] - Is it stable, expanding, or compressing? Why?
Operating Income (EBIT): [amount] - Is operating leverage positive (margins growing faster than revenue)?
Net Income: [amount] - What is the effective tax rate? Are one-time items inflating it?
```

Flag immediately:
- Revenue growing but gross margin compressing (pricing power loss or cost problem)
- Net income higher than operating income (non-operating gains masking operations)
- Large "other income" or restructuring charges that recur every year (not truly one-time)

### Step 2: Read the Balance Sheet for financial stability

Assess the quality and composition of assets, and whether the capital structure is sustainable.

```
Current Ratio: Current Assets / Current Liabilities - below 1.0 is a liquidity warning
Quick Ratio: (Cash + AR) / Current Liabilities - strips out inventory; below 0.8 is a stress signal
Debt-to-Equity: Total Debt / Total Equity - above 2.0 warrants scrutiny in most industries
AR Days (DSO): (AR / Revenue) x 365 - rising DSO means slower collections or revenue recognition issues
Inventory Days: (Inventory / COGS) x 365 - rising inventory days can signal demand weakness
Goodwill as % of Total Assets - high goodwill (>30%) reflects acquisition risk
```

Look for the balance sheet to tell a different story than the income statement. If AR is growing much faster than revenue, earnings quality is declining - customers are not paying.

### Step 3: Read the Cash Flow Statement to verify earnings quality

The cash flow statement is where accounting choices cannot hide. Real businesses convert profit to cash.

```
Operating Cash Flow (OCF): [amount]
Net Income: [amount]
OCF / Net Income ratio: [calculate] - below 0.8 consistently is a red flag
Capital Expenditures: [amount] - how much is maintenance vs. growth capex?
Free Cash Flow: OCF - Capex = [amount] - the real measure of financial health
```

Key patterns to flag:
- Net income positive but OCF negative (profit not converting to cash)
- Large swings in working capital driving OCF (AR, inventory, AP changes)
- Capex declining while depreciation rises (underinvestment in the business)

### Step 4: Calculate the core ratio set

Run these ratios and compare against prior periods and industry benchmarks:

**Profitability**
- Gross margin %: Gross Profit / Revenue
- EBITDA margin %: EBITDA / Revenue
- Return on Assets (ROA): Net Income / Total Assets
- Return on Equity (ROE): Net Income / Total Equity

**Liquidity**
- Current ratio, Quick ratio (calculated in Step 2)
- Cash conversion cycle: DSO + Inventory Days - AP Days

**Leverage**
- Debt-to-EBITDA: Total Debt / EBITDA (above 4x is high leverage)
- Interest coverage: EBIT / Interest Expense (below 2x is distress territory)

**Efficiency**
- Asset turnover: Revenue / Total Assets
- Revenue per employee (if headcount is available)

### Step 5: Write the findings summary

Structure the output as a short, opinionated memo - not a list of numbers:

```
FINANCIAL REVIEW: [Company / Period]

HEADLINE: [One sentence on overall financial health]

STRENGTHS
- [Specific strength with supporting metric]
- [Specific strength with supporting metric]

CONCERNS
- [Specific concern, what it means, what to watch]
- [Specific concern, what it means, what to watch]

EARNINGS QUALITY
OCF/Net Income: [ratio] - [interpretation]
[1-2 sentence verdict on whether reported earnings are backed by cash]

KEY RATIOS SUMMARY
[table of 6-8 ratios with current period vs. prior period vs. benchmark]

RECOMMENDED NEXT STEPS
- [Specific action or investigation]
- [Specific action or investigation]
```

## Anti-Patterns

**1. Reporting numbers without interpretation**
Bad: "Revenue was $10M, up from $8M last year."
Good: "Revenue grew 25% but gross margin compressed from 42% to 37%, suggesting the growth was bought through pricing concessions or higher input costs - not through operating leverage."

**2. Treating net income as the primary signal**
Bad: Leading with "the company is profitable" because net income is positive.
Good: Cross-check OCF against net income. Positive net income with negative OCF means profit is not converting to cash - a red flag for earnings manipulation or structural problems.

**3. Looking at ratios without trend or benchmark**
Bad: "The current ratio is 1.4."
Good: "The current ratio is 1.4, down from 2.1 two years ago and below the industry median of 1.8. Liquidity is deteriorating."

**4. Missing the cash flow statement**
Bad: Reviewing only the income statement and balance sheet.
Good: The cash flow statement is the most manipulation-resistant of the three. Always read it last to validate what the other two are saying.

**5. Ignoring footnotes**
Bad: Treating the face of the statements as complete.
Good: Revenue recognition policy, lease commitments, contingent liabilities, and related-party transactions live in the footnotes. Material issues are often disclosed there and nowhere else.

## Quality Checklist

- [ ] All three statements reviewed (income statement, balance sheet, cash flow)
- [ ] Earnings quality checked: OCF vs. net income ratio calculated
- [ ] DSO and inventory days calculated and trended
- [ ] At least one liquidity ratio and one leverage ratio computed
- [ ] Findings framed as interpretation, not raw numbers
- [ ] Red flags called out explicitly with supporting evidence
- [ ] Summary memo written in plain language a non-accountant can act on
- [ ] Prior period comparison included (at minimum one prior period)
- [ ] No placeholder ratios - every ratio has a calculated value or is flagged as unavailable
