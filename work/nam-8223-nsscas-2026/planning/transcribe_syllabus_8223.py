#!/usr/bin/env python3
"""Transcribe the assessment facts of the NSSCAS Biology 8223 syllabus into
curriculum/syllabus-facts.json. Every value carries the printed page that states it and the
verbatim text. Nothing here is typed from memory except the list of terms and codes to look for;
each one is located in the PDF text and the script fails if it cannot be found.

Run from the repository root:  python3 work/nam-8223-nsscas-2026/planning/transcribe_syllabus_8223.py
Then:                          python3 work/nam-8223-nsscas-2026/planning/verify_syllabus_facts.py
"""
import datetime
import json
import re
import subprocess
import sys

PDF = "Syllabi/Namibian Curricula/NSSCAS/NSSCAS_Biology_signed_off_and_approved_syllabus_26_November_2020.pdf"
OUT = "work/nam-8223-nsscas-2026/curriculum/syllabus-facts.json"
OFFSET = 3  # printed page = PDF page - 3 (PDF page 4 is printed page 1)
BULLET = re.compile(r"[\uf0b7\u2022\u25cf\u25aa]")


def page_text(p):
    return subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-raw", PDF, "-"],
                          capture_output=True, text=True, check=True).stdout


def norm(s):
    s = s.replace("\uf061", "\u03b1")  # symbol-font alpha in 2.4.1
    s = BULLET.sub(" ", s)
    s = s.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", s).strip()


def printed(p):
    return p - OFFSET


def fail(msg):
    print("FAIL:", msg)
    sys.exit(1)


pages = {p: page_text(p) for p in range(4, 50)}
N = {p: norm(t) for p, t in pages.items()}
SQ = {p: re.sub(r"\s+", "", t) for p, t in N.items()}


def squash(s):
    return re.sub(r"\s+", "", norm(s))


def locate(quote, lo=4, hi=49):
    q = squash(quote)
    hits = [p for p in range(lo, hi + 1) if q in SQ[p]]
    if not hits:
        fail("quote not found in PDF: " + norm(quote)[:90])
    return hits[0]


def src(p, section):
    return {"page": printed(p), "pdf_page": p, "section": section}


# ---------------------------------------------------------------- assessment objectives
ao_page = locate("The three Assessment Objectives in Biology are:")
ao_text = re.sub(r"NSSCAS Biology Syllabus, NIED 2020 \d+", " ", N[ao_page] + " " + N[ao_page + 1])
ao_text = re.sub(r"\s+", " ", ao_text)
start = ao_text.index("A Knowledge with understanding Learners should be able to demonstrate")
body = ao_text[start:]
body = body[: body.index("C5. plan, design and carry out investigations")] + body[body.index("C5. plan, design and carry out investigations"):]
codes = re.findall(r"\b([ABC][1-8])\.?\s", body)
sub = {}
pat = re.compile(r"\b([ABC][1-8])\.?\s+(.*?)(?=\s[ABC][1-8]\.?\s|\sThe Learning Content|\sThese skills cannot|\sLearners should be able to:|$)")
for m in pat.finditer(body):
    code, txt = m.group(1), m.group(2).strip().rstrip(";.")
    if code not in sub:
        sub[code] = txt
expected = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C1", "C2", "C3", "C4", "C5"]
if sorted(sub) != sorted(expected):
    fail("AO sub-skills parsed: %s" % sorted(sub))
ao_names = {"A": "Knowledge with understanding",
            "B": "Handling information and solving problems",
            "C": "Practical (experimental and investigative) skills and abilities"}
grid_page = locate("A Knowledge with understanding 40% (not more than 20% recall) 20 30 0")
assessment_objectives = []
for code, wt in (("A", 40), ("B", 40), ("C", 20)):
    verb = {"A": "A Knowledge with understanding", "B": "B HANDLING INFORMATION AND SOLVING PROBLEMS",
            "C": "C PRACTICAL (experimental and investigative) SKILLS AND ABILITIES"}[code]
    p = locate(verb) if verb in N[ao_page] or verb in N[ao_page + 1] else locate(verb)
    assessment_objectives.append({
        "code": code, "name": ao_names[code],
        "can_do": [{"code": c, "text": sub[c], "source": src(locate(sub[c][:60], ao_page, ao_page + 1), "6 Assessment objectives")}
                   for c in expected if c[0] == code],
        "source": src(p, "6 Assessment objectives"), "verbatim": verb,
        "qualification_weight_percent": wt,
        "weight_source": src(grid_page, "8 Specification grid"),
        "weight_verbatim": {"A": "A Knowledge with understanding 40% (not more than 20% recall) 20 30 0",
                            "B": "B Handling information, application and solving problems 40% 20 30 0",
                            "C": "C Practical (experimental and investigative) skills and abilities 20% 0 0 40"}[code],
        "weight_status": "printed in the grid; the grid itself says the weightings are approximate",
    })
