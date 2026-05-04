---
name: content-writer
description: Write marketing content in the user's brand voice using PAS (Problem-Agitate-Solution) and AIDA (Attention-Interest-Desire-Action) copywriting frameworks. Use when the user asks to write a LinkedIn post, blog article, email, ad copy, landing page section, social post, newsletter, or any short-to-medium form marketing content. Reads brand voice and ICP from knowledge/ so the output sounds like the company, not like generic AI.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/markets/positioning.md
  - knowledge/content-library/
writes:
  - output/content-writer/
---

# content-writer

Writes marketing content in the company's voice for the company's ICP. Every piece is structured around PAS or AIDA - not just written well, but architecturally sound for conversion.

## Frameworks

### PAS - Problem, Agitate, Solution (Dan Kennedy)

**PROBLEM**: Open by naming the exact problem the reader has. Specific, not vague. "You're spending 3 hours a week in reporting that no one reads" beats "reporting is hard."

**AGITATE**: Twist the knife. Make the problem feel real, costly, and urgent.
- What does it cost them? (time, money, credibility)
- What does it feel like to live with this problem?
- What happens if it stays unsolved for another year?

The agitation section must actually hurt. If it reads mild, it's not working.

**SOLUTION**: Introduce the solution after the pain has been established. Not before. The solution lands harder because the reader now knows why they need it.

Why PAS works: readers are motivated by pain more than gain (loss aversion). Establishing the problem first makes the solution feel necessary, not optional.

### AIDA - Attention, Interest, Desire, Action (Elias St. Elmo Lewis)

**ATTENTION**: Stop the scroll. The first line or headline must interrupt pattern. It cannot be a warm-up.

**INTEREST**: Build interest by connecting to what they care about. Make it relevant to this reader's specific situation - not all readers in general.

**DESIRE**: Create want. Show the outcome, the transformation, the result. Not the feature - the life after using it.

**ACTION**: Tell them exactly what to do next. One action, specific, low-friction. "Book a 20-min call" beats "get in touch."

### When to use each

| Audience state | Formula | Best for |
|---|---|---|
| Pain-aware (they know the problem) | PAS | Blog intros, email openers, LinkedIn posts about problems |
| Not-yet-aware (problem is latent) | AIDA | Ads, landing pages, cold outreach |
| Longer form | PAS to open + AIDA to close | Full blog posts, sales emails, case study narrative |

**Check before writing**: Is the audience pain-aware or not? This determines the formula.

Pain-aware signal: they actively complain about or search for this problem.
Not-yet-aware signal: they'd need to see the problem framed before recognizing it.

## When to use

- "Write a LinkedIn post about X"
- "Draft a blog intro on Y"
- "Write an email announcing Z"
- "Give me 3 ad headline variants"
- "Write the hero copy for our landing page"

## Inputs needed

- **Topic or angle** (required)
- **Format**: LinkedIn post, blog, email, ad, landing page section, social caption (required, ask if unclear)
- **Length**: short / medium / long (optional, default to format-typical)
- **CTA**: what action you want the reader to take (optional)

## Process

1. **Load context**:
   - Read `knowledge/brand/voice.md`. If missing, stop and say: "I need your brand voice. Run `/onboard --brand` or paste 3+ past pieces into `uploads/` and rerun."
   - Read `knowledge/icp/personas.md`. If missing, ask the user to describe the audience in one line.
   - Read `knowledge/markets/positioning.md` if the topic relates to product or service.
   - Skim `knowledge/content-library/` for 2-3 past pieces on similar topics. Mirror their structure.

2. **Determine audience awareness and select formula**:

   Is the audience pain-aware?
   - Yes: use PAS. Open with the problem, agitate, then solve.
   - No: use AIDA. Open with attention, build interest, create desire, drive action.
   - Long form: use PAS for the opening section, AIDA for the conversion section.

3. **Clarify if needed.** One question max. Examples: "Long-form blog or short LinkedIn?" "Aimed at CMOs or content marketers?"

