#!/usr/bin/env python3
"""Build YYeni flashcard-import batches (<=100 cards, one lesson per card) for the NSSCAS Biology template classroom (school 17) from
publish/nam-8223-nsscas-2026/flashcards. Only item_type flashcard is imported (multiple-choice sets, short answers and practical tasks are not
flashcards). Writes batch_NN.json and MAP.json into the directory given as argv[1]. Run from the repository root with plain python3."""
import json, glob, re, subprocess, sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
W = "work/nam-8223-nsscas-2026/"; P = "publish/nam-8223-nsscas-2026/flashcards/"
L = json.load(open(W + "planning/yyeni_template_lessons.json"))["lessons"]
L.update({"(L1)Planning investigations and taking measurements": 24071, "(L1)Microscopy, drawing and measuring specimens": 24072,
          "(L1)Recording and presenting data": 24073, "(L1)Analysis, conclusions and evaluation": 24074, "(L1)Number, units and accuracy": 24075,
          "(L1)Graphs, charts and rates of change": 24076, "(L1)Size, magnification and biodiversity calculations": 24077})
norm = lambda s: re.sub(r"[^a-z0-9]", "", re.sub(r"^\(l1\)", "", s.lower()))
byn = {norm(k): v for k, v in L.items()}
rev = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
BL = {"Remember": 1, "Understand": 2, "Apply": 3, "Analyse": 4, "Evaluate": 5, "Create": 6}
cards, mp = [], {}
key = lambda f: [int(p) for p in os.path.basename(f).split("-")[0].split(".")]
for f in sorted(glob.glob(P + "*.json"), key=key):
    d = json.load(open(f)); lid = byn[norm(d["topic_title"])]; n = 0
    for i in d["items"]:
        if i["item_type"] != "flashcard": continue
        expl = " ".join(i.get("marking_guidance") or [])
        cards.append({"lesson_id": lid, "question": i["prompt"], "answer": i["canonical_answer"], "explanation": expl or None,
                      "bloom_level": BL[i["blooms_level"]], "difficulty": i["difficulty"], "card_type": i["subtype"],
                      "source_metadata": {"repository": "yyeni-study-resources", "path": f, "revision": rev, "external_id": i["item_id"],
                                          "tags": ["8223", "NSSCAS Biology", "topic " + d["topic_number"]] + i["objective_ids"] + ["AO " + a for a in i["assessment_objectives"]]
                                                  + [i["command_word"], "%s mark%s" % (i["mark_tariff"], "" if i["mark_tariff"] == 1 else "s")]}})
        n += 1
    mp[d["topic_number"]] = {"lesson_id": lid, "cards": n}
for c in cards:
    if c["explanation"] is None: del c["explanation"]
batches = [cards[i:i + 100] for i in range(0, len(cards), 100)]
for k, b in enumerate(batches, 1): json.dump(b, open("%s/batch_%02d.json" % (OUT, k), "w"), ensure_ascii=False)
json.dump({"total": len(cards), "batches": len(batches), "per_topic": mp, "revision": rev}, open(OUT + "/MAP.json", "w"), indent=1)
print("cards", len(cards), "batches", len(batches), "revision", rev)
