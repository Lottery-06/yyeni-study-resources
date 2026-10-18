#!/usr/bin/env python3
"""Step 6 slot/label completeness audit for NSSCAS Biology 8223."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = (
    "subtype",
    "assessment_objectives",
    "blooms_level",
    "command_word",
    "mark_tariff",
)


def load(path):
    return json.loads(path.read_text())


problems = []
for topic_dir in sorted((ROOT / "topics").iterdir(), key=lambda p: p.name):
    if not topic_dir.is_dir():
        continue
    topic = topic_dir.name
    work_order = load(topic_dir / "work_order.json")
    items_path = next((topic_dir / "learning-items").glob("*.json"))
    items = load(items_path)["items"]
    notes_path = topic_dir / "authoring_notes.json"
    notes = load(notes_path) if notes_path.exists() else {"deviations": []}
    notes_text = json.dumps(notes, sort_keys=True)

    slots = {
        slot["slot"]: slot
        for group in ("item_slots", "performance_tasks")
        for slot in work_order.get(group, [])
    }
    by_id = {}
    for item in items:
        by_id.setdefault(item["item_id"], []).append(item)

    for slot_id, slot in slots.items():
        matches = by_id.get(slot_id, [])
        if len(matches) != 1:
            problems.append(f"{topic}: {slot_id} has {len(matches)} items (expected 1)")
            continue
        item = matches[0]
        for field in FIELDS:
            if field in slot and item.get(field) != slot[field]:
                documented = slot_id in notes_text and field in notes_text
                problems.append(
                    f"{topic}: {slot_id} {field}: planned={slot[field]!r}, "
                    f"actual={item.get(field)!r}, documented={documented}"
                )

    for item_id, matches in by_id.items():
        if item_id not in slots:
            documented = item_id in notes_text
            problems.append(
                f"{topic}: unplanned item {item_id} x{len(matches)}, documented={documented}"
            )

if problems:
    print("\n".join(problems))
    raise SystemExit(1)
print("PASS: every planned slot has exactly one item; no undocumented extra item or label change.")
