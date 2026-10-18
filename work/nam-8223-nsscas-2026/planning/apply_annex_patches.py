#!/usr/bin/env python3
"""Apply the annex-mapping patches (Paper 3 and Papers 1/2) to the by-year evidence files, normalise exam_series to one value per
sitting (so 'distinct series' counts years), and move the six 2025 Paper 1 placeholder records (no topic named in the report) out of
the evidence map into unmapped_2025_p1.json, so every exposure count recomputes from the evidence. Idempotent. Run from the repo root."""
import json, glob, re
W = "work/nam-8223-nsscas-2026/"
ann = {o["objective_id"] for o in json.load(open(W + "curriculum/annexe-objectives.json"))["objectives"]}
patches = {}
for f in ("patch_P3.json", "patch_P1P2.json"):
    for k, v in json.load(open(W + "assessment-evidence/annex-mapping/" + f))["patches"].items(): patches[k] = v
moved, added, touched = [], 0, 0
for f in sorted(glob.glob(W + "assessment-evidence/by-year/evidence_*.json")):
    d = json.load(open(f)); keep = []
    for r in d["records"]:
        if any("PLACEHOLDER" in n.upper() for n in r["notes"]):
            moved.append(r); continue
        r["exam_series"] = "Oct/Nov %d" % r["year"]
        p = patches.get(r["evidence_id"])
        if p:
            new = [i for i in p["add_objective_ids"] if i in ann and i not in r["objective_ids"]]
            if new:
                r["objective_ids"] += new; added += len(new); touched += 1
                r["notes"].append("annex_mapping: by meaning; confidence: %s; %s" % (p["confidence"], p["reason"]))
        keep.append(r)
    d["records"] = keep; json.dump(d, open(f, "w"), indent=1, ensure_ascii=False)
if moved:
    json.dump({"note": "2025 Paper 1 items whose report comment names no topic. Key letter, percentage correct and comment are kept here; they are excluded from the evidence map and every exposure count because no objective could be assigned.", "records": moved}, open(W + "assessment-evidence/unmapped_2025_p1.json", "w"), indent=1, ensure_ascii=False)
print("records touched:", touched, "| annex ids added:", added, "| placeholders moved:", len(moved))
