#!/usr/bin/env python3
"""Execute skill evals and produce a real pass rate.

This is the thing the hygiene gate cannot do. `skill_quality.py` checks whether a
skill HAS a self-check section; this checks whether following the skill actually
produces the behaviour the eval demands.

    python3 scripts/run_evals.py --skill retro                 # one skill
    python3 scripts/run_evals.py --role marketing --limit 5    # a sample
    python3 scripts/run_evals.py --role marketing --baseline   # with-skill vs without
    python3 scripts/run_evals.py --role marketing --estimate   # cost only, no calls

Design decisions that matter, each from a defect found in this repo:

1. THE JUDGE NEVER SEES THE SKILL. It receives the user prompt, the response, and
   the expected-behaviour criteria. If it saw the skill it would inherit the
   author's blind spot and grade the intent rather than the output.
2. THE JUDGE MUST QUOTE. Every verdict cites a span of the response, so a PASS
   cannot be a vibe. Missing quote = FAIL.
3. FAIL IS THE DEFAULT. Ambiguity resolves to FAIL, because a skill that only
   sometimes refuses to invent a statistic is a skill that invents statistics.
4. NOTHING RUNS UNTIL CALIBRATION PASSES, so a broken harness cannot produce
   confident numbers.
5. RESULTS ARE CACHED by (skill content + prompt + model), so re-running after
   editing one skill costs one skill, not the whole suite.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".eval-cache"
JUDGE_SCHEMA = '{"verdict": "PASS" | "FAIL", "quote": "<verbatim span from the response>", "reason": "<one sentence>"}'


def have_cli():
    return shutil.which("claude") is not None


def call(prompt: str, timeout: int = 240) -> tuple[str, float]:
    """One isolated, non-interactive model call via the Claude Code CLI."""
    t0 = time.time()
    try:
        r = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True, text=True, timeout=timeout,
            cwd=str(ROOT),
        )
    except subprocess.TimeoutExpired:
        return "__TIMEOUT__", time.time() - t0
    if r.returncode != 0:
        return f"__ERROR__ {(r.stderr or '').strip()[:300]}", time.time() - t0
    return r.stdout.strip(), time.time() - t0


def skill_body(skill_dir: Path) -> str:
    t = (skill_dir / "SKILL.md").read_text()
    m = re.match(r"^---\n.*?\n---\n", t, re.S)
    return t[m.end():] if m else t


def cache_key(*parts) -> Path:
    h = hashlib.sha256("||".join(parts).encode()).hexdigest()[:20]
    return CACHE / f"{h}.json"


def cached(key: Path):
    if key.exists():
        try:
            return json.loads(key.read_text())
        except Exception:
            return None
    return None


def judge(user_prompt: str, response: str, expected: str) -> dict:
    """Grade the RESPONSE against the criteria. The judge never sees the skill."""
    p = f"""You are grading one response against a specification. You have NOT seen the
instructions the responder was given, and you must not speculate about them. Grade only
what is present in the response text.

USER ASKED:
{user_prompt}

REQUIRED BEHAVIOUR (all of it must be evident in the response):
{expected}

RESPONSE TO GRADE:
---
{response[:12000]}
---

Rules:
- PASS only if every required behaviour is clearly evident in the response text.
- You MUST quote a verbatim span from the response that justifies your verdict. If you
  cannot quote one, the verdict is FAIL.
- If the required behaviour is a refusal or a placeholder (for example refusing to invent
  a statistic, or emitting [NEEDS INPUT]), then producing the invented content instead is
  a FAIL even if the response is otherwise excellent.
