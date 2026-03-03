---
name: substack-post
description: Write long-form Substack articles and newsletter posts. Use when user says "write a post", "write an article", "long-form piece", "newsletter issue", "draft about", "write about", "blog post", or wants a full article with narrative depth. Also trigger when user has a topic they want to turn into a complete written piece - even if they don't explicitly say Substack. For short-form notes (3-5 sentences), use substack-notes instead.
---

# Substack Post Generator

## Overview

This skill generates long-form Substack articles - full newsletter posts with narrative arc, sustained depth, and real value.

**Critical distinction:** A Substack post is not a long note. It is a complete piece with a beginning, middle, and end. It earns the reader's time through storytelling, specificity, and insight they couldn't get from a 5-sentence note. It should feel like something worth saving.

## How It Works

### Step 1: Identify Article Type

**Type 1: Experience Breakdown** - A real thing you did, with what you learned
Examples: "I ran 16 agents on one task - here's what happened", "I tracked every session for 30 days"

**Type 2: Person/Idea Deep Dive** - Unpacking someone's framework or philosophy
Examples: "[Person] built [thing] on a hunch", "The 7 rules from the person who runs 259 PRs/month"

**Type 3: How-To with Real Stakes** - A practical method grounded in personal use
Examples: "How I cut content time from 20 hours to 6", "Running multiple sessions in parallel"

**Type 4: Contrarian Take** - A belief you hold that most people don't, with evidence
Examples: "AI agents don't need to be autonomous to be useful", "The bottleneck isn't the model"

**Type 5: Build-in-Public Update** - Progress, numbers, honest reflection
Examples: "Month 3 of [your project]: what's working, what isn't"

Psychology: Knowing the type up front prevents structural drift. Each type has a natural arc. Pick the one that matches the content.

### Step 2: Structure the Article

Every article follows this spine:

```
[Opening scene or personal admission - 1-3 paragraphs]
[Setup: what this article is about and why it matters - 1 paragraph]

## Section 1 heading
[First major point, story, or argument]

## Section 2 heading
[Second major point - builds on or contrasts with Section 1]

## Section 3 heading (optional)
[Third major point or deepest insight]

[Synthesis paragraph - connect the threads]
[Closing - reflection + what the reader can do]
```

**Section count:** 2-4 sections. More than 4 and the piece loses focus.

**TOC:** Include for pieces over ~1500 words. Use the `substack-toc` skill after writing.

### Step 3: Write the Opening

The opening is the hardest part. It must earn the reader past the first screen.

**Opening type options:**

**Scene drop** - Drop into a specific moment
`"Last Tuesday, [person] closed 17 pull requests before lunch. Not unusual for them. This week they'll close 60 more."`

**Personal admission** - The default. Most honest, most effective.
`"I had no idea how I was actually using [tool] until I ran the analytics."`

**Surprising fact or number** - Ground the reader in something concrete before explaining
`"The experiment used 16 agents and zero hand-holding. It worked."`

**Problem framing** - Name the pain before offering anything
`"Most people use AI tools the way I used to: one tab, one task, one long conversation that gets worse as it gets longer."`

Rules for the opening:
- First sentence stands alone. Short, specific, arresting.
- Paint the scenario in the first 3 paragraphs before introducing the solution or framework
- No preamble. Don't explain what the article will cover. Just start.
- "I" before "you" - lead with your experience

### Step 4: Write Each Section

Each section should:
- Have a clear heading that states the insight, not just the topic
  - Weak: `## Using multiple sessions`
  - Strong: `## Method 1: Terminal panes (the fastest start)`
- Open with the key point or a scene
- Use concrete examples - real commands, real numbers, real outcomes
- Include one sustained metaphor per article (not per section - carry it through)
- End with either a transition to the next section or a mini-conclusion

**Paragraph rules:**
- Single-line for emphasis and punchlines
- 2-3 sentences for developing an idea
- No paragraph longer than 4 sentences
- White space between every paragraph
- Short sentences carry weight. Long sentences explain.

### Step 5: Write the Closing

The closing does two things: synthesizes the whole piece and gives the reader something to do.

**Synthesis first:** Bring back the article's central insight in new language. Not a summary - a restatement that feels earned after the journey.

**Then one of:**
- **Actionable close** - Something specific the reader can do today
- **Metaphor callback** - Return to the opening image, now resolved
- **Open question** - A question that extends the idea past the article's scope
- **Honest reflection** - What you still don't know, or what surprised you

Never close with: a list of takeaways, a summary of what was covered, or a generic CTA unrelated to the content.

### Step 6: Format for Substack

**Length:**
- 800-1200 words: tight, punchy, high re-read value
- 1200-2000 words: standard deep dive
- 2000+ words: only if the content genuinely demands it

**Formatting:**
- H2 (`##`) for main sections only
- Bold for key terms and emphasis - not decoration
- Code blocks for commands, code, or quoted text worth highlighting
- No H3 or H4 unless the piece is reference-style documentation
- Numbered lists for sequences; bullet lists for options
- No emojis

**Images/pulls:** Leave `[IMAGE: description]` placeholders where visuals would strengthen the piece.

## Anti-Patterns

**1. Summary opening**
Bad: "In this article, I'm going to cover three methods for running multiple agents in parallel."
Good: "Last Tuesday, [person] closed 17 pull requests before lunch. Not unusual for them."

**2. Vague section headings**
Bad: `## Why this matters`
Good: `## The bottleneck isn't the model - it's the queue`

**3. Dropped metaphor**
Bad: Introduce "junk drawer" in paragraph 1, never mention it again
Good: Introduce it, return to it at each key moment, resolve it in the close

**4. Padding**
Bad: Restating the same point with different words to hit a word count
Good: If a section is empty, cut it - two strong sections beat three weak ones

**5. Generic close**
Bad: "I hope you found this useful. Let me know what you think in the comments!"
Good: "Pick one method. Run it this week. Come back and tell me if the math changes."

**6. Teaching before showing**
Bad: "There are three key benefits to parallel sessions: first..."
Good: "[Person] has 4 terminal panes open at any given time. Each one is mid-task."

## Voice Reminders

- Personal admission before diagnosis. "I did X" before "you should Y"
- One metaphor, sustained. Not one per section - one per article.
- Problem before fix. Show the mess before you clean it up.
- "I" voice throughout. Never "we" unless citing a real team.
- Numbers over adjectives. "15 hours" not "significantly less time."
- Honest tension. "It's working, but here's what I still don't know."

## Quality Checklist

- [ ] Opens with scene, admission, or surprising fact - no preamble
- [ ] First sentence stands alone and is specific
- [ ] Section headings state insight, not topic
- [ ] One metaphor introduced and sustained through the piece
- [ ] Problem/scenario appears before solution in each section
- [ ] Closing synthesizes + gives reader something actionable
- [ ] No summary opening, no summary closing
- [ ] Numbers and specifics throughout - nothing vague
- [ ] Paragraphs are short with white space between them
- [ ] Would you read this start to finish?
