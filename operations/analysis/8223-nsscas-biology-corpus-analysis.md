# 8223 NSSCAS Biology: corpus analysis

Written 2026-10-18 for work/nam-8223-nsscas-2026. Every figure below is computed by `work/nam-8223-nsscas-2026/planning/compute_stats.py` and `write_analysis.py` over `assessment-evidence/assessment_evidence.json` (398 records). The mapping of each question part to objectives, and every description of how a part is marked, were made by reading (five mining agents, one per exam year, then spot-checked); the figures built on them are counts. AO tags and objective mappings are our judgement, labelled as such; keys, facility figures and printed tariffs are the board's.

## 1. The corpus
| Year | Papers held | Report held | Records |
|---|---|---|---|
| 2021 | P1 (First Proof), P2 (First Revised Proof), P3 (First Proof) | Biology Papers 2 and 3 (no Paper 1 section) | 40 + 28 + 15 |
| 2022 | P1, P2, P3 (all First Proof; the unlabelled 01.06.2022 P3 is identical) | Papers 1, 2, 3 | 40 + 24 + 15 |
| 2023 | P1 (First Proof), P2 and P3 (First Revised Proof) | **none** | 40 + 28 + 15 |
| 2024 | P1, P2, P3 (unlabelled) | Papers 1, 2, 3 | 40 + 27 + 14 |
| 2025 | **none** | Papers 1, 2, 3 (Paper 2 covers four questions, Paper 3 two) | 34 + 23 + 15 |

One record per Paper 1 item and per Paper 2/3 question part. Mapping confidence: high 226, medium 143, low 29. Six 2025 Paper 1 items whose report comment names no topic are kept in `assessment-evidence/unmapped_2025_p1.json` and are not in the evidence map or any count. **Changes since the analysis was first read (2026-10-18, during step 4):** the evidence map now excludes those six items (404 records became 398); every record carries a per-sitting series label so exposure recomputes; 272 practical-skill and maths-skill objective ids (Annexe A and C, topics 4.x and 5.x) were added by reading, so a Paper 3 or data-skill part now also maps to the skill it tests; exposure classes follow the build tools' definitions; and a few counts below changed with them.

**Used with limits:** 2021–2023 papers are proof versions and may differ from the printed exam; 2023 has no key, scheme or comment; 2025 has no papers, few stated tariffs and no command words; Paper 1 keys exist for 2022, 2024 and 2025 only (120 of 200 items) and were checked against the reports (120 of 120 match). **Set aside:** nothing was excluded; no older-syllabus papers are held.

## 2. What each paper looks like
- **Paper 1 (multiple choice, 40 marks, 1 hour).** Forty four-option items, one mark each, in syllabus order. Items test recognition and application: diagrams, graphs, sequences and statement-judging as well as recall. Of the 160 items 2021–2024, 102 were tagged A (knowledge) and 58 B (application), some both. The facility figures the 2024 and 2025 reports give run from 9% to 95%.
- **Paper 2 (structured, 60 marks, 1 hour 15).** Compulsory questions per year (2021: 6, 2022: 4, 2023: 5, 2024: 4; 2025 report covers 4), each built from linked parts of 1 to 8 marks around one stimulus (a table, graph, diagram, micrograph or short scenario). Mark tariffs by part: 1×30, 2×44, 3×19, 4×9, 5×3, 6×1, 8×1 (mark: number of parts). Parts sum to 60 each year 2021–2024.
- **Paper 3 (advanced practical, 40 marks, 2 hours).** Two experiments, each worth 20. Skills tested include tables, graphs, calibration with an eyepiece graticule, drawing plan and cell diagrams, variables, accuracy and reliability, and percentage-change arithmetic. 2021 part tariffs sum to 42, not 40 (see source doubts). The reports print little or no mark scheme for Paper 3, so what earns credit there is mostly commentary.

## 3. Command words actually used
Counted over Paper 2 parts 2021–2024 (the wording comes from the papers; 2025 has none recorded). The rule (AGENTS.md 5): only words the papers use may open a flashcard.

