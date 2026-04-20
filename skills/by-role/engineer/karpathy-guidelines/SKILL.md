---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.
created_by: Aman Parmar
last_modified: 20-04-2026
---

# Karpathy Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls (posted Jan 2026).

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

Example:
- Bad: User says "add caching" → silently pick Redis, add a client, wire it in.
- Good: "Caching can live in-memory (simple, per-process) or Redis (shared, needs infra). Which fits? I'll assume in-memory unless told otherwise."

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you can delete half the code and tests still pass, delete it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Verify Before Claiming Done

**Evidence before assertions. Never say "fixed" without proof.**

Before claiming a task is complete:
- Run the test, build, or command that proves it.
- Paste the output (or the relevant line) as evidence.
- If you can't verify (e.g., UI change, no test available), say so explicitly — don't imply success.

"Tests pass" without running them is a guess. "I ran `pytest tests/foo.py` and all 12 passed" is a claim.

## 6. Scope Discipline

**One task per change. Don't bundle unrelated fixes.**

- If you notice a second bug while fixing the first, note it — don't fix it in the same change.
- If the user asks for A and you also do B, you've made the diff harder to review and revert.
- Unrelated cleanup, renames, or formatting belong in their own commit.

The test: Could the user revert your change and only lose the thing they asked for? If no, you bundled too much.
