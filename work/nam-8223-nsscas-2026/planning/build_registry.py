#!/usr/bin/env python3
"""Build curriculum/objective_registry.json for NSSCAS Biology 8223: one container per topic (parent_id null) and one child per
objective. Syllabus objectives (152) come from curriculum/syllabus-facts.json with their printed page; practical and maths objectives
(74) from curriculum/annexe-objectives.json. objective_type, depth_tier and command words are our judgement (heuristic, then reviewed
with overrides below); syllabus text and page are transcribed. Run from the repository root with plain python3."""
import datetime, json, re, collections, sys
W = "work/nam-8223-nsscas-2026/"
facts = json.load(open(W + "curriculum/syllabus-facts.json"))
annex = json.load(open(W + "curriculum/annexe-objectives.json"))
LEVEL = "NSSCAS"
# command words the papers use (corpus analysis section 3); 'Define' never opens a part, so definitions are asked the way the papers ask them (State what is meant by / Explain what is meant by)
IN_USE = ["Describe", "Explain", "State", "Name", "Suggest", "Identify", "Outline", "Calculate", "Discuss", "Compare"]
VERB_CW = {"define": ["State", "Name"], "state": ["State", "Name"], "describe": ["Describe", "State"], "explain": ["Explain", "Describe"],
           "outline": ["Outline", "Describe"], "compare": ["Compare", "Describe", "State"], "distinguish": ["Compare", "State", "Explain"],
           "discuss": ["Discuss", "Explain"], "calculate": ["Calculate", "State"], "identify": ["Identify", "Name", "State"],
           "recognise": ["Identify", "Name", "State"], "interpret": ["Describe", "Explain", "Suggest"], "suggest": ["Suggest", "Explain"],
           "relate": ["Explain", "Describe"], "use": ["Describe", "State"], "investigate": ["Describe", "Suggest", "Explain"],
           "observe": ["Describe", "State"], "draw": ["Describe", "State", "Identify"], "make": ["Describe", "State"], "design": ["Describe", "Suggest"],
           "construct": ["Describe", "State"], "carry": ["Describe", "State"], "conduct": ["Describe", "Suggest"], "know": ["State", "Describe"]}
def verbs(text):
    """Command verbs at the start of the objective, and after 'and' or 'or' within the first words ('use and describe')."""
    toks = re.findall(r"[a-z]+|,", text.lower())[:9]; out = []
    for i, w in enumerate(toks):
        if w in VERB_CW and (i == 0 or toks[i - 1] in ("and", "or", ",")): out.append(w)
    return out or ["describe"]
def classify(text):
    t = text.lower(); v0 = verbs(text)[0]
    if re.search(r"\b(compare|contrast|distinguish|difference|differences|similarities)\b", t[:140]) and v0 in ("compare", "explain", "state", "describe", "distinguish"): return "bio_comparison"
    if v0 in ("calculate",) or re.search(r"\b(calculate|simpson|magnification|surface areas and volumes)\b", t[:120]): return "bio_quantitative"
    if v0 in ("investigate", "observe", "make", "conduct", "design", "construct", "carry") or t.startswith("describe and carry out") or t.startswith("draw") : return "bio_drawing" if re.search(r"\bdraw|diagram|drawings", t) else "bio_practical_skill"
    if v0 in ("identify", "recognise", "interpret"): return "bio_interpretation"
    if v0 == "relate" or re.search(r"\brelate\b", t[:60]): return "bio_structure_function"
    if v0 == "discuss": return "bio_explanation"
    if v0 == "define" or (v0 == "state" and not re.search(r"\band explain\b|differences? between", t)): return "bio_definition"
    if re.search(r"\b(explain|and explain)\b", t[:60]): return "bio_explanation"
    if re.search(r"\b(sequence of events|mitotic cell cycle|cardiac cycle|transcription and translation|semi-conservative replication|primary immune response|formation of|how .* (is|are) (initiated|loaded)|the process)\b", t): return "bio_process"
    if re.search(r"\bstructure\b|\broles?\b|\bfunctions?\b", t[:80]): return "bio_structure_function"
    return "bio_description"
