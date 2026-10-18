#!/usr/bin/env python3
"""Generate qualification-profile.yaml, curriculum/assessment-framework.json, curriculum/glossary.json and curriculum/unit_titles.json
from curriculum/syllabus-facts.json and assessment-evidence/corpus-statistics.json. Syllabus values are copied, not retyped; the
framework's command-word usage is computed. Judgement fields are marked. Run from the repository root with plain python3."""
import json, yaml, datetime, re
W = "work/nam-8223-nsscas-2026/"
f = json.load(open(W + "curriculum/syllabus-facts.json")); st = json.load(open(W + "assessment-evidence/corpus-statistics.json"))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
# ------------------------------------------------------------------ qualification profile
aos = [{"code": a["code"], "name": a["name"], "description": "; ".join("%s %s" % (c["code"], c["text"]) for c in a["can_do"]) + ".", "qualification_weight_percent": a["qualification_weight_percent"]} for a in f["assessment_objectives"]]
papers = []
for p in f["papers"]:
    papers.append({"paper_id": p["paper_id"], "name": p["name"], "duration_minutes": p["duration_minutes"], "marks": p["marks"], "qualification_weight_percent": p["weight_percent_printed_table"],
                   "question_basis": p["description"], "sections": [p["description"]],
                   "assessment_objective_weights": {k: round(100 * v / p["marks"]) for k, v in p["ao_marks"].items() if v}})
cwords = [{"word": c["word"], "meaning": c["meaning"]} for c in f["command_words"]]
qual = {"profile_id": "nied-8223-nsscas-2021-2025-v1", "version": "0.2.0-draft", "status": "draft",
        "board": "Namibia: syllabus by the National Institute for Educational Development (NIED), Ministry of Education, Arts and Culture; examinations set by the Directorate of National Examinations and Assessment (DNEA); approved by the National Examination, Assessment and Certification Board (NEACB)",
        "qualification": "Namibia Senior Secondary Certificate Advanced Subsidiary level (NSSCAS)", "subject": "Biology", "syllabus_code": "8223", "examination_years": [2021, 2022, 2023, 2024, 2025],
        "syllabus_version": "NIED 2020", "selected_level": "NSSCAS Advanced Subsidiary Level (Grade 12)",
        "route": {"route_id": "NSSCAS_AS", "name": "NSSCAS Biology, Papers 1, 2 and 3 (all compulsory)", "included_paper_ids": ["P1", "P2", "P3"], "excluded_paper_ids": [],
                  "notes": "All learners sit Papers 1, 2 and 3 (syllabus p.22). Grades a to e. NSSCO Biology (6116) is a separate qualification."},
        "language": "English", "guided_learning_hours": 180,
        "learner_entry_assumptions": ["NSSCO Biology is recommended prior learning, not a stated entry requirement (syllabus p.3)."],
        "key_concepts": ["Cellular organisation and membranes", "Biological molecules and enzymes", "Transport in plants and mammals", "Defence against disease", "Cell division and the continuity of genetic information", "Practical and mathematical skills"],
        "papers": papers, "assessment_objectives": aos, "command_words": cwords,
        "scope": {"included_topic_ids": [t["id"] for t in f["content_outline"] if t["is_leaf"]] + ["4.1", "4.2", "4.3", "4.4", "5.1", "5.2", "5.3"], "excluded_topic_ids": [], "optional_routes": []},
        "source_authority": {"curricular": ["NSSCAS Biology Syllabus 8223 (NIED 2020). Highest authority for scope and objective wording."],
                             "assessment": ["Papers 1-3 for 2021-2024 (2021-2023 are proof versions) and the NSSCAS Examiners Reports for 2021, 2022, 2024 and 2025 (2023 not held). No standalone mark schemes and no revision notes are held."],
                             "conceptual": ["None held: no NSSCAS Biology revision notes or approved teaching source exist in the repository. Content is authored from the syllabus and the assessment evidence, and every claim needs two sources before it can publish."],
                             "conflict_rule": "Syllabus decides scope; official assessment material decides assessment expectations; YYeni classroom curriculum never overrides the syllabus."},
        "notes": ["Topics 1.1 to 3.2.2 are the syllabus's own learning content. Topics 4.1 to 4.4 (Paper 3 practical skills, from Annexe A) and 5.1 to 5.3 (mathematical skills, from Annexe C) are our grouping of the syllabus's stated expectations.",
                  "Weights are as printed. The syllabus states three conflicting paper weightings and says the grid is only 'a general idea' that 'may vary slightly' (p.23); see curriculum/syllabus-facts.json conflicts_and_qualifiers. AO weights printed 40/40/20; the grid's marks give 35.7/35.7/28.6.",
                  "The Lincoln index is cited in objective 1.2 but not given in Annexe C. Simpson's index is printed as D = 1 - (sum of n/N) squared, which differs from the standard form; recorded as printed (syllabus-facts.json formulas_as_printed).",
                  "Source-use permission for this workspace is not yet recorded."]}
