# Annex mapping brief: add practical-skill and maths-skill objectives to the evidence records

NSSCAS Biology 8223. The evidence records in `work/nam-8223-nsscas-2026/assessment-evidence/by-year/evidence_<year>.json` (read-only for you) map each question part to the 152 content objectives in `curriculum/objective_ids.json`. Paper 3 (practical, AO C) and the numeric and data-skill parts of Papers 1 and 2 mostly test skills that live in two NEW topics, whose objectives are in `curriculum/annexe-objectives.json` (74 objectives):
- **Topic 4, practical skills** (4.1 planning investigations and taking measurements; 4.2 microscopy, drawing and measuring specimens; 4.3 recording and presenting data; 4.4 analysis, conclusions and evaluation). Source: syllabus Annexe A, the Paper 3 mark strands MMO, PDO and ACE.
- **Topic 5, mathematical skills** (5.1 number, units and accuracy; 5.2 graphs, charts and rates of change; 5.3 size, magnification and biodiversity calculations). Source: syllabus Annexe C.

## Your job
For every record in your assigned set, decide **by meaning, not by word match** which annex objectives the part genuinely tests, and write them to a patch file. Examples: a part that asks the candidate to plot data tests 4.3 graph objectives; "suggest an improvement to the method" tests 4.4 improvements; calibrating a graticule tests 4.2-03/4.2-04 and 5.3-02; a magnification or actual-size calculation tests 5.3-02 (and 4.2 if it is a microscope practical); a percentage-change item tests 5.1-05; a table design part tests 4.3 table objectives; naming independent and dependent variables tests 4.1-01. A recall part about biology content tests none: skip it. Add an annex id only when the part really requires that skill; do not pad. A part may get several.

## Rules
1. Read `curriculum/annexe-objectives.json` first (each objective has its syllabus text and a plain learner objective). Use only ids from it. Never invent an id.
2. Do not edit any evidence file or any other file. Write exactly one patch file (path below) and scratch files only under `work/nam-8223-nsscas-2026/planning/_scratch/` (create it).
3. Mine, do not reproduce: your reasons are in your own words (at most one short sentence each).
4. Say when unsure. Use confidence high, medium or low; low where the record text does not make the skill clear (for example 2025 Paper 2 and 3 parts known only from report commentary).
5. Records whose notes say `PLACEHOLDER` (2025 Paper 1, no topic named) must be skipped.

## Output: one JSON file
```
{"patch_id": "...", "patches": {"<evidence_id>": {"add_objective_ids": ["OBJ-8223-4.3-06", ...], "confidence": "high|medium|low", "reason": "one sentence"}, ...}, "skipped_with_reason": {"<evidence_id>": "why none applies"}}
```
Every record in your set must appear either in `patches` or in `skipped_with_reason`.

## Report (under 200 words)
Records examined, patched, skipped; how many low-confidence; which annex objectives got no record at all; anything in the records that made mapping unclear.
