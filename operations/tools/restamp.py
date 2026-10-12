#!/usr/bin/env python3
"""Re-stamp items and content-unit blocks whose text was edited after they were stamped.

Used whenever a reviewer or author changes learner-facing text after the checks passed
(playbook step 6). For every item and block in the topic whose text no longer matches its
authored_hash, this records the old hash as prior_hash, writes the new authored_hash, and adds a
repair_note if one is given. Nothing else is changed. Claim revisions and claims_seen are NOT
handled here: raise a claim's revision by hand, update claims_seen on what cites it, and record
reviewed_unchanged where the citing text needed no change.

    python3 operations/tools/restamp.py work/<workspace> <topic> [--note "why the text changed"] [--dry-run]

Run the checks afterwards: C-30 confirms every stamp is consistent.
"""
import argparse
import glob
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                'standard', 'v0.2.0-draft', 'checks'))
from yyeni_checks import _artefact_text  # noqa: E402  the same text the checks hash


def h(x):
    return hashlib.sha256(_artefact_text(x).encode()).hexdigest()


def dump(path, raw, data):
    lines = raw.split('\n')
    ind = len(lines[1]) - len(lines[1].lstrip(' ')) if len(lines) > 1 else 1
    with open(path, 'w') as fh:
        fh.write(json.dumps(data, indent=ind or 1, ensure_ascii=False) + ('\n' if raw.endswith('\n') else ''))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('workspace')
    ap.add_argument('topic')
    ap.add_argument('--note', default=None, help='repair_note to record on each re-stamped artefact')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    td = os.path.join(a.workspace, 'topics', a.topic)
    if not os.path.isdir(td):
        sys.exit(f'No topic folder {td}')
    changed, unstamped = [], []

    def fix(x, oid):
        new = h(x)
        old = x.get('authored_hash')
        if not old:
            unstamped.append(oid)
            return False
        if old and old != new:
            x['prior_hash'] = old
            x['authored_hash'] = new
            if a.note:
                x['repair_note'] = a.note
            changed.append(oid)
            return True
        return False

    for f in sorted(glob.glob(os.path.join(td, 'learning-items', '*.json'))):
        raw = open(f).read()
        d = json.loads(raw)
        hit = [fix(i, i.get('item_id', '?')) for i in d.get('items', [])]
        if any(hit) and not a.dry_run:
            dump(f, raw, d)
    for f in sorted(glob.glob(os.path.join(td, 'content-units', '*.json'))):
        raw = open(f).read()
        u = json.loads(raw)
        hit = [fix(b, '%s/%s' % (u.get('unit_id', '?'), b.get('block_id', '?'))) for b in u.get('blocks', [])]
        if any(hit) and not a.dry_run:
            dump(f, raw, u)
    print(('would re-stamp' if a.dry_run else 're-stamped'), len(changed), 'artefacts')
    for c in changed:
        print(' ', c)
    if unstamped:
        print(len(unstamped), 'artefacts have no authored_hash at all (never stamped); the author must stamp them:')
        for c in unstamped:
            print(' ', c)


if __name__ == '__main__':
    main()
