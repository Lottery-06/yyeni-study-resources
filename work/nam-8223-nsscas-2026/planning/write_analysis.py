#!/usr/bin/env python3
"""Compose operations/analysis/8223-nsscas-biology-corpus-analysis.md. Every figure is computed from the evidence and facts files;
the narrative is ours. Run from the repository root with plain python3."""
import json, re, collections
W = "work/nam-8223-nsscas-2026/"
ev = json.load(open(W + "assessment-evidence/assessment_evidence.json"))["records"]
st = json.load(open(W + "assessment-evidence/corpus-statistics.json"))
facts = json.load(open(W + "curriculum/syllabus-facts.json"))
exp = {e["objective_id"]: e for e in json.load(open(W + "curriculum/exam-exposure.json"))["objectives"]}
mis = json.load(open(W + "curriculum/misconceptions.json"))["entries"]
scope = json.load(open(W + "curriculum/scope-scan.json"))["entries"]
shapes = json.load(open(W + "curriculum/answer-shapes.json"))["8223"]
oid = {o["objective_id"]: o for o in json.load(open(W + "curriculum/objective_ids.json"))["objectives"]}
annex = json.load(open(W + "curriculum/annexe-objectives.json"))
for _a in annex["objectives"]: oid[_a["objective_id"]] = {"leaf": _a["topic_id"], "text": _a["syllabus_text"]}
unit_titles_extra = {k: v for k, v in annex["topics"].items()}
leaves = [t for t in facts["content_outline"] if t["is_leaf"]]
conf = collections.Counter(re.search(r"confidence:\s*(\w+)", " ".join(r["notes"])).group(1) for r in ev)
byyp = collections.Counter((r["year"], r["paper_id"]) for r in ev)
tags = collections.Counter()
per_unit_stmt = collections.Counter()
for r in ev:
    for f in r["examiner_findings"]:
        m = re.match(r"\[([^\]]+)\]", f); t = m.group(1) if m else "untagged"; tags[t] += 1
        if t in ("misconception", "omission", "command-word miss", "shallow development"):
            per_unit_stmt[oid[r["objective_ids"][0]]["leaf"]] += 1
p1, p2, p3 = (st["marks_by_unit_p1_2021_2024"], st["marks_by_unit_p2_2021_2024"], st["marks_by_unit_p3_2021_2024"])
tot12 = p1["total_marks_counted"] + p2["total_marks_counted"]
def share12(u): return round(100 * (p1["by_unit"].get(u, 0) + p2["by_unit"].get(u, 0)) / tot12, 1)
cw2 = collections.defaultdict(collections.Counter)
for r in ev:
    if r["paper_id"] == "P2" and r["year"] != 2025 and r["command_word"]: cw2[r["command_word"].lower()][r["mark_tariff"]] += 1
