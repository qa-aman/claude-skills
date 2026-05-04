---
name: icp-research
description: Build or refine the Ideal Customer Profile (ICP) and personas using the Jobs-to-be-Done framework (Clayton Christensen / Bob Moesta). Use when the user asks for ICP research, persona development, "who are our customers", buyer personas, audience research, "build our ICP", target customer definition, or wants to update persona docs. JTBD interview questions, three job dimensions (functional/emotional/social), and the Four Forces of Progress are wired into every persona. Writes to knowledge/icp/personas.md so all other skills get smarter.
reads:
  - knowledge/icp/personas.md
  - knowledge/services/
  - knowledge/markets/positioning.md
  - knowledge/content-library/case-studies/
  - knowledge/learnings.md
writes:
  - knowledge/icp/personas.md
  - output/icp-research/
---

# icp-research

Builds rigorous, evidence-based personas using Jobs-to-be-Done. Writes to `knowledge/icp/personas.md` directly so the rest of the OS uses the updated context.

Demographics and firmographics are context. The job the customer is hiring you for is the insight.

## When to use

- "Build our ICP from scratch"
- "Refine our buyer personas"
- "Who are we actually selling to?"
- "Update the persona doc based on these customer interviews"
- "I uploaded customer research, build personas from it"

## Inputs needed

- **Source material** (any combination):
  - Existing customer list (CSV in `uploads/`)
  - Customer interview notes
  - Win/loss data
  - Sales team input (paste in chat)
  - Existing case studies in `knowledge/content-library/case-studies/`
  - Pasted survey results
- **Number of personas** to build (default: 1 primary, 1-2 secondary; max 4)
- **Use case**: positioning, ABM targeting, content strategy, paid ads, sales enablement

## Framework: Jobs-to-be-Done (JTBD)

People don't buy products. They hire them to do a job in their life. The job - not the demographic - is what drives the purchase.

### Three job dimensions (all three required in every persona)

| Dimension | What it is | Example |
|---|---|---|
| **Functional job** | The practical task they need done | "Get pipeline without relying on the founder for every deal" |
| **Emotional job** | How they want to feel when it's done | "Feel confident when the CEO asks about marketing ROI" |
| **Social job** | How they want to be perceived | "Be seen as the person who finally fixed marketing" |

### The struggling moment

The moment when the customer's current solution broke and they started looking. More predictive of buying behavior than any demographic. Every persona must have one.

Format: "What was happening in their life/job when they started looking? What was the specific situation?"

### Hiring and firing triggers

- **Hiring trigger**: what made them actively seek a solution? (the push)
- **Firing trigger**: what were they using before, and why did it stop being enough? (the pull away)

### Four Forces of Progress

| Force | Direction | Question |
|---|---|---|
| **Push of the situation** | Moves them away from status quo | What's so broken they can't stay put? |
| **Pull of the new solution** | Attracts them to the new option | What's the specific promise that drew them? |
| **Anxiety of the new** | Holds them back | What are they afraid might go wrong? |
| **Habit of the present** | Inertia | What makes it easier to do nothing? |

Understanding all four forces explains why good products still lose deals - anxiety and habit beat push and pull.

### JTBD statement format

"When [struggling situation], I want to [motivation], so I can [expected outcome]."

Example: "When the board asks for pipeline attribution and I can't answer, I want a marketing analytics tool I can trust, so I can show that marketing is driving revenue and keep my budget."

## Process

1. **Load existing knowledge.** Read `knowledge/icp/personas.md` (if any), `knowledge/markets/positioning.md`, and case studies. If personas already exist, ask: "Replace or refine?"

2. **Gather evidence.** If `uploads/` has customer data, run analysis:
   - Common industries
   - Common company sizes (employees, revenue)
   - Common roles (the buyer, the user, the influencer)
   - Common geographies
   - Common acquisition channels
   - Win-rate by segment if available

   If no data, interview the user with these questions (not generic persona questions - JTBD-specific):

   **JTBD Interview Questions**

   *The struggling moment:*
   - "Walk me through the specific day or week when you decided to start looking for a solution."
   - "What was happening that made the status quo no longer acceptable?"
   - "How long had that situation been going on before you started looking?"

   *The firing trigger:*
   - "What were you doing before? A spreadsheet, a different tool, a consultant, nothing?"
   - "What happened that made that stop being enough?"

   *The hiring trigger:*
   - "What made you choose this solution over doing nothing, or staying with the old approach?"
   - "What was the specific promise that made you move?"

   *The four forces:*
   - "What were you most anxious about when you decided to switch?" (anxiety)
   - "What almost made you not do it?" (habit + anxiety)
   - "Who else had to sign off? What were their concerns?" (committee anxiety)

   *The three job dimensions:*
   - "When you imagined this working perfectly, what did that feel like?" (emotional job)
   - "How did you explain this decision to your CEO or team?" (social job)
   - "What specific outcome were you hired to produce?" (functional job)

   Standard questions for firmographic baseline:
   - "Who are your top 5 customers by revenue or fit?"
   - "What pattern do you see across them?"
   - "Who do you NOT want as a customer?"
   - "Which deals close fastest?"

