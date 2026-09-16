# Anthropic Fellows Program — The Anthropic Institute (Economics & Policy) track: mentor profiles

Compiled 2 September 2026. Listing: https://job-boards.greenhouse.io/anthropic/jobs/5183053008 (fetched 2 Sep 2026). Every URL below was fetched or returned by search during compilation; items I could not open are marked **[unverified]**.

> **Identity note.** The "Jim Baker" on this listing is **James H. Baker**, former Director of the Pentagon's Office of Net Assessment (2015–2025), who joined Anthropic as strategist-in-residence in May 2026 (Defense One, 1 May 2026). He is a different person from the former FBI General Counsel of the same name; no material on the latter is included here.

---

## 0. What the listing says (context for all five)

- 4-month, full-time, starts January 2027 (rolling; flexible). Stipend $3,850/£2,310/C$4,300 per week; ~$15k/month compute; work authorisation in US/UK/Canada required; no visa sponsorship. "Over 80% of prior fellows produced published work"; 25–50% of prior fellows received full-time offers. (Listing, fetched 2 Sep 2026.)
- Mentors: **Economics** — Maxim Massenkoff, Peter McCrory. **Policy, Security & Society** — Jack Clark, Marina Favaro, Jim Baker.
- Example project areas (verbatim themes from the listing): empirical research on AI's economic effects; methods for studying AI's labour-market impact; offense–defense analysis for AI-enabled cyber/bio capabilities; model-performance measurement with custom assessment tools; market mechanisms for societal resilience to AI threats; **metrics as early-warning signals for recursive self-improvement**.
- Selection language: Python fluency; strong technical background (CS/maths/physics); "fast implementation"; clear written communication; "ability to translate research into actionable recommendations."
- The Institute's own page lists four pillars: *AI, jobs, and the economy*; *Threats and resilience*; *How AI systems behave in the wild*; *AI research and development* (autonomous self-improvement, human oversight, governance). https://www.anthropic.com/institute

---

## 1. Maxim Massenkoff — Economics

