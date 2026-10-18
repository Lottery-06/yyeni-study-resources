# Plan: Namibia NSSCAS Biology 8223

The brief an authoring agent works to. Generated 18 October 2026 from `work/nam-8223-nsscas-2026/curriculum/`, the contracts and the topic work orders; regenerate rather than edit (`planning/write_plan.py`). The analysis it rests on is `operations/analysis/8223-nsscas-biology-corpus-analysis.md`; the syllabus brief is `operations/analysis/8223-nsscas-biology-syllabus-brief.md`.

## 0. What the syllabus says
Transcribed from the NIED 2020 syllabus, every value with its printed page (`curriculum/syllabus-facts.json`, checked by `planning/verify_syllabus_facts.py`).

| AO | what it covers (start) | weight | Paper 1 | Paper 2 | Paper 3 |
|---|---|---:|---:|---:|---:|
| A | scientific phenomena, facts, laws, definitions, concepts and theories; scientific vocabulary, terminology and … | 40% | 50% | 50% | 0% |
| B | locate, select, organise and present information from a variety of sources; translate information from one for… | 40% | 50% | 50% | 0% |
| C | Follow a sequence of instructions,using appropriate techniques, handling apparatus and materials competently a… | 20% | 0% | 0% | 100% |

- **Paper 1, Theory: multiple choice.** 40 marks, 1 hour, 29% of the qualification (printed table). Forty four-choice items on the specific objectives, AO A and B.
- **Paper 2, Theory: structured questions.** 60 marks, 1 hour 15 minutes, 42%. Compulsory short-answer, structured and free-response questions of variable mark value, AO A and B.
- **Paper 3, Advanced practical skills.** 40 marks, 2 hours, 29%. Two experiments, AO C only. Marked by strand (Annexe A, printed p.30): manipulation, measurement and observation (MMO) 16, presentation of data and observations (PDO) 12, analysis, conclusions and evaluation (ACE) 12.
- **Three disagreements inside the syllabus, recorded not resolved:** paper weights (prose 77/23, table 29/42/29, marks 28.6/42.9/28.6), AO weights (printed 40/40/20, grid marks 35.7/35.7/28.6), and the Lincoln index cited but not given in Annexe C. Simpson's index is printed as D = 1 − (Σ n/N)², which differs from the standard form. The plan targets the printed 40/40/20.
- NSSCO Biology is recommended prior learning, not required.

## 1. What the corpus says
398 evidence records from papers 2021–2024 and the 2025 examiner report (2021–2023 papers are proof versions, 2023 has no report, 2025 has no papers). Details, limits and the register of source doubts are in the corpus analysis; the gaps are in `assessment-evidence/GAPS.md`.
- **Theme 2 carries about two thirds of Papers 1 and 2 by marks; the practical (Paper 3) and mathematical skills are the other large block.** Emphasis follows exposure; coverage is complete.
- **Paper 2 asks describe, explain and state most, at 1–3 marks, usually with more creditworthy points than marks.** Recall is a minority of the marks (the syllabus caps it at 20%).
- **The failures that recur:** answering a different question; near-neighbour terms confused; key terms and spelling; not using the data given, or units and notation; reasoning in the wrong direction; practical skill gaps.
- **87 examiner-evidenced misconceptions**, curated by hand, each with a discriminating test.

## 2. Command words and tariffs
Use only these to open a prompt. The tariff is the one the work-order slot names; every slot tariff is one the papers set for that word (Paper 2 modal where the word is a question word).

| command word | in the syllabus table | parts (P2+P3, 2021–24) | modal tariff | tariffs seen |
|---|---|---:|---:|---|
| State | yes | 22 | 1 | 1, 2, 3, 4 |
| Explain | yes | 18 | 2 | 1, 2, 3, 4 |
| Describe | yes | 27 | 1 | 1, 2, 3, 4, 5, 6, 8 |
| Discuss | yes | 4 | 2 | 2, 3, 4 |
| Outline | yes | 5 | 3 | 2, 3, 4 |
| Suggest | yes | 11 | 2 | 1, 2, 3 |
| Calculate | yes | 7 | 1 | 1, 2 |
| Compare | yes | 1 | 2 | 2 |
| Name | no (observed) | 12 | 2 | 1, 2, 4, 5 |
| Identify | no (observed) | 9 | 2 | 1, 2, 3 |