- Ambiguity resolves to FAIL.
- Output ONLY this JSON, nothing else: {JUDGE_SCHEMA}"""
    out, _ = call(p, timeout=180)
    m = re.search(r"\{.*\}", out, re.S)
    if not m:
        return {"verdict": "FAIL", "quote": "", "reason": f"judge returned no JSON: {out[:120]}"}
    try:
        d = json.loads(m.group(0))
    except Exception:
        return {"verdict": "FAIL", "quote": "", "reason": "judge JSON did not parse"}
    if d.get("verdict") == "PASS" and not (d.get("quote") or "").strip():
        return {"verdict": "FAIL", "quote": "", "reason": "PASS without a supporting quote"}
    return d


def collect(root: Path, role: str | None, skill: str | None):
    base = root / "skills"
    cases = []
    for ev in sorted(base.rglob("evals/evals.json")):
        sd = ev.parent.parent
        if skill and sd.name != skill:
            continue
        if role and role not in str(sd):
            continue
        try:
            data = json.loads(ev.read_text())
        except Exception as e:
            print(f"  ! {sd.name}: unreadable evals.json ({e})")
            continue
        for c in data.get("evals", []):
            cases.append((sd, c))
    return cases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill")
    ap.add_argument("--role")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--baseline", action="store_true", help="also run without the skill, to measure lift")
    ap.add_argument("--estimate", action="store_true", help="count calls and stop, make none")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--out", default="evals/benchmark.json")
    a = ap.parse_args()

    cases = collect(ROOT, a.role, a.skill)
    if a.limit:
        cases = cases[: a.limit]
    if not cases:
        print("no eval cases matched")
        return 1

    calls = len(cases) * (2 if a.baseline else 1) * 2  # response + judge, per arm
    print(f"cases: {len(cases)}   model calls required: ~{calls}")
    if a.estimate:
        print("estimate only, nothing run. Re-run without --estimate to execute.")
        return 0

    if not have_cli():
        print("ERROR: `claude` CLI not on PATH. This runner shells out to it.")
        return 1

    # Gate: never produce numbers from an uncalibrated harness.
    cal = subprocess.run([sys.executable, str(ROOT / "scripts/skill_quality.py"), "--self-test"],
                         capture_output=True, text=True, cwd=str(ROOT))
    if cal.returncode != 0:
        print("Calibration self-test FAILED. Fix the instrument before trusting any score.\n")
        print(cal.stdout[-1200:])
        return 1

    CACHE.mkdir(exist_ok=True)
    results, t_start = [], time.time()

    for i, (sd, c) in enumerate(cases, 1):
        body = skill_body(sd)
        print(f"[{i}/{len(cases)}] {sd.name} #{c['id']}", flush=True)

        arms = [("with_skill", f"{body}\n\n---\nFollow the instructions above.\n\nUser: {c['prompt']}")]
        if a.baseline:
            arms.append(("baseline", c["prompt"]))

        row = {"skill": sd.name, "id": c["id"], "prompt": c["prompt"]}
        for arm, prompt in arms:
            key = cache_key(arm, prompt, c["expected_output"])
            hit = None if a.no_cache else cached(key)
            if hit:
                row[arm] = hit
                print(f"      {arm}: {hit['verdict']} (cached)")
                continue
            resp, secs = call(prompt)
            if resp.startswith("__"):
                v = {"verdict": "FAIL", "quote": "", "reason": resp[:160], "seconds": round(secs, 1)}
            else:
                v = judge(c["prompt"], resp, c["expected_output"])
                v["seconds"] = round(secs, 1)
                v["chars"] = len(resp)
            row[arm] = v
            key.write_text(json.dumps(v))
            print(f"      {arm}: {v['verdict']} - {v.get('reason','')[:90]}")
        results.append(row)

    passed = sum(1 for r in results if r["with_skill"]["verdict"] == "PASS")
    rate = 100 * passed / len(results)
    report = {
        "generated": time.strftime("%d-%m-%Y %H:%M"),
        "scope": {"role": a.role, "skill": a.skill, "cases": len(results)},
        "with_skill": {"passed": passed, "total": len(results), "pass_rate": round(rate, 1)},
        "duration_seconds": round(time.time() - t_start, 1),
        "results": results,
    }
    if a.baseline:
        bp = sum(1 for r in results if r.get("baseline", {}).get("verdict") == "PASS")
        report["baseline"] = {"passed": bp, "total": len(results), "pass_rate": round(100 * bp / len(results), 1)}
        report["lift_points"] = round(rate - 100 * bp / len(results), 1)

    out = ROOT / a.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n")

    print(f"\nwith skill: {passed}/{len(results)} = {rate:.1f}%")
    if a.baseline:
        print(f"baseline:   {report['baseline']['passed']}/{len(results)} = {report['baseline']['pass_rate']}%")
        print(f"lift:       {report['lift_points']:+.1f} points")
    fails = [r for r in results if r["with_skill"]["verdict"] == "FAIL"]
    if fails:
        print(f"\nFAILURES ({len(fails)}):")
        for r in fails:
            print(f"  {r['skill']} #{r['id']}: {r['with_skill'].get('reason','')[:110]}")
    print(f"\nreport: {out}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
