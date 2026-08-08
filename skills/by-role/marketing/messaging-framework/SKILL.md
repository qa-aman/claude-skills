---
name: messaging-framework
description: >-
  Build a brand messaging framework or messaging hierarchy. Use when the user says
  "messaging framework", "brand messaging", "what should our tagline be", "clarify our
  messaging", "StoryBrand", "brand script", "our website copy is confusing", "we need
  a messaging hierarchy", "homepage messaging", "value prop copy", or wants to create
  consistent, clear messaging that converts visitors into customers.
  For the underlying positioning, see positioning-doc. For applying the message to a page, see landing-page-writer. For checking live copy against it, see copy-review.
metadata:
  grounded_in:
    - "Building a StoryBrand - Miller"
  reads:
    - knowledge/brand/voice.md
    - knowledge/icp/personas.md
    - knowledge/markets/positioning.md
  writes:
    - knowledge/markets/positioning.md
    - output/messaging-framework/
---

## Overview

Based on **"Building a StoryBrand"** by Donald Miller (2017). Miller's core claim is that companies
lose customers because they force the customer to burn calories working out what is on offer, and
that story is the one structure the brain processes without effort. The fix is to cast the customer
as the hero and the brand as the guide. This skill produces a reusable brand script and messaging
hierarchy that the writing skills downstream all draw from.

## Where this method comes from: the SB7 framework

Miller's SB7 is seven story beats in a fixed order. The order is the method: a guide who appears
before the problem has nothing to be a guide about, and a call to action before the plan asks the
customer to jump a gap they cannot see. All seven are worked in the steps below.

| SB7 beat | The question | Worked in | Most common failure |
|---|---|---|---|
| 1. A character | What does the customer want? | Step 1 | Stating what the product does instead |
| 2. Has a problem | External, internal, philosophical | Step 2 | Only the external one is ever written |
| 3. Meets a guide | Empathy plus authority | Step 3 | The brand casts itself as the hero |
| 4. Who gives a plan | 3 steps, no more | Step 4 | A 7-step onboarding diagram |
| 5. And calls them to action | Direct plus transitional | Step 5 | "Learn more" as the only button |
| 6. That helps avoid failure | What is at stake if nothing changes | Step 6 | Omitted entirely, so there is no urgency |
| 7. And ends in success | The specific after-state | Step 6 | Abstractions like "growth" |

Miller's villain rule sits under beat 2: name one villain, make it a single thing the customer can
picture, and make it something the product actually defeats. "Inefficiency" is not a villain.
"Four tools that do not talk to each other" is.

## Before you write: is the input strong enough?

| Signal | Threshold | If below |
|---|---|---|
| `knowledge/brand/voice.md` exists and names words to use and avoid | Present | Run `/brand-context` first. Without it the output is on-message and off-voice, which is harder to fix than a blank page |
| `knowledge/markets/positioning.md` carries a positioning statement | Present | Run `/positioning-doc` first. Messaging without a position is decoration on an undecided claim |
| Real customer phrasings available for Step 1 and Step 2 | 3 minimum | Proceed, but mark every want and problem `[ASSUMED]`. Never present desk-invented phrasing as customer language |
| Sourced authority proof points for Step 3 | 1 minimum | Ship with what exists. Never invent a customer count, a years-in-business figure, or a testimonial |

Warning signs, in priority order:

1. The one-liner works equally well for a competitor. The positioning underneath it is not differentiated, so stop and fix `/positioning-doc` rather than rewording.
2. Step 2's internal problem is a restatement of the external one. That means no one has spoken to a customer.
3. The plan needs more than 3 steps to make sense. Either the product is genuinely complex, which is a product finding worth reporting, or the steps are being written from the company's process rather than the customer's experience.
4. Every proof point in Step 3 is a superlative rather than a number or a named customer. Authority is evidence, not adjectives.

## Workflow

### Step 1: Identify the customer's primary want

Miller's first SB7 element: what does the character (customer) want? Not what your product does - what does the customer want to achieve, feel, or become?

Write one clear sentence: "[Your audience] wants [specific desired outcome]."

Avoid outcomes that are too abstract ("success", "growth") or too narrow ("a faster dashboard"). Aim for the level of "close more deals without a bigger team" or "ship features without breaking production."