def tier(text, typ):
    n = len(text)
    if typ == "bio_definition" and n < 130: return 1
    if typ in ("bio_explanation", "bio_process", "bio_comparison", "bio_evaluation") and n > 170: return 3
    if typ == "bio_quantitative" and n > 150: return 3
    if n > 230: return 3
    if n < 70 and typ in ("bio_definition", "bio_description"): return 1
    return 2
# hand corrections after reading the first pass (objective suffix -> type or tier)
TYPE_OVERRIDE = {'1.3-07': 'bio_explanation', '2.1-03': 'bio_quantitative', '2.2-01': 'bio_structure_function', '2.4.1-02': 'bio_structure_function', '2.4.1-07': 'bio_structure_function', '2.5.2-02': 'bio_explanation', '2.8.1-01': 'bio_comparison', '2.8.1-02': 'bio_description'}
TIER_OVERRIDE = {'2.8.1-02': 2}
PREREQ = {"3.1.1-05": ["3.1.1-01"], "3.1.1-07": ["3.1.1-04"], "3.1.2-01": ["3.1.1-01", "3.1.1-04"], "3.1.2-02": ["3.1.2-01"], "3.2.1-02": ["3.2.1-01"],
          "3.2.1-03": ["3.2.1-01", "3.2.1-02"], "3.2.1-04": ["3.2.1-03", "3.1.1-04"], "3.2.1-05": ["3.2.1-04"], "3.2.2-02": ["3.2.2-01"],
          "3.2.2-03": ["3.2.2-01", "3.2.2-02", "3.2.1-03"], "3.2.2-04": ["3.2.2-01"], "3.2.2-05": ["3.2.2-04", "3.2.2-03"], "3.2.2-06": ["3.2.2-05"], "3.2.2-07": ["3.2.1-05"]}
limits = collections.defaultdict(list)
for l in facts["limits_stated_in_content"]: limits[l["in_objective"]].append(l["limit"])
for l in facts["content_requirements_stated"]: limits[l["in_objective"]].append(l["requirement"])
guid = lambda text: "; ".join(dict.fromkeys(limits.get(text, []))) or None
objs, cnt = [], collections.Counter()
SRC = {"rating": 0, "action": "generate_gap", "rationale": "No NSSCAS Biology revision notes or approved teaching source are held (the 8223 notes folder is empty). Content is authored from the syllabus wording and the assessment corpus."}
def container(topic, title, page, aos, papers, theme_note=None):
    return {"objective_id": "OBJ-8223-%s" % topic, "parent_id": None, "topic_id": topic, "syllabus_text": "%s %s" % (topic, title),
            "learner_objective": "%s (syllabus topic %s)" % (title, topic), "level": LEVEL, "route_status": "core", "mandatory": True,
            "objective_type": "bio_container", "assessment_objectives": aos, "command_words": [], "prerequisite_ids": [], "depth_tier": 4,
            "status": "planned", "syllabus_page": page, "papers": papers, "related_ids": [], "source_coverage": SRC}
for t in facts["content_outline"]:
    if not t["is_leaf"]: continue
    tid = t["id"]; page0 = t["specific"][0]["page"]
    objs.append(container(tid, t["title"], page0, ["A", "B"], ["1", "2"]))
    for i, b in enumerate(t["specific"], 1):
        suffix = "%s-%02d" % (tid, i); txt = b["text"]
        typ = TYPE_OVERRIDE.get(suffix) or classify(txt); cw = []
        for v in verbs(txt)[:2]:
            for w in VERB_CW[v]:
                if w not in cw: cw.append(w)
        cw = [w for w in cw if w in IN_USE][:4]
        if typ == 'bio_quantitative' and 'Calculate' not in cw: cw = (['Calculate'] + cw)[:4]
        o = {"objective_id": "OBJ-8223-" + suffix, "parent_id": "OBJ-8223-" + tid, "topic_id": tid, "syllabus_text": txt, "learner_objective": txt,
             "sub_topic": tid, "sub_topic_heading": t["title"], "syllabus_page": b["page"], "papers": ["1", "2"], "level": LEVEL, "route_status": "core",
             "mandatory": True, "objective_type": typ, "depth_tier": TIER_OVERRIDE.get(suffix) or tier(txt, typ), "assessment_objectives": ["A", "B"],
             "command_words": cw, "prerequisite_ids": ["OBJ-8223-" + p for p in PREREQ.get(suffix, [])], "status": "planned", "related_ids": [], "source_coverage": SRC}
        g = guid(txt)
        if g: o["syllabus_guidance"] = g
        objs.append(o); cnt[tid] += 1
