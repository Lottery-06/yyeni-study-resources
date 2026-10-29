# Subject tracker

Who is doing which subject. Claim a subject **before** you start it (playbook step 0): add or edit its row, then commit and push this file on its own straight away. Two people must never work on the same subject.

Each subject's detailed progress is in `work/<workspace>/STATUS.md`. This file only records who owns what.

- **Status values:** `in progress`, `blocked` (with a note), `published`.
- **Team:** Vitalis, Jeremy, Justus, Lotto.

## Pilots

The first subject of each new kind is run by Vitalis before the team scales that kind (playbook section 6). Mark a kind `piloted` when its pilot publishes.

| Kind | Pilot subject | Status |
|---|---|---|
| Cambridge IGCSE / AS | 9702 AS Physics and others below | piloted |
| Namibia NSSCO | 6116 Biology — pilot run by Lotto under a recorded exception to the Vitalis-only rule (Lotto, 2026-10-16); repository review copy only, with learner release still open; see `work/nam-6116-nssco-2026/STATUS.md` | piloted |
| Namibia NSSCAS | | not yet |
| Junior secondary, grades 8 to 9 | | not yet |
| Upper primary, grades 4 to 7 | | not yet |

## In progress and backlog

| Board and level | Code | Subject | Workspace | Owner | Authoring tool | Status | Notes |
|---|---|---|---|---|---|---|---|
| Cambridge IGCSE | 0500 | First Language English | `cie-0500-igcse-2024-2026` | Vitalis | | in progress | planned; check its STATUS.md or the latest run before claiming |
| Namibia NSSCO | 6117 | Chemistry | `nam-6117-nssco-2026` | Lotto N. Nanghonda Jr. | Codex | in progress | Owner confirmed 2026-10-24; Step 3 approved 2026-10-26; Step 4 approved 2026-10-26; nine-card prototypes approved 2026-10-26; Step 5 authored and editorial repairs complete 2026-10-29: 12 topics, 808 cards + 36 activities; independent re-verification pending; publication hold; see FINAL-EDITORIAL-HANDOVER-6117.md |

## Published

| Board and level | Code | Subject | Workspace | Authoring tool | Reviewed by | Items | Notes |
|---|---|---|---|---|---|---:|---|
| Cambridge AS | 9609 | Business | `cie-9609-as-2026-2028` | | Codex | | pilot subject |
| Cambridge AS | 9618 | Computer Science | `cie-9618-as-2026` | Hermes / OpenCode | Claude | 759 | |
| Cambridge AS | 9702 | Physics | `cie-9702-as-2025-2027` | Hermes / OpenCode | Claude | 860 | |
| Cambridge AS | 9093 | English Language | `cie-9093-as-2024-2026` | Hermes / OpenCode | Claude | 417 | |
| Cambridge IGCSE | 0460 | Geography | `cie-0460-igcse-2025-2026` | Hermes / OpenCode | Claude | 629 | |
| Cambridge IGCSE | 0450 | Business Studies | `cie-0450-igcse-2026` | Hermes / OpenCode | Claude | 913 | |
| Cambridge IGCSE | 0455 | Economics | `cie-0455-igcse-2026` | Hermes, then Codex | Claude | 674 | 46 diagrams in `publish/cie-0455-igcse-2026/diagrams/` |
| Namibia NSSCO | 6116 | Biology | `nam-6116-nssco-2026` | Codex, with Claude repair rounds | Claude Step 6 (also repaired) | 851 | Repository review copy under `work/`, 886 authored and 35 figure items held; pilot process complete under operator override; unverified and not released to learners. |

Historical Chemistry 6117 review repair update (2026-10-27; superseded by final handover 2026-10-29): authored bank repaired for re-verification; publication held. Full audit of 1,008 responses and 146 rewritten cards gives recall 23.31%; all QA reports hold for independent re-verification. See work/nam-6117-nssco-2026/REVIEW-REPAIRS-6117.md.
