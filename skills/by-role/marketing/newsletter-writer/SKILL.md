---
name: newsletter-writer
description: Write recurring newsletter issues with a consistent format and POV using the Curiosity Gap (George Loewenstein) and David Perell's Online Writing framework. Different from one-off emails (use /content-writer or /email-nurture). Use when the user asks for a newsletter, weekly/monthly newsletter, "write this week's issue", recurring email, Substack issue, internal newsletter, or any periodic publication with subscribers. Reads brand voice and content library from knowledge/.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/markets/positioning.md
  - knowledge/content-library/
  - knowledge/learnings.md
writes:
  - output/newsletter/
---

# newsletter-writer

Writes recurring newsletter issues. Optimizes for consistent format, distinctive POV, and subscriber retention. Uses the Curiosity Gap (George Loewenstein) to engineer subject lines and Perell's Online Writing framework to discipline every issue to one shiny idea.

## Frameworks

### Curiosity Gap - George Loewenstein

Curiosity is triggered when there is a gap between what we know and what we want to know. For a gap to work, it must be:
- **Specific enough** to feel real (not vague)
- **Small enough** to feel closeable (not overwhelming)
- **Valuable enough** to be worth closing (the payoff must be implied)

Loewenstein's key finding: curiosity peaks when you know JUST ENOUGH to know what you're missing.

Why "5 tips for better writing" fails: you don't know what you're missing.
Why "The one email mistake that costs 40% of your opens" works: you know exactly what gap exists.

**Subject line formula:** `[Specific thing the reader doesn't know] + [implied payoff if they close the gap]`

Examples:
- "Why your best email went to spam" - specific gap, implied cost
- "The metric 80% of SaaS CMOs ignore" - you don't know which one, but you know it matters
- "We tried X for 90 days. Here's what we got wrong" - gap is the mistake, payoff is learning from it

### David Perell's Online Writing Framework

1. **The Shiny Dime**: the smallest publishable unit. One specific idea, one angle. Not everything you know about a topic. If you can name more than one core idea, split the issue.
2. **Find Your Unique Angle**: personal experience + specific knowledge + distinct perspective. What can only this author or company say about this?
3. **Show Your Work**: readers trust writers who share process, mistakes, and reasoning - not just conclusions.
4. **Compress Insight**: take complex ideas and make them simple and memorable. One sentence the reader can repeat to a colleague.
5. **Specific Beats General**: "the CEO of a 200-person fintech company" beats "business leaders."

## When to use

- "Write this week's newsletter"
- "Draft the next Substack issue"
- "Build the customer newsletter"
- "Write an internal newsletter"
- "Create a recurring industry roundup"

## Newsletter types this skill handles

| Type | Audience | Cadence | Format |
|---|---|---|---|
| **Industry POV** (Substack-style) | External, subscribers | Weekly or biweekly | Long-form essay + curated links |
| **Product newsletter** | Customers | Monthly | What's new + how to use it + customer story |
| **Curated roundup** | External subscribers | Weekly | Annotated links, short |
| **Internal newsletter** | Employees | Weekly or monthly | Wins, updates, asks |
| **Sales/partner newsletter** | Channel partners or sales reps | Monthly | Enablement, wins, comp updates |
| **Investor update** | Investors and board | Monthly or quarterly | Metrics, narrative, asks |

## Inputs needed

- **Newsletter type** (from table)
- **Issue topic or theme** (or "you pick from recent material")
- **Source material**: drafts, links, data points, internal updates
- **Cadence and format consistency**: if prior issues exist, match them

## Process

1. **Load context.** Read brand voice and persona. Look in `knowledge/content-library/newsletter/` (if exists) for prior issues to match format and voice.

2. **Run the Shiny Dime test.** Before writing a single word:

   Answer: "What is the ONE thing this issue teaches, argues, or reveals?"

   If the answer contains "and" or a second complete idea, stop. Split into two issues or cut to the stronger one. The Shiny Dime test is mandatory - an issue that tries to say two things says nothing.

3. **Find the unique angle.** Answer:
   - What is the author's specific experience with this topic?
   - What does the author know about this that a generic writer doesn't?
   - What would the author say about this that contradicts conventional wisdom?

   If the answer is "nothing specific," the issue is generic. Push for a tighter angle or source a specific story, data point, or observation the author actually has.

4. **Engineer the subject line using the Curiosity Gap formula.**

   Draft 3 subject line options. For each, evaluate:
   - Does it name a SPECIFIC gap (not just a topic)?
   - Does the gap feel closeable (small enough to not feel like a lecture)?
   - Is the implied payoff valuable enough to act on?

   Pick the one with the strongest gap. Reject any subject line that merely describes the topic.

   Subject line rubric:
   | Test | Pass | Fail |
   |---|---|---|
   | Specific gap | "The metric SaaS CMOs ignore" | "Marketing tips" |
   | Closeable | One issue addresses it fully | "Everything about content" |
   | Valuable payoff | Revenue, time, clarity implied | Vague improvement |

