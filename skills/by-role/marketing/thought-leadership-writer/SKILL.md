---
name: thought-leadership-writer
description: Write long-form thought leadership articles, opinion pieces, industry POV essays, and CEO/founder bylines using the Made to Stick SUCCESs framework (Chip and Dan Heath). Use when the user asks for a long-form article, executive byline, opinion piece, industry POV, manifesto, "explain our point of view on X", or wants to publish an authority-building piece (1200-2500 words). Reads brand voice and positioning from knowledge/.
reads:
  - knowledge/brand/voice.md
  - knowledge/markets/positioning.md
  - knowledge/markets/competitors.md
  - knowledge/icp/personas.md
  - knowledge/content-library/
writes:
  - output/thought-leadership/
---

# thought-leadership-writer

Writes long-form opinion pieces that establish authority and get shared. Uses the **Made to Stick SUCCESs framework** (Chip & Dan Heath, *Made to Stick*) to ensure every piece is memorable, not just well-written.

**The core insight from Made to Stick:** Ideas fail to stick not because they're wrong, but because they're abstract, predictable, and forgettable. The SUCCESs framework systematically fixes this. A thought leadership piece that checks all 6 conditions will be remembered, quoted, and shared. One that checks none will be read once and forgotten.

## The SUCCESs Framework

Apply all 6 conditions to every piece. Each one is a checklist item, not optional.

| Letter | Condition | The test | How to apply |
|---|---|---|---|
| **S** | Simple | Can you express the core idea in one sentence? | Find the lead - the single most important insight. Strip everything that doesn't serve it. |
| **U** | Unexpected | Does the piece break a pattern the reader expected? | Open by violating an assumption. Say the thing the reader didn't see coming. |
| **C** | Concrete | Are there specific people, places, objects, and numbers? | Replace abstract claims with tangible examples. "Activation rate stuck at 52%" not "low engagement". |
| **C** | Credible | Why should anyone believe this? | Use statistics, named examples, or an "anti-authority" (a customer or peer, not just the brand). |
| **E** | Emotional | Does the reader care? | Tap the "self-interest" trigger (this affects you) or the "identity" trigger (this is about who you are). |
| **S** | Stories | Is there a narrative? | Use a story - even a short one - to make the idea travel. People remember stories, not arguments. |

## When to use

- "Write a thought leadership piece on X"
- "Draft an opinion article about Y"
- "We need a POV piece on the future of Z"
- "Write a CEO byline for <publication>"
- "Write a manifesto"

## Inputs needed

- **Thesis** (required): the one-sentence claim this piece defends. If the user doesn't have one, help them sharpen one before writing.
- **Audience**: industry insiders, prospects, peers, press (default: prospects)
- **Length**: 1200, 1800, or 2500 words (default: 1800)
- **Author voice**: founder, CEO, CMO, or company POV
- **Publication target**: own blog, LinkedIn article, Substack, trade pub

## Process

### Step 1: Load context
Read `knowledge/brand/voice.md`, `knowledge/markets/positioning.md`, `knowledge/markets/competitors.md`. Stop if voice is missing: "Run `/onboard --brand` first."

### Step 2: Sharpen the thesis
A weak thesis kills everything downstream. Before writing, run it through three tests:

**Test 1 - Specificity.** Can it be argued with?
- ✗ "AI will change marketing" (too vague)
- ✗ "Content marketing is important" (too obvious)
- ✓ "Activation rate is a proxy metric. Here's what actually predicts retention."
- ✓ "Most onboarding flows are too long. Cutting steps 6-11 will outperform redesigning steps 1-5."

**Test 2 - Contestability.** Would a reasonable person disagree?
- If everyone would agree, it is not thought leadership. It is a press release.
- The strongest pieces make people uncomfortable before they convince them.

**Test 3 - Alignment.** Does it reinforce `knowledge/markets/positioning.md`?
- Thought leadership should move the brand's position forward, not sideways.
- If the thesis contradicts the company's POV, flag it before writing.

If the thesis fails any test, propose 2-3 sharper versions before proceeding.

### Step 3: Run the SUCCESs pre-write
Complete this before writing:

```
SUCCESs pre-write for: [Working title]

S - SIMPLE (the core)
  One-sentence core idea (not the title - the insight):
  What gets cut if we had to strip 50% of the piece:

U - UNEXPECTED (the pattern break)
  What does the reader expect to hear on this topic?
  What's the unexpected angle or opening move?
  First sentence candidate (the pattern-breaker):

C - CONCRETE (the specifics)
  3 specific examples, numbers, or named cases to use:
    1.
    2.
    3.
  Any abstract claims that need a concrete replacement?

C - CREDIBLE (the proof)
  Primary credibility source (stat, study, customer, or self-experience):
  Anti-authority candidate (a peer, customer, or skeptic who validates the point):
  What the reader might object to, and the counter:

E - EMOTIONAL (why they should care)
  Self-interest angle: how does this affect the reader directly?
  Identity angle: what does believing this say about who they are?
  The "curse of knowledge" check: are we assuming context the reader doesn't have?

S - STORIES (the narrative)
  Opening story candidate (specific scene, not a parable):
  Supporting anecdote (from knowledge/content-library/ or user input):
  The moment of realization (the turn in the narrative):
```