### Step 2: Define the three levels of problem

Every customer has problems at three levels. Surface all three:

- **External problem** - the tangible, observable problem. Example: "Our sales team is manually logging calls in the CRM."
- **Internal problem** - the feeling the external problem creates. Example: "I feel like my team is wasting time on admin instead of selling."
- **Philosophical problem** - the sense of injustice. Example: "Salespeople should be selling, not doing data entry."

Great messaging speaks to all three, but especially the internal. Most brands only address the external.

### Step 3: Position your brand as the guide

The customer is the hero. Your brand is Yoda, not Luke. Two things make a guide credible:

- **Empathy** - show you understand the internal problem. "We know how frustrating it is when..."
- **Authority** - evidence you can help. Stats, testimonials, years of experience, number of customers.

Write 1-2 sentences for each. These become the "About" or trust section of any asset.

### Step 4: Write the plan (3 steps)

Miller: customers do not take action when the path is unclear. Reduce their perceived risk by giving them a 3-step plan. Not 5 steps, not 7. Three.

```
Step 1: [simple action verb + object]
Step 2: [simple action verb + object]
Step 3: [outcome they experience]
```

Example: "1. Book a 20-minute demo. 2. Get a custom setup in one day. 3. Close deals faster from week one."

### Step 5: Write the direct and transitional calls to action

- **Direct CTA** - asks for the sale or commitment. "Start free trial", "Book a demo", "Get a quote."
- **Transitional CTA** - builds trust before commitment. "Download the guide", "See how it works", "Read case studies."

Every page needs both. The direct CTA is primary. The transitional CTA captures people who are not ready yet.

### Step 6: Name the failure and the success

The two SB7 beats most often dropped. Without stakes there is no reason to act now, and without a
specific after-state there is nothing to buy.

- **Failure** - what stays true if they do nothing. Write 2 to 3 consequences, each concrete and each one the product genuinely prevents. Threat inflation is the trap here: if the consequence is not real, the copy reads as fear-selling and the reader discounts everything around it.
- **Success** - the after-state, in the customer's words. One sentence, observable. "The Monday report is done before the standup" beats "improved efficiency".

Never quantify either with a figure the user has not supplied. `[NEEDS INPUT: measured outcome]` is
the correct placeholder.

### Step 7: Assemble the brand script and messaging hierarchy

```
ONE-LINER
[Your brand] helps [audience] [achieve outcome] by [unique method].

TAGLINE
[Short phrase that encapsulates the primary want - under 8 words]

HOMEPAGE HERO COPY
Headline: [external problem or desired outcome - plain language]
Subhead: [who it is for + how it works + what they get]
Primary CTA: [direct CTA button text]
Secondary CTA: [transitional CTA link text]

VALUE PROP SECTION
[3 benefit statements, each tied to the external, internal, or philosophical problem]

STAKES SECTION
[What stays true if nothing changes - 2-3 consequences]
[Success after-state - one observable sentence]

TRUST SECTION
[Empathy statement + 2-3 authority proof points, each with its source named inline]
```

## Anti-Patterns

**1. Making the brand the hero**
Bad: "We built the most advanced AI platform in the industry, with 10 years of R&D."
Good: "[Your audience] closes more deals without adding headcount." (Add a figure only if `knowledge/company.md` or the user supplies one. Never estimate a customer outcome.)
The customer does not care about your journey. They care about their outcome.

**2. Burying the offer**
Bad: A homepage that explains your company history before the product.
Good: The headline names the customer's want or problem within 5 seconds of arrival.

**3. Weak or absent CTA**
Bad: "Learn more" as the only button on the page.
Good: Direct CTA ("Start free trial") and transitional CTA ("See a 3-minute demo") both present.

**4. More than 3 steps in the plan**
*Building a StoryBrand* treats the plan as risk reduction, so every extra step adds back the
perceived risk the plan exists to remove.
Bad: "Here are our 7 steps to onboarding."
Good: "1. Sign up. 2. Connect your data. 3. Get your first report in 10 minutes."
More steps signal complexity. Complexity kills conversion.

## Self-check

Each item is checkable by reading the finished framework. Count what the item says to count.