for a in assessment_objectives:
    locate(a["weight_verbatim"])

# ---------------------------------------------------------------- papers
sch = locate("7. SCHEME OF ASSESSMENT")
wt = locate("Weighting of papers The assessment will be based on the end of year national examination")
papers = []
spec = [
    ("P1", "Paper 1", "Theory: Multiple choice questions", 40, 60,
     ("This paper consists of forty multiple-choice items", "Candidates will answer on an answer sheet."), "1 hour 40",
     {"A": 20, "B": 20, "C": 0}, 29, "This paper consists of forty multiple-choice items"),
    ("P2", "Paper 2", "Theory: Structured questions", 60, 75,
     ("This paper will consist of compulsory short", "question paper [booklet]."), "1 hour 15 minutes 60",
     {"A": 30, "B": 30, "C": 0}, 42, "compulsory short-answer, structured and free-response"),
    ("P3", "Paper 3", "Advanced Practical Skills", 40, 120,
     ("This paper requires learners to carry out", "available for all of their learners."), "2 hours 40",
     {"A": 0, "B": 0, "C": 40}, 29, "This paper requires learners to carry out practical work in timed conditions"),
]
for pid, label, name, marks, mins, desc, durmarks, ao_marks, weight, locator in spec:
    page = locate(locator, sch, sch)
    d0, d1 = desc
    i0 = N[sch].index(d0)
    desc = N[sch][i0:N[sch].index(d1, i0) + len(d1)]
    total = sum(ao_marks.values())
    if total != marks:
        fail("AO marks do not sum to paper marks for " + pid)
    papers.append({
        "paper_id": pid, "label": label, "name": name, "marks": marks, "duration_minutes": mins,
        "description": norm(desc),
        "source": src(page, "7 Scheme of assessment"),
        "verbatim": durmarks,
        "verbatim_page": src(locate(durmarks, sch, sch), "7 Scheme of assessment"),
        "ao_marks": {"A": ao_marks["A"], "B": ao_marks["B"], "C": ao_marks["C"]},
        "ao_marks_source": src(grid_page, "8 Specification grid"),
        "ao_split_percent_derived_from_marks": {k: round(100 * v / marks) for k, v in ao_marks.items()},
        "weight_percent_printed_table": weight,
        "weight_table_verbatim": "Paper 1 Paper 2 Paper 3 (Advanced Practical Skills) 29% 42% 29%",
        "weight_source": src(wt, "7 Scheme of assessment, Weighting of papers"),
    })
total_row = locate("TOTAL 140", sch, sch)
prose = "Paper 1 and 2 will constitute 77% of the final assessment while Paper 3 will constitute 23%."
locate(prose)
locate("Paper 1 Paper 2 Paper 3 (Advanced Practical Skills) 29% 42% 29%")
conflicts = [
    {"id": "SYL-CONFLICT-PAPER-WEIGHTS",
     "statement": "Three figures for paper weighting disagree.",
     "values": {"prose_77_23": prose, "table_printed": "29% / 42% / 29%",
                "computed_from_marks_40_60_40_of_140": [round(100 * m / 140, 1) for m in (40, 60, 40)]},
     "sources": [src(locate(prose), "7 Scheme of assessment"), src(locate("29% 42% 29%"), "7 Scheme of assessment")],
     "quotes": [prose, "Paper 1 Paper 2 Paper 3 (Advanced Practical Skills) 29% 42% 29%"],
     "qualified_by_syllabus_as_approximate": False,
     "status": "computed"},
    {"id": "SYLCONFLICT-AO-WEIGHTS",
     "statement": "The printed AO percentages (40/40/20) differ from the grid's marks (A 20+30 = 50, B 20+30 = 50, C 40, of 140).",
     "values": {"printed": [40, 40, 20], "computed_from_grid_marks": [round(100 * m / 140, 1) for m in (50, 50, 40)]},
     "sources": [src(grid_page, "8 Specification grid")],
     "quotes": ["A Knowledge with understanding 40% (not more than 20% recall) 20 30 0", "C Practical (experimental and investigative) skills and abilities 20% 0 0 40"],
     "qualified_by_syllabus_as_approximate": True,
     "status": "computed"},
    {"id": "SYL-QUALIFIER-GRID-APPROXIMATE",
     "statement": "The syllabus says the grid is only a general idea and the balance on each paper may vary slightly.",
     "verbatim": "The Specification Grid in section 8 gives a general idea of how marks are allocated to assessment objectives in the different components. However, the balance on each paper may vary slightly.",
     "sources": [src(locate("gives a general idea of how marks are allocated"), "7 Scheme of assessment")]},
]
locate(conflicts[2]["verbatim"])

