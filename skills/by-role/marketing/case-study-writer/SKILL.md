---
name: case-study-writer
description: Write customer case studies and success stories using the Situation-Complication-Resolution (SCR) narrative framework and Barbara Minto's Pyramid Principle (conclusion first). Produces case studies where the headline states the result, the complication makes readers recognize their own situation, and every paragraph advances the story. Use when the user asks for a case study, customer story, customer success story, win story, reference write-up, or "turn this customer into a case study". Reads brand voice and service catalog from knowledge/. For a press announcement, see press-release-writer. For pitching the story to media, see pr-pitch-writer. For repurposing it into social, see content-repurposer.
metadata:
  grounded_in:
    - "Pyramid Principle - Minto (SCR)"
  reads:
    - knowledge/brand/voice.md
    - knowledge/services/
    - knowledge/icp/personas.md
    - knowledge/content-library/case-studies/
  writes:
    - output/case-study/
---

# case-study-writer

Turns raw customer interview material into a structured case study. Mandatory SCR (Situation-Complication-Resolution) narrative structure with Pyramid Principle headline. Designed for sales enablement and SEO. The reader is a busy prospect who will decide in 10 seconds whether to keep reading - the conclusion goes first, not last.

## When to use

- "Write a case study from these notes"
- "Turn this customer interview into a story"
- "Draft a customer success story for X"
- "We need a reference write-up"

## Framework: SCR + Pyramid Principle (McKinsey storytelling / Barbara Minto)

**Why SCR, not chronological storytelling:**
Chronological case studies bury the hook. Readers are busy. SCR gets to the problem in the first paragraph, which is where readers decide whether this is relevant to them.

**The 3 SCR components:**

| Component | Length | What it must do | It has failed when |
|---|---|---|---|
| **Situation** | 1 paragraph | State only what the reader accepts without argument | It reads as a company profile, or the reader has to be persuaded of anything in it |
| **Complication** | 2 paragraphs | Make the reader recognise their own situation, and show the cost of doing nothing | It lists missing features instead of naming a business or human problem |
| **Resolution** | 2-3 paragraphs plus results | Answer the complication directly, with specifics | It introduces a benefit the complication never asked for |

**SITUATION** - establish context. What was true before? Set the scene without drama. This is what the audience already knows or can accept. Keep it short - one paragraph maximum. Do not start the story here.

**COMPLICATION** - introduce the tension. What changed? What made the situation unacceptable? This is where the reader recognizes their own situation. The complication is the hook. If readers don't see themselves in this section, the case study will not convert.

**RESOLUTION** - answer the complication. What was done? How did it work? What happened? The resolution is the proof - specific, measurable, credible. Vague resolutions ("they saw great results") are worthless.

**Pyramid Principle application (Barbara Minto, *The Pyramid Principle*):**

Minto's core rule is that ideas at any level must **summarise** the ideas grouped beneath them. Applied here, that means the headline is not a teaser for the story, it is the story's conclusion, and everything below it exists to support that one claim. If a section does not support the headline, it belongs in a different document.

- Lead with the headline conclusion (the result) - never save it for the end
- Support with the 3 SCR arguments
- Each argument supported by evidence: quotes, metrics, specific events
- Every section answers "so what?" - what does this prove for the reader?
- Minto's grouping test: read only the section headings in order. They should tell the whole story without the body text. If they do not, the structure is wrong, not the prose

### Proof strength: rank the evidence before you write

Not all evidence carries the same weight, and a case study is only as strong as its weakest load-bearing claim. Rank what the inputs actually contain, and lead with the strongest.

| Rank | Evidence type | Why it ranks here |
|---|---|---|
| 1 | A before-and-after metric the customer measured themselves, with the measurement window stated | Checkable, and the customer owns it |
| 2 | A metric from your own product data that the customer has confirmed | Checkable, but the source has an interest |
| 3 | A named customer quote about a specific change | Not measurable, but attributable and human |
| 4 | A timeline fact: how long implementation took, when the change appeared | Weak alone, strong as corroboration |
| 5 | A qualitative statement with no number and no name | Nearly worthless as proof. Do not lead with it |

**Decision rules:**

