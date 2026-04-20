---
name: meeting-to-spec-update
description: |
  Update a product spec from a meeting transcript — extract decisions, open questions, spec changes,
  and flowchart updates. Use this skill when:
  - A meeting discussed changes to a product spec and you need to update the local .md + wiki page
  - The user shares a meeting URL or transcript ID and says "update the spec"
  - The user says "what needs to change in the spec from this meeting"
  - After processing a meeting, when decisions affect a spec's content (not just action items)
  Trigger phrases: "update spec from meeting", "what changed in the spec", "meeting to spec",
  "sync meeting decisions to spec", "add meeting decisions to spec"
created_by: Aman Parmar
last_modified: 20-04-2026
---

# Meeting-to-Spec Update

Update a product spec from a meeting transcript — decisions, open questions, spec text, flowcharts.

This skill focuses on **spec content changes** driven by meeting discussions. Pair it with a separate
"process meeting" skill if you also need to capture action items and tracker tickets.

## Inputs

The user provides:
1. **Meeting source** — a meeting URL, transcript ID, or "use the last meeting"
2. **Target spec** — file path, spec name, or "figure it out from context"

**Multi-spec meetings:** A single meeting may discuss changes to 2+ specs. If the transcript covers
multiple features, identify ALL affected specs in Step 2 and run Steps 3-8 for each spec sequentially.
Present a combined summary at the end. Ask the user which spec to start with if more than 3 are affected.

## Workflow

### Step 1: Fetch the Full Transcript

Always fetch BOTH the meeting summary AND the full transcript:
1. List-meetings or get-meeting (for summary, attendees, metadata)
2. get-meeting-transcript (for verbatim transcript — needed for zero-assumption accuracy)

**Never rely on summary alone.** The summary may omit nuance, disagreements, or conditional agreements.

### Step 2: Identify the Target Spec

If not specified by the user:
- Read your spec index (e.g., `epic-to-spec-map.yaml`) and match meeting keywords to spec keywords
- Confirm with the user before proceeding

Read the full spec file to understand current state.

**Multi-spec detection:** While reading the transcript, if you encounter discussions about features
NOT covered by the target spec, note the other spec(s) affected. After completing the primary spec,
ask: "The meeting also discussed [feature X] which maps to [spec Y]. Want me to update that spec too?"

### Step 3: Line-by-Line Transcript Audit

Go through the transcript systematically. For every point discussed, classify it as one of:

#### A. Confirmed Decision
**Criteria — ALL must be true:**
- Someone explicitly stated the decision ("let's go with X", "we'll do X", "agreed")
- No one objected or said "we need to check"
- The speaker did NOT say "I'll confirm later" or "pending confirmation"

For each confirmed decision, record:
- What was decided (exact wording from transcript)
- Who decided (names from transcript, resolved via your team directory, e.g., `.local/team/users.md`)
- Rationale (why, from transcript)
- What was rejected (if discussed)

#### B. Open Question
**Criteria — ANY of these:**
- Someone said "we need to check", "I'll confirm", "let's discuss offline"
- Multiple options were discussed but no agreement reached
- A concern was raised but not resolved
- The topic was acknowledged but explicitly deferred

For each open question, record:
- The question (clear, specific)
- Who needs to clarify (name + role)
- Context from the meeting

#### C. Spec Change
**Criteria:**
- A confirmed decision changes existing spec text
- New information was shared that updates a section
- A new feature, behaviour, or constraint was described and agreed

For each spec change, record:
- Which section is affected
- What the current spec says
- What it should say now
- Source (which decision or discussion point)

#### D. Not Relevant to Spec
- Action items (handled separately)
- Administrative discussions
- Tangential topics

### Step 4: Present for Review (MANDATORY — never skip)

**CRITICAL RULE: Zero assumptions.** Never proceed without user review.

Present these tables to the user:

**Table 1: Confirmed Decisions**
```
| # | Decision | Decided by | Confidence | Spec section |
```

