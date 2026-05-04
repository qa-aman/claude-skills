---
name: ab-copy-writer
description: Generate A/B copy variants for any piece of marketing copy with a hypothesis per variant. Use when the user says "A/B test this", "write variants", "give me options", "test different angles", "copy variants", "ab copy", "test this headline", "multiple versions", or wants to test copy before publishing. Produces 3-5 variants per copy element with angle, hypothesis, and expected audience response. Reads brand voice and ICP from knowledge/.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/markets/positioning.md
  - knowledge/learnings.md
writes:
  - output/ab-copy/
---

# ab-copy-writer

Produces testable copy variants. Every variant has a distinct angle, a hypothesis for why it will outperform, and a predicted audience response. Stops marketers from shipping one version and guessing.

## When to use

- "Write 3 variants of this LinkedIn post"
- "Give me A/B options for this email subject line"
- "Test different angles for our landing page hero"
- "I need to A/B test this ad headline"
- "Write copy variants for our webinar title"
- "Give me 5 versions of this CTA"

## Inputs needed

1. **The copy element**: what needs variants (headline, subject line, hero, CTA, LinkedIn hook, ad copy, webinar title, email opener)
2. **The source**: existing copy to riff on, or a brief description of what it should accomplish
3. **Number of variants**: default is 3, max is 5
4. **Channel**: where this copy will run (LinkedIn, email, landing page, ad, webinar registration page)
5. **What's being tested**: angle, tone, format, CTA, or length (ask if not clear)

## Angles this skill tests

For each variant, pick a distinct angle from this list. Never use the same angle twice in one set:

| Angle | Description | When it wins |
|---|---|---|
| **Outcome-led** | Leads with the specific result | When audience is ROI-focused and numbers-driven |
| **Pain-led** | Opens on the problem, not the solution | When audience is in active pain and aware of it |
| **Speed-led** | Emphasizes time-to-value | When audience is impatient or under pressure |
| **Contrarian** | Challenges a common belief | When audience is saturated with standard messaging |
| **Social proof** | Leads with a customer result or name | When audience trusts peers more than vendors |
| **Curiosity gap** | Creates a knowledge gap that demands closing | When audience is information-hungry |
| **Specificity** | Extremely specific number or detail as the hook | When vague claims are common and specifics stand out |
| **Fear of missing out** | What happens if you don't act | When cost of inaction is high and under-communicated |
| **How-to** | Practical, instructional framing | When audience wants actionable takeaways |
| **Founder/operator voice** | Written as a practitioner to a practitioner | When audience distrusts brand voice |

## Process

1. **Load context.** Read `knowledge/brand/voice.md` (for tone and style rules) and `knowledge/icp/personas.md` (for what this audience responds to). If either is missing, ask the user for the relevant context directly.

2. **Check `knowledge/learnings.md`** for any past A/B test results or copy performance data. If a previous test showed "outcome-led beats pain-led for our ICP", factor that in and note it.

3. **Understand the goal.** Ask if not provided: "What action should this copy drive? And what's the one thing the audience should feel or believe after reading it?"

4. **Generate variants.** For each:

   ```
   ## Variant [A/B/C/D/E]: [Angle name]

   **Copy:**
   [the actual copy - complete and ready to use]

   **Angle**: [name from the angles table]
   **Hypothesis**: [1-2 sentences on why this angle should outperform the others for this specific audience]
   **Predicted response**: [how the ICP is likely to feel reading this]
   **Best for**: [which segment of the ICP or which stage of the funnel this variant suits most]
   **Watch for**: [what signal would tell you this variant is winning - clicks, replies, saves, conversions]
   ```

5. **Recommend the test setup**:

   ```
   ## Recommended test setup

   **Test**: [Variant A] vs [Variant B] (start with the two most different angles)
   **Why these two**: [1 sentence on why this pairing gives the clearest signal]
   **Sample size needed**: [rough guidance - "at least 500 impressions per variant before reading results"]
   **How long to run**: [1-2 weeks for LinkedIn organic, 7 days minimum for paid, 3+ sends for email]
   **Primary metric**: [clicks / replies / saves / open rate / conversion - pick one]
   **How to read results**: [what delta counts as a win: ">10% difference in CTR is signal, <5% is noise"]
   ```

6. **Self-check each variant**:
   - Distinct angle from every other variant - no two variants are the same approach with different words
   - Matches `knowledge/brand/voice.md` style rules (no em dashes, no banned phrases, correct POV)
   - Uses language from `knowledge/icp/personas.md` where relevant
   - Hypothesis is specific to the ICP, not generic ("this will outperform because our ICP is measured on activation rate, not awareness, so outcome-led copy speaks directly to their KPI")

7. **Save** to `output/ab-copy/<DD-MM-YYYY>-<copy-element-slug>.md` with frontmatter:
   ```yaml
   ---
   format: ab-copy
   element: [headline|subject-line|hero|cta|hook|ad]
   channel: [linkedin|email|landing-page|ad|webinar]
   variants: [number]
   angles: [list of angles used]
   created: DD-MM-YYYY
   ---
   ```

8. **Offer follow-ups**:
   - "Run `/retro` after the test and log which variant won and why. This gets appended to `knowledge/learnings.md` so future copy benefits from the result."
   - "Run `/content-writer` or `/linkedin-post` to build out the winning variant into a full piece."
   - "Want me to write the full ad set or email sequence using Variant [X] as the control?"

## Copy length by channel

| Channel | Element | Length |
|---|---|---|
| LinkedIn | Hook (first 2 lines) | 15-25 words |
| LinkedIn | Full post | 80-220 words |
| Email | Subject line | 6-10 words |
| Email | Preview text | 8-12 words |
| Email | Opener (first sentence) | 10-20 words |
| Landing page | H1 | 5-10 words |
| Landing page | Sub-headline | 15-25 words |
| Google ad | Headline | 30 chars max |
| Google ad | Description | 90 chars max |
| LinkedIn ad | Intro text | 150 chars max |
| Webinar | Title | 8-12 words |
| CTA button | Text | 2-5 words |

## Rules

- Never produce variants that are only cosmetically different (swapping one word is not a different angle).
- Never use an angle that `knowledge/learnings.md` has already shown underperforms for this ICP without flagging: "Past data shows [angle] underperformed. Including it here for completeness, but Variant X is the higher-confidence bet."
- Every hypothesis must reference the ICP specifically. "This will perform well" is not a hypothesis. "Our ICP (Head of Growth, measured on activation rate) will respond to specificity because they are data-fluent and distrust vague ROI claims" is.
- Always recommend starting the test with the two most different variants, not adjacent ones. Adjacent variants give weak signal.
- If the user provides existing copy, always include one variant that is a direct evolution of their version (keep their angle, sharpen the execution) alongside genuinely different angles. They may want a baseline.