1. **No rank 1 or rank 2 evidence means this is not a case study yet.** Say so. Offer a shorter customer story or testimonial instead of stretching a rank-4 fact into a headline.
2. **The headline metric must be rank 1 or 2.** A headline built on a quote is an opinion presented as a result.
3. **Never state a metric without its window.** "Cut onboarding time by 60%" over one week and over one year are different claims.
4. **If the result has a cause other than your product** (they also hired three people, or changed process at the same time), say so in the Resolution. A prospect who discovers the omission later stops believing the whole document, and the customer knows the truth and is reading the draft.

**Case study structure using SCR + Pyramid:**

```
1. HEADLINE: conclusion first - "[Metric improvement] for [Customer] with [product/approach]"
2. SITUATION: who they are, what their world looked like before
3. COMPLICATION: what became unacceptable, what they tried, what wasn't working
4. RESOLUTION: what they did (with you), how it worked, the specific steps
5. RESULTS: quantified outcomes - metrics, timeline, before/after comparison
6. QUOTE: customer's own words on the complication and/or resolution
7. SO WHAT: what should the ideal prospect believe or do after reading this?
```

## Inputs needed (ask the user for each)

- **Customer**: name, industry, size, role of contact
- **Problem**: what they were doing before, what was broken
- **Solution**: which product or service they adopted
- **Implementation**: timeline, scope, who was involved
- **Results**: numbers, quotes, qualitative outcomes
- **Permission**: confirmed they can be named, or anonymous

If any are missing, ask. Do not invent.

### Stop conditions

Run these before drafting, in priority order. The first three are hard rules: they mean this piece does not get written today, and no amount of good material overrides them.

| Condition | Action |
|---|---|
| **No written permission and no decision to anonymise** | **Stop drafting a named study.** Default to anonymised and set `permission-confirmed: false`. See the approval gate below |
| **No rank 1 or rank 2 metric** | **Stop.** Offer a testimonial or a short customer story instead. Padding a case study with rank-4 facts produces a document sales will not use twice |
| **The contact who gave the material has left, or was never authorised to speak** | **Stop.** Confirm with someone who is currently authorised before anything carries their company's name |
| **The customer is still in an active escalation, renewal negotiation, or dispute** | Flag hard and ask before proceeding. Timing, not writing, is the risk here |
| **The result predates a major product change** | Flag it and date the study, so a prospect does not buy a version that no longer exists |
| **The metric is confidential or competitively sensitive to the customer** | Ask what they will allow: a percentage instead of an absolute, a range, or an order of magnitude. Their limit is the limit |

## Process

1. **Load context.** Read `knowledge/brand/voice.md`, the relevant `knowledge/services/<service>.md`, and 1-2 past case studies from `knowledge/content-library/case-studies/` to mirror structure.

2. **Confirm anonymization.** If the user has not confirmed permission to name the customer, default to anonymized ("a Series B fintech in EMEA") and flag for review.

3. **Map inputs to SCR before writing.** Fill this in mentally before drafting:
   - Situation: <what was true and stable before the problem>
   - Complication: <what changed or became unacceptable>
   - Resolution: <what they did and what happened>
   - Headline metric: <the single most compelling number from the results>

4. **Write using the SCR + Pyramid structure:**

   ```
   # <Headline: conclusion first>
   Format: "[Metric] for [Customer] with [product/approach]"
   Example: "How Acme cut onboarding time from 14 days to 3 using automated workflows"
   Rule: the headline must contain a specific number or measurable outcome.

   ## Situation
   1 paragraph. Who is the customer, what they do, their scale. End with the context that
   makes the complication make sense. This is the "given" - what the reader can accept
   without argument.

   ## Complication
   2 paragraphs.
   - Paragraph 1: What changed or became unacceptable. Specific, not generic.
     ("Their CSM team was spending 40% of the week on manual data entry" not
     "they had operational challenges")
   - Paragraph 2: What they tried before and why it didn't work. The cost of inaction:
     revenue at risk, hires deferred, churn increasing, competitor gaining ground.
   Rule: a reader from the same situation should recognize themselves in this section.
   If they don't, the complication is too abstract.

   ## Resolution
   2-3 paragraphs.
   - Why they chose this product (the decision, not the features)
   - What they implemented and who was involved
   - How the rollout went (specific steps, timeline, early signals)
   One pull quote from the customer about the decision or early experience.

   ## Results
   - Lead with the headline metric (the one in the title)
   - 3-5 supporting metrics as a bulleted list (specific numbers, not ranges)
   - Time-to-value: how long from start to result
   - One pull quote about the outcome - the customer's own words on what changed

   ## What this means for you
   1 paragraph. "So what" for the ideal reader.
   - What should the reader believe is now possible for their team?
   - Soft CTA: "If your team is dealing with <same complication>, see how <product> can help"
   Rule: this section must name the complication, not the product. The reader should feel
   spoken to, not sold to.
   ```

