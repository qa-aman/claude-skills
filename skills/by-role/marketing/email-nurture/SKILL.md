---
name: email-nurture
description: Write multi-email nurture sequences for lead-gen, onboarding, re-engagement, sales, and lifecycle marketing using the Hook Model (Nir Eyal) to architect the sequence arc and PAS (Problem-Agitate-Solution) to structure each email body. Use when the user asks for an email sequence, drip campaign, nurture flow, onboarding emails, re-engagement campaign, "write 5 emails for X", welcome series, or any multi-step email program. Reads brand voice and ICP from knowledge/.
reads:
  - knowledge/brand/voice.md
  - knowledge/icp/personas.md
  - knowledge/services/
  - knowledge/markets/positioning.md
writes:
  - output/email-nurture/
---

# email-nurture

Writes coordinated email sequences. Different from one-off emails (use `/content-writer` for those). Sequences have a narrative arc across emails, built on the Hook Model to systematically increase engagement and investment over time.

## When to use

- "Write a 5-email nurture for our ebook download leads"
- "Draft an onboarding email series for new signups"
- "Build a re-engagement campaign for dormant users"
- "Write a sales sequence for trial conversions"
- "Welcome series for new newsletter subscribers"

## Sequence types this skill handles

| Type | Length | Cadence | Goal |
|---|---|---|---|
| **Lead nurture** (post download) | 4-6 emails | day 0, 2, 5, 9, 14 | Qualify, educate, convert to demo |
| **Onboarding** (post signup) | 5-7 emails | day 0, 1, 3, 7, 14, 30 | Activate, drive first value |
| **Re-engagement** (dormant) | 3 emails | day 0, 4, 10 | Revive or sunset |
| **Sales sequence** (trial conversion) | 4-5 emails | day 0, 3, 7, 12, 14 | Convert to paid |
| **Welcome series** (newsletter) | 3 emails | day 0, 3, 7 | Set expectations, drive engagement |
| **Win-back** (churned) | 3 emails | day 0, 7, 21 | Resurrect lapsed customers |

## Inputs needed

- **Sequence type** (from table above)
- **Trigger event**: what causes someone to enter this sequence (download, signup, X days inactive, trial start)
- **Conversion goal**: book demo, upgrade, complete onboarding step, reply, click CTA
- **Audience persona**: from `knowledge/icp/personas.md`
- **Length and cadence**: default per type, override if needed
- **Sender identity**: founder, AE, generic company, or rotation

## Framework: Hook Model + PAS

### Hook Model (Nir Eyal, Hooked)

Every sequence must move the subscriber through four stages in order:

| Stage | What it is | Email role |
|---|---|---|
| **Trigger** | External cue that starts the behavior. Subject line IS the trigger. Must tap an internal trigger: anxiety, curiosity, FOMO, or identity. | Email 1 |
| **Action** | Simplest behavior done in anticipation of reward. One CTA. Zero friction. | Emails 2-3 |
| **Variable Reward** | Unpredictable value that satisfies and creates craving. Not "tip #4". Something that surprises. | Emails 4-5 |
| **Investment** | Ask the user to put something in: reply, complete a step, share a result. Investment increases future hook likelihood. | Email 6+ |

The sequence as a whole must escalate investment. If email 6 asks for less than email 2, the arc is broken.

### PAS (Problem-Agitate-Solution)

Every individual email body follows this structure:

- **Problem** (1-2 sentences): open with the specific problem this email addresses. Name it precisely, not generically.
- **Agitate** (2-3 sentences): make the pain feel real and immediate. Vivid, concrete, specific to the persona's situation.
- **Solution** (2-3 sentences): introduce the solution - but only after the pain has been established. Never lead with the solution.

## Process

1. **Load context.** Read `knowledge/brand/voice.md`, `knowledge/icp/personas.md`. Stop if voice is missing. Confirm persona match before proceeding.

2. **Map the Hook Model arc.** Before writing, map each email to a Hook stage:

   ```
   Hook Model Map - <Sequence Name>

   Email 1 (Day 0)  - TRIGGER
     Internal trigger tapped: <anxiety | curiosity | FOMO | identity>
     Subject line strategy: <explain how it triggers the internal cue>

   Email 2 (Day X)  - ACTION
     Action asked: <single micro-CTA>
     Friction removed: <what you did to make it dead simple>

   Email 3 (Day X)  - ACTION
     Action asked: <single micro-CTA>

   Email 4 (Day X)  - VARIABLE REWARD
     Reward type: <informational surprise | social connection | achievement>
     Why it's unpredictable: <not "here is tip #4">

   Email 5 (Day X)  - VARIABLE REWARD
     Reward: <what it is>

   Email 6 (Day X)  - INVESTMENT
     Investment asked: <reply with answer | complete setup step | share result>
     Why this increases commitment: <explain>
   ```

   Show this map to the user and get confirmation before drafting.

