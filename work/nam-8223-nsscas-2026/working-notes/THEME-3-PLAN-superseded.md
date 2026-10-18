> **SUPERSEDED 2026-10-18.** This Theme-3-only plan was written before the team playbook was found. The playbook's step 4 plan (whole subject, built with the repo tools) replaces it. Kept as working notes: the paper evidence, card-type ideas and verification approach are inputs to steps 3 and 4. Paths below use the old workspace name `nsscas-8223-biology`.

# Theme 3 plan — Development of the organism and the continuity of life (APPROVED 2026-10-18)

NSSCAS Biology 8223, pilot unit. Drafted and approved 2026-10-18. Nothing is imported until the cards pass the gates below.

## Scope (syllabus is the authority)
| Syllabus | YYeni lesson | Atomic objectives (syllabus bullets) | Cards |
|---|---|---|---:|
| 3.1.1 Replication and division of nuclei and cells | 6982 | 7: chromosome structure; importance of mitosis; root-tip mitotic stages (practical); mitotic cell cycle with G1/S/G2/cytokinesis; telomeres; stem cells; uncontrolled division and tumours | 18 |
| 3.1.2 Chromosome behaviour in mitosis | 6983 | 2: chromosome, nuclear envelope, membrane and spindle behaviour through the four stages; interpret photomicrographs and diagrams to name the stage | 14 |
| 3.2.1 Structure and replication of DNA | 6985 | 5: nucleotide and ATP structure; purines and pyrimidines; RNA and DNA structure and base pairing; semi-conservative replication; model-making (practical) | 16 |
| 3.2.2 Protein synthesis | 6988 | 7: gene = nucleotide sequence coding a polypeptide; features of the genetic code; transcription and translation (mRNA, tRNA, ribosome); gene mutation defined; substitution, deletion, insertion effects; HbA/HbS sequence; RNA model (practical) | 18 |
| **Total** | 4 lessons | | **66** (under the 100-card import limit) |

Card counts are a baseline. Atomic objectives (Stage 6) will be refined first; the counts may move by about 20% and any deviation is recorded.

