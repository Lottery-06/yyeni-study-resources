#!/usr/bin/env python3
"""Merge assessment-evidence/by-year/evidence_<year>.json into assessment-evidence/assessment_evidence.json and validate.
Run from the repository root with plain python3 (needs jsonschema)."""
import json, glob, sys, collections
import jsonschema
W = "work/nam-8223-nsscas-2026/"
schema = json.load(open("standard/v0.2.0-draft/schemas/assessment_evidence.schema.json"))
ids = {o["objective_id"] for o in json.load(open(W + "curriculum/objective_ids.json"))["objectives"]} | {o["objective_id"] for o in json.load(open(W + "curriculum/annexe-objectives.json"))["objectives"]}
recs, problems = [], []
for f in sorted(glob.glob(W + "assessment-evidence/by-year/evidence_*.json")):
    d = json.load(open(f)); recs += d["records"]
seen = collections.Counter(r["evidence_id"] for r in recs)
problems += ["duplicate evidence_id " + k for k, v in seen.items() if v > 1]
for r in recs:
    bad = [o for o in r["objective_ids"] if o not in ids]
    if bad: problems.append("unknown objective ids in %s: %s" % (r["evidence_id"], bad))
merged = {"map_id": "ASSESS-NAM-NSSCAS-8223-2021-2025", "status": "partial", "records": recs}
errs = list(jsonschema.Draft202012Validator(schema).iter_errors(merged))
problems += ["schema: %s %s" % (list(e.path)[:3], e.message[:90]) for e in errs[:10]]
if problems:
    print("\n".join(problems)); sys.exit(1)
json.dump(merged, open(W + "assessment-evidence/assessment_evidence.json", "w"), indent=1, ensure_ascii=False)
by = collections.Counter((r["year"], r["paper_id"]) for r in recs)
print("merged", len(recs), "records")
for k in sorted(by): print(" ", k, by[k])
print("tariff sums by year/paper (P2,P3 parts; P1 items are 1 mark):")
t = collections.defaultdict(int)
for r in recs:
    if r["mark_tariff"] is not None: t[(r["year"], r["paper_id"])] += r["mark_tariff"]
for k in sorted(t): print(" ", k, t[k])