5. **Voice rules:**
   - Customer is the hero, not the product
   - Use the customer's words verbatim where possible (mark as "[customer quote]")
   - Numbers are as specific as the source, never more so. If the customer said "nearly half", write "nearly half". Converting a hedge into a figure is a claim tightened past its source, and the source is a named customer who will read it
   - No marketing fluff ("revolutionary", "best-in-class", "industry-leading")
   - Every paragraph advances one of: situation, complication, or resolution. Cut anything that doesn't.

6. **Self-check.** Every item is checkable against the draft file. Point at the sentence, or the item fails.

   - The headline contains a digit or a stated measurable outcome, and that figure is rank 1 or rank 2 on the proof-strength table. Name its rank and its source
   - Every number in the draft appears in the inputs the user supplied. List each number beside the input line it came from. Any number without a matching input line is removed, not softened
   - Every hedge in the source survives in the draft. Search the inputs for "about", "roughly", "nearly", "around", "we think" and confirm each still appears where the source used it
   - Every quote appears verbatim in the interview material. Quote-match each one against the source text. A quote that was tidied for grammar is marked as edited, and the customer approves the edit
   - Every metric states its measurement window
   - The Situation is exactly one paragraph
   - The Complication contains a named cost of inaction: revenue, time, headcount, churn or a competitor gain
   - The Complication describes a business or human problem, not a list of features the customer lacked. Read it back with your product name removed. If it stops making sense, it is a feature list
   - The Resolution answers the complication that was stated, and introduces no benefit the Complication did not raise
   - Anything other than the product that contributed to the result is named in the Resolution
   - Results section contains only metrics and quotes the inputs contain. If fewer than 4 metrics or 2 quotes exist, it reads `[ONLY N PROVIDED]`. The quota never overrides the no-invention rule
   - "What this means for you" names the complication, and the product name appears at most once, in the CTA
   - Read the headings alone in order. They tell the story without the body (Minto's grouping test)
   - Every paragraph advances situation, complication, or resolution
   - Word count is stated and falls in 600-1000
   - Frontmatter `permission-confirmed` and `approval` are both filled in. Neither is blank
   - Voice matches `knowledge/brand/voice.md`

7. **Save** to `output/case-study/<DD-MM-YYYY>-<customer-slug>.md` with frontmatter:
   ```yaml
   ---
   format: case-study
   customer: <name or "anonymized">
   industry: <industry>
   service: <service from knowledge/services/>
   headline-metric: <the big number>
   permission-confirmed: <true|false>
   scr-situation: <1-sentence summary>
   scr-complication: <1-sentence summary>
   scr-resolution: <1-sentence summary>
   created: DD-MM-YYYY
   ---
   ```

8. **Offer derivative assets:**
   - LinkedIn post highlighting the headline metric (lead with the result, then the complication)
   - 1-pager PDF brief for sales (use `/ppt-maker` with case-study layout)
   - Quote graphic suggestions (complication quote + resolution quote as two options)

## Rules

- Headline states the result before the story starts. Never save the punchline for the end.
- The complication is not a list of features that were missing. It is a human or business situation that became unacceptable. Write it that way.
- Never invent metrics, quotes, or implementation details. If the user gave incomplete inputs, mark gaps as `[NEEDS INPUT: <what's missing>]` instead of fabricating.
- If permission is not confirmed, anonymize aggressively. Industry, region, and size only.
- Always show the cost of inaction in the complication. A case study without stakes has no tension and no pull.
- If every paragraph doesn't advance situation, complication, or resolution - cut it.

## What to cut when it runs long

600-1000 words is the target, and a case study that runs over does not get read by the prospect it was written for. Cut in this priority order, and never cut upward past a step to protect a favourite paragraph:

1. **Company background in the Situation.** Anything beyond what the Complication needs to make sense. This is where almost all overrun lives.
2. **Implementation detail in the Resolution.** Keep the decision and the timeline, cut the configuration steps. A prospect wants to know it worked, not how the sprint was run.
3. **Supporting metrics below rank 3.** Keep the strongest four, drop the rest. A weak metric beside a strong one drags the strong one down.
4. **The second quote if both make the same point.** Keep the one in the customer's plainer words.
5. **Adjectives in the Results section.** The number is the claim, and every adjective next to it reads as an attempt to make it sound bigger.

Never cut the cost of inaction from the Complication, and never cut the measurement window from a metric. Those are the two things that make the document credible, and they are the two most often removed for space. If the piece is still over 1000 words after step 5, the material is two case studies, not one. Say so rather than compressing both.

## Minimum bar before this goes to sales

A case study that sales will not use twice was not worth writing. Before handing it over:

1. The headline metric is rank 1 or 2, with a stated window.
2. At least one direct customer quote, attributed to a real named or role-described person, appears verbatim from the interview.
3. The Complication would be recognised by a prospect who has never heard of this customer.
4. Frontmatter `approval` reads `granted DD-MM-YYYY`, or the study is anonymised and says so on its face.

If any of the four fails, say which one and hand back a testimonial or a short story instead. Publishing a weak case study costs more than publishing nothing, because it becomes the proof asset everyone points at.

## Customer approval before publication

A named case study is a public claim about another company, usually carrying their logo, a quote
attributed to a named employee, and a metric about their business. Every real company requires
sign-off on that, and this is a legal exposure, not a courtesy.

1. Send the final draft to the customer contact for **written** approval before publication.
2. Record the result in frontmatter: `approval: pending | granted DD-MM-YYYY | refused`.
3. Never publish, and never pass to `/pr-pitch-writer` or `/press-release-writer`, while approval
   is `pending`.
4. If the customer asks for a metric to be softened or removed, that is their call, not a
   negotiation. Change it.
5. Anonymise by default until approval is explicit: "a Series B fintech" rather than the name.

## What this skill cannot know

These are limitations of the skill, not of the customer's story. Anything below that reaches the draft must be labelled `[NEEDS INPUT]` or `[UNVERIFIED]` there, never asserted.

- **Whether the customer's legal or communications team permits their name, logo or quote to be used.** Verbal agreement from one contact is not company approval, and the person who gave you the interview is often not the person who can grant it.
- **Whether the metric quoted is still accurate at publication.** Case studies are drafted weeks before they publish and then run for years. Date the measurement, and re-confirm before any republication.
- **Whether the named employee still works there or still endorses the quote.** A quote from someone who has left is worth re-clearing with their successor, or anonymising to the role.
- **Whether the result is actually attributable to the product.** Correlation is what the inputs usually contain. Say what the customer says, name anything else that changed, and do not upgrade it to causation.
- **Whether the metric is confidential.** Revenue, headcount and churn figures are frequently material or competitively sensitive, and a public company has disclosure rules the marketing contact may not have considered.
- **Whether the logo usage is within the terms of the contract.** Some agreements allow the name but not the logo, or one placement but not paid media.

## Related skills

- `/customer-research` for running the customer interview properly, before there is anything to write up
- `/content-repurposer` for turning the approved study into social and email derivatives, but only after approval is `granted`
- `/press-release-writer` for an announcement version, which needs the same approval and usually a second one from the customer's PR team
- `/pr-pitch-writer` for pitching the story to media, again only after approval is `granted`
- `/landing-page-writer` when the study becomes a gated asset with its own page
- `/linkedin-post` for the headline-metric post, keeping the number and its window intact
- `/messaging-framework` when three case studies in a row surface the same complication, which is a positioning signal rather than a content one
- `/ad-campaign-writer` for paid use of the proof, noting that ad consent is a separate permission from case-study consent

