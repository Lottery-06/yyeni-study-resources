# YYeni import state, NSSCAS Biology 8223 (as of 2026-10-18)

Our 709 flashcards (the `item_type: flashcard` items in `publish/nam-8223-nsscas-2026/flashcards/`) are mapped to YYeni lessons by topic. The 64 multiple-choice sets, short answers and practical tasks are not flashcards and are not imported.

## Where the cards are now
| Place | school / classroom | Cards | Notes |
|---|---|---|---|
| NSSCAS template | school 17, `79420c65-90b9-408f-96fb-e7d27c05a920` (id 374) | 709 | Template for school 68's classroom. 2 sections and 7 lessons added for topics 4.1-4.4 and 5.1-5.3. |
| Extra classroom, created by mistake | school 68, `3452693c-aca0-40b9-8935-5d6c76abdde0` (id 845), passcode `cc95bf41`, title "NSSCAS Biology (8223) 2026" | 709 | Made with duplicate_classroom when the backfill preview was too large. Not wanted: Jeremy wants the existing classroom used. The tools cannot delete a classroom; remove it in the admin UI or leave it. No learners in it. |
| Existing classroom (the live one) | school 68, `8a093de2-c976-4b4c-84b2-5f989b193810` | 0 of ours (500 old teacher cards untouched) | Has 10 learners. The 2 new sections and 7 new lessons now exist (lesson ids 24110-24116). Ours are NOT imported yet. |
| School 1 "NSSCAS Biology (8223)" | school 1, `8235f4c7-e478-44a5-a074-0afad5e6bb1a` | 0 | Untouched. |

Lesson ids for the existing classroom: `planning/yyeni_school68_lessons.json`. Template ids: `planning/yyeni_template_lessons.json` plus 24071-24077 for the new template lessons.

## Next step (decided with Jeremy): import our 709 cards into the existing school 68 classroom
- The batch builder is `planning/build_yyeni_import.py` (writes batches of 100; edit its lesson map to read `yyeni_school68_lessons.json` for school 68).
- The import tool takes cards as typed arguments; it cannot read files. A model has to reproduce the card JSON in each `preview_flashcard_import` call, then `confirm_flashcard_change`.
- A safety filter blocks long outputs unpredictably. Batches of 100 and 50 were blocked several times; chunks of 10 always passed and chunks of 25 passed. Use chunks of 25 or fewer, log finished chunks, relaunch after a block. Never retry by rephrasing.
- Backfill (`backfill_template`) from the template into the existing classroom is blocked: the preview is too large with 709 cards.
- The app's `max_mark` ends up as 1 or 2 only; the real mark tariff is in each card's explanation text.

## Audit of the 500 existing cards in the school 68 classroom
`review/existing-cards-audit/G1-G5.json`: per card KEEP 260 / FIX 156 / REPLACE 18 / DROP 66 (AI judgement against the syllabus, not human-verified). 420 had no Bloom level; 24 had a factual error. Archive is one card at a time (`flashcards.archive_card`, about 1,000 tokens per card, no fee, deck snapshots unchanged). Nothing has been archived.

## Not done
No deck has been created or assigned. Replacing decks for Maliro, Naame and Kaudife (school 68) needs Jeremy's approval of the N$20-per-learner fee. The claims remain unverified until a person approves them.
