---
name: content-repurposer
description: Take one piece of long-form content (blog post, podcast, talk, article, newsletter) and turn it into a multi-channel asset pack using the STEPPS framework (Jonah Berger, Contagious) to make each derivative asset more shareable. Use when the user says "repurpose this", "turn this into LinkedIn/Twitter/etc", "atomize this", "break this down for social", "create derivative content from X", "make a content pack from this", or wants to maximize output from one input. Each channel is mapped to its strongest STEPPS element. Orchestrates linkedin-post, content-writer, and other skills.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/content-library/
writes:
  - output/repurposed/
---

# content-repurposer

Orchestrator skill. One source piece becomes a coordinated asset pack across channels. Each output is fully native to its channel and optimized for shareability using STEPPS. Not a copy-paste with different word counts.

## When to use

- "Repurpose this blog post"
- "Turn this article into LinkedIn / Twitter / email"
- "Atomize my podcast episode"
- "Make a content pack from this newsletter"
- "Break this talk into social posts"

## Inputs needed

- **Source**: file path, URL, or pasted text
- **Source type**: blog, podcast transcript, conference talk, newsletter, video script, internal doc
- **Channels to produce for**: pick from list (default: all)
- **Author voice**: founder, CMO, company (default: company)

## Channels this skill produces

| Output | Format | Length | Primary STEPPS element | Skill it calls |
|---|---|---|---|---|
| LinkedIn post | text | 80-220 words | Social Currency | linkedin-post |
| LinkedIn carousel outline | slide-by-slide | 6-10 slides | Practical Value + Social Currency | inline |
| Twitter/X thread | numbered tweets | 7-12 tweets | Practical Value | inline |
| Substack note | text | 3-5 sentences | Stories + Emotion | inline |
| Email teaser | subject + body | 80-150 words | Triggers + Emotion | content-writer |
| Reddit version (relevant subs) | text + subreddit suggestions | 200-400 words | Practical Value | inline |
| Quote graphic suggestions | pull quotes | 3-5 quotes | Emotion + Social Currency | inline |
| YouTube short script | spoken | 45-60 seconds | Stories + Emotion | inline |
| SEO snippet variant | optimized intro | 150 words | Practical Value | inline |

## Framework: STEPPS (Jonah Berger, Contagious)

Six reasons things spread. Run this on the source piece before producing any assets.

| Element | What it means | Question to ask |
|---|---|---|
| **S - Social Currency** | Does sharing this make me look good, smart, or in-the-know? | Would someone share this to show off? |
| **T - Triggers** | What everyday cue will remind people of this idea? | What common situation or object does this connect to? |
| **E - Emotion** | High-arousal emotions drive sharing: awe, excitement, anxiety, anger. Low-arousal (contentment, sadness) do not. | Does this make someone feel something intensely? |
| **P - Public** | Can people see others engaging with this? Visibility drives imitation. | Is there a social proof layer? |
| **P - Practical Value** | Useful = shareable. "News you can use." | Can someone apply this today? |
| **S - Stories** | Information travels inside a narrative. The story is the Trojan horse. | Is there a narrative with tension and resolution? |

A score of 4+ out of 6 indicates high virality potential. Below 3, flag it.

## Process

1. **Load source.** If it's a file, read it. If it's a URL, use WebFetch. If pasted, use the chat content. Confirm with the user: "I read X. Source has N words and covers <main themes>. Proceed?"

2. **Run STEPPS scoring on the source piece.** Score each element 1-3 (1 = weak, 2 = present, 3 = strong). Show the table to the user before producing assets.

   ```
   STEPPS Score - <source title>

   | Element | Score (1-3) | Evidence from source | Notes |
   |---|---|---|---|
   | Social Currency | ? | <quote or example> | Does this make the sharer look good? |
   | Triggers | ? | <quote or example> | What everyday cue connects to this? |
   | Emotion | ? | <quote or example> | Awe, anxiety, excitement, anger? |
   | Public | ? | <quote or example> | Visibility layer present? |
   | Practical Value | ? | <quote or example> | Actionable, specific, saves time? |
   | Stories | ? | <quote or example> | Narrative with tension + resolution? |

   Total: ?/18
   Top 2 elements: <element>, <element>
   Weakest element: <element>
   ```

   If the total is below 9/18, flag: "This piece scores low on shareable elements. Here is what would help: [specific suggestions per weak element]." Offer to strengthen before repurposing.

3. **Extract the spine.** Identify:
   - **The one sentence** (the thesis or core insight)
   - **3-5 supporting points** (the substructure)
   - **The killer line** (the most quotable sentence)
   - **The data points** (numbers, examples)
   - **The contrarian angle** (what the source disagrees with)
   - **The narrative thread** (the story inside the content, if any)

   Show this to the user before producing assets. Get confirmation.

4. **Map each asset to its STEPPS element.** Before writing, confirm the STEPPS target for each channel:

   ```
   Asset STEPPS Map

   LinkedIn post        → Social Currency (makes sharer look insightful)
   LinkedIn carousel    → Practical Value + Social Currency (actionable + impressive)
   Twitter/X thread     → Practical Value (specific, step-by-step, saves time)
   Substack note        → Stories + Emotion (narrative hook, emotional pull)
   Email teaser         → Triggers + Emotion (tap a recurring cue + emotional spike)
   Reddit post          → Practical Value (genuine help, no promo feel)
   Quote graphics       → Emotion + Social Currency (striking + shareable identity signal)
   YouTube short        → Stories + Emotion (narrative, visual, emotional arc)
   SEO snippet          → Practical Value (answers question directly, useful)
   ```

