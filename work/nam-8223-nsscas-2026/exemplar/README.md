# 8223 structural exemplar

Two small slices that pass the full check suite. They show the SHAPE of authored material for NSSCAS Biology 8223. They are not content to reuse.

**3.1.2 Chromosome behaviour in mitosis** (a content topic, Papers 1 and 2, AO A and B). A complete topic to its real work order: 2 objectives, 7 claims, 1 content unit of 9 blocks (778 words in a 660-940 budget), 9 items: five flashcards (PROC, MECH, APP, DEF, MISCON) and two INTERP cards, a 12-question multiple-choice set and an 8-mark structured question. The MISCON card is built from entry MC-8223-3.1.2-01 as a discrimination: the error, the correct idea, the test.

**4.3 Recording and presenting data** (the Paper 3 practical topic, AO C). A small slice of three objectives only: OBJ-8223-4.3-01 (raw data table, no units in the body), OBJ-8223-4.3-05 (significant figures for calculated values) and OBJ-8223-4.3-07 (axes and labelling). 7 claims, 1 unit of 10 blocks (1004 words in a 960-1370 budget), 7 flashcards (FEATURE, APP, DEF, CALC) and one 10-mark practical task with our own invented readings in a markdown table, labelled as ours. The contract and work order for this slice were built from a reduced registry (the container and the three children), so slot ids and tariffs are the generator's own. The microscopy task slot (P02) the generator also plans is not written: none of the three objectives exercises it.

## The field set to copy

Claim: claim_id, objective_ids, text, claim_type, provenance ("generated_gap"), evidence ([]), derived_from_claim_ids ([]), revision (1), verification {status "unverified", method, reviewer_id null, reviewed_at null, confidence}, publishable false, notes. Every claim here carries `verification.status: "unverified"` and a note `verification_state: single_source`, so the publication gate (C-24) holds and nothing could be published on the strength of it.

Content unit: unit_id, title, objective_ids, level, core_status, objective_type, depth_tier, word_budget {min, target, max}, blocks, word_count (headings plus text, as C-26 counts them), qa_status, notes. Block: block_id, block_type, heading, text, claim_ids, context_tags, assessment_objectives, claims_seen, authored_hash.

Item: item_id (the slot id), objective_ids, claim_ids, item_type, subtype (null for the multiple-choice set, short answer and practical task), assessment_objectives (the letters A, B, C as the work order gives them, not AO1), blooms_level, command_word (null for the multiple-choice set), mark_tariff (the number of questions for the multiple-choice set), difficulty, prompt, canonical_answer, marking_guidance (a list), context, prerequisite_item_ids, core_status, intentional_duplicate_group, provenance, qa_status "review_required", claims_seen, authored_hash. Hash: sha256 of `_artefact_text(x)` exactly as in the AUTHOR role brief.

## What to copy, and what not to copy

Copy: the field set; one item per slot with the slot's five labels carried unchanged; marking guidance that names the parts the work order lists, in those words; a MISCON card that states the error, the correct idea and the test; a multiple-choice set with its key and a reason for the key and for each distractor; a structured question whose guidance gives the marks per part and says which parts credit which AO; a practical task whose readings are in a markdown table and are labelled as ours; arithmetic written as "a ÷ b = c" with c unrounded, then rounded in a following clause; no units in the body of a data table; units in singular SI form.

Do not copy: the facts. Every statement is illustrative and unverified, written from our own knowledge of standard biology with no second source. Do not copy the situations (the Katima Mulilo squash, the pondweed readings, the potometer figures) into other topics, and do not copy the wording or volume; the work order sets the budget.

These folders sit outside `topics/`, so `publish_subject.py` never sees them.

## The commands that prove the pass

The checks need the workspace under work/ and read the subject code from its folder name, so each slice was installed in a scratch copy, the real workspace was left untouched, and the scratch copies were deleted afterwards. From the repository root:

    python3 standard/v0.2.0-draft/build/render_notes.py work/nam-8223-nsscas-2026-exscratch 3.1.2
    python3 standard/v0.2.0-draft/checks/run_checks.py work/nam-8223-nsscas-2026-exscratch 3.1.2
    python3 standard/v0.2.0-draft/checks/what_to_fix.py work/nam-8223-nsscas-2026-exscratch 3.1.2

Scratch 3.1.2: qualification-profile.yaml, subject-profile.yaml, curriculum/, assessment-evidence/ and topics/3.1.2 (contract and work order) copied from this workspace, then the slice copied into topics/3.1.2/.

    python3 standard/v0.2.0-draft/build/conform_registry.py work/nam-8223-nsscas-2026-exscratch43
    python3 standard/v0.2.0-draft/build/make_contract.py work/nam-8223-nsscas-2026-exscratch43
    python3 standard/v0.2.0-draft/build/make_work_order.py work/nam-8223-nsscas-2026-exscratch43 4.3
    python3 standard/v0.2.0-draft/build/render_notes.py work/nam-8223-nsscas-2026-exscratch43 4.3
    python3 standard/v0.2.0-draft/checks/run_checks.py work/nam-8223-nsscas-2026-exscratch43 4.3
    python3 standard/v0.2.0-draft/checks/what_to_fix.py work/nam-8223-nsscas-2026-exscratch43 4.3

Scratch 4.3: the same copy, with curriculum/objective_registry.json cut to OBJ-8223-4.3 and its children -01, -05 and -07 before the three build commands. The contract's item_budget and required_outputs.learning_items were then set to 8, the number written (the generator plans 9, counting the microscopy task).

Result for both: 40 PASS, 3 NOT_RUN (C-35, C-41, C-43: no graphical stimulus, depiction or practice text), 1 WARN (C-18, the AO mix by item count, reported not targeted), DECISION PUBLISH, and `what_to_fix.py` printed "Nothing left to fix" and exited 0. PUBLISH here means the checks pass, not that the biology is verified.
