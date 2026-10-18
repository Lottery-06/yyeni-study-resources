# Step 6 cross-review — NSSCAS Biology 8223

Reviewer: Codex  
Authoring tool: Claude  
Date: 2026-10-18  
Verdict: **PUBLISH**

This verdict means the Codex cross-review gate is clean: all 32 topics pass the deterministic publication checks after repair, the work-order completeness audit passes, and the revised subject has been republished. It does **not** replace the planned human Biology truth check. The specialist findings below must be adjudicated before learner import.

## Review coverage and final state

- Read every topic’s complete notes and at least 20 learning items per topic, or every item where fewer than 20 existed. All items were read in topics 3.2.1 and 5.3 where the numerical/sequence audit required it.
- Recomputed worked figures while reading. Every worked number in the 5.3 notes, prompts and answers received a separate hand audit; the detailed ledger is in `working-notes/REVIEW-PROGRESS.md`.
- Final build: 676 claims, 32 content units, 772 learning items and 86,101 words of notes.
- Final checks: `DECISION: PUBLISH` for all 32 topics. No topic is blocked.
- Completeness script: PASS. Every work-order slot has exactly one item with the planned subtype, AO labels, Bloom level, command word and tariff; there are no undocumented extra items or label changes.
- Republished to `publish/nam-8223-nsscas-2026` after the repairs.

## Warnings

- C-18 warns in every topic because each topic’s item-level AO mix differs from the qualification-wide 40/40/20 target. Practical topics 4.1–4.4 are necessarily 100% AO C; most content topics contain no AO C. This is a visible planning/distribution warning, not a failed check.
- C-35, C-41 and C-43 are `NOT_RUN` where a topic has no graphical task, generated depiction or practice text. No generated diagram exists for a person to inspect in this build.
- C-24 confirms the gate holds: the 676 generated-gap claims remain unverified/non-publishable until documented human approval. This is especially important for the specialist list below.

## Copied-wording review

The final scan covered 19 official assessment files: 15 papers/teachers’ instructions and four examiner reports. It found 23 runs of 8+ words and **zero runs of 12+ words**.

The 8–11-word runs were allowed because they are one of the following, rather than reproduced question language:

- fixed scientific/mathematical terms or instructions: “number of species and their relative abundance”, surface-area:volume calculation wording, cell-surface-membrane/cytoplasm wording, and enzyme-reaction wording;
- generic task/stem language: an electron micrograph of a cell, concentration affecting reaction rate, or a trend in surface-area:volume ratio;
- canonical labels: prophase, metaphase, anaphase and telophase;
- numeric sequences in original data tables.

The earlier 4.3 and 4.4 significant-figures phrasing was correctly paraphrased and retained.

## Findings

| Severity | Topic/location | Finding | Disposition |
|---|---|---|---|
| High | 2.2 | Bacteria were described as lacking only “double membrane-bound” organelles. | Fixed in the earlier partial review to “no membrane-bound organelles”; claim revision and citations verified. |
| High | 1.3, item 010 | The answer supplied a decisive fact absent from the prompt: that Salvinia had no predators or competitors. | Fixed. The answer now uses only the stated mat and the light → plant death → reduced oxygen/food → biodiversity chain. |
| Medium | 2.5.2 | The alginate/diffusion cross-reference pointed to membrane structure (2.3.1), not movement across membranes. | Fixed to 2.3.2. |
| High | 2.10.1 | Notes/card said air alone holds alveoli open. | Fixed. The text now teaches only the supported elastic-fibre stretch/recoil role; surfactant/pressure context is left for specialist scope judgement. |
| Medium | 4.3 | Examiner-report wording around significant figures was too close. | Earlier paraphrase verified and retained. |
| Medium | 4.4 | Broken cross-reference to nonexistent topic 2.5. | Earlier correction to 2.5.1 and 2.5.2 verified and retained. |
| High | 4.4, block 18/item 043 | Keeping a lamp at one distance was said to make irradiance equal through red, green and blue filters. Filters transmit different amounts. | Fixed. The method now measures irradiance at the pondweed and adjusts lamp output, while standardising temperature and other variables. |
| High | 4.4, claims 020/021 and derivatives | A small percentage derived from half a scale division was said to prove closeness to the true value. It constrains only that reading uncertainty; calibration/systematic errors can remain. | Fixed. Claims raised to revision 2; all citations updated or recorded as reviewed unchanged. |
| Medium | 5.1, claim 004 and derivatives | Standard-form exponent was called a “whole number” while negative exponents were taught. | Fixed to “integer”; claim raised to revision 2 and all derivatives reviewed/restamped. |

