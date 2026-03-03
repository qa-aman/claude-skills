---
name: experiment-design
description: >
  Design statistically rigorous experiments to test data science hypotheses. Use when the user says
  "design an A/B test", "run an experiment", "test this hypothesis", "is this difference significant",
  "how many samples do I need", "randomized controlled trial", "causal inference", "uplift test",
  "holdout group", "significance test", "power calculation", "avoid p-hacking", or needs to determine
  whether an observed effect is real before making a product or model decision.
---

## Overview

Based on **"The Art of Statistics"** by David Spiegelhalter. The core principle: statistical significance is not the same as practical significance, and a poorly designed experiment produces confidently wrong answers. Rigorous experiment design means defining the question, estimating the required sample size, and setting success criteria before any data is collected - then interpreting results within the limits of what the experiment can actually prove.

## Workflow

### Step 1: State the hypothesis in falsifiable form

A hypothesis must specify: the intervention, the population, the outcome metric, and the expected direction.

Format: "Applying [intervention] to [population] will [increase/decrease] [metric] compared to the control condition."

Example: "Showing personalized recommendations to new users in the first session will increase 7-day retention compared to showing trending content."

Also state the null hypothesis explicitly: "There is no difference in 7-day retention between personalized and trending content groups."

Spiegelhalter's warning: if you cannot state what result would cause you to reject your hypothesis, you do not have a hypothesis - you have a belief.

### Step 2: Identify the primary metric and guard metrics

**Primary metric:** The single number that determines whether the experiment succeeded. Choose one. Multiple primary metrics make interpretation ambiguous.

**Guard metrics:** Metrics that must not significantly worsen. If the primary metric improves but a guard metric degrades, the experiment fails.

Example:
- Primary: 7-day retention rate
- Guards: session length (must not drop > 5%), support ticket volume (must not rise > 10%)

### Step 3: Calculate required sample size before running

Use a power calculation to determine how many observations you need. Running underpowered experiments wastes time and produces false negatives.

Inputs needed:
- Baseline rate: current value of the primary metric (e.g., 22% 7-day retention)
- Minimum detectable effect (MDE): smallest change that would be meaningful (e.g., 2 percentage points)
- Statistical significance level: alpha = 0.05 (5% false positive rate)
- Statistical power: 1 - beta = 0.80 (80% probability of detecting a true effect)

```python
from statsmodels.stats.power import NormalIndPower

analysis = NormalIndPower()
n = analysis.solve_power(
    effect_size=0.02 / (0.22 * (1 - 0.22)) ** 0.5,
    alpha=0.05,
    power=0.80,
    alternative="two-sided"
)
print(f"Required n per group: {n:.0f}")
```

If the required sample size exceeds your available traffic within a reasonable window, increase the MDE or extend the timeline. Do not run an underpowered test.

### Step 4: Design the randomization and control

Randomization unit must match the analysis unit.

- If analyzing per-user metrics: randomize by user ID
- If analyzing per-session metrics: randomize by session ID
- If analyzing geographic effects: randomize by region (cluster randomization)

Document:
- How users are assigned (hash of user ID mod 2, for example)
- Whether assignment is sticky (user always sees the same variant)
- Exclusion criteria (new users only? logged-in only? specific device types?)

Run a sanity check (A/A test) before the real experiment if possible - confirm the two groups are balanced on baseline characteristics.

### Step 5: Set the stopping rule before launch

Never stop an experiment early because the results look good. Peeking inflates false positive rates.

Define in advance:
- Minimum runtime: run for at least 1 full business cycle (usually 1-2 weeks) to account for day-of-week effects
- Maximum runtime: set a hard end date
- Sample size target: stop when you hit the calculated N, not when the p-value crosses 0.05

If early stopping is operationally required, use a sequential testing method (e.g., always-valid p-values, group sequential design) instead of standard frequentist stopping rules.

### Step 6: Analyze and report results with effect size, not just p-values

Spiegelhalter's emphasis: p-values tell you whether an effect exists; effect sizes tell you whether it matters.

Report:
- Observed difference (absolute and relative)
- 95% confidence interval for the difference
- p-value (as supporting evidence, not the conclusion)
- Practical significance: is the effect size large enough to act on?

```python
from scipy import stats
import numpy as np

control = df[df["group"] == "control"]["converted"]
treatment = df[df["group"] == "treatment"]["converted"]

t_stat, p_value = stats.ttest_ind(control, treatment)
effect_size = treatment.mean() - control.mean()
ci = stats.t.interval(0.95, len(df)-2, loc=effect_size, scale=stats.sem(np.concatenate([control, treatment])))

print(f"Effect: {effect_size:.4f} ({effect_size/control.mean()*100:.1f}% relative lift)")
print(f"95% CI: ({ci[0]:.4f}, {ci[1]:.4f})")
print(f"p-value: {p_value:.4f}")
```

State the conclusion as: "The data [supports / does not support] rejecting the null hypothesis. The observed effect was [X], with a 95% CI of [Y to Z]. This [is / is not] practically significant because [reason]."

## Anti-Patterns

**1. Peeking and stopping early**
Bad: Checking results daily and stopping as soon as p < 0.05.
Good: Pre-commit to a sample size and stop date. Do not look at significance until the stopping criterion is met.

**2. Multiple primary metrics**
Bad: "We'll call it a win if conversion OR retention OR revenue improves."
Good: One primary metric. Guard metrics are binary pass/fail, not additional wins.

**3. Reporting only p-values**
Bad: "The result was statistically significant (p = 0.03), so we should ship."
Good: "The result was significant (p = 0.03). The absolute lift was 0.4pp (95% CI: 0.1 to 0.7). This is below our 1pp MDE threshold, so we will not ship."

**4. Ignoring novelty effects**
Bad: Running an experiment for 3 days and seeing a spike from users trying something new.
Good: Running for at least 1-2 weeks and examining whether the effect size stabilizes over time.

## Quality Checklist

- [ ] Hypothesis stated in falsifiable form with intervention, population, metric, and direction
- [ ] Single primary metric defined, plus guard metrics with acceptable thresholds
- [ ] Sample size calculated using power analysis before the experiment launches
- [ ] Randomization unit matches analysis unit
- [ ] Stopping rule (runtime and sample size target) defined before launch
- [ ] Results reported with absolute effect, relative effect, and 95% confidence interval
- [ ] Practical significance assessed separately from statistical significance