done = set()
for a in annex["objectives"]:
    tid = a["topic_id"]
    if tid not in done:
        objs.append(container(tid, a["topic_title"], a["printed_page"], a["assessment_objectives"], a["papers"])); done.add(tid)
    cw = [w for w in VERB_CW.get(a["command_verb"], ["Describe"]) if w in IN_USE][:4]
    objs.append({"objective_id": a["objective_id"], "parent_id": "OBJ-8223-" + tid, "topic_id": tid, "syllabus_text": a["syllabus_text"],
                 "learner_objective": a["learner_objective"], "sub_topic": tid, "sub_topic_heading": a["topic_title"], "syllabus_page": a["printed_page"],
                 "papers": a["papers"], "level": LEVEL, "route_status": "core", "mandatory": True, "objective_type": a["objective_type"],
                 "depth_tier": a["depth_tier"], "assessment_objectives": a["assessment_objectives"], "command_words": cw, "prerequisite_ids": [],
                 "status": "planned", "related_ids": [], "source_coverage": SRC})
    cnt[tid] += 1
ids = {o["objective_id"] for o in objs}
for o in objs:
    for p in o["prerequisite_ids"]: assert p in ids, p
if len(ids) != len(objs): sys.exit("duplicate objective ids")
json.dump({"registry_id": "OBJREG-NAM-NSSCAS-8223", "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "authority": "NSSCAS Biology Syllabus 8223 (NIED 2020): topics 1.1-3.2.2 from the learning content (printed pp. 5-19); topics 4.1-4.4 from Annexe A (pp. 29-37) and topics 5.1-5.3 from Annexe C (p. 43), grouped and split by us.",
           "granularity_note": "One objective per specific objective the syllabus lists. Each syllabus unit (1.1 ... 3.2.2) is a topic with a container (parent_id null) and one child per objective. Topics 4.1-4.4 are our container for the Paper 3 practical skills and topics 5.1-5.3 for the mathematical skills of Annexe C: the syllabus states these as expectations, so each objective is a verbatim fragment with our plain-language learner_objective. objective_type, depth_tier, command_words and papers are our judgement.",
           "papers_note": "Topics 1.1-3.2.2 and 5.1-5.3 are assessed on Paper 1 (multiple choice) and Paper 2 (structured); topics 4.1-4.4 on Paper 3 (advanced practical, AO C). The papers value is a list of paper numbers as strings. Command words are limited to those the papers use as question openers (Define never opens a part, so definitions are asked as State).",
           "objectives": objs}, open(W + "curriculum/objective_registry.json", "w"), indent=1, ensure_ascii=False)
ch = [o for o in objs if o["parent_id"]]
print("registry:", len(objs), "objects =", len(objs) - len(ch), "containers +", len(ch), "children;", len({o['topic_id'] for o in objs}), "topics")
print("types:", dict(collections.Counter(o["objective_type"] for o in ch)))
print("tiers:", dict(sorted(collections.Counter(o["depth_tier"] for o in ch).items())))
if len(sys.argv) > 1 and sys.argv[1] == "list":
    for o in ch:
        if o["topic_id"].split(".")[0] in ("1", "2", "3"): print("%-9s T%d %-22s %-28s %s" % (o["objective_id"][8:], o["depth_tier"], o["objective_type"], "/".join(o["command_words"]), o["syllabus_text"][:62]))
