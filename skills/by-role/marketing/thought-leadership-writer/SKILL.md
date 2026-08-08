---
name: thought-leadership-writer
description: Write long-form thought leadership articles, opinion pieces, industry POV essays, and CEO/founder bylines using the Made to Stick SUCCESs framework (Chip and Dan Heath). Use when the user asks for a long-form article, executive byline, opinion piece, industry POV, manifesto, "explain our point of view on X", or wants to publish an authority-building piece (1200-2500 words). Reads brand voice and positioning from knowledge/. For a short-form post, see linkedin-post. For the newsletter, see newsletter-writer. For improving an existing draft, see copy-review.
metadata:
  grounded_in:
    - "Made to Stick - Heath & Heath"
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

### The villain the framework exists to defeat: the curse of knowledge

*Made to Stick* names one root cause for unstuck ideas. Once you know something, you cannot
imagine not knowing it, so you write the summary of your insight rather than the thing that
produced it. Every element of SUCCESs is a countermeasure to that one failure.

Practical test before you draft: hand the thesis sentence to someone outside the company. If they
need a follow-up question to understand what it claims, the curse is active and the piece will
read as abstract to everyone but the author.

### Heath's credibility toolkit, when you have no statistic

Credible is the element most often skipped in B2B writing, usually because the author has no
study to cite. The Heaths list several sources of credibility that are not statistics. Pick one
deliberately rather than defaulting to a number you would have to invent.

| Technique | What it is | Use it when |
|---|---|---|
| Anti-authority | A source credible precisely because they have no incentive to say it: a customer, a skeptic, a competitor conceding a point | The brand claiming it would read as self-serving |
| Testable credential | An invitation for the reader to check for themselves: "look at your own funnel between step 6 and step 11" | The reader has the data on hand |
| Vivid detail | Specific, checkable texture that signals first-hand knowledge | The claim rests on the author having actually been there |
| Human-scale statistic | A number rescaled to something a person can picture | You have a real figure but it is too large to feel |
| Sinatra test | One example so strong it settles the question by itself | You have one undeniable case rather than many weak ones |

**Rule: a human-scale statistic still needs a real underlying number.** Rescaling is a
presentation move, not a licence to estimate one. If there is no number, use anti-authority or a
testable credential instead.

### The three plots, for choosing the story rather than groping for one

| Plot | Shape | Best for a piece that argues |
|---|---|---|
| Challenge | Someone faces an obstacle bigger than them and overcomes it | This is hard but doable, here is the proof |
| Connection | Someone bridges a gap between people or groups | The problem is really a misalignment between two functions |
| Creativity | Someone solves a problem in a way nobody expected | The conventional method is not the only method |

Pick the plot from the argument, not from whichever anecdote is nearest. A Challenge plot
attached to a Creativity argument makes the piece feel effortful rather than surprising.

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
Read `knowledge/brand/voice.md`, `knowledge/markets/positioning.md`, `knowledge/markets/competitors.md`. Stop if voice is missing: "Run `/brand-context` first."

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

**Score the thesis before proceeding.** One point each:

| Point | Condition |
|---|---|
| 1 | A competent person in this industry could disagree with it in one sentence |
| 2 | It names a specific mechanism, metric, step or population, not a trend |
| 3 | The author has first-hand material that supports it, not just an opinion |
| 4 | It moves `knowledge/markets/positioning.md` forward rather than sideways |

**Threshold: write at 3 or 4. At 2, propose 2-3 sharper versions and rewrite. At 0 or 1, stop and
say the piece should not be written yet**, because a thesis nobody can disagree with produces an
article nobody can remember, and no amount of SUCCESs work at later steps rescues it.

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
  Credibility technique chosen (anti-authority | testable credential | vivid detail |
    human-scale statistic | Sinatra test):
  Primary credibility source (stat, study, customer, or self-experience) and where it came from:
  Anti-authority candidate (a peer, customer, or skeptic who validates the point):
  What the reader might object to, and the counter:

E - EMOTIONAL (why they should care)
  Self-interest angle: how does this affect the reader directly?
  Identity angle: what does believing this say about who they are?
  The "curse of knowledge" check: are we assuming context the reader doesn't have?

S - STORIES (the narrative)
  Plot type chosen (challenge | connection | creativity), and why it matches the argument:
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
                [ ] Quote the sentence that contradicts what section 2 said everyone believes.
                    If no sentence does, the piece agrees with the conventional wisdom it set up

C - Concrete:   [ ] At least 3 specific examples, each traceable to `knowledge/` or user input. Any example you could not source is marked `[SOURCE NEEDED]` in the draft, never written as fact
                [ ] No abstract claim left without a concrete anchor

