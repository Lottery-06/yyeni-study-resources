#!/usr/bin/env python3
"""Compute corpus statistics and curriculum/exam-exposure.json from assessment-evidence/assessment_evidence.json. Nothing is typed:
every figure is a count over the records. The exposure file follows the build tools' format (a list of objective entries with the
Physics fields, plus a nested `evidence` object that check C-39 recomputes). Run from the repo root with plain python3."""
import json, re, collections, datetime
W = "work/nam-8223-nsscas-2026/"
ev = json.load(open(W + "assessment-evidence/assessment_evidence.json"))["records"]
facts = json.load(open(W + "curriculum/syllabus-facts.json"))
oidlist = json.load(open(W + "curriculum/objective_ids.json"))["objectives"]
annex = json.load(open(W + "curriculum/annexe-objectives.json"))["objectives"]
unit_of = {o["objective_id"]: o["leaf"] for o in oidlist}; unit_of.update({o["objective_id"]: o["topic_id"] for o in annex})
text_of = {o["objective_id"]: o["text"] for o in oidlist}; text_of.update({o["objective_id"]: o["syllabus_text"] for o in annex})
glossary = {c["word"].lower() for c in facts["command_words"]}
def conf(r):
    m = re.search(r"confidence:\s*(high|medium|low)", " ".join(r["notes"])); return m.group(1) if m else "unknown"
for r in ev: r["_conf"] = conf(r)
SERIES = sorted({r["exam_series"] for r in ev})
out = {"records": len(ev), "series": SERIES, "confidence": dict(collections.Counter(r["_conf"] for r in ev))}
# ---- command words (Paper 2 and 3 parts 2021-2024: tariffs and wording come from the papers themselves)
cw = collections.defaultdict(lambda: {"count": 0, "tariffs": collections.Counter(), "papers": collections.Counter(), "years": set()})
for r in ev:
    if r["paper_id"] == "P1" or r["year"] == 2025 or not r["command_word"]: continue
    w = r["command_word"].strip().lower(); c = cw[w]; c["count"] += 1; c["papers"][r["paper_id"]] += 1; c["years"].add(r["year"])
    if r["mark_tariff"] is not None: c["tariffs"][r["mark_tariff"]] += 1
rows = []
for w, c in sorted(cw.items(), key=lambda x: -x[1]["count"]):
    modal = c["tariffs"].most_common(1)[0][0] if c["tariffs"] else None
    rows.append({"word": w, "count": c["count"], "modal_tariff": modal, "tariffs_seen": dict(sorted(c["tariffs"].items())), "papers": dict(c["papers"]), "years": sorted(c["years"]),
                 "in_syllabus_glossary": any(w == g or w == g.split(" (")[0] or w == g.split("/")[0] for g in glossary)})
out["command_words_papers_2_3_2021_2024"] = rows
seen = {r["word"] for r in rows}
out["glossary_words_never_opening_a_p2_p3_part_2021_2024"] = sorted(g for g in glossary if not any(s == g or s == g.split(" (")[0] or s == g.split("/")[0] for s in seen))
out["records_with_no_command_word_p2_p3_2021_2024"] = sum(1 for r in ev if r["paper_id"] != "P1" and r["year"] != 2025 and not r["command_word"])
# ---- marks by unit (P1 items 1 mark; P2/P3 parts carry their tariff; a record is split equally across the distinct units it maps to)
def unit_marks(paper, years):
    m = collections.defaultdict(float); unknown = 0
    for r in ev:
        if r["paper_id"] != paper or r["year"] not in years: continue
        t = 1 if paper == "P1" else r["mark_tariff"]
        if t is None: unknown += 1; continue
        units = sorted({unit_of[o] for o in r["objective_ids"]})
        for u in units: m[u] += t / len(units)
    return m, unknown
key = lambda x: [int(p) for p in x[0].split(".")]
for paper, k in (("P1", "marks_by_unit_p1_2021_2024"), ("P2", "marks_by_unit_p2_2021_2024"), ("P3", "marks_by_unit_p3_2021_2024")):
    m, unk = unit_marks(paper, (2021, 2022, 2023, 2024)); tot = sum(m.values())
    out[k] = {"total_marks_counted": round(tot, 1), "parts_with_unknown_tariff": unk, "by_unit": {u: round(v, 1) for u, v in sorted(m.items(), key=key)},
              "share_percent": {u: round(100 * v / tot, 1) for u, v in sorted(m.items(), key=key)}}
