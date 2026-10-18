#!/usr/bin/env python3
"""Compose PLAN-8223-nsscas-biology.md and HANDOVER-8223-nsscas-biology.md from curriculum/, the contracts and the work orders.
Every table is computed; the prose is ours. Regenerate, do not edit. Run from the repository root with plain python3."""
import json, glob, os, re, collections, datetime
W = "work/nam-8223-nsscas-2026/"
f = json.load(open(W + "curriculum/syllabus-facts.json")); fw = json.load(open(W + "curriculum/assessment-framework.json"))
st = json.load(open(W + "assessment-evidence/corpus-statistics.json")); mis = json.load(open(W + "curriculum/misconceptions.json"))
scope = json.load(open(W + "curriculum/scope-scan.json")); gl = json.load(open(W + "curriculum/glossary.json"))
reg = json.load(open(W + "curriculum/objective_registry.json"))["objectives"]
papers_of = {o["topic_id"]: o["papers"] for o in reg if o["parent_id"] is None}
topics = []
for c in glob.glob(W + "topics/*/contract.json"):
    t = os.path.basename(os.path.dirname(c)); ct = json.load(open(c)); wo = json.load(open(os.path.dirname(c) + "/work_order.json"))
    mis_slots = sum(1 for s in wo["item_slots"] if s["subtype"] == "MISCON")
    topics.append({"id": t, "title": ct["topic_title"], "papers": "/".join(papers_of[t]), "objs": wo["assessable_objective_count"], "items": wo["planned_item_count"],
                   "words": ct["depth_constraints"]["word_budget"], "marks": wo["marks_equivalent_total"], "mix": wo["planned_ao_mix_by_marks"], "miscon": mis_slots,
                   "tasks": [p["item_type"] for p in wo["performance_tasks"]]})
topics.sort(key=lambda x: [int(p) for p in x["id"].split(".")])
tot_items = sum(t["items"] for t in topics); tot_objs = sum(t["objs"] for t in topics); lo = sum(t["words"]["min"] for t in topics); hi = sum(t["words"]["max"] for t in topics)
tm = sum(t["marks"] for t in topics); share = {a: round(sum(t["mix"][a]["planned_share_percent"] * t["marks"] for t in topics) / tm) for a in "ABC"}
target = fw["ao_mark_budget"]["stated_qualification_weight_percent"]
tabrows = "\n".join("| %s | %s | %s | %d | %d | %s–%s |" % (t["id"], t["title"], t["papers"], t["objs"], t["items"], format(t["words"]["min"], ","), format(t["words"]["max"], ",")) for t in topics)
n_miscon = sum(t["miscon"] for t in topics); n_mcq = sum(t["tasks"].count("multiple_choice_set") for t in topics); n_sa = sum(t["tasks"].count("short_answer") for t in topics); n_prac = sum(t["tasks"].count("practical_task") for t in topics)
aotab = "\n".join("| %s | %s | %d%% | %s | %s | %s |" % (a["code"], "; ".join(c["text"] for c in a["can_do"])[:110] + "…", a["qualification_weight_percent"],
                  *["%d%%" % round(100 * p["ao_marks"][a["code"]] / p["marks"]) for p in f["papers"]]) for a in f["assessment_objectives"])
cwrows = "\n".join("| %s | %s | %d | %s | %s |" % (c["word"], "yes" if c["in_syllabus_table"] else "no (observed)", c["observed_count"], c["modal_tariff"] if c["modal_tariff"] is not None else "–", ", ".join(sorted(c["observed_tariffs"], key=int)) or "–")
                   for c in fw["command_words"] if c["use_in_prompts"])
