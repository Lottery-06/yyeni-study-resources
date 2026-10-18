# Handover prompt: Namibia NSSCAS Biology 8223

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
**32 topics, 773 items, 66,880–95,700 words of notes.** Work topic by topic (see the plan's topic table). For each topic `<T>` read `work/nam-8223-nsscas-2026/topics/<T>/contract.json` and `topics/<T>/work_order.json` (every slot pre-decided; `work_order.md` is the same plan as a table), then produce in `topics/<T>/`:
1. `claims/canonical_claim_ledger.json`: every statement the topic teaches, each mapped to the objectives it serves; 2–4 claims per objective.
2. `content-units/CU-8223-<T>.json`: prose blocks that cite the claims they rest on.
3. `learning-items/topic_<T>_items.json`: one item per slot.
4. Then render the notes and run the checks (commands at the end).

**Structural exemplar.** `exemplar/3.1.2` (a content topic) and `exemplar/4.3` (a practical slice) are in `work/nam-8223-nsscas-2026/exemplar/` and pass every check. Copy their **shape** (the field set of every claim, block and item; the stamps), never their facts: the facts are illustrative and unverified.

## Every item carries its labels
Each slot has already decided `subtype` (or `item_type`), `assessment_objectives`, `blooms_level`, `command_word` and `mark_tariff`. **Carry all five onto the item.** The item's `item_id` is its slot id; a MISCON slot also names its `misconception_entry`. `assessment_objectives` is what the examination credits and is written with this subject's letters **A, B or C** (not AO1 to AO3); `blooms_level` is what the learner is asked to do: different axes, both required.

## Rules that come from the syllabus and the corpus
1. **Command words.** Only these open a prompt: State, Explain, Describe, Discuss, Outline, Suggest, Calculate, Compare, Name, Identify. Never Define, List, Give, Deduce, Predict, Comment, Find, Measure, Determine, Estimate, Show, Recognise, Classify, Plot, Make, Prepare, Draw, Record, Take, Move, Look, Fill, Complete or Use. Definition cards are asked the way the papers ask them: "State what is meant by X" (1 mark) or, for a developed definition, "Explain what is meant by X" (2 marks); the guidance names the key words that carry the mark. The papers never open with Define, so you must not.
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
Where a slot does not fit its objective, change it and record the change in `work/nam-8223-nsscas-2026/topics/<T>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong. Where a required subtype genuinely does not fit, add an entry to the contract's `subtype_waivers` with a reason of at least twelve words.

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
- **The claim schema is authoritative.** Evidence entries are objects `{source_id, locator, support_type}`, `claim_type` is one of definition, factual, formula, procedural, comparison, causal, evaluative, inference, synthetic_example, misconception_correction, and `verification.status` is one of the schema's values (use `unverified`; there is no single-source value, so say `verification_state: single_source` in `notes`). Where the exemplar README differs, the schema wins.
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
