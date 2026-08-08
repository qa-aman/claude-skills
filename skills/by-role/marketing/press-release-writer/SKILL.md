---
name: press-release-writer
description: Write press releases for product launches, funding announcements, partnerships, executive hires, and milestones using the Inverted Pyramid (AP journalism) and Ogilvy on Headlines (David Ogilvy, Ogilvy on Advertising). The lede answers Who/What/When/Where/Why in 40 words or fewer. The headline selects the right audience and promises a specific benefit. Use when the user asks for a press release, media release, news announcement, PR for X, launch announcement, funding announcement, or "write a press release". Reads brand voice and positioning from knowledge/. For pitching it to a journalist, see pr-pitch-writer. For the customer story behind it, see case-study-writer.
metadata:
  grounded_in:
    - "Inverted Pyramid - AP journalism"
    - "Ogilvy on Advertising - David Ogilvy"
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

### Inverted Pyramid (AP journalism)

Put the most important information first, then supporting details, then background. The structure
exists because of how newsrooms work: journalists scan, and editors cut from the bottom to fit
space. If the news is in paragraph 4, it does not survive the cut.

| Level | Paragraphs | Contains | Word budget | Survives an editor's cut? |
|---|---|---|---|---|
| **Lede** | 1 | Who, what, when, where, why - the whole story | 40 or fewer | Never cut |
| **Supporting detail** | 2 to 3 | Why now, the problem solved, first quote | 50 to 80 each | Usually kept |
| **Background** | 4 to 6 | Specifics, deal terms, second quote, what is next | 30 to 80 each | Cut when space is tight |
| **Boilerplate** | last | About the company | 50 to 80 | Cut first, every time |

Two tests, both run on the finished draft:

1. **Lede test**: can someone read only the first paragraph and understand the full story? If not, rewrite the lede rather than adding to paragraph 2.
2. **Cut-from-the-bottom test**: delete the last 2 paragraphs. Is the story still complete and accurate? It must be. If deleting them removes a fact the story needs, that fact is in the wrong place.

### Ogilvy on Headlines (*Ogilvy on Advertising*, David Ogilvy, 1983)

"On average, five times as many people read the headline as read the body copy." Ogilvy's point is
that the headline is not a title, it is the ad. In a press release the headline is what decides
whether a journalist opens the email at all.

| Ogilvy rule | Applied to a press release | Fails when |
|---|---|---|
| The headline selects the audience | The reader knows in one line whether this is their beat | It names the company and nothing else |
| The headline promises a benefit or creates curiosity | It states what someone can now do | It labels the topic: "Company Announces Product Update" |
| Never a blind headline | No wordplay the reader must decode | A pun carries the news |
| Specifics beat generalities | The round size, the number, the named thing | "Significant funding", "major partnership" |

Ogilvy's best-performing headline formulas, in the order worth trying for a release:

1. **News**: announces something genuinely new, using a specific verb: Introduces, Launches, Names, Raises, Acquires
2. **How-to**: "How [company] [does X] for [audience]" - strongest for product launches with a clear job
3. **Command**: "Reduce [pain] by [specific amount]" - only with a number the user has supplied
4. **Question**: a question the target audience asks themselves - weakest here, because news beats curiosity for a journalist on deadline

Press release headline formula (AP plus Ogilvy combined):
`[Company] [verb: announces/launches/names/raises] [specific thing], [immediate benefit or impact]`

Example: "Threadline Raises $32M Series B to Help PLG Teams Ship Onboarding Without Engineering"
- Audience selected: PLG teams
- Benefit stated: ship onboarding without engineering
- News verb used: Raises
- Specific: $32M, Series B

The example above is a fictional company used to show the shape of the formula. Never carry any
figure from it into a real release.

## Before you draft: is there enough to announce?

A press release with a thin news hook does not fail quietly, it burns a journalist relationship.

| Signal | Threshold | If below |
|---|---|---|
| Attributed quotes supplied by the user | 2, one internal and one external | Draft with `[QUOTE NEEDED FROM <Name>, <Title>]` in place and tell the user the release cannot go out until both are real |
| Hard facts: figures, dates, names, titles | All confirmed by the user | Stop on the unconfirmed one. Ask. Never draft a round size, a customer count, a founding year, or an HQ city |
| Boilerplate in `knowledge/company.md` | Present | Ask the user for it. Do not assemble one from the positioning doc, because boilerplate is a legal and factual statement, not marketing copy |
| Something a reader can do or get that they could not before | 1 required | Say plainly that this is an internal milestone, not news, and offer a LinkedIn post or a customer email instead. That is a better outcome than a release nobody covers |

Warning signs, in priority order:

