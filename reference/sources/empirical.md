# How Anthropic's Economics, Societal-Impacts and Policy Research Is Actually Done: A Methods Review

Prepared 2 September 2026 for an applicant to the Anthropic Fellows Program (Economics & Policy, The Anthropic Institute). Every URL below was fetched on 2 September 2026 unless marked **[unverified]**. Where a page was a PDF, the text was extracted locally (Jan 2026 Economic Index report, Massenkoff & McCrory labor-market paper, WorkerRetraining.pdf, the August 2026 Risk Report, both METR review PDFs, the "81k" appendix). Two fetch failures: the arXiv HTML of 2511.15080 returned 404 and its PDF exceeded the fetch size limit, so that paper is cited from its abstract page plus the Anthropic web report; and no document containing METR's "8 ≈ e²" remark was found (see Section D).

---

## A. The Anthropic research pipeline, end to end

A typical Economic Index or Societal Impacts study is a seven-stage pipeline. The stages are remarkably stable across reports from February 2025 to June 2026; what changes is the classifier model, the sampling frame, and the set of "primitives" extracted.

### A1. Sampling

- **Products.** Early reports used only Claude.ai Free and Pro ("rather than API, Team, or Enterprise users"; Feb 2025). From September 2025 the frame is two parallel samples: 1M Claude.ai conversations (Free/Pro/Max) and 1M first-party (1P) API transcripts "sampled randomly from a pool of 1P API customers constituting roughly half of our 1P API usage". Claude Code studies use interactive sessions only (the expertise report: ~400,000 sessions from ~235,000 people, Oct 2025–Apr 2026, excluding third-party IDEs and headless CLI). The autonomy report adds "998,481 random tool calls from our public API".
- **Window.** A single 7–8 day slice: Dec 16–23 2024 and Jan 10–17 2025 (Feb 2025 paper); Aug 4–11 2025 (Sept 2025); Nov 13–20 2025 (Jan 2026); Feb 5–12 2026 (Mar 2026). The June 2026 report switched to "privacy-preserving telemetry, which continuously samples a slice of conversations every day", allowing hourly resolution over Apr 10–Jun 10 2026.
- **Exclusions.** Conversations "flagged as potential trust and safety violations" are dropped. The Feb 2025 paper additionally filtered with Claude 3.5 Haiku to occupationally relevant conversations; the March 2025 update abandoned that filter ("we simply filter out conversations that flagged our safety classifiers"). Affective-use work removed content-creation roleplay and kept roleplay only with ≥4 human messages. The education report restricted to accounts with higher-education email domains (1M → 574,740 academically relevant conversations). Values-in-the-Wild kept only "subjective" conversations (700,000 → 308,210, 44%).
- **Important structural fact.** 1P API records are "a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions" (Jan 2026 report). API data is therefore single-turn, which the reports repeatedly flag when comparing speedups or autonomy across platforms.

### A2. Privacy: Clio

Clio (arXiv 2412.13678) is the substrate for everything. Four steps, "powered entirely by Claude, not by human analysts": (1) **facet extraction** — some facets computed directly (turn count), others by prompting Claude to summarise a specific attribute "while omitting private details"; (2) **semantic clustering** — embeddings (all-mpnet-base-v2) and k-means; (3) **cluster description** — a title and summary "that captures common themes from the raw data while excluding private information"; (4) **hierarchy building** by combining k-means and prompting. Guardrails: minimum thresholds on unique accounts and conversations before a cluster is retained; a **privacy auditor** model that reads every summary and removes any containing identifying content; access controls (Trust & Safety can review clusters). Validation: on 19,476 synthetic multilingual transcripts with known ground truth, Clio "reconstructed the ground-truth distribution of topics ... with 94% accuracy" (random baseline 5%); Clio's per-cluster concern score correlates with existing safety classifiers at Pearson r = 0.71. A run over 100,000 conversations cost about $48.81. The thresholds used downstream are explicit: ≥15 conversations and ≥5 unique accounts for a task or geography cell; ≥500 conversations and ≥250 accounts for bottom-up "request clusters"; ≥200 observations for a country and ≥100 for a US state to appear in geographic analysis. What humans can see: aggregate categories and percentages, cluster summaries that have passed the auditor, and — only with explicit user permission — transcripts from users who gave feedback. Researchers "cannot manually inspect the underlying data due to privacy constraints" (autonomy report).

### A3. Classification: LLM-as-classifier and the taxonomies

Every facet is a prompt to Claude with a constrained output ("we prompt Claude to select a specific output and then use Claude's response as the output"). Chain-of-thought is kept only where it helped (human time estimate, human-with-AI time, AI autonomy). The taxonomies that recur:

- **O*NET tasks and occupations.** ~20,000 tasks; the Feb 2025 paper built a hierarchy of "12 top-level tasks, 474 middle-level tasks, and 19530 base-level (O*NET) tasks" and classified top-down. Later reports use 2019 O*NET-SOC codes plus bottom-up request clusters (630 clusters in three levels in March 2025).
- **Collaboration mode (augmentation vs automation).** Five sub-modes: Directive ("complete task delegation with minimal interaction"), Feedback Loop ("task completion guided by environmental feedback") = automation; Task Iteration, Learning, Validation = augmentation. Feb 2025: 57% augmentation / 43% automation (Directive 27.8%, Feedback Loop 14.8%, Task Iteration 31.3%, Learning 23.3%, Validation 2.8%). Claude Code (Apr 2025): 79% automation vs 49% on Claude.ai. Directive share rose "from 27% to 39%" between Dec 2024 and Aug 2025.
- **Economic primitives (Jan 2026).** Nine classifiers for five dimensions: task complexity (human-alone time, human-with-AI time, multi-task), human and AI skill (could the user have done it alone; years of education to understand the prompt and the response), use case (work / coursework / personal), AI autonomy (1–5, "none" to "extreme"), and task success (Claude's own judgement; "a simple classifier performed better than a nuanced, complex classifier"). Full prompt texts are in the Hugging Face appendix.
- **Artifacts (June 2026).** A classifier "identified 93% of Claude conversations as producing an artifact", sorted into >30 categories; a reading-level classifier gives years of education.
- **Values taxonomy.** 3,307 AI values in a four-level hierarchy (5 categories → 26 → 266 → values), later hand-compressed to 339 high-level values and reduced to four axes (Deference–Caution, Warmth–Rigor, Depth–Brevity, Candor–Execution) explaining 15% of variance.
- **Autonomy and risk scales.** Tool-call-level 1–10 risk and autonomy scores; irreversibility flag (0.8% of actions irreversible); safeguard presence (80% of tool calls from agents with at least one safeguard, 73% with a human in the loop somewhere).
- **Other one-off scales:** Bloom's taxonomy for student use; a 1–7 sentiment scale and multi-label "concerns" in the 81k study; a five-point novice-to-expert scale in the Claude Code expertise report; a 1–7 productivity scale in 81k-economics.

### A4. Weighting to the economy

- **Occupation and employment weights.** Tasks are mapped to the occupation that typically performs them and compared with BLS employment shares (Computer & Mathematical: 37.2% of usage vs 3.4% of US workers; Transportation 0.3% vs 9.1%).
- **Wage weights.** Median wages from O*NET (2019 scrape) or BLS OEWS (May 2024, May 2025). Productivity aggregation uses the wage-bill share of each occupation × time share of each task within the occupation × log speedup (Hulten's theorem).
- **AI Usage Index (AUI).** Share of Claude usage in a geography ÷ share of the working-age (15–64) population. AUI > 1 means over-representation. Canada's AUI is 4.4; Ontario has 43.9% of Canadian conversations; the four largest provinces ~94%.
- **Observed exposure** (labor-market paper): a task counts as covered if Eloundou et al. rate it theoretically feasible (β = 0.5 or 1) *and* it sees sufficient work-related use; automated use gets full weight, augmentative use half; task coverage is averaged to occupations weighted by time-on-task, then to categories weighted by employment.

### A5. Validation

Every report contains some subset of: (i) **human-rater agreement** on transcripts users opted to share — 95.3% / 91.3% / 86% accuracy at the three O*NET hierarchy levels and 90.7% for augmentation/automation (Feb 2025); 94% for the subjective filter and 98.8% for value extraction (Values in the Wild); "at least 90% agreement with a human on 25 labels" per classifier in the 81k study; (ii) **synthetic data** for API classifiers "using a mix of internal and synthetic data"; (iii) **external benchmark correlation** — Claude's time estimates against 1,000 JIRA tickets (Spearman ρ = 0.44 vs 0.50 for the developers' own estimates), education-years primitive against ACS share of bachelor's degrees by occupation, warm-up "last use" in the 81k study against Economic Index shares (34% coding vs 36%); (iv) **robustness** — rerunning V3 data with the older Sonnet 3.7 classifier, self-consistency across prompt variants (r = 0.89–0.93 on 1,800 consented conversations), rank-rank stability of exposure across "many resolutions" of judgment calls, progressive fixed-effects specifications (task, cluster, model, use case, country).

### A6. External linkage

- **CPS.** Massenkoff & McCrory match O*NET-SOC to CPS occ1990 via the Eckhart–Goldschlag crosswalk, then run difference-in-differences on unemployment (top quartile of observed exposure vs the 30% with zero exposure) and on the monthly job-start rate of 22–25-year-olds using the CPS panel dimension.
- **BLS projections.** Occupation-level regression weighted by employment: every 10 pp of coverage lowers projected 2024–34 growth by 0.6 pp; no such correlation using Eloundou's β alone.
- **Surveys linked to usage.** The Economic Index Survey (monthly, via Anthropic Interviewer) is linked to "up to 20 sessions per person" using privacy-preserving methods; June 2026 analysed ~9,700 linked respondents with ≥5 sessions.

### A7. The limitations they always state

Verbatim staples: "we don't argue that the uses in our dataset are a representative sample of AI use in general"; "our methods are not able to capture how users are using the outputs"; "Claude is advertised for use as a state-of-the-art coding model, we might expect coding to be overrepresented"; "in our data, users choose which tasks to bring to Claude"; "All of our classifications of sessions depend on a model's reading of the transcript"; "the model driving the categorization is also Claude"; "We can only analyze traffic from a single model provider"; "This analysis reflects a specific window of time"; "Without a counterfactual we can't make causal claims". Selection, causation, single-turn API data, model-as-classifier, static O*NET, and unobserved post-conversation behaviour appear in nearly every write-up.

---

## B. Catalogue of techniques

Each entry: what it is; where Anthropic uses it (with numbers); the classic reference; a try-it-yourself exercise (the public data is at https://huggingface.co/datasets/Anthropic/EconomicIndex — six releases, 2025-02-10 to 2026-06-26, CC-BY data, MIT code, 664 MB, plus a "labor market impacts" folder with task- and job-level observed coverage); and interview questions.

### 1. Privacy-preserving usage analysis (Clio)

**What.** Delegate reading to the model: extract facets, embed, cluster, summarise, audit, and enforce minimum-k thresholds so no human ever reads a raw conversation. It is closer to a data-governance design than a statistical method, but it determines what can be measured at all.
**Where.** Clio (Dec 2024, https://www.anthropic.com/research/clio): 1M conversations; 94% reconstruction of synthetic ground truth; $48.81 per 100k conversations. Every Economic Index release inherits its k-thresholds (15/5, 500/250).
**Classic reference.** k-anonymity (Sweeney 2002) and differential privacy (Dwork 2006) for the threshold logic; topic modelling (Blei et al. 2003) for the clustering lineage.
**Try it.** Take any public conversation dataset (e.g. an open chat corpus), write a facet prompt that returns a one-sentence topic with no names, embed with a sentence-transformer, k-means to 50 clusters, summarise each with a prompt, then drop clusters with <15 items; inspect what information survives.
**Interview questions.** Why both a conversation threshold and an account threshold? What does the auditor protect against that thresholds do not? What can Clio *not* prove (absence of a pattern)?

### 2. LLM-as-classifier with validation

**What.** Replace human coders with a prompted model returning a constrained label; validate on a small labelled set, on synthetic data, and by external correlation; keep prompts simple and only add chain-of-thought where it demonstrably helps.
**Where.** Feb 2025 paper (95.3/91.3/86% hierarchy accuracy, 90.7% for collaboration mode); Jan 2026 primitives (nine classifiers, "directionally accurate even if they may deviate somewhat from human ratings"); 81k study (≥90% agreement on 25 labels; a 1–7 sentiment prompt is printed in the appendix); personal-guidance study (Sonnet 4.5 as grader, "manually verified a small subset"); productivity paper (Claude ρ = 0.44 vs developer ρ = 0.50 against tracked JIRA times, with systematic compression of long tasks).
**Classic reference.** Krippendorff, *Content Analysis*; Cohen's kappa; Ziems et al. (2024) "Can LLMs transform computational social science?"; Gilardi et al. (2023) on ChatGPT vs crowdworkers.
**Try it.** Hand-label 50 O*NET task descriptions on a 1–5 "years of education" scale, prompt a model to do the same with and without chain-of-thought, and compute Spearman and mean absolute deviation for each variant.
**Interview questions.** Why can "directionally accurate" be enough for some uses and not others? How do you validate a classifier on data you are not allowed to read? What is the failure mode when the classifier and the subject are the same model?

### 3. Mapping usage to O*NET and weighting to occupations

**What.** Assign each conversation to a task, aggregate to occupations using O*NET's task-occupation links, then compare with BLS employment and wages.
**Where.** Feb 2025: 36% of occupations use AI for ≥25% of tasks, ~4% for ≥75%; usage peaks in the upper-middle wage range (US median wage reference $60,070). March 2025 caveat: "O*NET descriptions may not be optimally representative ... usage on Claude.ai probably tilts more towards digital art than sculpture". March 2026 values tasks with OEWS hourly wages.
**Classic reference.** Autor, Levy & Murnane (2003) task framework; Acemoglu & Restrepo (2018, 2022) task-based model; Eloundou et al. (2023) for the O*NET-based exposure design; Frey & Osborne (2017) as the older occupation-level contrast.
**Try it.** Load the 2025-09-15 release, join task shares to O*NET occupation-task tables and BLS OEWS employment, and compute the usage-to-employment ratio for each SOC major group; reproduce the 37.2% vs 3.4% style comparison.
**Interview questions.** Why do tasks, not occupations, carry the exposure analysis? What does O*NET's static nature hide? What breaks when one conversation contains several tasks?

### 4. Augmentation vs automation taxonomy

**What.** A five-mode classification of *how* the user collaborates with the model, collapsed to a binary and tracked over time and across platforms.
**Where.** 57/43 in Feb 2025; 79% automation in Claude Code vs 49% in Claude.ai (Apr 2025); directive share 27% → 39% over eight months (Sept 2025); "We don't see any occupational categories where automation dominates" (Mar 2025). The Jan 2026 report deliberately separates this from AI autonomy: "Translate this paragraph into French" is high automation but low autonomy.
**Classic reference.** Brynjolfsson (2022) "The Turing Trap"; Autor (2015) on complementarity; Agrawal, Gans & Goldfarb on prediction vs judgment.
**Try it.** Using the 2025-03-27 cluster file, compute the automation share by top-level occupational category and by cluster, then check whether the mode shift 2025→2026 is driven by composition (different tasks) or within-task change (a simple shift-share decomposition).
**Interview questions.** Why is "feedback loop" counted as automation? Why might a classifier upgrade (3.7 → Sonnet 4) alone move the directive share, and how did they check? What would "augmentation" look like in API data that is single-turn?

### 5. AI Usage Index, per-capita concentration and convergence

**What.** Normalise usage by working-age population, then measure inequality across regions with a Gini and fit a proportional-convergence regression to estimate the diffusion rate.
**Where.** Sept 2025: usage elasticity 0.7 to GDP per capita across countries, 1.8 across US states; task Gini 0.84 (Claude.ai) and 0.86 (API). Jan 2026: US state Gini fell from 0.37 to 0.32 between August and November 2025; OLS β̂ ≈ 0.77 (WLS 0.76) implies "little more than two years" to close most of the gap; 2SLS instrumenting August log-AUI with workforce composition gives β̂ ≈ 0.89 (0.86 weighted), "four to five years for the log deviation ... to shrink by 90%"; benchmark β = 0.99 "implies a half-life of about 17 years". Canada: AUI 4.4, second only to the US per capita.
**Classic reference.** Barro & Sala-i-Martin (1992) β-convergence; Comin & Hobijn (2010) technology diffusion; Griliches (1957) hybrid corn; attenuation bias and IV (Angrist & Pischke, *Mostly Harmless Econometrics*, ch. 4).
**Try it.** Take state AUI from the Sept 2025 and Jan 2026 releases; regress log AUI(t+1) on log AUI(t); compute the implied half-life ln(0.5)/ln(β); then instrument with a state's predicted usage from occupational composition (OEWS shares × national per-occupation usage) and compare.
**Interview questions.** Why does sampling noise bias OLS β toward faster convergence? What makes workforce composition a valid instrument, and what would violate exclusion? Why is a Gini over *tasks* a different object from a Gini over *states*?

### 6. Economic primitives and the speedup/productivity calculation

**What.** Elicit per-conversation estimates of human-alone time, human-with-AI time, education years, autonomy and success; compute speedup = human-alone ÷ human-with-AI; aggregate log speedups with wage-bill and time weights via Hulten's theorem; adjust by success; test complementarity with a CES aggregator.
**Where.** Productivity paper (Nov 2025, https://www.anthropic.com/research/estimating-productivity-gains): 100k conversations; median task 1.4 hours, $55 of labour; median time saving 81%; "1.8 percentage points" of annual labour productivity growth for a decade, i.e. 1.08% TFP with a 0.64 labour share; software developers contribute 19% of gains. Jan 2026 report: speedup 9× at 12 years of schooling, 12× at 16; success 70% for sub-high-school tasks vs 66% for college-level; success adjustment cuts the 1.8 to 1.2 (Claude.ai) and 1.0 (API); σ = 0.5 gives 0.7–0.9 pp (0.8/0.6 with success), σ = 1.5 gives 2.2–2.6 pp; task-inclusion threshold of 0.02% chosen "because it replicates our previous results", and with no threshold the number balloons to "roughly 5 percentage points" — a mechanical artefact they disclose.
**Classic reference.** Hulten (1978); Baumol (1967) cost disease as the σ<1 intuition; Aghion, Jones & Jones (2019) on bottleneck tasks; Acemoglu (2024) "The Simple Macroeconomics of AI"; Autor & Thompson (2025) on task removal and deskilling; Brynjolfsson, Li & Raymond (2023) for what a real productivity effect looks like.
**Try it.** From the 2026-01-15 primitives release, compute task-level log speedups, weight by (occupation wage bill × task time share), sum to get the Hulten number; multiply by success rate; then implement the two-level CES with ρ = (σ−1)/σ for σ ∈ {0.5, 1, 1.5}. Python needed: pandas, numpy.
**Interview questions.** Why log speedups rather than ratios? Why does σ = 1 collapse to Hulten? What does the 0.02% threshold tell you about the fragility of the headline? Why is success adjustment only an extensive-margin correction?

### 7. Theoretical vs observed exposure and CPS linkage

**What.** Build an exposure index that combines a theoretical feasibility score with actual usage, then run event-study/diff-in-diff on labour outcomes by exposure group and age.
**Where.** Massenkoff & McCrory, "Labor market impacts of AI" (Mar 2026): 97% of observed usage falls in β = 0.5 or 1 tasks; β = 1 tasks are 68% of usage, β = 0 only 3%; programmers 75% covered, data-entry keyers 67%; 30% of workers have zero coverage; exposed workers earn 47% more, are 16 pp more female, 11 pp more white; unemployment diff-in-diff since ChatGPT "small and insignificant"; detectable effect size ~1 pp; job-finding among 22–25-year-olds into exposed occupations falls ~0.5 pp per month, "a 14% drop ... barely statistically significant", none for over-25s; robustness across treatment cutoffs (median to 95th percentile) and using UI claimant data.
**Classic reference.** Eloundou et al. (2023) "GPTs are GPTs"; Brynjolfsson, Chandar & Chen (2025) "Canaries in the Coal Mine"; Autor, Dorn & Hanson (2013) as the exposure-shock template; Callaway & Sant'Anna (2021) and Sun & Abraham (2021) for modern event studies; Gans & Goldfarb (2025) O-ring logic for the "which workers" question.
**Try it.** Download CPS basic monthly via IPUMS, merge the HF observed-coverage file by occupation, define top-quartile vs zero exposure, and plot the unemployment gap 2016–2026 with a post-Nov-2022 indicator; then restrict to ages 22–25 and use the matched-month panel to compute new-job starts.
**Interview questions.** Why weight augmentation at half? Why might a null on unemployment coexist with a real hiring effect? What is the minimum detectable effect and why does it matter for "no impact" claims?

### 8. Surveys linked to usage data

**What.** Field a survey (here, an AI-conducted one) to a random sample of users and link responses to that user's own usage classifications under privacy constraints; report the selection explicitly.
**Where.** Economic Index Survey announcement (monthly; "anyone with a personal account at least two weeks old may be invited"); June 2026 report: ~9,700 linked respondents, ≥5 sessions, up to 20 sessions per person, "Women ... make up only 12% of our linked respondent sample", computer/math ~30% of respondents vs 4% of employment; "Reported exposure systematically exceeds observed exposure"; on automation and sentiment, "the people most enthusiastic about AI are also the most willing to hand over entire tasks to it. We can't rule this out entirely."
**Classic reference.** Groves et al., *Survey Methodology*; Bick, Blandin & Deming (2024) "The Rapid Adoption of Generative AI" as the population benchmark; Humlum & Vestergaard (2025) Danish survey-register linkage.
**Try it.** With any small survey you can run (e.g. 30 colleagues), ask self-reported weekly AI hours and then compare with a log-based measure; compute the reported/observed ratio by self-reported enthusiasm.
**Interview questions.** How do you link survey to logs without a researcher seeing either identity or transcript? Which direction does response selection bias the "AI helps me" share? Why filter out infrequent users, and what does that cost?

### 9. AI-conducted interviews and open-ended classification at scale

**What.** A prompted interviewer with a fixed core script and adaptive follow-ups; transcripts coded by validated classifiers, with bottom-up clustering used to build categories before coding.
**Where.** Anthropic Interviewer (Dec 2025): 1,250 crowdworker professionals (1,000 general, 125 creatives, 125 scientists), 10–15 minute interviews, three stages (plan, interview, analyse). "What 81,000 people want from AI" (Mar 2026): 112,846 interviews in a week, 80,508 passing quality filters, 159 countries, 70 languages, four core questions; 72% gave job information; concerns multi-label; each classifier ≥90% human agreement on 25 labels; representativeness checked against the Economic Index (34% vs 36% coding). 81k-economics: 1–7 productivity scale; 48% emphasised scope, 40% speed. Limitations named: ordering/priming effects, dropout, self-selected users.
**Classic reference.** Krippendorff; Braun & Clarke (2006) thematic analysis; Chopra & Haaland (2023) "Conducting Qualitative Interviews with AI"; Zarifhonarvar and others on LLM-coded open text.
**Try it.** Write a four-question interview script with follow-up rules, run it on 20 volunteers with a chat model, then build a codebook by clustering answers before writing the classifier prompt; measure agreement on 25 hand-coded cases.
**Interview questions.** What does "hand-validated on 25 labels" buy you, and what does it miss for rare codes? How do you check that a self-selected interview sample resembles the user base? Why exclude incomplete interviews only from the analyses that need the missing answers?

### 10. Randomised controlled trials of AI use

**What.** Random assignment to AI/no-AI, with outcomes chosen to separate output from learning or process.
**Where.** Shen & Tamkin (arXiv 2601.20245): 52 developers (26 per arm), $150, Trio library, 35 minutes; 14-question/27-point quiz on concepts, code reading and debugging; AI group scored 4.15 points lower (17%), d = 0.738, p = 0.010; no time difference; six interaction patterns (delegation and progressive reliance <40%, conceptual inquiry ≥65%). Project Fetch: 8 researchers, 4 vs 4; Team Claude 7/8 tasks vs 6/8, "about half the time", 9× more code, negative emotion d = 2.16 (p = 0.0017) — explicitly "one experiment with two teams". Persuasiveness: 28 topics × 2 claims, 3,832 human writers, 1–7 Likert pre/post, three raters per argument, the "Deceptive" prompt most persuasive. Discrimination: 70 decision scenarios with demographic attributes varied in prompts. Coding-agents-in-social-science: baseline for an RCT giving Claude Code access to 1,260 researchers, with the observational gap (users post ~half a working paper more) explicitly "not ... causal".
**Classic reference.** Brynjolfsson, Li & Raymond (2023) customer-support RCT; Noy & Zhang (2023); Dell'Acqua et al. (2023) "jagged frontier"; Peng et al. (2023) Copilot; METR (2025) developer RCT (a 19% slowdown); Duflo, Glennerster & Kremer (2007) toolkit; Bastani et al. (2024) on AI and learning.
**Try it.** Design a 40-person two-arm study on a small learning task; pre-register the primary outcome (a quiz, not task speed), compute the sample needed for d = 0.7 at 80% power, and write the analysis plan including the interaction-pattern coding.
**Interview questions.** Why is the quiz, not completion time, the primary outcome? What is the ecological-validity cost of a 35-minute lab task? With n = 8, what can Project Fetch legitimately claim?

### 11. Meta-analysis and evidence review

**What.** Systematic search, strict inclusion, random-effects pooling, meta-regression, and cost-benefit.
**Where.** "Reviewing the evidence on worker retraining programs" (WorkerRetraining.pdf, 2026): 146 impact estimates from 56 US randomised trials since 1973, plus 7 European RCT/RD studies and 2 judge-randomisation studies; REML random effects with study-clustered SEs; employment +2.5–2.9 pp in year 2, +1.7–1.8 pp in years 3–5 from a ~60–63% base; earnings +$1,139 and +$791 per year (2025 dollars) against ~$13,000 cost; sector programs raise earnings $5–10k; the CET replication "failed at all 14 trial sites"; Claude extracted traits and impacts from long government reports with a "reasoning table" and "adversarial review", spot-checked by humans; publication bias judged low because most trials were government-funded.
**Classic reference.** Card, Kluve & Weber (2018); Borenstein et al., *Introduction to Meta-Analysis*; Egger funnel tests; LaLonde (1986) and Heckman, LaLonde & Smith (1999) on training evaluation.
**Try it.** Clone github.com/droodman/job-training-meta-analysis, re-run the random-effects means, and then re-estimate excluding sector programs; draw the funnel plot.
**Interview questions.** Why ITT rather than treatment-on-treated? Why does low compliance shrink effects? What is the argument that publication bias is smaller in government-commissioned trials?

### 12. Measuring values and behaviours in the wild

**What.** Extract normative considerations from responses, build a bottom-up taxonomy, and compare across contexts, models and languages with controls for what users asked.
**Where.** Values in the Wild (Apr 2025): 308,210 subjective conversations; 3,307 values; 28.2% strong support, 3.0% strong resistance; mirroring in 20.1% of supportive vs 1.2% of resisting interactions. Claude values across models and languages (2026): 309,815 conversations, three models × 20 languages, ~5,000 per pair, 339 compressed values, 18 near-universal values dropped, four axes explaining 15% of variance, "controlled for each conversation's task, topic, and user-expressed values". Affective use: 2.9% of 4.5M conversations, 131,484 analysed, sentiment measured from first three to last three messages on −1..+1. Personal guidance: ~6% of 639k, sycophancy 9% overall and 25% in relationship advice.
**Classic reference.** Schwartz (1992) theory of basic values; Haidt's moral foundations; Rokeach; Grimmer & Stewart (2013) for text-as-data.
**Try it.** On a public dialogue dataset, prompt a model to list values expressed in each assistant turn, embed and cluster, and compute how the top-20 value shares change across three topic categories after residualising on topic.
**Interview questions.** Why restrict to subjective conversations? What is circular about Claude classifying Claude's values? Why control for user-expressed values before comparing languages?

### 13. Agent autonomy measurement

**What.** Use tool-call logs and session metadata to measure how long agents run unattended, how often humans intervene, and how risky/irreversible actions are.
**Where.** "Measuring agent autonomy" (2026): 99.9th-percentile turn duration "from under 25 minutes to over 45 minutes" (Oct 2025–Jan 2026); auto-approve in ~20% of new-user sessions rising to >40%; interruptions 5% → 9% of turns; on the hardest tasks Claude asks for clarification more than twice as often as humans interrupt; 998,481 API tool calls; 0.8% irreversible; software ~50%. Claude Code expertise: novices trigger ~5 actions and 600 words per prompt, experts 12 actions and 3,200 words; verified success 15% (novice) vs 28–33%; "verified" requires a hard signal (commit, PR, passing tests, explicit affirmation).
**Classic reference.** Sheridan & Verplank (1978) levels of automation; Parasuraman, Sheridan & Wickens (2000); METR (2025) task time-horizon methodology.
**Try it.** Instrument a small agent loop of your own to log tool calls, elapsed time per turn, and a model-scored reversibility flag; plot the turn-duration distribution and the share of turns ending in a clarification request.
**Interview questions.** Why is "human in the loop" at the API level unobservable? Why does a sampling frame of tool calls over-represent long workflows? What separates "judged" from "verified" success?

### 14. Capability evaluation with explicit cost accounting

**What.** Report capability together with the hours and dollars needed to obtain it, and benchmark against historical human timelines.
**Where.** N-days (2026): 18 SpiderMonkey patches and 21 Windows kernel EoP CVEs; Mythos Preview 14/18 crash PoCs, 8 working Firefox exploits in ~12 hours (first in under an hour); Windows: 18/21 triggers, 8 full chains at "$15,700 in API credits—an average of about $2,000 per privilege escalation", 13 of 14 "Exploitation Less Likely/Unlikely" bugs exploited; 50-trial consistency runs; contrast with WannaCry's 59 days and "expert-weeks". Attack Navigator: 832 banned accounts, 13,873 observations, 482 ATT&CK techniques, an additive 0–100 ARiES score chosen over a multiplicative one. Recursive self-improvement page: a supervised research project where agents recovered 97% of a gap in 800 cumulative hours for ~$18,000 versus two humans recovering 23% in a week; code-optimisation speedups from ~3× to ~52×. Multiagent systems: 266 vulnerabilities over a 27M-token run vs 21 over 6.5M tokens for independent agents; n = 400 and n = 120 episodes per model in the epistemic and turf-war experiments.
**Classic reference.** Weidinger et al. (2023) sociotechnical evaluation; the Anthropic "Challenges in evaluating AI systems" post (MMLU formatting shifts of ~5%, a week to implement BBQ, HELM taking months); Kapoor & Narayanan on cost-controlled leaderboards.
**Try it.** Take any public agent benchmark, run one model on 20 tasks, and report success rate, wall-clock, tokens and dollars per success, plus a pass@k consistency curve.
**Interview questions.** Why report dollars per exploit rather than success rate alone? What does a 50-trial consistency run tell you that a single run does not? Why did Attack Navigator choose additive scoring?

### 15. Production-function reasoning about productivity claims

**What.** Treat "X× more output" claims as inputs to a growth model, ask what is measured (quantity vs quality), whether uplifts compound, and which bottlenecks bind.
**Where.** "When AI builds itself" / recursive-self-improvement page: >80% of merged code authored by Claude, "the typical engineer was merging 8× as much code per day" in Q2 2026 vs 2024, with the caveat "Lines of code is an imperfect measure"; a March 2026 poll of 130 researchers with a median ~4× self-estimate that "the true degree of uplift ... was somewhat lower". Aug 2026 Risk Report §3.4–3.5: geometric-mean self-reported uplift "on the order of 4×", 1 of 18 thought a drop-in entry-level researcher existed, 4 of 18 gave ≥50% within three months; 57/886 sessions with unverified claims; CoBench (449 problems, 85% as the substitution bar, 300k vs 900k token budgets differ by ~3 pp); "meaningful acceleration starting in early-to-mid 2025, though by less than a factor of 2"; the RSP trigger is a doubling of pre-AI progress rates. "How AI is transforming work at Anthropic": 132 respondents (31% response), Claude share of work 28% → 59%, self-reported productivity +20% → +50%, 27% of Claude-assisted work "wouldn't have been done otherwise", with social-desirability and recency bias named.
**Classic reference.** Solow (1957) growth accounting; Jones (1995) semi-endogenous growth; Bloom, Jones, Van Reenen & Webb (2020) "Are ideas getting harder to find?"; Erdil & Besiroglu (2023) on explosive growth; Davidson (2023) takeoff model. On the "8 ≈ e²" point: 8× = e^2.08, i.e. about two natural-log units; because multiplicative uplifts add in logs, a 2-log-unit rise in one *input* (code merged) must be run through the input's elasticity in a production function before it says anything about *output* growth — an 8× rise in lines of code with elasticity 0.25 is a 1.7× rise in output, and less if quality falls. **[unverified: no METR document fetched contains this remark; the two METR review PDFs and the blog say only that "a median 1.4–2x self-reported change in value of work" is the relevant survey benchmark and recommend "tracking metrics like algorithmic efficiency over time or spend on various inputs to AI R&D" as leading indicators.]**
**Try it.** Take the 8× code figure and the 4× survey figure; write a Cobb-Douglas research production function with code, judgment and compute as inputs; show what elasticity of output to code volume is required for either figure to imply a 2× rate of progress.
**Interview questions.** Why is a geometric mean the right average for uplift factors? Why does "8× more code" not imply 8× more research? What leading indicator would you add and why is it less gameable than a survey?

### 16. External data release and independent replication

**What.** Publish aggregate data and code, allow outside researchers to run their own classifiers over private data without seeing it, and cite external replications.
**Where.** Hugging Face EconomicIndex (six releases, prompts in the appendix, labor-market coverage files); Massenkoff & McCrory's coverage published there; Clio-derived Anthropic Insights pilot ("Enabling independent research", 2026): Stanford SALT, Oxford HIP Lab and METR ran questions over ~250,000 Claude.ai/Claude Code conversations from Apr–May 2026, seeing "only ... final categories and the percentage of conversations", with an Imperial College London privacy audit, legal review limited to four enumerated grounds, <5% of categories altered, and "researchers are free to publish their results even if they are inconvenient for Anthropic". Retraining review code at github.com/droodman/job-training-meta-analysis. The Jan 2026 report cites Brynjolfsson, Chandar & Chen using the automation/augmentation split externally.
**Classic reference.** Nosek et al. (2015) transparency and openness guidelines; Christensen & Miguel (2018) on replication in economics; Card & Krueger (1995) on data availability.
**Try it.** Pick one headline number from any release (e.g. the 0.7 GDP elasticity) and reproduce it from the raw file, documenting every choice you had to make that the report did not pin down.
**Interview questions.** What can external researchers see under Insights, and what can they not? Which choices in a release are irrecoverable from the aggregates (window, classifier version)? Why does "inconvenient results may be published" matter for credibility?

### 17. Diff-in-diff and fixed-effects specifications on internal panels

**What.** Compare groups over time with progressively richer fixed effects to separate composition from within-unit change.
**Where.** March 2026 report on tenure: bivariate, then "fixed effects for specific O*NET tasks and request clusters", then "full controls" with model, use case and country fixed effects; all primitive differences p < 0.001 except human-only time (p < 0.05); survivorship and self-selection of high-tenure users named. Coding-agents survey: adjusted comparisons "controlling for career stage, discipline, and the week they completed the survey" with robust SEs.
**Classic reference.** Angrist & Pischke ch. 5; Bertrand, Duflo & Mullainathan (2004) on serial correlation; Goodman-Bacon (2021).
**Try it.** From the 2026-03-24 release, regress success rate on tenure with and without task fixed effects and read the change in the coefficient as the composition share.
**Interview questions.** What does adding task fixed effects remove? Why is survivorship a threat to a tenure gradient? When is week-of-response a necessary control?

### 18. Public-input elicitation for normative choices

**What.** Use deliberative platforms to source rules, then test whether the resulting model differs.
**Where.** Collective Constitutional AI (2023): ~1,000 US adults on Polis, 1,127 statements, 38,252 votes, 275 accepted statements against 58 in the standard constitution, ~50% overlap; no significant differences on MMLU/GSM8K or Elo, lower BBQ bias on all nine dimensions.
**Classic reference.** Fishkin deliberative polling; Ovadya & Thorburn on platform democracy; Bai et al. (2022) Constitutional AI.
**Try it.** Run a 30-person Polis-style vote on 20 AI-behaviour statements, cluster opinion groups, and write the rules that achieve cross-group majority.
**Interview questions.** Why weight by cross-group consensus rather than raw majority? What did deduplication risk?

---

## C. House style

**Structure.** Executive summary with 4–6 bolded findings; numbered chapters (usage, geography, primitives, tasks/productivity); a methods chapter placed *inside* the report rather than in an appendix; extensive footnotes with every threshold and sensitivity; a "data availability" line; a BibTeX block. Blog posts mirror this: what we did, what we found, what we can't say, what's next, then the dataset link.

**Hedging conventions.** Numbers are given to one decimal at most, usually rounded ("~1.8 percentage points", "on the order of 4×"); "early evidence" means a first pass on a short window that is expected to be revisited ("our estimates are based on just three months of data ... We will revisit"); "tentative" and "barely statistically significant" are used rather than dropped; a headline is almost always followed by the mechanical alternative that would have produced a different number.

Verbatim examples:

1. "This estimate should be taken as an exercise exploring what might happen based on current usage patterns, not a prediction of the impact on productivity that is actually most likely to happen." (Estimating productivity gains)
2. "Using survey data from the US, we find no impact on unemployment rates for workers in the most exposed occupations, although there's tentative evidence that hiring into those professions has slowed slightly for workers aged 22-25." (Labor market impacts)
3. "We selected a final set of nine new classifiers for the five primitives, all of which are directionally accurate even if they may deviate somewhat from human ratings." (Jan 2026 report)
4. "Differences should not be interpreted as causal, but as a first cut comparison between researchers using coding agents and those who are not." (Coding agents in social science)
5. "It's possible that this relationship is explained by selection, that the people most enthusiastic about AI are also the most willing to hand over entire tasks to it. We can't rule this out entirely." (June 2026 report)
6. "These self-reports are not free of bias: respondents may overestimate uplift on tasks they chose to delegate to Claude and underestimate it where the gain is in latency rather than task difficulty." (Aug 2026 Risk Report)
7. "Nothing above suggests that these failures are permanent—but nothing suggests they will fix themselves, either." (Multiagent systems)
8. "only one experiment with two teams—an obviously small sample size" (Project Fetch)

**Always released.** Aggregate data and prompts on Hugging Face; code for the retraining meta-analysis on GitHub; external reviews (METR) published with no redactions. A recurring "what we can't say" paragraph closes each report: outputs' downstream use, causation, representativeness, single provider, single window.

---

## D. What outsiders criticise, and what a good fellow proposal does about it

**1. Survey methods and leading indicators (METR, May 2026).** METR's review of the February 2026 Risk Report's R&D section found "significant issue(s)" in analytical rigor: the capability determination rested "primarily on the results of an internal survey of 16 Anthropic staff members"; the lowest response option ("Unlikely within 3 mo (<50% chance)") means "the level of risk could be anywhere between 0% and 50%"; survey title and table framing ("capabilities that we don't expect to see") anchor toward low capability; selective follow-up with the five higher-risk respondents could bias downward; one non-response was counted as a negative; and "from our previous experience running randomized controlled trials ... we are skeptical that respondents are calibrated". METR also argues that ruling out *full* automation does not rule out dramatic acceleration with humans still setting direction. Recommendations: finer response options (e.g. "<1%"), larger n, neutral wording, and tracking "algorithmic efficiency over time or spend on various inputs" as leading indicators. Anthropic's August report visibly responded: it "deprioritized this source of evidence", added CoBench, and reported AECI trend-break analysis. *Proposal move:* never let a self-report carry a risk conclusion; pre-register response scales that span the decision-relevant range; propose an input-side leading indicator you can compute from public data (compute spend, benchmark-per-dollar).

**2. Selection bias of Claude users.** Every report concedes it (coding over-represented; 12% women in the linked survey; 30% computer/math occupations vs 4% employment; "early adopters"). The retraining review adds the mirror-image problem: RCT subjects are "mostly low-income or persistently jobless", unlike future AI-displaced workers. *Proposal move:* benchmark against a population survey (Bick–Blandin–Deming), reweight by occupation × region × tier, and state results as "among users" unless reweighted.

**3. Classifier validity.** Validation sets are small (25 labels; "a small set of transcripts"); Claude estimates compress long tasks; Claude judges Claude's success and values; classifier upgrades shift shares (the Sonnet 3.7 → 4 rerun). *Proposal move:* dual-model classification with disagreement analysis, a larger consented gold set, a pre-specified calibration curve, and reporting classifier version as a covariate.

**4. Single-platform, single-turn data.** API records are prompt-response pairs, Claude Code excludes headless use "a substantial share of activity", and "agents built on other models may show different adoption patterns". *Proposal move:* triangulate with at least one non-Anthropic source (Upwork/ADP/job postings, or the Insights programme's independent counts), and treat API speedups as upper bounds.

**5. Conflicts of interest.** A vendor measuring its own product's productivity and safety; internal employee surveys with non-anonymous responses; METR's review passed through Anthropic publication review with veto rights ("METR aims to move in the direction of restricting publication review to purely cover redactions"). *Proposal move:* build the design so that inconvenient results are publishable by construction (pre-registration, external data custody, the Insights contractual terms), and include a falsifiable prediction that would embarrass the sponsor if wrong.

**6. Fragile aggregation choices.** The productivity headline moves from 1.8 to ~5 pp with a threshold change, halves with success adjustment, and spans 0.6–2.6 across σ. *Proposal move:* present the sensitivity table as the result, not the point estimate; specify σ from external evidence (e.g. within-occupation task substitution estimates) rather than sweeping it.

---

## E. A learning path

**Module 1 — The task-based frame (no Python required).** Read the Feb 2025 Economic Index paper (arXiv 2503.04761) alongside Autor, Levy & Murnane (2003) and Acemoglu & Restrepo (2018). Exercise: pick three occupations, list their O*NET tasks, and mark each as feasible (Eloundou β), observed, augmented or automated; compute time-weighted coverage by hand. Self-test: why does Anthropic's exposure differ from Eloundou's for Office & Admin (90% theoretical vs far lower observed)?

**Module 2 — Usage data and privacy-preserving classification (Python: pandas, sentence-transformers, an LLM API; ~2 days).** Read Clio (2412.13678) and Values in the Wild (2504.15236) with Grimmer & Stewart (2013). Exercise: build a mini-Clio on any public chat corpus with facet prompts, k-means, summaries, thresholds and a privacy-auditor prompt; validate on 100 synthetic conversations with known labels. Self-test: how do the 15/5 and 500/250 thresholds interact with the power-law of task frequency?

**Module 3 — Weighting, exposure and labour-market linkage (Python: pandas, statsmodels; or Stata/R).** Read Massenkoff & McCrory (Mar 2026 PDF), the Sept 2025 and Jan 2026 reports, and Brynjolfsson, Chandar & Chen (2025). Exercise: reproduce the state-level convergence regression (OLS and 2SLS) and the CPS diff-in-diff for top-quartile exposure; report the minimum detectable effect. Self-test: explain in one paragraph why attenuation bias makes OLS convergence look faster and why workforce composition is a plausible instrument.

**Module 4 — Causal designs: RCTs, diff-in-diff, event studies (Python: statsmodels/linearmodels, or R).** Read Shen & Tamkin (2601.20245), Project Fetch, the persuasiveness study, and Brynjolfsson, Li & Raymond (2023); Callaway & Sant'Anna (2021) for staggered designs. Exercise: write a pre-analysis plan for a 100-person RCT of AI assistance on a learning outcome, with power calculation for d = 0.5, a primary quiz outcome, and a secondary interaction-pattern coding; then simulate the data and run the analysis. Self-test: with n = 8 what is the widest claim Project Fetch can support, and how would you scale it?

**Module 5 — Surveys, interviews and linkage (minimal Python: pandas for tabulation).** Read the Anthropic Interviewer page, the 81k study and its appendix, the Economic Index Survey announcement and the June 2026 report; Groves et al. for survey design and Chopra & Haaland (2023) for AI interviewing. Exercise: run a 20-person AI-conducted interview with four core questions, derive codes by clustering, write classifier prompts, validate on 25 hand-labelled transcripts, and compute the reported/observed AI-use ratio against any log you can access. Self-test: name three selection stages between "Claude user" and "linked respondent with ≥5 sessions" and the sign of the bias each introduces.

**Module 6 — Measuring agents and capabilities with costs (Python: an agent loop with logging; ~1 day).** Read Measuring agent autonomy, Claude Code expertise, N-days, Attack Navigator, the Aug 2026 Risk Report §3.4–3.5 and METR's review; METR's time-horizon paper (2025) and Solow (1957) as classics. Exercise: instrument a small agent to log tool calls, turn duration, clarification stops and a reversibility flag; run a 20-task benchmark reporting dollars and hours per success; then write a one-page production-function memo translating an "8× code" claim into an output-growth range under elasticities 0.2–0.6. Self-test: why did Anthropic deprioritise the researcher survey, and which leading indicator would you compute from public inputs?

Minimum Python across the path: Modules 1 and 5 need none; Modules 2, 3, 4, 6 need pandas plus one of statsmodels (3, 4), sentence-transformers and an LLM client (2), or a simple loop with logging (6). Everything in Module 3 can also be done in R or Stata.

---

### Source verification log

Fetched with usable content: all listed anthropic.com pages; arxiv.org/abs/2503.04761, 2412.13678, 2504.15236, 2511.15080 (abstract only), 2601.20245 (full HTML); huggingface.co/datasets/Anthropic/EconomicIndex; the Jan 2026 report PDF, the labor-market PDF, WorkerRetraining.pdf, the Aug 2026 Risk Report PDF (redirected to www-cdn), the 81k appendix PDF, the METR blog and both METR review PDFs. **[unverified]**: the "8 ≈ e²" attribution to METR; arXiv HTML/PDF of 2511.15080 (404 / size limit).