**Table 2: Open Questions**
```
| # | Question | Clarification from | Context |
```

**Table 3: Spec Changes**
```
| # | Section | What changes | Source |
```

**Table 4: Diff Preview (current → proposed)**

For each spec change, show the user exactly what will change (CURRENT vs PROPOSED text blocks).

**Table 5: Decision Conflict Check**

Before writing decisions, check any existing `decisions.md` for contradictions:
```
| New decision | Existing decision | Conflict? |
```
If a conflict exists, the new decision must include `**Supersedes:** D-NNN-XXX` and the old decision's
status must be updated to `Superseded by D-NNN-XXX`.

Ask: "Please review. I'll only update the spec with items you confirm. Any corrections?"

### Step 5: Update the Spec

After user confirms, make changes in this order:

#### 5a. Update local .md spec file
- Make surgical edits — don't rewrite sections unnecessarily
- Add Open Questions as a new section in table format:
  ```markdown
  # 9. Open Questions

  | **ID** | **Question** | **Clarification needed from** | **Context** | **Raised on** | **Status** |
  |---|---|---|---|---|---|
  | OQ-001 | ... | ... | ... | DD-MM-YYYY | Open |
  ```
- Add a "Decisions Log" reference section pointing to `decisions.md`
- If flowcharts exist and any confirmed decision affects a flow, update the Mermaid code

#### 5b. Create/update decisions.md
- Follow a `D-NNN-XXX` format (NNN = spec folder number, XXX = sequential)
- Newest-first ordering
- Include: meeting reference (title + date), attendees (full names from the team directory),
  linked ticket, rationale, rejected alternatives
- **Decision confidence:** Only write "Agreed" decisions
- Cross-references: if a decision references another spec's decision, use the full wiki URL
- Update your spec index (e.g., `epic-to-spec-map.yaml`) to flip `has_decisions_log: false → true`
  if this is the first `decisions.md` for the spec

#### 5c. Update change.md
Append a new entry (newest-first) with:
- Source: meeting title + date + attendees
- What changed (section by section)
- What did NOT change
- Why it changed
- How to verify

#### 5d. Update versioning table
- Add a new version row to the spec's versioning table
- Use your wiki's date macro for dates, hyperlink the version to the wiki URL
- Use `<br/>` between each numbered point in the change description
- Reference the updater via your wiki's user-link macro (avoid plain text names)

#### 5e. Update acceptance criteria and test cases
If any confirmed decision changes expected behaviour, update the Acceptance Criteria section:
- Add new test scenarios for new behaviours
- Modify scenarios whose expected behaviour changed
- Add non-negotiable test cases for critical decisions

#### 5f. Update flowcharts (if applicable)
- If any confirmed decision changes the logic flow, update the Mermaid code in the spec
- Validate mermaid syntax before rendering: write to a temp `.mmd` file and run
  `npx @mermaid-js/mermaid-cli -i <file>.mmd -o /tmp/test.png -s 2 -b white`
- Render updated flowcharts as PNGs and store in `<spec-folder>/images/`

#### 5g. Update spec ecosystem index files

Check and update these index files if affected by the spec changes:

**a) `spec-decisions-index.md`** — if any confirmed decision adds, changes, or removes a business
   rule, threshold, or decision: add/update entries with spec reference and section number.

**b) `glossary.yaml`** — if the meeting introduced new terminology, acronyms, or product concepts:
   add new terms with definition, spec reference, and first-used date.

**c) Any feature-matrix files** — if the spec changes affect which variants/modules support the
   feature, update the feature's row accordingly.

If no updates are needed for any index file, state explicitly: "Checked [files] — no updates needed."

#### 5h. Add a comment on the linked tracker ticket

After spec changes are applied locally, add a comment on the linked ticket:
- Summarise what changed (section-level, not full detail)
- Link to the wiki spec page
- Reference the meeting title and date
- Use your team's `@name` mention format (auto-resolved from the team directory)

