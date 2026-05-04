---
name: seo-article-writer
description: Write SEO-optimized long-form articles targeting specific keywords using the They Ask You Answer Big 5 framework (Marcus Sheridan). Articles are categorized by Big 5 type (Cost, Problems, Versus, Best/Reviews, How-To) and structured accordingly. The "answer first" rule applies to every article. Use when the user asks for an SEO article, blog post for ranking, "rank for keyword X", organic content, search-optimized post, pillar page, or content for organic traffic. Includes keyword targeting, search intent matching, internal linking suggestions, and meta tags.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/services/
  - knowledge/markets/positioning.md
  - knowledge/content-library/
writes:
  - output/seo-article/
---

# seo-article-writer

Writes long-form articles tuned for organic search. Built on They Ask You Answer: the companies that answer buyer questions honestly - especially the uncomfortable ones about price, problems, and competitors - win the most qualified organic traffic and trust.

Different from thought leadership: optimizes for search intent and keyword coverage, not contrarian POV.

## When to use

- "Write an SEO article on <keyword>"
- "Build a pillar page for <topic>"
- "Rank for <keyword>"
- "Create content that ranks"
- "Write organic blog content on X"

## Inputs needed

- **Primary keyword** (required): the head term to rank for
- **Search intent**: informational, commercial, transactional, navigational (default: ask the user, or infer)
- **Target length**: 1500, 2500, or 3500 words (default: 2500 for pillar, 1500 for supporting)
- **Existing top 3 SERP results**: paste URLs or have the skill use WebFetch
- **Internal pages to link to**: list URLs from the user's site

## Framework: They Ask You Answer - Big 5 (Marcus Sheridan)

Buyers ask questions. Companies avoid answering the hard ones (price, problems, competitors) because they're afraid of the answer. The companies that answer honestly dominate organic search and build more trust than any competitor that hedges.

### The Big 5 content types

| Type | Triggers | Why it works | Honesty requirement |
|---|---|---|---|
| **1. Cost and Price** | "How much does X cost?" / "Price of Y" | Most searched, least answered. Companies hide it. Brave ones dominate. | Give real ranges. Explain what drives price up or down. Never say "contact us for pricing." |
| **2. Problems** | "Problems with X" / "Downsides of Y" / "Is X worth it?" | Buyers research problems before buying. Honest companies build more trust than defensive ones. | Enumerate real limitations. Add context. Do not hide. |
| **3. Versus and Comparisons** | "X vs Y" / "X or Y" / "Best X for [use case]" | High-intent search. Buyers are close to a decision. | Structured comparison table. Include competitors. Be fair. Recommend based on fit, not brand bias. |
| **4. Best and Reviews** | "Best X for [situation]" / "Top Y tools" / "X alternatives" | Buyers want trusted recommendations. | Include options you don't sell. Readers trust it more. Excluding competitors signals bias. |
| **5. How-To** | "How to do X" / "How to [achieve outcome]" / "Step-by-step guide" | Educational, early-funnel, authority-building. | Answer the question directly. Do not make them read 800 words to get to the answer. |

Every article must be categorized as one of the Big 5 before the outline is built.

## Process

1. **Load context.** Read `knowledge/brand/voice.md`, relevant `knowledge/services/`, and `knowledge/content-library/` to find related pieces for internal linking.

2. **Categorize the article.** Identify which Big 5 type this article is:

   ```
   Big 5 Categorization

   Primary keyword: <keyword>
   Big 5 type: <Cost | Problems | Versus | Best/Reviews | How-To>
   Why this type: <one sentence>
   Honesty check: <what is the uncomfortable truth this article must address?>
   Answer-first target: <the direct answer to the headline question, in 2-3 sentences>
   ```

   If the keyword doesn't map to a Big 5 type, note it and proceed with standard intent-matching, but flag: "This article is not a Big 5 topic. It will rank but may not drive high-intent traffic."

