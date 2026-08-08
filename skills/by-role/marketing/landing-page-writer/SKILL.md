---
name: landing-page-writer
description: Write landing page copy for product pages, campaign pages, lead-gen pages, pricing pages, and feature pages. Use when the user asks for landing page copy, product page, lead magnet page, "write the page for X", pricing page copy, feature page, hero section, or web copy that converts. Uses the StoryBrand SB7 framework (Donald Miller) to structure every page. Reads brand voice, positioning, and ICP from knowledge/. For improving an existing page's copy, see copy-review. For diagnosing why a page does not convert, see page-cro. For the ads driving traffic to it, see ad-campaign-writer.
metadata:
  grounded_in:
    - "Building a StoryBrand (SB7) - Donald Miller"
  reads:
    - knowledge/brand/voice.md
    - knowledge/icp/personas.md
    - knowledge/markets/positioning.md
    - knowledge/services/
  writes:
    - output/landing-page/
---

# landing-page-writer

Writes conversion-focused landing page copy using the **StoryBrand SB7 framework** (Donald Miller, *Building a StoryBrand*). Every page positions the customer as the hero, the brand as the guide - not the other way around.

**The core SB7 insight:** Most companies make themselves the hero of their own story. Customers don't care. Customers care about their own story. A brand that positions itself as the guide (Gandalf, not Frodo) converts dramatically better than one that leads with how great it is.

## The SB7 arc, in order

*Building a StoryBrand* is a sequence, not a checklist. The seven elements only work in this
order, because each one is the answer to the question the previous one raises in the reader.

| # | Element | The reader's unasked question it answers | If you skip it |
|---|---|---|---|
| 1 | A character | "Is this about me?" | The reader never enters the story |
| 2 | has a problem | "Do you understand what I am dealing with?" | Nothing creates the need to keep reading |
| 3 | and meets a guide | "Can I trust you, and have you done this before?" | You read as another vendor with a claim |
| 4 | who gives them a plan | "What exactly happens if I say yes?" | Anxiety about the unknown blocks the click |
| 5 | and calls them to action | "What do I do right now?" | The reader agrees with you and leaves |
| 6 | that helps them avoid failure | "What is at stake if I do nothing?" | Inertia wins, because doing nothing costs nothing |
| 7 | and ends in success | "What does my life look like after?" | There is nothing to want |

Two of Miller's tests are used as gates in this skill.

**The grunt test.** A stranger looking only at the area above the fold, for five seconds, must be
able to say three things: what you offer, how it makes their life better, and what they do next.
If any of the three is missing or takes reading to work out, the hero section fails and gets
rewritten before anything below it is drafted.

**The one-liner.** Before the page, write one sentence in Miller's shape: character, problem,
plan, success. Example shape, not example copy: "Most [role] are stuck with [problem]. We give
them [plan] so they can [success]." Every H1 and final CTA on the page must be consistent with
that sentence. If they are not, the page argues with itself.

**Element ordering by page type.** The arc stays in order, but pages compress differently.

| Page type | Leads with | Compresses or drops | Why |
|---|---|---|---|
| Product page | Character and problem | Nothing, run the full arc | The visitor is comparing, they need all seven |
| Campaign / launch page | Success, then problem | Guide is a single proof bar | Traffic arrives warm from the campaign |
| Lead magnet page | Plan (what is inside) | Failure, drop it entirely | Failure framing on a free asset reads as pressure |
| Pricing page | Plan and CTA | Problem, one line only | The visitor is past the problem, they are costing it |
| Feature page | Problem and plan | Character, one line only | They arrived already knowing who they are |

## When to use

- "Write the landing page for our new product"
- "Draft the campaign page for <event>"
- "Write copy for the pricing page"
- "We need a lead magnet page for the ebook"
- "Write the hero section for our homepage"

## Page types

| Type | Length | Sections |
|---|---|---|
| **Product page** | Long | Hero, social proof, problem, guide intro, plan, success, failure, CTA |
| **Campaign / launch page** | Medium | Hero, why-now, what's new, social proof, CTA |
| **Lead magnet page** | Short | Hero, what's inside, who it's for, form, social proof |
| **Pricing page** | Medium | Hero, plan comparison, feature matrix, FAQ, CTA |
| **Feature page** | Medium | Hero, problem, how it works, use cases, CTA |
| **Hero only** | 1 section | H1 + sub + CTA |