| Word (as printed, lower-cased) | Parts | Modal tariff | Tariffs seen |
|---|---:|---:|---|
| describe | 21 | 2 | 1 mark ×5, 2 marks ×7, 3 marks ×2, 4 marks ×3, 5 marks ×2, 6 marks ×1, 8 marks ×1 |
| explain | 18 | 2 | 1 mark ×2, 2 marks ×8, 3 marks ×6, 4 marks ×2 |
| state | 16 | 1 | 1 mark ×9, 2 marks ×6, 3 marks ×1 |
| name | 12 | 2 | 1 mark ×5, 2 marks ×5, 4 marks ×1, 5 marks ×1 |
| suggest | 8 | 2 | 2 marks ×5, 3 marks ×3 |
| use | 7 | 1 | 1 mark ×3, 2 marks ×3, 4 marks ×1 |
| identify | 5 | 2 | 2 marks ×4, 3 marks ×1 |
| calculate | 4 | 1 | 1 mark ×3, 2 marks ×1 |
| outline | 4 | 3 | 2 marks ×1, 3 marks ×2, 4 marks ×1 |
| discuss | 3 | 2 | 2 marks ×2, 4 marks ×1 |
| complete | 2 | 2 | 2 marks ×1, 3 marks ×1 |
| record | 2 | 1 | 1 mark ×2 |
| draw | 1 | 3 | 3 marks ×1 |
| compare | 1 | 2 | 2 marks ×1 |
| fill in | 1 | 3 | 3 marks ×1 |
2 Paper 2 parts open with no command word (a stem sentence then a labelling or drawing instruction).

**Paper 3 opening words** (practical instructions, 2021–2024): use ×10, describe ×6, state ×6, plot ×4, identify ×4, make ×4, prepare ×4, calculate ×3, suggest ×3, draw ×2, complete ×2, outline ×1, construct ×1, look ×1, sketch ×1, take ×1, discuss ×1, move ×1. "Use" usually introduces a read-off, measure or calculate task; make, prepare, plot, draw, take, move, look and complete are laboratory instructions, not questions a flashcard can pose.

**Listed in the syllabus glossary but never opening a Paper 2 or 3 part, 2021–2024:** classify, comment, deduce, define (the term(s)...)., determine, estimate, find, give a reason/ give reasons, list, measure, predict, recognise, show, what do you understand by/what is meant by (the term(s)...). Notably **"define" is never used** although three objectives begin "define" (1.2-01, 2.4.1-01, 2.8.1-01). The papers ask for definitions as "Explain what is meant by / the meaning of" (four Paper 2 parts, 2 marks, 2022–2024) and "State what … means" (one part, 1 mark, 2024); the syllabus glossary keeps Define (a formal statement), State (a concise answer) and "what is meant by" (a definition with comment on its significance) apart. **Used but not in the glossary:** name, identify, use, complete, plot, make, prepare, draw, record, look, fill in, take, move.

**Proposed verdict for prompts (the plan decides):** `use_in_prompts: true` for describe, explain, state, name, suggest, identify, outline, calculate, discuss (each opens three or more Paper 2 parts); allow compare (one Paper 2 part, but the syllabus names compare objectives); `false` for the practical instruction words and for every glossary word the papers never use, including Define (decision 2026-10-18: ask as the exams do). Definition cards open with "State what is meant by" or "Explain what is meant by".

## 4. What a creditable answer looks like
From the schemes and commentary in the 2021, 2022, 2024 and 2025 reports (structure only; `curriculum/answer-shapes.json` holds the detail).
- **More points on the scheme than marks.** Where the evidence records state a count, 16 of 18 Paper 2 parts offer more creditworthy points than marks (the learner scores up to the tariff). This is a small readable sample, so indicative only.
- **Point-marked and developed.** Describe, explain, suggest and outline answers earn one mark per distinct, correctly linked point; a later point can depend on an earlier one; a stated cap limits marks from one group (for example, only listing stages earns one mark).
- **Named terms matter.** Correct terminology is required and a wrong or misspelled key term can lose the mark; a wrong extra statement ("reject") can cancel a correct one.
- **Alternative wording and the reverse argument are credited**; any valid point and error carried forward appear in some years.
- **Data parts:** quote the data with units to reach the top mark; describing a graph is not explaining it.
- **Style:** full sentences for describe, explain, suggest, discuss, give a reason and outline; bullets only for list and state (reports 2021 p.37, 2022 p.42, 2024 p.39, 2025 p.43).

## 5. Where the marks fall
Share of Paper 1 plus Paper 2 marks 2021–2024 (400 marks counted; a part naming several topics is split equally between them): Theme 1 9.2%, Theme 2 66.1%, Theme 3 16.0%, with 4.3% mapped to the practical-skills topics (4.x) and 4.4% to the maths-skills topics (5.x). The syllabus lists 152 objectives across 25 units, plus the skills of Annexes A and C; this calibrates emphasis and **never removes coverage**.

