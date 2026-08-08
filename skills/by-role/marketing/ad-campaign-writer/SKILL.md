---
name: ad-campaign-writer
description: Write paid ad copy for LinkedIn, Google, Meta, and YouTube. Produces multiple variants per platform, each targeting a different Eugene Schwartz awareness level and Cialdini persuasion principle. Use when the user asks for ad copy, ad variants, "write LinkedIn ads", Google ads, Meta ads, paid social copy, ad headlines, or wants creative for a paid campaign. Reads brand voice, ICP, and positioning from knowledge/. For organic social posts, see linkedin-post or social-calendar. For the landing page the ad points at, see landing-page-writer. For testing variants, see ab-copy-writer.
metadata:
  grounded_in:
    - "Breakthrough Advertising - Eugene Schwartz"
    - "Influence - Robert Cialdini"
  reads:
    - knowledge/brand/voice.md
    - knowledge/icp/personas.md
    - knowledge/markets/positioning.md
    - knowledge/services/
  writes:
    - output/ad-campaign/
---

# ad-campaign-writer

Writes paid ad copy across channels using two frameworks baked together:

1. **Eugene Schwartz's Awareness Levels** (*Breakthrough Advertising*) - determines what to say based on where the buyer is in their journey
2. **Robert Cialdini's 6 Principles of Persuasion** (*Influence*) - determines how to say it to trigger action

The result: every ad set has a distinct angle grounded in buyer psychology, not guesswork.

## The two frameworks

### Framework 1: Schwartz's 5 Awareness Levels

The biggest mistake in ad copy: writing the same message regardless of where the audience is in their journey. Schwartz's levels fix this.

| Level | Who they are | What they believe | What your copy must do |
|---|---|---|---|
| **1. Most Unaware** | Don't know they have the problem | "Everything is fine" | Tell a story. Don't mention the product. Introduce the problem through emotion or narrative. |
| **2. Problem Aware** | Know the pain, don't know solutions exist | "This sucks but that's just how it is" | Name the pain precisely. Agitate it. Show you understand. Introduce the idea that solutions exist. |
| **3. Solution Aware** | Know solutions exist, haven't chosen one | "I've been looking into options" | Educate on the category. Show why your approach is right. Don't lead with your brand name yet. |
| **4. Product Aware** | Know your product, not convinced yet | "I've heard of them. Not sure if they're right for me" | Features, proof, objection handling. This is where testimonials and case studies earn their place. |
| **5. Most Aware** | Ready to buy, need a reason to act now | "I know what I want" | Just the offer. Pricing, urgency, the specific CTA. No education needed. |

**Rule:** Retargeting audiences are typically Level 4-5. Cold audiences are Level 1-3. Never run a Level 5 ad to a cold audience - it will fail.

**How to diagnose the level when the user does not know.** Ask these three, in order, and stop at the first "no":

1. Has this audience ever visited the site or engaged with the brand? No -> Level 1-3.
2. Do they already use a product in this category (a competitor, a spreadsheet, an internal tool)? No -> Level 1-2. Yes -> Level 3+.
3. Have they hit a pricing, demo or trial page? Yes -> Level 4-5.

If the user cannot answer question 1 from their own analytics or ad platform audience definitions, do not guess the level. Write `[NEEDS INPUT: audience source and prior engagement]` and produce Level 2-3 copy, which is the only range that is safe when the audience is unknown, because it names a pain without assuming familiarity.

### Framework 1b: Schwartz's 5 Stages of Market Sophistication

The second model in *Breakthrough Advertising*, and the one most ad writers skip. Awareness is about the **buyer**. Sophistication is about the **market**: how many claims like yours they have already heard. Two audiences at the same awareness level need different copy if their markets are at different sophistication stages.

| Stage | State of the market | What the headline must do | What fails here |
|---|---|---|---|
| **1. First** | You are the first to make this claim | State the claim plainly. "Get X." | Cleverness. Nobody needs convincing yet. |
| **2. Second** | Competitors are making the same claim | Enlarge the claim. Bigger, faster, more specific version. | Repeating the stage-1 claim verbatim. |
| **3. Third** | The claim is worn out, nobody believes it | Lead with the **mechanism**. How it works, not what it does. | Another superlative. |
| **4. Fourth** | Competitors are all selling mechanisms | Elaborate the mechanism. Make yours more complete or easier. | A bare mechanism claim. |
| **5. Fifth** | The market is exhausted and cynical | Shift to **identification**: who this is for, what it says about them. | Any product claim at all. |