## Inputs needed

- **Page type** (from table)
- **Audience persona**: from `knowledge/icp/personas.md`
- **Single conversion action**: book demo, sign up free, download, contact sales, start trial
- **Offer specifics**: what the visitor gets, how long, any pricing
- **Existing assets**: testimonials, customer logos, stats, screenshots
- **Constraints**: word count, brand patterns, must-include phrases

## Process

### Step 1: Load context
Read `knowledge/brand/voice.md`, the relevant persona, `knowledge/markets/positioning.md`, and the relevant service file. If brand voice is missing, stop and say: "Run `/brand-context` first."

### Step 2: Complete the SB7 BrandScript
Before writing a single word of copy, answer all 7 elements. These answers drive every section.

```
SB7 BrandScript for <Company/Product>

1. CHARACTER (the hero - who is the customer?)
   The customer is: [role, context, goal]
   What they want: [one thing - specific and simple]
   "A <role> who wants to <outcome>"

2. PROBLEM
   External problem (the practical problem): [what is broken in the world]
   Internal problem (how it makes them feel): [frustrated, embarrassed, overwhelmed...]
   Philosophical problem (why it's unjust): [it shouldn't have to be this way]
   The villain (what causes the problem): [never a person - a force, a system, a situation]

3. GUIDE (the brand - empathy + authority)
   Empathy statement: "We know what it's like to <feel the internal problem>"
   Authority proof: [3 specific credentials - customers helped, stats, awards]

4. PLAN
   3-step plan that reduces anxiety about buying:
   Step 1: [simple verb phrase]
   Step 2: [simple verb phrase]
   Step 3: [simple verb phrase]

5. CALL TO ACTION
   Direct CTA (buy, schedule, sign up): [exact button copy]
   Transitional CTA (for those not ready): [low-commitment offer]

6. SUCCESS (what their life looks like after)
   3 specific outcomes - make them vivid:
   - [functional win: what they can do now]
   - [emotional win: how they feel]
   - [status win: how others see them]

7. FAILURE (cost of not acting - used sparingly near the CTA)
   What happens if they do nothing: [specific, real, not apocalyptic]
```

### Step 3: Map BrandScript to page sections

```
## Hero
H1 (8-12 words): The CHARACTER's WANT + hint of the PLAN
  ✓ "Turn trial signups into activated users in 6 days"
  ✗ "The most powerful onboarding platform" (brand as hero)
Sub (15-25 words): External problem solved + who it's for
Primary CTA: Direct CTA from BrandScript (Step 5) - 2-4 words, action verb
Secondary CTA: Transitional CTA from BrandScript (Step 5)
Visual brief: Customer succeeding (success state), not product screenshot as hero

## Social proof bar (GUIDE authority - Step 3)
- 5-8 customer logos, OR
- 1 headline stat ("Trusted by 240+ growth teams"), OR
- 1 line testimonial with photo
Position: immediately below the fold

## Problem section (Steps 2 + 3)
H2: Name the EXTERNAL PROBLEM in the customer's exact language
Body (60-80 words): Agitate the INTERNAL PROBLEM (how it feels)
  - Use "if you're like most [persona], you've felt..." construction
  - Name the VILLAIN (the system/situation causing the problem, not a competitor)
Empathy line (15-25 words): "We know what that's like. [Empathy statement from Step 3]"

## Guide intro (GUIDE - Step 3)
Authority proof block:
  - [Stat: X customers / Y outcomes]
  - [Credibility: notable customer names or recognition]
  - [Differentiation: what makes us the right guide]

## Plan section (Step 4)
H2: "Here's how it works" or "Getting started is simple"
3-step plan (NOT features):
  Step 1: [Action verb] + [what they do]
  Step 2: [Action verb] + [what happens]
  Step 3: [Action verb] + [outcome they unlock]
Note: Steps should reduce the fear of getting started, not describe features

## Success section (Step 6)
H2: Paint the SUCCESS state in vivid, specific terms
Body: What their world looks like after using the product
Use all 3 success types:
  - Functional: "You ship your first onboarding flow in a week"
  - Emotional: "You stop worrying about activation and start measuring it"
  - Identity: "Your team becomes the team that fixed the onboarding problem"
Use customer quotes here if available (proof + success combined)

## Proof section
- 1 hero case study: [metric change] for [customer name]
- 2-3 testimonials: name + role + company + 1-sentence result
- 1 aggregate stat

## Pricing (if applicable)
Confirm actual prices before writing. Structure: plan names + what each includes + which is recommended (highlight the middle option).

## FAQ (5-8 questions)
Address FAILURE fears (Step 7) disguised as questions:
  - "What if it doesn't work for us?" (failure fear)
  - "How long does setup take?" (inertia fear)
  - "How is this different from [competitor]?" (uncertainty fear)
Never: "Is your product good?" / "Do you have a free trial?" (obvious, not objection-handling)

## Final CTA
H2: Restate the SUCCESS outcome (not the product name)
Body (30-50 words): What happens in the next 30 seconds after they click
Direct CTA button: Same as hero
FAILURE reminder (1 line, optional): Brief, factual - "Every week without X costs you Y"
Risk reducer: "No credit card" / "Cancel anytime" / "Free 14-day trial"
```