#### 5i. Cross-spec Impact Analysis (MANDATORY)

Every spec change can ripple into dependent specs. This step catches those ripples BEFORE the user asks.

**How to do it:**

1. **Read your spec index** — find the current spec's entry. Note its `depends_on` and look for other
   specs that have `depends_on` pointing to this spec.
2. **Grep `spec-decisions-index.md`** (or your equivalent) for keywords related to the changes made.
3. **Grep all spec .md files** for terms that intersect with the changes.
4. **For each potentially affected spec**, read the relevant section and assess:
   - Does the change in THIS spec contradict or modify what THAT spec says?
   - Does THAT spec reference a behaviour that has now changed?
   - Does THAT spec need a new assumption, caveat, or cross-reference?
5. **Present the impact table to the user:**

```
| # | Affected spec | Section | What needs updating | Why |
```

Ask: "These specs may need updates based on today's changes. Want me to apply them?"

**On confirmation:**
- Make surgical edits to each affected spec's .md file
- Append to each affected spec's `change.md` (with cross-reference to the source spec and meeting)
- Do NOT push to the wiki yet — present all local changes first, push only when user confirms

**If no cross-spec impact found:** State explicitly: "No cross-spec impact found. Checked N specs."

### Step 6: Self-Healing Eval (MANDATORY — runs automatically)

This eval runs BEFORE presenting results. If issues are found, fix them silently and only present
the fixed version.

#### 6a. Rubric Scoring

| # | Criteria | Min | Weight | What to check |
|---|----------|-----|--------|---------------|
| 1 | **Source fidelity** | 8 | 15% | For every change made, find the exact transcript line that justifies it. If none exists, remove the change. |
| 2 | **Completeness** | 8 | 15% | List every distinct topic discussed. Check each is captured as spec change, decision, open question, or "not relevant". |
| 3 | **Zero assumptions** | 9 | 15% | For every statement added as fact: (a) someone explicitly said it, (b) no one said "we need to check", (c) no conditional language. |
| 4 | **Engineering actionability** | 8 | 15% | Can a developer implement without asking a question? |
| 5 | **QA testability** | 8 | 10% | Can QA write a test case with clear expected behaviour? |
| 6 | **Structure** | 8 | 10% | Section numbers sequential, no duplicate headings, tables have headers, flowcharts render. |
| 7 | **Edge cases** | 7 | 10% | Offline scenarios, conflict resolution, missing data, boundary conditions captured. |
| 8 | **Cross-references** | 8 | 5% | All OQ-XXX and D-NNN-XXX references point to existing entries. Ticket/wiki links valid. |
| 9 | **Formatting** | 9 | 5% | DD-MM-YYYY dates, no em-dashes, hyperlinked ticket/wiki refs, no direct quotes in spec body, numbered lists. |
| 10 | **@mentions everywhere** | 9 | 5% | EVERY person name on the wiki uses the user-link macro — not plain text. |

#### 6b. Auto-Fix Protocol

For each criterion scoring below minimum:
1. Identify the gap
2. Fix it silently
3. Log the fix

Do NOT ask the user for permission to fix rubric failures. Fix them, then report what was fixed.

#### 6c. Present Results

After all fixes are applied, show the rubric scores and any auto-fixes applied.

#### 6d. Cross-spec Eval (if Step 5i was executed)

For each affected spec that was updated, run a mini-eval:
- Change is surgical (only the relevant section was modified)
- `change.md` updated (entry added with cross-reference to source spec)
- No contradictions with other content in the affected spec
- Cross-reference to source decision (D-NNN-XXX) added

If any check fails, fix silently and report.

### Step 7: Push to Wiki (if user confirms)

After user approves the local changes:

1. **Surgical section updates** using your wiki's API (e.g., a `confluence-update` script):
   - `replace-section` for changed sections
   - `add-section` for new sections (Open Questions, Decisions Log reference)
   - `add-table-row` or `replace-table-row` for the versioning table
