#!/usr/bin/env python3
"""Run after make_contract.py. make_contract lists every command word observed anywhere in the papers (including the procedural
instructions inside Paper 3 practicals: Plot, Draw, Use, Complete ...) as in scope. The handover forbids those as prompt openers
(AGENTS.md rule 5: only words the papers use to open a question part), and the framework already says so in use_in_prompts. This
makes each contract agree: command_words_in_scope keeps only the openers, and the rest are listed as procedural wording.
Run from the repository root with plain python3."""
import json, glob
W = "work/nam-8223-nsscas-2026/"
fw = json.load(open(W + "curriculum/assessment-framework.json"))
openers = [c["word"] for c in fw["command_words"] if c.get("observed_count", 0) > 0 and c.get("use_in_prompts")]
procedural = [c["word"] for c in fw["command_words"] if c.get("observed_count", 0) > 0 and not c.get("use_in_prompts")]
n = 0
for p in sorted(glob.glob(W + "topics/*/contract.json")):
    c = json.load(open(p)); a = c["assessment_expectations"]
    if a.get("command_words_in_scope") == openers and a.get("command_words_procedural_not_openers") == procedural: continue
    a["command_words_in_scope"] = openers; a["command_words_procedural_not_openers"] = procedural
    json.dump(c, open(p, "w"), indent=2, ensure_ascii=False); n += 1
print("openers:", openers); print("procedural, not openers:", procedural); print("contracts updated:", n)