| Unit | Title | P1 % | P2 % | P1+P2 % | P3 marks 2021–24 |
|---|---|---:|---:|---:|---|
| 1.1 | Classification | 1.9 | 3.7 | 3.0 | – |
| 1.2 | Biodiversity | 4.4 | 3.9 | 4.1 | 8.5 |
| 1.3 | Conservation | 4.1 | 0.8 | 2.1 | – |
| 2.1 | The microscope | 3.5 | 1.0 | 2.0 | 5.0 |
| 2.2 | Cell structure | 4.7 | 3.1 | 3.8 | 8.7 |
| 2.3.1 | Fluid mosaic membranes | 2.8 | 1.9 | 2.2 | 2.8 |
| 2.3.2 | Movement of substances into and out of cells | 5.0 | 5.5 | 5.3 | 2.8 |
| 2.4.1 | Carbohydrates and lipids | 5.6 | 5.8 | 5.7 | 2.0 |
| 2.4.2 | Proteins and water | 5.5 | 4.8 | 5.1 | 2.0 |
| 2.5.1 | Mode of action of enzymes | 1.8 | 2.1 | 2.0 | 5.5 |
| 2.5.2 | Factors that affect enzyme action | 5.9 | 4.8 | 5.2 | 19.8 |
| 2.6.1 | Structure of transport tissues | 2.2 | 0.4 | 1.1 | 5.8 |
| 2.6.2 | Mechanisms of transport in plants | 5.8 | 2.3 | 3.7 | 8.2 |
| 2.7.1 | Mammalian circulatory system | 4.7 | 4.2 | 4.4 | – |
| 2.7.2 | Mammalian heart | 3.4 | 0.0 | 1.4 | – |
| 2.8.1 | Infectious disease | 2.2 | 7.1 | 5.1 | – |
| 2.8.2 | Antibiotics | 1.6 | 4.5 | 3.3 | – |
| 2.9.1 | The response of the immune system to pathogens | 4.0 | 6.7 | 5.6 | – |
| 2.9.2 | Antibodies and vaccination | 4.6 | 1.7 | 2.8 | – |
| 2.10.1 | The gas exchange system | 5.0 | 5.1 | 5.1 | 3.3 |
| 2.10.2 | Smoking and its impact on the gas exchange and circulatory system | 3.1 | 1.7 | 2.2 | 1.7 |
| 3.1.1 | Replication and division of nuclei and cells | 5.3 | 5.4 | 5.4 | – |
| 3.1.2 | Chromosome behaviour in mitosis | 2.5 | 2.5 | 2.5 | – |
| 3.2.1 | Structure and replication of DNA | 3.7 | 4.8 | 4.4 | – |
| 3.2.2 | Protein synthesis | 0.9 | 5.6 | 3.8 | – |
| 4.1 | Planning investigations and taking measurements | 0.4 | 0.6 | 0.5 | 15.5 |
| 4.2 | Microscopy, drawing and measuring specimens | 0.3 | 0.0 | 0.1 | 22.2 |
| 4.3 | Recording and presenting data | 0.0 | 0.7 | 0.4 | 17.0 |
| 4.4 | Analysis, conclusions and evaluation | 0.7 | 5.0 | 3.3 | 13.0 |
| 5.1 | Number, units and accuracy | 1.7 | 0.9 | 1.2 | 3.7 |
| 5.2 | Graphs, charts and rates of change | 1.8 | 1.8 | 1.8 | 10.0 |
| 5.3 | Size, magnification and biodiversity calculations | 1.0 | 1.5 | 1.4 | 4.5 |

Unit 2.7.2 (Mammalian heart) has no Paper 2 marks in 2021–2024 but appears in Paper 1. Paper 3 evidence (2021–2024) maps to 20 topics: 1.2, 2.1, 2.2, 2.3.1, 2.3.2, 2.4.1, 2.4.2, 2.5.1, 2.5.2, 2.6.1, 2.6.2, 2.10.1, 2.10.2, 4.1, 4.2, 4.3, 4.4, 5.1, 5.2, 5.3.

