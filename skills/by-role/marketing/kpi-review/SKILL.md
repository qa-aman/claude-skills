---
name: kpi-review
description: Review marketing KPIs and produce an executive summary with insights, anomalies, and recommended actions using the Storytelling with Data framework (Cole Nussbaumer Knaflic). Every review starts with a Big Idea - one sentence capturing the insight, its implication, and why it matters. Use when the user asks for a KPI review, monthly metrics review, marketing dashboard review, "review last month's numbers", quarterly review, performance review, or wants to analyze marketing data. Reads kpis.md and any uploaded data files.
reads:
  - knowledge/kpis.md
  - knowledge/learnings.md
  - knowledge/icp/personas.md
writes:
  - output/kpi-review/
  - knowledge/kpis.md (appends snapshot)
---

# kpi-review

Acts as the user's data strategist. Reads KPIs, spots anomalies, recommends actions. Applies the Storytelling with Data framework (Cole Nussbaumer Knaflic) - every review has one Big Idea, every anomaly has a narrative arc, and every data display has a recommended chart type. Moves from analysis to actions: every review ends with three concrete next steps tied to specific insights, not generic observations.

## Framework: Storytelling with Data

### The Big Idea
Every data communication needs one singular "so what" - a single sentence that captures the insight + its implication + why it matters.

Data: "Our trial-to-paid rate dropped 4 points MoM."
Big Idea: "Our trial-to-paid rate dropped 4 points MoM, which means we're leaving $280K of ARR on the table this quarter unless we fix onboarding."

The Big Idea Worksheet (complete before analyzing):
1. What is the one thing I want the audience to know?
2. What do I want them to DO with that information?
3. Complete this sentence: "We need [audience] to [action] because [evidence]."

### Chart Type Rules
Match the display to the message. Never use 3D charts. Never use pie charts with more than 4 slices.
- Change over time: line chart
- Part of a whole: bar chart (preferred over pie)
- Comparison: bar chart side by side
- Relationship: scatter plot
- Ranking: horizontal bar chart

### Eliminate Clutter
Every element in a chart earns its place. Remove gridlines, legends (annotate directly), dual axes, unnecessary color variation.

### Focus Attention
Use pre-attentive attributes to direct the eye: color, size, position. Make the most important number impossible to miss.

### Narrative Arc for Anomalies
Data without narrative is noise. Every anomaly gets: situation (what happened) - complication (why it matters) - hypothesis (probable cause) - recommendation (what to do next).

## When to use

- "Review last month's KPIs"
- "Run a monthly metrics review"
- "Analyze our Q3 performance"
- "What does this dashboard tell us?"
- "Review our marketing numbers"

## Inputs needed

- **Period**: last week, month, quarter, custom range (default: last calendar month)
- **Data source**: file in `uploads/` (CSV from dashboard), pasted numbers in chat, or read from `knowledge/kpis.md` snapshots
- **Comparison baseline**: prior period, target, or both (default: both)

## Process

1. **Load context.** If `knowledge/kpis.md` does not exist, stop and say: "I need KPI context to run this review. Run `/onboard --kpis` first to define your metrics and targets." Otherwise read it to know which metrics matter and what the targets are. Read `knowledge/learnings.md` for context on prior anomalies and what was tried.

2. **Read the data.** If a CSV or report is in `uploads/`, parse it. If the user pasted numbers, work from chat. If neither, stop and ask: "Drop the data into `uploads/` or paste the numbers here."

3. **Write the Big Idea first.** Before building the review, complete the Big Idea Worksheet:
   - What is the one thing the reader needs to know from this period?
   - What action should they take?
   - Draft the Big Idea sentence: "[metric/trend] which means [implication] unless [action]."
   This becomes the TL;DR. Verify or revise it after analyzing all the data.