- [ ] Primary customer want is one sentence with one outcome in it, not a list joined by "and"
- [ ] All three problem levels are present, and the internal problem uses different words from the external one, not a paraphrase
- [ ] A single named villain appears in Step 2 and is something the product demonstrably defeats
- [ ] Step 3 has an empathy statement and at least one authority proof point, and every proof point names its source inline or is written `[NEEDS INPUT: <what evidence>]`
- [ ] The plan is exactly 3 numbered steps. Count them
- [ ] Both a direct CTA and a transitional CTA exist, and the direct CTA is a verb phrase, not "Learn more"
- [ ] Failure section lists 2 to 3 consequences and success is one observable sentence
- [ ] One-liner fills all four template blanks and is under 25 words
- [ ] Homepage hero block has all four fields filled: headline, subhead, primary CTA, secondary CTA
- [ ] Every word marked "avoid" in `knowledge/brand/voice.md` is absent from the customer-facing copy. Grep the draft against that list rather than asserting it
- [ ] The one-liner has been tested by swapping in a competitor's name. If it still reads true, that is recorded and escalated to `/positioning-doc`

## What this skill cannot know

These are the limitations that bite in practice. Where one applies to the artifact, write it into the document as an open question rather than leaving the reader to assume it was verified.

1. **Whether this is actually how customers describe their problem.** Miller's internal and philosophical problems come from listening, not deduction. Without transcripts this skill produces plausible phrasing, and plausible phrasing tests worse than real phrasing every time.
2. **Whether the message converts.** SB7, the framework *Building a StoryBrand* sets out, is a clarity framework, not a performance prediction. Only a live test through `/page-cro` or `/ab-copy-writer` decides between two clear messages.
3. **Whether the authority claims are safe to publish.** Customer counts, uptime figures, and named logos usually need legal or customer sign-off, which this skill has no visibility into.
4. **Whether the plan's 3 steps match the real onboarding.** If the product genuinely takes seven steps, a 3-step plan on the homepage is a promise the product breaks in week one. Confirm the steps against how onboarding actually runs.

## Context and output

**Before you start.** Read `knowledge/brand/voice.md` for tone and vocabulary rules, `knowledge/icp/personas.md` for the pains the message must answer, and `knowledge/markets/positioning.md` for the claim it must carry. If voice is missing, run `/brand-context` first, otherwise the output will be on-message and off-voice.

**When you finish.** Save to `output/messaging-framework/<DD-MM-YYYY>-<company-slug>.md` with YAML frontmatter carrying the date, the skill name, and the key decisions made.

## Shared file ownership: knowledge/markets/positioning.md

**`/positioning-doc` owns `knowledge/markets/positioning.md`.** This skill is an appender to that
file, not its author.

| Section of the file | This skill may |
|---|---|
| `## Message hierarchy` (one-liner, tagline, hero copy, value props, stakes, trust) | Create it, or replace it in full |
| Positioning statement, competitive alternatives, differentiators, owned attributes, proof points | Read only. Never edit, reword, or delete, even when the wording feels weak |

If the positioning sections look wrong, say so and route the user to `/positioning-doc`. Do not fix
them here. A message hierarchy silently contradicting the positioning statement above it in the same
file is the worst outcome available, because every downstream skill reads both.

The write gate, which is not optional:

1. Show the user a diff of the exact `## Message hierarchy` lines you would add or replace, and wait for an explicit yes before writing. Several other marketing skills read this file as truth.
2. If the positioning sections are missing, or 3 or more of the wants and problems are marked `[ASSUMED]`, do not offer the write. Save to `output/` only and say the hierarchy is not yet canon.
3. Never invent a customer phrasing, a testimonial, a customer count, or an outcome figure to complete a section. `[NEEDS INPUT: <what would fill it>]` is the correct output.

## Related skills

- `/positioning-doc` for defining the claim this expresses, and it must run first. This skill cannot resolve a contradiction it finds in the positioning
- `/brand-context` for creating the voice, persona and positioning files this reads, when the knowledge base is empty
- `/customer-research` for when Step 1 and Step 2 have no real customer language behind them
- `/landing-page-writer` for turning the hero block and value props into a full page
- `/content-writer` for applying the same hierarchy to blog and long-form work
- `/copy-review` for checking whether live copy still matches the hierarchy after it changes
- `/ab-copy-writer` for testing two headlines when SB7 leaves a genuine tie