## Truth findings requiring a Biology specialist

These are not hidden behind the PUBLISH verdict. They require subject-specialist or authoritative-source adjudication before import.

### Highest priority

1. **Carbon monoxide and haemoglobin — 2.7.1/2.10.2.** The syllabus wording says CO reduces haemoglobin’s affinity for oxygen. Accepted physiology is that CO occupies haem sites and increases the oxygen affinity of remaining sites, impairing unloading, as well as reducing carrying capacity. The present notes teach reduced carrying capacity but omit the remaining-site affinity effect. A specialist must decide the board-facing answer.
2. **Simpson’s Index — 1.2/5.3.** Confirm the board’s intended placement of the square. The resource uses `D = 1 − Σ(n/N)²`, which produces meaningful values; it explains why a literal alternative reading would produce zero for every sample. Jeremy previously approved the paper-used form, but a Biology specialist should sign it off.
3. **Lysosomes in plant cells — 2.2.** The material says plant and animal electron micrographs may show lysosomes. Many school accounts reserve conventional lysosomes for animal cells and treat the plant lytic vacuole as the counterpart.
4. **Maternal immunity example — 2.9.2.** Systemic infant protection against measles is chiefly associated with placental IgG; breast-milk antibodies chiefly protect mucosal surfaces. The worked classification example needs specialist wording.
5. **HbA/HbS sequence — 3.2.2.** Independently verify the codon table, 146-amino-acid beta-globin length, 438 coding bases plus stop, and the displayed HbA template `TGA GGA CTC CTC TTC` → HbS `TGA GGA CAC CTC TTC` sequence/orientation.

### Additional specialist/source checks

- **Ecology/conservation:** Namibian/regional examples in 1.3; simplified biodiversity–stability and concentration-along-food-chain terminology.
- **Cell/molecular biology:** microscope performance figures (2.1); insulin/liver-cell signalling simplification (2.3.1); hydrophobic “interaction” wording and biuret threshold (2.4.2); Km/affinity and pure non-competitive model (2.5.2); vacuolar transport pathway terminology (2.6.2); helicase/polymerase-only replication simplification and triphosphate detail (3.2.1).
- **Plant/animal physiology:** approximate vessel, cell, alveolar, heart-wall, AVN-delay, oxygen-curve and altitude values (2.7–2.10); “Purkyne/Purkinje” exam-facing spelling; tar/irritant and nicotine/platelet claims.
- **Disease/immunity:** measles 95% threshold, Plasmodium temperature threshold, protoctist terminology, simplified penicillin/course-completion advice, macrophage antigen-presentation emphasis, and added antibody-chain detail (2.8–2.9).
- **Cell division/genetics:** G2/telomerase simplification, nuclear-envelope timing convention, and the left-to-right codon/anticodon convention that suppresses 5′/3′ orientation (3.1–3.2).
- **Practicals/mathematics:** board conventions for risk labels, biological drawings, graph joins/tolerances, significant figures, half-smallest-division “actual error”, anomaly exclusion, equal-width histogram treatment, and whether surface-area:volume should be written as `x : 1` or with reciprocal-length units.
- **Approximate constants/examples:** branch frequencies in amylopectin/glycogen, lipid energy comparison, water-property values, water potentials and specimen dimensions.

## Plan problems and deviations

- Topic 2.6.1’s objective covers stem, root and leaf tissue distribution, but dedicated interpretation slots cover stem and root only. Leaf structure is taught in the notes and practised inside P01, so this is not a current missing-content defect; a future plan should distribute the leaf interpretation explicitly.
- The 1.3 and 4.4 work-order command choices sometimes disagree with the objective registry. The author followed the approved work order and recorded the deviations in `authoring_notes.json`; no reviewer label was changed.
- Topic 4.1’s work order triggers a diagram-modality check although the Biology build has no diagram renderer. Its apparatus arrangement is reconstructible from prose, but a future plan should decide whether to generate a diagram or remove the modality expectation.
- Topic 5.2’s contract lists Plot/Draw/Sketch/Construct/Use/Complete while the handover forbids those as item openers. The authored cards use permitted command words and the described graphs are reconstructible, but the planning inputs should be reconciled in a later version.

No plan problem is serious enough to require rebuilding the current subject before the cross-review verdict. The separate human Biology gate in `STATUS.md` remains mandatory before learner import.
