#!/usr/bin/env python3
"""Structural hygiene gate for SKILL.md files. NOT a quality score.

Usage:
    python3 scripts/skill_quality.py                      # whole repo
    python3 scripts/skill_quality.py skills/by-role/marketing
    python3 scripts/skill_quality.py --min 85 <path>      # fail below threshold
    python3 scripts/skill_quality.py --detail <path>      # per-skill breakdown

Exit 1 if any skill scores below --min (default 85).

WHAT THIS MEASURES: structural completeness. Does the skill declare a source,
load its context, save a dated artifact, guard against fabrication, carry a
self-check, cross-link siblings, ship evals, and stay spec-legal.

WHAT IT DOES NOT MEASURE: quality. On 09-08-2026 its ranking was compared against
a blind human-style review of the same 6 skills. Spearman correlation: 0.17.
Essentially uncorrelated. It scored a skill 100/100 whose self-assessed output
scores have no anchor, and it awarded fabrication-guard points to a rule that
points at a file the skill never loads. A regex counts the string; only a reader
sees the string does nothing.

USE IT AS: a cheap pre-filter that catches structural absence before a human or a
blind reviewer spends attention. A passing score means "nothing obvious is
missing", never "this is good".

NEVER: mass-edit skills to raise these numbers, or report a score as a quality
verdict. Run --self-test first; if calibration fails, the tool is wrong, not the
skills.
"""

import argparse
import json
import re
import sys
from pathlib import Path

SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
CC_KEYS = {"argument-hint", "disable-model-invocation", "disallowed-tools", "model", "context"}

# Evidence that a source is actually named rather than hand-waved. Pattern-based
# rather than a surname allowlist, because an allowlist silently fails on any
# author it has not met (it scored pr-pitch-writer at 35 by not knowing "Holiday").
ATTRIB = [
    re.compile(r'\bby\s+[A-Z][a-z]+\s+[A-Z][a-z]+'),          # "by Eugene Schwartz"
    re.compile(r'\*"[^"]{4,60}"\*'),                            # *"Book Title"*
    re.compile(r'\*\*"[^"]{4,60}"\*\*'),                        # **"Book Title"**
    re.compile(r'\*[A-Z][^*\n]{4,60}\*\s*\(\d{4}\)'),           # *Book Title* (1932)
    re.compile(r'\(([A-Z][a-z]+\s+(and|&)\s+)?[A-Z][a-z]+,\s*\*'),  # (Heath and Heath, *Book*)
    re.compile(r'\b[A-Z][a-z]+(\s+and\s+[A-Z][a-z]+)?\'s\s+[A-Z*"]'),  # Dunford's *Obviously*
    re.compile(r'\b(framework|model|method|principle|heuristic|matrix|sequence)\b[^.\n]{0,40}\('
               r'[A-Z][a-z]+', re.I),                           # framework (Chaffey
    re.compile(r'\([A-Z][a-z]+\s+[A-Z][a-z]+[,)]'),             # (Taiichi Ohno, / (Dave Chaffey)
    re.compile(r'\s-\s[A-Z][a-z]+\s+[A-Z][a-z]+(,|$)', re.M),  # Five Whys - Taiichi Ohno
]
VAGUE_SOURCE = re.compile(r"\b(best practices|industry standard|proven frameworks?|common wisdom)\b", re.I)
FABRICATION_GUARD = re.compile(
    r"never (invent|fabricate|make up)|do not (invent|fabricate|make up)|\[NEEDS INPUT|\[UNVERIFIED|\[INFERRED", re.I
)
HONEST_LIMITS = re.compile(
    r"what this skill cannot (know|verify)|what (i|this) \w* ?(could not|cannot|can't)|"
    r"could not (assess|fix|verify)|open questions|what this research cannot|"
    r"limitations|unverified|what i don'?t know", re.I
)
DECISION = re.compile(
    r"(\bthreshold|\bpriorit|rank(ed)? by|warning sign|\bflag (it|if|any|them)|\bstop:|hard rule|"
    r"do not (proceed|claim|publish|ship)|\bscore\b|\bbelow \d|\bat least \d|/5\b|/10\b|out of \d+|\btarget:|\bminimum|\bmax(imum)? \d|"
    r"under \d+ (char|word)|\d+-\d+ words|\bnever \w+ more than|non-negotiable|"
    r"\bif .{0,40}, (stop|flag|say so|do not))", re.I
)


def parse(md: str):
    m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
    fm, body = (m.group(1), md[m.end():]) if m else ("", md)
    keys = set(re.findall(r"^([a-zA-Z_-]+):", fm, re.M))
    d = re.search(r"^description:\s*(.*)$", fm, re.M)
    desc = d.group(1).strip() if d else ""
    if desc in (">", "|", ">-", "|-"):
        b = re.search(r"^description:\s*[>|]-?\s*\n((?:[ \t]+.*\n)+)", fm, re.M)
        desc = " ".join(l.strip() for l in b.group(1).splitlines()) if b else ""
    return fm, body, keys, desc