**Never open a prompt with:** Define, List, Give, Deduce, Predict, Comment, Find, Measure, Determine, Estimate, Show, Sketch, Construct, Recognise, Classify, Use, Complete, Plot, Make, Prepare, Draw, Record, Look, Fill, Take, Move. "Define" is listed in the syllabus but never opens a part in 2021–2024, so it does not open a prompt (AGENTS.md rule 5; Jeremy decided on 2026-10-18 to ask as the exams do). The papers ask for definitions as "Explain what is meant by … / the meaning of …" (four parts, 2 marks) and "State what … means" (one part, 1 mark), so a definition card opens with **State what is meant by** (1 mark) or, for a developed definition, **Explain what is meant by** (2 marks). The syllabus glossary keeps Define (a formal statement), State (a concise answer) and "what is meant by" (a definition with a comment on its significance) apart; the card's guidance names the key words that carry the mark. The practical instruction words (plot, make, prepare, draw, record, take, move, look, fill in, complete, use) are bench instructions and cannot be posed by a text card; their skills are asked as State, Describe, Explain or Calculate questions about the technique. These are verdicts from papers 2021–2024; 2023 and 2025 add no wording evidence.

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
| DEF | A definition or statement of a fact, stated precisely with the key terms | A, B, C | Remember |
| FEATURE | The features, parts or properties of a structure, with what each does | A, B, C | Remember |
| DIST | The difference between two confusable terms or structures | A, B, C | Understand |
| PROC | An ordered sequence: stages of a process or the steps of a method | A, B, C | Apply |
| WHY | The reason for a step, a structure or a condition | A, B, C | Understand |
| MECH | How something happens, explained biologically | A, B, C | Understand |
| LIM | A limitation or source of error in a procedure and what it does to the result | A, B, C | Analyse |
| APP | Using an idea on a given case, data set, diagram or specimen | A, B, C | Apply |
| CHAIN | A cause traced through to its consequence in several steps | A, B, C | Analyse |
| EVAL | Judging a claim, method or conclusion against evidence and giving a justified decision | A, B, C | Evaluate |
| CALC | A calculation with the equation, substitution, answer, unit and sensible significant figures | A, B, C | Apply |
| INTERP | Reading a graph, table, diagram or micrograph for a value, pattern or conclusion | A, B, C | Analyse |
| MISCON | Telling a correct idea from the error it is confused with | A, B, C | Understand |
| SYNTH | Two objectives joined in one problem | A, B, C | Create |

Performance tasks: multiple_choice_set = Apply; short_answer = Apply; practical_task = Analyse. A content topic gets a multiple-choice set and a structured question; a practical topic gets two practical tasks of about 10 marks (the second is a microscopy task where the topic concerns microscopy, otherwise a second investigation). Misconception cards on practical skills sit on the practical topics (independent and dependent variables, accuracy and reliability, plan diagrams versus cell drawings, graticule conversion) and on 5.1 (standard form).

## 5. The topics
32 topics: the 25 syllabus units, four practical-skills topics (4.1–4.4, from Annexe A) and three mathematical-skills topics (5.1–5.3, from Annexe C).