4. **Build the review in this format**:

   ```
   # KPI review: <period> (DD-MM-YYYY)

   ## TL;DR - Big Idea (read this if nothing else)
   [One sentence. Insight + implication + action. Readable in 10 seconds.]
   - **What's working**: <one sentence>
   - **What's broken**: <one sentence>
   - **What to do this week**: <one sentence>

   ## Metrics snapshot
   | Metric | Period | Prior | Target | Delta vs prior | Delta vs target | Chart type |
   |---|---|---|---|---|---|---|
   | MRR | $X | $Y | $Z | +12% | -3% | Line (trend) |
   | Pipeline | ... | ... | ... | ... | ... | Bar (comparison) |

   ## What changed and why
   For each metric that moved >10% or missed target by >10%:
   - **<Metric> moved <up/down> <X%>**
     - Situation: what happened, in one sentence
     - Complication: why this matters, what it puts at risk
     - Hypothesis: 2-3 probable causes ranked by likelihood
     - Recommendation: one specific action to validate or fix
     - Confidence: high / medium / low

   ## Anomalies
   For each anomaly, use the narrative arc:
   - **<Anomaly name>**
     - Situation: [what the data shows]
     - Complication: [why it's unexpected or concerning]
     - Hypothesis: [most likely explanation]
     - Recommendation: [what to do or investigate]
   Include: numbers that don't fit the pattern, diverging cohorts, channels that suddenly outperform or underperform, anything requiring a raw data look.

   ## Recommended actions
   Three actions, ranked. Each must connect to a specific Big Idea insight.
   - **What to do**
   - **Which insight it addresses** (tie directly to a finding above)
   - **Effort**: low / medium / high
   - **Expected impact**: which metric, by how much, by when

   1. ...
   2. ...
   3. ...

   ## Open questions
   Things you cannot answer from the data. The user should investigate or pull more data.

   ## What I don't know
   Be explicit about gaps. "I cannot say if the LinkedIn drop is seasonality or algorithm change without comparing to same period last year."
   ```

5. **Append to `knowledge/kpis.md`**: add a snapshot at the bottom of the file:
   ```
   ## Snapshot DD-MM-YYYY
   - MRR: $X
   - Pipeline: $Y
   - <metric>: <value>
   - Big Idea this period: [one sentence]
   ```
   This builds a longitudinal record over time.

6. **Self-check**:
   - TL;DR is the Big Idea - one sentence, readable in 10 seconds, action-oriented
   - Can the reader know what to DO in 10 seconds from the TL;DR? If not, rewrite it.
   - Every anomaly has all four narrative arc elements (situation, complication, hypothesis, recommendation)
   - Every metric in the snapshot table has a chart type note
   - Three actions are concrete (verbs, not "consider") and each tied to a specific finding
   - Confidence levels are explicit
   - "What I don't know" section is not empty (there is always something)

7. **Save** to `output/kpi-review/<DD-MM-YYYY>-<period>.md` with frontmatter:
   ```yaml
   ---
   format: kpi-review
   period: <period>
   start: DD-MM-YYYY
   end: DD-MM-YYYY
   big-idea: <one sentence>
   created: DD-MM-YYYY
   ---
   ```

8. **Offer follow-ups**:
   - Run `/retro` if a campaign just ended
   - Remind the user: "Set a calendar reminder to run `/kpi-review` again on [first of next month]."
   - Update `knowledge/kpis.md` if any targets need to change

## Rules

- Never invent numbers. If the data is incomplete, say so.
- Never recommend an action that is not tied to a specific insight in the review. No generic best practices.
- Every action must connect back to the Big Idea or a named anomaly. If the connection is not obvious, it is the wrong action.
- Confidence levels are required. "MRR dropped because of X" without a confidence label is not a finding.
- The "What I don't know" section is mandatory. If you skip it, you are pretending to know more than you do.
- The Big Idea is mandatory. If every metric looks fine, the Big Idea is "Everything is on track - the one risk to watch is X." There is always a so what.
