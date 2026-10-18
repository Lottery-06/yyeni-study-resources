#!/usr/bin/env python3
"""Build curriculum/scope-scan.json: one entry per limit the syllabus states (facts file, limits_stated_in_content), each with a
regex our authoring checks scan learner-facing text for, plus examples it must catch and in-scope text it must leave alone.
The sentence is the syllabus's; the pattern is our judgement of what teaching past the limit would look like. Every entry's
controls are executed here: the script fails if a must_catch example is missed or a must_allow example is flagged.
Run from the repository root with plain python3."""
import json, re, datetime
W = "work/nam-8223-nsscas-2026/"
facts = json.load(open(W + "curriculum/syllabus-facts.json"))
lim = {(l["topic"], i): l for i, l in enumerate(facts["limits_stated_in_content"])}
def L(topic, key):
    m = [l for l in facts["limits_stated_in_content"] if l["topic"] == topic and key.lower() in l["limit"].lower()]
    assert m, (topic, key); return m[0]
S = lambda topic, key: (lambda l: {"printed_page": l["page"], "topic": l["topic"], "quote": l["limit"]})(L(topic, key))
E = [
 ("species concepts other than the biological, morphological, ecological and behavioural concepts", r"\b(?:phylogenetic|cohesion|recognition|evolutionary|genotypic cluster)\s+species\s+concept", {"unit": "1.1"}, S("1.1", "limited to the biological"),
  ["The phylogenetic species concept groups organisms by common ancestry.", "Under the recognition species concept, organisms share a mate-recognition system."], ["The biological species concept says a species can interbreed to produce fertile offspring.", "The morphological concept uses observable structure.", "Cohesion is the attraction between water molecules."], "fail", None),
 ("mesosomes", r"\bmesosomes?\b", {"subject": True}, S("2.2", "mesosomes"),
  ["Bacteria have mesosomes that carry out respiration.", "A mesosome is an infolding of the cell membrane."], ["Prokaryotic cells have no membrane-bound organelles.", "The bacterial cell wall is made of peptidoglycan."], "fail", None),
 ("calculations of water potential", r"\bcalculat\w*\s+(?:the\s+)?(?:water|solute|pressure)\s+potential|\bψ\s*=\s*ψ|\bwater potential\s*=\s*solute potential|\bΨs\b|\bΨp\b", {"subject": True}, S("2.3.2", "no calculations involving water potential"),
  ["Calculate the water potential of the solution using the solute potential.", "Water potential = solute potential + pressure potential."], ["Water moves from a higher to a lower water potential.", "Place the tissue in sucrose solutions of different concentrations and find the concentration with no mass change."], "fail", None),
 ("solute potential, pressure potential and osmotic potential as terms", r"\b(?:solute|pressure|osmotic)\s+potential\b", {"subject": True}, S("2.3.2", "solute potential"),
  ["The solute potential of the cell sap is negative.", "Pressure potential rises as the cell becomes turgid."], ["Water potential is the tendency of water to move.", "A turgid cell has pushed against its wall."], "fail", None),
 ("roles of water beyond solvent action, specific heat capacity and latent heat of vaporisation", r"\b(?:ice floats|ice is less dense|maximum density|surface tension)\b", {"unit": "2.4.2"}, S("2.4.2", "limited to solvent action"),
  ["Ice floats because it is less dense than liquid water.", "Surface tension lets insects walk on water."], ["Water is a good solvent for ions and polar molecules.", "Its high specific heat capacity buffers temperature changes.", "Cohesion and tension in the xylem pull water upwards."], "fail", None),
 ("chloride shift", r"\bchloride shift\b|\bhamburger shift\b", {"subject": True}, S("2.7.1", "chloride shift"),
  ["Chloride ions move into the red cell in the chloride shift.", "The Hamburger shift keeps the cell electrically neutral."], ["Carbonic anhydrase makes carbonic acid from carbon dioxide and water.", "Hydrogen ions bind to haemoglobin, forming haemoglobinic acid."], "fail", None),
 ("nervous and hormonal control of the heart", r"\b(?:vagus nerve|cardiac centre|cardiovascular centre|cardioaccelerator|medulla oblongata)\b|\b(?:sympathetic|parasympathetic)\b[^.]{0,60}\bheart\b|\b(?:adrenaline|noradrenaline|acetylcholine)\b[^.]{0,60}\bheart (?:rate|beat)", {"unit": "2.7.2"}, S("2.7.2", "reference should be made"),
  ["The vagus nerve slows the heart rate.", "Adrenaline increases heart rate through the sympathetic nerves."], ["The sinoatrial node sends waves of excitation across the atria.", "Purkyne tissue carries the signal down the septum.", "Acetylcholine is released by a neurone and binds to a receptor on the next cell.", "Insulin acts on liver cells as a signalling molecule."], "fail", None),
 ("non-infectious disease examples other than sickle cell anaemia and lung cancer", r"\b(?:non-?infectious|not infectious)\b[^.]{0,80}\b(?:diabetes|coronary heart disease|scurvy|rickets|kwashiorkor|cystic fibrosis|haemophilia|huntington|osteoporosis)\b|\b(?:diabetes|coronary heart disease|scurvy|rickets|kwashiorkor|cystic fibrosis|haemophilia|huntington|osteoporosis)\b[^.]{0,80}\b(?:non-?infectious|not infectious)\b", {"unit": "2.8.1"}, S("2.8.1", "limited to sickle cell"),
  ["Diabetes is a non-infectious disease.", "A non-infectious disease such as scurvy has a dietary cause."], ["Sickle cell anaemia is a non-infectious disease caused by a gene mutation.", "Lung cancer is a non-infectious disease.", "Insulin acts on liver cells."], "fail", None),
 ("detailed life cycle of the malarial parasite", r"\b(?:sporozoites?|merozoites?|gametocytes?|schizonts?|hypnozoites?|oocysts?|trophozoites?|exo-?erythrocytic)\b", {"subject": True}, S("2.8.1", "life cycle of the malarial"),
  ["Sporozoites enter the liver cells and divide.", "Merozoites invade red blood cells."], ["The female Anopheles mosquito transmits Plasmodium.", "The parasite must develop in the mosquito before it can infect another person."], "fail", None),
 ("T-lymphocyte types other than T-helper and T-killer cells", r"\b(?:regulatory T|suppressor T|T-?regulatory|Tregs?|memory T cells?|gamma-?delta)\b", {"unit": "2.9.1"}, S("2.9.1", "limited to T-helper"),
  ["Regulatory T cells switch the response off.", "Suppressor T cells dampen the response."], ["T-helper cells stimulate B-lymphocytes.", "T-killer cells destroy infected cells.", "Memory cells give a faster secondary response."], "fail", None),
 ("chromosome structure beyond DNA, histone proteins, chromatids, centromere and telomeres", r"\b(?:kinetochores?|nucleosomes?|euchromatin|heterochromatin|cohesins?|condensins?)\b", {"unit": "3.1.1"}, S("3.1.1", "limited to DNA, histone"),
  ["The kinetochore attaches the chromosome to the spindle fibre.", "DNA winds round histones to form nucleosomes."], ["A chromosome has two chromatids joined at the centromere.", "Telomeres are caps at the ends of the chromatids.", "Spindle fibres attach to the centromere."], "fail", None),
 ("structural formulae of nucleotides and bases", r"\bstructural formulae? of (?:the )?(?:nucleotides?|bases?|purines?|pyrimidines?|adenine|guanine|cytosine|thymine|uracil)\b|\bC5H5N5\b|\bC4H5N3O\b|\bC5H5N5O\b|\bC4H4N2O2\b", {"unit": "3.2.1"}, S("3.2.1", "structural formulae are not required"),
  ["Draw the structural formula of adenine.", "Guanine has the formula C5H5N5O."], ["Adenine and guanine are purines with a double ring structure.", "A nucleotide has a phosphate group, a pentose sugar and a nitrogenous base."], "fail", None),
]
entries, bad = [], []
for construct, pat, applies, src, catch, allow, sev, note in E:
    rx = re.compile(pat, re.I)
    for c in catch:
        if not rx.search(c): bad.append("must_catch missed: %s | %s" % (construct[:40], c))
    for a in allow:
        if rx.search(a): bad.append("must_allow flagged: %s | %s" % (construct[:40], a))
    e = {"construct": construct, "pattern": pat, "applies_to": applies, "severity": sev, "source": src, "controls": {"must_catch": catch, "must_allow": allow}}
    if note: e["note"] = note
    entries.append(e)
if bad: print("\n".join(bad)); raise SystemExit(1)
json.dump({"scope_scan_id": "SCOPE-SCAN-NAM-NSSCAS-8223", "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "rule": "Each entry is one limit the NSSCAS Biology 8223 syllabus states, with the pattern authoring checks scan learner-facing text for. The quoted sentence is the syllabus's; the pattern is our judgement of what teaching past the limit would look like. The build tools ignore applies_to and scan every topic with every pattern, so each pattern is written to be safe anywhere: it fires only on text that is past the limit. The controls are run when this file is built. Two limits are not scanned because no safe pattern exists: the sampling-method limit (objective 1.2-06 allows suitable methods) and the local-or-regional restoration examples; a reviewer reads for those, and for teaching past any limit by paraphrase.",
           "entries": entries}, open(W + "curriculum/scope-scan.json", "w"), indent=1, ensure_ascii=False)
print("scope entries:", len(entries), "| all controls pass | fail:", sum(e['severity']=='fail' for e in entries), "review:", sum(e['severity']=='review' for e in entries))
