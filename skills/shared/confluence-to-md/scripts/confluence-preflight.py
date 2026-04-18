#!/usr/bin/env python3
"""
Confluence Pre-Push Preflight Check
====================================

Guards against overwriting manual edits on Confluence. Before pushing a local
.md file to an EXISTING Confluence page, run this script to detect whether
anyone has edited that page directly on Confluence since your last sync.

What this script does (in plain language):
1. Finds the project root (walks up from the local .md file)
2. Creates the snapshot directory `.local/confluence-snapshots/` if missing
3. Fetches the CURRENT Confluence page (via confluence-to-md.py) to a temp file
4. Loads the LAST-KNOWN snapshot at `.local/confluence-snapshots/<page_id>.md`
5. Compares:
   - If snapshot exists: 3-way diff — YOUR changes (local vs snapshot) vs
     THEIR changes (confluence vs snapshot). If "their changes" is non-empty,
     you would overwrite manual edits by pushing. STOP and merge first.
   - If snapshot missing: 2-way diff (local vs confluence). Prints a warning
     that no baseline exists — the first push/pull auto-creates one.
6. Exits 0 if safe to push, 1 if conflicts detected, 2 on error

Usage:
    python3 confluence-preflight.py <page_id> <local.md>
    python3 confluence-preflight.py <page_id> <local.md> --show-diff
    python3 confluence-preflight.py <page_id> <local.md> --force   # override

Snapshots are auto-saved by md-to-confluence.py (after push) and
confluence-to-md.py (after pull). This script only reads snapshots.
"""

import argparse
import difflib
import subprocess
import sys
import tempfile
from pathlib import Path


def find_project_root(start):
    """Walk up from `start` to find a directory containing .env or .git."""
    current = Path(start).resolve()
    if current.is_file():
        current = current.parent
    for _ in range(10):
        if (current / '.env').exists() or (current / '.git').exists():
            return current
        if current.parent == current:
            break
        current = current.parent
    return Path.cwd()


def ensure_snapshot_dir(project_root):
    """Create .local/confluence-snapshots/ if missing. Returns the path."""
    snap_dir = project_root / '.local' / 'confluence-snapshots'
    snap_dir.mkdir(parents=True, exist_ok=True)
    return snap_dir