annexc = locate("ANNEXEC: Mathematical requirements")
if "lincoln" in " ".join(N[p].lower() for p in range(annexc, annexc + 2)):
    fail("Lincoln appears in Annexe C: the recorded inconsistency is wrong")
lincoln_quote = "mark-release-recapture using the Lincoln index (as shown in the Mathematical requirements)"
conflicts.append({
    "id": "SYL-LINCOLN-XREF",
    "statement": "The 1.2 objective points to the Mathematical requirements for the Lincoln index, but Annexe C (Mathematical requirements) contains no Lincoln index or formula and does not say it will be supplied. Only Simpson's Index of Diversity appears there.",
    "quotes": [lincoln_quote],
    "sources": [src(locate(lincoln_quote), "3 Learning content, 1.2 Biodiversity")],
    "absence_checked_in": src(annexc, "Annexe C Mathematical requirements") ,
    "absence_check": "no occurrence of 'Lincoln' on the Annexe C pages (searched by the transcription script)",
    "status": "checked-by-search"})


# ---------------------------------------------------------------- command words (glossary, section 10)
g0 = locate("10. GLOSSARY OF TERMS USED IN SCIENCE PAPERS")
FOOT = re.compile(r"NSSCAS Biology Syllabus, NIED 2020 \d+")
gtext = re.sub(r"\s+", " ", FOOT.sub(" ", " ".join(N[p] for p in (g0, g0 + 1, g0 + 2))))
gtext = gtext[gtext.index("Define (the term(s)...)."):]
gtext = gtext[: gtext.index("In all questions, the number of marks")]
labels = ["Define (the term(s)...).", "What do you understand by/What is meant by (the term(s)...)", "State", "List", "Explain",
          "Give a reason/ give reasons", "Describe", "Discuss", "Outline", "Deduce", "predict", "Comment", "Suggest", "Find",
          "Calculate", "Measure", "Determine", "Estimate", "Show", "Sketch", "Construct", "Compare", "Recognise", "Classify"]
pos = []
cursor = 0
for lab in labels:
    if lab in ("Classify",):
        idx = gtext.index("Classify requires", cursor) if "Classify requires" in gtext[cursor:] else -1
        if idx < 0:
            fail("Classify")
        pos.append((lab, idx, len("Classify")))
        cursor = idx + 1
        continue
    pat = re.escape(lab).replace(r"\ ", r"\s+")
    m = re.compile(r"(?<![A-Za-z])" + pat + r"(?=\s)").search(gtext, cursor)
    if not m:
        fail("glossary term not found: " + lab)
    pos.append((lab, m.start(), m.end() - m.start()))
    cursor = m.end()
command_words = []
for i, (lab, st, ln) in enumerate(pos):
    end = pos[i + 1][1] if i + 1 < len(pos) else len(gtext)
    meaning = gtext[st + ln:end].strip()
    if lab == "Recognise":
        meaning = meaning.replace("Classify: group things based on common characteristics.", "").strip()
    page = locate((lab + " " + meaning)[:70].replace("...)", "..."), g0, g0 + 2) if False else locate(meaning[:50], g0, g0 + 2)
    command_words.append({"word": lab, "meaning": meaning, "source": src(page, "10 Glossary of terms used in science papers"),
                          "verbatim": norm(lab + " " + meaning)})
for c in command_words:
    if FOOT.search(c["meaning"]) or len(c["meaning"]) < 20:
        fail("empty meaning for " + c["word"])