C - Credible:   [ ] Primary credibility source present (stat, case study, or experience)
                [ ] At least 1 "anti-authority" (peer/customer validates, not just the brand)

E - Emotional:  [ ] Piece taps self-interest ("this affects you") or identity ("this is about who you are")
                [ ] No "curse of knowledge" - doesn't assume context reader doesn't have

S - Stories:    [ ] At least 1 narrative (specific scene with a beginning, middle, and turn)
                [ ] Close has a line worth quoting or sharing

Sourcing:      [ ] Every statistic, quote, company name and result is listed with its source.
                    Anything without one is `[SOURCE NEEDED: ...]` or `[NEEDS INPUT: ...]`
               [ ] Every external link was fetched in this session and resolved
               [ ] The credibility technique named in the pre-write is the one actually used

Voice checks:
                [ ] Thesis appears before word 300
                [ ] Voice matches knowledge/brand/voice.md
                [ ] Zero em dashes and zero en dashes
                [ ] Zero occurrences of: "In today's rapidly evolving landscape", "It's no secret
                    that", "At the end of the day", leverage, unlock, robust, seamless
                [ ] Word count within 10% of the target
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

## Stop conditions

Do not draft, or do not hand over, and say which condition fired.

1. **Thesis scores 0 or 1.** Stop. Say the piece has no defensible position yet and ask for the
   specific experience or result that would give it one.
2. **No first-hand material at all**, meaning no story, no client pattern, no observation the
   author personally has. The piece will be a summary of other people's ideas. Ask before writing.
3. **The credibility slot is empty and the only fix is a statistic you do not have.** Never invent
   the statistic. Switch to anti-authority or a testable credential, or write
   `[NEEDS INPUT: the real figure]`.
4. **The piece is a named executive byline and the user has not confirmed the executive holds this
   view.** Mark it `[APPROVAL NEEDED: <name>]` and say it must not publish unconfirmed.
5. **The thesis contradicts `knowledge/markets/positioning.md`.** Flag the conflict and ask which
   one is meant to move. Publishing against your own position confuses the market twice.
6. **The piece names a competitor and makes a factual claim about them** that is not in
   `knowledge/markets/competitors.md`. Route to the user before it goes anywhere.

## Warning signs in your own draft

Ranked worst first. The first four block handover.

1. A statistic, quote or named example with no source. Blocker.
2. A quote attributed to a real person who did not say it, in any form, including a paraphrase
   presented as their words. Blocker, and the most damaging thing this skill can produce.
3. A factual claim about a named competitor with no source. Blocker.
4. An executive byline with no confirmation. Blocker.
5. Section 3 restates section 2 in stronger language rather than contradicting it. The piece has
   no unexpected element, and the reader will finish it agreeing with what they already thought.
6. The story is a parable or a hypothetical rather than a scene that happened. Hypotheticals do
   not carry credibility, and readers can tell.
7. The close summarises rather than sharpening. If there is no line worth screenshotting, the
   piece will not be shared regardless of how good the argument is.
8. The new model has no name. Unnamed ideas do not travel.

## Related skills

- `/linkedin-post` for the short version, and for the distribution post once this publishes
- `/newsletter-writer` when the piece is an issue of a recurring publication with a fixed spine
- `/content-writer` when the piece is shorter than 1200 words or is really a marketing asset
- `/copy-review` to grade and tighten a draft the user already wrote
- `/positioning-doc` when the thesis keeps conflicting with the company's stated position
- `/messaging-framework` when the new model needs to become language the whole company uses
- `/competitor-analyst` before any piece that makes factual claims about named competitors
- `/pr-pitch-writer` when the goal is placement in a trade publication rather than owned publishing
- `/content-repurposer` after publishing, to turn the piece into posts, a talk and a thread
- `/brand-context` first, whenever `knowledge/brand/voice.md` does not exist yet

## What this skill cannot know

These are real limitations of this skill, and none can be settled from `knowledge/`. Ask the
user, or emit `[NEEDS INPUT: <what>]`.

1. **Whether the named author actually believes this.** A byline is a public position taken by a
   real person, and their view cannot be inferred from a brand voice file or a positioning doc.
2. **Whether a customer or peer agreed to be quoted or identified.** An anti-authority quote is
   the most persuasive element in the piece and the one most likely to have been given
   informally, in a call, without permission to publish.
3. **Whether a statistic from `knowledge/` is current, and whether its original source still says
   what the note says it said.** Second-hand statistics drift, and this piece will be the third
   hand.
4. **Whether the publication target will accept the piece as written.** Trade publications have
   house rules on promotion, sourcing and competitor mentions that are not visible from here.
5. **Whether the position creates commercial or legal exposure** with a partner, an investor or a
   regulator. Flag anything pointed, do not adjudicate it.
