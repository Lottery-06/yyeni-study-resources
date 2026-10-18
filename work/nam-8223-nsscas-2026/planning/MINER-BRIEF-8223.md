# Mining brief — NSSCAS Biology 8223, one exam year per agent

You are a MINER (read `standard/v0.2.0-draft/roles/MINER.md` first; this brief adds what is specific to this subject). Your job: turn one exam year's papers and examiner report into structured evidence about **what is asked, how it is marked, and where candidates lose marks**. Every later stage depends on your judgement of what each question really tests.

## Rules that do not bend
1. **Mine, do not reproduce.** Official papers, mark schemes and reports are evidence of structure, tariff and failure. Their wording never reaches a learner. In your records you describe the demand and the shape of credit **in your own words**. You may quote a stem fragment of at most 25 words in `notes` (prefixed `stem:`) so a human can audit your mapping. Never copy mark-scheme sentences into `creditworthy_points`; describe each marking point in your own words.
2. **Map objectives by MEANING, not by token match.** A question's words matching an objective's words is not evidence. Read what the learner is being asked to do and pick the objective(s) it credits. Use only ids from `work/nam-8223-nsscas-2026/curriculum/objective_ids.json` (152 ids, `OBJ-8223-<unit>-<nn>`, built from the syllabus). Never invent an id. A question may map to several. If a question tests something outside the syllabus, map it to the nearest objective and say so in `notes`.
3. **Record uncertainty.** Every record's `notes` starts with `mapping_method: by meaning; confidence: high|medium|low`. For low confidence say why. A limitation recorded is a limitation managed.
4. **Do not guess answers.** Where a source does not state the key, the marks or the examiner's finding, leave that field empty and say so in `notes`. Do not fill gaps from your own biology knowledge and do not label your own reading as a board statement. If you add your own reading, prefix it `own reading:`.
5. **Stay in your lane.** Write only your one output file (below) and nothing else. Do not edit any other file, do not commit, do not run build tools. Never open another subject's workspace.
6. Read page **images** (`pdftoppm -png -r 100 -f N -l N <pdf> <prefix>` then view the PNG) for any question whose meaning depends on a diagram, graph, micrograph or table you cannot see in the text. Say in `notes` when you used an image.