### Step 4: Voice and conversion checks

**Voice:**
- Match `knowledge/brand/voice.md` exactly
- Second person ("you", "your team") throughout
- Specific numbers everywhere. "4x faster" not "much faster"
- Active voice, present tense
- No: "leverage", "unlock", "robust", "seamless", "best-in-class", "industry-leading"
- No em dashes

**Conversion psychology (beyond SB7):**
- Above the fold: customer knows what it is, who it's for, what to do next
- Pain always before solution - customers don't buy products, they buy relief
- Proof before the ask - credibility before commitment
- One conversion action, repeated consistently

### Step 5: Self-check

Each item is answerable by pointing at the draft. Anything that needs an opinion is not a check.

Structure:
- [ ] The completed BrandScript appears above the copy in the working file, all 7 elements filled
- [ ] The one-liner is written down, and the H1 and final CTA are both consistent with it
- [ ] Grunt test: name the exact line that says what it is, the line that says how life improves,
      and the button that says what to do. Three lines, above the fold, all present
- [ ] H1 subject is the customer or the customer's outcome. Count how many times the company name
      appears above the fold. More than once fails
- [ ] The 3 plan steps are verb phrases describing what the customer does, and none of them is a
      product feature name
- [ ] The success section contains one functional, one emotional and one identity outcome. Point
      at each
- [ ] Failure appears exactly once, near the final CTA, in one sentence or less
- [ ] Social proof appears before the first fold break
- [ ] Count the distinct CTA verbs on the page. There must be exactly one direct CTA verb, used
      in every direct CTA button

Sourcing:
- [ ] Every statistic, customer name, logo and quote traces to a user-supplied asset or `knowledge/`
- [ ] Every unsourced proof slot reads `[PROOF NEEDED: ...]` or `[NEEDS INPUT: ...]`
- [ ] Prices in the draft were confirmed by the user in this conversation

Voice:
- [ ] Zero em dashes and zero en dashes
- [ ] Zero occurrences of: leverage, unlock, robust, seamless, best-in-class, industry-leading
- [ ] Every phrase in the brand's "avoids" list appears zero times

### Step 6: Save
`output/landing-page/<DD-MM-YYYY>-<slug>.md` with frontmatter:
```yaml
---
format: landing-page
page-type: <type>
framework: storybrand-sb7
conversion-action: <action>
audience: <persona>
created: DD-MM-YYYY
---
```

### Step 7: Companion assets
- Meta title (60 chars) and meta description (155 chars)
- Open Graph copy for social shares
- Confirmation page copy (post-conversion)
- Email follow-up after form submit (link to `/email-nurture`)

## Rules

- Complete the BrandScript before writing any copy. Copy written without it will be brand-as-hero.
- Keep the arc in the order *Building a StoryBrand* sets out. Reordering it, for example putting
  the guide's credentials before the customer's problem, is the single most common way a page
  ends up sounding like a company brochure while still containing all seven elements.
- One conversion action. Always. If the user names two, force them to pick one.
- Hero copy must work without the rest of the page.
- Never write pricing without confirming actual prices with the user.
- **Never write a testimonial, customer name, case-study metric, logo claim, or authority stat
  that the user did not supply or that is not in `knowledge/`.** Every proof slot on this page
  is a place an agent will otherwise invent a named customer, and a fabricated testimonial
  attributed to a real company is a legal and reputational incident, not a draft defect.
