# 8223 NSSCAS Biology — syllabus brief

Source: NSSCAS Biology Syllabus 8223, NIED 2020, signed off 26 November 2020, Advanced Subsidiary level, Grade 12, first examination 2021. Every value below is in `work/nam-8223-nsscas-2026/curriculum/syllabus-facts.json` with its printed page and verbatim line, and `planning/verify_syllabus_facts.py` re-opens the PDF to prove each quote (266 checked, 0 missing). The checker also ties every number to its cited cell, compares counts with a separately typed list, rejects footer text inside a value, and proves that every character on each content page is accounted for by a recorded objective or heading, so a split, dropped or truncated objective fails. It cannot machine-verify the Simpson formula (the text layer drops the fraction): that is held twice and was checked by eye from the page image and by Codex.. Page numbers are the numbers printed on the syllabus pages.

## Qualification
A one-year course after NSSCO, about 180 guided learning hours (p. 3). NSSCO Biology is recommended prior learning, not required (p. 3). Grades a to e (p. 3). All learners sit Papers 1, 2 and 3 (p. 22).

## Papers (p. 22–23)
| Paper | Questions | Duration | Marks | AO marks A / B / C (grid, p. 23) | Weight, printed table (p. 23) |
|---|---|---:|---:|---|---:|
| 1 Theory: multiple choice | forty four-choice items on the specific objectives | 1 hour | 40 | 20 / 20 / 0 | 29% |
| 2 Theory: structured | compulsory short-answer, structured and free-response questions of variable mark value | 1 hour 15 min | 60 | 30 / 30 / 0 | 42% |
| 3 Advanced practical skills | two experiments from different areas of Biology; collect, record and analyse data | 2 hours | 40 | 0 / 0 / 40 | 29% |
| Total | | | 140 | 50 / 50 / 40 | |

## Assessment objectives (p. 20–21, weights p. 23)
| AO | Name | Printed weight |
|---|---|---:|
| A | Knowledge with understanding (A1–A5), not more than 20% recall | 40% |
| B | Handling information and solving problems (B1–B8) | 40% |
| C | Practical (experimental and investigative) skills and abilities (C1–C5) | 20% |

Papers 1 and 2 test A and B only. Paper 3 tests C only. The syllabus says the grid gives only "a general idea" and "the balance on each paper may vary slightly" (p. 23), and states "a greater weighting of 60 per cent for skills ... compared to 40 per cent for knowledge and understanding" (p. 23).

## Two disagreements and one qualifier inside the syllabus
1. Paper weights: prose says Papers 1 and 2 = 77% and Paper 3 = 23%; the table says 29 / 42 / 29; the marks give 28.6 / 42.9 / 28.6.
2. AO weights: printed 40 / 40 / 20; the grid's marks (50 / 50 / 40 of 140) give 35.7 / 35.7 / 28.6.
3. Qualifier: the syllabus says the specification grid gives only "a general idea" and "the balance on each paper may vary slightly" (p. 23). That qualifies the AO grid (disagreement 2). It does not qualify the paper-weight disagreement (1).
The plan targets the **marks** in the grid for per-paper AO splits and records the printed percentages as printed; it does not choose between the conflicting percentages silently.

## Command words (section 10 glossary, p. 25–26)
24 entries: Define; What do you understand by / What is meant by; State; List; Explain; Give a reason / give reasons; Describe; Discuss; Outline; Deduce; predict; Comment; Suggest; Find; Calculate; Measure; Determine; Estimate; Show; Sketch; Construct; Compare; Recognise; Classify. The syllabus calls the glossary "neither exhaustive nor definitive", and says meaning depends partly on context. Which of these may open a flashcard is decided by the corpus analysis (AGENTS.md rule 5), not by this list.

## Content (p. 4–19)
3 themes, 25 leaf units, 152 specific objectives and 27 general objectives.
- Theme 1 Classification of living organisms: 1.1 Classification (5), 1.2 Biodiversity (6), 1.3 Conservation (7).
- Theme 2 Organisation and maintenance of the organism: 2.1 The microscope (5), 2.2 Cell structure (10), 2.3.1 Fluid mosaic membranes (4), 2.3.2 Movement of substances (5), 2.4.1 Carbohydrates and lipids (12), 2.4.2 Proteins and water (8), 2.5.1 Mode of action of enzymes (4), 2.5.2 Factors that affect enzyme action (4), 2.6.1 Structure of transport tissues (4), 2.6.2 Mechanisms of transport in plants (9), 2.7.1 Mammalian circulatory system (13), 2.7.2 Mammalian heart (6), 2.8.1 Infectious disease (5), 2.8.2 Antibiotics (3), 2.9.1 Response of the immune system (4), 2.9.2 Antibodies and vaccination (6), 2.10.1 The gas exchange system (8), 2.10.2 Smoking (3).
- Theme 3 Development of the organism and the continuity of life: 3.1.1 Replication and division of nuclei and cells (7), 3.1.2 Chromosome behaviour in mitosis (2), 3.2.1 Structure and replication of DNA (5), 3.2.2 Protein synthesis (7).

Stated limits inside the content (16, each with page): species concepts; sampling methods; conservation examples; mesosomes; water-potential calculations; solute potential; properties of water; chloride shift; malarial life cycle; heart control (SAN, AVN, Purkyne tissue, but not nervous or hormonal control); non-infectious disease examples; T-cell types; chromosome components; nucleotide and base structural formulae. Stated content requirements (7): Simpson's formula will be provided; movement of water to be described in terms of water potential (with solute potential not expected); haemoglobin as two alpha and two beta chains, with collagen molecules distinguished from collagen fibres; the lock-and-key and induced-fit hypotheses included; symplastic and apoplastic pathways and the Casparian strip included; heart control by SAN, AVN and Purkyne tissue; the four stage names of mitosis expected. Both lists are in `syllabus-facts.json` (`limits_stated_in_content`, `content_requirements_stated`).

**Formula printed in the syllabus.** The syllabus (p. 5) prints Simpson's Index of Diversity as D = 1 - (Σ n/N)², with the square outside the brackets. The standard index squares each term and then sums: D = 1 - Σ(n/N)². Recorded as printed in `formulas_as_printed` (verified from the page image, since the text layer drops the fraction). The plan must decide how a card handles it; it is not silently corrected here.

**Inconsistency in the syllabus.** The 1.2 objective sends the learner to the Mathematical requirements for the Lincoln index, but Annexe C (p. 43) contains no Lincoln index and does not say it will be supplied; only Simpson's index appears there (confirmed by searching the Annexe C pages). Recorded as `SYL-LINCOLN-XREF`. Until a source says otherwise, a learner may need to know the Lincoln formula.

## Annexes (not transcribed into the facts file)
Annexe A practical assessment (p. 27–38, ending with the Paper 3 invigilator's report form), Annexe B Paper 3 apparatus (p. 39; the contents page wrongly lists p. 37), Annexe C mathematical requirements (p. 43), Annexe D terminology, units and presentation of data (p. 44–46). They carry skills the cards must respect (magnification, percentage error, graph and table conventions) and will be read into the plan in step 4.