| topic | title | paper | objectives | items | notes words |
|---|---|---|---:|---:|---|
| 1.1 | Classification | 1/2 | 5 | 21 | 1,430–2,050 |
| 1.2 | Biodiversity | 1/2 | 6 | 27 | 1,800–2,580 |
| 1.3 | Conservation | 1/2 | 7 | 17 | 1,900–2,730 |
| 2.1 | The microscope | 1/2 | 5 | 18 | 1,590–2,270 |
| 2.2 | Cell structure | 1/2 | 10 | 34 | 2,880–4,120 |
| 2.3.1 | Fluid mosaic membranes | 1/2 | 4 | 16 | 1,190–1,700 |
| 2.3.2 | Movement of substances into and out of cells | 1/2 | 5 | 25 | 1,550–2,210 |
| 2.4.1 | Carbohydrates and lipids | 1/2 | 12 | 39 | 3,600–5,160 |
| 2.4.2 | Proteins and water | 1/2 | 8 | 30 | 2,490–3,560 |
| 2.5.1 | Mode of action of enzymes | 1/2 | 4 | 12 | 1,120–1,600 |
| 2.5.2 | Factors that affect enzyme action | 1/2 | 4 | 22 | 1,260–1,800 |
| 2.6.1 | Structure of transport tissues | 1/2 | 4 | 14 | 1,260–1,800 |
| 2.6.2 | Mechanisms of transport in plants | 1/2 | 9 | 28 | 2,760–3,950 |
| 2.7.1 | Mammalian circulatory system | 1/2 | 13 | 33 | 3,530–5,070 |
| 2.7.2 | Mammalian heart | 1/2 | 6 | 16 | 1,630–2,340 |
| 2.8.1 | Infectious disease | 1/2 | 5 | 15 | 1,440–2,070 |
| 2.8.2 | Antibiotics | 1/2 | 3 | 15 | 990–1,410 |
| 2.9.1 | The response of the immune system to pathogens | 1/2 | 4 | 15 | 1,260–1,800 |
| 2.9.2 | Antibodies and vaccination | 1/2 | 6 | 16 | 1,760–2,520 |
| 2.10.1 | The gas exchange system | 1/2 | 8 | 20 | 2,380–3,400 |
| 2.10.2 | Smoking and its impact on the gas exchange and circulatory system | 1/2 | 3 | 11 | 890–1,270 |
| 3.1.1 | Replication and division of nuclei and cells | 1/2 | 7 | 26 | 2,060–2,950 |
| 3.1.2 | Chromosome behaviour in mitosis | 1/2 | 2 | 9 | 660–940 |
| 3.2.1 | Structure and replication of DNA | 1/2 | 5 | 14 | 1,460–2,090 |
| 3.2.2 | Protein synthesis | 1/2 | 7 | 22 | 1,930–2,770 |
| 4.1 | Planning investigations and taking measurements | 3 | 12 | 37 | 3,610–5,160 |
| 4.2 | Microscopy, drawing and measuring specimens | 3 | 12 | 37 | 3,670–5,240 |
| 4.3 | Recording and presenting data | 3 | 11 | 26 | 3,440–4,910 |
| 4.4 | Analysis, conclusions and evaluation | 3 | 17 | 48 | 5,070–7,250 |
| 5.1 | Number, units and accuracy | 1/2 | 8 | 43 | 2,390–3,420 |
| 5.2 | Graphs, charts and rates of change | 1/2 | 9 | 38 | 2,450–3,510 |
| 5.3 | Size, magnification and biodiversity calculations | 1/2 | 5 | 29 | 1,430–2,050 |

**32 topics, 226 objectives, 773 items (87 misconception cards, 28 multiple-choice sets, 28 structured questions, 8 practical tasks), 66,880–95,700 words of notes.**

## 6. AO balance, in marks
| AO | planned | syllabus weight | gap |
|---|---:|---:|---:|
| A | 42% | 40% | +2 |
| B | 40% | 40% | +0 |
| C | 18% | 20% | -2 |

Content topics are examined on Papers 1 and 2 (A and B equally, no C); the four practical topics on Paper 3 (C only). The subject total answers to the printed 40/40/20 (largest gap 2 points; `curriculum/ao_coverage.md`). Never pad the bank to chase an AO.

## 7. Misconceptions, glossary and scope
- **87 examiner-evidenced misconceptions** in `curriculum/misconceptions.json`, each on its objective with a `test`. Every entry has its own MISCON slot in the work order. The correct ideas are our statements of standard biology and need two-source verification before import.
- **31 glossary terms** in `curriculum/glossary.json`, each with its settled sense (draft; needs verification).
- **12 scope patterns** in `curriculum/scope-scan.json`, carried by every contract as `excluded_constructs`; C-11 fails any learner-facing match:
  - species concepts other than the biological, morphological, ecological and behavioural concepts (syllabus, printed p.5, 1.1)
  - mesosomes (syllabus, printed p.8, 2.2)
  - calculations of water potential (syllabus, printed p.9, 2.3.2)
  - solute potential, pressure potential and osmotic potential as terms (syllabus, printed p.9, 2.3.2)
  - roles of water beyond solvent action, specific heat capacity and latent heat of vaporisation (syllabus, printed p.11, 2.4.2)
  - chloride shift (syllabus, printed p.14, 2.7.1)
  - nervous and hormonal control of the heart (syllabus, printed p.15, 2.7.2)
  - non-infectious disease examples other than sickle cell anaemia and lung cancer (syllabus, printed p.15, 2.8.1)
  - detailed life cycle of the malarial parasite (syllabus, printed p.15, 2.8.1)
  - T-lymphocyte types other than T-helper and T-killer cells (syllabus, printed p.16, 2.9.1)
  - chromosome structure beyond DNA, histone proteins, chromatids, centromere and telomeres (syllabus, printed p.18, 3.1.1)
  - structural formulae of nucleotides and bases (syllabus, printed p.19, 3.2.1)
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
