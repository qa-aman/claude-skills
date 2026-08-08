---
name: customer-research
description: Turn raw customer material into evidence-backed personas and verbatim voice-of-customer language. Two modes - analyse sources the user already has (call transcripts, support tickets, survey responses, sales notes, reviews), or source new material from public places customers actually talk. Produces quoted pains, objections, and switch triggers that other skills consume, never invented ones. Use when the user says "customer research", "voice of customer", "what do our customers actually say", "we need real quotes", "analyse these call transcripts", "read our support tickets", "build a persona from data", "find what customers complain about", or when a persona is marked provisional. For structuring the finished persona into the knowledge base, see brand-context. For the JTBD persona template itself, see customer-persona.
metadata:
  grounded_in:
    - "The Mom Test - Fitzpatrick"
    - "JTBD"
  reads:
    - knowledge/icp/personas.md
    - knowledge/markets/competitors.md
  writes:
    - knowledge/icp/personas.md
    - output/customer-research/
---

# customer-research

Closes the loop from nothing to a persona. Most persona work assumes the research already exists. This skill produces it.

## The interview discipline

Mode A analyses calls that may themselves be badly run, and Mode B reads what people volunteered.
Both need **Rob Fitzpatrick's rules from *The Mom Test* (2013)** applied as a filter:

1. **Talk about their life, not your idea.** Anything a person says about your product is a
   compliment or a courtesy, not data.
2. **Ask about specifics in the past, never generics about the future.** "What did you do the last
   time this happened" is evidence. "Would you use this" is noise, and should be discarded rather
   than coded.
3. **Listen more than you talk.** In a transcript, a long interviewer turn before an answer usually
   means the answer was led.

When coding quotes, discard anything that answers a leading or hypothetical question, and say how
many you discarded. A corpus of compliments produces a persona of people who do not exist.

The rule that makes the output worth anything: **every pain, objection and trigger is a quote with a source, or it is tagged as an inference.** No invented customer language, ever.

## Two modes

Ask which, or infer from what the user supplies.

### Mode A: analyse what they have
Sources, in descending order of value:

| Source | What it gives | Watch for |
|---|---|---|
| Won and lost deal call recordings or notes | Switch triggers, real objections | Sales notes are already paraphrased, treat as second-hand |
| Support tickets | Pains in the customer's own words | Skews to existing customers with problems, not prospects |
| Churn or exit interviews | The strongest signal in the whole list | Small N, treat each as a case not a statistic |
| Onboarding or sales discovery calls | The trigger event, stated fresh | |
| Open-text survey responses | Volume and language patterns | Leading questions produce leading answers, check the question |
| Reviews of you and of competitors | Public, comparative, unfiltered | Skews to extremes |

### Mode B: source new material
When the user has nothing. Use WebSearch and WebFetch to find where this audience already talks in public: review sites for the category, relevant subreddits and forums, community threads, comparison and alternatives posts, and question sites. Search for the problem in the customer's language rather than the product category, since people describe symptoms before they know the solution exists.

Always tell the user what Mode B cannot do: it finds language, not your customers. Public complaint skews negative and toward the vocal. It is a strong start and a weak conclusion, and the output must say so.

## Process

1. **Define the question.** What decision does this research inform? A persona for a new segment, the objections for a sales page, the language for an ad. Research without a decision produces a document nobody uses.

2. **Inventory sources.** List what exists, how many of each, and the date range. State the sample size in the output. Twelve tickets is not a pattern, it is a hint, and the output should say which one it is.

3. **Extract verbatim.** Pull actual sentences, not summaries. For each, record: the quote, the source type, the date if known, and the role of the speaker if known.

4. **Code the quotes.** Group into: pains, desired outcomes, trigger events, alternatives considered, objections, and the vocabulary they use for the problem. A quote can carry more than one code.

5. **Count.** How many distinct people expressed each theme, not how many quotes. Ten quotes from one angry customer is one data point.

6. **Separate signal from noise.** A theme is worth acting on if three or more distinct people raised it, or if one person raised it and it cost a deal. Everything else is listed as a hint, not a finding.

7. **Write the findings** and, if the user approves, merge into `knowledge/icp/personas.md`.

## The vocabulary table

The single most reusable output. Downstream writing skills consume it directly.

| They say | We say | Use theirs when |
|---|---|---|
| [customer phrase] | [our internal or industry term] | [ads, landing page headline, cold email subject] |

Customers search and click on their own words, not the category's. When these two columns differ, that gap is usually worth money.

## Output format

```markdown
# Customer research: [question]

**Decision this informs:** [what changes based on this]
**Mode:** A (existing sources) | B (public sourcing)
**Sources:** [type and count each, date range]
**Distinct people represented:** N
**Confidence:** high (N>=15 distinct, multiple source types) | moderate (N 5-14) | directional (N<5 or single source type)

## Findings

### Pains
| # | Theme | Distinct people | Verbatim | Source |
|---|---|---|---|---|
| 1 | [theme] | N | "[exact quote]" | [type, date] |

### Trigger events
[what was happening the day they started looking, quoted]

### Alternatives considered
[including doing nothing, with how often each appeared]

### Objections
| Objection | Distinct people | Verbatim | Who resolved it and how |
|---|---|---|---|

### Vocabulary
[the they-say / we-say table]

## Hints, not findings
[themes below the threshold, kept because they may matter later]

## What this research cannot tell you
[explicit limits: sample skew, missing segments, source bias, anything Mode B cannot see]

## Recommended next research
[the one gap most worth closing, and the cheapest way to close it]
```

## Merging into personas

Only on explicit approval. When merging into `knowledge/icp/personas.md`:

1. Replace any `[NEEDS INPUT: real customer language]` tag with a real quote and its source.
2. Upgrade `confidence: provisional` to `high` only when the persona has at least three distinct people behind it and at least one real quote per pain.
3. Never delete an existing quote. Add, and mark the older one with its date.
4. Append a source line: `Research: [file path], DD-MM-YYYY, N=[distinct people]`.

## Self-check before saving

- Every pain, objection and trigger has a verbatim quote or is explicitly tagged `[INFERRED]`
- No quote was smoothed, shortened, or corrected for grammar. Verbatim means verbatim
- Distinct-people counts are people, not quotes
- The confidence label matches the actual sample size
- "What this research cannot tell you" is filled in and specific, not boilerplate
- Mode B output states plainly that public sources are not your customers
- Themes below threshold are in Hints, not promoted into Findings

## Rules

- **Never write a quote that was not said.** This is the whole value of the skill. An invented quote is worse than no research, because it launders a guess into evidence that every downstream skill then trusts.
- Never present a single loud customer as a pattern.
- Preserve the customer's grammar and phrasing exactly. The awkward phrasing is often the exact phrase that should appear in an ad.
- Anonymise by default: role and company type, not names, unless the user confirms permission to use them.
- If the user asks for a persona and has no sources at all, say so plainly and offer Mode B, rather than producing a plausible persona from nothing.
- Save to `output/customer-research/<DD-MM-YYYY>-<topic-slug>.md`.

## Related skills

- `/brand-context` to write the finished persona into the knowledge base
- `/customer-persona` for the JTBD persona structure this feeds
- `/icp-research` for segment and firmographic definition, which is a different question from voice
- `/competitor-analyst` when the research surfaces competitor comparisons worth pursuing
- `/copy-review` to check whether existing copy uses the vocabulary this research found