**Decision rule:** count how many competitors in `knowledge/markets/positioning.md` make the same headline promise. Zero to one competitor, write stage 1-2 copy. Two to four, go to the mechanism (stage 3). Five or more, or the user says "everyone says that", go to identification (stage 5). If `knowledge/markets/positioning.md` has no competitor list, ask, and if the user cannot say, default to stage 3 - the mechanism is the safest claim because it is checkable.

Schwartz's own summary of the interaction is worth holding onto: awareness decides **what you may say first**, sophistication decides **how hard you have to work to be believed**.

### Framework 2: Cialdini's 6 Principles

Each ad variant tests a different persuasion lever. Use all 6 across a campaign, measure which performs for this audience.

| Principle | How to apply in ads |
|---|---|
| **1. Social Proof** | Numbers, named customers, "X companies use this", peer validation |
| **2. Authority** | Awards, publications, expertise, specific credentials |
| **3. Scarcity** | Limited spots, pricing ends, cohort-based intake |
| **4. Reciprocity** | Free resource, tool, audit, or insight in the ad itself |
| **5. Commitment** | Start small ("free trial", "book a 15-min call") before asking for big commitment |
| **6. Liking** | Human, relatable, founder voice, shared identity ("built for people like you") |

Later editions of *Influence* add a seventh principle, **Unity** (shared identity, "one of us"). Treat it as an optional seventh variant, not a replacement for Liking.

**Which principle to reach for first, by awareness level:**

| Awareness level | Try first | Try second | Avoid |
|---|---|---|---|
| 1-2 Unaware / Problem Aware | Liking, Reciprocity | Social Proof | Scarcity - there is no desire yet to make scarce |
| 3 Solution Aware | Authority, Reciprocity | Social Proof | Commitment - they have not picked a category winner |
| 4 Product Aware | Social Proof, Authority | Commitment | Reciprocity - a free guide now reads as a stall |
| 5 Most Aware | Scarcity, Commitment | Social Proof | Liking - they do not need warming, they need the offer |

**Cialdini's own constraint, and it is not optional:** every principle only works when the underlying fact is true. Scarcity that is not scarce, social proof that is not proof, and authority that is not earned all convert once and then poison the account. If the fact behind a principle is not in `knowledge/services/` or `knowledge/company.md`, do not use that principle for the variant. Pick a different one.

## Channels this skill handles

**These are starting defaults recorded at authoring time, not current published specs.** Every one of these limits has changed at least once since the platforms launched, several are display-truncation points rather than hard ceilings, and a few differ by placement and by market. Verify in the ad platform's own current documentation before shipping, and where this account's own ad library shows what actually rendered, that wins over the table.

| Channel | Format | Key limits (verify before shipping) |
|---|---|---|
| **LinkedIn Sponsored Content** | Single image, carousel, video | 150 char intro, 70 char headline |
| **LinkedIn Message Ads** | InMail | 60 char subject, 500 word body |
| **Google Search** | Responsive | 15 headlines (30 char each), 4 descriptions (90 char each) |
| **Google Display** | Responsive display | 5 short headlines, 5 long, 5 descriptions |
| **Meta feed** | Image, carousel, video | 125 char primary text, 40 char headline |
| **Meta Reels/Stories** | Vertical video | 15-30 sec script |
| **YouTube pre-roll** | Skippable | 5-sec hook + 30-sec full script |

## Inputs needed

- **Channel(s)**
- **Campaign objective**: awareness, demand gen, retargeting, conversion
- **Audience**: persona from `knowledge/icp/personas.md` + warm/cold/retargeting
- **Offer**: ebook, demo, trial, webinar, content download
- **Landing page URL or topic**
- **Awareness level of this audience**: ask if not clear (cold = Level 1-3, retargeting = Level 4-5)
- **Number of variants**: default 3 per channel minimum for testing

