---
name: decision-matrix
description: >
  Build a weighted decision matrix to evaluate options. Use when the user says
  "decision matrix", "compare options", "weighted scoring", "which option should we choose",
  "evaluate alternatives", "Wiegers priority matrix", "force field analysis",
  "decision table", "trade-off analysis", "option comparison" - even if they don't
  explicitly say "decision matrix".
---

## Overview

Based on **Software Requirements** by Karl Wiegers & Joy Beatty - the Wiegers Priority Matrix that scores options across 4 factors (relative benefit, relative penalty, relative cost, relative risk) to produce a data-driven ranking. Also draws on **Business Analysis Techniques** by James Cadle for Decision Tables, Decision Trees, and Force-Field Analysis, and **Lean Business Analysis** by Mark Sherrington for Real Options thinking - deferring irreversible decisions until the last responsible moment. The key insight from Wiegers: gut-feel prioritization always favors the loudest stakeholder. A structured matrix makes trade-offs visible and defensible.

## Workflow

### Step 1: Define the decision and options
```
DECISION: [What are we choosing between?]
CONTEXT: [Why this decision matters now]
OPTIONS:
  A: [option name and brief description]
  B: [option name and brief description]
  C: [option name and brief description]
DECISION MAKER: [who has final authority]
DEADLINE: [when must this be decided]
```

### Step 2: Define evaluation criteria
List criteria that matter for this decision. Common categories:
- **Value criteria**: business benefit, user impact, strategic alignment, revenue potential
- **Cost criteria**: development effort, operational cost, opportunity cost
- **Risk criteria**: technical risk, adoption risk, compliance risk, reversibility

### Step 3: Assign weights to criteria
Each criterion gets a weight reflecting its importance (must total 100%):
```
| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| Business impact | 30% | Primary driver per sponsor |
| Implementation cost | 25% | Budget-constrained project |
| Time to deliver | 20% | Regulatory deadline in Q3 |
| Technical risk | 15% | New technology stack |
| Scalability | 10% | Growth expected in Year 2 |
```

Get stakeholder agreement on weights before scoring. The weights reflect organizational priorities.

### Step 4: Score each option (Wiegers Priority Matrix)
Rate each option against each criterion on a consistent scale (1-5 or 1-10):
```
| Criterion (Weight) | Option A | Option B | Option C |
|---------------------|----------|----------|----------|
| Business impact (30%) | 8 | 6 | 9 |
| Implementation cost (25%) | 5 | 8 | 3 |
| Time to deliver (20%) | 7 | 9 | 4 |
| Technical risk (15%) | 6 | 7 | 5 |
| Scalability (10%) | 4 | 5 | 9 |
```

For the Wiegers 4-factor variant, score each option on:
- **Relative Benefit** (1-9): Value of including this option
- **Relative Penalty** (1-9): Cost of NOT including it
- **Relative Cost** (1-9): Effort to implement
- **Relative Risk** (1-9): Technical/delivery uncertainty

Priority = (Benefit% + Penalty%) / (Cost% + Risk%)

### Step 5: Calculate weighted scores
For each option: Sum of (score x weight) across all criteria.
```
Option A: (8x0.30) + (5x0.25) + (7x0.20) + (6x0.15) + (4x0.10) = 6.45
Option B: (6x0.30) + (8x0.25) + (9x0.20) + (7x0.15) + (5x0.10) = 7.15
Option C: (9x0.30) + (3x0.25) + (4x0.20) + (5x0.15) + (9x0.10) = 5.90
```

### Step 6: Apply Force-Field Analysis for close calls
When scores are close (within 10%), use Cadle's Force-Field Analysis:
```
DRIVING FORCES (for change)    |    RESTRAINING FORCES (against)
=============================== | ===============================
[force] ------>  strength: 4    | strength: 3  <------ [force]
[force] ------>  strength: 5    | strength: 2  <------ [force]
```

The option with stronger net driving forces is preferred.

### Step 7: Document the recommendation
```
RECOMMENDATION: [Option X]
SCORE: [weighted score]
KEY TRADE-OFFS: [what you're giving up by choosing this option]
REVERSIBILITY: [can this decision be changed later? at what cost?]
DISSENTING VIEWS: [any stakeholder disagreements to note]
```

## Anti-Patterns

**1. Choosing criteria after seeing the scores**
Bad: Adding or removing criteria to justify a preferred option.
Good: Define and weight criteria before scoring. Lock them with stakeholder agreement.

**2. Equal weights on everything**
Bad: All criteria weighted 20% each - hides the real priorities.
Good: Force-rank criteria. If everything is equally important, nothing is important.

**3. Scoring without evidence**
Bad: "I feel like Option A is an 8 on scalability."
Good: "Option A uses a horizontally scalable architecture tested to 10K concurrent users - score 8."

**4. Ignoring reversibility (Sherrington's Real Options)**
Bad: Treating all decisions as permanent.
Good: If a decision is easily reversible, it may not need a full matrix. Invest analysis time proportional to the cost of being wrong.

**5. Matrix replaces judgment**
Bad: "The matrix says Option B, so we go with B."
Good: The matrix informs the decision. If the result feels wrong, the weights or criteria may be wrong - revisit them.

## Quality Checklist

- [ ] Decision and options clearly defined
- [ ] Criteria cover value, cost, and risk dimensions
- [ ] Weights assigned and agreed by stakeholders before scoring
- [ ] Weights total 100%
- [ ] Scores supported by evidence (not gut feel)
- [ ] Weighted scores calculated correctly
- [ ] Close results analyzed with Force-Field Analysis or sensitivity check
- [ ] Trade-offs of the recommended option are explicit
- [ ] Reversibility of the decision is assessed
