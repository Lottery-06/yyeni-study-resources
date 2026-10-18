#!/usr/bin/env python3
"""Run after make_work_order.py --all. Adds the slots the generator cannot ask for, as decided at the step 6 review, and keeps the
contract's item budget in step (C-34 compares it with the build). Each added slot clones an existing slot of the same objective.
Idempotent. Run from the repository root with plain python3."""
import json
W = "work/nam-8223-nsscas-2026/topics/"
# topic -> (slot to clone, [(new slot number and subtype, reason)])
EXTRA = {"2.6.1": ("ITEM-8223-2.6.1-001-INTERP", [("011-INTERP", "leaf"), ("012-INTERP", "leaf proportions")])}
REASON = "added after the step 6 review: objective 2.6.1-01 names leaves, but the generated interpretation slots cover a stem and a root only"
for topic, (src, new) in EXTRA.items():
    wp, cp = W + topic + "/work_order.json", W + topic + "/contract.json"
    w = json.load(open(wp)); c = json.load(open(cp))
    have = {s["slot"] for s in w["item_slots"]}
    base = next(s for s in w["item_slots"] if s["slot"] == src); added = 0
    for num, _ in new:
        sid = "ITEM-8223-%s-%s" % (topic, num)
        if sid in have: continue
        s = dict(base); s["slot"] = sid; s["reason"] = REASON; w["item_slots"].append(s); added += 1
    if added:
        w["planned_item_count"] += added
        c["depth_constraints"]["item_budget"] += added; c["required_outputs"]["learning_items"] += added
        json.dump(w, open(wp, "w"), indent=2, ensure_ascii=False); json.dump(c, open(cp, "w"), indent=2, ensure_ascii=False)
        open(W + topic + "/work_order.md", "a").write("\n\n**Added after the step 6 review (planning/add_extra_slots.py):** %s. Slots: %s.\n" %
                                                      (REASON, ", ".join("ITEM-8223-%s-%s" % (topic, n) for n, _ in new)))
    print(topic, "slots added:", added, "item budget:", c["depth_constraints"]["item_budget"])
