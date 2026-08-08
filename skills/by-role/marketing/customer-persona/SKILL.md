---
name: customer-persona
description: >-
  Build a detailed buyer persona or customer profile. Use when the user says "write a
  persona", "build a buyer persona", "customer persona for [product]", "who is our target
  customer", "ICP document", "ideal customer profile", "define our buyer", "who are we
  building this for", "customer profile", "audience profile", or wants to create a
  documented, research-backed profile of who buys the product and why.
  For sourcing the real research behind a persona, see customer-research. For segment and firmographic definition, see icp-research. For writing it into the knowledge base, see brand-context.
metadata:
  grounded_in:
    - "Obviously Awesome - April Dunford"
  reads:
    - knowledge/icp/personas.md
    - knowledge/markets/positioning.md
  writes:
    - knowledge/icp/personas.md
    - output/customer-persona/
---

## Overview

Based on **"Obviously Awesome"** by April Dunford (2019). Traditional personas collect demographics
and job titles. Dunford's argument is that the useful unit is buying context: the situation at the
moment of purchase, the alternatives that were on the table, and the value that made switching worth
the friction. A persona without buying context produces marketing that reaches the right person with
the wrong message.

## Where this method comes from

Dunford's five positioning components are usually applied to a product. This skill applies them to a
single buyer, because her fourth component, "customers who care a lot", is the persona question. The
components she treats as universal (alternatives, attributes, value) become segment-specific here,
and that is the whole point: the same capability is worth different amounts to different buyers.

| Dunford component | Applied to one buyer | Worked in |
|---|---|---|
| Competitive alternatives | What this buyer actually evaluated, including doing nothing | Step 2 |
| Unique attributes | Which capabilities this buyer noticed at all | Step 4 |
| Value | Why those capabilities mattered to this buyer specifically | Step 4 |
| Customers who care a lot | The trigger that made the value urgent, not merely nice | Step 2 |
| Market category | The frame this buyer already had in their head when they searched | Step 3 |

Dunford's line that positioning is context-setting is what makes the trigger mandatory here. The
trigger is the buyer's context. Without it, everything else in the persona is a description of a job
title.

## Before you write: is the input strong enough?

A persona is written once and read for a year, and it lands in a shared knowledge file. Weak input
is not a reason to write it more carefully, it is a reason not to write it.

| Signal | Threshold | If below |
|---|---|---|
| Distinct customer conversations, sales calls, or win/loss records behind this persona | 5 minimum to enter the shared file. 10 or more for `confidence: high`, 5 to 9 for `medium` | Below 5, mark `confidence: low` and write to `output/` only, never to the shared knowledge file |
| Real objections captured in the customer's own words | 3 | Write the ones you have. Never fill the remaining slots from the desk. `[NEEDS INPUT: real objection]` is correct |
| A named trigger event for this persona | 1 required | Stop. Run `/customer-research` first. A persona with no trigger is a demographic profile with extra formatting |
| Alternatives this buyer actually evaluated | 2 | Proceed and mark `[ASSUMED]`, but say clearly the switching story is unverified |

Warning signs, in priority order:

1. The objections were written by whoever is writing the persona. That is the single highest-harm failure here, because `/copy-review` and `/landing-page-writer` will answer objections no buyer has.
2. The persona spans two seniority levels or two company stages. That is two personas being averaged, and the average matches nobody.
3. The trigger is a state ("they are growing") rather than an event ("headcount crossed 50 and Notion stopped holding the workflow"). States do not start buying processes.
4. Every capability in Step 4 is rated as high value. Nothing was prioritised, so the map cannot be used to decide what to lead with.

## Workflow

### Step 1: Identify the persona's label and segment

Give the persona a specific, descriptive label - not a cute name. The label should communicate who they are to a new team member instantly.

```
Persona label: [e.g., "Ops Lead at scaling startup", "Procurement Manager at mid-market SaaS"]
Primary segment this persona represents: [percentage of current customers or target market]
```

