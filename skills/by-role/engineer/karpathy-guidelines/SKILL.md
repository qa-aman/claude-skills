---
name: karpathy-guidelines
description: "Behavioral guardrails against the six most common LLM coding failure modes. Apply on every coding task: writing, editing, reviewing, or refactoring."
created_by: Aman Parmar
last_modified: 02-05-2026
---

# Karpathy Guidelines

Six failure modes. Six rules. Apply all six on every coding task.

Inspired by [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) (Jan 2026).

## Compliance Checklist

Run this before each phase:

**Before writing code:** rules 1, 2, 4
**While editing:** rule 3
**Before claiming done:** rules 5, 6

- [ ] 1. Did I name every assumption I'm making?
- [ ] 2. Is my solution the minimum that satisfies the request?
- [ ] 3. Did I change only what the request requires?
- [ ] 4. Did I define a verifiable success condition before starting?
- [ ] 5. Do I have command output proving completion?
- [ ] 6. Does my diff do exactly one thing?

---

## 1. Name Every Assumption Before Writing Code

**Trigger:** At the start of any task where the request requires an implicit choice - a library, a data structure, an architecture decision, an interpretation of ambiguous scope.

**Rule:** State every assumption before writing a line. If a requirement has multiple valid interpretations, list them and declare which one you will implement. Do not silently pick.

**Do:**
- "I'm assuming in-memory cache here, not Redis. This won't work across multiple instances - let me know if that matters."
- "This endpoint could return 404 or an empty array for missing records. I'll use 404 to match the pattern in `users.ts`."

**Do not:**
- Silently choose a library, algorithm, or pattern without naming it.
- Proceed when the request is ambiguous. Stop and write: "This could mean X or Y - which one should I implement?"
- State an assumption after you've already coded the decision.

**Self-audit:** List every decision you made that wasn't explicitly specified in the request. If any decision is unnamed, name it before proceeding.

---

## 2. Implement the Minimum That Satisfies the Request

**Trigger:** Before writing any code, adding a dependency, creating an abstraction, or adding an error handler.

**Rule:** Write only what was asked for. Every line of code you write must be traceable to an explicit requirement in the request. If it isn't, do not write it.

**Do:**
- Request: "Add a function to format a date as DD-MM-YYYY." → Write one function. Return a string. Nothing else.
- Request: "Handle the 400 error from the payments API." → Handle the 400 case. Leave other error codes alone.

**Do not:**
- Add an `options` parameter "in case someone needs flexibility later."
- Create an abstract base class when a single function was asked for.
- Add error handling for states that cannot occur given the current codebase.
- Extract a helper for code that has exactly one caller.
- Add logging, metrics, or observability that wasn't requested.

**Self-audit:** If you removed every line that wasn't directly traceable to the request, would the task still be complete? If yes, those lines should not exist.

---

## 3. Change Only What the Request Requires

**Trigger:** Every time you open an existing file to edit it.

**Rule:** Modify only the code necessary to fulfill the request. Do not refactor, rename, reformat, or clean up code adjacent to your changes - even if you would write it differently.

**Do:**
- Fix the broken function. Leave every other function in the file exactly as it is.
- Remove imports, variables, and helpers that YOUR change made unused.
- If you notice an unrelated issue, report it without touching it: "Noticed a potential off-by-one in `parseDate()` on line 47 - not in scope here, flagging for a separate fix."

**Do not:**
- Rename variables you find unclear but were not asked to rename.
- Reformat surrounding code to match your preferred style.
- Fix a bug you noticed in a nearby function.
- Delete pre-existing dead code unless explicitly asked to remove it.
- "Improve" a function while passing through it.

**Self-audit:** Can every changed line be explained by a direct requirement from the request? If a line changed for any other reason, revert it.

---

## 4. Define a Verifiable Success Condition Before Starting

**Trigger:** At the start of any task with more than one step, any bug fix, or any refactor.

**Rule:** Before writing code, state what "done" means as something you can verify with a command. Subjective criteria ("it works", "looks correct") are not success conditions. A passing test, a specific API response, or a zero-error build output are.

**Do:**
- "Fix the login bug" → "A test reproducing the exact failure exists and passes."
- "Add pagination" → "`GET /items?page=2` returns the correct slice with `total_pages` in the response body."
- For multi-step tasks, state the plan before starting:
  ```
  1. Write failing test for the broken case   → verified by: test output shows 1 failure
  2. Implement the fix                        → verified by: that test passes
  3. Confirm no regressions                   → verified by: full suite passes
  ```

**Do not:**
- Start writing code before you can answer: "What command will I run to confirm this is done?"
- Use criteria you cannot check without a human: "looks right", "should work", "seems correct."

**Self-audit:** Is your success condition something you can verify by running a command and reading the output? If not, restate it until it is.

---

## 5. Show Command Output Before Claiming Done

**Trigger:** Any time you are about to write the words "done", "fixed", "complete", "it works", or "tests pass."

**Rule:** Run the verification command. Paste the relevant output. Do not claim completion without evidence. If verification is impossible (UI-only change, no test harness), state that explicitly - do not imply success.

**Do:**
- "I ran `pytest tests/auth_test.py -v` - 14 passed, 0 failed." [paste output]
- "Build succeeded: `npm run build` exited with code 0." [paste last 5 lines]
- "There is no automated test for this UI change. Manual verification is required on the login screen at `/auth/login`."

**Do not:**
- Write "the tests should pass now" without running them.
- Summarize output instead of showing it ("all tests passed" without the actual run).
- Claim the task is done after reading the code without executing it.
- Say "it looks correct" as a substitute for running a check.

**Self-audit:** Does your response contain actual command output proving the task is complete? If not, run the command before responding.

---

## 6. Keep Each Change Atomic

**Trigger:** Any time you notice a second issue while working on the first, or when your diff touches more than one logical concern.

**Rule:** One diff, one purpose. If you discover a second bug while fixing the first, stop - report it and leave it unfixed. Do not bundle unrelated changes into the same commit.

**Do:**
- Fix only what was asked. For anything else discovered: "Noticed `validateToken()` has an off-by-one error on line 83 - not touching it here, flagging for a separate fix."
- Put formatting changes, renames, and cleanup in their own separate commits with their own messages.

**Do not:**
- Fix two bugs in one commit because they are "related."
- Add a feature and fix a bug in the same change.
- Rename a function and change its behavior in the same commit.
- Include whitespace or style cleanup in a functional change.

**Self-audit:** If the user ran `git revert` on this commit, would they lose only the thing they asked for - and nothing else? If they would also lose something unrelated, split the commit before proceeding.