def score(path: Path):
    md = (path / "SKILL.md").read_text()
    fm, body, keys, desc = parse(md)
    full = md
    c, notes = {}, []

    def add(key, pts, max_pts, note=None):
        c[key] = (pts, max_pts)
        if pts < max_pts and note:
            notes.append(note)

    # 1. Named source (12) - DECLARED in metadata.grounded_in, then verified against
    # the body. Declaration beats inference: a regex over prose can never enumerate
    # every attribution syntax, and every miss is a silent false negative.
    declared = re.findall(r"^\s{4}- \"?([^\"\n]+)\"?\s*$", 
                          re.search(r"grounded_in:\n((?:\s{4}- .*\n)+)", fm).group(1), re.M) \
               if re.search(r"grounded_in:\n((?:\s{4}- .*\n)+)", fm) else []
    honoured = [d for d in declared
                if any(tok in body for tok in re.findall(r"[A-Z][a-z]{3,}", d))]
    if not declared:
        pts, why = 0, "metadata.grounded_in not declared"
    elif not honoured:
        pts, why = 2, f"declares {declared} but the body never mentions it (declaration is unbacked)"
    else:
        pts, why = 12, None
    if VAGUE_SOURCE.search(full):
        pts, why = max(0, pts - 4), "leans on 'best practices' language"
    add("source", pts, 12, why)

    # 2. Framework applied, not name-dropped (12) - a structured model in the body
    tables = len(re.findall(r"\n\|[ :-]*-{2,}[ :|-]*\|", full))
    # how often the declared source is actually worked with in the body
    STOP = {"Building", "Advertising", "Methods", "Handbook", "Lessons", "Clarity", "Grace",
            "Group", "Model", "Framework", "Strategy", "Analytics", "Principle", "Plan"}
    toks = {tok for d in honoured for tok in re.findall(r"[A-Z][a-z]{3,}", d) if tok not in STOP}
    uses = sum(body.count(t) for t in toks)
    pts = (6 if tables >= 2 else 3 if tables == 1 else 0) + (6 if uses >= 3 else 3 if uses >= 1 else 0)
    add("framework", min(pts, 12), 12,
        "source declared but barely used in the body" if uses < 3 else "no structured model or table")

    # 3. Context binding (10) - declares reads AND the body loads them
    declares = "reads:" in fm
    loads = bool(re.search(r"(load context|read `knowledge|before you start|check .*exists)", body, re.I))
    add("context", (5 if declares else 0) + (5 if loads else 0), 10,
        "declares reads but body never loads them" if declares and not loads else "no context loading")

    # 4. Named artifact (10) - declares writes AND body gives a dated save path
    dec_w = "writes:" in fm
    saves = bool(re.search(r"output/[a-z-]+/<?DD-MM-YYYY|save.*to `output/", body, re.I)) or \
            bool(re.search(r"writes:\n(?:\s+- knowledge/)", fm))   # knowledge-writers are artifact producers too
    add("artifact", (4 if dec_w else 0) + (6 if saves else 0), 10,
        "no dated save path in the body")

    # 5. Anti-fabrication guard (12) - the highest-harm failure mode
    hits = len(FABRICATION_GUARD.findall(full))
    add("no_fabrication", 12 if hits >= 3 else 8 if hits == 2 else 4 if hits == 1 else 0, 12,
        "no explicit 'never invent' rule or [NEEDS INPUT] convention")

    # 6. Self-check section (10)
    has = bool(re.search(r"(^##+ .*(self-check|quality checklist|before saving|completeness gate"
                         r"|quality gate|proof audit|before you save|audit before)"
                         r"|\*\*self[- ]check\*\*|^\s*\d+\.\s+\*\*self[- ]check"
                         r"|^\s*self[- ]check:)", body, re.M | re.I))
    items = len(re.findall(r"^\s*[-*] ", body, re.M)) if has else 0
    add("self_check", (6 if has else 0) + (4 if items >= 6 else 2 if items >= 3 else 0), 10,
        "no self-check section")

    # 7. Negative routing in description (8)
    add("routing", 8 if re.search(r"\bsee [a-z-]{3,}\b", desc) else 0, 8,
        "description never says when NOT to fire")

    # 8. Related skills cross-links (6)
    links = {m for m in re.findall(r"`/([a-z][a-z0-9-]{3,})`", body)} - {path.name}
    has_rel = bool(re.search(r"^##+ .*(related skills|companion|follow-ups?)", body, re.M | re.I))
    add("related", 6 if (has_rel and links) else 4 if len(links) >= 2 else 0, 6,
        "no cross-links to sibling skills")

    # 9. Evals (10)
    ev = path / "evals" / "evals.json"
    n = 0
    if ev.exists():
        try:
            n = len(json.loads(ev.read_text()).get("evals", []))
        except Exception:
            n = 0
    add("evals", 10 if n >= 3 else 6 if n >= 1 else 0, 10, f"evals.json missing or thin ({n} cases)")

    # 10. Spec compliance (5)
    bad = keys - SPEC_KEYS - CC_KEYS
    pts = 5 if not bad else 0
    if len(desc) > 1536:
        pts = max(0, pts - 2)
    add("spec", pts, 5, f"non-spec frontmatter keys: {sorted(bad)}" if bad else "description over 1536 chars")

    # 11. Decision support (10) - thresholds, priorities, warnings, not just prose
    d = len(DECISION.findall(full))
    add("decisions", 10 if d >= 6 else 7 if d >= 3 else 3 if d >= 1 else 0, 10,
        "no thresholds, priorities or warning signs - it produces text but makes no calls")

    # 12. Honest limits (5)
    add("limits", 5 if HONEST_LIMITS.search(full) else 0, 5,
        "never states what it could not do or does not know")

    earned = sum(p for p, _ in c.values())
    possible = sum(m for _, m in c.values())
    total = round(100 * earned / possible)
    return total, c, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default="skills")
    ap.add_argument("--min", type=int, default=85)
    ap.add_argument("--detail", action="store_true")
    ap.add_argument("--self-test", action="store_true",
                    help="score hand-labelled fixtures; exit 1 if the TOOL disagrees with a human label")
    a = ap.parse_args()

    if a.self_test:
        cal = json.loads(Path("scripts/skill_quality_calibration.json").read_text())
        bad = 0
        print("Calibration: scoring cases a human already judged.\n")
        for case in cal["cases"]:
            t, c, _ = score(Path(case["skill"]))
            name = Path(case["skill"]).name
            errs = []
            if "min" in case and t < case["min"]:
                errs.append(f"scored {t}, human labelled '{case['label']}' (expected >= {case['min']})")
            if "max" in case and t > case["max"]:
                errs.append(f"scored {t}, human labelled '{case['label']}' (expected <= {case['max']})")
            for k in case.get("must_pass", []):
                got, mx = c.get(k, (0, 1))
                if got < mx:
                    errs.append(f"check '{k}' scored {got}/{mx} but the human says this skill has it")
            print(f"  {'FAIL' if errs else 'ok  '}  {name}: {t}/100  ({case['label']})")
            for e in errs:
                print(f"          {e}")
            bad += bool(errs)
        if bad:
            print(f"\nTOOL IS MISCALIBRATED on {bad} case(s). Do NOT act on any score until fixed.")
            print("The instrument is presumed wrong, not the skills.")
            return 1
        print("\nCalibrated. Scores may be acted on.")
        return 0

    root = Path(a.path)
    rows, unmigrated = [], []
    for sm in sorted(root.rglob("SKILL.md")):
        # SCOPE GUARD: this rubric only validly measures skills that adopted the
        # metadata.grounded_in convention. Scoring one that has not is meaningless
        # and produced a 3/100 on a substantial 294-line skill before this guard.
        fmtxt = re.match(r"^---\n(.*?)\n---\n", sm.read_text(), re.S)
        if not fmtxt or "grounded_in:" not in fmtxt.group(1):
            unmigrated.append(sm.parent.name)
            continue
        t, c, notes = score(sm.parent)
        rows.append((t, sm.parent.name, c, notes))
    if unmigrated:
        print(f"  NOT MIGRATED (excluded, no metadata.grounded_in): {len(unmigrated)} skills")
        print(f"  These are not scored and MUST NOT be read as failing.\n")
    if not rows:
        print(f"no migrated skills under {root}. Nothing scored.")
        return 0

    rows.sort()
    band = lambda t: "COMPLETE" if t >= 90 else "OK" if t >= a.min else "GAPS" if t >= 65 else "THIN"
    print(f"Structural hygiene: {root}  (threshold {a.min}/100)")
    print("This is a completeness check, not a quality score. Correlation with blind")
    print("human review measured at 0.17. A pass means nothing obvious is missing.\n")
    for t, name, c, notes in rows:
        print(f"  {t:3d}/100  {band(t):8s}  {name}")
        if a.detail and notes:
            for n in notes:
                print(f"           - {n}")
    fails = [r for r in rows if r[0] < a.min]
    avg = sum(r[0] for r in rows) / len(rows)
    print(f"\n  skills: {len(rows)}   mean: {avg:.1f}   below {a.min}: {len(fails)}")
    if fails:
        print("\nFAIL. Below threshold:")
        for t, name, c, notes in fails:
            print(f"  {name} ({t})")
            for n in notes:
                print(f"     - {n}")
        return 1
    print("\nPASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
