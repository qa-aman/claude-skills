---
name: competitor-analyst
description: Analyze competitors using Blue Ocean Strategy's ERRC Grid and Strategy Canvas (W. Chan Kim and Renee Mauborgne) to identify uncontested market space, not just who is better on the same axes. Produces an ERRC Grid, Strategy Canvas, positioning matrix, messaging comparison, and differentiation map. Use when the user asks for competitive analysis, competitor research, "how do we compare to X", positioning vs competitors, market landscape, "analyze our competition", "where is the blue ocean", or wants to update competitor docs. Writes to knowledge/markets/competitors.md.
reads:
  - knowledge/markets/competitors.md
  - knowledge/markets/positioning.md
  - knowledge/services/
  - knowledge/icp/personas.md
writes:
  - knowledge/markets/competitors.md
  - output/competitor-analysis/
---

# competitor-analyst

Builds an evidence-based competitor map using Blue Ocean Strategy's ERRC Grid and Strategy Canvas. The goal is not to find where we can be 10% better than the competition - it is to find where we can make the competition irrelevant. Writes to `knowledge/markets/competitors.md` so positioning and content skills get sharper.

## When to use

- "Analyze our competition"
- "Build a competitor matrix"
- "How do we compare to X?"
- "Update our competitive positioning"
- "Where do we win and lose vs <competitor>?"
- "Where is the blue ocean in our market?"

## Framework: Blue Ocean Strategy - ERRC Grid (Kim and Mauborgne)

Most companies compete in "red oceans" - the same market space, the same factors, trying to be marginally better. Blue Ocean Strategy creates uncontested market space by competing on different factors entirely.

**The ERRC Grid** - apply to every competitive analysis before building comparison tables:

| Action | Question | Purpose |
|---|---|---|
| **Eliminate** | Which factors the industry takes for granted should be eliminated? | Remove cost and complexity that buyers don't actually value |
| **Reduce** | Which factors should be reduced well below industry standard? | Stop over-delivering where buyers don't care |
| **Raise** | Which factors should be raised well above industry standard? | Deliver more where the industry systematically under-delivers |
| **Create** | Which factors should be created that the industry has never offered? | New value that no competitor provides |

**Strategy Canvas** - a line chart with competing factors on the x-axis and performance level (1-10) on the y-axis, one line per player. The goal is a different curve shape, not a higher version of the same curve.

**Self-check question**: Does our value curve look meaningfully different from competitors, or just higher on the same axes? If it's just higher, we are in a red ocean.

## Inputs needed

- **Competitors to analyze** (3-7 max)
- **Source URLs**: each competitor's homepage, pricing page, comparison pages, recent funding announcements
- **Lens**: positioning, messaging, pricing, features, GTM, content
- **Use case**: sales battle cards, marketing positioning, product roadmap input

## Process

1. **Load context.** Read `knowledge/markets/positioning.md` (so you know our position), `knowledge/icp/personas.md` (so you compare on what matters to the buyer), and any existing `knowledge/markets/competitors.md`.

2. **Pull competitor data.** For each competitor:
   - Use WebFetch on homepage to capture their headline, sub, and primary CTA
   - Use WebFetch on pricing page if public
   - Use WebFetch on any "vs <our brand>" comparison page they have published
   - Search recent news (funding, leadership, launches) via WebSearch

   If WebFetch fails or pages are gated, ask the user to paste content.

3. **Run the ERRC Grid first.** Before any comparison table, complete this analysis:

   ```
   ## ERRC Grid (Blue Ocean Strategy)

   ### Eliminate
   Which factors does this industry compete on that add cost and complexity but buyers don't actually care about?
   - <Factor>: <why it should be eliminated>
   - <Factor>: <why it should be eliminated>

   ### Reduce
   Which factors does the industry over-invest in where buyers don't value the excess?
   - <Factor>: current industry level vs what buyers actually need
   - <Factor>: current industry level vs what buyers actually need

   ### Raise
   Which factors does the industry systematically under-deliver on relative to what buyers need?
   - <Factor>: current industry level vs what buyers actually want
   - <Factor>: current industry level vs what buyers actually want

   ### Create
   Which factors could be created that no competitor currently offers?
   - <Factor>: new value source, why buyers would care
   - <Factor>: new value source, why buyers would care
   ```

4. **Build the Strategy Canvas.**

   ```
   ## Strategy Canvas

   Competing factors (x-axis): list 6-10 factors the industry competes on
   Score each player 1 (low) to 10 (high)

   | Factor | <Us> | <Competitor 1> | <Competitor 2> | <Competitor 3> |
   |---|---|---|---|---|
   | <Factor 1> | | | | |
   | <Factor 2> | | | | |
   | <Factor 3> | | | | |
   | <Factor 4> | | | | |
   | <Factor 5> | | | | |
   | <Factor 6> | | | | |

   **Curve analysis**:
   - Where our curve is identical to competitors: red ocean - we are competing on the same factors
   - Where our curve diverges: potential blue ocean - we are competing differently
   - Factors we should CREATE (from ERRC): these add new rows to the canvas that competitors cannot score
   ```