1. The headline needs the subheadline to make sense. The headline is doing labelling, not news.
2. Every number in the draft came from the skill rather than the user. Stop and get them confirmed, one by one.
3. The lede is the headline rewritten. It must add the five Ws the headline omits.
4. The most interesting sentence is in paragraph 5. The pyramid is upside down, so restructure before polishing.

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
- **Boilerplate**: pull from `knowledge/company.md`. If missing, **ask the user** - never draft a founding year, HQ city, customer name or scale figure. The same never-invent rule applies to every number in the release.
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

6. **Self-check.** Every item is checkable against the draft itself. Where an item names a number,
   count it rather than asserting it.

   - [ ] Headline: name the audience it selects and the benefit it promises, in the working notes. If either cannot be named from the headline alone, rewrite it
   - [ ] Headline verb is one of the specific news verbs, and the headline is 60 to 80 characters. Count them
   - [ ] Lede: count the words. 40 or fewer, and each of the five Ws is present. Mark which clause carries each W
   - [ ] Lede test run: read paragraph 1 alone and write the one-sentence story it gives. If it is missing a W, the lede fails
   - [ ] Cut-from-the-bottom test run: delete the last 2 paragraphs and confirm no fact the story needs disappeared
   - [ ] Exactly 2 or more quotes, each with a full name, a title and an organisation. Every quote is either supplied by the user verbatim or is a `[QUOTE NEEDED FROM ...]` placeholder. Count the placeholders and state the count to the user
   - [ ] Every figure in the draft traces to a user-supplied fact or `knowledge/company.md`. List the figures and their sources in the working notes
   - [ ] Boilerplate present, last, and taken from `knowledge/company.md` unedited
   - [ ] Press contact block has a name and an email
   - [ ] Search the body for "we", "our" and "us" outside quotation marks. Zero hits
   - [ ] Total length 400 to 600 words. Count them
   - [ ] Search the body for the banned marketing words: revolutionary, industry-leading, best-in-class, game-changing, seamless, robust, cutting-edge. Zero hits outside quotes

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
- **Never invent a number.** Round sizes, valuations, customer counts, ARR, headcount, uptime, percentage improvements, founding year, HQ city. Every one is a factual claim in a public document that a journalist may verify and a regulator may read. Unsupplied is `[NEEDS INPUT: <the exact fact>]`, never an estimate.
- Never invent a name, a title, an investor, or a partner organisation, and never adjust a supplied title to sound better. Titles in a release are checked.
- Never soften a placeholder to make the draft read smoothly. A draft that reads finished but contains an invented quote is the worst artifact this skill can produce, because it is the one most likely to be published as-is.
- Do not write a customer name into the release without confirming the customer has approved being named.

## Files this skill reads and writes

This skill writes to `output/press-release/` only. It has no shared-knowledge write path and no
ownership collision with any sibling skill, which is deliberate: a release is a dated artifact, not
canon.

| File | Access | Owner |
|---|---|---|
| `knowledge/company.md` | Read only, and boilerplate is copied unedited | `/brand-context` |
| `knowledge/brand/voice.md` | Read only | `/brand-context` |
| `knowledge/markets/positioning.md` | Read only | `/positioning-doc` |
| `output/press-release/<DD-MM-YYYY>-<slug>.md` | Write | This skill |

If the boilerplate in `knowledge/company.md` is wrong or stale, say so and route the user to
`/brand-context`. Do not correct it from here, and do not write a better version into the release
while leaving the knowledge file untouched, because the next release would then disagree with this
one.

## What this skill cannot know

These are the limitations that bite in practice. Where one applies to the artifact, write it into the document as an open question rather than leaving the reader to assume it was verified.

1. **Whether the news is legally clear to announce.** Funding rounds, acquisitions, customer names and executive departures usually need counsel, investor or customer sign-off. This skill has no visibility into what has been cleared.
2. **Whether a journalist will care.** Newsworthiness depends on the beat, the week, and what else is announcing that day. The structure here maximises the chance a release survives a scan, and it cannot manufacture a hook that is not in the facts.
3. **Whether the supplied figures are accurate or current.** The skill can refuse to invent a number and can demand a source. It cannot audit one.
4. **Embargo mechanics.** Whether an outlet honours an embargo, and what was promised to whom, lives in the relationship, not in the document. Confirm the time and timezone with the user explicitly, and never assume one.

## Related skills

- `/pr-pitch-writer` for the email that puts this release in front of a journalist, and it is what actually gets it read
- `/case-study-writer` for the customer story a launch release should point to, when the proof is a customer outcome rather than a figure
- `/brand-context` for creating or fixing the `knowledge/company.md` boilerplate this skill copies unedited
- `/positioning-doc` for when the release keeps describing the product differently from the positioning file
- `/linkedin-post` for the founder or executive announcement post that runs alongside the release
- `/social-calendar` for scheduling the announcement day across channels once the embargo time is fixed
- `/thought-leadership-writer` for when the check above found an internal milestone rather than news, and the story is better told as a point of view