## Process

### Step 1: Load context
Read `knowledge/brand/voice.md`, the relevant persona, `knowledge/markets/positioning.md`, and the relevant service file.

### Step 1b: Triage the brief before writing a single line

Paid media makes bad inputs expensive rather than merely wrong. Run these checks and say what you found. The first three are stop conditions.

| Check | Warning sign | Action |
|---|---|---|
| Offer matches awareness | Cold audience pointed at a demo booking | **Stop.** Tell the user the ad will spend for clicks that do not convert, and propose a lower-commitment offer for the cold set. |
| Landing page matches the ad | The page sells the product, the ad promises a guide | **Stop.** Message-match failure is the single most common cause of a high CTR with no conversions. Fix the page or change the offer. |
| Claims are sourced | A number the user cannot point to a source for | **Stop.** Write `[NEEDS INPUT: source for <claim>]` and do not write around it. |
| Audience size | Fewer than a few thousand matched people | Flag it. Below that, four variants will not separate from noise within a normal test window, so cut to two. |
| Variant count vs budget | More variants than the budget can give meaningful volume | Flag it. Split budget across too many variants and every result stays inconclusive. Recommend cutting to the two strongest hypotheses. |
| Regulated claim | Health, finance, legal, employment, housing, credit | Flag for legal review before publishing, and check the platform's restricted-category policy, which often bans targeting options as well as wording. |

### Step 2: Determine awareness level
Ask the user: "Is this audience cold (never heard of you), warm (visited your site, engaged with content), or retargeting (already showed buying intent)?"

Map to Schwartz levels:
- Cold → Levels 1-3 (depending on category awareness)
- Warm → Levels 3-4
- Retargeting → Levels 4-5

### Step 3: Build the variant matrix
For each channel, produce variants that cross awareness levels with Cialdini principles:

```
Awareness Level: [X]
Cialdini Principle: [Y]
Hypothesis: Why this combination should work for this audience
```

Minimum variant set for a cold LinkedIn campaign targeting Level 2-3:
```
Variant A: Level 2 (Problem Aware) × Social Proof
Variant B: Level 2 (Problem Aware) × Reciprocity
Variant C: Level 3 (Solution Aware) × Authority
Variant D: Level 3 (Solution Aware) × Liking
```

Minimum variant set for retargeting (Level 4-5):
```
Variant A: Level 4 (Product Aware) × Social Proof (testimonial-led)
Variant B: Level 4 (Product Aware) × Scarcity (limited time offer)
Variant C: Level 5 (Most Aware) × Commitment (clear CTA, specific offer)
```

### Step 4: Write per channel

**LinkedIn Sponsored Content:**
```
Variant A: [Awareness Level 2 × Social Proof]
  Hypothesis: Cold audience experiencing the problem responds to peer validation
  Intro (≤150 char): <name the pain in their exact words - NO mention of product>
  Headline (≤70 char): <peer proof + outcome>
  Description (≤100 char): <supporting social proof line>
  CTA button: [Learn More | Download | Register]
  Visual brief: <real customer / real result, not product UI>

Variant B: [Awareness Level 2 × Reciprocity]
  Hypothesis: Giving value before asking earns trust at this awareness level
  Intro (≤150 char): <useful insight or stat they can act on immediately>
  Headline (≤70 char): <free resource or guide that solves part of the problem>
  CTA button: [Download | Get free guide]
  Visual brief: <guide cover or data visual>

Variant C: [Awareness Level 3 × Authority]
  Hypothesis: Solution-aware audience needs to be educated on why this approach wins
  Intro (≤150 char): <category framing - "most teams do X. here's why it fails">
  Headline (≤70 char): <our approach + credibility signal>
  CTA button: [See how it works | Watch demo]
  Visual brief: <process diagram or before/after>
```