3. **Write the persona doc.** Use this structure (one block per persona):

   ```
   # ICP and Personas (DD-MM-YYYY)

   ## Primary persona: <Name + role>
   Example: "Maya, Head of Demand Gen at Series B SaaS"

   ### Demographics
   - Role: <title>
   - Seniority: <IC | Manager | Director | VP | C-level>
   - Team size: <range>
   - Reports to: <role>

   ### Firmographics
   - Company stage: <seed | A | B | C | growth | enterprise>
   - Employees: <range>
   - Revenue: <range>
   - Industries: <list>
   - Geographies: <list>

   ### The struggling moment
   <Specific narrative of the situation that triggered them to look for a solution.
   Must be a concrete scenario, not a general pain point.>
   Example: "It's the Thursday before the board meeting. Pipeline is flat.
   The CEO just asked 'what is marketing doing?' and Maya doesn't have an answer
   that will hold up to scrutiny."

   ### Jobs-to-be-Done

   **Functional job** (the practical task):
   <What they need done, specifically.>

   **Emotional job** (how they want to feel):
   <How they want to feel when the job is done.>

   **Social job** (how they want to be perceived):
   <How they want others to see them as a result.>

   **JTBD statement**:
   "When [struggling situation], I want to [motivation], so I can [expected outcome]."

   List 2-3 JTBD statements if the persona has multiple jobs.

   ### Four Forces of Progress

   | Force | What it is for this persona |
   |---|---|
   | Push (away from status quo) | <specific situation that's making them move> |
   | Pull (toward new solution) | <specific promise that attracted them> |
   | Anxiety (about the new) | <what they're afraid might go wrong> |
   | Habit (inertia) | <what makes doing nothing easier> |

   ### Goals (what they're measured on)
   1. ...
   2. ...
   3. ...

   ### Pains (what's broken today)
   1. ... (specific, not generic)
   2. ...
   3. ...

   ### Hiring / Firing triggers
   - **Hiring trigger**: <what caused them to actively seek a solution>
   - **Firing trigger**: <what they were using before and why it stopped working>

   ### How they buy
   - Discovery channels: <where they find tools>
   - Influencers: <who they trust>
   - Decision criteria: <ranked: outcomes, price, fit, brand, integrations>
   - Buying committee: <other roles involved>
   - Typical sales cycle: <weeks/months>
   - Common objections: <list - mapped to the four forces where possible>

   ### Where they hang out
   - Communities (Slack, Discord, Reddit subs)
   - Newsletters and podcasts
   - Conferences
   - LinkedIn groups, hashtags

   ### Voice (how to write to them)
   - Words they use: ...
   - Words they avoid: ...
   - Tone: <formal | conversational | technical>
   - Length tolerance: <skim | medium | deep dives>

   ### Anti-persona (NOT this person)
   Who looks similar but isn't a fit. Example: "Solopreneurs and pre-seed founders.
   They don't have budget or scale."

   ### Evidence
   - Source 1: <interview, survey, win-rate analysis>
   - Source 2: ...
   - Confidence level: high / medium / low (based on N data points)

   ---

   ## Secondary persona: <Name + role>
   Same structure, shorter
   ```

4. **Cross-check against case studies.** Open `knowledge/content-library/case-studies/`. Do the existing customers fit the personas? Specifically: do their struggling moments match? If not, flag the mismatch. Demographic fit without JTBD fit is a weak persona.

5. **Check against `knowledge/learnings.md`**. Past campaigns may have revealed which struggling moment converts fastest. Update the four forces accordingly.

6. **Self-check**:
   - [ ] Every persona has a struggling moment (specific scenario, not a job title)
   - [ ] Every persona has all three job dimensions: functional, emotional, social
   - [ ] Every persona has a JTBD statement in proper format ("When X, I want Y, so I can Z")
   - [ ] Every persona has all four forces mapped
   - [ ] Hiring and firing triggers are named
   - [ ] At least 3 specific pains, not generic ones
   - [ ] Anti-persona is explicit and concrete
   - [ ] Confidence level is honest (low if fewer than 5 data points)
   - [ ] Voice notes are concrete enough that `/content-writer` can use them

7. **Write to `knowledge/icp/personas.md`** (replace or merge based on user choice).

8. **Save a version snapshot** to `output/icp-research/<DD-MM-YYYY>-personas.md` so prior versions are preserved.

9. **Offer follow-ups**:
   - Update positioning to match (`/onboard --markets` or manual edit)
   - Build content briefs targeted at the struggling moment (not generic persona)
   - Run `/competitor-analyst` to map competitors against the same JTBD

## Rules

- Never invent firmographics. If you have 3 customers, say "based on 3 interviews, low confidence" rather than overstating.
- The struggling moment is mandatory. A persona without one is just a demographic profile.
- The anti-persona is mandatory. If you don't know who is NOT your customer, you don't know who is.
- Pains must be specific. "Wants to grow revenue" is not a pain. "Spending 30% of week manually pulling reports that still don't answer the CEO's questions" is.
- All three job dimensions (functional, emotional, social) are required. Most personas have functional jobs only. Emotional and social jobs are where messaging differentiation lives.
- Voice notes must be concrete enough to use. "Professional" is useless. "Uses 'GTM' not 'go-to-market', avoids exclamation points, prefers numbered lists" is useful.
- Update `knowledge/icp/personas.md` directly. The whole OS depends on this file being current.

## Quick Reference: JTBD Framework

| Concept | What to capture | Why it matters |
|---|---|---|
| Struggling moment | The specific situation that triggered the search | More predictive than demographics |
| Functional job | The practical task needing done | The baseline - everyone captures this |
| Emotional job | How they want to feel | Where messaging resonates |
| Social job | How they want to be perceived | Where brand and positioning live |
| Push force | What's making them leave status quo | Drives urgency |
| Pull force | What attracted them to the new option | Drives conversion |
| Anxiety force | What might make them not switch | Drives objections |
| Habit force | Inertia keeping them in status quo | Drives loss to "do nothing" |
| Hiring trigger | What started active search | Defines the entry point |
| Firing trigger | What they used before and why it failed | Defines the competitive switch |