5. **Build the full comparison matrix.**

   ```
   # Competitor analysis (DD-MM-YYYY)

   ## Blue ocean positioning assessment
   Are we currently in a red ocean (competing on same factors) or a blue ocean (competing differently)?
   - **Current state**: <red/blue ocean assessment with evidence>
   - **Blue ocean opportunity**: <factor(s) from CREATE quadrant that no competitor addresses>
   - **Recommended move**: <one concrete repositioning action>

   ## Quick comparison
   | | <Us> | <Competitor 1> | <Competitor 2> | <Competitor 3> |
   |---|---|---|---|---|
   | **Tagline** | | | | |
   | **Primary persona** | | | | |
   | **Stage / size** | | | | |
   | **Pricing model** | | | | |
   | **Free tier** | | | | |
   | **Key differentiator** | | | | |
   | **Strongest channel** | | | | |
   | **Weakness** | | | | |

   ## Positioning map
   Plot competitors on two axes (pick the two that matter most for your category):
   - Axis 1: <e.g. ease of use vs power>
   - Axis 2: <e.g. SMB vs enterprise>

   Describe where each sits and where the gaps are.

   ## Per-competitor deep dive

   ### <Competitor 1>
   - **What they do well**: 3 specific things
   - **Where they're weak**: 3 specific things
   - **How they message**: 3 examples of their language vs ours
   - **Their ideal customer**: who they're winning
   - **Our angle when competing**: what to lead with vs them
   - **Our risk**: where they could beat us
   - **Recent moves**: funding, launches, hires (last 6 months)
   - **Sources**: URLs and dates

   <repeat per competitor>

   ## Messaging comparison
   For each competitor, paste their:
   - H1 from homepage
   - Sub-headline
   - Primary CTA copy
   - One feature description

   Then compare to ours. Identify:
   - Where we sound the same (a problem - red ocean language)
   - Where we say less than them (a gap)
   - Where we say more (good if true, bad if puffery)

   ## Where we win
   List 3-5 specific advantages, each with evidence:
   - Advantage: <claim>
   - Evidence: <source>
   - When to use it: <sales scenario or content angle>

   ## Where we lose
   Be honest. List 3-5 disadvantages:
   - Disadvantage: <claim>
   - Workaround: <how to handle it in sales conversations>
   - Roadmap implication: <what to build/communicate to close the gap>

   ## Battle card (one per major competitor)
   - **30-second pitch when up against them**
   - **Top 3 trap-setting questions** (questions to ask the prospect that surface our advantages)
   - **Top 3 objections** they will raise about us, with responses
   - **Pricing posture**: when to discount, when to hold

   ## Open questions and gaps
   What we couldn't verify. The user should investigate.

   ## Sources
   - List every URL with date accessed
   ```

6. **Update `knowledge/markets/competitors.md`** with the executive summary (ERRC Grid + quick comparison + per-competitor advantages/disadvantages). Keep it tight (under 500 lines) so other skills can load it cheaply.

7. **Save the full analysis** to `output/competitor-analysis/<DD-MM-YYYY>-comparison.md`.

8. **Self-check**:
   - ERRC Grid is complete before the comparison matrix
   - Strategy Canvas shows whether our value curve is different or just higher
   - "Blue ocean opportunity" section names at least one CREATE factor
   - Every claim has a source (URL or interview)
   - Compared on what the buyer cares about, not on what's easy to compare
   - "Where we lose" is not empty (if it is, you're flattering yourself)
   - Battle card is short enough that a sales rep can use it on a call

9. **Offer follow-ups**:
   - Update `knowledge/markets/positioning.md` if the ERRC analysis surfaced a repositioning opportunity
   - Run `/landing-page-writer` for a new homepage that addresses competitor weak spots
   - Run `/thought-leadership-writer` for a POV piece that stakes out the blue ocean territory

## Rules

- Run the ERRC Grid before any comparison table. The grid tells you what to compare. The table does not tell you what to compete on.
- Never compare on features alone. The buyer compares on outcomes. Tie features to outcomes.
- Always include "where we lose". If you can't find weaknesses in your own product vs competitors, you're not looking hard enough.
- If the Strategy Canvas shows our curve is identical to competitors on every factor, say so directly. That is the finding. Repositioning is required before more campaigns will work.
- Pricing comparisons must reference the date scraped. Pricing changes frequently.
- Comparison pages from the competitor (their "vs you" page) are a goldmine. Read theirs before writing yours.
- Do not produce sales battle cards without confirming with the user that sales reps will actually use them. Otherwise it's dead documentation.
