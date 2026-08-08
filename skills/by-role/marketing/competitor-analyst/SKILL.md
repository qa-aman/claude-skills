---
name: competitor-analyst
description: Analyze competitors using Blue Ocean Strategy's ERRC Grid and Strategy Canvas (W. Chan Kim and Renee Mauborgne) to identify uncontested market space, not just who is better on the same axes. Produces an ERRC Grid, Strategy Canvas, positioning matrix, messaging comparison, and differentiation map. Use when the user asks for competitive analysis, competitor research, "how do we compare to X", positioning vs competitors, market landscape, "analyze our competition", "where is the blue ocean", or wants to update competitor docs. Writes to knowledge/markets/competitors.md. For a lightweight competitor summary in the knowledge base, see brand-context. For positioning against them, see positioning-doc.
metadata:
  grounded_in:
    - "Blue Ocean Strategy - Kim & Mauborgne"
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

## Framework: Blue Ocean Strategy (W. Chan Kim and Renee Mauborgne)

From *Blue Ocean Strategy* (2005). Most companies compete in "red oceans": the same market space,
the same competing factors, everyone trying to be marginally better on axes the industry inherited
rather than chose. Kim and Mauborgne's move is value innovation, pursuing differentiation and low
cost at the same time by changing which factors are on the board at all.

**The ERRC Grid** - apply to every competitive analysis before building comparison tables. The four
actions are deliberately paired: Eliminate and Reduce take cost out, Raise and Create put buyer
value in. A grid that fills only Raise and Create is a feature wishlist, not a strategy, because it
adds cost without removing any.

| Action | Question | Purpose | Fails when |
|---|---|---|---|
| **Eliminate** | Which factors the industry takes for granted should be eliminated? | Remove cost and complexity buyers do not actually value | Left empty. An empty Eliminate row means nothing was questioned |
| **Reduce** | Which factors should be reduced well below the industry's standard level? | Stop over-delivering where buyers do not care | It names a factor buyers turn out to buy on |
| **Raise** | Which factors should be raised well above the industry's standard level? | Deliver more where the industry systematically under-delivers | It is really a roadmap item, not a positioning move |
| **Create** | Which factors should be created that the industry has never offered? | New value no competitor provides | The "new" factor already exists at a competitor. Check before claiming it |

**Strategy Canvas** - a line chart with competing factors on the x-axis and offering level (1 low to
10 high) on the y-axis, one curve per player. Kim and Mauborgne's test of a strong curve is three
properties, and this skill reports on all three:

| Property | What it means | How to read it off the canvas |
|---|---|---|
| **Focus** | The curve is high on a few factors, not middling on all of them | A flat curve across 8 factors has no focus |
| **Divergence** | The curve's shape differs from the industry's, not just its height | Overlay the curves. Different height, same shape, is a red ocean |
| **Compelling tagline** | The strategy states itself in one true sentence | If you cannot write it from the curve, the curve is not a strategy |

**Self-check question**: does our value curve look meaningfully different from competitors, or just
higher on the same axes? If it is just higher, we are in a red ocean, and that is the finding.

## Before you analyse: is the input strong enough?

| Signal | Threshold | If below |
|---|---|---|
| Competitors to analyse | 3 minimum, 7 maximum | Below 3, the canvas has no industry curve to diverge from. Above 7, no reader will use it. Ask the user to cut to the ones that appear in real deals |
| Sourceable evidence per competitor: homepage, pricing, one third source | 2 of 3 | Analyse what you can and list the competitor under Open questions. Never fill the gap from memory of the brand |
| Competing factors on the canvas | 6 to 10 | Fewer than 6 hides the shape. More than 10 and the curve is unreadable |
| Buyer-side input, meaning `knowledge/icp/personas.md` exists | Present | Proceed, but say clearly that the factors were chosen from the supply side. Factors picked without the buyer are the factors that are easy to compare, not the ones that decide deals |

Warning signs, in priority order:

1. Every scored cell is filled and none is blank. On a real analysis some cells cannot be sourced, so a complete table usually means estimates were entered as data.
2. "Where we lose" is empty or soft. That is flattery, and a battle card built on it fails on the first call.
3. The Eliminate and Reduce rows are empty. The analysis found things to add and nothing to drop, which is the most common way an ERRC grid becomes a roadmap.
4. Our curve is highest on every factor. Nobody is best at everything, so this is a scoring bias, not a finding.

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
   Score each player 1 (low) to 10 (high).
**Score only cells you can source.** Leave unknown cells blank and list them under Open questions.
Never estimate a competitor's score to complete the table: the canvas is the most authoritative-
looking artifact this skill produces and it is read as data. Append the source URL and fetch date
for each scored row. A client asking "where did the 4 for their ease-of-use come from?" must have
an answer.

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