Write the persona for your most valuable segment first. If you have multiple segments, write separate personas - do not blend them.

### Step 2: Document the buying situation (Dunford's core contribution)

This is what most personas skip. Define:

- **Trigger** - what happened in the customer's world that started the buying process? Not "they needed software." What specifically changed? (Headcount crossed a threshold, a new regulation took effect, a previous tool failed, a new executive joined.)
- **Alternatives considered** - what did they evaluate before choosing you? Name the actual options: specific competitors, internal builds, spreadsheets, doing nothing.
- **Switching cost they accepted** - what friction did they overcome to buy? Migrating data, getting budget approval, changing a workflow. If they accepted high switching cost, they saw real value.

### Step 3: Define the job they are hiring the product to do

Write it as: "[Customer] is trying to [make progress toward outcome] in the context of [situation]. The obstacle is [what is in the way]."

Avoid defining the job as a feature. "They need a dashboard" is not a job. "They need to show their CEO that marketing spend is producing pipeline" is a job.

### Step 4: Write the capability-to-value map for this persona

Dunford: different customer segments value the same product features differently. Document which capabilities matter most to this persona and why.

| What they value most | Why it matters to them specifically | The alternative they would use instead |
|---|---|---|
| [capability or feature] | [business or personal outcome it drives] | [what they would use if this did not exist] |

Limit to 3-4 rows. If everything is a priority, nothing is.

### Step 5: Document their objections and responses

List the 3 most common objections and the factual response to each.

```
Objection 1: "[exact words the customer uses]"
Response: [factual, specific answer - include data or proof where possible]

Objection 2: "[exact words]"
Response: [...]

Objection 3: "[exact words]"
Response: [...]
```

Source these from sales call recordings, support tickets, or customer interviews. Made-up objections produce made-up responses.

### Step 6: Write the persona summary card

```
PERSONA: [Label]

Trigger: [1 sentence - what started their search]
Job to be done: [1 sentence]
Top 3 valued capabilities: [brief list]
Primary alternative: [what they would use instead]
Deal-breaker objection: [the one objection that kills deals if not addressed]
Best channel to reach them: [where they spend attention]
Proof that resonates: [data, peer testimonials, case studies, or demos]
```

## Anti-Patterns

**1. Demographics-first persona**
Bad: "Sarah, 34, Marketing Manager, lives in Austin, has 2 kids, shops at Whole Foods."
Good: "Ops lead whose team just crossed 50 people and can no longer manage workflows in Notion."
Demographics do not predict buying behavior. Situation does.

**2. Blending multiple segments into one persona**
*Obviously Awesome* is explicit that the same capability carries different value to different
segments, so a blended persona averages two value maps into one that describes neither.
Bad: A persona that represents "SMB and enterprise" or "both technical and non-technical buyers."
Good: Separate personas for each distinct buying context.

**3. Inventing objections from the desk**
Bad: "They probably worry about price and security."
Good: "In 12 sales calls, the top objection was [exact quote]. Here is the response that works."

**4. No buying trigger**
Bad: Persona that describes who the customer is but not what caused them to start looking.
Good: "Trigger: their previous tool deprecated the integration they relied on, forcing a switch within 30 days."

## Self-check

Every item is checkable against the finished persona document. Where an item says count, count it.

- [ ] Persona label is a role plus a context, contains no first name, and a new joiner could say who it is without asking
- [ ] The trigger names a dated or datable event. If it contains the words "wants", "needs" or "is growing", it is a state and fails
- [ ] Alternatives section names at least 2 actual products or behaviours. The word "competitors" alone does not count
- [ ] Job to be done matches the template exactly: trying to, in the context of, the obstacle is
- [ ] Capability-to-value table has 3 or 4 rows, every cell filled, and the rows are in priority order with the top row identified as the lead
- [ ] All 3 objections are in quotation marks and each carries a source tag naming where it came from (call, ticket, interview, survey), or is written `[NEEDS INPUT: real objection]`. Count how many are sourced and record the number
- [ ] Summary card has all 7 fields filled and fits on one page
- [ ] Exactly one seniority level and one company stage appear in the persona. Two of either means split it
- [ ] The `confidence` value in the frontmatter matches the number of distinct data points listed in the evidence section. Compare the two rather than asserting