3. **Write each email** using PAS structure:

   ```
   ---
   email: 1 of N
   day: 0
   hook-stage: TRIGGER
   internal-trigger: <anxiety | curiosity | FOMO | identity>
   trigger: <event>
   sender: <name|company>
   ---

   Subject: <under 50 chars, no clickbait, no all caps>
   Preview text: <30-90 chars, complements subject, never repeats it>

   [PROBLEM - 1-2 sentences: name the specific problem]

   [AGITATE - 2-3 sentences: make the pain vivid and immediate]

   [SOLUTION - 2-3 sentences: introduce it after the pain lands]

   <CTA - one action, low friction>

   <Sign-off>
   <Sender name and role>

   P.S. <optional but high-performing. One line. Reinforce the CTA.>
   ```

4. **Subject line as trigger - internal trigger checklist.** For each subject line, confirm which internal trigger it taps:

   - [ ] **Anxiety**: "Are you making this mistake with X?"
   - [ ] **Curiosity**: "What most teams get wrong about X"
   - [ ] **FOMO**: "What [peer segment] is doing that you're not"
   - [ ] **Identity**: "You're the kind of person who cares about X"

   If the subject line taps none of these, rewrite it. A subject that doesn't tap an internal trigger is just an announcement.

5. **Voice rules**:
   - Match `knowledge/brand/voice.md`
   - Conversational, like writing to one person
   - Second-person ("you"), not third-person
   - One CTA per email. If you have two, the second should be a soft "or just reply"
   - No "Hope this email finds you well"
   - No "I just wanted to reach out"
   - No "Circling back" unless this is intentionally a follow-up

6. **Subject line rules**:
   - 30-50 chars (most clients truncate at 60)
   - No emojis unless `knowledge/brand/voice.md` says they are part of the voice
   - Curiosity, specificity, or self-interest. Pick one.
   - Lowercase or sentence case (matches conversational tone)
   - Test variants: provide 2 alt subject lines per email

7. **Self-check** for the full sequence:
   - [ ] Each email earns its place (no filler emails to hit a number)
   - [ ] The Hook Model stages are present in order: Trigger, Action, Variable Reward, Investment
   - [ ] Investment escalates over time (later emails ask for more than earlier ones)
   - [ ] Every email body follows PAS - solution never leads
   - [ ] The CTA escalates over time (low-friction first, direct ask last)
   - [ ] No two emails repeat the same hook
   - [ ] No two emails share the same internal trigger tap
   - [ ] Total reading time across the sequence under 5 minutes

8. **Save** to `output/email-nurture/<DD-MM-YYYY>-<sequence-name>/`:
   ```
   output/email-nurture/25-04-2026-trial-conversion/
   ├── README.md          (sequence overview, hook map, cadence, goals, A/B test ideas)
   ├── email-1-day-0.md
   ├── email-2-day-3.md
   ├── email-3-day-7.md
   ├── email-4-day-12.md
   └── email-5-day-14.md
   ```

9. **README.md template**:
   ```
   # <Sequence name>

   **Type**: <type>
   **Trigger**: <event>
   **Audience**: <persona>
   **Goal**: <conversion goal>
   **Length**: N emails
   **Total window**: N days

   ## Hook Model Map
   | # | Day | Hook Stage | Internal Trigger | Subject | Job | CTA |
   |---|---|---|---|---|---|---|
   | 1 | 0 | Trigger | Anxiety | ... | ... | ... |

   ## A/B test ideas
   - Test subject line A vs B on Email 1
   - Test PS variant on Email 4
   - Test send time (Tue vs Thu)

   ## Success metrics
   - Email 1 open rate target: >40%
   - Sequence reply rate target: >2%
   - Conversion to <goal> target: <%>
   ```

## Rules

- Never write emails that don't have a clear job. Each email earns its place.
- One CTA per email. Two CTAs = no CTA.
- Subject lines must reflect what's actually inside. No clickbait.
- PAS is mandatory for every email body. Do not open with the solution.
- If the user is sending from a real person (founder, AE), include a check: "Confirm this matches how <Name> writes before sending."
- Every sequence ends with a clear off-ramp: either a clear ask or "we'll stop emailing you about this."
- If the sequence has no Investment-stage email, it is not a Hook sequence. Add one or tell the user why it was omitted.

## Quick Reference: Hook Model

| Stage | Goal | Question to ask |
|---|---|---|
| Trigger | Get them to open and engage | What internal emotion does the subject line tap? |
| Action | Get one simple behavior | Is the CTA the simplest possible next step? |
| Variable Reward | Deliver surprising value | Would someone forward this unprompted? |
| Investment | Get them to put something in | Does this email ask them to give something back? |

## Quick Reference: PAS

| Section | Length | Rule |
|---|---|---|
| Problem | 1-2 sentences | Name the specific problem. Not generic. |
| Agitate | 2-3 sentences | Make the pain vivid, real, and immediate. |
| Solution | 2-3 sentences | Only introduce it after the pain has landed. |