3. **Analyze the SERP.** If the user provided top 3 URLs, use WebFetch to read each. Identify:
   - Average word count
   - Common H2 headings (the questions search expects answered)
   - Information gaps (what they all miss)
   - Format type (listicle, guide, comparison, definition)
   - Honesty gaps: are competitors hedging on price, problems, or comparisons?

   If the user did not provide URLs, ask them to paste the top 3 they're competing against.

4. **Match Big 5 type to structure.** Use the type-specific structure below. Override only if the SERP analysis shows a different format dominates:

   ### Cost and Price structure
   ```
   H1: How Much Does [X] Cost? (2026 Pricing Guide)
   - Intro (answer first): give the range in the first paragraph. Do not hedge.
   - H2: What is the typical price range?
   - H2: What factors affect the price?
   - H2: What is included (and what costs extra)?
   - H2: How does [X] pricing compare to alternatives?
   - H2: Is [X] worth the cost?
   - H2: FAQ (pricing objections, contract terms, ROI)
   - Conclusion + CTA
   ```
   Honesty check: Did you give a real number in the first 200 words? If not, rewrite.

   ### Problems structure
   ```
   H1: [X] Problems: What to Know Before You Buy
   - Intro (answer first): acknowledge this exists. Name the top 3 problems upfront.
   - H2: Problem 1 (specific, not vague)
   - H2: Problem 2
   - H2: Problem 3
   - H2: Who [X] is NOT right for
   - H2: How to decide if [X] is still the right choice for you
   - H2: Alternatives if [X] isn't the fit
   - Conclusion + fair recommendation
   ```
   Honesty check: Did you name real problems, or did you write "some users find the learning curve steep"? Specific or rewrite.

   ### Versus and Comparisons structure
   ```
   H1: [X] vs [Y]: Which Is Right for You? (Honest Comparison)
   - Intro (answer first): give a one-sentence verdict based on use case. Do not make them read to find out.
   - H2: Quick comparison table (features, pricing, integrations, support)
   - H2: Where [X] wins
   - H2: Where [Y] wins
   - H2: Who should choose [X]
   - H2: Who should choose [Y]
   - H2: What users say (real quotes if available)
   - Conclusion: clear recommendation by use case, not by brand bias
   ```
   Honesty check: Did you recommend the competitor for use cases they're genuinely better at? If not, the reader will notice and bounce.

   ### Best / Reviews structure
   ```
   H1: Best [X] for [Situation]: [Year] Guide
   - Intro (answer first): name the top pick in the first paragraph. Explain why.
   - H2: How we evaluated (criteria + weighting)
   - H2: Best overall: [tool]
   - H2: Best for [use case]: [tool] (include options you don't sell)
   - H2: Best budget option: [tool]
   - H2: Comparison table (all tools side by side)
   - H2: How to choose (the decision framework)
   - Conclusion + CTA
   ```
   Honesty check: Is every tool on this list included because it deserves to be? Including only your own products or partners reads as advertising.

   ### How-To structure
   ```
   H1: How to [Achieve Outcome]: Step-by-Step Guide
   - Intro (answer first): give the core process in 2-3 sentences. State how long it takes.
   - H2: What you need before you start
   - H2: Step 1: [action verb + specific outcome]
   - H2: Step 2:
   - H2: Step N:
   - H2: Common mistakes (and how to avoid them)
   - H2: FAQ
   - Conclusion + next step CTA
   ```
   Honesty check: Did you answer the question in the first 200 words, or did you make them scroll through background context to find the actual steps?

5. **The "Answer First" rule.** Every article must answer the headline question within the first 200 words. No exceptions.

   - Cost article: give the real number or range in paragraph 1
   - Problems article: name the top 3 problems in the intro
   - Versus article: give the one-sentence verdict in the intro
   - Best article: name the top pick in the intro
   - How-To article: state the core process in the intro

   If the intro does not answer the headline question directly, rewrite it before proceeding to the body.

