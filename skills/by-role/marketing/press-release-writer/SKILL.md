---
name: press-release-writer
description: Write press releases for product launches, funding announcements, partnerships, executive hires, and milestones using the Inverted Pyramid (AP journalism) and Ogilvy on Headlines (David Ogilvy, Ogilvy on Advertising). The lede answers Who/What/When/Where/Why in 40 words or fewer. The headline selects the right audience and promises a specific benefit. Use when the user asks for a press release, media release, news announcement, PR for X, launch announcement, funding announcement, or "write a press release". Reads brand voice and positioning from knowledge/.
reads:
  - knowledge/company.md
  - knowledge/brand/voice.md
  - knowledge/markets/positioning.md
  - knowledge/services/
writes:
  - output/press-release/
---

# press-release-writer

Writes press releases in AP style using the Inverted Pyramid structure and Ogilvy's headline principles. Optimized for journalists who scan, not read. The most important information is always first. The headline selects the right audience and promises a concrete benefit - not a label.

## Framework: Inverted Pyramid + Ogilvy on Headlines

### Inverted Pyramid
Put the most important information first. Then supporting details. Then background.

Why: journalists scan. Editors cut from the bottom. If the most important news is in paragraph 4, it will not get published or read.

The levels:
1. **LEDE** (first paragraph): answers Who, What, When, Where, Why - the entire story in 40 words or fewer. Someone reading only this should understand the full story.
2. **SUPPORTING DETAILS** (paragraphs 2-3): the most important context, quotes, proof
3. **BACKGROUND** (paragraphs 4-5): company boilerplate, secondary details, additional context
4. **BOILERPLATE** (final paragraph): standard "about the company" - editors cut this first

Lede test: can someone read ONLY the first paragraph and understand the full story? If not, rewrite the lede.

Cut-from-the-bottom test: if an editor cut the last 2 paragraphs, is the story still complete and accurate? It must be.

### Ogilvy on Headlines
"On average, five times as many people read the headline as read the body copy." (Ogilvy on Advertising)

Rules:
- The headline must select the right audience - readers self-qualify from the headline alone
- The headline must promise a benefit or create curiosity - not just label the topic
- Never a "blind headline" - the reader should know what they're getting
- No puns, no wordplay that obscures the news

Ogilvy's best-performing headline formulas:
- How-to: "How [company] [does X] for [audience]"
- News: announces something genuinely new, uses "Introduces", "Launches", "Names"
- Question: a question the target audience asks themselves
- Command: "Reduce [pain] by [specific amount]"

Press release headline formula (AP + Ogilvy combined):
`[Company] [verb: announces/launches/names/raises] [specific thing], [immediate benefit or impact]`

Example: "Threadline Raises $32M Series B to Help PLG Teams Ship Onboarding Without Engineering"
- Audience selected: PLG teams
- Benefit stated: ship onboarding without engineering
- News verb used: Raises
- Specific: $32M, Series B

## When to use

- "Write a press release for our Series B"
- "Draft a media release announcing the partnership with X"
- "Write the launch announcement for <product>"
- "We need a press release for the new CMO hire"

## Release types this skill handles

- Product launch
- Funding round
- Partnership / integration
- Executive hire or appointment
- Customer milestone (Xth customer, $Y ARR, etc.)
- Acquisition (buyer side or sell side)
- Award or certification

## Inputs needed (ask if missing)

- **Type** of release (from list above)
- **Headline news** (the one sentence)
- **Date and dateline city**
- **Key facts**: numbers, names, titles, dates
- **Quote 1** (executive at company): name, title, full quote
- **Quote 2** (external: investor, partner, customer, board): name, title, organization, full quote
- **Boilerplate**: pull from `knowledge/company.md`. If missing, draft one.
- **Press contact**: name, email

If quotes are missing, ask. Never invent.

## Process

1. **Load context.** Read `knowledge/company.md`, `knowledge/brand/voice.md`, `knowledge/markets/positioning.md`.