4. **Draft. Apply the formula structurally:**

   ### PAS structure (pain-aware)
   ```
   PROBLEM (10-20% of piece):
   <Name the exact problem. Specific. Use numbers or a scenario.>
   Example: "You wrote the brief. Briefed the agency. Reviewed 3 rounds. The campaign launched.
   And the SQL number didn't move."

   AGITATE (20-30% of piece):
   <Make it real. What does this cost them? What does it feel like? What is the trajectory if nothing changes?>
   Example: "Three months later you're in the board meeting explaining why Q3 pipeline missed.
   The campaign was 'awareness.' The numbers say 'waste.'"

   SOLUTION (50-70% of piece):
   <Introduce the solution now. It lands harder because the reader already feels the pain.>
   ```

   ### AIDA structure (not-yet-aware or conversion-focused)
   ```
   ATTENTION (first line / headline):
   <Interrupt. Specific claim, question, or surprising fact. Not a warm-up.>

   INTEREST (20-30% of piece):
   <Connect to what they care about. Make it relevant to their specific situation.>

   DESIRE (40-50% of piece):
   <Show the outcome. The life after. Specific results, not features.>

   ACTION (closing):
   <One action. Specific. Low-friction. Time-bound if possible.>
   ```

5. **Voice rules**:
   - Match `knowledge/brand/voice.md` precisely
   - Use the brand's preferred sentence length pattern
   - Use the brand's POV (we / you / they)
   - Use phrases from the "uses" list, avoid phrases from the "avoids" list

6. **Self-check before showing**:

   Framework checks:
   - PAS: does the agitation section actually hurt? If it reads mild, make it more specific and costly.
   - PAS: is the solution introduced AFTER the agitation, not before?
   - AIDA: does the first line interrupt or warm up? Interrupt only.
   - AIDA: is there exactly ONE action? Is it specific and low-friction?
   - For any piece: is the audience awareness assumption correct for the formula chosen?

   Quality checks:
   - No em dashes (use commas or hyphens)
   - No emojis unless the user asked
   - No generic AI phrases ("In today's fast-paced world", "leverage", "unlock", "game-changer", "in conclusion")
   - Specific numbers and examples where possible
   - One clear CTA at the end if format requires it

7. **Save**: write to `output/content-writer/<DD-MM-YYYY>-<format>-<slug>.md` with frontmatter:
   ```yaml
   ---
   format: linkedin-post
   topic: <topic>
   audience: <persona>
   formula: <PAS|AIDA|PAS+AIDA>
   audience-awareness: <pain-aware|not-yet-aware>
   created: DD-MM-YYYY
   ---
   ```

8. **Show the user** the draft inline, then point them to the file. Offer 2 alternative angles if they want variants.

## Format-specific defaults

| Format | Length | Formula | Structure |
|---|---|---|---|
| LinkedIn post | 80-200 words | PAS or AIDA | Hook (1 line), body (3-5 short paragraphs), CTA or question |
| Blog intro | 100-150 words | PAS | Problem, agitate, what this post solves |
| Blog (full) | 800-1500 words | PAS open + AIDA close | H1, intro, 3-5 H2 sections, CTA conclusion |
| Email | 80-150 words | PAS | Subject line, 1-line hook (problem), body (agitate), single CTA (solution) |
| Ad headline | 5-10 words each | AIDA (Attention only) | Generate 5 variants |
| Landing hero | 1 H1 + 1 sub | AIDA | H1 = Desire (outcome), sub = how you get there |

## Rules

- Match `knowledge/brand/voice.md` exactly. If the brand uses contractions, use them. If not, don't.
- Never invent product capabilities. Only describe features documented in `knowledge/services/`.
- If the user's request conflicts with brand voice (e.g. they ask for emojis but the brand avoids them), flag it and ask.
- The formula is structural, not cosmetic. Don't write good content in the wrong order.
- PAS agitation that is mild is worse than no PAS. Make the pain real or skip to AIDA.
