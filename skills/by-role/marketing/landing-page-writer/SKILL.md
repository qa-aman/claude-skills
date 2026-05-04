---
name: landing-page-writer
description: Write landing page copy for product pages, campaign pages, lead-gen pages, pricing pages, and feature pages. Use when the user asks for landing page copy, product page, lead magnet page, "write the page for X", pricing page copy, feature page, hero section, or web copy that converts. Uses the StoryBrand SB7 framework (Donald Miller) to structure every page. Reads brand voice, positioning, and ICP from knowledge/.
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
Read `knowledge/brand/voice.md`, the relevant persona, `knowledge/markets/positioning.md`, and the relevant service file. If brand voice is missing, stop and say: "Run `/onboard --brand` first."

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
- [ ] Brand is the GUIDE, not the hero - customer is the hero throughout
- [ ] SB7 BrandScript completed before copy was written
- [ ] H1 is outcome-led (customer's outcome, not brand's achievement)
- [ ] 3-step PLAN reduces anxiety, not describes features
- [ ] SUCCESS state is specific and vivid (all 3 types: functional, emotional, identity)
- [ ] FAILURE acknowledged near final CTA
- [ ] Social proof appears within first scroll
- [ ] One CTA, consistently repeated
- [ ] Voice matches `knowledge/brand/voice.md`
- [ ] No buzzwords

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
- One conversion action. Always. If the user names two, force them to pick one.
- Hero copy must work without the rest of the page.
- Never write pricing without confirming actual prices with the user.
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
