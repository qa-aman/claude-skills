---
name: social-calendar
description: Plan a monthly content calendar across channels using the Content Marketing Matrix (Dave Chaffey, Smart Insights) - Entertain/Inspire/Educate/Convince. Every post gets a quadrant label. The monthly calendar must hit 40% Educate, 40% Inspire+Convince, 20% Entertain. Produces a week-by-week posting schedule with topics, formats, channels, and asset links. Use when the user says "content calendar", "social calendar", "plan next month's content", "what should we post", "content plan", "editorial calendar", "schedule posts for the month", or wants a structured posting plan for LinkedIn, Twitter, email, or blog. Reads brand voice, ICP, and past learnings from knowledge/.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/markets/positioning.md
  - knowledge/services/
  - knowledge/content-library/
  - knowledge/learnings.md
  - knowledge/kpis.md
writes:
  - output/social-calendar/
---

# social-calendar

Plans a full month of content across channels. Every post has a job tied to a business goal and a quadrant in the Content Marketing Matrix. No random posting. No quadrant over-concentration.

## Framework: Content Marketing Matrix

### The 2x2 Matrix (Dave Chaffey, Smart Insights)
Map content by two axes:
- X axis: Emotional (left) to Rational (right) - does it appeal to feelings or logic?
- Y axis: Awareness (top) to Purchase (bottom) - is it for new audiences or ready-to-buy?

The 4 quadrants:

| Quadrant | Axes | Purpose | Content types | Primary metrics |
|---|---|---|---|---|
| **ENTERTAIN** | Emotional + Awareness | Build brand affinity through personality | Behind-the-scenes, culture, storytelling, humor | Reach, shares, followers |
| **INSPIRE** | Emotional + Purchase | Drive action through aspiration and proof | Case studies, testimonials, transformation stories | Demo requests, trial signups |
| **EDUCATE** | Rational + Awareness | Build authority through useful information | How-to guides, research, explainer posts, frameworks | Saves, newsletter signups, shares |
| **CONVINCE** | Rational + Purchase | Close through logic and proof | Comparison posts, ROI data, product demos, pricing | Conversions, trial starts |

### The 40/40/20 Rule
- 40% EDUCATE: builds the audience that buys
- 40% INSPIRE + CONVINCE combined: drives conversions
- 20% ENTERTAIN: builds the human brand people trust

### Warning Signs
Flag these in the calendar summary if they appear:
- >60% ENTERTAIN: brand awareness without pipeline
- >60% CONVINCE: pushy, algorithmic penalty risk, audience fatigue
- 0% INSPIRE: missing social proof entirely - a critical gap in a B2B calendar
- <10% EDUCATE: no authority building, audience has no reason to follow

### Weekly coverage rule
Each week should cover at least 3 of the 4 quadrants. A week that is all EDUCATE or all CONVINCE is out of balance.

## When to use

- "Plan next month's content"
- "Build a content calendar for Q3"
- "What should we post this month?"
- "Give me a 4-week editorial calendar"
- "Schedule our LinkedIn and email content for June"

## Inputs needed

1. **Month and year**: which month to plan (default: next calendar month)
2. **Channels**: LinkedIn organic, Twitter/X, newsletter, blog, YouTube - pick which apply
3. **Primary goal this month**: awareness, demand gen, retention, or event-driven (launch, webinar, conference)
4. **Posting cadence per channel**: how many times per week per channel (ask if not provided)
5. **Themes or constraints**: product launches, campaigns, events, or topics to avoid

## Process

1. **Load context.** Read `knowledge/brand/voice.md`, `knowledge/icp/personas.md`, `knowledge/kpis.md`. If `knowledge/brand/voice.md` is missing, stop: "I need voice context. Run `/onboard --brand` first."

2. **Check `knowledge/learnings.md`** for past content performance data. Surface any patterns: what formats outperformed, what topics resonated, what cadence worked.

3. **Check `knowledge/content-library/`** for existing content that can be repurposed or sequenced into the month.

4. **Define the month's content pillars** (3-4 max):
   - Each pillar maps to one ICP pain or goal from `knowledge/icp/personas.md`
   - Each pillar maps to one business outcome from `knowledge/kpis.md`
   - Map each pillar to its dominant quadrant (a pillar can span quadrants, but it should have a primary one)
   - Never let one pillar dominate more than 50% of posts

5. **Pre-check the quadrant distribution** before building week-by-week:
   - Count total planned posts for the month
   - Calculate targets: 40% EDUCATE, 20% ENTERTAIN, 40% INSPIRE+CONVINCE
   - Flag any warning signs before writing the calendar