## Out of scope (goes in each contract's excluded_constructs)
- Meiosis, genetic crosses, genetic engineering, gene regulation (not in this syllabus's Theme 3).
- Structural formulae of nucleotides and bases (3.2.1 says not required).
- Mesosomes (2.2). Names of other cell-cycle regulators or checkpoints (the syllabus asks only that uncontrolled division can form a tumour).
- Anything in adjacent lessons: amino acid and peptide-bond structure and protein structure are 2.4.2; ATP's role in cells is 2.2. A Theme 3 card may name them in passing but does not teach them.
- Hands-on practical manipulation (squash preparation, modelling). Planning, variables, data handling and conclusions from these practicals can be carded.

## Evidence from 2021–2024 papers and the 2025 examiner report
Paper analysis: `assessment-evidence/THEME-3-PAPER-ANALYSIS.md`. Paper 2 Theme 3 marks: 10, 16, 11, 9 across 2021–2024. 20 Paper 1 items on Theme 3. Each recurring item gets at least one card:
1. Telomeres: description, role in replication, shortening over time, telomerase and tumours (2021 Q5, MCQ 2021, 2023, 2024; 2025 Q37 only 42% correct).
2. Mitosis stage recognition and the behaviour of chromosomes after a given stage (2022 Q3, MCQ 2021 Q33–35, 2024 Q36, 2025 Q35–36).
3. Cell cycle phases and what happens in S phase (2022 Q3(a)(i), MCQ 2021 Q36, 2024 Q35 and Q38, 2025 Q34).
4. DNA replication enzymes and their functions (2022 Q3(d)); semi-conservative replication (2022 Q3(d)(ii), 2023 Q2(b)).
5. RNA versus DNA structure; shared features of DNA and mRNA (2023 Q2(a), MCQ 2022 Q39).
6. Purines and pyrimidines, hydrogen bonds between bases (MCQ 2021 Q39–40).
7. Transcription outline; mRNA from tRNA anticodons; DNA template strand (2024 Q3(b),(c); 2023 Q2(c)).
8. Gene mutation effects on a polypeptide and on a cell's metabolism (2024 Q3(d), MCQ 2022 Q40 sickle cell).
9. Misconceptions from the 2025 report: each chromosome has two chromatids with two telomeres each; three nucleotides code each amino acid.
Not mined for a card source: Paper 3 (practical), and 2021–2024 examiner commentary (not obtained).

## Card design
- **Bloom mix:** Remember ~30%, Understand ~30%, Apply ~15%, Analyse ~25%. Recall stays a minority (syllabus: not more than 20% of marks are recall). Analyse cards are 2-mark cards in YYeni, marked for structure and content.
- **Card types:**
  - Recall: define/state/name (e.g. telomere, semi-conservative, purine, gene mutation, replication enzymes and functions).
  - Compare: RNA vs DNA, mitosis stage behaviours, transcription vs translation (one contrast per card).
  - Explain/suggest: answer written as numbered marking points with a stated maximum and a reject list, in full sentences (the 2025 report says bullets are not acceptable for describe/explain/suggest). Examples: how high telomerase enables a tumour; how a substitution changes a polypeptide and a cell's metabolism.
  - Misconception: the error, the correct idea, and the test that tells them apart.
  - Sequence application: codons, anticodons, template and mRNA strands with the card supplying its own data. Cards supply fixed examples; changing-number practice is a later activity, not a card.
  - Diagram: identify a labelled stage or part (see Diagrams).
- Every card gets `objective_ids`, `exam_evidence` (the paper item or report remark behind it) or `exam_status: not_examined_background`, a command word from the syllabus glossary, and `review_status`.
- Original wording and original scenarios. No board question, mark scheme or report wording reproduced (stems are identified, not quoted).
- LaTeX only for the few formulae or sequences; no Markdown emphasis on maths. Spelling: key terms listed for exact spelling (centromere, chromatid, telomere, anticodon). Write "pH" if it appears.
- Namibian context only where the syllabus or the YYeni lesson already supplies it (CR-004 is only proposed).

## Diagrams
- Needed: (1) metaphase chromosome with centromere, sister chromatids and telomeres; (2) the cell cycle (G1, S, G2, M); (3) the four stages of mitosis drawn as schematics for "name the stage and give a reason"; (4) optionally a replication fork and a translation diagram.
- Rule (RS-47, CR-005): a depiction is generated from declared data, not hand-drawn. Each diagram is rendered from a small structured spec, and the spec is kept next to the card so the picture can be regenerated and checked.
- Delivery: YYeni accepts managed image assets (`question_asset_id`, `answer_asset_id`). The teacher MCP can render JSON diagrams or import raster bytes. A test render must succeed before cards are drafted around it.
- Real photomicrographs: not in the first build unless a licensed source is chosen. Stage recognition from a photomicrograph stays a stated gap.

## Verification of answers (no 2021–2024 board mark scheme exists)
- Stage 10 claim ledger first: 2–4 claims per atomic objective, each with provenance, a verification state and a publishability state. Cards cite the claims they rest on.
- Each claim needs two sources: the syllabus wording for scope, plus one independent source for correctness (the 2025 report where it speaks to the point; Cambridge 9700 material; a second Biology reviewer). A claim with one source is marked `single_source` and cannot publish.
- Cambridge 9700 mark-scheme download: **declined by Jeremy 2026-10-18**. Second sources are therefore the 2025 examiner report where it speaks to the point, the 10 Cambridge 9700 mark schemes already in the repo where relevant, and the independent Codex review. A claim none of these can corroborate stays `single_source` and cannot publish.

## Other deliverables
- Revision notes per lesson, written first, with cards derived from them (the 8223 notes folder is empty). Notes follow the pipeline's depth tiers.
- Setup files this workspace does not have yet: qualification profile, subject profile, objective registry for Theme 3 (partial, like Maths 6131), and contracts.
- Later, not in this pilot: Paper 2 style practice questions and Paper 3 planning tasks as activities.

## Quality gates
1. Atomic objectives and claim ledger reviewed (you).
2. Deterministic checks (`standard/v0.2.0-draft/checks/run_checks.py`) once the profiles and contracts exist; fix every failure.
3. Independent Codex review of the full packet (profile, objectives, claims, items, exclusions log, deterministic report), looping fixes back to the earliest affected stage.
4. Subject-expert review of every answer by Codex before import (AI review; see Decisions). No card is imported on single-source claims.
5. Preview with the MCP (`preview_flashcard_import`), your approval, then `confirm_flashcard_change`. Import is 100 cards per batch, shared classroom cards, no deck assignment or billing.

## Known gaps
- No 2021–2024 mark schemes or examiner reports; 2025 report covers the 2025 papers only, and those papers are not in the repo.
- Most papers are proof versions; wording may differ from the printed exam.
- Diagrams: stage recognition needs generated schematics; photomicrographs unresolved.
- Several MCQ keys in 2021–2024 are unknown. MCQ-style cards are written from the syllabus and claims, not from those items.
- YYeni lesson titles are semantic, not verbatim, matches to the syllabus; lesson IDs 6982, 6983, 6985, 6988 need a final check against the live classroom at import.
- The Codex review of the syllabus summary was not completed (last result: NEEDS CHANGES on two small annex points, since fixed; not re-confirmed).

## Decisions (2026-10-18)
1. Scope, 66-card count and card types: **approved**.
2. Cambridge 9700 Paper 2 and 4 mark-scheme download: **declined**.
3. Subject-expert reviewer for gate 4: **Codex**. This is an AI review, not a human subject expert, and Codex shares training-data blind spots with the author. It is recorded as a known limit: until a human Biology teacher checks the answers, cards are imported with `review_status: ai_reviewed`, not `teacher_reviewed`, and the import report says so.
