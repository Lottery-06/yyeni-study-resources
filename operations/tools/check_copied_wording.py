#!/usr/bin/env python3
"""Find learner-facing text that repeats wording from exam papers, mark schemes or examiner reports.

Used at playbook step 6 (cross-review). Official assessment material is mine-do-not-reproduce:
a run of 12 or more identical words is a defect, a run of 8 to 11 is reviewed by eye.

    python3 operations/tools/check_copied_wording.py work/<workspace> <source> [<source> ...]

<source> is a PDF, a .txt file, or a folder searched recursively for both. Pass ONLY the subject's
question papers, mark schemes and examiner reports (for example sources/<board>/<level>/<code>-<subject>/assessment/).
Do NOT pass the syllabus: learner text is meant to use the syllabus's own terms. Files with
"syllabus" in their name are skipped as a safety net, but a syllabus without that word is not.

Learner-facing text checked: every item's prompt, canonical answer and marking guidance, every
content-unit block's heading and text, and every practice text under topics/<T>/texts/.

Exit code 0 when no run reaches 12 words, 1 otherwise. A report is printed and also written to
work/<workspace>/review/copied-wording.md.
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys

N = 8          # shortest run reported
DEFECT = 12    # a run this long is a defect
WORD = re.compile(r"[a-z0-9]+")


def words(text):
    return WORD.findall(text.lower())


def pdf_text(path):
    """Text of a PDF. Two-column papers read differently in layout and raw modes, so use both."""
    out = []
    if shutil.which('pdftotext'):
        for mode in (['-layout'], ['-raw']):
            try:
                out.append(subprocess.run(['pdftotext', *mode, path, '-'], capture_output=True,
                                          text=True, timeout=120).stdout)
            except Exception:
                pass
    if not any(o.strip() for o in out):
        try:
            from pypdf import PdfReader
            out.append('\n'.join(p.extract_text() or '' for p in PdfReader(path).pages))
        except Exception as e:
            print(f'  could not read {path}: {e}', file=sys.stderr)
    return '\n'.join(out)


def source_files(paths):
    for p in paths:
        if os.path.isdir(p):
            for f in sorted(glob.glob(os.path.join(p, '**', '*'), recursive=True)):
                if f.lower().endswith(('.pdf', '.txt')):
                    yield f
        elif os.path.isfile(p):
            yield p


def source_grams(paths):
    grams, n_files = set(), 0
    for f in source_files(paths):
        text = pdf_text(f) if f.lower().endswith('.pdf') else open(f, errors='ignore').read()
        if 'syllabus' in os.path.basename(f).lower():
            print(f'  skipped (looks like a syllabus): {f}', file=sys.stderr)
            continue
        w = words(text)
        grams.update(tuple(w[i:i + N]) for i in range(len(w) - N + 1))
        n_files += 1
    return grams, n_files


def learner_texts(ws):
    for f in sorted(glob.glob(os.path.join(ws, 'topics', '*', 'learning-items', '*.json'))):
        for it in json.load(open(f)).get('items', []):
            g = it.get('marking_guidance') or []
            parts = [it.get('prompt') or '', it.get('canonical_answer') or ''] + ([g] if isinstance(g, str) else list(g))
            yield f, it.get('item_id', '?'), '\n'.join(parts)
    for f in sorted(glob.glob(os.path.join(ws, 'topics', '*', 'content-units', '*.json'))):
        u = json.load(open(f))
        for b in u.get('blocks', []):
            yield f, '%s/%s' % (u.get('unit_id', '?'), b.get('block_id', '?')), (b.get('heading') or '') + '\n' + (b.get('text') or '')
    for f in sorted(glob.glob(os.path.join(ws, 'topics', '*', 'texts', '*.md'))):
        yield f, os.path.basename(f), open(f).read()


def runs(text, grams):
    """Maximal runs of consecutive words, at least N long, whose every 8-word window occurs in the sources."""
    w = words(text)
    hit = [tuple(w[i:i + N]) in grams for i in range(len(w) - N + 1)]
    out, i = [], 0
    while i < len(hit):
        if hit[i]:
            j = i
            while j + 1 < len(hit) and hit[j + 1]:
                j += 1
            out.append((j - i + N, ' '.join(w[i:j + N])))
            i = j + 1
        else:
            i += 1
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('workspace')
    ap.add_argument('sources', nargs='+')
    a = ap.parse_args()
    ws = a.workspace.rstrip('/')
    grams, n_files = source_grams(a.sources)
    if not n_files:
        sys.exit('No source PDFs or .txt files found in the paths given.')
    found = []
    for f, oid, text in learner_texts(ws):
        for length, run in runs(text, grams):
            found.append((length, os.path.relpath(f, ws), oid, run))
    found.sort(key=lambda x: -x[0])
    defects = [x for x in found if x[0] >= DEFECT]
    L = [f'# Copied wording check: {os.path.basename(ws)}', '',
         f'{n_files} source files; {len(found)} runs of {N}+ words; {len(defects)} of {DEFECT}+ words (defects).', '',
         f'Runs of {DEFECT}+ words must be reworded unless they are a standard definition or formula; say which you allowed.',
         f'Runs of {N}-{DEFECT - 1} words: read each; reword any that copy an exam\'s phrasing rather than standard terminology.', '',
         '| words | file | id | run |', '|---:|---|---|---|']
    L += [f'| {n} | {f} | {oid} | {r} |' for n, f, oid, r in found]
    report = '\n'.join(L) + '\n'
    os.makedirs(os.path.join(ws, 'review'), exist_ok=True)
    open(os.path.join(ws, 'review', 'copied-wording.md'), 'w').write(report)
    print(report if len(found) <= 60 else '\n'.join(L[:8 + 60]) + f'\n... {len(found) - 60} more in review/copied-wording.md')
    sys.exit(1 if defects else 0)


if __name__ == '__main__':
    main()
