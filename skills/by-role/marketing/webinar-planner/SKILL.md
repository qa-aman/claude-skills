---
name: webinar-planner
description: Plan a webinar end-to-end using April Dunford's Obviously Awesome positioning framework to find the topic angle that makes the webinar obviously valuable to the right audience. Produces topic positioning, abstract, speaker brief, registration page, promotion sequence, day-of run-of-show, and post-webinar follow-up. Use when the user asks to plan a webinar, virtual event, online workshop, "we need a webinar on X", host a webinar, online masterclass, or any live virtual event with promotion and follow-up. Reads ICP, services, and brand voice from knowledge/.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/markets/positioning.md
  - knowledge/services/
  - knowledge/learnings.md
writes:
  - output/webinar/
---

# webinar-planner

Plans a webinar as a campaign, not a one-off. Treats the live event as one moment in a multi-week arc: pre-event demand, live execution, post-event nurture. Before any of that, uses April Dunford's Obviously Awesome positioning framework to find the topic angle that makes the webinar obviously valuable to the right audience.

## When to use

- "Plan a webinar on <topic>"
- "We need a virtual event for <audience>"
- "Build a workshop on X"
- "Host a webinar with <partner or guest>"
- "Promote and run a masterclass"

## Framework: Obviously Awesome Positioning (April Dunford)

Most webinar topics compete in red oceans: "Introduction to X", "Best practices for Y", "The future of Z". These sound like every other webinar in the inbox and get ignored.

Dunford's argument: positioning defines the lens through which everything is understood. Get the positioning right and the webinar sells itself. Get it wrong and no amount of promotion fixes it.

**The 5 components - apply to the webinar itself, not just the product:**

1. **Competitive alternatives**: What would the attendee do instead of attending this webinar? (Scroll LinkedIn? Read a blog post? Ask a colleague? Attend a competitor's event?) This is the real competition.

2. **Unique attributes**: What does this webinar offer that the alternatives don't? (Specific framework? Practitioner speakers who've done it, not just studied it? Live benchmarking? Proprietary data?)

3. **Value**: So what? For each unique attribute, what does it actually enable for the attendee? (Saves X hours, avoids Y mistake, gets them to Z outcome faster)

4. **Target customer characteristics**: Who specifically cares most about this value? Not "marketers" - which marketers, at which stage, with which problem, right now?

5. **Market category**: What frame of reference makes this webinar's value immediately obvious? (Not "a marketing webinar" - what specific context makes the target customer say "this is exactly for me"?)

**Positioning self-check**: Could this webinar title and topic be run by any of our competitors? If yes, it is not positioned - it is generic.

**Example of repositioning a topic:**
- Generic (red ocean): "Using AI in Marketing"
- Positioned (blue ocean): "How Series B marketing teams are cutting content production time by 60% without losing brand voice - a live walkthrough with 3 practitioners"

The second version signals: who it is for (Series B marketing teams), what they get (60% time reduction), the specific problem (losing brand voice), and the format (live, practitioners, not theorists).

## Inputs needed

- **Topic and angle** (required)
- **Audience persona** from `knowledge/icp/personas.md`
- **Goal**: pipeline gen, brand awareness, customer education, partner co-marketing, recruiting
- **Format**: solo talk, panel, fireside, workshop, customer story
- **Length**: 30, 45, 60 minutes (default 45)
- **Date and time** (DD-MM-YYYY, timezone)
- **Speakers**: name, role, company, prep notes
- **Registration platform**: Zoom, Webex, Hopin, Restream, etc.

## Process

1. **Load context.** Read brand voice, primary persona, positioning, learnings (especially any prior webinar retros).