open(W + "qualification-profile.yaml", "w").write("# Generated by planning/build_profiles.py from curriculum/syllabus-facts.json (2026-10-18). Weights as printed; see notes.\n" + yaml.safe_dump(qual, sort_keys=False, allow_unicode=True, width=1000))
# ------------------------------------------------------------------ assessment framework
cwst = {r["word"]: r for r in st["command_words_papers_2_3_2021_2024"]}
# P2-only modal tariffs: the exact tariff a Paper 2 question word carries (Paper 3 verbs are practical instructions)
import collections
ev = json.load(open(W + "assessment-evidence/assessment_evidence.json"))["records"]
p2t = collections.defaultdict(collections.Counter)
for r in ev:
    if r["paper_id"] == "P2" and r["year"] != 2025 and r["command_word"] and r["mark_tariff"] is not None: p2t[r["command_word"].lower()][r["mark_tariff"]] += 1
glossary_words = ["Define", "State", "List", "Explain", "Give", "Describe", "Discuss", "Outline", "Deduce", "Predict", "Comment", "Suggest", "Find", "Calculate", "Measure", "Determine", "Estimate", "Show", "Sketch", "Construct", "Compare", "Recognise", "Classify"]
observed_extra = ["Name", "Identify", "Use", "Complete", "Plot", "Make", "Prepare", "Draw", "Record", "Look", "Fill", "Take", "Move"]
PROMPT_OK = {"describe", "explain", "state", "name", "suggest", "identify", "outline", "calculate", "discuss", "compare"}
PRIMARY_AO = {"state": ["A"], "name": ["A"], "describe": ["A", "B"], "explain": ["A", "B"], "outline": ["A"], "identify": ["A"], "suggest": ["B"], "calculate": ["B"], "discuss": ["B"], "compare": ["A", "B"]}
gloss = {c["word"].lower().split(" (")[0].split("/")[0].strip(): c for c in f["command_words"]}
gloss["give"] = gloss.get("give a reason", gloss.get("give", None)) or gloss.get("give a reason")
cw = []
for w in glossary_words + observed_extra:
    key = w.lower(); obs = cwst.get({"fill": "fill in"}.get(key, key))
    modal = None
    if key in p2t and p2t[key]: modal = p2t[key].most_common(1)[0][0]
    elif obs and obs["modal_tariff"] is not None: modal = obs["modal_tariff"]
    ent = {"word": w, "in_syllabus_table": key in gloss}
    if key in gloss: ent.update({"meaning": gloss[key]["meaning"], "meaning_provenance": "syllabus, printed p.%d" % gloss[key]["source"]["page"], "syllabus_page": gloss[key]["source"]["page"]})
    ent.update({"primary_assessment_objectives": PRIMARY_AO.get(key, ["C"] if w in ("Plot", "Make", "Prepare", "Draw", "Record", "Look", "Take", "Move", "Fill") else ["B"]), "assessment_objectives_provenance": "judgement",
                "observed_count": obs["count"] if obs else 0, "observed_tariffs": {str(k): v for k, v in (obs["tariffs_seen"] if obs else {}).items()}, "modal_tariff": obs["modal_tariff"] if obs else None,
                "papers": obs["papers"] if obs else {}, "observation_provenance": "corpus: Paper 2 and 3 parts 2021-2024 (assessment_evidence.json)",
                "verdict": "primary" if obs and obs["count"] >= 8 else "occasional" if obs and obs["count"] >= 3 else "rare" if obs else "listed_not_used",
                "use_in_prompts": key in PROMPT_OK, "exact_mark_tariff": modal, "used_at_level": bool(obs)})
    cw.append(ent)
subs = [("DEF", ["A", "B", "C"], "A definition or statement of a fact, stated precisely with the key terms", "Remember"), ("FEATURE", ["A", "B", "C"], "The features, parts or properties of a structure, with what each does", "Remember"),
        ("DIST", ["A", "B", "C"], "The difference between two confusable terms or structures", "Understand"), ("PROC", ["A", "B", "C"], "An ordered sequence: stages of a process or the steps of a method", "Apply"),
        ("WHY", ["A", "B", "C"], "The reason for a step, a structure or a condition", "Understand"), ("MECH", ["A", "B", "C"], "How something happens, explained biologically", "Understand"),
        ("LIM", ["A", "B", "C"], "A limitation or source of error in a procedure and what it does to the result", "Analyse"), ("APP", ["A", "B", "C"], "Using an idea on a given case, data set, diagram or specimen", "Apply"),
        ("CHAIN", ["A", "B", "C"], "A cause traced through to its consequence in several steps", "Analyse"), ("EVAL", ["A", "B", "C"], "Judging a claim, method or conclusion against evidence and giving a justified decision", "Evaluate"),
        ("CALC", ["A", "B", "C"], "A calculation with the equation, substitution, answer, unit and sensible significant figures", "Apply"), ("INTERP", ["A", "B", "C"], "Reading a graph, table, diagram or micrograph for a value, pattern or conclusion", "Analyse"),
        ("MISCON", ["A", "B", "C"], "Telling a correct idea from the error it is confused with", "Understand"), ("SYNTH", ["A", "B", "C"], "Two objectives joined in one problem", "Create")]