2. **Write the headline first using Ogilvy's formula.**
   - Identify the audience: who is this news for?
   - Identify the benefit: what can they now do or get that they could not before?
   - Apply the formula: `[Company] [verb] [specific thing], [immediate benefit]`
   - Self-check: does the headline select the right audience? Does it promise a specific benefit? Is the news verb specific (not "announces exciting update")?

3. **Write the lede.** One paragraph, 40 words or fewer. Must answer: Who, What, When, Where, Why.
   Apply the lede test: someone reading only this paragraph should understand the full story.

4. **Write the release in Inverted Pyramid structure**:

   ```
   FOR IMMEDIATE RELEASE

   <Headline: Ogilvy formula applied. 60-80 chars, sentence case, news-led, benefit-stated>
   <Subheadline: 100-130 chars, adds the "why this matters">

   <DATELINE CITY, DD-MM-YYYY> -- <Lede: 30-40 words. Who, what, when, where, why. Full story in one paragraph.>

   <Paragraph 2: 50-80 words. The most important supporting context. Why now? What problem does this solve? Include one supporting stat if available.>

   <Quote 1: from company executive. Full attribution: "Quote," said <Name>, <Title> at <Company>. "Continued quote." 40-60 words total.>

   <Paragraph 4: 50-80 words. Specifics. Product details, deal terms, timeline. Likely paragraph to be cut by editors - make it skippable without breaking the story.>

   <Quote 2: from external party. Same attribution format. 30-50 words.>

   <Paragraph 6: 30-50 words. What's next. Availability, rollout plan, how to learn more.>

   ###

   About <Company>
   <Boilerplate from knowledge/company.md, 50-80 words. Name, what they do, founded, HQ, notable customers or scale, website.>

   Press contact:
   <Name>
   <Title>
   <Email>
   <Phone if provided>
   ```

5. **Style rules**:
   - AP style: spell out numbers under 10, use figures for 10+
   - Dates: spell out month in the body, e.g. "April 25, 2026" (AP requires this; use DD-MM-YYYY for filename and frontmatter only)
   - Titles capitalized only before names ("Chief Executive Officer Jane Doe" but "Jane Doe, chief executive officer")
   - No exclamation points
   - No marketing language in the body ("revolutionary", "industry-leading", "best-in-class")
   - Past tense for the news ("announced today")
   - Active voice

6. **Self-check**:
   - Headline: does it select the right audience? Does it promise a specific benefit? Is the news verb specific?
   - Lede: does it answer all 5 Ws in 40 words or fewer? Lede test passed?
   - Cut-from-the-bottom test: cut the last 2 paragraphs - is the story still complete?
   - Two quotes minimum, both attributed
   - Boilerplate present (and last - editors cut it first)
   - Press contact present
   - No first-person voice anywhere except inside quotes
   - Length: 400-600 words
   - No marketing language in the body

7. **Save** to `output/press-release/<DD-MM-YYYY>-<slug>.md` with frontmatter:
   ```yaml
   ---
   format: press-release
   type: <launch|funding|partnership|hire|milestone|acquisition|award>
   headline: <full headline>
   embargo: <none|until DD-MM-YYYY HH:MM TZ>
   created: DD-MM-YYYY
   ---
   ```

8. **Offer companion assets**:
   - Email pitch to journalists (3 sentences + the release attached)
   - LinkedIn announcement post
   - Internal Slack message
   - Customer email if relevant

## Rules

- Never invent quotes. If the user does not have a quote yet, leave a placeholder: `[QUOTE NEEDED FROM <Name>, <Title>]` and tell the user.
- Never embargo without confirming the embargo time and timezone explicitly.
- For funding announcements, confirm the round size, lead investor, and use of funds with the user before drafting. These are factual claims that cannot be wrong.
- For executive hires, confirm the start date, prior role, and reporting line.
- The lede is not the headline rewritten. It must add the 5 Ws that the headline omits.
- If the most important information is not in the first paragraph, the structure is wrong - fix it before saving.