- If a proof slot has no real asset, emit `[PROOF NEEDED: 1 customer logo / 1 metric / 1 quote]`
  and list what the team has to collect. An honest gap ships. A fake quote does not.
- Visual briefs are required for every section that needs an image.
- If the page involves regulatory claims (medical, financial, legal), flag for legal review.

## SB7 Quick reference

| SB7 element | Page section | Common mistake |
|---|---|---|
| Character | Hero H1 | Making the brand the character |
| Problem | Problem section | Skipping internal/philosophical problem |
| Guide | Social proof + empathy | Only using authority, skipping empathy |
| Plan | How it works | Listing features instead of steps |
| CTA | All CTAs | Weak verbs ("Submit", "Learn more") |
| Success | Proof + success section | Vague outcomes ("improve your results") |
| Failure | Final CTA area | Skipping it entirely (leaving motivation on the table) |

## Proof audit before saving

- Every statistic, customer name, logo and quote traces to a user-supplied asset or `knowledge/`
- No proof slot was filled to complete the template
- Every unsourced slot reads `[PROOF NEEDED: ...]`

## Stop conditions

Do not draft the page when any of these holds. Name the blocker and what you need.

1. **Two conversion actions requested.** Stop and force a choice. A page with a demo button and a
   free-trial button converts worse than either alone, because the visitor now has a decision to
   make before the decision you wanted.
2. **No proof assets at all**, meaning no logo, no metric, no quote, nothing. Draft the page, but
   fill every proof slot with `[PROOF NEEDED: ...]` and tell the user the page should not go live
   until at least one is real. Never invent one to complete the layout.
3. **Pricing requested with no confirmed prices.** Write `[NEEDS INPUT: price per plan]`. Do not
   infer a price from a competitor, from the market, or from an earlier draft.
4. **Regulated claim** (medical, financial, legal, employment, safety). Draft it, mark it
   `[LEGAL REVIEW]`, and say the page must not publish unreviewed.
5. **The user cannot name what the customer wants in one sentence.** That is BrandScript element
   1 and it cannot be inferred. Ask, and do not start until you have it.

## Warning signs in your own draft

Ranked worst first. The top three are ship-blockers.

1. A testimonial, customer name, logo or metric that the user did not supply. Blocker.
2. A price that nobody confirmed. Blocker.
3. A regulated claim with no `[LEGAL REVIEW]` marker. Blocker.
4. The H1 works as a description of the company rather than of the customer's outcome. The brand
   has become the hero, rewrite the hero section.
5. The plan section lists features with step numbers in front of them. Steps reduce anxiety,
   features do not.
6. More than one direct CTA verb across the page.
7. Failure framing appearing more than once, or reading as a threat rather than a cost. On a lead
   magnet page, any failure framing at all.
8. Success outcomes with no unit or object ("better results", "more growth").

## Related skills

- `/page-cro` when the page already exists and the question is why it does not convert
- `/copy-review` for grading and tightening an existing page rather than writing a new one
- `/messaging-framework` when the one-liner needs to hold across every asset, not just this page
- `/positioning-doc` when the BrandScript keeps stalling because the position itself is unclear
- `/ad-campaign-writer` for the ads driving traffic here, so the ad promise matches the H1
- `/email-nurture` for the sequence that fires after the form submit
- `/case-study-writer` when the proof section needs a real customer story built first
- `/ab-copy-writer` when the hero has two credible versions and the choice should be tested
- `/brand-context` first, whenever `knowledge/brand/voice.md` does not exist yet

## What this skill cannot know

These are real limitations of this skill. It cannot resolve them from `knowledge/`, so ask the
user or emit `[NEEDS INPUT: <what>]`.

1. **Whether a named customer has consented to appear on a public page.** A logo file in the
   knowledge base is not consent for this page, in this market, at this time.
2. **Whether a quoted metric is still current.** Case study numbers age silently. Ask when the
   result was measured, and put the period in the copy if the user has it.
3. **Whether a claim needs legal or regulatory review in your market.** Rules differ by
   jurisdiction and by industry. Flag it, do not decide it.
4. **Whether the page will actually render as designed.** Fold position, image behaviour and
   mobile stacking are layout decisions this skill does not control, so "above the fold" here
   means "in the hero block", and someone has to confirm it on the built page.