2. **Complete positioning pre-work before choosing a title.** Work through all 5 Dunford components:

   ```
   ## Webinar positioning (Obviously Awesome framework)

   **1. Competitive alternatives**
   What will our target attendee do instead of attending this webinar?
   - Alternative 1: <e.g. read a blog post on the same topic>
   - Alternative 2: <e.g. ask a colleague who's done it>
   - Alternative 3: <e.g. attend a competitor's event>
   Why would they choose us instead? <specific answer>

   **2. Unique attributes**
   What does this webinar offer that those alternatives don't?
   - Attribute 1: <specific thing, e.g. "3 practitioners who've 10x'd pipeline sharing exact playbooks">
   - Attribute 2: <specific thing, e.g. "live Q&A with people who made the same mistakes">
   - Attribute 3: <specific thing>

   **3. Value (so what?)**
   For each unique attribute, what does it enable for the attendee?
   - Attribute 1 -> Value: <outcome, e.g. "walk away with a tested framework they can run next week">
   - Attribute 2 -> Value: <outcome>
   - Attribute 3 -> Value: <outcome>

   **4. Target customer characteristics**
   Who cares most about this value right now?
   - Role: <specific, e.g. "VP Marketing at Series B SaaS companies">
   - Situation: <specific, e.g. "first marketing hire, no established playbook">
   - Urgency: <what makes this matter now, e.g. "board has asked for pipeline targets 3x last quarter">

   **5. Market category**
   What frame of reference makes this value immediately obvious?
   - Category: <e.g. "pipeline generation for early-stage B2B" not "marketing webinar">
   ```

3. **Build the title using the positioning output.**

   Title formula: **[Specific value for specific audience] + [unique attribute or approach]**

   - Lead with the value or outcome (what the attendee gets)
   - Name the audience or situation (who this is for)
   - Include a differentiator (what makes this worth 45 minutes of their time)

   Generate 3 title options ranked by specificity. The most specific one wins.

   Bad title: "AI for Marketing Teams"
   Good title: "How we cut content review cycles from 2 weeks to 2 days - a live walkthrough for B2B content teams"

4. **Validate the topic.** Pressure-test:
   - Does the title pass the positioning self-check? (Could a competitor run this exact webinar with their branding? If yes, reposition.)
   - Is it specific enough that a busy person blocks 45 minutes?
   - Does it match a real pain in `knowledge/icp/personas.md`?
   - Is the title outcome-led? "How to <achieve outcome> in <timeframe>" beats "Introduction to X"

   If it fails any check, propose 3 repositioned alternatives before proceeding.

5. **Build the full webinar pack** in `output/webinar/<DD-MM-YYYY>-<slug>/`:

   ```
   output/webinar/25-04-2026-ai-marketing-stack/
   ├── README.md                    # the master plan
   ├── abstract.md                  # public-facing description
   ├── speaker-brief.md             # what speakers need to prepare
   ├── registration-page.md         # landing page copy
   ├── promotion-sequence/          # all promo assets
   │   ├── linkedin-posts.md        # 5-7 posts across 3 weeks
   │   ├── email-invites.md         # 3-email invite sequence
   │   ├── partner-co-marketing.md  # if partner involved
   │   └── ad-creative.md           # paid ads if budget
   ├── day-of/
   │   ├── run-of-show.md           # minute-by-minute timing
   │   ├── speaker-prep-checklist.md
   │   ├── poll-questions.md        # 3-5 audience polls
   │   └── chat-moderation-script.md
   └── follow-up/
       ├── attendee-email.md        # within 24 hours
       ├── no-show-email.md         # different message
       ├── nurture-sequence.md      # 3-email follow-up over 14 days
       └── recap-blog-post.md       # SEO content from the recording
   ```