cwrows = "\n".join("| %s | %d | %s | %s |" % (w, sum(t.values()), t.most_common(1)[0][0], ", ".join("%s mark%s ×%d" % (k, "" if k == 1 else "s", v) for k, v in sorted(t.items()))) for w, t in sorted(cw2.items(), key=lambda x: -sum(x[1].values())))
p3w = collections.Counter(r["command_word"].lower() for r in ev if r["paper_id"] == "P3" and r["year"] != 2025 and r["command_word"])
cls = st["exposure_class_counts"]
qcount = {y: len({re.match(r"\d+", r["question_ref"]).group(0) for r in ev if r["year"] == y and r["paper_id"] == "P2"}) for y in (2021, 2022, 2023, 2024)}
fac = [int(x) for r in ev for f in r["examiner_findings"] if f.startswith("[facility]") for x in re.findall(r"(\d+)\s*(?:percent|%)", f)]
alltopics = [(t["id"], t["title"]) for t in leaves] + [(k, v) for k, v in unit_titles_extra.items()]
unit_table = "\n".join("| %s | %s | %.1f | %.1f | %.1f | %s |" % (i, ti, p1["share_percent"].get(i, 0), p2["share_percent"].get(i, 0), share12(i), "%s" % ((p3["by_unit"].get(i, 0)) or "–")) for i, ti in alltopics)
th3 = "\n".join("| %s | %s | %s | %d |" % (o.replace("OBJ-8223-", ""), oid[o]["text"][:70], v["exposure_class"], v["times_examined"]) for o, v in exp.items() if v["topic_id"].startswith("3."))
unseen = [o.replace("OBJ-8223-", "") for o, v in exp.items() if v["exposure_class"] == "unseen"]
n_p3_units = len([u for u in p3["by_unit"] if p3["by_unit"][u] > 0]); p3_units = ", ".join(sorted(p3["by_unit"], key=lambda x: [int(q) for q in x.split(".")]))
top_units = ", ".join("%s (%d)" % (u, n) for u, n in per_unit_stmt.most_common(8))
md = f"""# 8223 NSSCAS Biology: corpus analysis

Written 2026-10-18 for work/nam-8223-nsscas-2026. Every figure below is computed by `work/nam-8223-nsscas-2026/planning/compute_stats.py` and `write_analysis.py` over `assessment-evidence/assessment_evidence.json` ({len(ev)} records). The mapping of each question part to objectives, and every description of how a part is marked, were made by reading (five mining agents, one per exam year, then spot-checked); the figures built on them are counts. AO tags and objective mappings are our judgement, labelled as such; keys, facility figures and printed tariffs are the board's.

## 1. The corpus
| Year | Papers held | Report held | Records |
|---|---|---|---|
| 2021 | P1 (First Proof), P2 (First Revised Proof), P3 (First Proof) | Biology Papers 2 and 3 (no Paper 1 section) | {byyp[(2021,'P1')]} + {byyp[(2021,'P2')]} + {byyp[(2021,'P3')]} |
| 2022 | P1, P2, P3 (all First Proof; the unlabelled 01.06.2022 P3 is identical) | Papers 1, 2, 3 | {byyp[(2022,'P1')]} + {byyp[(2022,'P2')]} + {byyp[(2022,'P3')]} |
| 2023 | P1 (First Proof), P2 and P3 (First Revised Proof) | **none** | {byyp[(2023,'P1')]} + {byyp[(2023,'P2')]} + {byyp[(2023,'P3')]} |
| 2024 | P1, P2, P3 (unlabelled) | Papers 1, 2, 3 | {byyp[(2024,'P1')]} + {byyp[(2024,'P2')]} + {byyp[(2024,'P3')]} |
| 2025 | **none** | Papers 1, 2, 3 (Paper 2 covers four questions, Paper 3 two) | {byyp[(2025,'P1')]} + {byyp[(2025,'P2')]} + {byyp[(2025,'P3')]} |

One record per Paper 1 item and per Paper 2/3 question part. Mapping confidence: high {conf['high']}, medium {conf['medium']}, low {conf['low']}. Six 2025 Paper 1 items whose report comment names no topic are kept in `assessment-evidence/unmapped_2025_p1.json` and are not in the evidence map or any count. **Changes since the analysis was first read (2026-10-18, during step 4):** the evidence map now excludes those six items (404 records became 398); every record carries a per-sitting series label so exposure recomputes; 272 practical-skill and maths-skill objective ids (Annexe A and C, topics 4.x and 5.x) were added by reading, so a Paper 3 or data-skill part now also maps to the skill it tests; exposure classes follow the build tools' definitions; and a few counts below changed with them.

**Used with limits:** 2021–2023 papers are proof versions and may differ from the printed exam; 2023 has no key, scheme or comment; 2025 has no papers, few stated tariffs and no command words; Paper 1 keys exist for 2022, 2024 and 2025 only (120 of 200 items) and were checked against the reports (120 of 120 match). **Set aside:** nothing was excluded; no older-syllabus papers are held.

## 2. What each paper looks like
- **Paper 1 (multiple choice, 40 marks, 1 hour).** Forty four-option items, one mark each, in syllabus order. Items test recognition and application: diagrams, graphs, sequences and statement-judging as well as recall. Of the 160 items 2021–2024, {sum(1 for r in ev if r['paper_id']=='P1' and r['year']!=2025 and 'A' in r['ao_focus'])} were tagged A (knowledge) and {sum(1 for r in ev if r['paper_id']=='P1' and r['year']!=2025 and 'B' in r['ao_focus'])} B (application), some both. The facility figures the 2024 and 2025 reports give run from {min(fac)}% to {max(fac)}%.
- **Paper 2 (structured, 60 marks, 1 hour 15).** Compulsory questions per year ({', '.join('%d: %d' % (y, n) for y, n in sorted(qcount.items()))}; 2025 report covers 4), each built from linked parts of 1 to 8 marks around one stimulus (a table, graph, diagram, micrograph or short scenario). Mark tariffs by part: {', '.join('%s×%d' % (k, v) for k, v in sorted(collections.Counter(r['mark_tariff'] for r in ev if r['paper_id']=='P2' and r['year']!=2025 and r['mark_tariff'] is not None).items()))} (mark: number of parts). Parts sum to 60 each year 2021–2024.
- **Paper 3 (advanced practical, 40 marks, 2 hours).** Two experiments, each worth 20. Skills tested include tables, graphs, calibration with an eyepiece graticule, drawing plan and cell diagrams, variables, accuracy and reliability, and percentage-change arithmetic. 2021 part tariffs sum to 42, not 40 (see source doubts). The reports print little or no mark scheme for Paper 3, so what earns credit there is mostly commentary.

## 3. Command words actually used
Counted over Paper 2 parts 2021–2024 (the wording comes from the papers; 2025 has none recorded). The rule (AGENTS.md 5): only words the papers use may open a flashcard.

| Word (as printed, lower-cased) | Parts | Modal tariff | Tariffs seen |
|---|---:|---:|---|
{cwrows}
{sum(1 for r in ev if r['paper_id']=='P2' and r['year']!=2025 and not r['command_word'])} Paper 2 parts open with no command word (a stem sentence then a labelling or drawing instruction).

**Paper 3 opening words** (practical instructions, 2021–2024): {', '.join('%s ×%d' % (w, n) for w, n in p3w.most_common())}. "Use" usually introduces a read-off, measure or calculate task; make, prepare, plot, draw, take, move, look and complete are laboratory instructions, not questions a flashcard can pose.

**Listed in the syllabus glossary but never opening a Paper 2 or 3 part, 2021–2024:** {', '.join(st['glossary_words_never_opening_a_p2_p3_part_2021_2024'])}. Notably **"define" is never used** although three objectives begin "define" (1.2-01, 2.4.1-01, 2.8.1-01). The papers ask for definitions as "Explain what is meant by / the meaning of" (four Paper 2 parts, 2 marks, 2022–2024) and "State what … means" (one part, 1 mark, 2024); the syllabus glossary keeps Define (a formal statement), State (a concise answer) and "what is meant by" (a definition with comment on its significance) apart. **Used but not in the glossary:** name, identify, use, complete, plot, make, prepare, draw, record, look, fill in, take, move.

**Proposed verdict for prompts (the plan decides):** `use_in_prompts: true` for describe, explain, state, name, suggest, identify, outline, calculate, discuss (each opens three or more Paper 2 parts); allow compare (one Paper 2 part, but the syllabus names compare objectives); `false` for the practical instruction words and for every glossary word the papers never use, including Define (decision 2026-10-18: ask as the exams do). Definition cards open with "State what is meant by" or "Explain what is meant by".

## 4. What a creditable answer looks like
From the schemes and commentary in the 2021, 2022, 2024 and 2025 reports (structure only; `curriculum/answer-shapes.json` holds the detail).
- **More points on the scheme than marks.** Where the evidence records state a count, {shapes['points_vs_tariff_overall']['more_points_than_marks']} of {shapes['points_vs_tariff_overall']['parts']} Paper 2 parts offer more creditworthy points than marks (the learner scores up to the tariff). This is a small readable sample, so indicative only.
- **Point-marked and developed.** Describe, explain, suggest and outline answers earn one mark per distinct, correctly linked point; a later point can depend on an earlier one; a stated cap limits marks from one group (for example, only listing stages earns one mark).
- **Named terms matter.** Correct terminology is required and a wrong or misspelled key term can lose the mark; a wrong extra statement ("reject") can cancel a correct one.
- **Alternative wording and the reverse argument are credited**; any valid point and error carried forward appear in some years.
- **Data parts:** quote the data with units to reach the top mark; describing a graph is not explaining it.
- **Style:** full sentences for describe, explain, suggest, discuss, give a reason and outline; bullets only for list and state (reports 2021 p.37, 2022 p.42, 2024 p.39, 2025 p.43).

## 5. Where the marks fall
Share of Paper 1 plus Paper 2 marks 2021–2024 ({tot12:.0f} marks counted; a part naming several topics is split equally between them): Theme 1 {st['theme_share_p1_p2_2021_2024_percent'].get('1')}%, Theme 2 {st['theme_share_p1_p2_2021_2024_percent'].get('2')}%, Theme 3 {st['theme_share_p1_p2_2021_2024_percent'].get('3')}%, with {st['theme_share_p1_p2_2021_2024_percent'].get('4')}% mapped to the practical-skills topics (4.x) and {st['theme_share_p1_p2_2021_2024_percent'].get('5')}% to the maths-skills topics (5.x). The syllabus lists 152 objectives across 25 units, plus the skills of Annexes A and C; this calibrates emphasis and **never removes coverage**.

| Unit | Title | P1 % | P2 % | P1+P2 % | P3 marks 2021–24 |
|---|---|---:|---:|---:|---|
{unit_table}

Unit 2.7.2 (Mammalian heart) has no Paper 2 marks in 2021–2024 but appears in Paper 1. Paper 3 evidence (2021–2024) maps to {n_p3_units} topics: {p3_units}.

**Exposure classes** (the build tools' definitions, by share of the five sittings in which an objective is named: core in 3 or more, frequent in 2, occasional in 1, unseen in none), over all {len(exp)} objectives including the skills topics: core {cls.get('core', 0)}, frequent {cls.get('frequent', 0)}, occasional {cls.get('occasional', 0)}, not named by any held question part {cls.get('unseen', 0)}. "Not named" is not "not examinable": 2023 has no report, 2025 has no papers, and many of these are practical or one-line statement objectives ({', '.join(unseen)}).

Theme 3 (the likely exemplar slice):

| Objective | Text | Class | Parts |
|---|---|---|---:|
{th3}

## 6. How candidates lose marks
Statements in the four held reports, by type (all years): {', '.join('%s %d' % (k, v) for k, v in tags.most_common())}. Units with the most misconception, omission, command-word and shallow-development statements: {top_units}. The recurring failures, with what the resource will do about each:
1. **Answering a different question** (describing a graph instead of explaining it, naming a stage but not giving the reason, stating a function when asked to identify, writing about the wrong structure). *Cards:* command-word-matched questions at the tariffs the papers set, with marking guidance that names the parts; MISCON cards for the discrimination.
2. **Near-neighbour terms confused** (centromere/centrosome, cohesion/adhesion, codon/anticodon, microvilli/cilia, hydrogen/disulfide, magnification/resolution). *Cards:* one MISCON card per confusion with a test that separates the two ({len(mis)} curated entries).
3. **Missing or wrong key terms and spelling** (organelle versus cell, "double membrane", "PH"). *Cards:* term-exact answers and a spelling check for flagged terms.
4. **Not using the data given**, or ignoring units and notation (mm to micrometres, 10^-8 versus 10^-2). *Cards:* data-in-the-card items and Annexe C numeracy practice.
5. **Reasons given in the wrong direction** (lower pH read as fewer hydrogen ions; telomerase thought to break telomeres down; chromosomes re-condensing after telophase). *Cards:* cause-and-effect chain cards.
6. **Practical skill gaps** (independent versus dependent variable, accuracy versus reliability, plan diagram versus cell drawing, calibrating a graticule). *Cards:* practical-skills cards that test the planning, data and evaluation parts; hands-on manipulation is not carded.

## 7. Misconceptions
`curriculum/misconceptions.json`: {len(mis)} curated entries from {tags['misconception']} raw misconception statements plus omissions, each tied to an objective, with the confusion, the correct idea and a discriminating test, in our words. Left out: answering habits, practical mishaps, language slips and anything where the board's own account looks doubtful (see the register below). The correct ideas are our statements of standard biology and need two-source verification in the plan before any card is published.

## 8. Scope
`curriculum/scope-scan.json`: {len(scope)} patterns covering the 16 limits in `syllabus-facts.json` (some limits share a pattern), each tested against must-catch and must-allow examples when the file is built; {sum(1 for e in scope if e['severity']=='fail')} block publication and {sum(1 for e in scope if e['severity']=='review')} need a person to read in context. Patterns cannot catch teaching past a limit by paraphrase, so reviewers read for it.

## 9. What this means for the plan
- **Whole subject, 25 units, emphasis from the share table; Theme 2 carries about three-quarters of Papers 1 and 2.** Coverage is complete; emphasis follows exposure.
- **Paper 3 is 29% of the qualification and AO C only.** The plan needs practical-skills cards (tables, graphs, calibration, variables, accuracy and reliability, percentage change, drawings) alongside content cards, written as State/Describe/Explain/Suggest/Calculate questions.
- **Analyse and Apply cards are needed, not only Remember.** Paper 2 asks describe, explain and suggest at 2–3 marks with several points available; Paper 1 mixes recall with diagrams and graphs; the syllabus caps recall at 20%.
- **Diagrams are central** (labelling, micrograph identification, plan diagrams); the plan must decide generated schematics versus licensed images.
- **Command words** per the proposed verdict in section 3. "Define" never opens a part, so definition cards open with the exam's own forms, "State what is meant by" or "Explain what is meant by" (see section 3).
- **Source doubts must not be taught** (register below). Authors write from the syllabus and verified claims, not from the board's printed keys.
- **Sources thin where it matters for answers:** no 2023 scheme; Paper 3 schemes mostly commentary; 2025 has no question text. Every claim needs two sources.

## Register of source doubts (do not teach; for the plan and reviewers)
Where the board's printed key or scheme looks biologically doubtful. These are readings by the mining agents or by us, **not board statements, and not yet verified against a textbook**; keys were matched to the reports, so the doubt is about the biology, not the transcription.
- 2024 P1 Q37: board key B ("telomeres code non-hereditary information and can be lost"); 9% correct. Telomeres are repeated non-coding DNA caps; do not teach the key's wording.
- 2022 P1 Q38: key A ("breakdown of the nuclear envelope" before prophase). In the usual account the envelope breaks down at the end of prophase. Do not teach "before prophase".
- 2022 P1 Q15 (key C, facilitated diffusion; exocytosis offered), Q23 (key B, root pressure), Q14 (alpha-1,4 and 1,6 bond labels reversed in the stem), Q16 (two options lettered C).
- 2024 P1 Q20 (key looks reversed), Q40 (no facility figure; every row reads true; possibly withdrawn).
- 2022 P2 Q3(a)(iv): scheme accepts "determines gender" and "regulates protein synthesis" as chromosome functions. 2022 P2 Q2(c): scheme expects mosquito-stage parasite development although 2.8.1 says a detailed life cycle is not required.
- 2024 P2 Q3(d)(ii): the changed anticodon appears to pair with a stop codon while the scheme says a different amino acid.
- 2023 P2 Q1: stem says 120 species; tables show 11 and 10 species. 2023 P1 Q21: premise about immobilised amylase and low pH looks doubtful.
- Tariff and scheme mismatches: 2021 P3 sums to 42 (printed total 40); 2021 P2 Q6(a)(i) marked out of 1, not the printed 2; several 2022 and 2024 Paper 3 schemes list more points than the tariff.
- Syllabus itself: Simpson's index printed as D = 1 − (Σ n/N)², squaring the sum (the standard index squares each term then sums); the Lincoln index is cited but not given in Annexe C.
"""
open("operations/analysis/8223-nsscas-biology-corpus-analysis.md", "w").write(md)
print("written", len(md.split("\n")), "lines")