5. **Produce each channel asset.** For each one, include a one-line STEPPS note at the top of the file:

   ```
   <!-- STEPPS target: Social Currency — this post is designed to make the sharer
   look ahead of the curve on [topic]. The hook uses [specific element] to signal
   insider knowledge. -->
   ```

   Each asset must be:
   - **Native to the channel** (not a copy-paste with different word count)
   - **Stand-alone valuable** (works without the source)
   - **Optimized for its primary STEPPS element** (named explicitly)
   - **Linked back to the source** if appropriate (CTA at the end)

6. **Save** all outputs as separate files in `output/repurposed/<DD-MM-YYYY>-<source-slug>/`:
   ```
   output/repurposed/25-04-2026-thoughts-on-ai-pm/
   ├── linkedin-post.md
   ├── linkedin-carousel.md
   ├── twitter-thread.md
   ├── substack-note.md
   ├── email-teaser.md
   ├── reddit-post.md
   ├── quote-graphics.md
   ├── youtube-short.md
   └── README.md
   ```

7. **Generate the README.md** for the folder summarizing:
   - Source link or path
   - STEPPS score table
   - Spine (one sentence + 3 points)
   - Which STEPPS element each asset targets
   - Whether the pack covers at least 4 of 6 STEPPS elements
   - Where each asset is meant to be published
   - Suggested publishing sequence and cadence

8. **Self-check: STEPPS coverage.** The asset pack as a whole must cover at least 4 of 6 STEPPS elements. If it doesn't, name which are missing and suggest one asset type that would fill the gap.

   ```
   STEPPS Coverage Check

   Social Currency  - covered by LinkedIn post
   Triggers         - covered by email teaser
   Emotion          - covered by quote graphics, YouTube short
   Public           - NOT COVERED (suggest: add a screenshot-friendly stat for the carousel)
   Practical Value  - covered by Twitter thread, carousel, Reddit post
   Stories          - covered by Substack note, YouTube short

   Coverage: 5/6 - PASS
   ```

## Channel-specific rules

### LinkedIn post (Social Currency)
- Open with an insight, not an announcement. Sharers want to look smart.
- The hook should be a claim someone would disagree with at first, then agree with after reading.
- End with a takeaway the reader can quote in their next meeting.

### LinkedIn carousel (Practical Value + Social Currency)
- Slide 1: hook (8-12 words, big text)
- Slide 2: setup (the problem or context)
- Slides 3-7: one point per slide
- Last slide: CTA + tag line
- Output: structured outline ready for design ("Slide 3: Title 'X', body bullets, visual: graph showing Y")

### Twitter/X thread (Practical Value)
- Tweet 1: hook only, no thread emoji
- Tweets 2-N: one actionable idea per tweet, max 280 chars each
- No "1/", use natural numbering only if it adds clarity
- Last tweet: payoff and CTA (link, follow, save)
- Practical Value = specific, actionable, saves time. Not opinion. Not commentary.

### Substack note (Stories + Emotion)
- 3-5 sentences max
- Lead with a moment, not a point. Start mid-scene.
- One contrarian or counterintuitive claim
- The emotional payoff should land in the last sentence
- Link to full piece at the end

### Email teaser (Triggers + Emotion)
- Subject line should connect to a recurring situation the reader faces (the trigger)
- Body opens with the emotional spike, not the content summary
- CTA is one click, zero friction

### Reddit (Practical Value)
- Suggest 2-3 specific subreddits
- Adapt voice: less promotional, more conversational
- Lead with value, not the link
- Include "(I wrote about this in more depth here)" only at the end
- Flag any community rules to check (no self-promo, etc.)

### YouTube short (Stories + Emotion)
- 45-60 seconds spoken (~120-150 words)
- Hook in 3 seconds - start with tension, not context
- One insight, one example, one takeaway
- Emotional arc: problem felt, resolution shown
- Visual cue suggestions in [brackets]

### Quote graphics (Emotion + Social Currency)
- 3-5 pull quotes
- Each under 140 chars
- Each works without context
- High-arousal only: awe, anxiety, excitement. Cut contentment quotes.
- Specify which is best for which platform (LinkedIn carousel cover vs Instagram quote vs Twitter image)

## Rules

- Never paraphrase the source word for word. Each asset must add framing or context appropriate to its channel.
- Never produce identical content with different word counts. A 220-word LinkedIn post is structurally different from a 220-word Substack note.
- The source's killer line should appear in at least one derivative, often the LinkedIn post or a quote graphic.
- If the source has no killer line, flag it: "I cannot find a quotable line. Want me to write one or skip the quote graphics?"
- Each asset file must include its STEPPS target as a comment at the top.
- If the STEPPS score is below 9/18, address it with the user before producing 9 assets from weak source material.

## Quick Reference: STEPPS

| Element | Channel fit | What to amplify |
|---|---|---|
| Social Currency | LinkedIn post, quote graphics | Make the sharer look smart or ahead of the curve |
| Triggers | Email teaser, carousel | Connect to a cue the reader encounters regularly |
| Emotion (high-arousal only) | Quote graphics, YouTube short, Substack note | Awe, anxiety, excitement, anger - not contentment |
| Public | Carousel, thread | Add visible social proof or community signal |
| Practical Value | Thread, Reddit, carousel, SEO snippet | Specific, actionable, saves time |
| Stories | Substack note, YouTube short | Tension + resolution. Start mid-scene. |
