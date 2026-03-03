---
name: competitive-analysis
description: >
  Conduct a competitive analysis. Use when the user says "competitive analysis",
  "how do competitors handle X", "market landscape", "what does [competitor] do",
  "compare us to X", "positioning analysis", or wants to understand how a product
  or feature compares to alternatives - even if they don't say "competitive analysis".
---

## Overview

A competitive analysis answers two questions: where are you stronger, and where are you weaker? The output should inform product decisions, not just describe what competitors built.

## Workflow

### Step 1: Define the scope
Clarify with the user:
- Is this for a specific feature or the whole product?
- Who are the known competitors? (direct, indirect, adjacent)
- What's the decision this analysis will inform?

Scope determines depth. A pricing decision needs different analysis than a roadmap decision.

### Step 2: Identify competitors
Group into:
- **Direct** - Same user, same problem, similar solution
- **Indirect** - Same user, same problem, different solution
- **Adjacent** - Different user or problem, but overlapping features

Cap at 5-7 competitors. More than that dilutes the analysis.

### Step 3: Define comparison dimensions
Choose 5-8 dimensions relevant to the decision. Common ones:
- Core feature set
- Pricing model
- Target user segment
- Onboarding experience
- Integration ecosystem
- Performance / reliability
- Mobile experience

### Step 4: Build the comparison matrix
Present as a table:

| Dimension | [Your Product] | Competitor A | Competitor B | Competitor C |
|-----------|---------------|--------------|--------------|--------------|

Use: Strong / Partial / Missing / Not applicable

### Step 5: Identify gaps and opportunities
Answer explicitly:
- Where do competitors consistently outperform you?
- Where do you consistently outperform them?
- What do users want that nobody is building?

### Step 6: State implications
End with 2-3 bullet points: "Given this analysis, we should consider..."

Analysis without implications is research, not strategy.

## Anti-Patterns

**1. Feature-listing without insight**
Bad: "Competitor X has a dashboard. Competitor Y has a dashboard. Competitor Z has a dashboard."
Good: "All major competitors offer dashboards. Our lack of one is a table-stakes gap, not a differentiator opportunity."

**2. Scope creep**
Bad: Analyzing 12 competitors across 20 dimensions.
Good: 5 competitors, 7 dimensions, focused on the decision at hand.

**3. Static analysis**
Bad: "Competitor X doesn't have mobile support."
Good: Note when the data was collected. Competitive landscapes shift. Flag anything likely to change.

**4. No implications**
Bad: Analysis ends with the comparison table.
Good: Always ends with: "What this means for us is..."

## Quality Checklist

- [ ] Scope is defined (feature vs. product, decision it informs)
- [ ] Competitors categorized as direct / indirect / adjacent
- [ ] No more than 7 competitors
- [ ] Dimensions are relevant to the decision, not generic
- [ ] Comparison matrix is clear and scannable
- [ ] Gaps and opportunities are stated explicitly
- [ ] Analysis ends with implications, not just observations