## What this skill cannot know

These are the limitations that bite in practice. Where one applies to the artifact, write it into the document as an open question rather than leaving the reader to assume it was verified.

1. **Whether this persona is the one that buys, or the one that uses.** In most B2B deals they differ, and the economic buyer often never appears in user research. If the evidence is all from users, say so.
2. **How large the segment is.** Nothing here sizes the market or estimates what share of revenue this persona represents. Any percentage in Step 1 must come from the user's own customer data, never from this skill.
3. **Whether the objections still hold.** Objections decay as the product ships and competitors move. An objection captured a year ago may already be answered, or may have been replaced by a harder one.
4. **Whether the frame is right.** *Obviously Awesome* treats the market category as the context that makes value obvious, and Step 3 records the frame the buyer already had. This skill cannot tell you whether that frame is the one the rest of the market uses, only what one buyer brought to the search.
5. **Whether the buying committee has other members.** A single-persona view can miss the security reviewer, the procurement gate, or the finance approver who kills the deal without ever speaking to sales.

## Context and output

**Before you start.** Read `knowledge/icp/personas.md` for any existing personas, and `knowledge/markets/positioning.md` for the segment this persona should belong to. If there is no research behind this persona, say so and run `/customer-research` before writing, rather than inventing pains.

**When you finish.** Save to `output/customer-persona/<DD-MM-YYYY>-<persona-slug>.md` with YAML frontmatter carrying the date, the skill name, the `confidence` value, and the key decisions made.

## Shared file ownership: knowledge/icp/personas.md

**`/icp-research` owns `knowledge/icp/personas.md`.** It owns the file's structure, the section
order, the primary and secondary persona slots, and the anti-persona. This skill contributes single
persona blocks into that structure.

| Part of the file | This skill may |
|---|---|
| One named persona block | Add a new block, or replace that one block in full |
| Other persona blocks, the ICP firmographic summary, the anti-persona, the file's headings and ordering | Read only. Never edit, reorder, or delete |

The write gate is the same gate `/icp-research` applies to this file, and neither skill may relax it:

1. Show the user a diff of the exact lines you would add or replace, and wait for an explicit yes before writing. Five other marketing skills read this file as truth, so an ungated write turns one thin session into permanent canon nobody can trace back.
2. If confidence is low, meaning fewer than 5 distinct data points, write to `output/` only and say plainly that the persona is not yet canon. Low-confidence personas never enter the shared file, in either skill.
3. Carry a `confidence: high | medium | low` field into every block written, using the same scale `/icp-research` applies to this file: 10 or more distinct sources is high, 5 to 9 is medium, fewer than 5 is low and never enters the shared file. A reader must be able to tell canon from draft without opening the sources.
4. Never invent an objection, a trigger, a quote, or a piece of customer vocabulary to complete a block. Invented customer language is the worst thing this skill can emit, because `/content-writer` and `/copy-review` then treat it as observed speech and put it into public copy.

## Related skills

- `/customer-research` for sourcing the verbatim quotes and objections this persona needs, and it must run first when there are fewer than 3 real objections
- `/icp-research` for the segment and firmographic definition, and it owns the shared personas file this writes into
- `/brand-context` for creating the knowledge base when `knowledge/icp/personas.md` does not exist yet
- `/positioning-doc` for when the persona work reveals the product is positioned for a different buyer than the one who actually pays
- `/copy-review` for checking whether existing copy answers this persona's real objections
- `/case-study-writer` for turning one of this persona's real switching stories into a published proof point
