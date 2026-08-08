---
name: growth-experiment
description: >-
  Design and document a marketing growth experiment. Use when the user says "run a growth
  experiment", "test this channel", "growth test", "I want to experiment with [channel]",
  "traction experiment", "acquisition experiment", "let's test if [channel] works for us",
  "bullseye framework", "which channels should we try", "run a traction test", or wants
  to systematically test a marketing or acquisition channel before committing budget.
  For page-level conversion hypotheses, see page-cro. For copy variants to test, see ab-copy-writer. For recording the result, see retro.
metadata:
  grounded_in:
    - "Traction - Weinberg & Mares"
  reads:
    - knowledge/kpis.md
    - knowledge/icp/personas.md
    - knowledge/learnings.md
  writes:
    - output/growth-experiment/
---

## Overview

Based on **"Traction"** by Gabriel Weinberg and Justin Mares. The Bullseye Framework: most founders and marketers focus on 1-2 channels they are comfortable with and ignore the 17 others that might work better. Traction's framework forces you to test across the outer ring (all channels), identify the promising middle ring (likely channels), and then go all-in on the one channel in the bullseye. This skill structures a single growth experiment for one channel within that framework.

## Workflow

### Step 1: State the traction channel under test

Weinberg and Mares identify 19 traction channels. Name the one this experiment targets:

```
Channel: [e.g., Content Marketing / SEO, Paid Social, Cold Outreach, Partnerships, PR,
          Viral Marketing, Engineering as Marketing, Community Building, Events, etc.]
Hypothesis: [If we do X on this channel, we expect Y result within Z timeframe]
```

Be specific about the channel variant. "Paid Social" is too broad. "LinkedIn single-image ads targeting [role] at [company type]" is testable.

### Step 2: Define the experiment parameters

Before running anything, commit to these numbers in writing:

```
Budget: $[amount] or [hours] of time
Duration: [number] days/weeks
Target audience: [exactly who will see or receive this]
Volume: [minimum sample size - e.g., 500 ad impressions, 100 cold emails]
```

Traction's rule: a channel test that is too small produces no signal. Underfunded experiments produce false negatives.

### Step 3: Define the success metric and threshold

One metric. Set the threshold before you run the experiment - not after.

```
Primary metric: [e.g., cost per lead, click-through rate, reply rate, trial signups]
Baseline: [current value, from knowledge/kpis.md or the user, with the date measured]
   If no measured baseline exists, STOP and ask for one. **Never substitute an industry benchmark
   from memory** - the success threshold, the failure threshold and therefore the kill/scale
   decision all inherit it. If the user supplies a benchmark, record its source URL and tag the
   threshold [UNVERIFIED BASELINE].
Success threshold: [the minimum result that would justify investing more in this channel]
Failure threshold: [the result below which you kill this channel for now]
```

If you cannot define success before running, the experiment is not an experiment - it is activity.

### Step 4: Write the experiment brief

```
What we are testing: [specific creative, copy, targeting, or offer being tested]
What we are not testing: [variables held constant so results are attributable]
Tracking setup: [UTM params / pixel / tracking link / CRM tag]
Who is responsible: [name]
Decision date: [date you will review results and decide next action]
```

The "what we are not testing" line is as important as what you are testing. Changing headline and image and audience simultaneously means you will not know what drove results.

### Step 5: Document the expected learning

State in advance: what will you learn from this experiment regardless of whether it succeeds or fails?

- If it succeeds: "We learn that [channel] can deliver [metric] at [cost] for [audience] - and we should scale budget."
- If it fails: "We learn that [channel] does not work at this price point / for this audience / with this offer."

Writing the learning in advance prevents post-hoc rationalization after the results come in.

### Step 6: Log the results and decision

After the experiment completes:

```
Results:
- Primary metric: [actual value] vs. [target]
- Secondary observations: [anything unexpected]

Decision: Scale | Iterate | Kill
Rationale: [1-2 sentences]
Next action: [specific next step with owner and date]
```

Save the experiment log to `output/growth-experiment/<DD-MM-YYYY>-<channel-slug>.md` (see Context and output below). One location, so past experiments are findable. Companies that win on distribution run more experiments than competitors, not better gut-feel decisions.

## Anti-Patterns

**1. Testing too many variables at once**
Bad: New ad copy, new audience, new landing page, new offer all in the same test.
Good: One variable changes. Everything else held constant.

