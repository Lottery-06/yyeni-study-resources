#!/usr/bin/env python3
"""Transcribe the practical-skills (Annexe A) and mathematical-requirements (Annexe C) objectives of the NSSCAS Biology 8223 syllabus
into curriculum/annexe-objectives.json. Each objective's syllabus text is a verbatim fragment typed from the PDF and PROVEN here:
the script locates it on a page (whitespace-insensitive) and fails if it is not found. The learner-facing paraphrase, command
verb, depth tier and type are our judgement, labelled as such. Run from the repository root with plain python3."""
import datetime, json, re, subprocess, sys
PDF = "Syllabi/Namibian Curricula/NSSCAS/NSSCAS_Biology_signed_off_and_approved_syllabus_26_November_2020.pdf"
OUT = "work/nam-8223-nsscas-2026/curriculum/annexe-objectives.json"
OFFSET = 3
def clean(s): return re.sub(r"\s+", "", re.sub(r"[-•]", " ", s.replace("", "α")).replace("’", "'").replace("‘", "'"))
pages = {p: clean(subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-raw", PDF, "-"], capture_output=True, text=True).stdout) for p in range(30, 50)}
def locate(q, lo, hi):
    hits = [p for p in range(lo, hi + 1) if clean(q) in pages[p]]
    if not hits: print("FAIL: not on pages %d-%d: %s" % (lo - OFFSET, hi - OFFSET, q[:80])); sys.exit(1)
    return hits[0]
A_LO, A_HI = 32, 40   # printed pp. 29-37 (Annexe A strands A3.1-A3.3)
C_LO, C_HI = 46, 46   # printed p. 43 (Annexe C)
TOPICS = {
 "4.1": "Planning investigations and taking measurements", "4.2": "Microscopy, drawing and measuring specimens",
 "4.3": "Recording and presenting data", "4.4": "Analysis, conclusions and evaluation",
 "5.1": "Number, units and accuracy", "5.2": "Graphs, charts and rates of change", "5.3": "Size, magnification and biodiversity calculations"}
# (topic, strand, syllabus fragment, learner objective, command verb, tier, type, aos)
X = [
 # ---- 4.1 Planning investigations and taking measurements (Annexe A3.1 MMO, investigation strand)
 ("4.1", "A3.1 MMO", "Identify the independent and dependent variables.", "Identify the independent and dependent variables in an investigation.", "identify", 1, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "Decide how the independent variable should be changed within a suitable range to provide accurate results.", "Decide how to change the independent variable over a suitable range.", "describe", 2, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "decide the number of values at which measurements are recorded (a minimum of 5 measurements, replicates or more measurements around a specific value)", "Decide how many values to measure at, and where to take more.", "state", 2, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "decide how to identify the presence of a biological molecule and estimate its quantity by standardising the appropriate test", "Decide how to identify a biological molecule and estimate its quantity by standardising a test.", "describe", 3, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "Describe an appropriate control which removes the effect of the independent variable (including replacing a solution with the same volume of water or denaturing an enzyme by boiling) and variables to standardise.", "Describe an appropriate control and the variables to standardise.", "describe", 2, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "Decide which variables to standardise because they may change the results if the variable changes during the investigation and decide how to standardise each variable to provide accurate results.", "Decide which variables to standardise and how.", "describe", 2, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "Decide and describe how the dependent variable should be measured to obtain accurate and precise results.", "Decide and describe how to measure the dependent variable accurately and precisely.", "describe", 3, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "decide whether to repeat or replicate readings in order to identify anomalous results or to provide a more accurate estimate", "Decide whether to repeat or replicate readings, and why.", "explain", 2, "bio_experiment_design"),
 ("4.1", "A3.1 MMO", "follow instructions or diagrams for a range of techniques to collect results", "Follow instructions or diagrams for a range of techniques to collect results.", "describe", 2, "bio_practical_skill"),
 ("4.1", "A3.1 MMO", "assess the risk of a procedure as low, medium or high considering the hazards of solutions and reagents and the procedure", "Assess the risk of a procedure as low, medium or high.", "state", 2, "bio_practical_skill"),
 ("4.1", "A3.1 MMO", "take readings using a range of apparatus to obtain accurate data or observations with the expected pattern of results", "Take accurate readings with a range of apparatus.", "describe", 2, "bio_practical_skill"),
 ("4.1", "A3.1 MMO", "Qualitative results from observations of colour changes, using clear descriptions", "Record qualitative results, such as colour changes, in clear terms.", "describe", 1, "bio_practical_skill"),
 # ---- 4.2 Microscopy, drawing and measuring specimens (microscope strands of A3.1, A3.2 and A3.3)
 ("4.2", "A3.1 MMO (microscope)", "set up a light microscope to view and observe specimens, in order to make either plan diagrams to show tissue distribution or to draw cells to include only the observable features", "Set up a light microscope to make plan diagrams or cell drawings.", "describe", 2, "bio_practical_skill"),
 ("4.2", "A3.1 MMO (microscope)", "stain and make a slide of cells", "Stain and mount a slide of cells.", "describe", 2, "bio_practical_skill"),
 ("4.2", "A3.1 MMO (microscope)", "calibrate an eyepiece graticule using a stage micrometer", "Calibrate an eyepiece graticule against a stage micrometer.", "calculate", 3, "bio_quantitative"),
 ("4.2", "A3.1 MMO (microscope)", "obtain actual sizes of tissues or cells using a calibrated eyepiece graticule, by measuring the tissues or cells to obtain a mean measurement, using the correct units for microscopy", "Find actual sizes of tissues or cells with a calibrated graticule, as a mean, in micrometres.", "calculate", 3, "bio_quantitative"),
 ("4.2", "A3.1 MMO (microscope)", "estimate the number of cells or cell organelles in a whole slide or field of view using a sample or using a grid", "Estimate the number of cells or organelles in a field of view or slide.", "calculate", 3, "bio_quantitative"),
 ("4.2", "A3.1 MMO (microscope)", "observations by drawing the distribution of tissues in a specimen, as plan diagrams, with no cells drawn and correct proportions of layers of tissues", "Draw a plan diagram: tissue layers in correct proportion and no cells.", "state", 2, "bio_drawing"),
 ("4.2", "A3.1 MMO (microscope)", "observations by drawing the observable features of cells in a specimen", "Draw the observable features of cells: shapes, cell walls, relative sizes and observable contents only.", "state", 2, "bio_drawing"),
 ("4.2", "A3.1 MMO (microscope)", "similarities and differences between two specimens using only their observable features", "Compare two specimens using only observable features.", "compare", 2, "bio_comparison"),
 ("4.2", "A3.2 PDO (microscope)", "make drawings, using a sharp pencil, to give finely drawn lines", "Make clear, unshaded drawings with sharp, unbroken lines that use the space available.", "state", 1, "bio_drawing"),
 ("4.2", "A3.2 PDO (microscope)", "Candidates should be able to show calculations, clearly show all the steps in their calculation", "Show every step in graticule, actual-size, magnification, count-per-area, mean and ratio calculations.", "calculate", 3, "bio_quantitative"),
 ("4.2", "A3.3 ACE (microscope)", "Compare observable features of specimens of biological material including similarities and differences between microscopic slides of specimens and photomicrographs of specimens.", "Compare observable features of slides and photomicrographs.", "compare", 2, "bio_comparison"),
 ("4.2", "A3.3 ACE (microscope)", "make scientific explanations of:", "Use biological knowledge to explain observations, calculated values and how a specimen is adapted to its habitat.", "explain", 3, "bio_explanation"),
 # ---- 4.3 Recording and presenting data (A3.2 PDO)
 ("4.3", "A3.2 PDO", "Record only the raw data (unprocessed results) as quantitative data and qualitative observations in a fully ruled table with no units in the body of the table", "Record raw data in a fully ruled table with no units in the body.", "state", 2, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "prepare a table with a heading for the independent variable in the left column or top row with appropriate units and a heading for the dependent variable with units", "Head table columns with the quantity and unit, independent variable first.", "state", 2, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "record quantitative data to the same number of significant figures dependent on the measuring instrument used", "Record measurements to the same number of significant figures, set by the instrument.", "state", 2, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "show calculations clearly showing all the steps in the calculation and their reasoning", "Show every step and the reasoning in a calculation.", "calculate", 2, "bio_quantitative"),
 ("4.3", "A3.2 PDO", "use the correct number of significant figures for calculated quantities. This should be the same number of significant figures as (or one more than) the measured quantity of least accuracy.", "Give calculated values to the same number of significant figures as, or one more than, the least accurate measurement.", "state", 2, "bio_quantitative"),
 ("4.3", "A3.2 PDO", "select whether data should be shown as a graph or chart and then present the graph or chart clearly and accurately", "Choose between a graph and a chart, then present it clearly and accurately.", "state", 2, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "axes with the independent variable on the x-axis, clearly labelled (to match the relevant table heading) with units where appropriate and the dependent variable (to match the relevant table heading) on the y-axis labelled with units, where appropriate", "Put the independent variable on the x-axis and the dependent variable on the y-axis, both labelled with units.", "state", 2, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "a scale where both axes should use most or all of the grid available", "Choose scales that use most of the grid and can be read easily.", "state", 2, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "all points plotted accurately.", "Plot every point accurately as a small cross or dot in a circle.", "state", 1, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "for a graph (based on data provided) the plotted points should be connected with a clear, sharp and unbroken", "Join plotted points correctly: line of best fit, smooth curve or ruled straight lines, without extrapolating.", "state", 2, "bio_data_presentation"),
 ("4.3", "A3.2 PDO", "bars should be separated for discrete or categorical data and joined for continuous data", "Draw bars separated for discrete or categorical data and joined for continuous data.", "state", 1, "bio_data_presentation"),
 # ---- 4.4 Analysis, conclusions and evaluation (A3.3 ACE)
 ("4.4", "A3.3 ACE", "calculate the correct answer with the correct number of significant figures using quantitative results or data provided.", "Calculate an answer to the correct number of significant figures from results or data.", "calculate", 2, "bio_quantitative"),
 ("4.4", "A3.3 ACE", "find an unknown value by using co-ordinates or intercepts with axes on a graph or extrapolation where the data allows", "Find an unknown value from graph coordinates, intercepts or extrapolation.", "calculate", 2, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "estimate the concentration of unknown solutions from qualitative results", "Estimate the concentration of an unknown solution from qualitative results.", "state", 3, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "identify the contents of unknown solutions using biological molecule tests", "Identify the contents of an unknown solution using biological molecule tests.", "identify", 2, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "identify anomalous results and remove them before beginning calculations, e.g. when calculating means", "Identify anomalous results and leave them out before calculating a mean.", "identify", 2, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "describe patterns and trends using the data provided in tables and graphs", "Describe patterns and trends in tables and graphs, using the data.", "describe", 2, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "identify systematic or random errors from using apparatus in an investigation and understand that systematic errors do not affect the trend in results whereas a random error", "Identify systematic and random errors and say how each affects results.", "explain", 3, "bio_evaluation"),
 ("4.4", "A3.3 ACE", "identify the significant sources of error in a particular investigation as any variable that may change during the recording of results so making the results less accurate", "Identify the significant sources of error in an investigation.", "identify", 3, "bio_evaluation"),
 ("4.4", "A3.3 ACE", "estimate quantitatively, by calculating the actual error or percentage error (where a particular measurement is given) to evaluate the uncertainty in quantitative measurements and evaluate the confidence in the accuracy of results", "Calculate actual and percentage error and judge confidence in the results.", "calculate", 3, "bio_evaluation"),
 ("4.4", "A3.3 ACE", "evaluate the effect of the standardisation of variables on the general trend or pattern and therefore the confidence with which conclusions might be made.", "Judge how standardising variables affects confidence in a conclusion.", "explain", 3, "bio_evaluation"),
 ("4.4", "A3.3 ACE", "to predict a trend from provided information or results", "Predict a trend from information or results provided.", "suggest", 2, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "from the patterns and trends in data", "Draw a conclusion from the patterns and trends in data.", "state", 2, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "on whether investigational data support a given hypothesis", "Decide whether data support a given hypothesis.", "explain", 3, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "from results, including estimating an unknown concentration using known concentrations", "Draw a conclusion from results, including estimating an unknown concentration from known ones.", "calculate", 3, "bio_interpretation"),
 ("4.4", "A3.3 ACE", "Make scientific explanations, using skills, knowledge and understanding", "Explain data, observations, calculated values and conclusions using biological knowledge.", "explain", 3, "bio_explanation"),
 ("4.4", "A3.3 ACE", "Suggest improvements to a procedure that will increase the accuracy of the procedure for the investigation or accuracy of the observations", "Suggest improvements that make the procedure or the observations more accurate.", "suggest", 3, "bio_evaluation"),
 ("4.4", "A3.3 ACE", "Suggest how to modify or extend the investigation to answer a new question or change the independent variable", "Suggest how to modify or extend an investigation to answer a new question.", "suggest", 3, "bio_evaluation"),
 # ---- 5 Mathematical skills (Annexe C, Learners should be able to)
 ("5.1", "Annexe C", "understand averages, decimals, fractions, percentages, ratios and reciprocals", "Work with averages, decimals, fractions, percentages, ratios and reciprocals.", "calculate", 1, "bio_quantitative"),
 ("5.1", "Annexe C", "recognise and use expressions in decimal and standard form", "Use decimal and standard form, including negative powers of ten.", "calculate", 2, "bio_quantitative"),
 ("5.1", "Annexe C", "understand and use the prefixes: giga (G), mega (M), kilo (k), milli (m), micro", "Use the prefixes giga, mega, kilo, milli, micro and nano.", "state", 1, "bio_quantitative"),
 ("5.1", "Annexe C", "take account of accuracy in numerical work and handle calculations so that significant figures are neither lost unnecessarily nor carried beyond what is justified", "Keep significant figures justified: not lost early, not carried too far.", "calculate", 2, "bio_quantitative"),
 ("5.1", "Annexe C", "calculate percentages and percentage changes", "Calculate percentages and percentage changes.", "calculate", 1, "bio_quantitative"),
 ("5.1", "Annexe C", "express errors in experimental work as percentage errors", "Express errors in experimental work as percentage errors.", "calculate", 2, "bio_quantitative"),
 ("5.1", "Annexe C", "recognise and use ratios", "Recognise and use ratios.", "calculate", 1, "bio_quantitative"),
 ("5.1", "Annexe C", "use direct and inverse proportion", "Use direct and inverse proportion.", "calculate", 2, "bio_quantitative"),
 ("5.2", "Annexe C", "draw charts and graphs from given data", "Draw charts and graphs from given data.", "state", 1, "bio_data_presentation"),
 ("5.2", "Annexe C", "interpret charts and graphs", "Interpret charts and graphs.", "describe", 1, "bio_interpretation"),
 ("5.2", "Annexe C", "select suitable scales and axes for graphs", "Select suitable scales and axes for a graph.", "state", 1, "bio_data_presentation"),
 ("5.2", "Annexe C", "construct and interpret frequency distributions and diagrams, such as pie charts, bar charts and histograms", "Construct and interpret frequency distributions, pie charts, bar charts and histograms.", "describe", 2, "bio_data_presentation"),
 ("5.2", "Annexe C", "understand when information should be presented in the form of a bar chart, histogram or line graph", "Choose between a bar chart, histogram and line graph.", "state", 2, "bio_data_presentation"),
 ("5.2", "Annexe C", "recognise when it is appropriate to join the points on a graph with straight ruled lines and when it is appropriate to use a line (straight or curved) of best fit", "Decide between ruled straight lines and a line of best fit.", "state", 2, "bio_data_presentation"),
 ("5.2", "Annexe C", "calculate the rate of change from a line on a graph", "Calculate a rate of change from a graph line.", "calculate", 2, "bio_quantitative"),
 ("5.2", "Annexe C", "draw and use the slope of a tangent to a curve as a means to obtain the rate of change", "Draw and use a tangent to a curve to find a rate of change.", "calculate", 3, "bio_quantitative"),
 ("5.2", "Annexe C", "translate information between graphical, numerical, and algebraic forms", "Translate information between graphical, numerical and algebraic forms.", "describe", 2, "bio_interpretation"),
 ("5.3", "Annexe C", "recognise and use the relationship between length, surface area and volume and their units on metric scales", "Use the relationship between length, surface area and volume and their units.", "calculate", 2, "bio_quantitative"),
 ("5.3", "Annexe C", "calculate magnifications and actual sizes", "Calculate magnifications and actual sizes.", "calculate", 2, "bio_quantitative"),
 ("5.3", "Annexe C", "calculate areas of triangles, circumferences and areas of circles and rectangles, surface areas and volumes of cylinders and rectangular blocks", "Calculate areas, circumferences, surface areas and volumes of simple shapes.", "calculate", 2, "bio_quantitative"),
 ("5.3", "Annexe C", "use positive, whole number indices", "Use positive whole-number indices.", "calculate", 1, "bio_quantitative"),
 ("5.3", "Annexe C", "use Simpson's Index of Diversity (D) to calculate the biodiversity of a habitat", "Use Simpson's Index of Diversity to calculate and interpret biodiversity.", "calculate", 3, "bio_quantitative"),
]
objs, cnt = [], {}
for topic, strand, text, learner, verb, tier, typ in X:
    lo, hi = (C_LO, C_HI) if topic.startswith("5") else (A_LO, A_HI)
    pg = locate(text, lo, hi)
    cnt[topic] = cnt.get(topic, 0) + 1
    objs.append({"objective_id": "OBJ-8223-%s-%02d" % (topic, cnt[topic]), "topic_id": topic, "topic_title": TOPICS[topic], "strand": strand,
                 "syllabus_text": text, "printed_page": pg - OFFSET, "pdf_page": pg,
                 "learner_objective": learner, "command_verb": verb, "depth_tier": tier, "objective_type": typ,
                 "assessment_objectives": ["C"] if topic.startswith("4") else ["B"],
                 "papers": ["3"] if topic.startswith("4") else ["1", "2"],
                 "status": "judgement: learner_objective, command_verb, depth_tier, objective_type, papers and AO are ours; syllabus_text and page are transcribed"})
json.dump({"annexe_objectives_id": "ANNEXE-OBJ-NAM-NSSCAS-8223", "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "rule": "Topic 4 (practical skills, Paper 3, AO C) is built from Annexe A strands A3.1-A3.3 (printed pp. 29-37); Topic 5 (mathematical skills, Papers 1 and 2, AO B) from Annexe C (printed p. 43). The syllabus states these as expectations, not as numbered objectives; grouping into topics and splitting into objectives are ours. Every syllabus_text is a verbatim fragment proven on its printed page by this script.",
           "topics": TOPICS, "objectives": objs}, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", len(objs), "objectives:", cnt, "| pages used:", sorted({o["printed_page"] for o in objs}))