never = ", ".join(c["word"] for c in fw["command_words"] if not c["use_in_prompts"])
subrows = "\n".join("| %s | %s | %s | %s |" % (s["subtype"], s["tests"], ", ".join(s["assessment_objectives"]), s["blooms_level"]) for s in fw["flashcard_subtype_ao_map"])
scoperows = "\n".join("  - %s (syllabus, printed p.%s, %s)" % (e["construct"], e["source"]["printed_page"], e["source"]["topic"]) for e in scope["entries"])
allowed = ", ".join(c["word"] for c in fw["command_words"] if c["use_in_prompts"])
exemplar_note = "`exemplar/3.1.2` (a content topic) and `exemplar/4.3` (a practical slice)"
today = "18 October 2026"
plan = f"""# Plan: Namibia NSSCAS Biology 8223

The brief an authoring agent works to. Generated {today} from `work/nam-8223-nsscas-2026/curriculum/`, the contracts and the topic work orders; regenerate rather than edit (`planning/write_plan.py`). The analysis it rests on is `operations/analysis/8223-nsscas-biology-corpus-analysis.md`; the syllabus brief is `operations/analysis/8223-nsscas-biology-syllabus-brief.md`.

## 0. What the syllabus says
Transcribed from the NIED 2020 syllabus, every value with its printed page (`curriculum/syllabus-facts.json`, checked by `planning/verify_syllabus_facts.py`).

| AO | what it covers (start) | weight | Paper 1 | Paper 2 | Paper 3 |
|---|---|---:|---:|---:|---:|
{aotab}

- **Paper 1, Theory: multiple choice.** 40 marks, 1 hour, 29% of the qualification (printed table). Forty four-choice items on the specific objectives, AO A and B.
- **Paper 2, Theory: structured questions.** 60 marks, 1 hour 15 minutes, 42%. Compulsory short-answer, structured and free-response questions of variable mark value, AO A and B.
- **Paper 3, Advanced practical skills.** 40 marks, 2 hours, 29%. Two experiments, AO C only. Marked by strand (Annexe A, printed p.30): manipulation, measurement and observation (MMO) 16, presentation of data and observations (PDO) 12, analysis, conclusions and evaluation (ACE) 12.
- **Three disagreements inside the syllabus, recorded not resolved:** paper weights (prose 77/23, table 29/42/29, marks 28.6/42.9/28.6), AO weights (printed 40/40/20, grid marks 35.7/35.7/28.6), and the Lincoln index cited but not given in Annexe C. Simpson's index is printed as D = 1 − (Σ n/N)², which differs from the standard form. The plan targets the printed 40/40/20.
- NSSCO Biology is recommended prior learning, not required.

## 1. What the corpus says
{st['records']} evidence records from papers 2021–2024 and the 2025 examiner report (2021–2023 papers are proof versions, 2023 has no report, 2025 has no papers). Details, limits and the register of source doubts are in the corpus analysis; the gaps are in `assessment-evidence/GAPS.md`.
- **Theme 2 carries about two thirds of Papers 1 and 2 by marks; the practical (Paper 3) and mathematical skills are the other large block.** Emphasis follows exposure; coverage is complete.
- **Paper 2 asks describe, explain and state most, at 1–3 marks, usually with more creditworthy points than marks.** Recall is a minority of the marks (the syllabus caps it at 20%).
- **The failures that recur:** answering a different question; near-neighbour terms confused; key terms and spelling; not using the data given, or units and notation; reasoning in the wrong direction; practical skill gaps.
- **{len(mis['entries'])} examiner-evidenced misconceptions**, curated by hand, each with a discriminating test.

## 2. Command words and tariffs
Use only these to open a prompt. The tariff is the one the work-order slot names; every slot tariff is one the papers set for that word (Paper 2 modal where the word is a question word).

| command word | in the syllabus table | parts (P2+P3, 2021–24) | modal tariff | tariffs seen |
|---|---|---:|---:|---|
{cwrows}

**Never open a prompt with:** {never}. "Define" is listed in the syllabus but never opens a part in 2021–2024, so it does not open a prompt (AGENTS.md rule 5; Jeremy decided on 2026-10-18 to ask as the exams do). The papers ask for definitions as "Explain what is meant by … / the meaning of …" (four parts, 2 marks) and "State what … means" (one part, 1 mark), so a definition card opens with **State what is meant by** (1 mark) or, for a developed definition, **Explain what is meant by** (2 marks). The syllabus glossary keeps Define (a formal statement), State (a concise answer) and "what is meant by" (a definition with a comment on its significance) apart; the card's guidance names the key words that carry the mark. The practical instruction words (plot, make, prepare, draw, record, take, move, look, fill in, complete, use) are bench instructions and cannot be posed by a text card; their skills are asked as State, Describe, Explain or Calculate questions about the technique. These are verdicts from papers 2021–2024; 2023 and 2025 add no wording evidence.

## 3. Answer shapes
From the reports' schemes and the evidence records (`curriculum/answer-shapes.json`, structure only). Write each answer to the shape its tariff carries.

| command, marks | how it is marked |
|---|---|
| State 1, Name 1–2 | one precise element, with the key term; a wrong extra statement can cancel a right one |
| Describe 2–3, Outline 3 | one mark per distinct, correctly linked point; more points are available than marks; written as full sentences in order, not bullets |
| Explain 2–3, Suggest 2 | a point and its reason, each its own sentence; a later point may depend on an earlier one; reasons run cause to effect, not the other way round |
| Identify 2, Compare 2 | the named structure or both sides of the comparison, with the reason where asked |
| Calculate 1–2 | the working in steps, the answer with its unit, to a justified number of significant figures |
| Discuss 2–3 | the points for and against or the factors, each developed |
| multiple-choice set | one mark per question; every distractor is a named error from the misconception register |

Marking guidance names the accepted alternatives and the rejects (accept/reject/ignore lists) and any cap (a maximum for one group of points). The reports state that terminology and spelling are credited.

## 4. Card types, assessment objectives and Bloom levels
Each slot declares its subtype, its AO (set by objective type and paper) and its Bloom level.

| subtype | tests | permitted AOs | Bloom level |
|---|---|---|---|
{subrows}

Performance tasks: multiple_choice_set = Apply; short_answer = Apply; practical_task = Analyse. A content topic gets a multiple-choice set and a structured question; a practical topic gets two practical tasks of about 10 marks (the second is a microscopy task where the topic concerns microscopy, otherwise a second investigation). Misconception cards on practical skills sit on the practical topics (independent and dependent variables, accuracy and reliability, plan diagrams versus cell drawings, graticule conversion) and on 5.1 (standard form).

## 5. The topics
32 topics: the 25 syllabus units, four practical-skills topics (4.1–4.4, from Annexe A) and three mathematical-skills topics (5.1–5.3, from Annexe C).

| topic | title | paper | objectives | items | notes words |
|---|---|---|---:|---:|---|
{tabrows}

**32 topics, {tot_objs} objectives, {tot_items} items ({n_miscon} misconception cards, {n_mcq} multiple-choice sets, {n_sa} structured questions, {n_prac} practical tasks), {lo:,}–{hi:,} words of notes.**

## 6. AO balance, in marks
| AO | planned | syllabus weight | gap |
|---|---:|---:|---:|
| A | {share['A']}% | {target['A']}% | {share['A']-target['A']:+d} |
| B | {share['B']}% | {target['B']}% | {share['B']-target['B']:+d} |
| C | {share['C']}% | {target['C']}% | {share['C']-target['C']:+d} |

Content topics are examined on Papers 1 and 2 (A and B equally, no C); the four practical topics on Paper 3 (C only). The subject total answers to the printed 40/40/20 (largest gap {max(abs(share['A']-target['A']),abs(share['B']-target['B']),abs(share['C']-target['C']))} points; `curriculum/ao_coverage.md`). Never pad the bank to chase an AO.

## 7. Misconceptions, glossary and scope
- **{len(mis['entries'])} examiner-evidenced misconceptions** in `curriculum/misconceptions.json`, each on its objective with a `test`. Every entry has its own MISCON slot in the work order. The correct ideas are our statements of standard biology and need two-source verification before import.
- **{len(gl['terms'])} glossary terms** in `curriculum/glossary.json`, each with its settled sense (draft; needs verification).
- **{len(scope['entries'])} scope patterns** in `curriculum/scope-scan.json`, carried by every contract as `excluded_constructs`; C-11 fails any learner-facing match:
{scoperows}
  Two limits cannot be scanned safely and are checked by a reader: the sampling methods of 1.2 (limited to frame quadrats, line and belt transects and mark-release-recapture) and the local or regional restoration examples of 1.3.

## 8. Rules particular to this subject
- **Biology is explained as cause and effect.** Every process is a chain (this, so that, so that); every structure says what each part does; every comparison names both sides. Describe and explain cards are written as full sentences in order.
- **Terms exact; near neighbours kept apart.** Use `curriculum/glossary.json` for every term; codon and anticodon, cohesion and adhesion, magnification and resolution, centromere and centrosome and the others in the misconception register are never used interchangeably.
- **Diagrams.** The authoring pipeline cannot draw them (`depictions: chart_model: none`), so every identification or labelling card is answerable from its own text, describing the structure or the stage by its features. Teaching diagrams (chromosome structure, the cell cycle, the four stages of mitosis, replication and translation schematics, plan diagrams) are generated after authoring by a subject script from declared structure, mapped to the cards they accompany, and attached at import, as for 0455 Economics.
- **No fences, no LaTeX.** Data and readings go in markdown tables; a graph is described by its axes, shape and key values, or given as a table for the learner to plot. Equations and sequences are plain text with Unicode symbols.
- **Practical data is ours, and says so.** Readings in a practical task are introduced as our readings, realistic and consistent with the biology. The notes for topics 4.1–4.4 say plainly that the manipulation marks are earned at the bench; the cards test the planning, recording, presentation, analysis and evaluation.
- **Significant figures and units.** Calculations show the equation, the substitution and the answer with its unit, carried to a justified number of significant figures; lengths seen under the microscope are given in micrometres (μm), following the syllabus's conventions for units and presentation (Annexe D).
- **Do not teach the board's doubtful keys.** The register of source doubts in the corpus analysis lists places where a printed key looks biologically wrong (the 2024 telomere key; the 2022 nuclear-envelope timing). Authors write from the syllabus and the verified claims, not from a key.
- **Claims carry their sources.** Every claim lists its evidence (the syllabus line and any report that speaks to it) and is written `verification.status: unverified`, `publishable: false`, with a note recording single_source or the second source. The build's PUBLISH decision does not check verification; our gate is the import into YYeni. No card is imported into YYeni until its claims have been verified by an independent reader and a person has checked a sample of the answers.
- **Paper 1 practice is a multiple-choice set per content topic**, four options, one key, every distractor built from a named error (the misconception register first), the reason each distractor is wrong on the back.

## 9. Decisions (Jeremy, 2026-10-18)
1. **Diagrams: approved as recommended.** Every identification or labelling card is answerable from its own text; teaching diagrams are generated after authoring from declared structure, mapped to their cards and attached at import. Photomicrographs remain a stated gap unless a licensed source is chosen.
2. **Simpson's index: the form the paper prints (confirmed).** The syllabus prints D = 1 − (Σ n/N)², with the square outside the brackets; since Σ n/N is 1 for every sample, that form gives D = 0 for every habitat. The 2023 Paper 2 prints and supplies the standard form, D = 1 − Σ(n/N)². Cards use the paper's form, note that the syllabus typesets it differently, and ask the learner to use and interpret the index, not to recall it. Jeremy first said "go with the syllabus", then set the rule of asking as the exams do, and confirmed this recommendation on 2026-10-18.
3. **Lincoln index: approved as recommended.** Taught as a method with its assumptions; the formula (n1 × n2 ÷ n3) is put in the card, as the 2024 Paper 3 does.
4. **AO C weight: the printed 20% is kept.** (Planned 18%; the grid's marks give Paper 3 28.6%.)
5. **Reviewer: Codex only for now.** No Biology teacher is available. A further check will be worked out alongside the Codex review; until then every card imports as AI-reviewed only.
6. **Define does not open a prompt; definitions are asked as the exams ask them** (State what is meant by; Explain what is meant by). Jeremy first kept Define, then reversed that the same day (2026-10-18).
"""
open("work/nam-8223-nsscas-2026/PLAN-8223-nsscas-biology.md", "w").write(plan)
hand = f"""# Handover prompt: Namibia NSSCAS Biology 8223

Paste everything below the line into the harness with this repository open. It is self-contained: the agent needs no other instruction from you.

---

You are authoring the complete learner resource for **Namibia NSSCAS Biology, syllabus code 8223** (NIED 2020, first examination 2021). The learners are Namibian Grade 12 students, English medium, sitting Papers 1, 2 and 3. They may have nothing else to learn from.

## Start here
Read these before writing anything:
1. `AGENTS.md` (repository root): you are the AUTHOR.
2. `work/nam-8223-nsscas-2026/PLAN-8223-nsscas-biology.md`: the plan. This is your brief. Read all of it.
3. `work/nam-8223-nsscas-2026/subject-profile.yaml`: the answer parts your marking guidance must name for each subtype, the conditioned mechanisms, the variant register, the prohibited patterns and the depiction rule.
4. `work/nam-8223-nsscas-2026/curriculum/answer-shapes.json`: how each command word and tariff is marked.
5. `standard/v0.2.0-draft/roles/AUTHOR.md`: written for business subjects. Where it conflicts with this handover, this handover wins. Money appears only where a situation involves it; "never say what a paper contains" means never claim frequencies or what examiners do.

Everything is derived already. `curriculum/syllabus-facts.json` records where each assessment value came from. Do not re-derive, do not re-read the syllabus PDF, and do not open any other subject's workspace.

## The job
**32 topics, {tot_items} items, {lo:,}–{hi:,} words of notes.** Work topic by topic (see the plan's topic table). For each topic `<T>` read `work/nam-8223-nsscas-2026/topics/<T>/contract.json` and `topics/<T>/work_order.json` (every slot pre-decided; `work_order.md` is the same plan as a table), then produce in `topics/<T>/`:
1. `claims/canonical_claim_ledger.json`: every statement the topic teaches, each mapped to the objectives it serves; 2–4 claims per objective.
2. `content-units/CU-8223-<T>.json`: prose blocks that cite the claims they rest on.
3. `learning-items/topic_<T>_items.json`: one item per slot.
4. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** {exemplar_note} are in `work/nam-8223-nsscas-2026/exemplar/` and pass every check. Copy their **shape** (the field set of every claim, block and item; the stamps), never their facts: the facts are illustrative and unverified.

## Every item carries its labels
Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all five onto the item.** The item's `item_id` is its slot id; a MISCON slot also names its `misconception_entry`. `assessment_objectives` is what the examination credits and is written with this subject's letters **A, B or C** (not AO1 to AO3); `blooms_level` is what the learner is asked to do: different axes, both required.

## Rules that come from the syllabus and the corpus
1. **Command words.** Only these open a prompt: {allowed}. Never Define, List, Give, Deduce, Predict, Comment, Find, Measure, Determine, Estimate, Show, Recognise, Classify, Plot, Make, Prepare, Draw, Record, Take, Move, Look, Fill, Complete or Use. Definition cards are asked the way the papers ask them: "State what is meant by X" (1 mark) or, for a developed definition, "Explain what is meant by X" (2 marks); the guidance names the key words that carry the mark. The papers never open with Define, so you must not.
2. **Tariffs.** Use the slot's. A point-marked answer lists more creditworthy points than its tariff where the plan says so, and its guidance says which and states the cap.
3. **Answer shape.** Describe, explain, suggest and outline answers are full sentences in order, not bullets. A calculation shows the equation, the substitution and the answer with its unit. The marking guidance names every part `subject-profile.yaml -> answer_structures` declares for the subtype, and the accepted alternatives and rejects.
4. **Misconceptions.** Each MISCON slot names its entry in `curriculum/misconceptions.json`. A MISCON card is a **discrimination**: the error, the correct idea, and the test that tells them apart (the entry's `test`). Never the correct definition repeated.
5. **Glossary.** `curriculum/glossary.json` settles every term's sense. Use them exactly, everywhere. Keep codon, anticodon and amino acid apart; keep cohesion, adhesion, magnification and resolution apart.
6. **Scope.** The contract's `excluded_constructs` are the limits the syllabus states, each with the pattern C-11 scans every learner-facing text for. Any match fails the topic: do not teach, practise or mention them, not even to say they are not required.
7. **Truth.** No unqualified universals (always, never, only, every) unless definitional. The conditioned mechanisms in the subject profile carry their conditions wherever they appear (C-37). Never claim what examiners reward or what a paper contains: the words "examiner" and "mark scheme" do not appear in learner-facing text (C-10).
8. **Do not teach the board's doubtful keys.** The register of source doubts in `operations/analysis/8223-nsscas-biology-corpus-analysis.md` lists them. You are not allowed to write from the printed keys or schemes; write from the syllabus and your own verified understanding. Where you are unsure of a biological fact, say so in the claim's notes and leave it unverified.
9. **Self-containment.** A flashcard supplies its own scenario, data, table or readings and never depends on another card. Arithmetic is correct (C-32 recomputes it) and every quantity carries its unit. An identification or labelling card describes the structure or stage by its features so it is answerable from its own text; a diagram will accompany it later.
10. **Nothing is reproduced.** No question, scenario, mark-scheme or report wording, anywhere. Every scenario, prompt, model answer and piece of guidance is yours. Situations are Namibian and southern African.
11. **Claims and verification.** Every claim lists its evidence (the syllabus line it restates and any report that speaks to it) and is written `verification.status: "unverified"`, `publishable: false`, with a note in `notes` of `verification_state: single_source` (one source named) or `second source: <what>`. The schema has no single-source status. Do not mark anything verified: the build's PUBLISH decision does not check verification, so the hold on importing unverified claims is ours, kept by the lead and the reviewers.
12. **Filenames are derived, never chosen.** Do not pass `--out` to the renderer and do not rename anything afterwards.
13. **Plain text.** Equations and sequences in plain text with Unicode symbols; no code fences, no LaTeX. Write pH, never PH.
14. **Multiple-choice sets.** `item_type: "multiple_choice_set"`, one item per slot, `mark_tariff` equal to the number of questions. The prompt numbers the questions, each with four options A–D on their own lines; the canonical answer gives the key ("Key: 1 B, 2 C, …") and, for each question, why the key is right and what error each distractor comes from.
15. **Practical tasks (topics 4.1–4.4).** `item_type: "practical_task"`. Describe the experiment or specimen in words, give our readings or values in a markdown table with quantity and unit headings, introduce them as ours, and number the parts with their marks. The notes say plainly that manipulation marks are earned at the bench; test the planning, recording, presentation, analysis and evaluation. Readings must be realistic and consistent (check them).
16. **Stated limits.** Some objectives carry a limit in `syllabus_guidance`. They are boundaries for you; C-11 scans for them.

## Voice
Plain, direct explanatory prose in British English. Short paragraphs. Full teaching depth: the notes are the source the flashcards are cut from, the offline study text and a standalone learning text at once. Every process is a chain of cause and effect; every structure says what each part does. Situations are Namibian and southern African where a situation is used; invented names for people only.

## The work order is a baseline, not a cage
Where a slot does not fit its objective, change it and record the change in `work/nam-8223-nsscas-2026/topics/<T>/authoring_notes.json` as `{{from, to, why}}`. An unrecorded deviation is the only kind that is wrong. Where a required subtype genuinely does not fit, add an entry to the contract's `subtype_waivers` with a reason of at least twelve words.

## Finishing each topic
```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/nam-8223-nsscas-2026 <T>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/nam-8223-nsscas-2026 <T>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/nam-8223-nsscas-2026 <T>
```
`what_to_fix.py` prints only failures, structure first, each with the action that clears it, and exits 0 when clean. Loop on it. `not_run` on C-35, C-41 and C-43 and a C-18 warning are expected. When all topics are clean:
```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/nam-8223-nsscas-2026
```

## Lessons from the first authored topics (apply these; each cost a fix round)
- **The claim schema is authoritative.** Evidence entries are objects `{{source_id, locator, support_type}}`, `claim_type` is one of definition, factual, formula, procedural, comparison, causal, evaluative, inference, synthetic_example, misconception_correction, and `verification.status` is one of the schema's values (use `unverified`; there is no single-source value, so say `verification_state: single_source` in `notes`). Where the exemplar README differs, the schema wins.
- **C-37.** Wherever you write denature or denaturation with pH or temperature, carry the condition in the same text: far or well above or below the optimum, permanent. The same applies to the other registered mechanisms (competitive inhibition: the active site and substrate concentration; telomere shortening: at each replication; semi-conservative: one old and one new strand).
- **C-13.** Avoid grouping phrases such as "two groups", "two kinds", "three families"; write "two sets" or name the members.
- **C-14.** Do not start a sentence or follow "and" with a forbidden command word (find, measure, determine, show, give, list, define and the rest) even inside a distractor or guidance; reword.
- **C-16.** The marking guidance must contain a word from each pattern in `answer_structures` for its subtype (for example INTERP needs words like "means" or "shows"; WHY needs "because" or "reason").
- **C-32 (arithmetic).** Write each step as "a × b = c" with c unrounded, then round in a following clause. A percentage is "× 100 = 85 per cent", not "= 85%" straight after "=". Never begin a line with a list number followed by arithmetic ("9. -0.50 ÷ …"): the check reads it as part of the equation.
- **Evidence entries.** `support_type` must be one of direct, paraphrase, corroboration, correction or derivation (use paraphrase for a claim that restates a syllabus line in other words).
- **Source labels.** In a claim's `evidence`, the syllabus is always `source_id: "NSSCAS-8223-SYLLABUS-2020"` with the printed page or unit as the locator. Cite an examiner-report finding by the evidence id from `assessment-evidence/assessment_evidence.json` (for example `EV-8223-2024-P2-Q3d-i`). Do not invent other labels.
- **Check wording.** C-16 matches whole words: INTERP guidance needs "means" (not "mean").
- **Universals.** Do not write always, never, only or every as an unqualified claim (a check flags them); say what is true under what condition.
- **Cross-links.** Name only topics that exist in `topics/` and whose title matches.
- **Scope limits are global.** The contract's `excluded_constructs` hold every topic's syllabus limits, so a word such as mesosome or chloride shift fails in any topic. Do not use them anywhere.
- **No scratch outside your topic.** Keep any generator inside `topics/<T>/` or do without; do not write to `/tmp`.

## Boundaries
- Do not edit anything under `standard/`, or anything in `work/nam-8223-nsscas-2026/curriculum/`, the contracts or the work orders (list plan problems in your report).
- Do not touch another subject's workspace, and do not edit `exemplar/`.
- Do not commit or push.
- There is no review round before the independent review after the build; the deterministic suite is your gate.
"""
open("work/nam-8223-nsscas-2026/HANDOVER-8223-nsscas-biology.md", "w").write(hand)
print("PLAN and HANDOVER written | topics", len(topics), "| objectives", tot_objs, "| items", tot_items, "| notes words %s-%s" % (format(lo, ","), format(hi, ",")), "| AO", share, "| miscon", n_miscon, "mcq", n_mcq, "sa", n_sa, "prac", n_prac)