**2. Calling the experiment too early**
Bad: "We ran 50 impressions and got 0 clicks, so this channel does not work."
Good: Commit to minimum sample size before starting. Do not review until you hit it.

**3. Skipping the pre-experiment success threshold**
Bad: Reviewing results and then deciding what "good" looks like.
Good: "We define success as cost per trial signup under $40 before we start."

**4. No experiment log**
Bad: Running tests in people's heads with no written record.
Good: Every experiment documented with hypothesis, parameters, results, and decision.

## Quality Checklist

- [ ] Baseline is a measured number with a date, from `knowledge/kpis.md` or the user. No industry benchmark from memory
- [ ] `knowledge/learnings.md` was read, and any channel already tried is named
- [ ] Success and failure thresholds were set BEFORE launch, not after seeing data
- [ ] The experiment is saved to `output/growth-experiment/<DD-MM-YYYY>-<channel-slug>.md`
- [ ] Any `[UNVERIFIED]` input is tagged in the output and its effect on the decision is stated

- [ ] Specific traction channel named - not a broad category
- [ ] Hypothesis written in "if X then Y within Z" format
- [ ] Budget and duration committed in writing before starting
- [ ] Minimum sample size defined before starting
- [ ] Primary metric is single and measurable
- [ ] Success and failure thresholds set before the experiment runs
- [ ] Variables held constant are explicitly listed
- [ ] Tracking setup documented (UTM, pixel, or equivalent)
- [ ] Expected learning written for both success and failure scenarios
- [ ] Decision date set in advance

## Context and output

**Before you start.** Read `knowledge/kpis.md` for the OMTM and its current baseline, `knowledge/icp/personas.md` for where this audience already is, and `knowledge/learnings.md` for channels already tried. A threshold set without a baseline is a guess, so if `knowledge/kpis.md` is missing, get the baseline from the user before setting any success criterion.

**When you finish.** Save to `output/growth-experiment/<DD-MM-YYYY>-<channel-slug>.md` with YAML frontmatter carrying the date, the skill name, and the key decisions made.

After the experiment concludes, run `/retro` so the result is appended to `knowledge/learnings.md` and the next experiment does not repeat it.

## Related skills

- `/brand-context` creates the KPI baseline this depends on
- `/page-cro` produces page-level hypotheses worth testing
- `/ab-copy-writer` generates the variants
- `/retro` records the outcome so it compounds

## Handling [UNVERIFIED] and [NEEDS INPUT] tags

`brand-context` tags any number the user was unsure of as `[UNVERIFIED]`, and several skills tag
gaps as `[NEEDS INPUT]`. Those tags are a contract, and it only works if this skill honours it.

1. **Carry the tag forward.** If a baseline, benchmark or proof point arrives tagged, every figure
   derived from it is tagged too. A target built on an unverified baseline is an unverified target.
2. **Never silently promote.** Do not drop the tag because the number looked confident in the
   source file.
3. **Say it in the output.** List every tagged input in its own line near the top, so a reader
   knows which numbers are measured and which are estimates before they act on them.
4. **A decision that would change if the tagged number were wrong must say so explicitly.**

## The Bullseye framework (Weinberg and Mares)

*Traction* argues that most companies get most of their growth from one channel, and that the
channel is usually found by systematic elimination rather than intuition. Three rings, run in order.

| Ring | What it holds | What you do |
|---|---|---|
| **Outer** | All 19 channels, brainstormed without filtering | Write one plausible idea per channel. Cheap ideas count |
| **Middle** | The 3-5 that seem most promising | Run cheap, time-boxed tests to see which produce a signal |
| **Inner** | The one that works | Focus, and optimise it until it stops scaling |

The common failure is starting in the inner ring: picking a channel because a competitor uses it,
then optimising it for a quarter before asking whether it was ever the right channel.

**Test size matters more than test cleverness.** A channel test too small to produce signal has not
failed the channel, it has failed the test, and the conclusion drawn from it will be wrong.

## Warning signs, worst first

1. A threshold set after data started arriving. That is not an experiment, it is a story.
2. A baseline taken from an industry benchmark rather than this account's own history.
3. A channel already tried and recorded in `knowledge/learnings.md`, being retested unchanged.
4. A test still running past its decision date because the result is close.

## What this skill cannot know

- Whether the baseline supplied is measured or remembered
- Whether an external factor (seasonality, a competitor launch, a pricing change) is moving the metric alongside the test
- Whether the channel was already tried before the current team arrived
- Whether the sample will accumulate fast enough to decide by the stated date
