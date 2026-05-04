---
name: case-study-writer
description: Write customer case studies and success stories using the Situation-Complication-Resolution (SCR) narrative framework and Barbara Minto's Pyramid Principle (conclusion first). Produces case studies where the headline states the result, the complication makes readers recognize their own situation, and every paragraph advances the story. Use when the user asks for a case study, customer story, customer success story, win story, reference write-up, or "turn this customer into a case study". Reads brand voice and service catalog from knowledge/.
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

**SITUATION** - establish context. What was true before? Set the scene without drama. This is what the audience already knows or can accept. Keep it short - one paragraph maximum. Do not start the story here.

**COMPLICATION** - introduce the tension. What changed? What made the situation unacceptable? This is where the reader recognizes their own situation. The complication is the hook. If readers don't see themselves in this section, the case study will not convert.

**RESOLUTION** - answer the complication. What was done? How did it work? What happened? The resolution is the proof - specific, measurable, credible. Vague resolutions ("they saw great results") are worthless.

**Pyramid Principle application (Barbara Minto):**
- Lead with the headline conclusion (the result) - never save it for the end
- Support with the 3 SCR arguments
- Each argument supported by evidence: quotes, metrics, specific events
- Every section answers "so what?" - what does this prove for the reader?

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
   - Numbers are specific (47%, not "nearly half")
   - No marketing fluff ("revolutionary", "best-in-class", "industry-leading")
   - Every paragraph advances one of: situation, complication, or resolution. Cut anything that doesn't.

6. **Self-check:**
   - Headline contains a specific number or measurable outcome (Pyramid Principle: conclusion first)
   - Situation is 1 paragraph max - not a company brochure
   - Complication check: would a reader in the same situation recognize themselves here? If not, make it more specific.
   - Resolution answers the complication directly - does not introduce new problems
   - Results: at least 4 quantified metrics, at least 2 pull quotes
   - "What this means for you" names the complication, not the product
   - Every paragraph advances situation, complication, or resolution - nothing else
   - Length: 600-1000 words
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