fw = {"framework_id": "FRAMEWORK-NAM-NSSCAS-8223", "generated_at": NOW, "generated_by": "planning/build_profiles.py", "authority": "NSSCAS Biology Syllabus 8223 (NIED 2020) and the assessment corpus 2021-2025.",
      "syllabus_facts_ref": "curriculum/syllabus-facts.json", "provenance_rule": "Syllabus values are copied from syllabus-facts.json (printed page cited). Observed counts and tariffs are computed from assessment_evidence.json. Judgement fields are labelled.",
      "evidence_window": "%d records, Papers 1-3, sittings 2021-2025; command words and tariffs from Paper 2 and 3 parts 2021-2024." % st["records"],
      "assessment_objectives": [{"code": a["code"], "name": a["name"], "name_provenance": "syllabus, printed p.%d" % a["source"]["page"], "definition": "; ".join(c["text"] for c in a["can_do"]), "qualification_weight_percent": a["qualification_weight_percent"], "provenance": "syllabus, printed pp.20-21 and 23"} for a in f["assessment_objectives"]],
      "papers": [{"paper": p["paper_id"][1:], "name": p["name"], "marks": p["marks"], "duration_minutes": p["duration_minutes"], "weight_percent": p["weight_percent_printed_table"],
                  "ao_split": {k: round(100 * v / p["marks"]) for k, v in p["ao_marks"].items()}, "structure": p["description"], "provenance": "syllabus, printed pp.22-23"} for p in f["papers"]],
      "command_word_table_source": "syllabus section 10, printed pp.25-26 (24 entries; the multi-word entry 'What do you understand by / What is meant by' is not represented as a single word here)",
      "command_words": cw,
      "ao_mark_budget": {"per_paper_marks": {"P" + p["paper_id"][1:]: p["ao_marks"] for p in f["papers"]}, "weighted_share_percent": {"A": 35.7, "B": 35.7, "C": 28.6}, "stated_qualification_weight_percent": {"A": 40, "B": 40, "C": 20},
                         "arithmetic_note": "Targets use the stated 40/40/20. The grid's marks (A 50, B 50, C 40 of 140) give 35.7/35.7/28.6; the syllabus states the grid is approximate (printed p.23). All AO calculations downstream are marks-equivalent, never item counts."},
      "flashcard_subtype_ao_map": [{"subtype": a, "assessment_objectives": b, "tests": c, "blooms_level": d} for a, b, c, d in subs],
      "flashcard_subtype_ao_map_note": "Permitted AO set per subtype. Which AO an item carries is set by the slot plan (objective type and paper): content topics use A and B, Paper 3 topics C.",
      "blooms_taxonomy": {"scheme": "Revised Bloom's taxonomy (Anderson and Krathwohl).", "why_both": "The assessment objective says what the examination credits. The Bloom level says what the learner is asked to do. Every item carries both.",
                          "levels": [{"level": l, "means": m} for l, m in [("Remember", "Recall a fact, term or list as stated."), ("Understand", "Explain an idea in the learner's own words, or tell it apart from a neighbouring one."), ("Apply", "Use the idea on a case, figure, diagram or specimen the learner has not been given the answer to."), ("Analyse", "Break a situation into parts and trace a cause through to its consequence."), ("Evaluate", "Weigh options against a criterion and reach a justified decision."), ("Create", "Build something new from two or more ideas.")]],
                          "by_subtype": {a: d for a, b, c, d in subs}, "by_performance_task": {"multiple_choice_set": "Apply", "short_answer": "Apply", "calculation": "Apply", "practical_task": "Analyse"}, "required_on_every_item": True},
      "item_mix_target": {"basis": "marks-equivalent", "target_share_percent": {"A": 40, "B": 40, "C": 20}, "note": "Balance the SUBJECT against this, never a single topic."},
      "command_words_in_use": [c["word"] for c in cw if c["used_at_level"]], "command_words_listed_but_never_used": [c["word"] for c in cw if c["in_syllabus_table"] and not c["used_at_level"]],
      "command_words_used_but_not_listed": [c["word"] for c in cw if c["used_at_level"] and not c["in_syllabus_table"]]}
json.dump(fw, open(W + "curriculum/assessment-framework.json", "w"), indent=1, ensure_ascii=False)
# ------------------------------------------------------------------ unit titles
json.dump({"1": "Classification of living organisms", "2": "Organisation and maintenance of the organism", "3": "Development of the organism and the continuity of life", "4": "Practical skills (Paper 3)", "5": "Mathematical skills"}, open(W + "curriculum/unit_titles.json", "w"), indent=1, ensure_ascii=False)
print("qualification profile, framework (%d command words: %d in use, %d never used, %d used but not listed), unit titles written" % (len(cw), len(fw["command_words_in_use"]), len(fw["command_words_listed_but_never_used"]), len(fw["command_words_used_but_not_listed"])))
print("in use:", fw["command_words_in_use"]); print("never used:", fw["command_words_listed_but_never_used"])
print("exact tariffs:", {c["word"]: c["exact_mark_tariff"] for c in cw if c["use_in_prompts"]})