**Current role.** "Head of core economic research at Anthropic" per his personal site (http://maximmassenkoff.com/); described as "Economist at Anthropic" by INET Oxford and NBER (https://www.nber.org/people/massenkoff, email maxim@anthropic.com). **Join date not verified.** Inference: he is *not* an author on the Sept 2025 Economic Index report, is a lead author on the Jan 2026 report, and his Oct 16 2025 working paper still carries an NPS affiliation — so he most likely joined in Q4 2025. **[inference, unverified]**

**Career.** Research Assistant, Federal Reserve Board, Aug 2010–Jun 2012 (large datasets on banking, mortgages, voting; Java and Python automation; S-plus charts for the Board of Governors); Research Assistant, Harvard Psychology Department, Jun 2012–Jun 2014 ("designing and conducting experiments studying the evolution of moral cognition, language, and disputes", i.e. the Pinker/DeScioli lineage behind *What happens in vagueness*) [LinkedIn, pasted by Emily 7 Sep 2026]; PhD Economics, UC Berkeley (2020); Assistant Professor, Naval Postgraduate School; Applied Scientist at Elicit (AI research-assistant startup); then Anthropic. Research "covered in the New York Times, The Economist, and… Marginal Revolution." (INET Oxford event page: https://www.inet.ox.ac.uk/events/labor-market-impacts-of-ai-a-new-measure-and-early-evidence; personal site.)

**Key publications (verified).**
- *An evidence review of worker retraining* (with David Roodman, independent), 12 Aug 2026. Meta-analysis of 146 impact estimates from 56 US RCTs (1973–present): training raises employment by ~1.7 pp and earnings by ~$800/yr on average; large federal programmes "mostly come up short"; a few "sector programs" lift pay $5–10k/yr but "filter out >80% of applicants"; recommends a "fire drill" evaluation to scale and randomize leading programmes. Code: github.com/droodman/job-training-meta-analysis. https://www-cdn.anthropic.com/4ef47f859bc67be739a14f5d40b43927eecacdb6/WorkerRetraining.pdf
- *Anthropic Economic Index report: Cadences* (with Lyubich, Sacher, Hitzig, Zhang, Heller, McCrory), 26 Jun 2026. Hourly-level sampling; a classifier for 30+ output "artifact" types ("93% of Claude conversations" produce an identifiable output); privacy-preserving linkage of ~9,700 survey responses to usage; personal share rises from ~35% weekdays to ~50% weekends; women show 0.33 SD lower automation share; users who delegate whole tasks are *more* optimistic about their careers. https://www.anthropic.com/research/economic-index-june-2026-report
- *What 81,000 people told us about the economics of AI* (with Saffron Huang), 22 Apr 2026. Open-ended survey classified by Claude; ~1/5 worried about displacement; early-career workers more anxious; "U-shaped" threat response. https://www.anthropic.com/research/81k-economics
- *Anthropic Economic Index report: Learning curves* (with Lyubich, McCrory, Appel, Heller), 24 Mar 2026. High-tenure users ~5 pp (4 pp with O*NET task and request-cluster fixed effects) more likely to have a successful conversation; users pick Opus for higher-wage tasks (+1.5 pp per $10 wage on Claude.ai, +2.8 pp on API); top-10 tasks fall from 24% to 19% of traffic. https://www.anthropic.com/research/economic-index-march-2026-report
- *Labor market impacts of AI: A new measure and early evidence* (with McCrory), 5 Mar 2026. Introduces **"observed exposure"** — Eloundou et al. (2023) theoretical exposure weighted by actual automated, work-related Claude usage — and tests it against CPS unemployment and job-finding rates. Computer & math occupations: 94% theoretical vs ~33% observed coverage. "We find no systematic increase in unemployment for highly exposed workers since late 2022, though we find suggestive evidence that hiring of younger workers has slowed in exposed occupations" (22–25-year-olds, ~14% lower job-finding, "just barely statistically significant"). Highly exposed workers are 16 pp more likely female, earn 47% more, ~4x as likely to hold graduate degrees. https://www.anthropic.com/research/labor-market-impacts ; PDF https://cdn.sanity.io/files/4zrzovbb/website/3f7fd9d552e66269bdb108e207c5d80531d04b8b.pdf ; coverage: https://www.theregister.com/software/2026/03/07/anthropic-bods-say-ai-hasnt-had-much-impact-on-jobs/5180415
- *Anthropic Economic Index report: Economic primitives* (lead author with Appel and McCrory; plus McCain, Heller, Neylon, Tamkin), 15 Jan 2026. Five "primitives" elicited by asking Claude about anonymized transcripts: user/AI skill (education level), task complexity (human time-to-complete), autonomy, success, and purpose (work/school/personal). Success falls with task length "much like prominent evals measuring the longest tasks that AIs can reliably perform"; success-weighted exposure; travel agents would be *deskilled*, property managers *upskilled* if observed tasks were removed. https://www.anthropic.com/research/anthropic-economic-index-january-2026-report ; PDF https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf
- *How predictable is job destruction? Evidence from the Occupational Outlook*, working paper, 16 Oct 2025 (NPS affiliation). Tests 80 years of BLS forecasts (~4,000 predictions): informative, but "technology-focused forecasts were less accurate because, on average, they underestimated the extent of job loss." http://maximmassenkoff.com/papers/OccupationalOutlooks.pdf
- *What happens in vagueness* (with DeScioli, Thomas, Pinker), *J. Economic Behavior & Organization*, Nov 2025. https://www.sciencedirect.com/science/article/pii/S0167268125002811
- *Rubbing Shoulders: Class Segregation in Daily Activities* (with Nathan Wilmers), *J. Public Economics*, Apr 2025. https://www.sciencedirect.com/science/article/pii/S0047272725000337 [page content 403; citation from personal site]
- *Family formation and crime* (with Evan K. Rose), *AEJ: Applied*, 2024 (47 cites) and *Activity-adjusted crime rates show that public safety worsened in 2020* (with Aaron Chalfin), *PNAS*, 2022 (45 cites) — from Google Scholar (https://scholar.google.com/citations?user=aYALu3oAAAAJ&hl=en; 1,310 citations, h-index 11). Also coauthor on the 2013 JPSP "How universal is the Big Five?" (Gurven et al., 729 cites).
- **Talk:** INET Oxford, Economics, Inequality and Opportunity Programme, online, 14 May 2026, hosted by Zachary Parolin (URL above).

**From his CV (maximmassenkoff.com/CV.pdf, dated Feb 2025, saved as sources/massenkoff-cv.pdf; fetched 7 Sep 2026).** Teaching: probability and statistics, applied econometrics (NPS); program evaluation (Goldman School, 2018); game theory and psychology (Harvard and MIT, 2013–14); Bok Prize for Teaching Excellence, Harvard 2014. Moral-psychology publications: "Kill or die: Moral judgment alters linguistic coding of causality" (with De Freitas, DeScioli, Nemirow, Pinker; JEP:LMC 2017); "Equity or equality? Moral judgments follow the money" (DeScioli, Kurzban, Shaw, Petersen; Proc R Soc B 2014); "How universal is the Big Five? Testing the five-factor model among forager-farmers in the Bolivian Amazon" (Gurven et al., JPSP 2013). Labour: "Economic outcomes of strikers in an era of weak unions" (JOLE 2024), "Wage stagnation and the rise of merit pay" (AEJ Applied 2023), "Racial inequality in the US unemployment insurance system" (NBER WP 30252), "Job search and unemployment insurance: new evidence from one million audits". Crime and health: "A new racial disparity in traffic fatalities" (JAMA Surgery 2024), air pollution and birth weight. Work in progress: "People, Places, and Moves: Place Effects in the US Military" (Heissel, Rose); "How common are compelling event studies?"; congestion pricing in NYC (Rothstein, Walker) and the NJ temporary-worker bill of rights (Rothstein), both with OSF pre-analysis plans. Reviewer for AER, AEJ Applied, AEJ Policy, JOLE, JPubE, REStat. Upjohn Early Career Award 2022. What this adds: he pre-registers; he is sceptical of weak identification ("how common are compelling event studies?"); he separates place from people; and he has tested whether a Western psychological construct holds in another culture, which is exactly the classifier-validity question in the mood post.

**Interests, themes, vocabulary.** Applied micro / labour economist with a crime-and-family background who now does *measurement* of AI diffusion: "observed vs theoretical exposure," "coverage," "task success," "learning-by-doing," "augmentation vs automation," "deskilling/upskilling," "humility" about forecasting ("the track record of past approaches gives reason for humility"). Strong taste for historical baselines (BLS Outlooks since the 1940s; 50 years of training RCTs) and for policy relevance (retraining is "the most popular policy… we ask if these efforts would work"). Pillar: *AI, jobs, and the economy*.

**What a fellow would do.** Empirical: Claude usage data mapped to O*NET/BLS/CPS; regressions with task fixed effects; survey linkage; meta-analysis; possibly new "primitives" or exposure measures. Public data: Hugging Face `Anthropic/EconomicIndex` (six releases, Feb 2025–Jun 2026; https://huggingface.co/datasets/Anthropic/EconomicIndex).

**Handles.** Site http://maximmassenkoff.com/ ; Scholar aYALu3oAAAAJ ; NBER page ; LinkedIn https://www.linkedin.com/in/mmassenkoff/ [not opened]. No X/Bluesky found.

**Conversation hooks.**
1. The retraining review's "fire drill" RCT proposal — propose a concrete design (which sector programmes, what outcome horizon, how to select for the white-collar unemployed who differ from historical trainees).
2. The young-worker hiring signal (14%, borderline significant): can it be sharpened with LinkedIn/ADP/JOLTS-style data or with observed-exposure time series updated monthly?
3. His BLS-forecast paper found technology forecasts *underestimate* job loss — does the Economic Index's "coverage gap" (94% vs 33%) mean the same bias is operating today?
4. "Cadences" gender gap in automation share (0.33 SD) — mechanism? Occupation mix vs preferences vs trust.
5. Success-weighted exposure vs METR-style task horizons — a validation study linking the two.

---

## 2. Peter McCrory — Economics

**Current role.** Head of Economics, Anthropic; leads the Anthropic Economic Index (Exponential View, 15 & 21 Jan 2026: https://www.exponentialview.co/p/anthropics-head-of-economics-peter-mccrory ; https://www.exponentialview.co/p/anthropics-head-of-economics-on-ai ; Fortune 7 Apr 2026: https://fortune.com/2026/04/07/anthropic-peter-mccrory-ai-automation-white-collar-jobs-claude-recession/ ; LinkedIn headline "Head of Economics at Anthropic": https://www.linkedin.com/in/peter-mccrory-econ/ [not opened]). **Join date not verified**; he is lead author on the 15 Sep 2025 report, so at Anthropic by mid-2025.

**Career (partly verified).** PhD Economics, UC Berkeley — dissertation "Essays in Macroeconomics," advised by Yuriy Gorodnichenko, on using disaggregate cross-sectional variation to study aggregate policy effects (search snippet; eScholarship record https://escholarship.org/uc/item/6hq3j9d2 returned empty on fetch **[unverified]**). RePEc lists him at the **Federal Reserve Bank of St. Louis** with district "Report on Economic Conditions" pieces 2013–2016 (https://ideas.repec.org/f/pmc240.html) — i.e., a pre-PhD research role. A ZoomInfo record describes him as "Economist (US)" at **JPMorgan** (https://www.zoominfo.com/p/Peter-Mccrory/6422233561) **[weak source; not otherwise verified]**. CEPR profile exists (https://cepr.org/about/people/peter-b-mccrory, 403 on fetch).

**Academic papers (Google Scholar https://scholar.google.com/citations?user=_EHyNzIAAAAJ&hl=en; 703 cites, h-index 8).**
- *Unemployment effects of stay-at-home orders* (with Baek, Messer, Mui), *Review of Economics and Statistics*, 2021 — 252 cites.
- *Fiscal multipliers in the COVID19 recession* (with Auerbach, Gorodnichenko, Murphy), *J. International Money and Finance*, 2022 — 92 cites.
- *A cup runneth over: Fiscal policy spillovers from the 2009 Recovery Act* (with Bill Dupor), *Economic Journal*, 2018 — 91 cites.
- *The Local-Spillover Decomposition of an Aggregate Causal Effect* (with Conley, Dupor, Ebsim, Li), *St. Louis Fed Review*, 2026 (RePEc).
- SSRN author page: https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=2975423 (403 on fetch).

**Anthropic outputs.** Lead author, *Economic Index: Uneven geographic and enterprise AI adoption*, 15 Sep 2025 (with Appel, Tamkin; McCain, Neylon, Stern) — introduces the **Anthropic AI Usage Index (AUI)**; first enterprise API analysis (77% automation vs 50% consumer); "directive" conversations rose 27%→39%. https://www.anthropic.com/research/anthropic-economic-index-september-2025-report ; arXiv https://arxiv.org/pdf/2511.15080. Co-lead on *Economic primitives* (Jan 2026), coauthor on *Learning curves* (Mar 2026) and *Cadences* (Jun 2026), coauthor of *Labor market impacts of AI* (Mar 2026) — all URLs in §1. A search summary attributes to him an essay "Why hasn't AI increased unemployment?" — **URL not found; unverified.**

**Media and positions (quotes).**
- "We understand the coal industry better than the AI economy right now"; "Capability doesn't instantly deliver adoption"; adoption follows "a staircase" not a smooth curve; "tacit knowledge extraction"; "cognitive endurance." (Exponential View, 21 Jan 2026.)
- "AI might very well be an innovation in the method of innovation itself"; "For some jobs, there might be de-skilling where Claude's taking over the most complex tasks in your job." (Exponential View, 15 Jan 2026.)
- "exposure to AI is by no means fatal"; "jobs as bundles of tasks is a very useful analytic frame." (Fortune, 7 Apr 2026.)
- Marketplace, 1 Jul 2026, "How Anthropic is tracking AI's impact on the labor market" (https://www.marketplace.org/episode/2026/07/01/how-anthropic-is-tracking-ais-impact-on-the-labor-market) **[403 on fetch; content unverified]**. X interview clip via @MTSlive (https://x.com/MTSlive/status/2091252532689658001) **[unverified]**.

**Interests, themes.** Macro/empirical-macro economist (fiscal multipliers, spillovers, COVID labour shocks) turned AI-diffusion measurer. Vocabulary: "augmentation vs automation," "task bundles," "observed exposure," "adoption lag," "method of innovation," "de-skilling." Pillar: *AI, jobs, and the economy*, with an eye to macro aggregates (productivity, unemployment, GDP).

**What a fellow would do.** Empirical macro/labour: CPS/BLS/O*NET plus Economic Index data; cross-sectional identification (his signature — regional/occupational variation to infer aggregates); time-series monitoring of exposure vs unemployment; possibly firm-level API-usage analysis.

**Handles.** X @PeterMcCrory (https://x.com/PeterMcCrory) ; LinkedIn peter-mccrory-econ ; Scholar _EHyNzIAAAAJ ; RePEc pmc240 ; SSRN 2975423.

**Conversation hooks.**
1. His "local-spillover decomposition" method — could it be applied to AI adoption (regional AUI shocks and spillovers to non-adopting regions)?
2. "Staircase" adoption: propose a formal test using the Index's monthly aggregates (released Jun 2026).
3. The Sept 2025 finding that enterprise API use is *less* price-sensitive than expected — implications for a productivity-vs-wage decomposition.
4. "Coal industry better than AI economy" — what national-statistics gap would he most want a fellow to close (e.g., linking Claude usage to BLS OEWS or Census BTOS)?
5. Youth hiring slowdown vs the Cadences finding that delegators are more optimistic — reconcile.

---

## 3. Jack Clark — Policy, Security & Society

**Current role.** Co-founder; **Head of Public Benefit** and head of The Anthropic Institute since the Institute's launch, 11 Mar 2026 (https://www.anthropic.com/news/the-anthropic-institute ; Engadget 11 Mar 2026: https://www.engadget.com/ai/anthropic-is-opening-an-office-in-dc-while-battling-pentagon-in-court-115700127.html ; his own X post https://x.com/jackclarkSF/status/2031746606496944609 [X blocked on fetch]). Previously Head of Policy / Policy Director at Anthropic (House testimony, Feb 2024).

**Career.** Technical journalist (The Register, Bloomberg BusinessWeek) → Policy Director, OpenAI → co-founded Anthropic (2021). Founding member of Stanford's AI Index (2017–2024); inaugural member of the US National AI Advisory Committee (2021–2024). Author of *Import AI* (~70k subscribers per his site; "over 100,000 weekly readers" per Oxford Schwarzman Centre). https://jack-clark.net/about/ ; https://www.schwarzmancentre.ox.ac.uk/people/jack-clark-bnrd

**Key writing and talks.**
- *When AI builds itself* (with Marina Favaro; editorial support Santi Ruiz), published 4 Jun 2026 (data through May 2026). Three scenarios (trend stalls; compounding efficiency gains with humans keeping direction-setting; full recursive self-improvement). Numbers: Claude authored >80% of merged production code (May 2026); 8x code per engineer since Q2 2024; 4x median self-reported productivity multiplier (Mar 2026 employee survey); model success at choosing better next research steps 51%→64% (Nov 2025→Apr 2026). Proposals: a verifiable mechanism for labs to *credibly pause* contingent on others doing so; training-run detection/verification ("harder than missile silos"); a deliberative multi-stakeholder process; **early-warning metrics** on capability benchmarks and "research judgment." Vocabulary: Amdahl's law, "research taste," "perspiration vs inspiration," "gift economy of small favors." https://www.anthropic.com/institute/recursive-self-improvement ; coverage TIME 7 Aug 2026 https://time.com/article/2026/08/07/ai-recursive-self-improvement-anthropic-openai/
- *Import AI 431: Technological Optimism and Appropriate Fear*, 13 Oct 2025 (remarks at The Curve, Berkeley). "What we are dealing with is a real and mysterious creature, not a simple and predictable machine"; "The pile of clothes on the chair is beginning to move"; "We must do a better job of listening to the concerns people have"; "Force us to share economic data… force us to monitor… force us to publish details"; "There will surely be some crisis. We must be ready to meet that moment with policy ideas and a pre-existing transparency regime." https://jack-clark.net/2025/10/13/import-ai-431-technological-optimism-and-appropriate-fear/ ; https://x.com/jackclarkSF/status/1977828314871218378
- *Challenges in evaluating AI systems* (Ganguli, Schiefer, Favaro, Clark), 4 Oct 2023 — six evaluation challenges; asks for funding of evaluation science, NIST-like capacity, legal safe harbours for security testing. https://www.anthropic.com/research/evaluating-ai-systems
- Written testimony, House Science, Space & Technology Committee, 6 Feb 2024 (as Policy Director): standardized capability measurement, NIST-led frameworks, transparency, third-party testing, risk-tiered governance, allied coordination. https://www.congress.gov/118/meeting/house/116790/witnesses/HHRG-118-SY15-Wstate-ClarkJ-20240206.pdf
- Recent *Import AI* (Jul 27–Aug 31, 2026; https://jack-clark.net/): "23 RSI ideas; PostTrainBench+; trust and transparency interplay with AI racing" (#468, 10 Aug); "Science AI; RSI simulator" (#469, 17 Aug); "Self-sustaining AI viruses; pacing AI progress" (#467, 3 Aug); "Five Eyes on AI" (#471, 31 Aug). Themes: RSI, emergent multi-agent coordination, lab collective-action problems, open-weight dual-use.
- Talks/interviews 2026: Oxford Schwarzman Centre, 20 May 2026 — "by the end of 2028, it's more likely than not that we have an AI system where you would be able to say to it: 'Make a better version of yourself'"; "Change is inevitable. Autonomy is not."; forecasts framed as "planning assumptions" (https://letsdatascience.com/blog/anthropic-jack-clark-60-percent-ai-builds-successor-2028). Cosmos HAI Lab Lecture, Oxford, 26 May 2026 (https://www.oxford-aiethics.ox.ac.uk/news/2026-cosmos-hai-lab-lecture-jack-clark-co-founder-anthropic). Reason podcast, 24 Jun 2026 — Institute is "a think tank with a supercomputer inside Anthropic"; "You need to start with mandated transparency from the companies about how they've tested their systems"; "You need to know how to measure it. You need to know how to potentially control it." (https://reason.com/podcast/2026/06/24/anthropic-co-founder-the-most-powerful-technology-ever-built/). Axios "Behind the Curtain: Intelligence explosion," 7 May 2026 (https://www.axios.com/2026/05/07/anthropic-jack-clark-ai-intelligence-explosion) [403; unverified]. CNN, June 2026: "all I have is a gas pedal. I don't have a brake pedal" (via ABC7, 5 Jun 2026: https://abc7news.com/post/san-francisco-based-anthropic-calls-global-freeze-ai-development-warns-could-soon-escape-human-control/19240090/). TIME, 7 Aug 2026: "I can't give you a specific number, because we don't have a measure"; "the constraints are more organizational than resource driven today."
- Podcasts the brief mentions (80,000 Hours, Hard Fork): **not verified in this pass** (search budget exhausted).

**Recurring themes.** Measurement as the precondition of governance; mandated transparency; "appropriate fear"; AI as "creature"; compression of the timeline (coder speed-ups → RSI); pause/coordination mechanisms; legitimacy and "listening" to publics; human autonomy/sovereignty. Pillars: *AI research and development* (RSI early-warning) and *Threats and resilience*; also spans *AI in the wild*.

**What a fellow would do.** Mostly policy-relevant measurement: build metrics/dashboards for RSI early warning (research-judgment evals, code-share, productivity multipliers), transparency regimes, scenario/forecasting work; deliverables are public reports rather than journal papers.

**Handles.** X @jackclarkSF ; https://jack-clark.net ; https://importai.substack.com.

**Conversation hooks.**
1. "We don't have a measure" (TIME, Aug 2026) — propose one: an organisation-level acceleration index combining code share, merge throughput, research-step-selection accuracy, and compute per result.
2. The pause mechanism in *When AI builds itself*: what verification signal would be robust to training concealment? Tie to Favaro's arms-control background.
3. "Force us to share economic data" — sketch the minimal statutory transparency schedule and how the Economic Index could be a template.
4. His 60%-by-2028 "planning assumption" — what observable would change his mind by mid-2027?
5. Import AI #468's "trust and transparency interplay with AI racing" — model the collective-action problem among labs.

---

## 4. Marina Favaro — Policy, Security & Society

**Current role.** "Lead at The Anthropic Institute" per LinkedIn headline (https://www.linkedin.com/in/marina-favaro/ [not opened; headline from search]); co-author with Clark of *When AI builds itself* (Jun 2026); coverage calls her "lead at the Anthropic Institute." Joined Anthropic **January 2023** as Senior Policy Analyst (theorg.com listing: https://theorg.com/org/anthropic/org-chart/marina-favaro — the page rendered without her details on fetch; date from search snippet **[partly unverified]**). Non-Resident Fellow, UC Berkeley Risk & Security Lab, listed as "Marina Favaro, Anthropic" (https://brsl.berkeley.edu/non-resident-fellows/). Google Scholar (verified anthropic.com email): https://scholar.google.com/citations?user=ato2FJcAAAAJ&hl=en — 907 citations, h-index 11.

**Career.** Master's in International Relations and Politics, University of Cambridge. Analyst, RAND Europe (space security, cyber, defence innovation; e.g., *Exploring the use of Zcash cryptocurrency for illicit or criminal purposes*, RAND 2020). Managed the Emerging Technologies programme at BASIC (2020–21). Consultant, Centre for Science & Security Studies, King's College London. Research Fellow, Institute for Peace Research and Security Policy (IFSH), University of Hamburg. Methods: "quantitative and qualitative research… including futures and foresight methods (e.g. horizon scanning, STREAM, Delphi, and scenario development)." (Bulletin bio https://thebulletin.org/biography/marina-favaro/ ; ELN bio https://europeanleadershipnetwork.org/person/marina-favaro/ ; RAND author page https://www.rand.org/pubs/authors/f/favaro_marina.html [403].)

**Key publications.**
- *Weapons of Mass Distortion: A new approach to emerging technologies, risk reduction, and the global nuclear order*, KCL CSSS, June 2021. Ten emerging technologies clustered by ML into **distort / compress / thwart / illuminate**; deepfakes and satellite spoofing most dangerous for NC3; AI can also *support* verification. https://www.kcl.ac.uk/csss/assets/weapons-of-mass-distortion.pdf ; KCL news 2 Jun 2021 https://www.kcl.ac.uk/news/new-study-analyses-impact-of-emerging-technology-on-nuclear-safety ; ELN summary 19 Jul 2021 https://europeanleadershipnetwork.org/commentary/emerging-technologies-and-nuclear-stability/ ; APLN version https://www.apln.network/analysis/commentaries/emerging-technologies-and-nuclear-stability
- *We can't prevent tomorrow's nuclear wars unless we imagine them today* (with Sara Kutchesfahani), Bulletin, Aug 2021. https://thebulletin.org/2021/08/we-cant-prevent-tomorrows-nuclear-wars-unless-we-imagine-them-today/
- *Will DIANA—NATO's DARPA-style innovation hub—improve or degrade global stability?* (with Ulrich Kühn, Neil Renic), Bulletin, Mar 2023. https://thebulletin.org/2023/03/will-diana-natos-darpa-style-innovation-hub-improve-or-degrade-global-stability/
- *False sense of supremacy: emerging technologies, the war in Ukraine, and the risk of nuclear escalation* (with Heather Williams), *J. for Peace and Nuclear Disarmament*, 2023 (41 cites; Scholar).
- *Re-evaluating space norms in a changing orbital environment*, ELN, Jul 2020. https://europeanleadershipnetwork.org/commentary/re-evaluating-space-norms-in-a-changing-orbital-environment/
- *Confidence-Building Measures for Artificial Intelligence: Workshop Proceedings* (Shoker, Reddie, … Favaro, … Sellitto, Trager et al.), arXiv, Aug 2023 — hotlines, incident sharing, transparency cards, provenance, collaborative red-teaming, dataset/eval sharing. https://arxiv.org/abs/2308.00862
- *Challenges in evaluating AI systems* (with Ganguli, Schiefer, Clark), Anthropic, 4 Oct 2023 (URL in §3).
- Coauthor, *Sleeper Agents* (Hubinger et al., 2024; 621 cites) — policy contribution.
- *When AI builds itself* (with Clark), 4 Jun 2026 (URL in §3). Joint quote: "Full recursive self-improvement also might increase the risks of humans losing control over AI systems" (ABC7, 5 Jun 2026).
- UK Parliament written evidence (https://committees.parliament.uk/writtenevidence/35529/html/) **[403; unverified]**. The brief's "AI security for boards/investors" CLTC piece: search snippet says she wrote for the UC Berkeley CLTC blog on investors and board risk oversight, but a site search of cltc.berkeley.edu returned nothing — **unverified**. BRSL "Governing the cyber-AI nexus" side event (Apr 2023; https://brsl.berkeley.edu/2023/03/29/governing-the-cyber-ai-nexus/) — page did not confirm her role on fetch.

**Interests, themes, vocabulary.** Arms-control/foresight analyst applied to frontier AI: escalation dynamics, NC3, verification, confidence-building measures, scenario development, horizon scanning; now RSI early warning and "pause" verification. Vocabulary: distort/compress/thwart/illuminate; "imagine tomorrow's wars"; CBMs; Amdahl's law; research taste. Pillars: *AI research and development* and *Threats and resilience*.

**What a fellow would do.** Policy research with structured methods: scenario exercises, Delphi/expert elicitation, metric design for RSI signals, verification/CBM proposals, arms-control analogies tested against AI specifics — with a quantitative bent (she used ML clustering in 2021 and is comfortable with eval data).

**Handles.** LinkedIn marina-favaro ; Scholar ato2FJcAAAAJ ; Bulletin and ELN author pages. No X/Bluesky found.

**Conversation hooks.**
1. Map her 2021 distort/compress/thwart/illuminate taxonomy onto RSI: which AI-R&D capabilities *compress* decision time for governments?
2. Verification for a credible pause: adapt the CBM list (incident sharing, transparency cards) into a training-run verification protocol; evaluate against concealment incentives named in *When AI builds itself*.
3. Foresight methods — propose a Delphi on RSI indicators with the 64%/51% research-step metric as an anchor.
4. Her nuclear-analogy work vs the arXiv paper "The Nuclear Analogy in AI Governance Research" (https://arxiv.org/pdf/2510.21203) — where does the analogy break?
5. Frontier Red Team outputs (e.g., "Measuring LLMs' impact on N-day exploits," 8 Jun 2026; "Patterns and problems in emerging multiagent systems," 13 Aug 2026; https://www.anthropic.com/research/team/frontier-red-team) as inputs to an offense–defense resilience model.

---

## 5. James H. ("Jim") Baker — Policy, Security & Society

**Current role and timing.** Strategist-in-residence at Anthropic, "focusing on the policy and strategic implications of AI"; the hire was announced in late April and reported 1 May 2026. Remit: "lead analysis examining how AI impacts U.S. institutions and U.S.-China competition." Sources: Defense One, 1 May 2026 (https://www.defenseone.com/technology/2026/05/former-head-pentagons-think-tank-joins-anthropic/413256/); Washington Technology (https://www.washingtontechnology.com/companies/2026/05/former-head-pentagons-think-tank-joins-anthropic/413311/); CFR expert page (https://www.cfr.org/experts/jim-baker); Aspen Ideas speaker page (https://www.aspenideas.org/speakers/jim-baker). Whether he formally sits inside the Institute is **not stated** in these sources, but the remit matches the Institute's *AI R&D* and *Threats and resilience* pillars and the listing names him as a mentor. Concurrent affiliations (CFR page): Senior Fellow for Strategic Competition, Council on Foreign Relations; Distinguished Visiting Fellow, Hoover Institution; Senior Advisor, RAND; Managing Director, Halcyon Group LLC.

**Career.** Trained as an engineer; oversaw major defense technology programmes; strategist and advisor to two Chairmen of the Joint Chiefs of Staff; Director, Office of Net Assessment (ONA — "the Pentagon's think tank," est. 1973), 2015–2025, producing "long-range assessments that informed decisions by the secretary of defense, the joint chiefs of staff and other cabinet officers"; more than 17 years in senior strategy roles; three distinguished civilian service awards. ONA was shuttered in March 2025 and reinstated in smaller form in October 2025. During his tenure the office studied accelerating AI and its implications for Cold War-era institutions. (Aspen; CFR; Defense One.) **Education details beyond "trained as an engineer" not found.**

**Writing and appearances.**
- "Power, Policy, and the AI Race," HumanX, 13 Apr 2026 (video; listed in CFR archive https://www.cfr.org/experts/jim-baker/archive).
- "The Challenge of China," Aspen Ideas, 28 Jun 2025 (https://www.youtube.com/watch?v=lVop2l-H2Hc&t=1025s).
- **The Fitness of Nations** — a CFR diagnostic framework assessing national vitality through "100+ criteria across nine dimensions, from population and territory to governance, innovation, and military power," with an interactive platform in development for CFR's site; part of CFR's Future of American Strategy initiative (CFR page).
- Quotes on joining Anthropic: "We aren't spending enough time thinking about the implications of recursive self-improvement… a multi-decade structural—even civilizational—problem"; "The greatest risk is the long-term viability of present institutions in war and in peace." (Defense One / Washington Technology, May 2026.)
- **Co-author, *Claude's values across models and languages* (13 Jul 2026), verified 7 Sep 2026 from the byline** (Kearney, Zhang, Carter, Shen, Handa, ... Jim Baker, Troy, Botvinick, ... Ganguli, Durmus): 309,815 conversations, three models × 20 languages, four value axes (Deference–Caution, Warmth–Rigor, Depth–Brevity, Candor–Execution), systematic variation by language. His role on the 24-author byline is not stated. This is the only listed mentor with a byline on an *AI systems behavior in the wild* paper. https://www.anthropic.com/research/claude-values-models-languages
- Hoover profile page not found at guessed URLs **[unverified]**.

**Interests, themes, vocabulary.** Net assessment: long-range, comparative, institution-centred diagnosis of relative power; great-power competition (US–China); "fitness"/vitality of nations as multi-criteria indices; recursive self-improvement framed as a structural shock to the institutions that manage war and peace. Pillars: *Threats and resilience*; *AI research and development* (institutional consequences of RSI).

**What a fellow would do.** Strategic-analytic rather than econometric: build indicator frameworks (à la Fitness of Nations) for institutional resilience under rapid AI-driven change; comparative US–China assessments of AI-R&D acceleration (compute, talent, code-share, adoption); scenario/net-assessment memos with quantitative backbones. Python would go to data pipelines, indices, and dashboards more than causal inference.

**Handles.** CFR expert page; Aspen speaker page. No personal X/LinkedIn/site verified.

**Conversation hooks.**
1. Extend "Fitness of Nations" with an AI-R&D dimension using Economic Index and RSI metrics — a bridge to the economics mentors.
2. A net-assessment-style comparison of US vs China exposure to RSI-driven institutional stress (his stated remit).
3. "Long-term viability of present institutions" — pick one (procurement, courts, the Fed) and model how a 4–8x knowledge-work multiplier (numbers from *When AI builds itself*) changes its feedback loops.
4. The ONA closure/reinstatement (2025) as a case study in institutional fragility during rapid technological change.
5. Offense–defense balance from a net-assessment lens using Frontier Red Team cyber results (N-day exploits, Jun 2026; multiagent systems, Aug 2026).

---

## 6. How the mentors map to the fellowship's stated research areas

| Listing project area | Institute pillar | Primary mentor(s) |
|---|---|---|
| Empirical research on AI's economic effects | AI, jobs & the economy | Massenkoff, McCrory |
| Methods for studying AI's labour-market impact | AI, jobs & the economy | Massenkoff (observed exposure, retraining RCTs), McCrory (macro identification) |
| Offense–defense analysis for AI-enabled cyber/bio | Threats & resilience | Favaro (escalation/arms control), Baker (net assessment), with Frontier Red Team data |
| Model performance measurement with custom assessment tools | AI in the wild / AI R&D | Clark (evaluation science, transparency), Favaro |
| Market mechanisms for societal resilience | Threats & resilience | McCrory/Massenkoff (economics) with Favaro/Baker (policy) |
| Metrics as early-warning signals for RSI | AI R&D | Clark & Favaro (authors of *When AI builds itself*), Baker (institutional implications) |

**Revised 7 Sep 2026.** For *AI systems behavior in the wild*, no listed mentor owns the pillar; its papers come from the Societal Impacts team (Tamkin, Durmus, McCain, Huang, Handa), who are not mentors. Among the five: **Baker** is the only one with a byline on a pillar paper (values across models and languages, Jul 2026); **Clark** leads the Institute the pillar sits in and his themes (listening to publics, transparency, human autonomy) match, but his own writing is RSI and governance; the economists touch it through the autonomy primitive and the Clio-based Index. Earlier recommendation (Favaro and Clark) predates the applicant's research consolidating on cross-society usage and behaviour.

## 7. Signals about what they select for

- **From the listing:** Python fluency and "fast implementation" are hard requirements even on the policy side; outputs are expected to be *public* (papers/reports); "translate research into actionable recommendations."
- **From past fellow outputs:** *How AI Impacts Skill Formation* (Judy Hanwen Shen & Alex Tamkin, arXiv 28 Jan 2026, https://arxiv.org/abs/2601.20245) — a 52-developer RCT with behavioural coding of six interaction patterns; *Stress-Testing Model Specs* (Jifan Zhang, Anthropic Fellows Program, with Sleight, Peng, Schulman, Durmus; arXiv Oct 2025, https://arxiv.org/abs/2510.07686 ; https://alignment.anthropic.com/2025/stress-testing-model-specs/) — 300k+ generated scenarios, 12 frontier models, released dataset. Both are *empirical, scalable, and release artefacts*; both use LLM-based classification or generation as method. Earlier-cohort highlights (Built In: https://builtin.com/articles/anthropic-fellows-program): agentic-misalignment ("blackmail") work and $4.6M of smart-contract vulnerabilities; ">80% of the first cohort's participants produced research papers."
- **From the mentors' own work:** the Institute's house style is *measurement first* — new metrics (AUI, primitives, observed exposure, RSI indicators), privacy-preserving pipelines, public datasets, historical baselines, explicit humility about forecasting. Policy pieces (Clark/Favaro) are evidence-laden and end with concrete mechanisms (pause verification, transparency schedules). Baker's remit favours indicator frameworks.
- **Practical implication:** a strong application proposes one crisp, buildable measurement or empirical design tied to a named pillar, names the public data it would use (Economic Index on Hugging Face; Frontier Red Team evals; BLS/CPS/O*NET), and states the policy decision it would inform.

## 8. Items not verified (summary)
- Join dates at Anthropic for Massenkoff, McCrory, and Favaro (only inferred/snippet-based). Baker's Institute membership (vs. company-wide role).
- McCrory's JPMorgan stint (ZoomInfo only) and dissertation details (eScholarship page empty on fetch); "Why hasn't AI increased unemployment?" essay URL.
- Favaro's CLTC investors piece and UK Parliament evidence; her exact current title (LinkedIn headline only).
- Clark's 80,000 Hours / Hard Fork appearances; the Axios 7 May 2026 piece (403); his X post text.
- Baker's formal placement within the Institute and his education beyond "trained as an engineer"; Hoover profile page.
- Marketplace 1 Jul 2026 episode content (403).

## 9. Locations (checked 7 Sep 2026)
- Listing: "designated shared workspaces in London and Berkeley where fellows will work from and mentors will visit"; "open to remote fellows in the UK, US, or Canada"; applicants are asked about availability to work from Berkeley or London full- or part-time.
- Massenkoff: San Francisco Bay Area (LinkedIn/search summary). McCrory: San Francisco (LinkedIn/search summary). Favaro: moved from London to San Francisco in January 2023 to join Anthropic (LinkedIn post). Clark: San Francisco (handle @jackclarkSF; Anthropic HQ); Anthropic announced a DC office at the Institute launch (Engadget, 11 Mar 2026). Baker: not stated; CFR senior fellow and ex-Pentagon, so almost certainly Washington, DC **[inferred]**.
- Implication: none of the five is London-based. A UK fellow works remotely or from the London workspace with mentors visiting; Berkeley availability is worth offering if possible.