**Google Search Ads (responsive):**
```
Note: Google Search is typically Level 3-5 (they're searching for a solution)

Headlines (15, each ≤30 char) - mix across principles:
  [Social Proof]: "240+ Teams Use Threadline"
  [Authority]: "[Authority claim from knowledge/services/ - never invented]"
  [Scarcity]: "Free Trial Ends Friday"
  [Commitment]: "Start Free in 5 Minutes"
  [Outcome-led]: "Activate Users in 6 Days"
  [Problem-led]: "Onboarding Killing Trials?"
  ... (fill to 15 mixing approaches)

Descriptions (4, each ≤90 char):
  1. [Social proof + CTA]: "Trusted by [named customers from knowledge/company.md] and [N] teams. Start your free trial today."
  2. [Reciprocity]: "Free onboarding audit included with every trial. See where users drop off in 24 hours."
  3. [Authority + outcome]: "Ship your first onboarding flow in [N] days. [Third-party rating only if it genuinely exists]."
  4. [Scarcity + commitment]: "14-day trial, no card needed. Pricing increases 15-05-2026."

Display path: /<keyword>/<benefit>
```

**Meta feed:**
```
Variant A: [Level 2 × Liking] - relatable human story
  Primary text (≤125 char): <founder/customer voice, problem narrative, first person>
  Headline (≤40 char): <outcome promise>
  Description (≤30 char): <social proof or urgency>
  CTA: [Learn More]
  Visual brief: <authentic human image - real person, not stock>

Variant B: [Level 4 × Scarcity] - retargeting
  Primary text (≤125 char): <they've seen you before - cut to the offer>
  Headline (≤40 char): <specific offer + deadline>
  CTA: [Sign Up | Get Started]
  Visual brief: <product result / dashboard>
```

### Step 5: Voice checks
- Match `knowledge/brand/voice.md`
- Specific numbers ("47% faster", "6 days", "240 customers")
- Active voice, present tense
- No: "revolutionary", "best-in-class", "synergy", "leverage"
- No claims not documented in `knowledge/services/`

### Step 6: Self-check

Each item is checkable by reading the output file. If you cannot point at the line that satisfies it, it fails.

- [ ] Every variant block carries an explicit `Awareness Level: N` and `Cialdini Principle: <name>` line
- [ ] The variant matrix table has no duplicated (level, principle) pair
- [ ] Every variant names a market sophistication stage, and the stage matches the competitor count used to pick it
- [ ] In every Level 1-3 variant, the brand and product name do not appear in the first line of copy. Search the file for the brand name and check each hit's position
- [ ] Every Level 5 variant contains a specific offer term (price, deadline, trial length, or a named CTA destination)
- [ ] Every character-limited field carries its own measured count in the output, written as `(N chars)`, and every one was checked against the platform's current published spec today, not against the table in this skill. Several of these limits are display-truncation points rather than hard ceilings, so never amputate correct copy to hit a number you did not verify
- [ ] Every variant has a `Hypothesis:` line stating what a win would prove, not just what the ad says
- [ ] Every variant has a `Visual brief:` line naming a concrete subject, not an adjective
- [ ] Every proper noun, number, rating and customer name in the file traces to a line in `knowledge/` or to something the user supplied in this session. List the sources in the README
- [ ] The README kill and scale thresholds are numbers from this account's history, or are marked `[NEEDS INPUT]`. No benchmark from memory

### Step 7: Save
`output/ad-campaign/<DD-MM-YYYY>-<campaign-slug>/`

```
output/ad-campaign/25-04-2026-q2-launch/
├── README.md (awareness level map, test plan, benchmarks)
├── linkedin-sponsored.md
├── google-search.md
├── meta-feed.md
└── [other channels]
```

README.md must include:
```
# <Campaign> ad creative

**Audience**: <persona> | <cold/warm/retargeting>
**Awareness level targeted**: [1-5]
**Offer**: <offer>

## Variant matrix
| Variant | Channel | Awareness Level | Cialdini Principle | Hypothesis |
|---|---|---|---|---|

## Test plan
- Run all variants: [X days]
- Kill threshold: <[CTR below Y]>
- Scale threshold: <[CTR above Z, CPL below $X]>

## Benchmarks
- LinkedIn: [UNVERIFIED - replace with this account's own historical CTR]
- Google search: [UNVERIFIED - replace with this account's own historical CTR]
- Meta: [UNVERIFIED - replace with this account's own historical CTR]

Any industry benchmark carried into this section without a named, dated source is a
fabricated number. This account's own last-90-days performance is the only comparison
that is valid for setting a kill threshold.
```