6. **README.md (master plan)**:

   ```
   # Webinar: <Title>

   **Date**: DD-MM-YYYY HH:MM <TZ>
   **Format**: <solo|panel|fireside|workshop>
   **Length**: <minutes>
   **Speakers**: <names + roles>
   **Audience persona**: <from knowledge/icp/>
   **Goal**: <pipeline|awareness|education|co-marketing|recruiting>

   ## Positioning summary
   - **Target**: <specific audience from Dunford component 4>
   - **Competitive alternative**: <what they'd do instead>
   - **Unique value**: <what this webinar offers that alternatives don't>
   - **Category**: <frame of reference from Dunford component 5>

   ## Success metrics
   - Registrations target: <number>
   - Attendance rate target: <%>
   - Conversion target: <metric, e.g. demo bookings, MQLs>
   - On-demand views target: <14-day post-event>

   ## Timeline
   | Days out | Activity | Owner |
   |---|---|---|
   | -28 | Topic locked, speaker confirmed, page live | |
   | -21 | Promo wave 1 (LinkedIn, email) | |
   | -14 | Promo wave 2 + paid ads if budget | |
   | -7  | Promo wave 3 + partner push | |
   | -3  | Final push, reminder email 1 | |
   | -1  | Reminder email 2, speaker rehearsal | |
   |  0  | Live | |
   | +1  | Attendee + no-show emails | |
   | +3  | Nurture email 1, recap blog live | |
   | +7  | Nurture email 2, on-demand promo | |
   | +14 | Nurture email 3, retro | |
   ```

7. **Abstract must-include list** (for abstract.md):
   - Name the competitive alternative in the opening line: "Most teams are doing X by [alternative approach]. Here's a better way."
   - State the unique value explicitly: what specific outcome will attendees leave with?
   - Name the target customer characteristics: "This is for [specific role] dealing with [specific situation]."
   - End with a concrete deliverable: "You'll leave with [specific thing] you can use [specific timeframe]."

8. **Promotion sequence rules**:
   - Every promotional message leads with value, not features. "You'll learn how to X" not "we'll cover topic Y"
   - Each promo post names the target audience so the right people self-select
   - 7-10 LinkedIn posts across 3 weeks (use `/linkedin-post` for each)
   - 3 invite emails (initial, mid, last-call) (use `/email-nurture` patterns)
   - 2 reminder emails (day before, day of)
   - Partner co-marketing if applicable: dedicated assets they can paste into their channels
   - Paid ads only if there's budget (use `/ad-campaign-writer`)

9. **Day-of run-of-show** (minute by minute):

   ```
   00:00-00:02  Pre-roll: hold music + countdown timer
   00:02-00:05  Welcome + housekeeping (chat, Q&A, recording)
   00:05-00:10  Speaker intros + agenda
   00:10-00:30  Main content block 1
   00:30-00:32  Poll #1 + reaction
   00:32-00:55  Main content block 2
   00:55-00:58  Poll #2
   00:58-01:15  Q&A
   01:15-01:18  Recap + CTA + on-demand link
   01:18-01:20  Close
   ```

10. **Follow-up sequence**:
    - Attendee email (24h): thank you + recording + single CTA (book demo, download resource)
    - No-show email (24h): different copy, lead with "you missed this" + recording
    - Nurture day +3: deeper resource related to webinar topic
    - Nurture day +7: customer story or case study related to topic
    - Nurture day +14: direct ask (demo, trial, sales call)

11. **Self-check**:
    - Positioning pre-work is complete before the title is chosen
    - Title passes the competitor self-check (a competitor could not run this exact webinar)
    - Title contains specific audience + specific value - not a topic name
    - Abstract names the competitive alternative, unique value, and target characteristics
    - All promo messages lead with value, not features or agenda topics
    - Promotion has at least 3 channels
    - Day-of has poll questions and Q&A buffer
    - Follow-up differentiates attendees vs no-shows
    - All copy reads in brand voice
    - Recap blog leverages the recording for SEO

12. **Save** all files. Print the folder tree at the end.

## Rules

- Complete the Dunford positioning before picking a title. The positioning output determines the title, not the other way around.
- A webinar is a campaign, not an event. If you produce only the day-of plan, you've done 10% of the work.
- If the title could describe a competitor's webinar, it is not positioned. Reject it and reposition.
- Differentiate attendee vs no-show messaging. Treating them the same wastes the no-show segment.
- Always plan the recap content. The recording is reusable for 90+ days as on-demand content, blog post, social clips.
- Never overpromise. The title must match the actual content. Bait-and-switch destroys trust and kills future registration rates.
- Check `knowledge/learnings.md` for prior webinar retros. Apply what worked, drop what didn't.
