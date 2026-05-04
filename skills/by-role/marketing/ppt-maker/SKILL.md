---
name: ppt-maker
description: Build branded PowerPoint decks (.pptx) for pitches, internal updates, sales decks, customer QBRs, board updates, conference talks using the Pyramid Principle and SCQA framework (Barbara Minto, The Minto Pyramid Principle). Every deck starts with the answer - conclusion on slide 2, evidence after. Slide titles are conclusions, not topics. Use when the user asks for a deck, presentation, slides, pitch deck, sales deck, board deck, QBR, "make slides for X", or "build a presentation". Uses templates/ for brand assets. Generates structured slide content with speaker notes.
reads:
  - knowledge/brand/voice.md
  - knowledge/brand/visual.md
  - knowledge/markets/positioning.md
  - knowledge/services/
  - templates/
writes:
  - output/ppt/
---

# ppt-maker

Builds .pptx decks using the brand template, with structured slide content and speaker notes. Applies the Pyramid Principle (Barbara Minto) - the top of the pyramid is the one answer, below it are the supporting arguments, below each argument is the evidence. State the conclusion first, then prove it.

## Framework: Pyramid Principle and SCQA

### The Pyramid Principle
Ideas form a pyramid. The deck title is the one overarching recommendation or answer. Below it are 3-5 supporting arguments (the sections). Below each argument is the data and evidence that proves it.

Top-down rule: state the conclusion first, then prove it. Never build to a reveal. Never make the audience wait for the answer.

### SCQA Structure
Complete this before building any slide:

**SITUATION**: what the audience already knows and accepts as true. Sets the context.
**COMPLICATION**: what changed, what went wrong, what tension exists. Creates the "so what?"
**QUESTION**: the question the complication raises in the audience's mind.
**ANSWER**: the deck answers this question. State it on slide 2 or 3 - before any evidence.

The SCQA opening creates immediate relevance. The audience understands WHY they're in this meeting before seeing the first data slide.

### Action Titles (Slide-Level Pyramid Principle)
- Slide title = the conclusion of that slide (not the topic)
- BAD: "Q3 Results"
- GOOD: "Q3 pipeline missed by 22% due to top-of-funnel drop"
- Maximum 3 supporting points per slide. If you need more than 3, you have two slides.
- The audience should be able to read only the slide titles and understand the full argument.

### Pyramid Check
Deck title -> section titles -> slide titles must form a coherent argument.
Test: read only the titles in order. Does the argument hold? If not, the structure is wrong.

## When to use

- "Build a pitch deck for X"
- "Make a sales deck for <product>"
- "Draft slides for the board update"
- "Create a customer QBR deck"
- "Turn this article into a 10-slide presentation"

## Deck types this skill handles

| Type | Slide count | Structure |
|---|---|---|
| Pitch deck (investor) | 10-12 | Sequoia format: problem, solution, market, model, traction, team, ask |
| Sales deck | 8-12 | Hook, problem, agitate, solution, proof, pricing, next step |
| Board deck | 12-20 | KPIs, wins, misses, asks, plan |
| QBR (customer) | 6-10 | Recap, results, learnings, plan, asks |
| Conference talk | 15-30 | Hook, framework, evidence, application, takeaway |
| Internal update | 5-10 | Goal, progress, blockers, next steps |

## Inputs needed

- **Deck type** (from table above) or "custom"
- **Audience and goal**: who is this for, what action should they take after?
- **Source material**: notes, document, article, data points, or "build from scratch"
- **Length**: number of slides (default per type)
- **Brand template**: confirm `templates/<brand>.pptx` exists. If not, ask the user to drop one in.

## Process

1. **Load context.** Read `knowledge/brand/voice.md` (for slide copy) and `knowledge/brand/visual.md` (for color, type, image style references). Read `knowledge/markets/positioning.md` for any positioning slides. Confirm a `.pptx` template exists in `templates/`.

2. **Complete the SCQA pre-work.** Before touching slides:
   ```
   SITUATION: [what the audience already knows]
   COMPLICATION: [what changed or what the tension is]
   QUESTION: [what the complication makes the audience ask]
   ANSWER: [the one-sentence answer the deck delivers]
   ```
   The ANSWER becomes the deck title. The deck is the proof for that answer.

