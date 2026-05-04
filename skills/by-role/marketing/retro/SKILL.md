---
name: retro
description: Capture learnings from a campaign, launch, sprint, or initiative using Five Whys (Taiichi Ohno, Toyota Production System) for root cause analysis and Start-Stop-Continue for action planning. Append reusable insights to knowledge/learnings.md so future runs of the OS get smarter. Use when the user asks for a retro, retrospective, post-mortem, "what did we learn", "campaign wrap-up", "lessons learned", or after a campaign or launch ends. Critical feedback loop that makes the OS compound over time.
reads:
  - knowledge/kpis.md
  - knowledge/learnings.md
  - output/campaign-brief/
writes:
  - knowledge/learnings.md (appends)
  - output/retro/
---

# retro

Captures structured learnings and persists them. The OS gets smarter every time this runs. Built on Five Whys (Taiichi Ohno) for root cause analysis and Start-Stop-Continue for action planning. The combination prevents "surface retros" - where the team identifies symptoms but repeats the same mistakes with different details.

## Frameworks

### Five Whys - Taiichi Ohno, Toyota Production System

When something goes wrong - or unexpectedly right - ask "why?" five times. Each answer becomes the basis for the next "why." The goal is the root cause, not the symptom.

Marketing example:
- Campaign missed pipeline target by 40%. Why?
- Lead quality was poor. Why?
- We targeted too broadly. Why?
- We hadn't updated our ICP definition. Why?
- No one owns ICP maintenance. Why?
- There's no process for reviewing ICP after each cycle.
- **Root cause: missing process, not bad execution.**

Without Five Whys, the team would have concluded "lead quality was poor" and changed the ad creative. The problem would repeat.

**Five Whys applies to wins too.** An unexpected outperformance has a root cause. Understanding it is how you replicate it, not just celebrate it.

### Start-Stop-Continue

**START**: What should we begin doing that we haven't tried?
**STOP**: What should we stop doing because it's not working or is waste?
**CONTINUE**: What's working that we should do more of?

Start-Stop-Continue is the action layer. Five Whys is the analysis layer. The two work together: Five Whys identifies WHY something happened, Start-Stop-Continue determines WHAT TO DO about it.

### Reusable insight classification

Every insight from a retro must be classified:
- **This campaign only**: a one-off factor (specific timing, specific partner, one-time event) that won't recur
- **All future campaigns**: a structural finding that applies broadly and should update how we operate

Only "all future campaigns" insights go into `knowledge/learnings.md`. Campaign-only insights stay in the retro document.

## When to use

- "Run a retro on the Q3 launch"
- "Let's debrief the campaign"
- "Capture what we learned from <initiative>"
- "Post-mortem on the webinar"

## Inputs needed

- **What's being retro'd**: campaign name, launch, sprint, etc.
- **Time period**: DD-MM-YYYY to DD-MM-YYYY
- **Outcome**: did it hit its primary KPI? What was the target vs actual?
- **Who was involved**: marketing, sales, product, contractors, agencies

## Process

1. **Load context.** Read the relevant `output/campaign-brief/<file>.md` if a brief exists. Read `knowledge/learnings.md` so you know what was already learned and don't repeat the same insight.

2. **Gather performance data.** For every metric, record: target, actual, delta (%). Flag any metric that missed by more than 10% or outperformed by more than 20%. These are the Five Whys candidates.

3. **Run Five Whys on every flagged metric.**

   Apply the Five Whys drill for each miss (>10% below target) AND each significant outperformance (>20% above target):

   ```
   Metric: <name>
   Target: <X>    Actual: <Y>    Delta: <Z%>

   Why 1: <observed factor>
   Why 2: <underlying cause of why 1>
   Why 3: <underlying cause of why 2>
   Why 4: <underlying cause of why 3>
   Why 5: <root cause>

   Root cause: <one sentence statement of the actual problem or advantage>
   Reusable: <this campaign only | all future campaigns>
   ```

   Stop at the root cause even if fewer than 5 whys are needed. Stop when you reach a process, ownership, or assumption gap - not a tactic.

