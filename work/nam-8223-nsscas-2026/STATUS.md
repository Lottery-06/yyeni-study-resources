# STATUS — 8223 Biology (Namibia NSSCAS)
Workspace: work/nam-8223-nsscas-2026/   Owner: Jeremy   Authoring tool: Claude (Claude Code)

Second NSSCAS subject, run in parallel with the 8224 Chemistry pilot. Vitalis agreed (confirmed by Jeremy, 2026-10-18). Scope: the whole subject. This workspace began before the playbook was read; earlier files (`CLAIM.md`, `curriculum/SYLLABUS-SUMMARY.md`, `assessment-evidence/THEME-3-PAPER-ANALYSIS.md`, `working-notes/`) are working notes. They do not replace `syllabus-facts.json` or the corpus analysis. Process: TEAM-PLAYBOOK.md for how, and Jeremy's workflow diagram for the order and extra gates (steps 8–9 below).

- [x] 0 Claim: tracker row added (uncommitted) — 2026-10-18
- [x] 1 Sources found — 2026-10-18 (syllabus NIED 2020, signed off 26 Nov 2020; 15 files: Papers 1–3 for 2021–2024, two Paper 3 teachers' instructions and an extra 2022 Paper 3; 0 standalone mark schemes; examiner reports for 2021, 2022, 2024 and 2025 (2023 not found); 0 revision notes). Drive checked, nothing extra.
- [x] 1 YOU: sources complete — Jeremy, 2026-10-18 (2023 examiner report not found; recorded gap)
- [x] 2 Syllabus facts written (`curriculum/syllabus-facts.json`; 264 quotes verified against the PDF by `planning/verify_syllabus_facts.py`; Codex review 2026-10-18 found 8 problems, all fixed; brief at `operations/analysis/8223-nsscas-biology-syllabus-brief.md`) — 2026-10-18
- [x] 2 YOU: AO table and paper table checked against the PDF (printed pp. 20-23) — Jeremy, 2026-10-18
- [x] 3 Corpus analysis written (`operations/analysis/8223-nsscas-biology-corpus-analysis.md`; 404 evidence records, 5 mining agents; curriculum files: exam-exposure, misconceptions (87), scope-scan (14), answer-shapes; gaps in assessment-evidence/GAPS.md) — 2026-10-18
- [x] 3 YOU: analysis read; sounds like the exam learners sit — Jeremy, 2026-10-18
- [x] 4 Plan built (AO gap: 2 points; 32 topics, 226 objectives, 772 items; PLAN-8223-nsscas-biology.md, HANDOVER-8223-nsscas-biology.md, exemplar/ passes the suite) — 2026-10-18
- [x] 4 YOU: plan approved — Jeremy, 2026-10-18 ("i think we can start now"; decisions 1-6 recorded above)
- [ ] 4 YOU: plan committed (not yet; Jeremy to commit; authoring started before the commit at his instruction)
- [x] 5 Topics authored: 32 / 32, every topic DECISION: PUBLISH on re-run (C-18 AO-mix warning only; C-35/41/43 not_run). Claim source labels normalised to NSSCAS-8223-SYLLABUS-2020. Author flags for the reviewer in working-notes/REVIEW-FLAGS.md — 2026-10-18
- [x] 5 Published: `publish/nam-8223-nsscas-2026` (32 topics, 772 items, 86,137 words of notes) — 2026-10-18
- [x] 6 Reviewed by Codex: verdict publish — 2026-10-18 (32/32 topics PUBLISH; completeness and copied-wording audits clean; learner-facing defects repaired and republished; Biology-specialist truth findings remain mandatory before learner import; report: `review/STEP-6-REVIEW-REPORT.md`)
- [ ] 6 YOU: verdict read
- [ ] 7 YOU: committed and pushed
- [ ] 8 (diagram) Compare with existing YYeni NSSCAS Biology cards (school 17, classroom `79420c65-90b9-408f-96fb-e7d27c05a920`; 0 cards on 2026-10-18)
- [ ] 8 (diagram) YOU: approve replacements, preview and import into YYeni

## Quality additions agreed 2026-10-18 (beyond the playbook)
- Codex review content fixes go back to the author (Claude), and Codex re-checks them.
- Every claim needs two sources; `single_source` claims cannot publish (no 2021–2024 board mark schemes exist).
- A human Biology check of a sample of answers before import (Maths 6131 used a 95% bar); until then cards import as AI-reviewed only.
- Every generated diagram is viewed by a person, not only checked by the data checks.
- Diagrams are generated from data (RS-47). Photomicrographs are a stated gap.

## Step 4 decisions (Jeremy, 2026-10-18)
Diagrams: text-complete cards, diagrams generated after authoring. Simpson's index: the form the paper prints (the syllabus form gives D = 0 always); Jeremy confirmed. Lincoln: method plus formula in card. AO C: printed 20%. Reviewer: Codex only for now; a human Biology check to be worked out. Define does not open a prompt (Jeremy reversed an earlier exception): definitions are asked as the exams ask them, State what is meant by / Explain what is meant by. Simpson's index follows the form the paper prints (confirmed).

## Review policy (Jeremy, 2026-10-18)
No further Codex or independent reviews at the early stages (facts, analysis, plan). The syllabus-facts review in flight is the last one before the build. The next Codex review is the step 6 cross-review after authoring and the required quality checks. Early stages rely on deterministic checks and the YOU checkpoints.

## Open items
- YOU: the examiner reports are in `sources/` inside this workspace (2021, 2022, 2024, 2025). Agents never write to top-level `sources/`; file it by hand under `sources/namibia/nsscas/8223-biology/assessment/2025/` and log it. It was fetched by hand, not with the harvester (SOURCES.md).
- Qualification profile draft needs the six fixes listed at the top of `qualification-profile.yaml`; rebuild it in step 4.
- Examiner reports: 2021, 2022, 2024 and 2025 are in `sources/` (Wayback copies of the official files; see SOURCES.md). 2023 was not found (the Ministry listing has none; only a gated Scribd copy). Person to file the four reports by hand under top-level `sources/` and log them.
- Syllabus summary reviews by Codex: two rounds complete, the third (confirming) did not finish. Its two known findings were fixed. Superseded by step 2 (syllabus facts).
- `operations/SUBJECT-TRACKER.md` is modified by another session too (8224 row); neither row is committed.