5. **Establish the newsletter's spine** (do this once on the first issue, then reuse):

   Lock these on issue 1:
   - **Section 1**: the hook (a personal opener, observation, or one-line setup)
   - **Section 2**: the main piece (the substance, varies by issue)
   - **Section 3**: a consistent recurring segment (e.g., "What I'm watching", "3 things I read", "Customer of the week")
   - **Section 4**: CTA or close (consistent sign-off)

   If prior issues exist, lift the spine from them. Do not invent a new format every week. Subscribers want consistency.

6. **Write the issue.**

### Industry POV newsletter (Substack-style)

```
Subject: <Curiosity Gap formula. 30-50 chars. Specific gap.>
Preview text: <Complementary, 30-90 chars. Don't repeat subject.>

# <Issue title>

<Hook: 80-150 words. Personal observation, news reaction, or contrarian claim. Show your work - share how you arrived at this. Earns the read.>

## <Main piece title>
<800-1500 words. One core argument - the Shiny Dime. Specific examples. POV is required.
Include at least one "show your work" moment: a mistake, a process detail, or behind-the-scenes reasoning.
Use specific language: "a 45-person B2B SaaS team" not "small companies".>

## <Recurring segment>
<200-400 words. Three items, links, or quick takes. Consistent across issues.>

## What I'm reading / watching / building
<3-5 annotated links. Each: title, URL, 1-line take. Why does it matter to THIS reader?>

---

<Sign-off line, consistent across issues>
<Author name>

P.S. <Optional. Often a soft ask: "Reply with your take" or "Forward to a friend who'd like this">
```

### Product newsletter

```
Subject: <Curiosity gap from a customer outcome. Not a feature name.>
Preview text: <Complementary>

## What's new
<3-5 features released. Each: name, what it does, who it's for, link to docs/changelog>

## How to use it
<One feature deep-dive. Step-by-step or 3-tip format. 200-300 words. Show the work - include a real use case.>

## Customer of the month
<One customer story, 100-150 words. Outcome + quote + link to full case study. Specific: company size, use case, result number.>

## What's coming
<2-3 things on the roadmap. Only commit to what will actually ship.>

## CTA
<One call to action: book demo, attend webinar, try new feature>
```

### Curated roundup

```
Subject: <Curiosity gap tease on the most surprising item in the issue>
Preview text: <Tease the second-most interesting one>

## <Issue title>
<Hook: 50-100 words. Why does this week's collection matter now?>

## <Section header>
- **<Title 1>**: <2-line annotation. Why does this matter? What's the gap it fills?> [Link]
- **<Title 2>**: <annotation> [Link]
- ... 5-10 items total

## <Optional second section>
<Same format, different category>

## Closing
<Sign-off + ask for forwards/replies>
```

### Internal newsletter

```
Subject: <Theme of the week>

## This week's wins
- <3-5 wins, with credit>

## What's shipping
- <Roadmap items moving this week>

## What we learned
<1-2 short retros from the team>

## Asks
- <Where the team needs help, hires, intros>

## Heads up
<Process changes, all-hands logistics, etc.>
```

7. **Voice rules**:
   - Match `knowledge/brand/voice.md`
   - First-person where appropriate (POV newsletters always)
   - Conversational, like writing to one engaged subscriber
   - Specific names, numbers, examples
   - No "Hope this finds you well"
   - Match the rhythm of prior issues if they exist (sentence length, paragraph density)

8. **Self-check** (run before finalizing):

   Curiosity Gap checks:
   - Does the subject line open a specific gap or just describe the topic?
   - Is the payoff implied clearly enough that the reader knows it's worth their time?
   - Would a reader reading the subject line know EXACTLY what they're missing?

   Perell framework checks:
   - What is the Shiny Dime? Can I say it in one sentence?
   - Is there a unique angle only this author/company can own?
   - Is there at least one "show your work" moment in the main piece?
   - Is every claim specific? Replace any vague language with a specific example.

   Format checks:
   - Issue follows the established spine (sections, length, voice)
   - Specific examples, not abstractions
   - At least one place where the reader thinks "huh, didn't know that"
   - Length matches the type's norm (POV: 1500-2500w, product: 600-900w, roundup: 400-700w, internal: 300-500w)
   - One CTA

9. **Save** to `output/newsletter/<DD-MM-YYYY>-<issue-slug>.md` with frontmatter:
   ```yaml
   ---
   format: newsletter
   type: <type>
   issue-number: <N>
   issue-title: <title>
   theme: <theme>
   shiny-dime: <one sentence>
   curiosity-gap-subject: <yes/no and notes>
   words: <count>
   created: DD-MM-YYYY
   ---
   ```

10. **Offer derivative content**:
    - LinkedIn post pulling the strongest insight (use `/linkedin-post`)
    - Substack note teasing the issue
    - 3 quote graphics

## Rules

- Consistency beats novelty. Subscribers stay because they know what they're getting. Don't reinvent the format every week.
- Every issue needs a POV in the main piece. A roundup of links without commentary is replaceable.
- The Shiny Dime test is non-negotiable. One issue, one idea. If it tries to say two things, it says nothing.
- Subject lines that describe the topic are not subject lines. They are table of contents entries.
- Track open rate and CTR per issue if data is available. Update `knowledge/learnings.md` with what works.
- Never publish without rereading. Fresh-eyes pass catches 80% of voice misses.
- Personal > corporate. Even brand newsletters perform better with a name and face attached.