8. **Self-check.** Every item is checkable by reading the finished analysis. Where an item says
   count, count it in the artifact rather than asserting the item passed.

   - [ ] The ERRC Grid appears above the comparison matrix in the document, and all four quadrants have at least one entry. Count the entries in Eliminate and Reduce specifically: two empty cost-side quadrants means the grid was not run
   - [ ] The canvas reports all three Kim and Mauborgne properties by name: focus, divergence, and the one-sentence tagline. If the tagline could not be written, that is recorded as the finding
   - [ ] Every scored cell carries a source URL and a fetch date next to it, and every unsourced cell is blank and repeated under Open questions. Count blanks and sources, and state both counts
   - [ ] "Blue ocean opportunity" names at least one CREATE factor, and that factor was checked against each competitor's own site before being called new
   - [ ] "Where we lose" lists 3 to 5 entries, each with a workaround. An empty or one-line section fails
   - [ ] Every per-competitor "recent moves" entry carries a dated source. Undated moves are dropped, not guessed
   - [ ] Pricing rows carry the date scraped
   - [ ] Battle card fits on one screen and every claim on it also appears, with its source, in the full analysis
   - [ ] The Sources section lists every URL with its access date, and the count matches the number of sourced cells

   **Stop conditions.** Do not write the executive summary to `knowledge/markets/competitors.md`
   when any of these hold, and say which one triggered:
   - Fewer than 3 competitors had 2 sourceable evidence types
   - More than a third of the canvas cells are unsourced
   - No CREATE factor survived the check against competitor sites, and the curve is the same shape as the industry's. That is a real finding, and it belongs in `output/` with the recommendation to reposition, not in the shared file as a competitor map

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
- **Never invent a competitor's pricing, headcount, funding, customer count, roadmap, or weakness.** A competitive doc is read as fact by sales, and an invented weakness becomes a claim a rep makes on a call to a prospect who knows better. Unverified goes under Open questions as `[UNVERIFIED: <what would confirm it>]`.
- Never make up a canvas score to complete a row. See the scoring rule in the Strategy Canvas step: blank plus an open question beats a plausible number.
- Do not fabricate the competitor's own words. Messaging comparison uses pasted H1s, subheads and CTAs, quoted exactly with the URL and date. Paraphrase from memory is not evidence.

## Shared file ownership: knowledge/markets/competitors.md

**This skill owns `knowledge/markets/competitors.md`.** It owns the file's structure and every
competitor entry in it. `/brand-context` may create a lightweight placeholder version of this file
when the knowledge base is first set up. Once this skill has written a full analysis, `/brand-context`
does not overwrite it.

| Part of the file | This skill may | Other skills may |
|---|---|---|
| Competitor entries, ERRC summary, quick comparison, win and lose lists | Create and replace in full | Read only |
| `knowledge/markets/positioning.md` | Read only. Recommend the change, never make it | `/positioning-doc` owns it |

The write gate, which is not optional:

1. Show the user a diff of the exact lines you would change in `knowledge/markets/competitors.md`, and wait for an explicit yes before writing. `/positioning-doc`, `/landing-page-writer`, `/ab-copy-writer` and the sales-facing skills all read this file as truth.
2. Apply the stop conditions in the self-check. If any triggered, save to `output/competitor-analysis/` only and say plainly which one, rather than writing a thin map into the shared file.
3. When the analysis surfaces a repositioning opportunity, write it as a recommendation in the output document and route the user to `/positioning-doc`. Never edit `knowledge/markets/positioning.md` from here.

## What this skill cannot know

1. **What the competitor is about to do.** Everything here is scraped from public surfaces, so an unannounced release, a repricing, or an acquisition invalidates the canvas without warning. Date-stamp every row so a reader can judge staleness.
2. **Whether a competitor's marketing matches their product.** A homepage is a claim. Feature parity read off a pricing page is a claim about a claim, and it is routinely wrong in both directions.
3. **How buyers actually score these factors.** The canvas scores are the analyst's read of the evidence, not measured buyer preference. Only win/loss interviews or a conjoint study give real weights, and without them focus and divergence are hypotheses.
4. **Enterprise pricing.** Public price pages rarely describe what large deals actually close at, so any pricing comparison above the self-serve tier is directional at best.

## Related skills

- `/positioning-doc` for turning a CREATE factor into a positioning statement, and it owns the positioning file this skill must not edit
- `/icp-research` for the buyer-side view that decides which competing factors belong on the canvas at all
- `/brand-context` for creating the knowledge base when `knowledge/markets/competitors.md` does not exist yet
- `/landing-page-writer` for rebuilding a page around the divergence the canvas found
- `/thought-leadership-writer` for a point of view that stakes out the blue ocean territory before a competitor names it
- `/ab-copy-writer` for testing the new angle against the current one rather than assuming the analysis was right
- `/customer-research` for when "where we lose" is empty, because losses live in lost-deal interviews, not on competitor websites