4. **Run the retro structure**:

   ```
   # Retro: <Initiative> (DD-MM-YYYY)

   ## Outcome
   - **Primary KPI**: target <X>, actual <Y>, delta <%>
   - **Verdict**: hit / missed / partial

   ## Performance breakdown
   | Metric | Target | Actual | Delta | Five Whys root cause |
   |---|---|---|---|---|
   | <metric> | <X> | <Y> | <Z%> | <root cause> |

   ## Root cause analysis (Five Whys)
   <Full Five Whys drill for each flagged metric. See process step 3 above.>

   ## What worked
   List 3-5 things. Each must be specific and reusable.
   - <Specific tactic, channel, or decision> -> <observed outcome> -> <root cause of the win>
   - Example: "Founder-voice LinkedIn posts pulled 4x engagement vs company-voice. Root cause:
     personal credibility signals outperform brand signals in this ICP."

   Avoid vague statements like "the team executed well" or "messaging resonated."

   ## What didn't work
   List 3-5 things. Each must include the root cause from Five Whys:
   - <What failed> -> <Five Whys root cause>
   - Example: "Webinar attendance was 22% of registrants. Root cause: no ICP match in the
     registration list - we optimized for volume, not fit."

   "It just didn't perform" is a failure of analysis. Every miss has a root cause.

   ## Start-Stop-Continue
   <Actions derived from the root causes above. Every action traces to a Five Whys finding.>

   **START:**
   - <Action we should begin. What root cause does it address?>

   **STOP:**
   - <Action we should stop. What root cause revealed this is waste?>

   **CONTINUE:**
   - <Action we should keep. What root cause confirms it's working?>

   ## Surprises
   Things we didn't predict. These are the most valuable findings because they update our model.
   Apply Five Whys to surprises too - understanding WHY something surprised us is the real insight.

   ## Reusable insights
   Classify each insight:
   - <Insight> | applies to: <campaign type, channel, audience> | scope: <this campaign only | all future campaigns>

   Only "all future campaigns" insights go to knowledge/learnings.md.

   ## Root cause vs symptom check
   For each "what didn't work" item: is this insight about WHAT happened or WHY it happened?
   If it's about what happened, run Five Whys again until you reach why.

   ## Counterfactual check
   What would have happened if we had not run this campaign at all?
   If the answer is "roughly the same", flag it. Attribution matters.
   ```

5. **Persist to `knowledge/learnings.md`**: append "all future campaigns" insights only. Campaign-only insights stay in the retro document.

   ```
   ## <Initiative> retro (DD-MM-YYYY)

   **Result**: <hit|missed|partial> primary KPI - actual <Y> vs target <X>

   **Root causes (Five Whys)**:
   - <Metric that missed>: root cause was <finding>
   - <Metric that outperformed>: root cause was <finding>

   **Start-Stop-Continue (reusable actions)**:
   - START: <action> (applies to: <scope>)
   - STOP: <action> (applies to: <scope>)
   - CONTINUE: <action> (applies to: <scope>)

   **Reusable insights** (all future campaigns):
   - <Insight 1> (applies to: <campaign type, channel, audience>)
   - <Insight 2>
   ```

   Order: newest entries at the top. Every skill that reads `learnings.md` will see this.

6. **Cross-link**: if the retro contradicts or confirms an earlier learning, note it:
   "This contradicts the <DD-MM-YYYY> retro finding that <X>. Updated assumption: <Y>."

7. **Save the full retro** to `output/retro/<DD-MM-YYYY>-<initiative>.md`.

8. **Offer next actions**:
   - Schedule the next campaign brief with the new constraints applied (`/campaign-brief`)
   - Update `knowledge/icp/personas.md` if persona insights changed
   - Update `knowledge/markets/positioning.md` if positioning insights changed

## Rules

- Specificity is non-negotiable. "Messaging resonated" is not a learning. "Subject line with a number outperformed without by 38%" is.
- Every "what didn't work" entry must have a Five Whys root cause. Not a symptom. Not a hypothesis. A root cause.
- Five Whys applies to wins, not just misses. Wins you don't understand are luck, not capability.
- Start-Stop-Continue actions must trace back to a specific root cause. If an action doesn't map to a Five Whys finding, it's a guess.
- "Reusable" classification is mandatory. Campaign-only insights do not go into knowledge/. They clutter future retros.
- Always check the counterfactual. Sometimes campaigns "succeed" because the market was already moving.
- The `knowledge/learnings.md` summary is the most-read artifact in this OS. Make it tight, scannable, and actionable.