3. **Pyramid check.** Draft the deck structure as a pyramid:
   ```
   DECK TITLE (= the Answer from SCQA)
   ├── Section 1: [supporting argument 1]
   │   ├── Slide: [conclusion that proves argument 1]
   │   └── Slide: [conclusion that proves argument 1]
   ├── Section 2: [supporting argument 2]
   │   └── Slide: [conclusion that proves argument 2]
   └── Section 3: [supporting argument 3]
       └── Slide: [conclusion that proves argument 3]
   ```
   Read the titles top to bottom. Does the argument hold without the body content? If not, restructure.

4. **Outline first.** Show the user the slide-by-slide outline as a numbered list, with action titles:
   ```
   1. Title slide: [deck title = the SCQA Answer]
   2. The answer: [SCQA Answer restated as the key recommendation - slide 2, before evidence]
   3. [Section 1 header: argument 1]
   4. [Slide title = conclusion of slide 4]
   ...
   ```
   Wait for the user to confirm or edit before building the file.

5. **Build the deck.** For each slide, generate:
   - **Slide title** (action title - the conclusion, 5-9 words, sentence case)
   - **Body content** (3 supporting points max OR one big number OR one pull quote OR one diagram description)
   - **Speaker notes** (2-4 sentences, what the presenter says out loud)
   - **Visual recommendation** (the visual type: "screenshot of dashboard", "chart: bar, MRR by month", "icon grid: 4 logos")

6. **Use python-pptx to write the file.** Pseudocode the script if you do not have execution access; otherwise run it. The script should:
   - Open `templates/<brand>.pptx` as the base
   - Add slides using existing layouts (Title, Title+Content, Section Header, etc.)
   - Insert title and body text into the layout placeholders, not free-floating text boxes
   - Add speaker notes via `slide.notes_slide.notes_text_frame`
   - Save to `output/ppt/<DD-MM-YYYY>-<slug>.pptx`

   If the user does not have python-pptx installed, fall back to:
   - Generate `output/ppt/<DD-MM-YYYY>-<slug>.md` with the full slide-by-slide content
   - Tell the user how to install python-pptx and rerun

7. **Slide design rules**:
   - One idea per slide. If you have two, split.
   - 6 words max per bullet
   - 3 bullets max per slide (Pyramid Principle: no more than 3 supporting points)
   - Numbers > words ("$2.4M" beats "significant revenue")
   - Title states the conclusion, not the topic (Pyramid Principle action title rule)

8. **Self-check**:
   - SCQA completed before slides were built
   - Slide 2 states the answer (SCQA-A) before any evidence slides
   - Every slide title is a conclusion, not a topic label
   - Reading only the slide titles tells the full story - test this explicitly
   - Pyramid holds: deck title -> section titles -> slide titles form a coherent argument
   - Title slide includes presenter name, date in DD-MM-YYYY, audience name
   - Every slide has speaker notes
   - Closing slide has one clear CTA or ask
   - Voice matches `knowledge/brand/voice.md`
   - Brand template applied (no default Office theme)

9. **Save** the .pptx and a parallel `.md` outline to `output/ppt/`.

## Building the file

Use python-pptx inline:

```python
from pptx import Presentation
from pathlib import Path

template = Path("templates") / "brand.pptx"
prs = Presentation(str(template))
# Use existing layouts, do not create new ones
title_layout = prs.slide_layouts[0]
content_layout = prs.slide_layouts[1]
# ... add slides
prs.save("output/ppt/DD-MM-YYYY-deck-name.pptx")
```

## Rules

- Never put a slide together without first completing the SCQA and showing the user the outline.
- Never use the default PowerPoint theme. If no template is in `templates/`, stop and ask the user to drop one in.
- Speaker notes are not optional. A deck without notes is half-done.
- Slide titles are conclusions, not topics. If a title does not contain a verb or a clear claim, it is a topic label - rewrite it.
- For pitch decks, confirm the financial numbers (ARR, runway, ask) with the user before building. Do not pull from old `knowledge/kpis.md` without confirming they are current.
- "What does the audience need to DO?" must be answerable from the deck title alone. If it is not, the deck title is wrong.