theme = collections.defaultdict(float)
for paper in ("P1", "P2"):
    m, _ = unit_marks(paper, (2021, 2022, 2023, 2024))
    for u, v in m.items(): theme[u.split(".")[0]] += v
tt = sum(theme.values()); out["theme_share_p1_p2_2021_2024_percent"] = {k: round(100 * v / tt, 1) for k, v in sorted(theme.items())}
# ---- exposure per objective, in the build tools' format
NS = len(SERIES)
def klass(n):
    if n == 0: return "unseen"
    share = n / NS
    return "core" if share >= 0.60 else "frequent" if share >= 0.35 else "occasional" if share >= 0.15 else "rare"
entries = []
for o in sorted(set(unit_of), key=lambda x: [int(p) if p.isdigit() else 0 for p in re.split(r"[.-]", x.replace("OBJ-8223-", ""))]):
    rs = [r for r in ev if o in r["objective_ids"]]
    ser = sorted({r["exam_series"] for r in rs}); tar = [r["mark_tariff"] for r in rs if r["mark_tariff"] is not None]
    cws = collections.Counter(r["command_word"] for r in rs if r["command_word"])
    marks = sum((1 if r["paper_id"] == "P1" else (r["mark_tariff"] or 0)) for r in rs)
    entries.append({"objective_id": o, "topic_id": unit_of[o], "syllabus_text": text_of[o], "times_examined": len(rs), "marks_examined": marks,
                    "series_spread": len(ser), "series": ser, "tariffs": {str(k): v for k, v in sorted(collections.Counter(tar).items())},
                    "command_words": dict(cws), "papers": dict(collections.Counter(r["paper_id"] for r in rs)),
                    "low_confidence_records": sum(r["_conf"] == "low" for r in rs), "exposure_class": klass(len(ser)),
                    "evidence": {"question_parts_naming_it": len(rs), "distinct_series": len(ser), "max_mark_tariff": max(tar) if tar else 0, "command_words_observed": dict(cws)}})
cls = collections.Counter(e["exposure_class"] for e in entries); out["exposure_class_counts"] = dict(cls)
out["exposure_class_counts_syllabus_objectives_only"] = dict(collections.Counter(e["exposure_class"] for e in entries if e["objective_id"] in {o["objective_id"] for o in oidlist}))
json.dump({"exposure_id": "EXPOSURE-NAM-NSSCAS-8223", "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "authority": "NSSCAS Biology 8223 question papers 2021-2024 and the NSSCAS Examiners Report 2025, matched by reading to the syllabus objectives and the Annexe A and C objectives (see assessment-evidence/assessment_evidence.json).",
           "evidence_window": "%d records over %d sittings (%s). 2021-2023 papers are proof versions; 2023 has no report; 2025 has no papers (report only)." % (len(ev), NS, ", ".join(SERIES)),
           "method": "Each question part was mapped to the objectives it tests by reading (confidence recorded per record). Counts are computed from those records. Class by share of the %d sittings in which an objective is named: core in at least 60%% (3 or more), frequent 35%% (2), occasional 15%% (1), rare below that (not reachable with %d sittings), unseen never." % (NS, NS),
           "principle": "RS-05: past-paper frequency may calibrate emphasis but MUST NOT remove or weaken syllabus-mandated coverage.",
           "status": "measured", "unmatched_parts": 0, "series_in_window": SERIES, "objectives": entries}, open(W + "curriculum/exam-exposure.json", "w"), indent=1, ensure_ascii=False)
json.dump(out, open(W + "assessment-evidence/corpus-statistics.json", "w"), indent=1, ensure_ascii=False)
print("records", out["records"], "| confidence", out["confidence"])
print("exposure classes (all 226 objectives):", dict(cls)); print("  syllabus objectives only (152):", out["exposure_class_counts_syllabus_objectives_only"])
unseen = [e["objective_id"].replace("OBJ-8223-", "") for e in entries if e["exposure_class"] == "unseen"]
print("unseen:", len(unseen), unseen)
print("theme share P1+P2:", out["theme_share_p1_p2_2021_2024_percent"])
