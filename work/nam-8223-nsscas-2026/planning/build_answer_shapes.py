#!/usr/bin/env python3
"""Build curriculum/answer-shapes.json. Computed parts come from assessment_evidence.json; report-derived conventions carry the
report year and printed page they were read from. Structure only: no mark-scheme wording. Run from the repository root."""
import json, re, collections, statistics, datetime
W = "work/nam-8223-nsscas-2026/"
ev = json.load(open(W + "assessment-evidence/assessment_evidence.json"))["records"]
facts = json.load(open(W + "curriculum/syllabus-facts.json"))
stats = json.load(open(W + "assessment-evidence/corpus-statistics.json"))
NUM = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve".split())}
def points_listed(r):
    for c in r["creditworthy_points"]:
        m = re.search(r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\d+)\s+(?:distinct\s+|marking\s+|creditable\s+|separate\s+)?(?:points?|ideas?|marking points?|criteria)\b", c, re.I)
        if m:
            w = m.group(1).lower(); return NUM.get(w) if w in NUM else int(w)
    return None
rows = collections.defaultdict(list)
for r in ev:
    if r["paper_id"] != "P2" or r["year"] == 2025 or r["mark_tariff"] is None or not r["creditworthy_points"]: continue
    k = points_listed(r)
    if k: rows[(r["command_word"] or "none").lower(), r["mark_tariff"]].append((k, r["evidence_id"]))
by_cw = collections.defaultdict(lambda: {"parts": 0, "points_gt_tariff": 0, "points_eq_tariff": 0, "points_lt_tariff": 0})
allp = []
for (w, t), v in rows.items():
    for k, eid in v:
        b = by_cw[w]; b["parts"] += 1
        b["points_gt_tariff" if k > t else "points_eq_tariff" if k == t else "points_lt_tariff"] += 1
        allp.append((k, t))
shape = {w: dict(v) for w, v in sorted(by_cw.items(), key=lambda x: -x[1]["parts"])}
papers = {p["paper_id"]: {"name": p["name"], "marks": p["marks"], "duration_minutes": p["duration_minutes"], "ao_marks": p["ao_marks"], "syllabus_page": p["source"]["page"], "description": p["description"]} for p in facts["papers"]}
conv = [
 {"convention": "mp numbering", "meaning": "Marking points are numbered; a later point can depend on an earlier one (a point is not credited unless the one it depends on is).", "seen_in_report_years": [2021, 2024, 2025]},
 {"convention": "alternative wording (AW)", "meaning": "A different wording of the same idea earns the same credit.", "seen_in_report_years": [2021, 2022, 2024, 2025]},
 {"convention": "or reverse argument (ora)", "meaning": "The argument made the other way round earns the same credit.", "seen_in_report_years": [2021]},
 {"convention": "accept / reject / ignore lists", "meaning": "Some answers are explicitly accepted, rejected or ignored (2025 uses A and R prefixes); a reject on a wrong word can cancel an otherwise right answer.", "seen_in_report_years": [2021, 2022, 2024, 2025]},
 {"convention": "maximum cap per category", "meaning": "Marks from one group of points are capped (for example a maximum of 2 for the explanation, or 1 for only listing stages).", "seen_in_report_years": [2024, 2025]},
 {"convention": "error carried forward (ecf)", "meaning": "A wrong answer in one part is not penalised again where it feeds a later part that is otherwise correct.", "seen_in_report_years": [2021, 2024, 2025]},
 {"convention": "list rule", "meaning": "Where a question asks for a number of items, only the first answers on the answer lines are marked.", "seen_in_report_years": [2021], "verified_page": "2021 report printed p.38"},
 {"convention": "any valid point (AVP)", "meaning": "A creditworthy point not on the scheme can earn a mark.", "seen_in_report_years": [2021]},
]
conv_note = "Years come from a count of these conventions inside each report's Biology section (page ranges not asserted except where a verified_page is given)."
style = [
 {"rule": "Answer describe, explain, suggest, discuss, give a reason and outline questions in full sentences; use bullet points only when asked to list or state.", "seen": {"2021": "report printed p.37", "2022": "report printed p.42", "2024": "report printed p.39 (bullets)", "2025": "report printed p.43"}, "verified_pages": True},
 {"rule": "Use the number of marks to decide how many steps or reasons to give.", "seen": "syllabus section 10, printed p.26"},
 {"rule": "Refer to the data given at least once, with the unit, to reach the top mark on a data question.", "seen": {"2025": "report printed p.46"}, "verified_pages": True},
 {"rule": "Terminology and spelling are credited: a misspelled or wrong term (for example 'PH' for pH) can lose the mark.", "seen": {"2024": "report printed p.39", "2025": "report printed p.43 and p.50"}, "verified_pages": True},
 {"rule": "Answer the question set: describing a graph is not explaining it; naming a stage is not giving its reason.", "seen": {"2022": "Biology Paper 2 and 3 commentary", "2025": "Biology Paper 2 and 3 commentary"}, "verified_pages": False},
]
out = {"_provenance": {"derived_from": "assessment_evidence.json (404 records from papers 2021-2024 and the 2025 report), the syllabus facts, and the printed pages of the 2021, 2022, 2024 and 2025 NSSCAS examiners reports cited per entry", "derivation_policy": "structure only. No mark-scheme or report wording is reproduced in learner-facing output.",
       "validation": "Computed parts are counts over the evidence file. 'points listed' is read from the evidence records' own descriptions of each part's marking points (n=%d parts with a readable count); it is a count of ideas on the scheme, not a quote." % len(allp),
       "limits": "2023 has no scheme, so contributes no shape. 2025 has few stated tariffs and no command words. 2021 Paper 3 and some 2022 and 2024 Paper 3 parts have schemes with a different number of points than their tariff (flagged in the evidence notes)."},
       "8223": {"subject": "NSSCAS Biology 8223", "paper_architecture": papers,
       "points_vs_tariff_paper_2_2021_2024_by_command_word": shape,
       "points_vs_tariff_overall": {"parts": len(allp), "more_points_than_marks": sum(k > t for k, t in allp), "equal": sum(k == t for k, t in allp), "fewer": sum(k < t for k, t in allp)},
       "command_word_tariffs_papers_2_3_2021_2024": stats["command_words_papers_2_3_2021_2024"],
       "mark_scheme_conventions": conv, "mark_scheme_conventions_note": conv_note, "answer_style_rules_from_reports": style}}
json.dump(out, open(W + "curriculum/answer-shapes.json", "w"), indent=1, ensure_ascii=False)
print("parts with a readable points count:", len(allp), out["8223"]["points_vs_tariff_overall"])
for w, v in list(shape.items())[:8]: print(" ", w, v)