# ---------------------------------------------------------------- content outline and limits
content_pages = range(8, 23)  # printed pages 5 to 19
heading = re.compile(r"^(\d+\.\d+(?:\.\d+)?)\.?\s+(.*)$")
theme_re = re.compile(r"^THEME (\d+): (.*)$")
skip = re.compile(r"^(TOPIC\s+GENERAL OBJECTIVES?|Learners will:|SPECIFIC OBJECTIVES|Learners should be able to:|NSSCAS Biology Syllabus, NIED 2020 \d+)$")
topics = {}
order = []
themes = {}
cur_theme = None
cur = None
cur_bullet = None
block_id = 0
for p in content_pages:
    lines = pages[p].split("\n")
    in_head = False
    for raw in lines:
        line = raw.strip()
        if not line or skip.match(norm(line)):
            continue
        mt = theme_re.match(norm(line))
        if mt:
            cur_theme = mt.group(1)
            themes[cur_theme] = {"title": mt.group(2).title(), "page": printed(p)}
            cur = None
            continue
        first = BULLET.search(line)
        head_part = line[:first.start()] if first else line
        mh = heading.match(norm(head_part)) if not cur_bullet or head_part.strip() else None
        is_heading = bool(mh) and (not first or first.start() > 3 or True) and (line[:1].isdigit())
        if is_heading:
            tid, title = mh.group(1), mh.group(2)
            title = re.sub(r"\s*\(continued\)\s*$", "", title)
            if tid not in topics:
                topics[tid] = {"id": tid, "theme": cur_theme, "title": title, "general": [], "specific": [], "pages": [printed(p)]}
                order.append(tid)
            elif printed(p) not in topics[tid]["pages"]:
                topics[tid]["pages"].append(printed(p))
            cur = topics[tid]
            block_id += 1
            in_head = True
            cur_bullet = None
            rest = line[first.start():] if first else ""
        else:
            rest = line
        if cur is None:
            continue
        # split a line on bullet glyphs
        parts = BULLET.split(rest)
        chunks = [c for c in parts]
        if first or BULLET.search(rest):
            # first chunk (before any glyph) continues the previous bullet or heading
            lead = chunks[0].strip()
            if lead and in_head and not is_heading:
                cur["title"] = norm(cur["title"] + " " + lead)
            elif lead and cur_bullet is not None:
                cur_bullet["text"] = norm(cur_bullet["text"] + " " + lead)
            for c in chunks[1:]:
                cur_bullet = {"text": norm(c), "page": printed(p), "block": block_id}
                cur["_bullets"] = cur.get("_bullets", []) + [cur_bullet]
            in_head = False
        else:
            if in_head and not is_heading:
                cur["title"] = norm(cur["title"] + " " + line)
            elif cur_bullet is not None:
                cur_bullet["text"] = norm(cur_bullet["text"] + " " + line)
GENERAL_VERBS = ("know", "understand", "realise", "recognise", "acknowledge")
for tid in order:
    t = topics[tid]
    t["title"] = re.sub(r"\s*\(continued\)\s*", " ", t["title"]).strip()
    run_block, in_run, seen_general = None, False, set()
    for b in t.pop("_bullets", []):
        if b["block"] != run_block:
            run_block, in_run = b["block"], True
        first_word = b["text"].split(" ")[0].lower()
        if in_run and first_word in GENERAL_VERBS:
            txt = re.sub(r"\s*\(continued\)\s*", " ", b["text"]).strip()
            key = re.sub(r"\s+", "", txt)[:40].lower()  # general objectives repeat, and wrap, across continuation pages
            item = {"text": txt, "page": b["page"], "variants": [{"page": b["page"], "text": txt}]}
            if key in seen_general:
                for g in t["general"]:
                    if re.sub(r"\s+", "", g["text"])[:40].lower() == key:
                        g["variants"].append({"page": b["page"], "text": txt})
                        if len(txt) > len(g["text"]):
                            g["text"], g["page"] = txt, b["page"]
            else:
                seen_general.add(key)
                t["general"].append(item)
        else:
            in_run = False
            t["specific"].append({k: v for k, v in b.items() if k != "block"})
    parts = tid.split(".")
    t["parent_id"] = ".".join(parts[:-1]) if len(parts) == 3 else (None if len(parts) == 2 else None)
    t["is_leaf"] = bool(t["specific"])

# limits stated inside the content
LIMIT_TRIGGERS = ["limited to", "not required", "not expected", "no calculations", "will not be set", "no reference", "but not to", "details of"]
REQ_TRIGGERS = ["will be provided", "are expected", "should be included", "include reference", "reference should be made", "should be a distinction", "appreciate that", "should be described"]


def enclosing_paren(text, pos):
    """Outermost parenthetical that contains pos, or None."""
    depth, start = 0, None
    for i, ch in enumerate(text):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
            if depth == 0 and start is not None and start < pos < i:
                return text[start + 1:i].strip()
    return None


def fragments(text, triggers):
    out = []
    low = text.lower()
    for trig in triggers:
        for m in re.finditer(re.escape(trig), low):
            frag = enclosing_paren(text, m.start())
            if frag is None:
                if trig == "limited to":
                    tail = text[m.start():]
                    frag = tail.split("(")[0].strip()
                else:
                    sentences = re.split(r"(?<=[.])\s+", text)
                    frag = next((x for x in sentences if trig in x.lower()), text).strip()
            if frag and frag not in out:
                out.append(frag)
    return out