6. **Write the article**:
   - **Title**: 50-60 chars, primary keyword in first half
   - **Meta description**: 140-155 chars, primary keyword + benefit + soft CTA
   - **Intro**: 100-150 words. Answer the keyword question directly. Answer-first.
   - **Body**: H2 sections per Big 5 type structure above. Each section 200-400 words.
   - **Use the keyword** in: H1, first paragraph, one H2, image alt text, conclusion. Avoid keyword stuffing.
   - **Semantic variants**: include 5-10 LSI/related terms naturally
   - **Internal links**: 3-5 to other pieces in `knowledge/content-library/` or pages on the user's site
   - **External links**: 2-3 to authoritative sources (with the source link)
   - **One table** if it adds clarity (mandatory for Versus and Best articles)
   - **One FAQ section** at the end (3-5 questions, 50-80 words each)
   - **Conclusion**: 100-150 words. Summarize, then CTA.

7. **Voice rules**:
   - Match `knowledge/brand/voice.md`
   - Avoid AI tells: no "In today's fast-paced world", no "navigating the complexities of", no "leverage", no em dashes
   - Use specific examples and named companies, not "many businesses"
   - Active voice

8. **Self-check**:
   - [ ] Article categorized as one of the Big 5 (or explicitly flagged as not Big 5)
   - [ ] Headline question answered in the first 200 words
   - [ ] For Cost articles: real number or range given in paragraph 1 (not "contact us")
   - [ ] For Problems articles: real problems named, not softened hedges
   - [ ] For Versus articles: competitor strengths acknowledged honestly
   - [ ] For Best articles: includes options the company doesn't sell
   - [ ] Primary keyword appears in title, first 100 words, one H2, conclusion
   - [ ] 3-5 internal links present
   - [ ] At least one table or list for scanability
   - [ ] FAQ section present
   - [ ] Word count matches target ±10%
   - [ ] No em dashes
   - [ ] Trust check: would a buyer trust this more than a competitor's article on the same topic? If not, what needs to change?

9. **Save** to `output/seo-article/<DD-MM-YYYY>-<keyword-slug>.md` with frontmatter:
   ```yaml
   ---
   format: seo-article
   big-5-type: <Cost | Problems | Versus | Best | How-To | Other>
   primary-keyword: <keyword>
   intent: <informational|commercial|transactional|comparison|how-to>
   target-length: <words>
   actual-length: <words>
   internal-links: <count>
   meta-title: <title>
   meta-description: <desc>
   answer-first-word-count: <word number where headline question is answered>
   created: DD-MM-YYYY
   ---
   ```

10. **Offer follow-ons**:
    - LinkedIn post promoting the article
    - 3 supporting articles to build a topic cluster (suggest which Big 5 types would complement this one)
    - Schema markup recommendation (Article, FAQ, HowTo, Product)

## Rules

- Categorize every article as a Big 5 type before writing the outline. If you skip this, the structure will be generic and the ranking potential drops.
- Answer the headline question in the first 200 words. Every time. No exceptions.
- Never write SEO content without the top 3 SERP URLs. Without them, you are guessing what to beat.
- Never stuff keywords. Density above 2% is a red flag.
- For Cost articles: if the user says "we don't publish pricing", tell them: "Competitors or review sites will answer this question for you, and they'll frame it however they want. Answering it honestly gives you control of the narrative."
- For Problems articles: if the user says "we don't want to highlight our problems", tell them: "Buyers are already researching this. If you don't write it, a competitor or G2 review will. An honest article from you builds more trust than a defensive one."
- People-first content. If you would not want to read this as a human, do not publish it.
- Every H2 must answer a question someone actually searches. If you cannot turn an H2 into a "People also ask" question, rework it.

## Quick Reference: Big 5 Framework

| Type | Headline pattern | Answer-first rule | Honesty requirement |
|---|---|---|---|
| Cost and Price | "How Much Does X Cost?" | Give range in paragraph 1 | Real numbers. No "contact us." |
| Problems | "X Problems: What to Know" | Name top 3 problems in intro | Real problems, not softened hedges |
| Versus | "X vs Y: Which Is Right for You?" | Give verdict in paragraph 1 | Acknowledge where the competitor wins |
| Best / Reviews | "Best X for [Situation]" | Name top pick in paragraph 1 | Include options you don't sell |
| How-To | "How to [Achieve Outcome]" | State core process in intro | Answer the question. Don't bury the steps. |
