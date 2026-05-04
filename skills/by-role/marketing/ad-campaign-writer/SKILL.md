---
name: ad-campaign-writer
description: Write paid ad copy for LinkedIn, Google, Meta, and YouTube. Produces multiple variants per platform, each targeting a different Eugene Schwartz awareness level and Cialdini persuasion principle. Use when the user asks for ad copy, ad variants, "write LinkedIn ads", Google ads, Meta ads, paid social copy, ad headlines, or wants creative for a paid campaign. Reads brand voice, ICP, and positioning from knowledge/.
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

## Channels this skill handles

| Channel | Format | Key limits |
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
  [Authority]: "Rated #1 Onboarding Tool"
  [Scarcity]: "Free Trial Ends Friday"
  [Commitment]: "Start Free in 5 Minutes"
  [Outcome-led]: "Activate Users in 6 Days"
  [Problem-led]: "Onboarding Killing Trials?"
  ... (fill to 15 mixing approaches)

Descriptions (4, each ≤90 char):
  1. [Social proof + CTA]: "Trusted by Ramp, Linear, and 240+ PLG teams. Start your free trial today."
  2. [Reciprocity]: "Free onboarding audit included with every trial. See where users drop off in 24 hours."
  3. [Authority + outcome]: "Ship your first onboarding flow in 6 days. Rated best-in-class by G2 reviewers."
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
- [ ] Each variant has a named awareness level and Cialdini principle
- [ ] No two variants use the same combination
- [ ] Cold audience variants do NOT lead with product name or brand
- [ ] Retargeting variants get straight to the offer
- [ ] Character limits respected (hard limits, no exceptions)
- [ ] Hypothesis written for each variant (this is what gets tested)
- [ ] Visual briefs written for every variant

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
- LinkedIn: 0.5-1.5% CTR, $X CPL
- Google search: 3-6% CTR, $X CPC
- Meta: 1-2% CTR, $X CPL
```

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