**Exposure classes** (the build tools' definitions, by share of the five sittings in which an objective is named: core in 3 or more, frequent in 2, occasional in 1, unseen in none), over all 226 objectives including the skills topics: core 100, frequent 46, occasional 42, not named by any held question part 38. "Not named" is not "not examinable": 2023 has no report, 2025 has no papers, and many of these are practical or one-line statement objectives (1.1-04, 1.3-04, 1.3-07, 2.2-04, 2.2-05, 2.2-09, 2.3.1-02, 2.3.2-02, 2.5.1-01, 2.5.1-02, 2.7.1-01, 2.7.1-08, 2.7.1-11, 2.7.1-13, 2.7.2-02, 2.7.2-03, 2.9.2-06, 2.10.1-01, 2.10.1-02, 2.10.2-03, 3.1.1-03, 3.2.1-05, 3.2.2-01, 3.2.2-07, 4.1-05, 4.1-10, 4.2-02, 4.2-05, 4.3-03, 4.4-03, 4.4-09, 4.4-10, 5.1-06, 5.2-06, 5.2-07, 5.2-08, 5.2-09, 5.3-04).

Theme 3 (the likely exemplar slice):

| Objective | Text | Class | Parts |
|---|---|---|---:|
| 3.1.1-01 | describe the structure of a chromosome, limited to DNA, histone protei | core | 6 |
| 3.1.1-02 | explain the importance of mitosis in the production of genetically ide | occasional | 1 |
| 3.1.1-03 | observe and draw the mitotic stages visible in temporary root tip squa | unseen | 0 |
| 3.1.1-04 | outline the mitotic cell cycle, including interphase (growth in G1 and | core | 7 |
| 3.1.1-05 | outline the significance of telomeres in permitting continued replicat | core | 6 |
| 3.1.1-06 | outline the role of stem cells in cell replacement and tissue repair b | occasional | 1 |
| 3.1.1-07 | explain how uncontrolled cell division can result in the formation of  | frequent | 2 |
| 3.1.2-01 | describe, with the aid of photomicrographs and diagrams, the behaviour | core | 7 |
| 3.1.2-02 | interpret photomicrographs, diagrams and microscope slides of mitosis  | core | 6 |
| 3.2.1-01 | describe the structure of nucleotides, including the phosphorylated nu | frequent | 2 |
| 3.2.1-02 | state that adenine and guanine are purines with a double ring structur | occasional | 1 |
| 3.2.1-03 | describe the structure of RNA and DNA and explain the importance of ba | core | 5 |
| 3.2.1-04 | describe the semi-conservative replication of DNA during S phase | core | 5 |
| 3.2.1-05 | design and make a model of DNA to illustrate the semi-conservative rep | unseen | 0 |
| 3.2.2-01 | state that a polypeptide is coded for by a gene and that a gene is a s | unseen | 0 |
| 3.2.2-02 | state the features of the genetic code | occasional | 1 |
| 3.2.2-03 | describe how the information in DNA is used during transcription and t | core | 8 |
| 3.2.2-04 | state that a gene mutation is a change in the sequence of nucleotides  | occasional | 2 |
| 3.2.2-05 | explain that a gene mutation occurs by substitution or deletion or ins | occasional | 1 |
| 3.2.2-06 | describe the way in which the nucleotide sequence codes for the amino  | core | 4 |
| 3.2.2-07 | design and make a model of RNA to contrast it with the DNA model | unseen | 0 |

## 6. How candidates lose marks
Statements in the four held reports, by type (all years): misconception 126, facility 98, omission 96, other 59, command-word miss 44, shallow development 21, language/terminology 18. Units with the most misconception, omission, command-word and shallow-development statements: 2.5.2 (31), 2.3.2 (26), 2.8.1 (20), 2.7.1 (19), 1.2 (19), 2.6.2 (18), 2.2 (16), 2.4.1 (15). The recurring failures, with what the resource will do about each:
1. **Answering a different question** (describing a graph instead of explaining it, naming a stage but not giving the reason, stating a function when asked to identify, writing about the wrong structure). *Cards:* command-word-matched questions at the tariffs the papers set, with marking guidance that names the parts; MISCON cards for the discrimination.
2. **Near-neighbour terms confused** (centromere/centrosome, cohesion/adhesion, codon/anticodon, microvilli/cilia, hydrogen/disulfide, magnification/resolution). *Cards:* one MISCON card per confusion with a test that separates the two (87 curated entries).
3. **Missing or wrong key terms and spelling** (organelle versus cell, "double membrane", "PH"). *Cards:* term-exact answers and a spelling check for flagged terms.
4. **Not using the data given**, or ignoring units and notation (mm to micrometres, 10^-8 versus 10^-2). *Cards:* data-in-the-card items and Annexe C numeracy practice.
5. **Reasons given in the wrong direction** (lower pH read as fewer hydrogen ions; telomerase thought to break telomeres down; chromosomes re-condensing after telophase). *Cards:* cause-and-effect chain cards.
6. **Practical skill gaps** (independent versus dependent variable, accuracy versus reliability, plan diagram versus cell drawing, calibrating a graticule). *Cards:* practical-skills cards that test the planning, data and evaluation parts; hands-on manipulation is not carded.

## 7. Misconceptions
`curriculum/misconceptions.json`: 87 curated entries from 126 raw misconception statements plus omissions, each tied to an objective, with the confusion, the correct idea and a discriminating test, in our words. Left out: answering habits, practical mishaps, language slips and anything where the board's own account looks doubtful (see the register below). The correct ideas are our statements of standard biology and need two-source verification in the plan before any card is published.

## 8. Scope
`curriculum/scope-scan.json`: 12 patterns covering the 16 limits in `syllabus-facts.json` (some limits share a pattern), each tested against must-catch and must-allow examples when the file is built; 12 block publication and 0 need a person to read in context. Patterns cannot catch teaching past a limit by paraphrase, so reviewers read for it.

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