limits, requirements = [], []
for tid in order:
    for b in topics[tid]["specific"]:
        for frag in fragments(b["text"], LIMIT_TRIGGERS):
            limits.append({"topic": tid, "page": b["page"], "limit": frag, "in_objective": b["text"]})
        for frag in fragments(b["text"], REQ_TRIGGERS):
            requirements.append({"topic": tid, "page": b["page"], "requirement": frag, "in_objective": b["text"]})

formulas = [{
    "topic": "1.2", "page": 5, "pdf_page": 8,
    "text_layer": "D = 1 – (Ʃ )2",
    "as_printed": "D = 1 - (Σ n/N)^2, with n over N stacked beside Σ inside the brackets and the square outside the brackets",
    "verified_from": "page image, viewed 2026-10-18 (the text layer drops the fraction)",
    "note": "The syllabus says the formula will be provided (p. 5, and Annexe C p. 43, whose text layer is identical). As printed it squares the sum. The standard Simpson's index of diversity is D = 1 - Σ(n/N)^2, which squares each term and then sums. Recorded as printed; not corrected here. The plan must decide how a card handles it.",
}]
locate("use Simpson's Index of Diversity (D) to calculate the biodiversity of an area")

# verify limits and bullets are in the cited page text
for tid in order:
    for kind in ("general", "specific"):
        for b in topics[tid][kind]:
            pdfp = b["page"] + OFFSET
            if norm(b["text"]) not in N[pdfp] and norm(b["text"]).replace(" ", "") not in N[pdfp].replace(" ", ""):
                fail("bullet not on its page: %s %s" % (tid, b["text"][:60]))
for l in limits:
    if squash(l["limit"]) not in SQ[l["page"] + OFFSET]:
        fail("limit not on its page: " + l["limit"][:60])
for l in requirements:
    if squash(l["requirement"]) not in SQ[l["page"] + OFFSET]:
        fail("requirement not on its page: " + l["requirement"][:60])

facts = {
    "facts_id": "SYLFACTS-NAM-NSSCAS-8223",
    "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "generated_by": "work/nam-8223-nsscas-2026/planning/transcribe_syllabus_8223.py",
    "authority": "NSSCAS Biology Syllabus 8223 (NIED 2020), signed off 26 November 2020, Advanced Subsidiary Level, Grade 12, for implementation and first examination in 2021.",
    "source_document": PDF,
    "pages_in_document": 50,
    "page_numbering": "page = the number printed on the syllabus page; pdf_page = the PDF page index (printed page + 3).",
    "rule": "STEP ZERO of the pipeline. Every value here is transcribed from the syllabus and carries the page that states it. Nothing downstream may assert an AO weighting, a per-paper split, a paper structure or a command word that is not in this file. A value without a citation is a value we do not have. Values marked computed or derived are arithmetic on transcribed values, not syllabus statements.",
    "route": "NSSCAS Advanced Subsidiary Level (Grade 12)",
    "papers_sat": ["Paper 1 Theory: Multiple choice questions", "Paper 2 Theory: Structured questions", "Paper 3 Advanced Practical Skills"],
    "first_exam": "2021",
    "assessment_objectives": assessment_objectives,
    "papers": papers,
    "paper_total_marks": {"value": 140, "source": src(total_row, "7 Scheme of assessment"), "verbatim": "TOTAL 140"},
    "conflicts_and_qualifiers": conflicts,
    "command_words": command_words,
    "command_word_table": {"page": printed(g0), "section": "10 Glossary of terms used in science papers", "count": len(command_words),
                           "note": "The syllabus calls its glossary 'neither exhaustive nor definitive' and says a term's meaning depends partly on its context. 'predict' is lower-case in the source. A word the papers use that is not listed is recorded separately as observed-not-listed; a word listed but never used as listed-not-observed. Neither is guessed."},
    "themes": themes,
    "content_outline": [topics[t] for t in order],
    "limits_stated_in_content": limits,
    "content_requirements_stated": requirements,
    "formulas_as_printed": formulas,
    "transcribed_notes": [],
}
json.dump(facts, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", OUT)
print("AO subskills:", len(sub), "| papers:", len(papers), "| command words:", len(command_words))
print("themes:", {k: v["title"] for k, v in themes.items()})
print("leaf topics:", len(order))
for t in order:
    print(" ", t, "general", len(topics[t]["general"]), "specific", len(topics[t]["specific"]), "|", topics[t]["title"][:55])
print("limits:", len(limits), "| requirements:", len(requirements))