def fetch_remote_to_temp(page_id):
    """Run confluence-to-md.py to fetch the remote page into a temp file.
    Returns path to the fetched .md, or None on failure.

    Looks for confluence-to-md.py in two possible locations (since this
    preflight script lives in BOTH skill folders):
    1. Same scripts/ directory (when preflight is in confluence-to-md/scripts/)
    2. Sibling skill's scripts/ directory (when preflight is in md-to-confluence/scripts/)
    """
    this_script = Path(__file__).resolve()
    candidates = [
        this_script.parent / 'confluence-to-md.py',
        this_script.parent.parent.parent / 'confluence-to-md' / 'scripts' / 'confluence-to-md.py',
    ]
    sibling = next((c for c in candidates if c.exists()), None)
    if not sibling:
        print(f"ERROR: confluence-to-md.py not found in any of: {candidates}")
        return None

    tmp_dir = Path(tempfile.mkdtemp(prefix=f'preflight-{page_id}-'))
    tmp_md = tmp_dir / f'{page_id}.md'

    print(f"Fetching current Confluence page {page_id}...")
    result = subprocess.run(
        ['python3', str(sibling), page_id, str(tmp_md)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"ERROR: confluence-to-md.py failed:\n{result.stderr}")
        return None
    if not tmp_md.exists():
        print(f"ERROR: expected output at {tmp_md} but not created")
        return None
    return tmp_md


def normalize_md(text):
    """Remove noise that causes false-positive diffs.

    - Strip trailing whitespace on every line
    - Drop the '> Source: [Confluence](...)' line (local-only reference)
    - Collapse 3+ consecutive blank lines to 2
    """
    lines = [l.rstrip() for l in text.splitlines()]
    lines = [l for l in lines if not l.lstrip().startswith('> Source: [Confluence]')]
    out = []
    blank_count = 0
    for l in lines:
        if l == '':
            blank_count += 1
            if blank_count <= 2:
                out.append(l)
        else:
            blank_count = 0
            out.append(l)
    return '\n'.join(out)


def compute_diff(a_text, b_text, a_name, b_name):
    """Return unified diff of a → b (empty string if identical after normalize)."""
    a_lines = normalize_md(a_text).splitlines(keepends=True)
    b_lines = normalize_md(b_text).splitlines(keepends=True)
    diff = list(difflib.unified_diff(a_lines, b_lines, fromfile=a_name, tofile=b_name, n=3))
    return ''.join(diff)


def summarize_diff(diff_text):
    """Count added/removed lines in a unified diff output."""
    added = sum(1 for l in diff_text.splitlines()
                if l.startswith('+') and not l.startswith('+++'))
    removed = sum(1 for l in diff_text.splitlines()
                  if l.startswith('-') and not l.startswith('---'))
    return added, removed


def main():
    parser = argparse.ArgumentParser(description='Confluence pre-push preflight check')
    parser.add_argument('page_id', help='Confluence page ID')
    parser.add_argument('local_md', help='Path to local .md file about to be pushed')
    parser.add_argument('--show-diff', action='store_true',
                        help='Print full unified-diff output')
    parser.add_argument('--force', action='store_true',
                        help='Exit 0 even when conflicts are detected (override)')
    args = parser.parse_args()

    local_path = Path(args.local_md)
    if not local_path.exists():
        print(f"ERROR: Local file not found: {local_path}")
        sys.exit(2)

    project_root = find_project_root(local_path)
    snap_dir = ensure_snapshot_dir(project_root)
    snap_path = snap_dir / f'{args.page_id}.md'

    print(f"Project root: {project_root}")
    print(f"Snapshot dir: {snap_dir}")
    print(f"Snapshot: {snap_path.name} [{'FOUND' if snap_path.exists() else 'MISSING'}]")
    print()

    remote_path = fetch_remote_to_temp(args.page_id)
    if remote_path is None:
        sys.exit(2)

    local_text = local_path.read_text()
    remote_text = remote_path.read_text()

    print()
    print('=' * 60)
    print('PREFLIGHT RESULT')
    print('=' * 60)

    if not snap_path.exists():
        print()
        print('WARNING: NO BASELINE FOUND — cannot precisely detect who edited what.')
        print('         Running 2-way diff (local vs Confluence).')
        print()
        diff = compute_diff(remote_text, local_text, 'confluence', 'local')
        added, removed = summarize_diff(diff)

        if not diff:
            print('OK: Local and Confluence match. Safe to push.')
            print('    (Snapshot will be auto-created after push.)')
            sys.exit(0)

        print(f'Differences: local has +{added} / -{removed} lines vs Confluence')
        print()
        print('Without a baseline, YOU CANNOT TELL which side made the changes.')
        print('Review the diff carefully before pushing. If Confluence has content')
        print('your local .md is missing, MERGE IT IN FIRST.')
        print()
        if args.show_diff:
            print(diff)
        else:
            print('Re-run with --show-diff to see the full diff.')

        sys.exit(0 if args.force else 1)

    # Snapshot exists — 3-way analysis
    snap_text = snap_path.read_text()
    your_changes = compute_diff(snap_text, local_text, 'snapshot', 'local')
    their_changes = compute_diff(snap_text, remote_text, 'snapshot', 'confluence')

    y_add, y_rem = summarize_diff(your_changes)
    t_add, t_rem = summarize_diff(their_changes)

    print()
    print(f'YOUR CHANGES   (local vs snapshot):      +{y_add} / -{y_rem} lines')
    print(f'THEIR CHANGES  (confluence vs snapshot): +{t_add} / -{t_rem} lines')
    print()

    if not their_changes:
        print('OK: No changes on Confluence since last sync. Safe to push.')
        sys.exit(0)

    print('STOP: Confluence has been edited since your last sync.')
    print('      Pushing now would OVERWRITE those edits.')
    print()
    if args.show_diff:
        print('--- THEIR CHANGES (confluence vs snapshot) ---')
        print(their_changes)
        print()
        if your_changes:
            print('--- YOUR CHANGES (local vs snapshot) ---')
            print(your_changes)
    else:
        print('Re-run with --show-diff to see both diffs.')
    print()
    print('Suggested workflow:')
    print(f'  1. Pull the latest Confluence page to a temp file:')
    print(f'     python3 .claude/skills/confluence-to-md/scripts/confluence-to-md.py \\')
    print(f'       {args.page_id} /tmp/latest-{args.page_id}.md')
    print(f'  2. Diff /tmp/latest-{args.page_id}.md against {local_path}')
    print(f'  3. Merge the Confluence-side additions into {local_path}')
    print(f'  4. Re-run this preflight — should show no "THEIR CHANGES"')
    print(f'  5. Push.')

    sys.exit(0 if args.force else 1)


if __name__ == '__main__':
    main()