6. **Build the calendar** week by week:

   ```
   # Content calendar: [Month YYYY]

   **Goal**: [primary goal]
   **Channels**: [list]
   **Cadence**: [X posts/week per channel]
   **Pillars**:
   - Pillar 1: [topic] -> speaks to [ICP pain] -> drives [metric] -> primary quadrant: [E/I/Ed/C]
   - Pillar 2: [topic] -> speaks to [ICP pain] -> drives [metric] -> primary quadrant: [E/I/Ed/C]
   - Pillar 3: [topic] -> speaks to [ICP pain] -> drives [metric] -> primary quadrant: [E/I/Ed/C]

   **Quadrant distribution target**: [N] EDUCATE | [N] ENTERTAIN | [N] INSPIRE | [N] CONVINCE

   ---

   ## Week 1 (DD-MM to DD-MM) | Quadrants this week: Ed, I, C, En

   | Day | Channel | Format | Pillar | Quadrant | Topic/Angle | Asset needed |
   |---|---|---|---|---|---|---|
   | Mon | LinkedIn | Text post | P1 | EDUCATE | [specific angle] | None - write in chat |
   | Wed | LinkedIn | Carousel | P2 | INSPIRE | [specific angle] | 6-slide design |
   | Thu | Newsletter | Issue | P3 | EDUCATE | [specific angle] | Full draft |
   | Fri | Twitter/X | Thread | P1 | CONVINCE | [specific angle] | None - write in chat |

   **Week 1 theme**: [one sentence connecting the week's posts]
   **Leading into**: [what week 2 builds toward]
   **Quadrant coverage this week**: Ed (2), I (1), C (1), En (0) - [flag if <3 quadrants covered]

   ## Week 2 (DD-MM to DD-MM)
   [same format]

   ## Week 3 (DD-MM to DD-MM)
   [same format]

   ## Week 4 (DD-MM to DD-MM)
   [same format]

   ---

   ## Quadrant distribution summary
   | Quadrant | Count | % of total | Target | Status |
   |---|---|---|---|---|
   | EDUCATE | X | X% | 40% | [on track / over / under] |
   | ENTERTAIN | X | X% | 20% | [on track / over / under] |
   | INSPIRE | X | X% | 20% | [on track / over / under] |
   | CONVINCE | X | X% | 20% | [on track / over / under] |

   **Warning sign flags**: [list any quadrant >60% or missing entirely, or clear the flags]

   ---

   ## Asset production queue
   List every asset that needs to be created, by type:
   - **Write in chat** (no design needed): [list of posts]
   - **Needs design**: [list with specs]
   - **Needs long-form draft**: [list]
   - **Needs video/audio**: [list]

   ## Skills to run for production
   - `/linkedin-post` for: [list specific posts by week/day]
   - `/newsletter-writer` for: [list issues]
   - `/content-repurposer` if: [list any anchor pieces to atomize]
   - `/thought-leadership-writer` for: [list long-form pieces]
   ```

7. **Self-check**:
   - Every post has a quadrant label
   - Monthly quadrant distribution hits 40/40/20 target (within 5% tolerance)
   - No quadrant is >60% of the total
   - No quadrant is 0% (especially INSPIRE - missing social proof is a common blind spot)
   - Each week covers at least 3 of 4 quadrants
   - Every post maps to a pillar, and every pillar maps to a business metric
   - No two consecutive posts on the same topic on the same channel
   - At least one proof point or customer reference per week
   - Newsletter anchors the week it falls in (other posts support it)
   - Cadence matches what was requested - do not over-schedule
   - Does the calendar serve all stages of the buyer journey? (Awareness through Purchase)

8. **Save** to `output/social-calendar/<DD-MM-YYYY>-<month-slug>.md` with frontmatter:
   ```yaml
   ---
   format: social-calendar
   month: [Month YYYY]
   goal: [awareness|demand|retention|launch]
   channels: [list]
   pillars: [list]
   quadrant-distribution: {educate: X%, entertain: X%, inspire: X%, convince: X%}
   created: DD-MM-YYYY
   ---
   ```

9. **Offer next actions**:
   - "Run `/linkedin-post` for any post on the calendar and I'll write it now."
   - "Run `/newsletter-writer` for [month] issue [N] to draft it."
   - "Run `/content-repurposer` on [anchor piece] to generate derivative posts."
   - "Set a reminder to run `/retro` at the end of the month to capture what worked."

## Channel-specific rules

**LinkedIn organic:**
- Max 5 posts/week or engagement drops
- Vary formats: text, carousel, poll, document
- Best days: Tuesday-Thursday
- Never post twice in one day

**Twitter/X:**
- Threads outperform single tweets for B2B
- 3-5 tweets per thread is the sweet spot
- Quote-tweet your own LinkedIn posts for cross-channel reach

**Newsletter:**
- One issue per week maximum for B2B audiences
- Tuesday or Wednesday sends outperform Monday and Friday
- Issue topic should anchor the week's social content

**Blog/SEO:**
- One pillar article per month minimum
- Long-form takes 2 weeks to write, edit, publish - account for lead time
- Every blog post generates 3-5 social posts via `/content-repurposer`

## Rules

- Never plan more posts than the team can realistically produce. If cadence seems high, flag it: "This is [N] posts/week. Confirm this is achievable before I finalize."
- Never schedule a product post without a paired proof point (stat, customer quote, or case study reference). Product posts without proof are CONVINCE posts that cannot convince.
- If `knowledge/learnings.md` has data showing a format underperforms, do not include it in the plan without flagging.
- No filler content. Every post earns its slot with a specific business reason and a quadrant assignment.
- If the user's goal is pure awareness, the mix can shift to 50% EDUCATE + 30% ENTERTAIN + 20% INSPIRE/CONVINCE. Adjust and note the shift explicitly.
