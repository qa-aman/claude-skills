---
name: newsletter-writer
description: Write recurring newsletter issues with a consistent format and POV using the Curiosity Gap (George Loewenstein) and David Perell's Online Writing framework. Different from one-off emails (use /content-writer or /email-nurture). Use when the user asks for a newsletter, weekly/monthly newsletter, "write this week's issue", recurring email, Substack issue, internal newsletter, or any periodic publication with subscribers. Reads brand voice and content library from knowledge/. For a nurture or lifecycle sequence, see email-nurture. For long-form thought leadership, see thought-leadership-writer. For the monthly plan, see social-calendar.
metadata:
  grounded_in:
    - "Curiosity Gap - George Loewenstein"
    - "Online Writing framework - David Perell"
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

**Applying Perell's five to an issue, in order.** Each stage has a decision at the end of it, and
you do not move on until that decision is made.

| Stage | What you produce | The decision | If it fails |
|---|---|---|---|
| 1. Shiny Dime | One sentence naming the single idea | Does the sentence contain "and", or two verbs with two objects? | Split into two issues, or cut to the stronger half |
| 2. Unique angle | The author's specific claim on this idea | Could a competent stranger have written this sentence? | Source a real story, number or observation the author personally has |
| 3. Show your work | One process detail, mistake or piece of reasoning | Is there a moment where the author was wrong or uncertain? | Ask the author for the version of the story that includes the mistake |
| 4. Compress insight | The repeatable one-liner | Can a reader say it to a colleague from memory? | Cut clauses until they can |
| 5. Specific beats general | The concrete replacements | Count abstract nouns with no example attached | Replace each one, or delete the sentence |

**The kill rule.** If stage 2 fails twice, do not write the issue. A generic issue costs more
than a skipped one, because a subscriber who opens two forgettable issues in a row stops opening.
Tell the user the angle is not there yet and ask for the material that would make it specific.

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

8. **Self-check** (run before finalizing). Each item is settled by quoting or counting the draft,
   not by judging how the issue feels.

   Curiosity Gap checks:
   - The subject line names one thing the reader does not know. Write that thing down in one noun
     phrase. If you cannot, the subject line describes a topic and fails
   - The subject line is answered somewhere in the issue. Quote the sentence that answers it
   - Preview text does not repeat any 3-word run from the subject line

   Perell framework checks:
   - The Shiny Dime sentence is written in the frontmatter and contains no "and" joining two ideas
   - The unique-angle sentence names a specific experience, number or observation the author has
   - At least one paragraph in the main piece describes a process, a mistake or a piece of
     reasoning, not just a conclusion. Point at it
   - Count abstract nouns with no example attached ("engagement", "growth", "alignment"). Each one
     is either replaced or deleted

   Sourcing checks:
   - Every statistic, company size, customer quote and result traces to `knowledge/` or the user.
     List each one with its source
   - Every link in the issue was fetched in this session and resolved. List any that did not, and
     remove them
   - Anything unsourced reads `[NEEDS INPUT: <what>]` in the draft

   Format checks:
   - The section headings match the spine used in the last issue. Diff them
   - Word count is inside the type's range: POV 1500-2500, product 600-900, roundup 400-700,
     internal 300-500
   - Exactly one CTA. Count the imperative sentences aimed at the reader
   - Zero em dashes and zero en dashes

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

## Never invent

- **No statistic, customer quote, company size, or result number, including in subject lines.**
  A curiosity gap is built from a real specific. A plausible-sounding percentage is a fabrication
  that gets forwarded further than anything else in the issue.
- The worked hook examples in this skill are illustrations of SHAPE, not numbers to imitate.
  Never pattern-match a figure out of them.
- Customer stories need a real quote, a real company detail and a real result, from
  `knowledge/content-library/case-studies/` or the user. If any part is missing, write
  `[NEEDS INPUT: <what>]` rather than completing the pattern.
- **Validate every URL before the issue ships.** Fetch each link; drop anything that does not
  resolve. A hallucinated link in a curated-links section destroys the section's whole premise.

## Stop conditions

Do not send, and name the condition that fired.

1. **The Shiny Dime sentence still contains two ideas after one split attempt.** Ship the
   stronger half as this issue and hold the other for the next one.
2. **The unique angle failed twice.** See the kill rule. Skip the issue rather than send a
   generic one.
3. **A link did not resolve.** Remove it. A curated section with one dead or wrong link
   invalidates the reader's trust in the other nine.
4. **A customer story is missing the quote, the company detail or the result.** Write
   `[NEEDS INPUT: <what>]`. Never complete the pattern with a plausible detail.
5. **A roadmap item has no confirmed ship window.** Say "in progress" with no date, or cut it.
   A missed date in a newsletter is remembered longer than the feature.

## Reading the numbers, if the account has them

Never compare against an external benchmark this file does not have. Compare against this
publication's own trailing average, which is the only honest baseline available.

| Signal | What it points at | First thing to change |
|---|---|---|
| Open rate below the trailing 6-issue average for 2 consecutive issues | The subject lines stopped opening a gap | Rerun step 4, draft 3 subject lines, pick on gap strength not cleverness |
| Opens holding but clicks falling | The issue is readable but the CTA is buried or vague | Move the single CTA up, make the verb specific |
| Unsubscribes rising after a format change | You broke the spine subscribers subscribed to | Revert the spine, change one section at a time |
| Replies near zero on a POV newsletter | No POV, or no explicit invitation to reply | Sharpen the angle first, then add one direct ask |
| Forwards concentrated on one section | That section is the real product | Consider promoting it from segment to main piece |

Record what you find in `knowledge/learnings.md` so the next issue starts from it.

## Related skills

- `/email-nurture` when the sequence is lifecycle-triggered rather than a recurring publication
- `/content-writer` for a one-off email or announcement that is not part of the newsletter
- `/thought-leadership-writer` when the main piece is really a standalone 1800-word argument
- `/linkedin-post` for the derivative post pulling the strongest insight out of this issue
- `/content-repurposer` to turn one issue into a run of assets across channels
- `/social-calendar` to plan the issue themes alongside the rest of the calendar
- `/case-study-writer` when the customer segment needs a real documented story behind it
- `/kpi-review` for the periodic read on open rate, click rate and list growth
- `/brand-context` first, whenever `knowledge/brand/voice.md` does not exist yet

## What this skill cannot know

These are real limitations of this skill, and none of them can be resolved from `knowledge/`.
Ask the user or emit `[NEEDS INPUT: <what>]`.

1. **Whether a linked piece still says what it said when it was added.** Pages get edited and
   paywalled. Fetch every link in the session you send, not the session you drafted.
2. **Whether a customer has approved being named in a public newsletter.** Approval for a case
   study is not approval for this issue, and a newsletter forwards further than a web page.
3. **Whether a roadmap item will ship on the date given.** Only the team that owns it knows, and
   this skill will happily repeat a date it was handed six weeks ago.
4. **What the deliverability picture looks like.** Spam placement, list hygiene and sending
   reputation change what the open rate means, and none of it is visible from the draft.

## Platform figures are not facts

Any cadence, character count, best-day, format spec or benchmark in this skill is a starting
default recorded at authoring time, not a published platform rule. Two obligations:

1. **Verify current specs in the platform itself before shipping** anything that depends on them.
2. **This account's own historical data always wins.** Where `knowledge/learnings.md` or the
   team's analytics contradict a default here, follow the data and say so in the output.

Never present a default from this file to a client as though the platform published it. That is
the claim their in-house specialist corrects in the meeting, and the correction discredits
everything else in the document.
