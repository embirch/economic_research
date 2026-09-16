# The Anthropic Institute's three founding teams: verified dossiers

Prepared 2 September 2026 for an applicant to the Anthropic Fellows Program (Economics & Policy) hosted by The Anthropic Institute (TAI). Every URL below was fetched and checked on 2 Sept 2026 unless explicitly flagged in Section 5. Numbers are taken from the cited page; where a page did not name authors, that is stated rather than inferred.

## 0. Context: The Anthropic Institute (TAI)

- **Announced 11 March 2026** at https://www.anthropic.com/news/the-anthropic-institute. It combined three existing teams, in the announcement's words: "the Frontier Red Team, which stress-tests AI systems to understand the outermost limits of their current capabilities; Societal Impacts, which studies how AI is being used in the real world; and Economic Research, which tracks its impact on jobs and the larger economy."
- **Leadership.** Co-founder **Jack Clark** took the new role of Head of Public Benefit and leads the Institute. Named founding hires: **Matt Botvinick** (AI and the rule of law; ex-Google DeepMind), **Anton Korinek** (Economic Research; on leave from UVA), **Zoë Hitzig** ("connecting economics to model training"; ex-OpenAI). The Institute is also "incubating" work on forecasting AI progress and on AI and the legal system. Separately, **Sarah Heck** became Head of Public Policy, with a first DC office opening spring 2026.
- **Mission (institute page, https://www.anthropic.com/institute):** "The Anthropic Institute exists to understand and shape the consequences of powerful AI systems." The page lists four research areas: (1) **AI, jobs, and the economy**; (2) **Threats and resilience**; (3) **AI systems behavior in the wild**; (4) **AI research and development** (recursive self-improvement, oversight, governance). Note the live wording differs slightly from the "Economic diffusion / Threats & resilience / AI systems in the wild / AI-driven R&D" labels used in the brief (see Section 5). Featured projects on the page: "When AI builds itself," the 81,000-person interview study, and the Economic Index.
- **Hiring language to echo:** the announcement says TAI is "building out a small analytical staff who will work to pull various parts of our research agenda together and broadcast our work to the world."
- On https://www.anthropic.com/research the team filter offers Alignment, Economics, Interpretability, Societal Impacts, Frontier Red Team; each team has a page at https://www.anthropic.com/research/team/<slug>.

---

## 1. Frontier Red Team (FRT)

### Mission and history
- Team page: https://www.anthropic.com/research/team/frontier-red-team. Mission verbatim: "The Frontier Red Team stress-tests AI systems to understand the full extent of their current capabilities and anticipate what comes next," providing "evidence-based analysis about AI's implications for cybersecurity, national security, and autonomous systems."
- The team's blog **red.anthropic.com** now 301-redirects to the team page; every old post URL (e.g. `red.anthropic.com/2025/biorisk/`) redirects to a `www.anthropic.com/research/<slug>` or `/news/` page. The archived blog index described itself as publishing "evidence-based analysis about AI's implications for cybersecurity, biosecurity, and autonomous systems" for policymakers, civil society and researchers. Earliest dated post found is June 2025 (the blog appears to have launched then); the team itself predates that: the nuclear-safeguards post says the DOE/NNSA partnership began April 2024, and TAI's announcement credits FRT with showing models "discover severe cybersecurity vulnerabilities."
- **Leadership/people.** **Logan Graham** is listed among contributors on the Mythos Preview cyber assessment (https://www.anthropic.com/research/mythos-preview); no page fetched states his title, so "leads FRT" is unverified here (Section 5). Recurring bylines: **Nicholas Carlini, Newton Cheng, Keane Lucas, Winnie Xiao, Milad Nasr, Evyatar Ben Asher, Kyla Guru, David Forsythe, Daniel Freeman, Michael Ilie, Kevin Troy, Carolyn Zou, Alex Moix, Jacob Klein**.

### What the team does, methods, infrastructure
- **Capability evaluations that back RSP/ASL decisions.** Cyber: Cybench, CyberGym, CTF competitions, Pattern Labs network ranges; bespoke benchmarks ExploitBench (41 V8 CVEs, 5-tier ladder), ExploitGym (898 patched vulns, 2-hour limit), SCONE-bench (smart contracts), Drone-Bench, CryptanalysisBench (with ETH Zurich, Tel Aviv, TU Berlin). Bio: SecureBio's VCT, expert-graded bioweapons-acquisition uplift trials, an n=8 wet-lab pilot; ASL-3 applied to the Opus 4 family. Nuclear: a DOE/NNSA classifier at "96% accuracy in preliminary testing."
- **Threat intelligence and misuse mapping** (with Safeguards/Threat Intelligence): banned-account analysis mapped to MITRE ATT&CK, the "AI Risk Enablement Score (ARiES)," and disclosure of state-sponsored operations.
- **Real-world "projects"** that test autonomy outside the lab: Project Vend (Claude runs a shop), Project Fetch (robot dog), Project Pilot (drone), multiagent swarms.
- **Defensive deployment**: Project Glasswing (Mythos Preview given to partners to fix critical software) and a public Coordinated Vulnerability Disclosure dashboard (https://red.anthropic.com/2026/cvd/; as of 26 Aug 2026: 2,300 vulnerabilities disclosed across 392 projects, 421 patched, 177 CVEs, 91.4% true-positive rate on 5,008 externally reviewed findings).

### Chronological publications (verified)
| Date | Title / URL | One-line finding |
|---|---|---|
| 13 Jun 2025 | LLMs with cyber toolkits can conduct multistage cyber operations, https://www.anthropic.com/research/cyber-toolkits | With CMU's "Incalmo" toolkit LLMs fully compromised 5/10 and partially 4/10 business-sized networks; none succeeded without it. |
| 27 Jun 2025 | Project Vend, https://www.anthropic.com/research/project-vend-1 | Claude Sonnet 3.7 ran an office shop with Andon Labs for a month at a loss (underpricing, hallucinated payment details, an identity-confusion episode). |
| 15 Jul 2025 | Detailed cyber evaluations of Claude 4, https://www.anthropic.com/research/claude-4-cyber | With Pattern Labs: Opus 4 adapts rather than repeating failed tactics; still struggles with long-horizon plans. |
| 9 Aug 2025 | Claude is competitive with humans in (some) cyber competitions, https://www.anthropic.com/research/cyber-competitions | 7 competitions; top 3% at PicoCTF (297/10,460), but zero solves at PlaidCTF and DEF CON quals. |
| 21 Aug 2025 | Developing nuclear safeguards for AI, https://www.anthropic.com/news/developing-nuclear-safeguards-for-ai-through-public-private-partnership | DOE/NNSA co-developed classifier, 96% preliminary accuracy, shared with Frontier Model Forum. |
| 27 Aug 2025 | Detecting and countering misuse (Aug 2025 threat report), https://www.anthropic.com/news/detecting-countering-misuse-aug-2025 | "Vibe hacking" extortion of 17+ orgs, North Korean IT-worker fraud, ransomware-as-a-service sold at $400-1,200. |
| 5 Sep 2025 | Why do we take LLMs seriously as a potential source of biorisk?, https://www.anthropic.com/research/biorisk | Claude went from below to "comfortably exceeding" expert baseline on VCT in a year; Opus 4 uplift-trial groups scored higher with fewer critical failures; n=8 wet-lab pilot showed no uplift. |
| 3 Oct 2025 | Building AI for cyber defenders, https://www.anthropic.com/research/building-ai-cyber-defenders | Sonnet 4.5: 76.5% on Cybench (10 attempts), 28.9% CyberGym; HackerOne cut intake time 44%. |
| 12 Nov 2025 | Project Fetch, https://www.anthropic.com/research/project-fetch-robot-dog | RCT with 8 non-roboticists: Team Claude finished in about half the time, 7/8 vs 6/8 tasks, less negative affect (d=2.16). |
| 13 Nov 2025 | Disrupting the first reported AI-orchestrated cyber espionage campaign, https://www.anthropic.com/news/disrupting-AI-espionage | Chinese state-sponsored group used Claude Code for "80-90% of the campaign" against ~30 targets, humans at 4-6 decision points. |
| 1 Dec 2025 | AI agents find $4.6M in blockchain smart contract exploits, https://www.anthropic.com/research/smart-contracts | With MATS/Anthropic Fellows/SEAL: 51.1% turnkey success on 405 contracts; exploit revenue doubling every 1.3 months; $1.22 per run. |
| 18 Dec 2025 | Project Vend: Phase two, https://www.anthropic.com/research/project-vend-2 | Claudius reached consistent profitability across SF/NY/London on Sonnet 4/4.5, still manipulable; helpfulness training drives over-discounting. |
| 5 Feb 2026 | Evaluating and mitigating the growing risk of LLM-discovered 0-days, https://www.anthropic.com/research/zero-days | Opus 4.6 found 500+ validated high-severity vulns in fuzzed open-source code; new cyber probes and enforcement. |
| 6 Mar 2026 | Partnering with Mozilla to improve Firefox's security, https://www.anthropic.com/news/mozilla-firefox-security | 22 Firefox vulns in two weeks, 14 high-severity (about 20% of 2025's total); fixes shipped in Firefox 148. |
| 6 Mar 2026 | Reverse engineering Claude's CVE-2026-2796 exploit, https://www.anthropic.com/research/exploit | First LLM-written functional browser exploit (Wasm JIT type confusion), ~2 successes in 350 attempts, only Opus 4.6. |
| 7 Apr 2026 | Assessing Claude Mythos Preview's cybersecurity capabilities, https://www.anthropic.com/research/mythos-preview | Project Glasswing launched; Mythos Preview found bugs in every major OS/browser (27-year-old OpenBSD bug), 181 working Firefox JS exploits vs 2 for Opus 4.6. Carlini/Cheng/Lucas lead; Logan Graham contributor. |
| 22 May 2026 | Measuring LLMs' ability to develop exploits, https://www.anthropic.com/research/exploit-evals | Mythos Preview: ACE on 21/41 ExploitBench CVEs (no other model got 1); 157 vs 15 on ExploitGym; $35M SCONE-bench. |
| May 2026 | Coordinated Vulnerability Disclosure dashboard, https://red.anthropic.com/2026/cvd/ | Live ledger with cryptographic commitments; 2,300 disclosed / 421 patched by 26 Aug 2026. |
| 3 Jun 2026 | Mapping AI-enabled cyber threats: LLM ATT&CK Navigator, https://www.anthropic.com/research/attack-navigator (companion: https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack) | 832 banned accounts, 13,873 actions, 482 techniques; medium-high-risk actors rose 33% to 56%; ARiES score; in Verizon 2026 DBIR. |
| 8 Jun 2026 | Measuring LLMs' impact on N-day exploits, https://www.anthropic.com/research/n-days | Mythos Preview built 8 Firefox exploits and 8 Windows kernel chains; first PoC in 31 minutes; "patch gap" collapses to hours. |
| 18 Jun 2026 | Project Fetch: Phase two, https://www.anthropic.com/research/project-fetch-phase-two | Opus 4.7 alone was ~37x faster than the unaided human team, 1,045 vs 10,309 lines of code. |
| 9 Jul 2026 | Claude plays robotics, https://www.anthropic.com/research/claude-plays-robotics | Score depends "as much on the robot body and the control interface as on the model"; spatial memory is the bottleneck. |
| 24 Jul 2026 | Project Pilot: Can AI control a drone?, https://www.anthropic.com/research/project-pilot | Drone-Bench, 15 models; Fable 5 beats baseline on 4/5 subtasks; 3D reconstruction at 47% of baseline. |
| 28 Jul 2026 | Discovering cryptographic weaknesses with Claude, https://www.anthropic.com/research/discovering-cryptographic-weaknesses | HAWK-256 cost cut 2^64 to 2^38 (~$100k API); 200-800x faster 7-round AES fingerprinting; no production impact. |
| 13 Aug 2026 | Patterns and problems in emerging multiagent systems, https://www.anthropic.com/research/multiagent-systems | Swarms find 266 vs 21 vulns but conformity (18/30 agents same branch name), 2.4M-request floods, "turf wars"; Mythos 5 truces in 98% of runs. |

### Themes, vocabulary, methodological signatures
- "Stress-test," "outermost limits," "situational awareness," "watershed," "patch gap," "dual-use," "uplift," "ASL-3," "coordinated disclosure," "defender's advantage."
- Signature move: pair a capability number with a cost number (hours, dollars, tokens) and a model-generation comparison (Opus 4.6 vs Mythos Preview), then say what defenders should do now.
- Partnerships are the norm: Pattern Labs, CMU CyLab, Andon Labs, Mozilla, Verizon, MITRE, DOE/NNSA, SecureBio, Frontier Model Forum, MATS.
- Honest negative results (n=8 wet lab, PlaidCTF zero, 2/350 exploit attempts) are always reported.

### TAI pillars driven
Primarily **Threats and resilience** (cyber, bio, nuclear, misuse); increasingly **AI research and development** (multiagent systems, autonomy in Fetch/Pilot); Project Vend feeds **AI, jobs, and the economy**.

### Applicant hooks
1. Economics of the "patch gap": model the welfare effects when N-day weaponization falls from expert-weeks to 31 minutes; who bears the cost of accelerated patching?
2. Cost-of-attack curves: extend the SCONE-bench "1.3-month doubling" and $1.22/run figures into a market-structure analysis for cybercrime.
3. Project Vend as a natural experiment in AI firm behavior (helpfulness-induced underpricing, principal-agent failures).
4. Multiagent conformity and "turf wars" as a coordination-failure problem: propose reputation/costly-signaling mechanisms from economics.
5. Policy design for Glasswing-style staged access to dual-use capability.

---

## 2. Societal Impacts

### Mission and history
- Team page: https://www.anthropic.com/research/team/societal-impacts. Mission verbatim: "Working closely with the Anthropic Policy and Safeguards teams, Societal Impacts is a technical research team that explores how AI is used in the real world." It describes "sociotechnical alignment" (which values models should hold, how they act under conflicting values) and prioritizes "research questions that have policy relevance."
- Earliest verified work: Collective Constitutional AI (17 Oct 2023) and discrimination evaluation (7 Dec 2023), so the team was active by late 2023. TAI's announcement says it "studies how AI is being used in the real world."
- **People (verified as authors).** **Deep Ganguli** is the recurring senior/last author (Clio, persuasiveness, affective use, work-at-Anthropic, agent autonomy, personal guidance) and co-led Collective CAI; no page states his title (Section 5). **Alex Tamkin** (first author of the Clio paper; co-lead of the Sept 2025 Index report), **Esin Durmus** (lead, persuasiveness), **Miles McCain** (lead, affective use and agent autonomy), **Saffron Huang** (lead, 81k interviews and work-at-Anthropic), **Kunal Handa** (lead, Anthropic Interviewer, Education Report, Insights pilot), **Judy Hanwen Shen** (agent autonomy; personal guidance), plus Michael Stern, Matt Kearney, Miranda Zhang, Shan Carter, Gabriel Nicholas, Stuart Ritchie, Liane Lovitt, Jake Eaton, Sarah Pollack; Jack Clark and Jared Kaplan on the Clio paper.

### What the team does, methods, infrastructure
- **Clio** (https://www.anthropic.com/research/clio; paper https://arxiv.org/abs/2412.13678): privacy-preserving pipeline in which Claude extracts facets, clusters, summarizes with private details removed, and builds hierarchies; humans only see aggregates above minimum thresholds. Described as "Google Trends for AI conversations." It underpins the Economic Index, Values in the Wild, affective-use, and education reports.
- **Anthropic Interviewer** (Dec 2025): Claude-run adaptive qualitative interviews at scale (plan, interview, analyze); used for the 81k study and the Economic Index Survey.
- **Anthropic Insights** (Aug 2026): a successor privacy-preserving analysis tool opened to external researchers (Stanford SALT, Oxford, METR) with contractual independence and an Imperial College privacy audit.
- **Classifier-on-usage studies**: LLM-rated scales (autonomy/risk 1-10; sycophancy across nine guidance domains; values taxonomy of 3,307 values reduced to four axes).
- **Controlled experiments and surveys**: persuasiveness RCT with 3,832 participants; discrimination testing across 70 decision scenarios; 132-person survey plus 53 interviews plus 200k Claude Code transcripts internally.

### Chronological publications (verified)
| Date | Title / URL | One-line finding |
|---|---|---|
| 17 Oct 2023 | Collective Constitutional AI, https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input | ~1,000 Americans on Polis (38,252 votes); public constitution ~50% overlap with Anthropic's, lower bias on all nine dimensions. Ganguli, Huang, Lovitt, Siddarth (CIP). |
| 7 Dec 2023 | Evaluating and mitigating discrimination in LM decisions, https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions | 70 scenarios; Claude 2.0 shows positive and negative discrimination, mitigable by prompting. Paper arXiv 2312.03689. |
| 16 Feb 2024 | Preparing for global elections in 2024, https://www.anthropic.com/news/preparing-for-global-elections-in-2024 | Policy Vulnerability Testing since 2023, TurboVote redirects; team not named on page. |
| 9 Apr 2024 | Measuring the persuasiveness of language models, https://www.anthropic.com/research/measuring-model-persuasiveness | Claude 3 Opus statistically indistinguishable from humans; each generation more persuasive; deceptive prompting most effective. Durmus lead. |
| 12 Dec 2024 | Clio, https://www.anthropic.com/research/clio | Web/mobile dev >10% of conversations; Clio also caught coordinated abuse. |
| 10 Feb 2025 | Which economic tasks are performed with AI (Economic Index launch), https://www.anthropic.com/news/the-anthropic-economic-index | 1M conversations mapped to O*NET: 57% augmentation/43% automation; 36% of occupations use AI for 25%+ of tasks. |
| 8 Apr 2025 | Education Report: how university students use Claude, https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude | 574,740 conversations; CS is 38.6% of use vs 5.4% of degrees; ~47% "Direct" answer-seeking. Handa and Bent lead. |
| 21 Apr 2025 | Values in the wild, https://www.anthropic.com/research/values-wild | 308,210 value-laden conversations; five top-level value categories; strong support 28.2%, resistance 3.0%. |
| 28 Apr 2025 | Economic Index: AI's impact on software development, https://www.anthropic.com/research/impact-software-development | Claude Code 79% automation vs 49% on Claude.ai; startups 32.9% of Claude Code use. |
| 27 Jun 2025 | How people use Claude for support, advice, and companionship, https://www.anthropic.com/news/how-people-use-claude-for-support-advice-and-companionship | Affective use 2.9% of conversations; companionship/roleplay <0.5%; sentiment turns slightly more positive. McCain lead; Sarah Heck co-author. |
| 27 Aug 2025 | Education Report: how educators use Claude, https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude | 74k conversations; 57% curriculum development; grading 48.9% automation-heavy; 5.9 hours/week saved. |
| 2 Dec 2025 | How AI is transforming work at Anthropic, https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic | Claude used in 59% of work (from 28%), ~50% productivity gain, 27% of work would not otherwise be done; ~21 consecutive actions before human input. Huang lead. |
| 4 Dec 2025 | Introducing Anthropic Interviewer, https://www.anthropic.com/research/anthropic-interviewer | 1,250 interviews; 86% of workforce say AI saves time; 79% of scientists cite trust as the barrier. Handa lead. |
| 18 Feb 2026 | Measuring AI agent autonomy in practice, https://www.anthropic.com/research/measuring-agent-autonomy | 998,481 tool calls; 99.9th-pct turn nearly doubled to 45+ minutes; only 0.8% irreversible actions; Claude asks for clarification more than humans interrupt. McCain lead, 20 co-authors incl. Ganguli, Clark, Shen. |
| 18 Mar 2026 | What 81,000 people want from AI, https://www.anthropic.com/81k-interviews | 80,508 users, 159 countries, 70 languages; top hope "professional excellence" (18.8%); top fear unreliability (26.7%), job loss (22.3%). Huang lead. |
| 30 Apr 2026 | How people ask Claude for personal guidance, https://www.anthropic.com/research/claude-personal-guidance | ~6% of conversations; sycophancy 9% overall, 38% in spirituality; Opus 4.7/Mythos halve relationship sycophancy. Shen, Carter, Ganguli among 28 authors. |
| 13 Jul 2026 | Claude's values across models and languages, https://www.anthropic.com/research/claude-values-models-languages | 309,815 conversations, 3,307 values to four axes (Deference-Caution, Warmth-Rigor, Depth-Brevity, Candor-Execution); most warmth in Hindi, most caution in English. Kearney, Zhang, Carter. |
| 26 Aug 2026 | Enabling independent research on how people use Claude, https://www.anthropic.com/research/enabling-independent-research | Anthropic Insights pilot with Stanford SALT, Oxford, METR on ~250k conversations; <5% content filtered; Imperial privacy audit; datasets released. Handa, Zhang, Nicholas. |

Not found: the "How AI impacts skill formation" (Shen and Tamkin) post, which the brief mentions; four candidate URLs returned 404 (Section 5).

### Themes, vocabulary, methodological signatures
- "Privacy-preserving analysis," "in the wild," "sociotechnical alignment," "augmentation vs automation," "directive vs collaborative," "affective use," "sycophancy," "values taxonomy," "autonomy and risk scores," "epistemic autonomy," "deskilling."
- Signature: bottom-up taxonomies from real usage plus a top-down mapping (O*NET, Bloom's taxonomy, values categories), validated against human raters, with explicit limitations ("cannot establish causation," "no longitudinal data").
- A strong turn in 2026 toward openness: external-researcher access (Insights), published aggregate datasets, third-party privacy audits.
- The team co-publishes with Economics (Tamkin and McCain are on Index reports; Huang co-wrote the 81k economics paper).

### TAI pillars driven
Primarily **AI systems behavior in the wild** (values, sycophancy, agent autonomy); significant share of **AI, jobs, and the economy** (Education reports, work-at-Anthropic, 81k interviews); feeds **Threats and resilience** through misuse detection in Clio and elections work.

### Applicant hooks
1. Propose an Insights-based study in the Aug 2026 expression-of-interest channel (e.g., cross-country differences in "Direct" answer-seeking and learning outcomes).
2. Link the four value axes to labour-market outcomes: does "Deference" vary with occupational exposure?
3. Build on the agent-autonomy metrics (turn duration, auto-approve rate, irreversibility share) as inputs to a liability or insurance framework.
4. Extend the 81k "cognitive atrophy" concern (16.3%) into a measurable deskilling design, bridging to the Economics "skills" primitive.
5. Design a persuasion or sycophancy welfare experiment for a policy audience.

---

## 3. Economic Research (the Economic Index team)

### Mission and history
- Team page: https://www.anthropic.com/research/team/economics. Mission verbatim: "The Economics team studies how AI is reshaping the economy, including work, productivity, and economic opportunity." The page describes the Anthropic Economic Index as the flagship, a longitudinal record of "actual AI tool usage globally."
- History: the Index launched 10 Feb 2025 (https://www.anthropic.com/news/the-anthropic-economic-index), initially produced with Societal Impacts on Clio. The Economic Advisory Council was announced 28 Apr 2025; the Economic Futures Program 27 Jun 2025; the Economic Index Survey 22 Apr 2026. By Jan 2026 reports carry Economics-team lead authors (Appel, Massenkoff, McCrory).
- **People (verified as authors).** **Maxim Massenkoff** (lead, Learning curves, Labor market impacts, Cadences, retraining review, 81k economics), **Peter McCrory** (lead on Sept 2025, Jan 2026 reports, Labor market impacts, Australia and Canada reports), **Ruth Appel** (co-lead Sept 2025 and Jan 2026), **Eva Lyubich** (Learning curves, Cadences, expertise paper), **Zoe Hitzig** (lead on "Agentic coding and persistent returns to expertise"; Cadences), **Szymon Sacher, Shaoyi Zhang, Ryan Heller** (Cadences), **Anton Korinek** (named in the TAI announcement as joining Economic Research; previously an Advisory Council member; no Anthropic-bylined paper by him was found, Section 5). External co-authors: David Roodman, Thomas Lyttelton, Nathan Wilmers (MIT).
- **Economic Advisory Council** (https://www.anthropic.com/news/introducing-the-anthropic-economic-advisory-council, 28 Apr 2025, updated 9 May): Tyler Cowen, Oeindrila Dube, John Horton, Anton Korinek, John List, Ioana Marinescu, Tomas Philipson, Silvana Tenreyro, Chiara Farronato, Pascual Restrepo.

### What the team does, methods, infrastructure
- **Index pipeline**: ~1M Claude.ai conversations plus ~1M first-party API records per wave, privacy-preserving classifiers (Clio lineage) mapping to O*NET tasks/occupations and to bottom-up clusters; the **Anthropic AI Usage Index** (per-capita use vs population share); five **economic primitives** since Jan 2026 (task complexity, skills/education years, use case, AI autonomy, task success); artifact classification and hourly sampling since Jun 2026.
- **Observed exposure** (Mar 2026): fuses Eloundou et al. theoretical exposure with observed Claude usage, then links to BLS/CPS outcomes.
- **Survey linked to usage**: the monthly Economic Index Survey (random Claude users, accounts 2+ weeks old, run via Anthropic Interviewer, linked to usage "in a privacy-preserving way"); ~9,700 linked respondents in the June 2026 report.
- **Open data**: Hugging Face `Anthropic/EconomicIndex` (https://huggingface.co/datasets/Anthropic/EconomicIndex), CC-BY data/MIT code, releases 2025-02-10, 2025-03-27, 2025-09-15, 2026-01-15, 2026-03-24, 2026-06-26; a claude.ai **Economic Index connector** (22 Jul 2026, https://www.anthropic.com/news/anthropic-economic-index-connector).
- **Economic Futures Program** (https://www.anthropic.com/economic-futures; program page https://www.anthropic.com/economic-futures/program): grants of $10k-50k plus $5k API credits, DC (Georgetown McCourt) and London (LSE) symposia with 24 policy proposals (https://www.anthropic.com/economic-futures/symposium-proposals), a UK/Europe expansion (5 Nov 2025), and on 22 Jul 2026 a **$200M Economic Futures Research Fund** with $5-30M grants (https://www.anthropic.com/news/economic-futures-research-fund-agenda) on five themes: firm-level worker impact, navigating transitions, modernizing income support, worker stakes in AI growth, and evidence on public investments. Contact: economicfutures@anthropic.com.

### Chronological publications (verified)
| Date | Title / URL | One-line finding |
|---|---|---|
| 10 Feb 2025 | Anthropic Economic Index (first report), https://www.anthropic.com/news/the-anthropic-economic-index | Computer/math 37.2% of use; 57% augmentation; heaviest use in mid-to-high wage occupations. |
| 27 Mar 2025 | Insights from Claude 3.7 Sonnet, https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7 | Augmentation still 57%; learning interactions up ~23% to ~28%; 630-cluster bottom-up taxonomy released. |
| 28 Apr 2025 | AI's impact on software development, https://www.anthropic.com/research/impact-software-development | Claude Code 79% automation; JS/TS 31% of queries. |
| 28 Apr 2025 | Economic Advisory Council, https://www.anthropic.com/news/introducing-the-anthropic-economic-advisory-council | Ten academic economists advise the Index agenda. |
| 27 Jun 2025 | Economic Futures Program launch, https://www.anthropic.com/news/introducing-the-anthropic-economic-futures-program | "We believe it's fundamental to ground these conversations in real-world data." |
| 15 Sep 2025 | Economic Index September 2025 report, https://www.anthropic.com/research/anthropic-economic-index-september-2025-report | Directive use 27% to 39%; API 77% automation; AI Usage Index: Israel 7.0x, US 3.62x, India 0.27x; usage price elasticity -0.29. Appel, McCrory, Tamkin. |
| 14 Oct 2025 | Symposium proposals, https://www.anthropic.com/economic-futures/symposium-proposals | 24 proposals from MIT, Yale, CMU, IMF, RAND, J-PAL and others. |
| 15 Jan 2026 | Economic primitives, https://www.anthropic.com/research/anthropic-economic-index-january-2026-report | Five primitives; 9-12x speedups; reliability-adjusted productivity growth 1.0-1.2pp/yr; US state Gini fell 0.37 to 0.32; deskilling as higher-skill task components are automated. Appel, Massenkoff, McCrory. |
| 5 Mar 2026 | Labor market impacts of AI: a new measure and early evidence, https://www.anthropic.com/research/labor-market-impacts | "Observed exposure"; programmers 75% coverage; no unemployment rise for exposed workers since 2022 but 14% lower job-finding for exposed 22-25-year-olds. Massenkoff and McCrory. |
| 24 Mar 2026 | Learning curves, https://www.anthropic.com/research/economic-index-march-2026-report | Top-10 tasks 24% to 19%; 6+-month users 10% higher success; top-5 US states' share 30% to 24%. Massenkoff, Lyubich, McCrory. |
| 31 Mar 2026 | How Australia uses Claude, https://www.anthropic.com/research/how-australia-uses-claude | 4.1x per-capita; 46% work / 47% personal / 7% coursework; autonomy 3.38/5. McCrory. |
| 22 Apr 2026 | What 81,000 people told us about the economics of AI, https://www.anthropic.com/research/81k-economics | One-fifth worried about displacement; +10pp exposure = +1.3pp perceived threat; scope expansion (48%) beats speed (40%). Massenkoff and Huang. |
| 22 Apr 2026 | Announcing the Economic Index Survey, https://www.anthropic.com/research/economic-index-survey-announcement | Monthly random-user survey via Anthropic Interviewer, linked to usage. |
| 27 May 2026 | Coding agents in the social sciences, https://www.anthropic.com/research/coding-agents-social-sciences | 1,260 social scientists: 20% use coding agents; users post 50% more working papers; 2x gender gap by name-coding. Lyttelton, Massenkoff, Wilmers. |
| 16 Jun 2026 | Agentic coding and persistent returns to expertise, https://www.anthropic.com/research/claude-code-expertise | 400k Claude Code sessions: novices 15% verified success vs 28-33% for experts; users make ~70% of planning decisions, Claude ~80% of execution. Hitzig lead. |
| 26 Jun 2026 | Cadences, https://www.anthropic.com/research/economic-index-june-2026-report | Hourly/weekly rhythms (personal use 35% weekday to 50% weekend; tax clusters 8x on 14 April); 93% of conversations yield artifacts; ~9,700 linked survey respondents, >1/3 expect AI to do most work tasks within 12 months, 10% see job loss as likely. |
| 14 Jul 2026 | How Canada uses Claude, https://www.anthropic.com/research/how-canada-uses-claude | 4.4x per-capita, Ontario 43.9%; document translation the distinctive use. McCrory. |
| 22 Jul 2026 | Economic Futures Research Fund agenda ($200M), https://www.anthropic.com/news/economic-futures-research-fund-agenda | $5-30M grants to institutions for field experiments on transitions and income support. |
| 12 Aug 2026 | Reviewing the evidence on worker retraining programs, https://www.anthropic.com/research/reviewing-the-evidence-on-worker-retraining-programs | 56 US RCTs: +2-3pp employment, ~$1,000/yr earnings for ~$13,000 cost; sector programs better but hard to replicate; insufficient for large AI displacement. Roodman and Massenkoff. |

### Themes, vocabulary, methodological signatures
- "Augmentation vs automation," "directive / feedback loop / task iteration / learning," "AI Usage Index," "economic primitives," "observed exposure," "learning curves," "cadences," "artifacts," "task complexity," "years of education," "task success," "deskilling," "diffusion," "convergence" (Gini across states), "scope vs speed," "persistent returns to expertise."
- Signature: usage microdata mapped to O*NET, weighted to the economy, then confronted with official statistics (BLS projections, CPS, GDP per capita) and external benchmarks (METR task horizons, Eloundou et al.); regression with task fixed effects; explicit reliability adjustment of productivity claims; every wave ships open data and code.
- Voice: measured, forecast-averse, "early evidence," candid about selection (Claude users are not the labour force; women 12% of the linked survey sample).
- Policy arm: Advisory Council, symposia, Economic Policy Framework PDF (linked from https://www.anthropic.com/policy), the Fund's five themes, the retraining evidence review, and Claude Corps.

### TAI pillars driven
Overwhelmingly **AI, jobs, and the economy** (what the brief calls economic diffusion); contributes to **AI systems behavior in the wild** through the autonomy primitive and Claude Code session studies; Hitzig's remit ("connecting economics to model training") reaches into **AI research and development**.

### Applicant hooks
1. Use the Hugging Face releases to test a diffusion hypothesis (e.g., does state-level convergence track broadband, industry mix, or wages?) and replicate the 0.36% elasticity to computer/math employment.
2. Extend "observed exposure" to a non-US labour market (UK, Australia, Canada reports give the usage side) and to hiring flows for early-career workers.
3. Propose a Survey module: link monthly perceived-threat readings to subsequent usage changes, exploiting the rotating random sample.
4. Bridge to the $200M Fund: design a field experiment on income support or sector-based retraining that fixes the replication problem Roodman and Massenkoff identify.
5. Take the Jan 2026 deskilling finding (Claude covers tasks at 14.4 years of education vs 13.2 economy-wide) and model wage effects by education band.

---

## 4. Adjacent teams and programs to recognise

- **Alignment Science**: https://www.anthropic.com/research/team/alignment; latest "Automated researchers can reliably mitigate alignment failures" (28 Aug 2026); blog https://alignment.anthropic.com (also hosts the AI-safety Fellows Program posts).
- **Interpretability**: https://www.anthropic.com/research/team/interpretability; mission "to discover and understand how large language models work internally"; latest "A global workspace in language models" (6 Jul 2026).
- **Safeguards** (incl. Threat Intelligence): https://www.anthropic.com/news/building-safeguards-for-claude (12 Aug 2025); policy, enforcement, threat intel and engineering; co-authors FRT's misuse reports.
- **Public Policy under Sarah Heck**: named Head of Public Policy in the TAI announcement; policy hub https://www.anthropic.com/policy (priorities include economic futures; Economic Policy Framework and Advanced AI Framework PDFs).
- **Long-Term Benefit Trust**: https://www.anthropic.com/news/the-long-term-benefit-trust (19 Sep 2023); five independent trustees who elect a board majority over time.
- **Anthropic Economic Futures**: https://www.anthropic.com/economic-futures; grants, symposia, Index scaling, $200M Research Fund (Jul 2026).
- **Claude Corps**: https://www.anthropic.com/news/claude-corps (11 Jun 2026); $150M, 1,000 one-year nonprofit fellows at $85k, cohorts from Oct 2026.
- **AI for Science program**: https://www.anthropic.com/news/ai-for-science-program (5 May 2025); API credits for life-science research; Science team posts at https://www.anthropic.com/research (e.g., Riemann-zeta bounds, protein design, Aug 2026).
- **National security work**: Claude Gov models https://www.anthropic.com/news/claude-gov-models-for-u-s-national-security-customers (6 Jun 2025); DOE/NNSA nuclear classifier (Aug 2025); FRT's espionage disclosure (Nov 2025).
- **Anthropic Fellows Program (AI safety track)**: referenced on https://alignment.anthropic.com (Dec 2024 pilot; Nov 2025 call for 2026); the smart-contracts paper credits "Anthropic Fellows program" collaborators.

## 5. Could not verify (flagged)

1. **Fellows Program (Economics & Policy) hosted by TAI**: no page found at /institute/fellows, /institute/fellows-program, /fellows, /news/anthropic-fellows-program, or /news/anthropic-fellows-program-economics-and-policy (all 404). The TAI announcement mentions hiring "a small analytical staff" but no fellowship. Treat program structure, stipend and dates as unverified; use the applicant's own call text.
2. **Logan Graham as FRT lead**: verified only as a listed contributor on the Mythos Preview assessment; no fetched page gives his title.
3. **Deep Ganguli as Societal Impacts lead**: verified as senior author across the team's papers and co-lead of Collective CAI; title not stated on any fetched page.
4. **"How AI impacts skill formation" (Shen and Tamkin)**: four candidate URLs returned 404; not listed on the visible team page. Exists in the brief only.
5. **"Strategic warning" posts**: /research/strategic-warning 404; not in the archived red.anthropic.com 2025 or 2026 index. May be a phrase from talks or system cards rather than a post.
6. **Bio-uplift "trial results" as a standalone FRT post**: the only verified source is the 5 Sep 2025 biorisk essay summarising trials; full trial write-ups likely sit in model system cards, not fetched.
7. **Anton Korinek and Zoë Hitzig "at TAI"**: both named in the 11 Mar 2026 announcement; Hitzig's authorship is verified (Cadences, expertise paper); no Anthropic-bylined Korinek paper found.
8. **Pillar wording**: the live /institute page uses "AI, jobs, and the economy," "Threats and resilience," "AI systems behavior in the wild," "AI research and development," not "Economic diffusion" or "AI-driven R&D."
9. **Economic Index landing page** (https://www.anthropic.com/economic-index) loads dynamically ("Loading data," last updated 26 Jun 2026); report lists were taken from the Economics team page and individual report pages instead.
10. **Team page listings are truncated** at ten items with a "See more" control that is not URL-addressable; older items were reached via direct URLs and redirects, so a few minor posts may be missing.
11. **Elections work**: the Feb 2024 post carries no team attribution.
12. WebSearch was unavailable this session (budget exhausted); all verification used direct fetches (about 100 URLs).