### Step 8: Set the kill and scale thresholds

A variant set without stopping rules runs until someone remembers to look at it. Derive both numbers from this account's own history in `knowledge/kpis.md` or the ad platform:

1. **Kill threshold**: the variant's CTR falls below the account's trailing median for that channel, after it has served enough impressions to be readable. If the account has no history, do not invent a number - state the rule as "kill the bottom variant once the top variant has twice its click volume" which needs no benchmark.
2. **Scale threshold**: cost per qualified lead is below the account's blended target from `knowledge/kpis.md`. CTR alone is never a scale signal, because the cheapest clicks are usually the least qualified.
3. **Minimum run**: never judge before the platform's own learning period has completed, and never on a weekend-only or holiday window.
4. **Priority when results conflict**: conversion rate beats cost per lead, cost per lead beats CTR, CTR beats impressions. A variant that wins on CTR and loses on conversion is a wrong-audience signal, not a copy win.

## Rules

- Always identify the awareness level before writing. Copy direction changes completely between levels.
- Never run Level 5 copy to a cold audience. It assumes familiarity that doesn't exist.
- Always produce minimum 3 variants. One ad is not testable.
- Always write the visual brief. Designers cannot ship without it.
- Never fabricate claims. If a user wants a stat not in `knowledge/services/`, flag it.
- Regulated industries: include "Confirm with legal before publishing" on any health, finance, or legal claim.

## Quick reference: awareness level copy direction

| Level | First line of copy must... | Never do at this level |
|---|---|---|
| 1 - Most Unaware | Tell a relatable story with no product mention | Name the brand or product |
| 2 - Problem Aware | Name their pain precisely, in their words | Lead with a solution |
| 3 - Solution Aware | Frame the category, educate on approach | Assume they know your brand |
| 4 - Product Aware | Address objections, show proof | Educate on why the category matters |
| 5 - Most Aware | Just the offer and the CTA | Explain what the product does |

## Never invent

- **No customer name, third-party rating, award, user count, or performance figure** unless it is
  in `knowledge/company.md` / `knowledge/services/` or supplied by the user. The worked examples in
  this skill are shape illustrations. Never carry a name or a number out of them.
- Filling 15 headline slots is not a licence to generate 12 more claims. Slots you cannot source
  read `[NEEDS INPUT: <what>]`.
- Never state a benchmark you did not measure. This account's own history is the only valid
  comparison.

## What this skill cannot know

These are limitations of the skill, not of the campaign. Anything in this list that reaches the output must be labelled `[UNVERIFIED]` there, not quietly asserted.

- **Current platform character limits, ad formats, image and video specs, and policy rules.** Every table in this file is a starting default from authoring time. Open the ad platform's current documentation before shipping.
- **Whether a claim is permissible under the platform's advertising policy in your market.** Restricted categories differ by country, and some restrict targeting options as well as wording. Comparative claims and superlatives are separately regulated in several jurisdictions.
- **Current CPC, CPL or CTR for this account, industry or geography.** No benchmark is stated here for that reason. Pull the account's own trailing numbers.
- **Whether the landing page still says what the ad promises.** Message match is checked by opening the page, not by reading the brief.
- **Whether a named customer has agreed to appear in paid media.** Case-study consent and ad consent are different permissions, and paid placement is often excluded from the original agreement.

## Related skills

- `/campaign-brief` for the objective, budget and audience decisions that must exist before ad copy is written
- `/landing-page-writer` for the destination page, when the ad and page do not currently make the same promise
- `/ab-copy-writer` for turning the variant matrix here into a properly powered test with a stopping rule
- `/messaging-framework` when every variant keeps drifting, which usually means the core message was never fixed
- `/positioning-doc` when the sophistication check lands on stage 4-5, because the fix is positioning and not copy
- `/customer-persona` when the awareness-level diagnosis cannot be answered from existing persona files
- `/linkedin-post` and `/social-calendar` for organic posting, which is a different job from paid creative
- `/copy-review` for a second pass on finished variants before they go into the ad account
- `/kpi-review` for the account's own trailing CTR, CPL and conversion rates, which override every default here