### Step 4: Structure the piece

Use this structure. Each section maps to SUCCESs elements.

```
## 1. Hook (150-200 words) [U + S + stories]
Open with the UNEXPECTED move. Options:
  - A specific scene ("Last Tuesday, a Head of Growth showed me her dashboard...")
  - A counterintuitive stat ("The average B2B trial has 11 onboarding steps. The best ones have 4.")
  - A direct challenge to conventional wisdom ("Most companies are measuring the wrong metric.")

Rule: The thesis should appear by the end of the hook, or at the start of section 2.
Never open with "In today's..." / "As we all know..." / "It's no secret that..."

## 2. What everyone believes (200-300 words) [Credible]
Steelman the conventional wisdom. Be generous. Don't strawman.
  - "The standard advice is X, and it's not wrong. It's just incomplete."
  - Name real examples of the conventional approach being applied

## 3. Why it's wrong (or incomplete) (300-500 words) [Unexpected + Concrete + Credible]
The UNEXPECTED argument. Specific evidence.
  - Name the cracks in the conventional approach
  - Use concrete examples (named companies, specific numbers, real situations)
  - "We've seen this in [X] clients. The pattern is..."
  - The anti-authority: quote a peer, customer, or skeptic - not just the brand

## 4. The new model (400-600 words) [Simple + Concrete + Emotional]
The author's POV. This is where the SIMPLE core lives.
  - Define new terms if needed (give the idea a name it can travel with)
  - Show how the new model works with a CONCRETE example
  - Tap EMOTIONAL: "Here's why this matters for you specifically"
  - Include a framework, visual, or 3-part structure the reader can remember and repeat

## 5. What to do about it (200-400 words) [Concrete + Emotional + Stories]
Practical application. Not abstract implications.
  - 3 specific actions the reader can take
  - At least one they can take today or this week
  - One supporting story from knowledge/content-library/ if available

## 6. Close (100-150 words) [Simple + Unexpected]
The quotable line. One sentence the reader will screenshot.
  - Restate the core insight in its sharpest form
  - Call to something: a belief, an action, a question
  - The ending should feel inevitable in hindsight, not obvious from the start
```

### Step 5: Write
Apply voice from `knowledge/brand/voice.md`. Rules:
- Specific examples, named companies, real numbers throughout
- Cite any statistics with the source (inline link)
- One idea per paragraph - maximum 3 sentences
- Headers in sentence case
- No em dashes
- No: "In today's rapidly evolving landscape", "It's no secret that", "At the end of the day"

### Step 6: SUCCESs self-check (run after writing)

```
S - Simple:    [ ] Core idea expressible in one sentence
               [ ] No paragraphs that don't serve the core idea

U - Unexpected: [ ] Opening breaks a pattern or assumption
                [ ] Reader encounters at least 1 "I didn't expect that" moment

C - Concrete:   [ ] At least 3 specific examples (named company, number, or scene)
                [ ] No abstract claim left without a concrete anchor

C - Credible:   [ ] Primary credibility source present (stat, case study, or experience)
                [ ] At least 1 "anti-authority" (peer/customer validates, not just the brand)

E - Emotional:  [ ] Piece taps self-interest ("this affects you") or identity ("this is about who you are")
                [ ] No "curse of knowledge" - doesn't assume context reader doesn't have

S - Stories:    [ ] At least 1 narrative (specific scene with a beginning, middle, and turn)
                [ ] Close has a line worth quoting or sharing

Voice checks:
                [ ] Thesis appears before word 300
                [ ] Voice matches knowledge/brand/voice.md
                [ ] No em dashes, no filler openers, no buzzwords
```

### Step 7: Save
`output/thought-leadership/<DD-MM-YYYY>-<slug>.md` with frontmatter:
```yaml
---
format: thought-leadership
framework: made-to-stick-success
thesis: <one-sentence claim>
author: <name or role>
target: <publication>
words: <count>
success-score: S/U/C/C/E/S checked
created: DD-MM-YYYY
---
```

### Step 8: Offer derivative assets
- LinkedIn post version (`/linkedin-post`)
- Substack note (3-5 sentences, the sharpest version of the thesis)
- 5-tweet thread
- 3 pull-quote candidates for graphics (the most quotable lines)

## Rules

- Run the SUCCESs pre-write before writing. Pieces written without it will be technically correct and completely forgettable.
- A thought leadership piece must take a position someone reasonable could disagree with. If your draft offends no one, it is not thought leadership.
- Never invent quotes, stats, or examples. Flag "user should add a real source here" rather than fabricating.
- Named executive pieces: "Confirm this reflects what <Name> actually believes before publishing."
- The close must contain 1 quotable line. If you can't find it, rewrite the close.

## SUCCESs quick reference

| Most common failures | Fix |
|---|---|
| Piece is technically accurate but boring | Missing U (unexpected) and S (stories) |
| Piece makes big claims nobody believes | Missing C (credible) |
| Piece is smart but nobody shares it | Missing E (emotional) - reader doesn't see why it matters to them |
| Piece is interesting but hard to remember | Missing S (simple) - no single core idea |
| Piece is full of jargon and abstractions | Missing C (concrete) - no specific examples |
