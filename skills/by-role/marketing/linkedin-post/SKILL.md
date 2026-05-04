---
name: linkedin-post
description: Write a high-performing LinkedIn post in the user's brand voice using Hook-Story-Offer (Alex Hormozi, $100M Offers) and the Curiosity Gap hook method (George Loewenstein). Every post starts by selecting a named hook formula - specific number + surprising result, contrarian statement, personal confession, direct challenge, or before/after. Use when the user asks for a LinkedIn post, LinkedIn update, LinkedIn content, "post for LinkedIn", thought-leadership post, founder post, or short professional social content. Reads brand voice and ICP from knowledge/ so output sounds like the company, not generic AI.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/markets/positioning.md
  - knowledge/content-library/
writes:
  - output/linkedin-post/
---

# linkedin-post

Writes LinkedIn posts that get read, saved, and reshared. Applies the Hook-Story-Offer structure (Alex Hormozi) with the Curiosity Gap hook method (George Loewenstein). Every post creates a specific information gap in the hook, closes it in the story, and ends with one clear action.

## Framework: Hook-Story-Offer + Curiosity Gap

### Hook-Story-Offer (Alex Hormozi)
**HOOK**: stop the scroll. Create a pattern interrupt. The hook must create enough curiosity or pain recognition that the reader clicks "see more." The hook fails if someone can scroll past without wondering what comes next.

**STORY**: make the hook real. Provide context, the journey, the insight. This is where trust is built. Show, don't tell. Specific details, numbers, named situations.

**OFFER**: what should the reader DO? The offer can be: click a link, follow, save the post, reply with a word, or believe something new. One action only. Low friction. "What do you think?" is not an offer - it is an afterthought.

Note: "offer" in LinkedIn context is NOT always a sales pitch. The offer is whatever action you want the reader to take - including "bookmark this framework" or "reconsider this belief."

### Curiosity Gap Hook Method (George Loewenstein)
Best LinkedIn hooks create a specific information gap between what the reader knows and what the post promises to reveal. The gap must be:
- Specific (not vague) - "one change" beats "some changes"
- Closeable only by reading on - the answer cannot be guessed
- Relevant to the reader's world - they must care about closing the gap

Hook quality test: does the hook create a specific gap the reader needs to close? If someone can guess the answer from the hook alone, it is not a gap - it is a headline.

### The 5 Hook Formulas
Pick one before writing. Name it in the process.

1. **Specific number + surprising result**: "I made one change to our onboarding flow. Trial-to-paid went from 19% to 29%." Gap: what was the change?
2. **Contrarian statement + no explanation yet**: "Cold outreach is dead. Here's what replaced it." Gap: what replaced it?
3. **Personal confession + open loop**: "I was wrong about [belief]. Here's what changed my mind." Gap: what changed their mind?
4. **Direct challenge**: "Most [audience] make this mistake. Are you?" Gap: what is the mistake?
5. **Before/after without the how**: "6 months ago: 8 demo requests/month. Today: 47. Here's what changed." Gap: what changed?

## When to use

- "Write a LinkedIn post about X"
- "Draft a founder post on Y"
- "Give me 3 LinkedIn variants for our launch"
- "Turn this article into a LinkedIn post"

## Inputs needed

- **Topic, angle, or source material** (required)
- **Goal**: drive traffic, build authority, generate leads, recruit, announce (default: build authority)
- **Author voice**: founder, CMO, generic company (default: company)
- **CTA**: comment, click link, DM, none (optional)

## Process

1. **Load context.** Read `knowledge/brand/voice.md`. If missing, stop and tell the user to run `/onboard --brand`.

2. **Read 3-5 high-performing past posts** from `knowledge/content-library/` if they exist. Mirror cadence and rhythm, not topic.

3. **Select a hook formula.** Pick one of the 5 formulas. Name it explicitly before writing. Do not skip this step.
   ```
   Hook formula selected: [formula name]
   Gap this hook creates: [one sentence - what does the reader not know yet?]
   ```

4. **Write the hook.** First line decides everything. Rules:
   - Under 12 words
   - Specific, not generic
   - Creates a gap that can only be closed by reading on
   - No "Excited to share", no "I'm thrilled", no questions that can be answered yes/no without thinking
   - Apply the curiosity gap quality check: is the gap specific? Is it closeable? Will the reader care?

5. **Write the story.** 3-7 short paragraphs using Hook-Story-Offer structure:
   - Show, don't tell. Specific details. Numbers. Named situations.
   - One idea per paragraph. Line breaks are generous.
   - The story closes the gap created by the hook. If reading the story does not satisfy the hook's promise, rewrite one of them.
   - Bullets only if the structure is a list. Avoid emojis unless `knowledge/brand/voice.md` says they are part of the voice.

6. **Write the offer.** One line. One action. Low friction.
   - State what specific action you want: save, comment, follow, click, reply with a word
   - "What do you think?" alone is not an offer - add a specific action alongside or instead
   - Match friction to goal: if the goal is lead gen, a link is fine. If the goal is authority, "save this" is better.

7. **Self-check** before showing:
   - Named hook formula used and gap is clearly created in the hook
   - Hook under 12 words
   - Story closes the gap from the hook
   - Offer is one specific, low-friction action
   - No em dashes
   - No corporate phrases ("leverage", "unlock", "game-changer", "in today's fast-paced world")
   - 80-220 words total (LinkedIn cuts off around 210 words on mobile)
   - Voice matches `knowledge/brand/voice.md`
   - One clear takeaway

8. **Save** to `output/linkedin-post/<DD-MM-YYYY>-<slug>.md` with frontmatter:
   ```yaml
   ---
   format: linkedin-post
   topic: <topic>
   author: <founder|cmo|company>
   goal: <goal>
   hook-formula: <formula name>
   words: <count>
   created: DD-MM-YYYY
   ---
   ```

9. **Offer 2 hook variants** unless the user only wanted one. The hook is the highest-leverage edit point - a different hook formula on the same content can double or halve performance.

## Format guardrails

- 80-220 words total
- First line = hook (the only line guaranteed to be seen before "see more")
- Lines 2-3 must earn the click to "see more"
- No more than 2 hashtags, end of post, lowercase, niche-specific (skip generic ones like #marketing)
- Tag people only if the user explicitly named them

## Hook formula reference (quick pick)

| Situation | Best formula |
|---|---|
| You have a specific metric result | Formula 1: Specific number + surprising result |
| You want to challenge a common belief | Formula 2: Contrarian statement |
| You changed your own mind about something | Formula 3: Personal confession |
| You see a widespread mistake | Formula 4: Direct challenge |
| You have a transformation story | Formula 5: Before/after without the how |

## Rules

- Never skip the hook formula selection. Naming the formula is a forcing function - it prevents generic hooks.
- Never invent stats, customer quotes, or product capabilities. Pull from `knowledge/services/` and `knowledge/content-library/case-studies/` only.
- The offer must be specific. "Let me know your thoughts" is vague. "Comment with the one thing you'd add" is specific.
- If the user wants to share a competitor opinion, flag risk and ask before publishing.
- The gap created in the hook must be closed in the body. If the post does not answer what the hook implied, the reader feels tricked - they will not follow or save.