## Sources (all under `/Users/jeremytiboth/Documents/yyeni-study-resources/`)
- Syllabus facts (read for context, do not edit): `work/nam-8223-nsscas-2026/curriculum/syllabus-facts.json`, and `objective_ids.json` beside it.
- Papers: `Question Banks/Namibian Curricula/NSSCAS/Biology (8223)/<year>/` (Papers 1, 2, 3; some years also a Paper 3 teachers' instructions).
- Examiner reports (one PDF per year, all NSSCAS subjects; find the BIOLOGY section by the contents page): `work/nam-8223-nsscas-2026/sources/NSSCASExaminersReport<year>.pdf`. Reports contain, per question: examiner commentary, and the marking scheme (shown in italics in the original). Paper 1 sections give the key, the percentage correct and a comment.
- Extract text with `pdftotext -layout` and `pdftotext -raw` (two-column pages read differently in each).
- Put scratch files only in `/private/tmp/claude-502/-Users-jeremytiboth/45f18be7-94fc-401d-8b36-966466e3b78e/scratchpad/mine-<year>/`.

## Per-year facts
| Year | Papers held | Report held | Notes |
|---|---|---|---|
| 2021 | P1 (First Proof), P2 (First Revised Proof), P3 (First Proof), P3 teachers' instructions | 2021: **Biology Papers 2 and 3 only** | No Paper 1 key or comment exists in any held source. P1 records have empty keys. |
| 2022 | P1, P2, P3 (all First Proof), plus an unlabelled P3 dated 01.06.2022 | 2022: Papers 1, 2, 3 | The unlabelled P3 is the later version; use it for P3 and say so. |
| 2023 | P1 (First Proof), P2 and P3 (First Revised Proof) | **none** | No key, no scheme, no examiner comment exists. Records carry what the paper asks only. `creditworthy_points`, `examiner_findings` and `common_errors` stay empty; say so in `notes`. |
| 2024 | `8223-1.pdf`, `8223-2.pdf`, `8223-3.pdf`, `8223-3TI.pdf` (unlabelled) | 2024: Papers 1, 2, 3 | |
| 2025 | **no papers held** | 2025: Papers 1, 2, 3 | Mine the report only. P1: key letter, % correct and comment per item; the question text is absent, so map by the comment's meaning and mark confidence low or medium unless the comment makes the topic unambiguous. P2/P3: the report describes each question through its commentary and marking scheme. |

## What to produce: one file
`work/nam-8223-nsscas-2026/assessment-evidence/by-year/evidence_<year>.json`:
```
{"map_id": "ASSESS-NAM-NSSCAS-8223-<year>", "status": "partial", "records": [ ... ]}
```
It must validate against `standard/v0.2.0-draft/schemas/assessment_evidence.schema.json` (additionalProperties is false: use only these fields). Validate before you finish with a script that loads the schema and your file with `jsonschema.Draft202012Validator` (run with plain `python3`, not `-I`, so user-installed jsonschema is found).

**One record per question part** (Paper 2, Paper 3) and **one per multiple-choice item** (Paper 1). Fields:
- `evidence_id`: `EV-8223-<year>-P<n>-Q<ref>` e.g. `EV-8223-2022-P2-Q3a-ii`, `EV-8223-2022-P1-Q38`.
- `source_id`: `NSSCAS-8223-<year>-P<n>`.
- `evidence_type`: `"past_paper"` (your records combine paper and report evidence).
- `exam_series`: `"Oct/Nov"`. `year`: integer. `paper_id`: `"P1"|"P2"|"P3"`. `variant`: null. `question_ref`: e.g. `"3(a)(ii)"` or `"38"`.
- `mark_tariff`: integer marks for that part (1 for every P1 item). Reconcile part tariffs against the printed question total.
- `objective_ids`: one or more ids (see rule 2).
- `command_word`: the word that opens the question, as printed, capitalised (e.g. `"Explain"`); null for P1 items and for parts with no opening command word. Record exactly what the paper uses, including words not in the syllabus glossary.
- `ao_focus`: from `["A","B","C"]`. Judge by what the part demands (recall of knowledge = A; interpreting data, applying to a new situation, calculating, reasoned explanation from given information = B; practical skills = C). Say in `notes` if you were unsure.
- `context_type`: one of `recall`, `diagram-labelling`, `diagram-interpretation`, `data-table`, `graph`, `calculation`, `novel-scenario`, `practical`, `sequence-or-code`, `other`.
- `context_summary`: one or two sentences, in your own words, of what the learner is asked to do and with what material.
- `creditworthy_points`: the **shape** of credit in your own words: how many distinct points, whether a point must be developed to score, whether a named term is required, what is rejected or accepted, ecf (error carried forward). For P1: `["key: <letter> (2022 report p.<n>)"]` if the report gives it, else empty.
- `examiner_findings`: each statement the report makes about this part, paraphrased, **prefixed with one of** `[misconception]`, `[omission]`, `[command-word miss]`, `[shallow development]`, `[facility]` (for the % correct on a P1 item), `[language/terminology]`, or `[other]`. End each with `(report p.<printed page>)`.
- `common_errors`: the wrong ideas or wrong moves candidates make, in your own words.
- `strong_response_features`: what the report says strong answers do.
- `source_locator`: paper file name and printed page; report file and printed page.
- `notes`: starts with `mapping_method: by meaning; confidence: ...`; then flags (proof version; image used; key not held; part tariff inferred), `stem: "<=25 words>"`.

## What to report back (as your final message, under 300 words)
Records written by paper; how many carry creditworthy points, findings and common errors; how many records are low-confidence and why; anything you could not read or map; anything in the sources that looks wrong (a printed answer that is biologically incorrect, a question outside the syllabus, a scheme that does not match its question, a tariff that does not reconcile). Do not paste records into the report.
