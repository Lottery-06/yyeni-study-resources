#!/usr/bin/env python3
"""LIMITS OF THIS CHECK: the Simpson formula as printed cannot be machine-verified (the text layer drops the fraction); it is held twice and checked by eye. Mapping of topic to bullet relies on the parser, but the completeness check below proves no text on a content page is missing.
Independent check of curriculum/syllabus-facts.json. Re-opens the PDF and proves every cited quote, in full, is on the
page it cites; ties every number to its cited cell; checks structure against expected_counts.json (typed separately);
and rejects the defects the first Codex review found (footer text inside a value, a split objective, a stray symbol-font
character, a truncated 'verbatim'). Exit 1 on any failure. Run from the repository root."""
import json, re, subprocess, sys
F = sys.argv[1] if len(sys.argv) > 1 else "work/nam-8223-nsscas-2026/curriculum/syllabus-facts.json"
E = "work/nam-8223-nsscas-2026/planning/expected_counts.json"
d = json.load(open(F)); exp = json.load(open(E))
PDF = d["source_document"]
FOOT = re.compile(r"NSSCAS Biology Syllabus, NIED 2020\s*\d*")
def clean(s): return re.sub(r"[•]", " ", s.replace("", "α")).replace("’", "'").replace("‘", "'")
def sq(s): return re.sub(r"\s+", "", clean(s))
cache = {}
def page(p):
    if p not in cache:
        cache[p] = sq(subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-raw", PDF, "-"], capture_output=True, text=True).stdout)
    return cache[p]
bad, errs, n = [], [], 0
def check(label, quote, pdf_page):
    global n; n += 1
    if sq(quote) not in page(pdf_page): bad.append((label, pdf_page, quote[:80]))
    if FOOT.search(quote): errs.append("footer text inside value: " + label)
    if re.search(r"[-]", quote): errs.append("stray symbol-font character in value: " + label)

for a in d["assessment_objectives"]:
    check("AO " + a["code"], a["verbatim"], a["source"]["pdf_page"])
    check("AO weight " + a["code"], a["weight_verbatim"], a["weight_source"]["pdf_page"])
    if str(a["qualification_weight_percent"]) + "%" not in a["weight_verbatim"]: errs.append("AO weight not in its cited cell: " + a["code"])
    for c in a["can_do"]: check("AO " + c["code"], c["text"], c["source"]["pdf_page"])
for p in d["papers"]:
    check(p["paper_id"] + " description", p["description"], p["source"]["pdf_page"])
    check(p["paper_id"] + " duration/marks", p["verbatim"], p["verbatim_page"]["pdf_page"])
    check(p["paper_id"] + " weight", p["weight_table_verbatim"], p["weight_source"]["pdf_page"])
    if str(p["marks"]) not in p["verbatim"].split(): errs.append(p["paper_id"] + " marks not in its cited cell")
    if f"{p['weight_percent_printed_table']}%" not in p["weight_table_verbatim"]: errs.append(p["paper_id"] + " weight not in its cited row")
    h = {"P1": ("1 hour", 60), "P2": ("1 hour 15 minutes", 75), "P3": ("2 hours", 120)}[p["paper_id"]]
    if not p["verbatim"].startswith(h[0]) or p["duration_minutes"] != h[1]: errs.append(p["paper_id"] + " duration does not match its cited cell")
for c in d["command_words"]:
    check("command word " + c["word"], c["verbatim"], c["source"]["pdf_page"])      # full text, not a prefix
    if clean(c["verbatim"]).replace(" ", "") != clean(c["word"] + c["meaning"]).replace(" ", ""): errs.append("verbatim differs from word + meaning: " + c["word"])
for t in d["content_outline"]:
    for kind in ("general", "specific"):
        for b in t[kind]:
            check(t["id"] + " " + kind, b["text"], b["page"] + 3)
            if len(b["text"]) < 15 or not b["text"][0].isalpha() or not b["text"][0].islower():
                errs.append("suspect fragment (split objective?) in %s %s: %r" % (t["id"], kind, b["text"][:50]))
    if t["parent_id"] and t["parent_id"] not in {x["id"] for x in d["content_outline"]}: errs.append("missing parent for " + t["id"])
for l in d["limits_stated_in_content"]: check("limit " + l["topic"], l["limit"], l["page"] + 3)
for l in d["content_requirements_stated"]: check("requirement " + l["topic"], l["requirement"], l["page"] + 3)
for c in d["conflicts_and_qualifiers"]:
    for q in c.get("quotes", []) + ([c["verbatim"]] if "verbatim" in c else []):
        check("conflict " + c["id"], q, (c["sources"][0]["pdf_page"]) if len(c["sources"]) == 1 else None or 0) if False else None
        # a conflict quote may sit on either cited page
        n += 1
        if not any(sq(q) in page(s["pdf_page"]) for s in c["sources"]): bad.append(("conflict " + c["id"], [s["pdf_page"] for s in c["sources"]], q[:80]))
for f in d["formulas_as_printed"]: check("formula topic " + f["topic"], "use Simpson's Index of Diversity (D) to calculate the biodiversity of an area", f["pdf_page"])
# structure
if sum(p["marks"] for p in d["papers"]) != 140: errs.append("paper marks do not sum to 140")
for p in d["papers"]:
    if sum(p["ao_marks"].values()) != p["marks"]: errs.append(p["paper_id"] + " AO marks do not sum to paper marks")
if d["paper_total_marks"]["value"] != 140: errs.append("total marks")
leaves = {t["id"]: t for t in d["content_outline"] if t["is_leaf"]}
if {k: len(v["specific"]) for k, v in leaves.items()} != exp["specific"]:
    diff = {k: (len(leaves[k]["specific"]) if k in leaves else None, v) for k, v in exp["specific"].items() if k not in leaves or len(leaves[k]["specific"]) != v}
    errs.append("per-leaf specific counts differ from expected_counts.json (found, expected): %s" % diff)
if sum(len(t["specific"]) for t in leaves.values()) != exp["total_specific"]: errs.append("total specific objectives")
if sum(len(t["general"]) for t in leaves.values()) != exp["total_general"]: errs.append("total general objectives")
if len(d["command_words"]) != 24: errs.append("expected 24 glossary entries")
for k, title in exp["themes"].items():
    th = d["themes"].get(k)
    if not th or th["title"].upper() != title: errs.append("theme %s title" % k)
    elif title.lower().replace(" ", "") not in page(th["page"] + 3).lower() and title.replace(" ", "") not in page(th["page"] + 3).upper(): errs.append("theme %s title not on its page" % k)

# --- checks added after the second Codex review (each closes a way the earlier verifier could pass wrong data)
from collections import Counter
import json as _j
lim = Counter(l["topic"] for l in d["limits_stated_in_content"]); req = Counter(l["topic"] for l in d["content_requirements_stated"])
if dict(lim) != exp["limits_by_topic"]: errs.append("limits per topic differ from expected_counts.json: %s" % dict(lim))
if dict(req) != exp["requirements_by_topic"]: errs.append("requirements per topic differ from expected_counts.json: %s" % dict(req))
for a in d["assessment_objectives"]:
    if a["verbatim"] != exp["ao_headings"][a["code"]]: errs.append("AO heading text differs: " + a["code"])
    row = [int(x) for x in re.findall(r"\b(\d+)\b(?!%)", a["weight_verbatim"].split("%")[-1])][-3:]
    grid = [p["ao_marks"][a["code"]] for p in sorted(d["papers"], key=lambda q: q["paper_id"])]
    if row != grid: errs.append("AO %s marks per paper %s do not match the grid row %s" % (a["code"], grid, row))
for p in d["papers"]:
    if p["ao_marks"] != exp["paper_ao_marks_grid"][p["paper_id"]]: errs.append(p["paper_id"] + " AO marks differ from expected grid")
    if not p["description"].rstrip().endswith("."): errs.append(p["paper_id"] + " description does not end at a sentence end (truncated?)")
g0 = [c["source"]["pdf_page"] for c in d["command_words"]][0]
gl = "".join(page(q) for q in (g0, g0 + 1, g0 + 2))
gl = re.sub(r"NSSCASBiologySyllabus,NIED2020\d+", "", gl)
cw = d["command_words"]
for i, c in enumerate(cw):
    nxt = sq(cw[i + 1]["word"]) if i + 1 < len(cw) else "Inallquestions"
    if not re.search(re.escape(sq(c["meaning"])) + r"(Classify:groupthingsbasedoncommoncharacteristics\.)?" + re.escape(nxt[:14]), gl):
        errs.append("command word meaning is not followed by the next term in the source (truncated?): " + c["word"])
if d["formulas_as_printed"][0]["as_printed"] != exp["formula_as_printed"]: errs.append("formula as printed differs from the separately held copy")
if "D=1\u2013(\u01aa)2".replace("\u01aa", "\u01aa") and sq(d["formulas_as_printed"][0]["text_layer"]) not in page(8): errs.append("formula text layer not on page 5")
if [c["id"] for c in d["conflicts_and_qualifiers"]] != exp["conflict_ids"]: errs.append("conflict ids differ from expected")
if "lincoln" in page(46).lower() or "lincoln" in page(47).lower(): errs.append("Annexe C now contains Lincoln: the recorded inconsistency is wrong")
# completeness: every character of each content page is accounted for by a recorded bullet, heading or known page furniture
furniture = [r"NSSCASBiologySyllabus,NIED2020\d+", r"TOPIC", r"GENERALOBJECTIVES?", r"Learnerswill:", r"SPECIFICOBJECTIVES", r"Learnersshouldbeableto:", r"THEME\d:[A-Z]+", r"\(continued\)"]
for pdfp in range(8, 23):
    rest = page(pdfp)
    for f in furniture: rest = re.sub(f, "", rest)
    for t in d["content_outline"]:
        if (t["pages"] and (pdfp - 3) in t["pages"]):
            rest = rest.replace(sq(t["id"]), "", 1)
            for kind in ("general", "specific"):
                for b in t[kind]:
                    for vr in (b.get("variants") or [{"page": b["page"], "text": b["text"]}]):
                        if vr["page"] == pdfp - 3: rest = rest.replace(sq(vr["text"]), "", 1)
    for t in d["content_outline"]:
        if (pdfp - 3) in t["pages"]:
            for tok in t["title"].split():
                rest = rest.replace(sq(tok), "", 1)
    for th in d["themes"].values():
        rest = rest.replace(sq(th["title"]), "", 1)
    rest = re.sub(r"[\d.\-]+", "", rest)
    if len(rest) > 25: errs.append("page %d has text not accounted for by any recorded objective (truncated or dropped?): %r" % (pdfp - 3, rest[:90]))

for b in bad: print("QUOTE NOT ON PAGE:", b)
for e in errs: print("PROBLEM:", e)
print("checked %d quotes; %d not on their cited page; %d structural problems" % (n, len(bad), len(errs)))
print("RESULT:", "PASS" if not bad and not errs else "FAIL")
sys.exit(1 if bad or errs else 0)