2. **Upload flowchart PNGs** as attachments, then insert via the wiki's image macro
3. **Never full-page push** — always surgical updates
4. `replace-section` HTML must NOT include the heading tag — the script keeps the original heading
   and replaces only the content below it. Including the heading creates a duplicate.
5. **Post-push duplicate heading check** — verify no heading text appears twice

### Step 8: Work Log

Auto-log this spec update to your daily work log:
- Meeting title, spec name, number of decisions logged, open questions added, sections changed,
  cross-spec impact count

### Step 9: Summary

```
Spec updated from meeting: "<Meeting Title>" (DD-MM-YYYY)
  Decisions logged:     X (D-NNN-001 to D-NNN-00X)
  Open questions added: Y
  Sections updated:     §A, §B, §C
  Flowcharts updated:   F1, F3 (re-rendered + uploaded)
  Cross-spec impact:    N specs affected
  Quality score:        X.X/10
  Auto-fixes applied:   N

  Files changed (primary spec):
  - <spec-path>/spec.md
  - <spec-path>/decisions.md (created/updated)
  - <spec-path>/change.md
  - <spec-path>/images/*.png (if flowcharts changed)
  - epic-to-spec-map.yaml (has_decisions_log, last_reviewed)

  Files changed (cross-spec impact):
  - <affected-spec>/spec.md — §X updated
  - <affected-spec>/change.md — entry added

  Wiki:
  - Page version: N → N+M
  - URL: <page-url>
```

## Key Rules

1. **Zero assumptions** — if confidence < 100%, mark as open question and ask user.
2. **Decisions only if certain** — never log a discussed-but-not-agreed proposal as a decision.
3. **No raw meeting-tool URLs in shared docs** — source attribution in `decisions.md` uses meeting title + date only.
4. **Names from the team directory** — always look up full names, never use transcript approximations.
5. **Never fabricate account IDs** — always grep the team directory. Fake IDs render as "Unlicensed user" on wikis.
6. **Numbered lists on the wiki** — use 1,2,3 or a,b,c. Build HTML programmatically with `<ol><li>` for multi-item lists.
7. **Tracker smart-links on the wiki** — use the tracker-issue macro, not plain `<a href>`.
8. **Hyperlink all references** — ticket IDs, wiki pages, filters, dashboards must be clickable in generated .md.
9. **No quotes in specs** — never use direct quotes or "X said" in spec documents. Quotes belong in `decisions.md` and meeting notes.
10. **Date format** — always DD-MM-YYYY.
11. **Auto-review before done** — always run the 10-criteria rubric, fix issues below threshold.
12. **Versioning table format** — date macros, hyperlinked versions, `<br/>` between numbered points.
13. **Update references on rename** — if a section number changes, grep the entire repo and update all cross-references.
14. **Attendee resolution fallback** — if a name cannot be resolved from the team directory, flag it:
    "Could not resolve '[name]'. Please provide full name and account ID, or confirm this person is external." Never guess.

## Anti-Patterns

1. **Skipping the user-review step** (Step 4) — always get explicit approval before editing the spec.
2. **Writing "likely agreed" decisions as confirmed** — only log things that were explicitly agreed.
3. **Full-page wiki pushes** — always surgical updates.
4. **Inlining quotes into the spec body** — quotes belong in `decisions.md`, not the spec.
5. **Running without a team directory** — you will either fabricate IDs or lose context.

## Quality Checklist

- [ ] Full transcript fetched (not just summary)
- [ ] Multi-spec detection run before editing
- [ ] User approved all three tables (decisions, open questions, spec changes)
- [ ] `decisions.md` created/updated with meeting reference and rejected alternatives
- [ ] `change.md` appended with section-by-section diff
- [ ] Versioning table updated with date macro and hyperlinked version
- [ ] Cross-spec impact analysis run and reported
- [ ] 10-criteria rubric scored ≥ threshold on every item
- [ ] Wiki pushed surgically (never full-page)
- [ ] Daily work log entry appended
