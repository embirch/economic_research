# Anthropic Economic Index — Publications & Reports Log

Compiled 2026-09-07 for Emily Birch (Anthropic Fellows, Economics & Policy). Purpose: a faithful, number-exhaustive record of each Economic Index publication so that extensions can be designed as falsifiable tests. Numbers are quoted or closely paraphrased from the source; where the source text gave a qualifier instead of a number ("slightly", "sharply"), the qualifier is recorded as such. Anything not retrievable is marked [NOT FETCHED].

Fetch method: WebFetch on the Anthropic page and (where one exists) the arXiv/PDF. Fetched text is summarised by a small model, so treat any single number as "verify against the PDF/HF dataset before publishing" (see memory: research-detail-rule).

---

## 1. The Anthropic Economic Index (first report) — Feb 2025

- **Title (post):** "The Anthropic Economic Index"
- **Title (paper):** "Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations"
- **Date:** post 10 Feb 2025; arXiv 2503.04761 submitted 11 Feb 2025 (v1)
- **URLs:** https://www.anthropic.com/news/the-anthropic-economic-index ; https://arxiv.org/abs/2503.04761
- **Authors (paper):** Kunal Handa, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah Heck, Jared Mueller, Jerry Hong, Stuart Ritchie, Tim Belonax, Kevin K. Troy, Dario Amodei, Jared Kaplan, Jack Clark, Deep Ganguli. Post has no byline.

### 1.1 Quantitative findings (post)
1. Share of conversations by O*NET occupational category: Computer & Mathematical 37.2%; Arts, Design, Sports, Entertainment & Media 10.3%; Education & Library 9.3%; Office & Administrative 7.9%; Life, Physical & Social Science 6.4%; Business & Financial 5.9%; Transportation 0.3%; Farming, Fishing & Forestry 0.1%.
2. Software development + writing tasks together = "nearly 50%" of usage (paper abstract).
3. Depth of use: ~4% of occupations use AI for 75%+ of their tasks; ~36% of occupations use AI for at least 25% of their tasks.
4. Augmentation 57% (57.4%) vs automation 43% (42.6%) of conversations.
   - Augmentation sub-modes: Task Iteration 31.3%; Learning 23.3%; Validation 2.8%.
   - Automation sub-modes: Directive 27.8%; Feedback Loop 14.8%.
5. Wage gradient: usage peaks in mid-to-high wage occupations (e.g. computer programmers, copywriters); both very-low-wage and very-high-wage occupations show low use. US median wage reference: $60,070.
   - Illustrative: Computer Programmers (median salary ~$75k–$100k) ≈ 3–6% of conversations; Shampooers (~$25k) <1%; Obstetricians (~$200k) low.
6. Sample: "approximately one million conversations" (post) / "over four million Claude.ai conversations" (paper abstract — the 1M is the filtered occupational-task subset; verify in Appendix).
7. O*NET task universe: "around 20,000 specific work-related tasks".

### 1.2 Data
- Platform: Claude.ai **Free and Pro** only. Excludes API, Team, Enterprise.
- Window: not stated in post (paper: Dec 2024–Jan 2025 — VERIFY against PDF; see 1b).
- Filter: "used a language model to filter this data to only contain conversations relevant to an occupational task".
- Comparison baseline: "compared the rates in our data to the rates at which each occupation appeared in the labor market in general".

### 1.3 Methods named
- **Clio** ("Claude insights and observations"): "an automated analysis tool that allows us to analyze conversations with Claude while preserving user privacy".
- Pipeline: conversation → task classification via Clio → O*NET task match → occupation → 6 (post) / 22 (paper) occupational categories.
- Task-level rather than occupation-level framing: "sometimes it makes sense to focus on occupational tasks rather than occupations themselves".
- Augmentation vs automation taxonomy (5 modes): Validation, Task Iteration, Learning (augmentation); Feedback Loop, Directive (automation).
- Wage mapping: O*NET/BLS median US salary crossed with usage share.

### 1.4 Limitations / caveats (verbatim where possible)
- "We can't know for certain whether someone using Claude for a task was completing a task for work. Someone asking Claude for writing or editing advice could be doing so at work, but they could also be doing so for the novel they're writing as a hobby."
- "Relatedly, we don't know how the users were using the responses from Claude. Were they, for instance, copy-pasting code snippets? Were they fact-checking responses or accepting them uncritically? Some of what appears in our data to be automation could, in fact, be augmentation: for example, a user might ask Claude to write a full memo for them (which would appear as automation), but then edit it themselves afterwards (which would be augmentation)."
- "We also only analyze data from Claude.ai Free and Pro plans, rather than API, Team, or Enterprise users."
- "The sheer number of different tasks means it is possible that Clio classified some conversations incorrectly (please see the full paper, in particular Appendix B, for details on how we validated the analysis)."
- "Claude can't generate images (except indirectly via code), and so some creative uses won't be referenced in the data."
- "Given that Claude is advertised for use as a state-of-the-art coding model, we might expect coding to be overrepresented as a use case. For that reason, we don't argue that the uses in our dataset are a representative sample of AI use in general."
- Paper abstract: "While our data and methods face important limitations and only paint a picture of AI usage on a single platform, they provide an automated, granular approach for tracking AI's evolving role."
- Policy disclaimer: "Our research gives data on how AI is being used, but it doesn't provide policy prescriptions. Answers to questions about how to prepare for AI's impact on the labor market can't come directly from research in isolation; instead, they'll come from a combination of evidence, values, and experience from broad perspectives."

### 1.5 Future work / open questions
- "We'll repeat many of the analyses above over time to help track the societal and economic changes that are likely to occur. We'll regularly release the results and the associated datasets as part of the Anthropic Economic Index."
- "We'll be able to monitor changes in the depth of AI use within occupations. If it remains the case that AI is used only for certain tasks, and only a few jobs use AI for the vast majority of their tasks, the future might be one where most current jobs evolve rather than disappear. We can also monitor the ratio of automation to augmentation, providing signals of areas where automation is becoming more prevalent."
- Implicit open questions: does the wage-usage hump persist; does depth-of-use within occupations rise; does automation share rise as capability rises.

### 1.6 Terminology
"augmentation", "automation", "directive", "feedback loop", "task iteration", "learning", "validation", "occupational tasks", "O*NET", "Clio", "depth of AI use", "Anthropic Economic Index".

### 1b. arXiv paper detail (2503.04761, HTML version)
- **Data window:** two one-week windows — 16–23 Dec 2024 and 10–17 Jan 2025.
- **Sample:** 1 million Claude.ai Free + Pro conversations for main analyses; 500k for the skills analysis. Model mix in sample: 54% Claude 3.5 Sonnet, 46% Opus (Sonnet used more for coding; Opus more for creative/educational work).
- **Privacy threshold:** a task is reported only if it has ≥15 conversations across ≥5 unique accounts.
- **O*NET hierarchy built by Clio:** 3 levels — 12 top-level, 474 middle-level, 19,530 base-level task statements (~20,000 unique tasks).
- **Top-level shares:** IT/technology ~50%; creative/cultural ~20%; business/finance/customer service ~15%. Middle-level: software development/website maintenance ~14%; computer systems programming ~11%; system administration 4–6%. Base-level: "modifying software to correct errors" and debugging dominant.
- **Depth of use:** ~4% of occupations ≥75% of tasks; ~11% ≥50%; ~36% ≥25%.
- **Wages:** "Usage peaks in the upper quartile of wages"; low at both extremes (examples: anesthesiologists and waiters).
- **Job Zones (barrier to entry) — conversation share / labour-market baseline / representation ratio:** Zone 1 (minimal prep) 0.23% / 0.57% / 0.40; Zone 2 9.40% / 12.06% / 0.78; Zone 3 16.50% / 17.63% / 0.94; Zone 4 (bachelor's) 54.45% / 36.33% / 1.50; Zone 5 (advanced degree) 19.43% / 33.41% / 0.58.
- **Skills (O*NET skills most present in conversations):** Critical Thinking, Reading Comprehension, Programming, Writing highest; Installation, Equipment Maintenance, Repairing lowest.
- **Mode concentration:** Feedback Loop mostly coding/debugging; Task Iteration front-end dev and professional communication; Learning general education; Validation smallest, concentrated in translation.
- **Human validation (Appendix B):** 150 hand-labelled examples for the task hierarchy — top-level accuracy 95.3%, middle 91.3%, base 86%. Automation/augmentation classification: 90.7% agreement on 150 examples.
- **Non-work share:** "Non-work conversations only comprise 23% of the dataset, and usage relating to coursework comprises only 5–10% of conversations."
- **Robustness:** "qualitatively similar results when mapping a single conversation to multiple tasks".
- **Limitations (paper wording):** "quite likely that our sample differs in important ways from API data or data from other AI model providers"; using Claude to classify "may also introduce potential inconsistencies if the model's understanding of tasks differs from the intended reading"; "Our method does not account for the complexity of user queries—for example, providing instructions for a basic omelette does not indicate culinary expertise"; O*NET "cannot capture emerging tasks and occupations that AI systems such as Claude may create or transform"; "Our methods are not able to capture how users are using the outputs of Claude.ai conversations"; "Claude.ai only outputs text as opposed to other modalities"; "Occupational classification of a conversation does not necessarily mean the user was a professional in that field"; "Our findings should be interpreted as an imperfect snapshot of AI usage across the labor market"; "cannot definitively map these relationships" between usage and long-term labour-market consequences.
- **Future work listed:** dynamic tracking over time; task-level rather than job-level measurement; longitudinal linkage of usage to workplace outcomes; expansion beyond text modalities; cross-platform comparison with API/other providers; re-measurement as capabilities evolve.
- **Terminology:** "depth of use" (fraction of an occupation's tasks with observed usage), "representation ratio" (usage % ÷ baseline %), "task-level" vs "occupation-level", "Job Zone".

---

## 2. Anthropic Economic Index: Insights from Claude 3.7 Sonnet — Mar 2025

- **Date:** 27 Mar 2025. **URL (live):** https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7 (the URL given in the brief, .../insights-from-claude-3-7-sonnet, returns 404). **Authors:** no byline.

### 2.1 Quantitative findings
1. Sample: 1 million anonymised Claude.ai Free + Pro conversations over the **11 days following the Claude 3.7 Sonnet launch** (late Feb–early Mar 2025).
2. Occupational shift vs report 1: coding share rose; education, sciences and healthcare rose modestly. Computer & Mathematical had the largest absolute increase, **+3 percentage points** (the Sept 2025 report gives the Mar 2025 Computer & Math peak as 40%; Jan 2026 report likewise says "peak March 2025: 40%").
3. Augmentation overall **57%** (unchanged from Feb). **Learning** interactions rose from ~23% to ~28%.
4. Community & Social Service tasks ~75% augmentation; Production and Computer/Mathematical occupations ~50/50. "We don't see any occupational categories where automation dominates."
5. Extended thinking mode usage share by occupation (occupations with ≥0.5% representation only): computer & information research scientists ~10%; software developers ~8%; multimedia artists/animators ~7%; video game designers ~6%.
6. Mode by occupation: copywriters/editors highest task iteration (~58%); translators/interpreters among highest directive; librarians highest learning (~56%).
7. Depth of use: ~40% of occupations use AI in ≥20% of their tasks; "little change in the curves between our first and second reports".
8. Released a bottom-up taxonomy of Claude.ai usage with **630 granular clusters** in a 3-level hierarchy, each with description and automation/augmentation breakdown (example clusters: water management systems, physics simulations, font selection, job applications).
9. O*NET task universe referred to here as ~17,000 tasks (vs "~20,000" in report 1 — the count differs by vintage/level; note for verification).

### 2.2 Data & methods
- Claude.ai Free + Pro (incl. mobile app). Classification model switched from Claude 3.5 Sonnet to **Claude 3.7 Sonnet** "for improved classification accuracy".
- **Filtering change:** report 1 filtered "based on whether conversations are relevant to an occupational category"; this report instead filters "out conversations that flagged our safety classifiers", "preserving more data" so the bottom-up taxonomy could be released.
- Clio; O*NET mapping; five interaction modes (learning, task iteration, validation, directive, feedback loop).

### 2.3 Limitations / caveats
- "O*NET descriptions may not be optimally representative of what Claude is being used for—for example, while we see usage in the occupation 'fine artists...,' usage on Claude.ai probably tilts more towards digital art than sculpture."
- On extended thinking: "many important questions remain about this new model capability".
- Occupational reporting limited to occupations with ≥0.5% representation.
- On the rise in education/science: "could reflect either ongoing diffusion of AI throughout the economy, novel applications of coding to those domains, or unexpected capability improvements" — explicitly unresolved.
- Detailed analysis of the 630-cluster taxonomy "left to future work".

### 2.4 Future work
- "In the coming months, we aim to continue tracking these metrics and developing new metrics as capabilities improve." Data on Hugging Face (Anthropic/EconomicIndex); an open form for researchers to request analyses.

### 2.5 Terminology
"extended thinking", "bottom-up taxonomy", "granular clusters", "learning", "task iteration", "directive", "depth of use".

---

## 3. Anthropic Economic Index: AI's impact on software development (Claude Code) — Apr 2025

- **Date:** 28 Apr 2025. **URL:** https://www.anthropic.com/research/impact-software-development. **Authors:** no byline.

### 3.1 Quantitative findings
1. Automation vs augmentation: **Claude Code 79% automation / 21% augmentation**; **Claude.ai (coding conversations) 49% automation / 51% augmentation**.
2. Automation sub-modes — Claude Code: Feedback Loop 35.8%, Directive 43.8%. Claude.ai coding: Feedback Loop 21.3%, Directive 27.5%.
3. Within Claude.ai, software conversations vs non-software: Feedback Loop +18.3pp, Directive −11.2pp (software shows more feedback loops, fewer directive).
4. Programming languages (combined platforms): JavaScript/TypeScript 31%; HTML/CSS 28%; Python 14%; SQL 6%.
5. Top coding use cases: UI/UX component development 12%; web & mobile app development 8%; software architecture/code design and debugging/performance optimisation also high.
6. Project type: Claude Code — startup work 32.9%, enterprise 23.8%; Claude.ai — startup ~13%, enterprise 25.9%.
7. Unclassifiable conversations: Claude.ai 5%; Claude Code 2%.
8. Sample: 500,000 coding-related interactions, split between Claude Code and Claude.ai.

### 3.2 Data
- Window: 6–13 April 2025. Platforms: Claude.ai (Free + Pro, filtered to coding) and Claude Code. Excludes Team, Enterprise, API.
- "We analyzed the 500,000 total Claude interactions (split between Claude Code and Claude.ai) using our privacy-preserving analysis tool" (Clio). Analyses "equally weighted Claude Code and Claude.ai interactions where applicable".

### 3.3 Methods
- Clio; the five-mode automation/augmentation taxonomy (Directive, Feedback Loop, Task Iteration, Learning, Validation); bottom-up clustering for languages, use cases, project types; inference of user type (startup/enterprise/personal) from context.

### 3.4 Limitations (verbatim excerpts)
- "We analyzed data from Claude.ai and Claude Code only. We excluded Team, Enterprise, and API usage that might show different patterns, particularly in professional settings."
- "The boundary between automation and augmentation becomes increasingly blurred with agentic tools like Claude Code."
- "Our categorization of who is using Claude for coding relied on inference from limited context."
- "Our dataset likely captures early adopters. These users might not represent the broader developer population."
- "Due to privacy considerations, we only analyzed data within a specific retention window, potentially missing cyclical patterns in software development."
- "The representativeness of Claude usage is unclear, relative to overall AI coding assistance adoption."
- "We only studied what developers delegate to AI—not how they ultimately use AI outputs in their codebase, the quality of the resulting code, or whether these interactions effectively improved productivity or code quality."

### 3.5 Open questions (verbatim)
- "Will the prevalence of 'feedback loops,' where humans are still involved in the process, persist as AI capabilities advance?"
- "As AI systems become capable of building larger-scale pieces of software, will developers shift to mostly managing and guiding these systems, rather than writing code themselves?"
- "Which software development roles will change the most, and which might disappear entirely?"

### 3.6 Terminology
"vibe coding" ("developers of varying levels of experience describe their desired outcomes in natural language and let AI take the wheel on implementation details"); Feedback Loop = "Claude completes tasks autonomously but with help of human validation (for example, where the user sends any errors back to Claude)"; Directive = "Claude completed a task with minimal user interaction"; "agentic".

---

## 4. Anthropic Economic Index report: Learning curves — Mar 2026

- **Date:** 24 Mar 2026. **URL:** https://www.anthropic.com/research/economic-index-march-2026-report
- **PDF (report):** https://cdn.sanity.io/files/4zrzovbb/website/4053bf3440c0c85b8852052770c5b4cf882689c3.pdf (fetched; text extracted locally). **PDF (appendix):** https://cdn.sanity.io/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf and https://cdn.sanity.io/files/4zrzovbb/website/a3cdcd9e67c3c4c51440429dd016cacba514b35b.pdf (two near-identical appendix versions are linked). **Data:** https://huggingface.co/datasets/Anthropic/EconomicIndex
- **Authors:** Maxim Massenkoff*, Eva Lyubich*, Peter McCrory* (lead), Ruth Appel, Ryan Heller. Bibtex key massenkoff2026learning.
- **Curiosity:** the PDF contains a stray editorial note on p.14 next to Table 2.1 — "It gets rounded to 3.4 and 3.4. Needs to be 3.42 and 3.40" — i.e. the AI-autonomy row was corrected at the last minute.

### 4.1 Quantitative findings — Chapter 1 "What has changed since our last report"
1. **Sample:** 1M Claude.ai (Free/Pro/Max) conversations + 1M 1P API transcripts, **5–12 Feb 2026**; "three months following the release of Claude Opus 4.5 and coincident with the release of Claude Opus 4.6". 1P API sample "includes data from Claude Code".
2. **Computer & Mathematical tasks = 35% of Claude.ai conversations** (using 2019 O*NET-SOC codes; previous reports used the 2010 vintage — footnote 2).
3. **Top-10 O*NET task concentration (Figure 1.1):** Claude.ai fell from **24% (Nov 2025) to 19% (Feb 2026)**. Full series as plotted — Claude.ai: Jan 2025 21%, Mar 2025 ~24%, Aug 2025 23%, Nov 2025 24%, Feb 2026 19%; 1P API: Aug 2025 28%, Nov 2025 32%, Feb 2026 33% (Discussion: "top 10 O*NET tasks now accounting for 33% of traffic, up from 28%" since Aug 2025). [Mar 2025 value inferred from figure-label ordering — verify.]
4. **Use-case mix on Claude.ai (Figure 1.2):** work 46% → 45%; personal 35% → 42%; coursework 19% → 12% (Nov 2025 → Feb 2026). Footnote 3: "The drop in coursework conversations was 5 percentage points in countries where the school term was active and 12 percentage points in the countries where most students were on break."
5. **Job coverage:** "About 49% of jobs have seen at least a quarter of their tasks performed using Claude" — "that cumulative estimate barely changed" vs Nov 2025 (Appendix Fig A.2). "Our data from this report showed many fewer novel O*NET tasks than in our previous report"; "almost all tasks in this sample appeared in at least one of our previous samples".
6. **Collaboration modes, Claude.ai (Figure 1.3):** "augmentation in Claude.ai increased slightly... driven by small bumps in validation and learning patterns." Plotted series (augmentation / automation): Jan 2025 55/41, Mar 2025 55/42, Aug 2025 49/47, Nov 2025 52/45, Feb 2026 53/44 (remainder unclassified). [Ordering inferred from figure labels; verify in PDF Fig 1.3. Note the Sept 2025 report gave Aug 2025 automation as 49% under Sonnet 4 classification.] "Automation = directive + feedback loop; Augmentation = validation + task iteration + learning."
7. **1P API modes (Appendix Fig A.3):** "automation decreased sharply in the 1P API data" — no number in text (figure only). [NOT EXTRACTED — image.]
8. **Occupational migration:** since Aug 2025, Computer & Mathematical share "increased by 14% in the API and decreased by 18% in Claude.ai" (relative changes). Management tasks in Claude.ai rose from 3% to 5% ("analytical tasks (e.g., preparing an investment memo) and responding to customer questions").
9. **Average task value (Figure 1.4; volume-weighted mean hourly wage of workers doing the task, Feb 2026 $):** Claude.ai **$49.3 (Nov 2025) → $47.9 (Feb 2026)**; 1P API ~$50.5 (Aug 2025), $50.4 (Nov 2025), $50.7 (Feb 2026); earlier Claude.ai points $48.9 / $48.5 / $48.3 (Jan, Mar, Aug 2025 — ordering inferred). US average hourly wage reference **$37.3**. Decline "mostly due to an increase in simple factual questions (e.g., sports outcomes, weather) and a decrease in coding as it shifts to the API". Discussion: value "has declined on Claude.ai since our first report, while rising among API users."
10. **Table 1.1 — Claude.ai primitives, Nov 2025 → Feb 2026:** Human education 12.21 → 11.92 yr (−0.29); AI autonomy 3.38 → 3.41 (+0.02 as printed; arithmetic gives +0.03); Human-only time 185.53 → 183.77 min (−1.76); Human-and-AI time 15.35 → 14.30 min (−1.05); Human can't do alone 12.09% → 12.24% (+0.15pp). "All differences are statistically significant with p<0.001, except Human-only time with p<0.05."
11. **Emergent API automation patterns** (footnote 6 filter: O*NET tasks appearing ≥300 times in current data with ≥2× growth vs previous report): (a) business sales & outreach automation (sales enablement generation, B2B lead qualification research, customer data enrichment, cold-email drafting); (b) automated trading & market ops (monitor markets/positions, propose specific investments, inform traders of market conditions).
12. **Geographic convergence (Figure 1.5, Lorenz curves of AUI):** US states Gini **0.37 (Aug 2025) → 0.31 (Nov 2025) → 0.29 (Feb 2026)**; countries Gini **0.48 (Aug 2025) → 0.46 (Nov 2025) → 0.50 (Feb 2026)**. Top-5 US states' share of per-person usage 30% → 24% (Aug 2025 → Feb 2026); top-10 states 40% → 38% since last report. Top-20 countries 45% → 48% of population-adjusted usage. Convergence horizon for US states revised to **5–9 years** (from 2–5) — footnote 7: "5 years with weights, 9 years without".

### 4.2 Quantitative findings — Chapter 2 "Learning to use AI"
13. **Model selection (paid Claude.ai accounts, all model classes available):** Opus = **51%** of overall usage; **55% of Computer & Mathematical** tasks (+4.4pp); Educational tasks 45%. Figure 2.1 over/under-representation of Opus by occupation group: Computer & Mathematical +4.4pp; Business & Financial +2.3pp; Management +1.9pp; Life/Physical/Social Science +0.9pp; Office & Admin −0.6pp; Sales −1.6pp; Arts/Design/Media −5.7pp; Educational Instruction −6.5pp. Headline: "Opus is used 4 percentage points more than average for coding tasks and 7 percentage points less than average for tutoring-related tasks."
14. **Opus share vs occupation wage (Figure 2.2):** Claude.ai slope **+1.48pp per +$10/hr**; 1P API slope **+2.79pp per +$10/hr** ("about twice as large"). Examples: Software Developer tasks 34% Opus vs Tutor tasks 12% (Claude.ai).
15. **Table 2.1 — Low vs high tenure (high = signed up ≥6 months before the data pull):**
    - Collaboration mode: directive 38.1% vs 29.4% (−8.7pp); feedback loop 11.7% vs 12.1% (+0.5); task iteration 24.5% vs 28.2% (+3.6); validation 4.4% vs 5.6% (+1.3); learning 21.3% vs 24.7% (+3.4).
    - Use case: work 41.6% vs 48.9% (+7.3pp); personal 44.3% vs 40.3% (−4.0); coursework 14.1% vs 10.8% (−3.3).
    - Task success rate **66.7% vs 73.1% (+6.4pp)** (the summary's "10% higher success rate" is the relative figure).
    - Top-10 tasks' share of usage 22.2% vs 20.7% (−1.6pp).
    - Numeric facets (mean): AI autonomy 3.42 vs 3.40 (−0.6%); human education 11.5 vs 12.3 yr (+6.6%); AI education 11.7 vs 12.4 yr (+6.0%).
    - Footnote 2: "These results are similar however we define high tenure."
16. **Figure 2.3 (binned scatter by days since signup, 0–18 months):** years of schooling of the prompt "increases by almost 1 year for every additional year of Claude usage" (axis range ~11.4–12.8 yr); personal use falls from **44% (newest users) to 38% (signed up a year ago)** (axis ~34–46%).
17. **Request clusters with highest mean tenure:** AI research, git operations, revising manuscripts, startup fundraising. Lowest: writing haikus, checking sports scores, suggesting food for a party.
18. **Figure 2.4 — regression of binary success on high-tenure indicator (log-level data):** (1) raw ≈ **+5pp**; (2) + O*NET task and request-cluster fixed effects ≈ **+3pp**; (3) + full controls (model, use case, country fixed effects; language also mentioned) ≈ **+4pp**. 95% CIs plotted (not given numerically). Standard errors and N not reported in the PDF text.

### 4.3 Data & methods
- Privacy-preserving system (Clio); random 1M + 1M samples; 1P API record = prompt-response pair, "in some instances mid-session for multi-turn interactions". Consumer data = Claude.ai Free/Pro/Max; enterprise data = 1P API.
- **Log-level data:** "analysis performed at the log level, as opposed to aggregated task groupings. This is necessary for estimating the correlation between two primitives." Regressions "only estimate fixed effects for groupings that satisfy our privacy requirements—otherwise such cells are dropped prior to estimation"; minimum aggregate thresholds for unique accounts and conversations apply to any reported statistic.
- **Request clusters:** "A bottom-up taxonomy of what people ask Claude to do, generated using a privacy-preserving method that groups semantically similar conversations."
- **Economic primitives (Table A.1 prompts):** human time estimate (hours a competent professional with domain knowledge, tools, context and no AI would need); human-with-AI time (minutes the user spent, incl. reading, thinking, implementing outside the conversation "only if directly relevant"); multitasking (yes/no); human ability to complete task alone (yes/no); human education years (0–20, discrete); AI education years (0–20); use case (work / coursework / personal); AI autonomy (1 none – 5 extreme); task success (yes/no).
- Task value: May 2024 BLS OEWS; when multiple occupations do the same task, wages averaged "weighting by employment and the fraction of time spent on that task" (example: "Compute moisture or salt content..." done only by Food Science Technicians, wage $26.15).
- O*NET 2019 SOC codes for occupational figures (Fig A.1) vs 2010 vintage earlier.
- Convergence model re-run from the Jan 2026 report (AUI_{s,t} = AUI_{s,t-1}^β), with and without weights.

### 4.4 Limitations / caveats (verbatim)
- "The high-tenure users are self-selected and the differences here could reflect stable characteristics. They may be computer programmers, for example, who were more likely to be early adopters."
- "Further, there's an inherent survivorship bias: people who signed up a year before our data pull may be seeing positive results from their usage. We do not observe people who signed up a year ago but are no longer using Claude."
- "This could reflect that higher tenure users are better at prompting. But what if it reflects that they bring different tasks to Claude—ones more likely to be successful?"
- "While this could reflect sophistication of early adopters, it could also be evidence of learning-by-doing, where people get better at using Claude through experience."
- "An alternative interpretation, of course, is that these results are driven by cohort effects or survivorship bias. Early adopters could be more technical. Those who continue using Claude could be those with tasks that it is distinctly well-equipped to do. But carefully controlled regressions rule out simple versions of this confounding, like that long-tenured users bring different kinds of tasks. Over time, we will be able to more cleanly isolate cohort and survivorship bias from learning-by-doing."
- "Some of the drop in coursework can be explained by academic calendars in countries where students were on winter break during our sample period." "At the same time, increasing signups beginning around February brought more casual AI users."
- Footnote 3 (Ch.2): "Our sampling period overlapped with the release of our Super Bowl advertisements, which brought many first-time users."
- On model choice: "Technical users may notice performance gains and actively switch away from Sonnet, the default. Or efficiency-minded users may learn to use Sonnet for simpler tasks to avoid hitting usage limits. Relatedly, the differences here could reflect that most educational tasks are already fairly easy for Sonnet, or that students are more likely to be mindful of usage limits."
- "Overall, Claude is used for high-value, complex work that is not broadly representative of the US economy."
- "One change goes ostensibly in the opposite direction: the tasks performed by Claude were judged to be slightly less possible for a human without access to AI."
- Success is "Claude's assessment of whether the conversation was successful" (model-judged, not user-reported).

### 4.5 Open questions / future work
- "do experienced users get better over time? How does their usage differ?" — answered only correlationally; isolating learning-by-doing from cohort/survivorship is deferred: "Over time, we will be able to more cleanly isolate...".
- "Little is known about how AI users choose between different models, navigating tradeoffs around speed, performance, and cost."
- "This pushes back against a hypothesis we made last year that automated use may be more typical of more experienced, sophisticated users; instead, we find that the most advanced users are more likely to iterate with Claude." (Reverses the Sept 2025 conjecture that rising directive share reflects learning-by-doing.)
- Skill-biased technological change channel: "early adopters with high-skill tasks have more successful interactions with Claude than later, less technical adopters. These early-adopting users may simultaneously be the most exposed to AI-driven disruption and most aided by AI."
- "If effective AI use requires complementary skills and expertise... and if such skills can be acquired through use and experimentation, then the benefits from early adoption may be self-reinforcing."
- "we expect that this migration from Claude.ai to the API may signal more imminent transformation of work for the associated jobs."
- Lower-income countries "paradoxically showing more complex use in some cases" because early adopters dominate their user base — implies a composition-vs-learning identification problem for cross-country primitives.

### 4.6 Terminology
"learning curves", "learning-by-doing", "tenure" (days since signup), "high tenure" (≥6 months), "task success", "economic primitives", "request clusters", "log-level data", "1P API" / "consumer data" / "enterprise data", "task value" (volume-weighted mean wage), "Anthropic AI Usage Index (AUI)", "Lorenz curve", "Gini coefficient", "observed exposure" (borrowed from the labor-market-impacts paper), "emergent automation patterns", "model selection", "demand for intelligence", "adoption curve", "skill-biased technological change", "collaboration mode".

---

## 5. Estimating AI productivity gains from Claude conversations — Nov 2025

- **Date:** 25 Nov 2025. **URL:** https://www.anthropic.com/research/estimating-productivity-gains. **Authors:** Alex Tamkin, Peter McCrory.

### 5.1 Quantitative findings
1. Sample: 100,000 Claude.ai conversations (Free, Pro, Max).
2. Median estimated human-only completion time per conversation task: **1.4 hours**. Median time saving **80%** (median conversation 84%); distribution concentrated in the 50–95% range, peaking at 80–90%.
3. Median implied labour cost of the task: **$55** per conversation.
4. Average human-only task duration by occupation group: Management 2.0 h; Legal 1.8 h; Education 1.7 h; Arts/Media 1.6 h; Food preparation, Installation/maintenance, Transportation 0.3–0.5 h.
5. Average implied cost by group: Management $133; Legal $119; Computer/Mathematical $82; Business/Financial $69; Food prep/serving $8.
6. Examples: curriculum development 4.5 h → 11 min (89% saving); invoice/memo writing 87%; financial-analyst task 80% saving, $31 implied cost; compiling information from reports 95%; checking diagnostic images 20%.
7. Economy-wide: implied US labour-productivity growth **+1.8 percentage points per year over a 10-year horizon**; implied TFP increase 1.08% annualised (labour share assumed 0.64). Comparators: 2019 rate 1.8%/yr ("doubles recent" rate — i.e. adds 1.8pp on top); 2.1% average since 1947; TFP <1% since early 2000s, 1.6% 1995–2004, 0.7% avg 2015–2024.
8. Occupational contribution to the aggregate gain: Software developers 19%; General & operations managers 6%; Market research analysts/marketing specialists 5%; Customer service representatives 4%; Secondary school teachers 3%.
9. Self-consistency across prompt variants: log-scale correlations r = 0.89–0.93 (1,800 conversations per variant).
10. External benchmark (JIRA tasks, 1,000 with ground-truth durations): human developer estimates Spearman ρ = 0.50, r_log = 0.67; Claude Sonnet 4.5 ρ = 0.44, r_log = 0.46; Sonnet 4.5 with 10 examples ρ = 0.39, r_log = 0.48. Claude's estimates are compressed (overestimates short, underestimates long). Sonnet 4.5 > Sonnet 4.
11. Comparison: recent RCT time savings 14%–56% vs the 80% model estimate; the 1.8pp sits "towards the upper end of recent estimates" (OECD 2024 "Miracle or Myth"; Filippucci, Gal & Schief 2024 chart in appendix).

### 5.2 Data
- Claude.ai Free/Pro/Max, 100k transcripts, analysed via the privacy-preserving system (Clio). Window not stated in fetched text (likely Nov 2025 — VERIFY).
- Wages: BLS OEWS May 2024. O*NET task lists and time allocations. Task time = median of estimates per O*NET task.

### 5.3 Methods
- **Claude-as-estimator:** Claude reads anonymised transcripts and estimates time-without-AI and time-with-AI.
- **O*NET mapping**; **Hulten's theorem** to aggregate task-level log time differences using Domar weights (task share of wage bill × labour share); **growth accounting** following Acemoglu (2024) baseline; productivity improvement = ln(time without AI) − ln(time with AI); prompt-variation self-consistency; JIRA benchmark validation.

### 5.4 Limitations (verbatim)
- "Claude's predictions are imperfect and we lack real-world validation of Claude's time estimates. AI systems are imperfect predictors, and can't see activity that happens after the user finishes their interaction with the model."
- Estimates "might overstate current productivity effects to at least some degree" because they omit "additional time humans spend on tasks outside of their conversations with Claude, including validating the quality or accuracy of Claude's work."
- "Real jobs are more complex than an O*NET task list, and the time allocations we estimate for each task are only approximate. Many important aspects of work—tacit knowledge, relationships, judgment under uncertainty—don't appear in these formal task descriptions."
- "A recent randomized controlled trial studying end-to-end software features did not see time savings due to AI."
- The human-vs-AI comparison "could either understate the productivity gains – since it takes additional resources we're not accounting for to hire an employee and communicate context, and possibly overstate it, if the quality of the AI's work is worse than a human's."
- "Our model can help predict the effects of such a restructuring, but it cannot predict how companies might decide to restructure, or how quickly this process might happen."
- "Our model does not capture how AI systems could accelerate or even automate the scientific process, nor the effects that would have on productivity, growth, and the structure of work."
- "Our dataset is derived from Claude.ai conversations only. This sample is not representative of the full spectrum of AI uses, and there's likely some selection effect where the instances of tasks people use Claude for are the ones they think Claude will be most useful."
- "Due to our finite sample size, we likely miss some less common AI tasks."
- "This estimate should be taken as an exercise exploring what might happen based on current usage patterns, not a prediction of the impact on productivity that is actually most likely to happen"; it "does not account for unevenness in adoption, which might reduce real-world productivity gains in the short term."

### 5.5 Open questions
Speed of diffusion; how firms restructure and when; AI in scientific discovery; which tasks become "bottleneck tasks"; time spent refining output outside the chat.

### 5.6 Terminology
"current-generation AI models", "task-level efficiency gains", "intra-task variation", "within-task heterogeneity", "Domar weight", "labor share of income" (0.64; 0.57 in AI-exposed industries per Acemoglu 2024), "bottleneck tasks", "selection effect", "Claude-as-estimator".

---

## 6. Country reports (2026): Australia and Canada

### 6A. How Australia Uses Claude: Findings from the Anthropic Economic Index — 31 Mar 2026
- **URL:** https://www.anthropic.com/research/how-australia-uses-claude. **Author:** Peter McCrory (acknowledgements: Keir Bradwell, Ria Strasser Galvis, Ryan Heller, Eva Lyubich, Jennifer Martinez, Maxim Massenkoff, Jared Mueller, Sarah Pollack).

**Quantitative findings**
1. Australia = **1.6%** of global Claude.ai traffic; **11th** by volume (Feb 2026 sample).
2. **AUI = 4.1** (usage ~4× what working-age population predicts); **7th** per capita globally (behind Singapore, Israel, Luxembourg, Switzerland, US, Canada). [Compare Sept 2025: Australia AUI 4.10, 3rd. A later Mi3 press piece (Jul 2026) reports Australia "first among 121 countries" at 6.4× in May 2026 — from a later data cut, not this report.]
3. Share of Australian conversations by state: NSW 37.2%; Victoria 30.8%; Queensland 17.7%; WA 7.6%; SA 4.6%; ACT 1.4%; Tasmania 0.6%; NT 0.1%.
4. State AUI (relative to Australian working-age population): NSW 1.20; Victoria 1.19; WA 0.68; Tasmania 0.32; NT 0.12.
5. Use-case mix: work 46%, coursework 7%, personal 47%.
6. Primitives: prompts need **11.9 years** of schooling on average (comparable to Anglosphere peers, above global median); estimated human-only task duration **2.7 hours** vs global 3.3 hours (~20% shorter); AI autonomy **3.38** on 1–5 (lower = more collaborative).
7. Task diversity: top-100 tasks cover 47.3% of Australian usage vs US 47.7%, UK 48.3%, Canada 50.2%, global 52.3%. Distinct tasks observed: Australia 171; global 3,258. (NZ and Ireland omitted: "fewer than 100 distinct tasks were observed".)
8. SOC major-group differences vs global (top-100 tasks): Computer & Mathematical −8.0pp; Educational Instruction −2.7pp; Management +2.3pp; Office & Admin Support +1.3pp; Life/Physical/Social Science +1.3pp. Anglosphere-average Computer & Math shortfall 8.9pp; Anglosphere Educational Instruction +1.6pp (Australia −2.7pp — Australia is unusual here).
9. Request clusters vs global: general coding assistance 13.5% vs 16.8% (−3.3pp); document translation under-represented; over-represented: personal life management +1.9pp, health & well-being support +1.8pp, workplace correspondence +1.7pp, business documents +1.6pp, financial guidance +1.3pp.
10. Australian users "more likely than the global average to keep humans in the loop".

**Data & methods:** Claude.ai, Feb 2026, 1M conversations (same sample as the March 2026 report); AUI = share of Claude usage ÷ share of working-age population; ABS Estimated Resident Population (June qtr 2025); ABS State Accounts 2024–25 (GSP per capita); O*NET + SOC major groups; request clusters; economic primitives (education years, human-only time, autonomy, success).

**Limitations (verbatim where possible)**
- "Since we can only compare across the eight, the lack of correlation between income and usage is suggestive rather than conclusive."
- Workforce composition is "a likely factor" (inferred, not measured); ACT public sector "may reflect barriers"; WA's low usage despite high GSP/capita unexplained (mining-heavy).
- Coding under-representation is "expected" for high-adoption countries.

**Open questions:** why WA is low; what occupational composition drives NSW/Vic; public-sector adoption in ACT; whether the state pattern (composition not income) generalises.

**Terminology:** "Anthropic AI Usage Index (AUI)", "economic primitives", "AI autonomy", "top 100 tasks", "request clusters", "Anglosphere peers", "high-adoption economies" (AUI > 1).

### 6B. How Canada Uses Claude: Findings from the Anthropic Economic Index — Jul 2026 (page dated 14 Jul 2026; bibtex date 2026-06)
- **URL:** https://www.anthropic.com/research/how-canada-uses-claude. **Author:** Peter McCrory.

**Quantitative findings**
1. Canada = **2.6%** of global Claude.ai traffic; **8th** by volume; **AUI 4.4** (≈4× expected); 2nd-highest AUI among the top-10-by-volume countries (after the US).
2. Provincial share of Canadian conversations: Ontario 43.9%; Quebec 20.8%; British Columbia 18.9%; Alberta 10.2% (top 4 ≈ 94%).
3. Provincial AUI (within Canada): BC 1.4×; Ontario 1.1×; Newfoundland & Labrador 0.2×; other provinces below parity. Territories below reporting threshold.
4. Use-case mix range across provinces: work 34–40%; coursework 13–18%; personal 44–51%.
5. Provincial income per capita: "no clear correlation" with adoption; share of employment in professional, scientific & technical services: systematic positive correlation with usage per capita. Globally (IMF advanced economies with ≥200 conversations) usage per capita tracks GDP per working-age capita, and Canada sits above the line.
6. Translation: document translation is the most distinctive Canadian use vs Anglosphere peers (Australia, UK, US); translation/editing requests correlate with public-administration employment shares across the seven provinces above threshold ("official bilingualism").
7. Over-represented vs peers: academic coursework (maths/STEM), coding assistance, resume drafting, document translation ("tilts toward education and labor-market entry"). Under-represented: professional communication, workplace email, marketing content, legal assistance, everyday personal tasks (cooking, home maintenance, health). Figure 7 covers groupings ≥1% of Canadian conversations (6 most Canadian + 6 most peer-distinctive).
8. Top-100 tasks cover 50.2% of Canadian usage (from the Australia report's table).

**Data & methods:** Claude.ai, Feb 2026, 1M conversations; AUI; Statistics Canada provincial employment and GDP; World Bank; IMF advanced-economy list; work/coursework/personal classifier; request clusters.

**Limitations:** territories below threshold; seven provinces only for translation; consumer data only; single month; no time series; classifier and reweighting details deferred to main reports.

**Open questions:** why provincial income is uncorrelated when the cross-country relationship is strong; mechanism from workforce composition to adoption; whether the coursework tilt persists outside term time.

**Terminology:** "usage per capita", "working-age population", "advanced economies", "labor-market entry", "official bilingualism", "Anglosphere peers".

---

## 7. Anthropic Education Report: The AI Fluency Index — Feb 2026 (education/AI-fluency report)

- **Date:** report dated 16 Feb 2026 (page 23 Feb 2026). **URL:** https://www.anthropic.com/research/AI-fluency-index → redirects to https://academy.claude.com/tutorials/the-ai-fluency-index (original: anthropic.com/news/anthropic-education-report-the-ai-fluency-index). **Authors:** Kristen Swanson, Drew Bent, Zoe Ludwig, Rick Dakan, Joe Feller.
- Not an Economic Index report, but uses the same Clio pipeline and is the source of the "artifacts" and iteration/evaluation framing.

### 7.1 Quantitative findings
1. Sample: **9,830** anonymised multi-turn Claude.ai conversations, **20–26 Jan 2026**.
2. Prevalence of the 11 observable behaviours: iterates & refines 85.7%; clarifies goal 51.1%; provides examples 41.1%; specifies format/structure 30%; sets interaction mode 30%; communicates tone/style 22.7%; identifies missing context 20.3%; defines audience 17.6%; questions reasoning 15.8%; consults on approach before execution 10.1%; checks facts 8.7%.
3. Iteration effect: conversations with iteration (n=8,424) show 2.67 other fluency behaviours on average vs 1.33 without (n=1,406). In iterative conversations: clarifies goal 54.5% vs 30.9%; provides examples 44.4% vs 21.8%; identifies missing context 22.8% vs 5.7%; specifies format 32.4% vs 16.1%; questions reasoning 17.9% vs 3.2% (5.6× more likely; 4× more likely to identify missing context).
4. **Artifact paradox** (artifacts in 12.3% of conversations; n=1,209 vs 8,621): direction behaviours up — refines 94.1% vs 84.5%; clarifies goal 64% vs 49.3%; examples 52.9% vs 39.5%; format 42.8% vs 28.3%. Evaluation behaviours down — identifies missing context 15.8% vs 21%; checks facts 5.5% vs 9.2%; questions reasoning 13% vs 16.2%.
5. Robustness: day-of-week variation 1–5pp (iteration 81.4% Saturday vs 87.9% weekday peak); across six languages most behaviours vary ≤3pp.
6. Only 30% of users explicitly set interaction norms.

### 7.2 Data & methods
- 4D AI Fluency Framework (Dakan & Feller with Anthropic): 24 behaviours; 11 directly observable analysed; 13 unobservable excluded. 11 binary classifiers (Claude Sonnet 4); Haiku 3.5 for language detection; Clio privacy pipeline; filtered to multi-turn, excluding greetings/tests/chitchat (manual review of 200 excluded chats).

### 7.3 Limitations (verbatim)
- "Our sample reflects Claude.ai users who engaged in multi-turn conversations during a single week in January 2026." Users "likely skew towards early adopters"; "a baseline for this population, not as a universal benchmark"; cannot capture "seasonal or longitudinal effects"; Claude.ai only.
- "In this study, we only assessed the 11 of the 24 behavioral indicators that are directly observable in conversations on Claude.ai." "All behaviors related to the responsible and ethical use of AI outputs occur outside of these conversations, and are not captured."
- Binary present/absent coding "likely misses significant nuance—like arguable or partial demonstrations of behaviors, or overlapping signals between them".
- "Users might demonstrate fluency behaviors mentally (such as fact-checking Claude's claims against their own knowledge) without expressing these behaviors in conversation." "This seems especially relevant for our data on artifacts—users might be evaluating Claude's outputs through testing and practical use."
- "The relationships we identify are correlational." "We don't know whether one behavior causes another, or whether they both reflect some common underlying factor, like task complexity or user preferences."
- Three unresolved hypotheses for the artifact paradox: polished outputs discourage questioning; artifact tasks care less about factual precision; evaluation happens off-platform.

### 7.4 Future work (verbatim)
- "In future work, we plan to conduct 'cohort analyses,' comparing new users to experienced ones in order to understand how familiarity with AI is correlated with fluency development."
- Qualitative methods for unobservable behaviours; causal tests ("whether encouraging iterative conversations leads to greater critical evaluation"); Claude Code analysis ("initial analysis that found consistency between Claude Code conversations and ones in Claude.ai... still preliminary").

### 7.5 Terminology
"AI fluency", "Description / Delegation / Discernment / Diligence" (4D), "artifacts" ("code, documents, interactive tools, and other outputs"), "iterates and refines", "staying in the conversation", "questioning polished outputs", "setting the terms of the collaboration", "augmentative" use.

### 7.6 Related external paper
"A paradox of AI fluency" (Potts & Sudhof, arXiv 2604.25905, 28 Apr 2026): 27,000 WildChat-4.8M transcripts; fluent users have more but visible/recoverable failures; novices have "invisible failures". Not Anthropic; useful as a counterpoint.

---

## Supplementary A. Anthropic Economic Index report: Uneven geographic and enterprise AI adoption — Sep 2025 (V3)

Not in the brief's list, but it introduces the AUI, the 1P API sample and the directive-share time series that later reports build on; logged so the cross-report threads have their origin numbers.

- **Date:** 15 Sep 2025. **URL:** https://www.anthropic.com/research/anthropic-economic-index-september-2025-report (arXiv 2511.15080). **Authors:** Ruth Appel, Peter McCrory, Alex Tamkin (lead); Miles McCain, Tyler Neylon, Michael Stern.

**Quantitative findings**
1. Claude.ai V1 → V3 (Dec 2024/Jan 2025 → Aug 2025): coding ~36% → 36%; Educational/Library 9.3% → 12.4%; Life/Physical/Social Science 6.3% → 7.2%; Business/Financial 6% → 3%; Management 5% → 3%; "programming creation" tasks 4.1% → 8.6%; debugging/error correction 16.1% → 13.3%; web search/database tasks 0.03% → 0.49%; internet-based research 0.003% → 0.27%; instructional-materials development 0.2% → 1.5%; multimedia documents 0.16% → 0.55%.
2. **Directive share (Claude.ai): 27% (V1) → 39% (V3).** V3 is the first report where automation exceeds augmentation on Claude.ai: 49% automation with Sonnet 4 classification (45% under Sonnet 3.7 robustness re-classification).
3. **AUI definition:** "For each geography, we calculate its share of Claude usage, and its share of the working-age population (ages 15-64). We then calculate the AUI by dividing these shares."
4. Top AUI countries: Israel 7.0; Singapore 4.57; Australia 4.10; New Zealand 4.05; South Korea 3.73. Low: Indonesia 0.36; India 0.27; Nigeria 0.2. Share of global usage: US 21.6%; India 7.2%; Brazil 3.7%.
5. US states by AUI: DC 3.82; Utah 3.78 (flagged: "a notable fraction of its usage appeared to be possibly associated with coordinated abuse"); California 2.13; New York 1.58; Virginia 1.57.
6. Income elasticities: countries — 1% higher GDP per working-age capita → 0.7% higher usage per capita; US states — 1% higher state GDP per capita → 1.8% higher AUI.
7. Coding share: global ~1/3; India >50%. Higher-AUI countries use Claude more collaboratively (augmentation) after controlling for task mix.
8. **1P API (Aug 2025, 1M transcripts ≈ half of 1P API usage):** automation-dominant patterns in **77%** of transcripts; automation dominates in 97% of O*NET tasks in API vs 47% on Claude.ai. Occupational mix API vs Claude.ai: Computer/Math 44% vs 36%; Office/Admin 10% vs ~5%; Education/Library 3.6% vs 12.3%; Arts/Entertainment 5.2% vs 8.2%. Bottom-up API uses: debugging web apps ~6%; resolving technical issues ~6%; developing AI-system evaluations ~5%; marketing materials 4.7%; business/recruitment data processing 1.9%.
9. Task concentration Gini: Claude.ai 0.84; 1P API 0.86. Bottom 80% of task categories = 12.7% of Claude.ai usage and 10.5% of API usage.
10. Tokens: output-length elasticity to input length 0.38; 90th-percentile tasks >4× output of 10th-percentile.
11. Cost sensitivity: raw elasticity of usage to cost ≈ +3.0 (costlier tasks used more); controlling for task characteristics −0.29: "A 10% cost reduction for a particular task would only increase usage by around 3%."
12. External context cited: Gallup 2025 — 40% of US employees use AI at work (20% in 2023); Census Aug 2025 — 9.7% of firms use AI (3.7% fall 2023), Information sector 25%.

**Data:** Claude.ai 1M conversations 4–11 Aug 2025 (Free/Pro/Max); privacy cells ≥15 conversations & ≥5 accounts; bottom-up clusters ≥500 conversations & ≥250 accounts; VPN/anycast/hosting excluded; 150+ countries, 50 states + DC; countries with ≥200 observations only for the primitives figures. 1P API 1M transcripts, Aug 2025, prompt-response pairs. Classification with Sonnet 4 (V2 used Sonnet 3.7).

**Limitations (verbatim excerpts):** "We only include countries with at least 200 observations..."; "Future work, for example using stratified sampling, will allow us to explore these patterns with higher accuracy given limited observations for smaller countries and states."; "V3 uses Claude Sonnet 4 for classification, while V2 used Sonnet 3.7, which complicates direct comparison."; elasticity estimates are "a preliminary exploration"; "Output length does not capture all dimensions of task complexity"; geographic data not available for 1P API; conversations are the unit and one user can contribute several ("sampling conversations at random versus stratified by user does not yield substantively different results").

**Open questions (verbatim):** "What are the local labor market consequences for workers and firms of AI usage & adoption?"; "What determines AI adoption across countries and within the US? What can be done to ensure that the benefits of AI do not only accrue to already-rich economies?"; "What role, if any, does cost-per-task play in shaping enterprise deployment patterns?"; "Why are firms able to automate some tasks and not others?"; whether the rise in directive use "is attributable to improving model capabilities or learning-by-doing"; whether "highly concentrated use" will "evolve towards a broader distribution".

**Terminology:** "Anthropic AI Usage Index (AUI)", tiers "Leading / Upper Middle / Lower Middle / Emerging / Minimal", "1P API", "O-Ring forces", "context" (input tokens), "bottom-up taxonomy".

---

## Supplementary B. Anthropic Economic Index report: Economic primitives — Jan 2026 (V4)

The immediate predecessor of "Learning curves"; introduces the five primitives, success rates, task horizons, effective coverage and the convergence model. **Date:** 15 Jan 2026. **URL:** https://www.anthropic.com/research/anthropic-economic-index-january-2026-report; PDF https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf (fetched, text extracted). **Authors:** Ruth Appel*, Maxim Massenkoff*, Peter McCrory* (lead); Miles McCain, Ryan Heller, Tyler Neylon, Alex Tamkin.

**Data:** 1M Claude.ai (Free/Pro/Max) conversations + 1M 1P API transcripts, **13–20 Nov 2025** ("just prior to the release of Opus 4.5"). Privacy cells ≥15 conversations & ≥5 accounts; bottom-up clusters ≥500 & ≥250. Classifier: Sonnet 4.5 (previous report Sonnet 4): "different models can generate different classification outcomes, though these effects tend to be modest". "over 3,000 unique work tasks in Claude.ai".

**Quantitative findings (PDF text, verbatim numbers)**
1. Top-10 task concentration: Claude.ai 24% (up from 23%); 1P API 32% (up from 28%). Most common task both platforms: "modifying software to correct errors" — 6% of Claude.ai usage, ~1 in 10 API records.
2. **Collaboration modes, Claude.ai:** Jan 2025 56% augmentation / 41% automation; Aug 2025 automation > augmentation; Nov 2025 augmentation "jumped 5pp to 52%", automation "fell 4pp to 45%"; unclassified fell 3.9% → 3.0%. **Directive: 27% (Jan 2025) → 39% (Aug 2025) → 32% (Nov 2025)** ("fallen 7pp"). "the automation share was still elevated as compared to nearly one year ago... suggesting that the underlying trend is still toward greater automation even as the August spike overstated how quickly it was materializing." Rise in augmentation "driven mainly by... 'task iteration' rather than... 'learning'". Suggested cause: "Product changes during this period—including file creation capabilities, persistent memory, and Skills for workflow customization—may have shifted usage patterns toward more collaborative, human-in-the-loop interactions."
3. **Claude.ai vs 1P API (Nov 2025):** work 46% vs 74%; directive 32% vs 64%; automation "less than half" vs "three-quarters"; human time with AI 15 min vs 5 min; human-only time 3.1 h vs 1.7 h; task success 67% vs 49%; Claude.ai users grant more autonomy and bring more tasks they couldn't do alone. Occupational (Ch.3 comparison): Computer & Math 36% vs 52%; Office & Admin 8% vs 15%; Educational Instruction 16% vs 4%; Arts/Design/Entertainment 11% vs 6%. [The web summary also reported Computer & Math 34% (Claude.ai) and 46% / Office & Admin 13% (API) — these appear to come from Fig 1.2 with a different denominator/vintage; verify which figure before citing.] API Office & Admin "rose 3pp in August to 13% in November 2025" (example API tasks: B2B cold sales emails 0.47%, analyse emails/draft replies 0.28%, invoice processing 0.24%, classify emails 0.23%, calendar scheduling 0.16%).
4. **Use case (Claude.ai global):** 46% work, 19% coursework, 35% personal. Work and personal more common in higher-income countries; coursework in lower-income (echoes Microsoft).
5. **Primitives by cluster:** software development — 3.3 h human-only, ~15 min with AI, 13.8 yrs education, 82% could do alone, 64% work, 61% success; personal life management — 1.8 h, ~15 min, 9.1–9.4 yrs, 96% could do alone, 17% work, 78% success; both ≈3.5 autonomy. Global Claude.ai averages (from Mar 2026 Table 1.1): education 12.21 yr, autonomy 3.38, human-only 185.5 min, with-AI 15.4 min, can't-do-alone 12.1%.
6. Education: mean predicted education for all O*NET tasks 13.2 yr vs Claude-covered tasks 14.4 yr; prompt and response education r > 0.92; "Claude.ai may somewhat underestimate the human education years needed for many tasks".
7. **Speedup vs education (Fig 4.1):** ~9× at 12 yrs, ~12× at 16 yrs on Claude.ai; API higher at all levels. Success falls with complexity: <high-school tasks 70% vs college-level 66% (Claude.ai). "the automation share is essentially unrelated to the human levels of education required to write the prompt."
8. **Task horizons (Fig 4.3):** API success ~60% for sub-hour tasks → ~45% for 5+ h; fitted 50%-success horizon **3.5 h** (METR: 2 h Sonnet 4.5, ~5 h Opus 4.5); Claude.ai extrapolated 50% horizon **~19 h**.
9. **Effective AI coverage:** weighted sum of task success × time share × frequency; "49% of jobs have seen AI usage for at least a quarter of their tasks" (with 2010 O*NET). Examples: data entry keyers, medical transcriptionists, radiologists high; microbiologists low despite 50% task coverage.
10. **Geography:** AUI = country share of usage ÷ share of working-age population; Denmark AUI 2.1. 1% higher GDP per capita → 0.7% higher usage per capita. US: top-5 states 50% of usage vs 38% of working-age population; each +1% share of computer/math workers → +0.36% usage per capita, explaining "nearly two-thirds of the cross-state variation"; KL-divergence of state workforce from Claude usage mix predicts AUI. **US-state Gini 0.37 (Aug) → 0.32 (Nov 2025)**; world "essentially unchanged". Convergence model AUI_{s,t} = AUI_{s,t−1}^β: OLS β≈0.77, WLS β≈0.76, 2SLS β≈0.89 (unweighted)/0.86 → "2–5 years" to parity, "roughly 10x faster than the spread of previous economically consequential technologies"; "based on a change observed over a three month period".
11. Higher-AUI / higher-income countries: less automation, less autonomy delegated; not significant across US states. Task success negatively related to education across countries but positively within US states (insignificant with controls).
12. **Deskilling/upskilling:** net first-order effect is deskilling because "AI removes tasks that require relatively higher levels of education" (technical writers, travel agents, teachers deskilled; real-estate managers upskilled).
13. **Productivity:** baseline 1.8pp/yr for a decade (both platforms); success-adjusted 1.2pp (Claude.ai) / 1.0pp (API); CES σ=0.5 → 0.7–0.9pp (0.8/0.6 with success adjustment); σ=1.5 → 2.2–2.6pp. Based on tasks with ≥200 observations.
14. Validation: Claude.ai classifiers checked against a human researcher on transcripts users had given feedback on; API classifiers on "internal and synthetic data"; simple prompts beat complex ones for success; chain-of-thought kept for three facets only. "While we are very confident in the directional accuracy of the new measures... none of the measures should be taken as exact or definitive."

**Limitations / open questions (verbatim):** "users choose which tasks to bring to Claude. This means observed success rates reflect not just model capability but also user judgment about what will work, the cost of setting up the problem for Claude, and the expected time savings if the task succeeds."; "there's no guarantee that more performant models would show improvement in this plot, because users may respond to new models by providing more challenging presentations of otherwise similar O*NET tasks."; "Its implications depend on how often these Claude conversations actually displace or augment work that would otherwise be done by humans"; "In future work, we could leverage our 1P API data to understand which of these tasks are being integrated into production workflows"; σ is "largely a question of fact that our data cannot resolve"; "We will revisit this question of the pace of diffusion in future reports."; "Diffusion may ultimately proceed more slowly in the months and years to come."

**Terminology:** "economic primitives", "task success", "AI autonomy", "human-only time", "speedup", "task horizon", "effective AI coverage", "deskilling/upskilling", "AUI", "Lorenz curve", "Gini", "proportional convergence", "half-life", "consumer data" / "enterprise data".

---

## Supplementary C. Labor market impacts of AI: A new measure and early evidence — Mar 2026

Source of the term **"observed exposure"** used in the March 2026 report. **Date:** 5 Mar 2026. **URL:** https://www.anthropic.com/research/labor-market-impacts; PDF https://cdn.sanity.io/files/4zrzovbb/website/a42bc3fc08283562f08fd8bdee8f6f9a3d506e87.pdf. **Authors:** Maxim Massenkoff, Peter McCrory (feedback from Martha Gimbel, Anders Humlum, Evan Rose, Nathan Wilmers).

**Key findings (verbatim bullets):** "We introduce a new measure of AI displacement risk, observed exposure, that combines theoretical LLM capability and real-world usage data, weighting automated (rather than augmentative) and work-related uses more heavily"; "AI is far from reaching its theoretical capability: actual coverage remains a fraction of what's feasible"; "Occupations with higher observed exposure are projected by the BLS to grow less through 2034"; "Workers in the most exposed professions are more likely to be older, female, more educated, and higher-paid"; "We find no systematic increase in unemployment for highly exposed workers since late 2022, though we find suggestive evidence that hiring of younger workers has slowed in exposed occupations".

**Numbers**
1. Tasks rated β=1 by Eloundou et al. (2023) account for **68%** of observed Claude usage; β=0 tasks **3%**; 97% of observed tasks are β=0.5 or 1.0. (Usage from the Aug and Nov 2025 Economic Index datasets; "for O*NET tasks that are highly semantically similar, we split the counts across them".)
2. Theoretical β coverage: Computer & Math 94%, Office & Admin 90% of tasks; **observed coverage of Computer & Math tasks only 33%**.
3. Most exposed occupations: Computer Programmers **75%** coverage; Customer Service Representatives next ("whose main tasks we increasingly see in first-party API traffic"); Data Entry Keyers **67%**. **30% of workers have zero coverage** (tasks too rare to meet the threshold — Cooks, Motorcycle Mechanics, Lifeguards, Bartenders, Dishwashers...).
4. BLS 2024–2034 projections: each +10pp observed exposure → **−0.6pp** projected growth (employment-weighted OLS; "the relationship is slight"; "no such correlation using the Eloundou et al. measure alone").
5. Top-quartile-exposure vs zero-exposure workers (CPS, Aug–Oct 2022): +16pp female; +11pp white; ~2× as likely Asian; earn **47% more**; graduate degrees 17.4% vs 4.5%.
6. Unemployment difference-in-differences since ChatGPT: "small and insignificant"; detectable effect ≈ 1pp differential. Scenario: laying off all top-10%-coverage workers would raise top-quartile unemployment 3% → 43% and aggregate 4% → 13%; a "Great Recession for white-collar workers" would take top-quartile unemployment 3% → 6%.
7. Young workers (22–25): job-start rate into exposed occupations fell by ~0.5pp/month vs stable 2%/month for unexposed — a **14% drop** vs 2022, "just barely statistically significant"; no decrease for workers >25. Brynjolfsson et al. cited: 6–16% employment fall for ages 22–25.

**Method:** covered = theoretically feasible (β>0) AND sufficient work-related Claude usage; fully automated implementations full weight, augmentative use half weight; task coverage averaged to occupation weighted by time fraction, then to category weighted by employment. Crosswalk O*NET-SOC → occ1990 via Eckhardt & Goldschlag (2025). Robustness: Spearman rank correlation of exposure "exceedingly high" across alternative choices (footnote 6 lists the judgment calls).

**Limitations / future work (verbatim):** "There are judgment calls involved at every step."; "The young workers who are not hired may be remaining at their existing jobs, taking different jobs, or returning to school."; "job transitions may be more vulnerable to mismeasurement in surveys"; "The Eloundou et al. metric could also be updated, to the extent that it is linked to LLM capabilities as of early 2023"; "a key next step might be to look at how recent graduates with educational credentials in exposed areas are navigating the labor market"; "Our task- and occupation-level exposure measures can readily incorporate other usage data, and be extended to different countries."

**Terminology:** "observed exposure", "theoretical exposure/capability" (β), "task coverage", "O-ring model" (Gans & Goldfarb 2025), "treated" workers, "job finding rate".

---

## Supplementary D. Anthropic Economic Index report: Cadences — Jun 2026

Latest report at time of writing; logged for the cross-report timeline. **Date:** 26 Jun 2026. **URL:** https://www.anthropic.com/research/economic-index-june-2026-report. PDF: https://cdn.sanity.io/files/4zrzovbb/website/9e0eadc8097864886c5d5060ebb1f89b02ea29d6.pdf; appendix https://cdn.sanity.io/files/4zrzovbb/website/03ed1410f74a65ae4cc2a27120d0875e1e569535.pdf. **Authors:** Maxim Massenkoff, Eva Lyubich, Szymon Sacher, Zoe Hitzig, Shaoyi Zhang, Ryan Heller, Peter McCrory. [Numbers below are from the web page via WebFetch; PDF not parsed.]

**Numbers**
1. **Cadences:** personal conversations ~35% on weekdays → ~50% on weekends; news requests peak 7am local; business correspondence 10–11am; recipes 2.3× average at 6pm; tax clusters 8× more common on 14 April than an average May day. Higher-wage tasks rise on nights/weekends.
2. **Artifacts (new classifier, >30 categories):** 93% of conversations produce an identifiable artifact; explanations 17%, documents/reports 15%, guidance 11%; conversational outputs ~33%, written deliverables ~33%, code/technical ~16%. Work conversations: documents 20%, explanations 9%, email drafts 7%, analyses 6%. Coursework: documents 21%, explanations 20%, educational materials 11%, academic papers 6%. Personal: explanations 25%, recommendations 22%, documents 6%.
3. **Tokens vs wages:** top vs bottom wage tercile — tokens 2.07×; output per turn 1.34×; user turns 1.53×; extended thinking 34% vs 31%. Marketing managers ($80/hr) use ~2.5× the tokens of editors ($37/hr). 44% of the wage gradient in tokens is explained by output mix. Building apps = 3× median tokens; explanations ≈ 1/5.
4. **Autonomy:** Claude Code +0.37 points vs chat/Cowork (scripts +0.53); Opus 54% of Claude Code vs 10% of chat; same-model (Sonnet) gap 0.26; r = 0.68 between mean autonomy and median tokens. Blog/article: median 13 rounds in chat vs 1 prompt in Claude Code.
5. **Reading level:** academic papers 16+ yrs (15% at 20+); recipes/guidance <10 yrs; output exceeds prompt by ~1 yr on average (images +2.6, games +1.9, apps +1.7; blogs −0.1); r = 0.87 prompt vs output.
6. **Survey (April 2026, ~9,700 linked respondents, ≤20 sessions each, ≥5 sessions required):** Computer/Math 30% of respondents vs 4% of US employment; Management 23% vs 7%; women 12%. 60% expect a higher AI-exposure band next year; >33% expect AI to handle most/nearly all their tasks within 12 months. Reported exposure 10pp lower in high-income countries and 10pp lower for 15+ yrs experience; rises with automation share. 10% rate own job loss likely (38% of them attribute to AI); >1/3 put junior-colleague job loss >60%. Productivity gains reported: speed 86%, scope 82%, quality 69%, cost savings 27%. 68% learn more with AI; 57% say skills more valuable. Women: Claude Code share −0.24 SD (−6.3pp); automation share −0.33 SD (−7.3pp), controlling for SOC minor group.
7. Pipeline changes: higher sampling rate (hourly), window 10 Apr–10 Jun 2026, monthly aggregation, BLS OEWS May 2025 wages.

**Limitations (verbatim excerpts):** "The Anthropic Economic Index Survey is not representative of the general population"; "Accurately classifying the work that Claude does will remain a moving target"; "We can't conclusively identify the jobs of people making these requests"; "It's possible that this relationship is explained by selection..."; "These are self-assessments, and skills can erode even as they become more valuable... data do not rule out skill erosion"; binned survey scales "biased towards zero"; "Interpret the comparison of slopes qualitatively rather than as precise estimates"; "As AI capabilities increase, AIs may increasingly interact and exchange with each other, perhaps in ways inscrutable to humans or simple classifiers".

**Terminology:** "cadences", "artifacts", "reported exposure", "anticipated exposure", "observed exposure", "theoretical exposure", "Cowork", "extended thinking", "reading level".

---

## Cross-report threads (numbers side by side)

Platform key: **C** = Claude.ai (Free/Pro; Max from Aug 2025), **A** = 1P API (from Aug 2025; includes Claude Code by Feb 2026), **CC** = Claude Code (Apr 2025 only). Report key: V1 Feb 2025 (data Dec 2024–Jan 2025), V2 Mar 2025 (11 days post-3.7 Sonnet), CC-report Apr 2025 (6–13 Apr 2025), V3 Sep 2025 (4–11 Aug 2025), V4 Jan 2026 (13–20 Nov 2025), V5 Mar 2026 (5–12 Feb 2026), V6 Jun 2026 (10 Apr–10 Jun 2026).

### T1. Directive share over time
| Sample | C directive | A directive | Notes |
|---|---|---|---|
| Dec24/Jan25 (V1) | 27.8% | – | Sonnet 3.5 classifier |
| Feb/Mar25 (V2) | n/s (aug 57% unchanged) | – | Sonnet 3.7 classifier |
| Apr25 (CC) | 27.5% (coding convs only) | CC 43.8% | Claude Code feedback loop 35.8% |
| Aug25 (V3) | 39% | – (A automation 77%) | Sonnet 4; 45% automation under 3.7 re-run |
| Nov25 (V4) | 32% | 64% | "fallen 7pp"; Sonnet 4.5 |
| Feb26 (V5) | low-tenure 38.1% / high-tenure 29.4% (overall n/s in text) | "decreased sharply" (fig only) | Directive falls with tenure |
Interpretive arc: V3 conjectured rising directive = capability + learning-by-doing; V4 called the Aug spike an overstatement and pointed to product changes; V5 explicitly "pushes back against a hypothesis we made last year that automated use may be more typical of more experienced, sophisticated users".

### T2. Automation vs augmentation share by platform
| Sample | C automation / augmentation | A automation | CC automation |
|---|---|---|---|
| V1 | 42.6% / 57.4% | – | – |
| V2 | ~43% / 57% | – | – |
| CC-report (coding only) | 49% / 51% | – | 79% / 21% |
| V3 | 49% / <49% (first time auto > aug) | 77% (97% of O*NET tasks automation-dominant vs 47% on C) | – |
| V4 | 45% / 52% (3.0% unclassified) | "three-quarters" (~75%) | – |
| V5 | ~44% / ~53% (Fig 1.3, "increased slightly") | decreased "sharply" (Fig A.3, no number) | – |
| V6 | – | – | autonomy +0.37 pts vs chat; women −7.3pp automation share |
Mode-level V5 tenure split: task iteration 24.5→28.2%, learning 21.3→24.7%, validation 4.4→5.6%, feedback loop 11.7→12.1% (low→high tenure).

### T3. Task concentration (top-10 O*NET tasks) and task Gini
- C: 21% (Jan25) → ~24% (Mar25) → 23% (Aug25) → 24% (Nov25) → **19% (Feb26)**. High-tenure 20.7% vs low-tenure 22.2% (Feb26).
- A: 28% (Aug25) → 32% (Nov25) → 33% (Feb26).
- Task-share Gini (V3): C 0.84, A 0.86; bottom 80% of task categories = 12.7% (C) / 10.5% (A) of usage.
- Distinct tasks: >3,000 work tasks on C (V4); 3,258 global (country reports, Feb26); Australia 171.

### T4. Geographic concentration — AUI and Gini
| Sample | US-state Gini | Country Gini | Top-5 states share | Top-20 countries share (pop-adjusted) | Convergence horizon |
|---|---|---|---|---|---|
| Aug25 (V3) | 0.37 | 0.48 | 30% | 45% | – |
| Nov25 (V4) | 0.31/0.32 | 0.46 | 50% of raw usage vs 38% of pop | ~45% | 2–5 yrs (β≈0.76–0.77; 2SLS 0.86–0.89) |
| Feb26 (V5) | 0.29 | 0.50 | 24% | 48% | 5–9 yrs (5 weighted / 9 unweighted) |
Top-10 states 40% → 38% (Nov25 → Feb26). Country AUI: Israel 7.0, Singapore 4.57, Australia 4.10, NZ 4.05, S. Korea 3.73 (Aug25); Denmark 2.1 (Nov25); Australia 4.1 (7th), Canada 4.4 (Feb26). Income elasticity of usage per capita: 0.7 (countries, V3 & V4); 1.8 (US states, V3). Provincial/state income uncorrelated with AUI inside Australia and Canada; workforce composition (computer/math or professional-scientific-technical share) is the predictor (US: +0.36% usage per +1% tech-worker share; two-thirds of cross-state variation).

### T5. Occupational mix on Claude.ai (Computer & Mathematical share)
37.2% (V1) → ~40% (V2 peak) → 36% (V3) → 34–36% (V4) → 35% (V5, 2019 SOC). Relative change Aug25→Feb26: −18% on C, +14% on A. Educational Instruction 9.3% (V1) → 12.4% (V3) → 15–16% (V4). Management 3% → 5% (V4→V5). Business/Financial 6% → 3% and Management 5% → 3% (V1→V3).

### T6. Use-case mix (work / coursework / personal), Claude.ai
V1 paper: non-work 23%, coursework 5–10%. V4: 46 / 19 / 35. V5: 45 / 12 / 42. V5 tenure: low 41.6 / 14.1 / 44.3, high 48.9 / 10.8 / 40.3. Australia 46 / 7 / 47. Canada provinces 34–40 / 13–18 / 44–51. V6: personal ~35% weekdays → ~50% weekends. Coursework drop V4→V5 partly winter break (−5pp term-time countries vs −12pp break countries).

### T7. Economic primitives over time (Claude.ai means)
| Primitive | Nov25 (V4) | Feb26 (V5) | High tenure (V5) | Australia (Feb26) |
|---|---|---|---|---|
| Human education (yr) | 12.21 | 11.92 | 12.3 (low 11.5) | 11.9 |
| AI autonomy (1–5) | 3.38 | 3.41 | 3.40 (low 3.42) | 3.38 |
| Human-only time (min) | 185.5 | 183.8 | – | 162 (2.7 h) |
| Human+AI time (min) | 15.35 | 14.30 | – | – |
| Can't do alone (%) | 12.09 | 12.24 | – | – |
| Task success | 67% (A 49%) | – | 73.1% (low 66.7%) | – |
| Task value ($/hr) | 49.3 (A 50.4) | 47.9 (A 50.7) | – | – |
Jan25/Mar25/Aug25 Claude.ai task value ≈ $48.9 / $48.5 / $48.3 (figure-inferred). US avg wage $37.3.

### T8. Task success by tenure and by task characteristics
- Tenure (V5): raw +5pp; + task & cluster FE ≈ +3pp; + model/use-case/country FE ≈ +4pp. Table: 66.7% → 73.1%.
- Complexity (V4): C 70% (<HS) → 66% (college); A 60% (<1 h) → 45% (5+ h); 50%-success horizon A 3.5 h vs C ~19 h. Personal tasks 78% vs software dev 61%.
- Productivity adjusted for success (V4): 1.8pp → 1.2pp (C) / 1.0pp (A).

### T9. Model selection / "demand for intelligence" (first measured V5)
Opus 51% of paid C usage; +1.48pp per +$10/hr task wage on C, +2.79pp on A; Computer & Math +4.4pp, Educational −6.5pp. V6: Opus 54% of Claude Code vs 10% of chat. Cost elasticity (V3, API): −0.29 after task controls.

### T10. Depth of use / job coverage
V1: 36% of occupations ≥25% of tasks; 11% ≥50%; 4% ≥75%. V2: ~40% ≥20%, "little change". V4: 49% ≥25% (with success-weighted "effective coverage" variant). V5: 49%, "barely changed"; "many fewer novel O*NET tasks". Labor-market paper: Computer Programmers 75% covered; Computer & Math category 33% observed vs 94% theoretical; 30% of workers zero coverage.

### T11. Productivity estimates
Nov25 productivity note: 1.8pp/yr labour productivity (TFP 1.08%), median 80% time saving, median task 1.4 h, $55. V4: 1.8pp baseline; 1.2/1.0pp success-adjusted; 0.7–0.9pp at σ=0.5; 2.2–2.6pp at σ=1.5. RCT comparators 14–56%.

### T12. Classifier/vintage changes that break comparability (log for any time-series extension)
Classifier model: Sonnet 3.5 (V1) → 3.7 (V2) → Sonnet 4 (V3) → Sonnet 4.5 (V4, V5). Filtering: occupational-relevance filter (V1) → safety-flag filter (V2+). O*NET vintage: 2010 (V1–V4) → 2019 SOC (V5 occupational figures). Platforms: Free/Pro (V1–CC) → +Max and 1P API (V3+) → API includes Claude Code (V5) → chat/Cowork vs Claude Code split, hourly sampling (V6). Sample windows: one week each except V2 (11 days), V6 (two months). Confounds noted by authors: Super Bowl ads (V5), winter break (V5), Utah abuse (V3), product changes — file creation, memory, Skills (V4).

### T13. Recurring open questions (candidate falsifiable extensions)
1. Learning-by-doing vs cohort/survivorship (V5: "Over time, we will be able to more cleanly isolate..."). Testable with signup-cohort × calendar-time panels once ≥2 pulls with tenure exist.
2. Whether directive/automation rises with capability (V3 hypothesis) or falls with product-driven collaboration (V4) — V5 tenure split suggests the sophisticated-user→automation link is wrong on C; A moves opposite.
3. Migration of tasks C → A as a leading indicator of "more imminent transformation of work" (V5) — test against observed-exposure changes and BLS/CPS outcomes (labor-market paper's DiD framework; detectable effect ≈ 1pp unemployment).
4. Selection in observed success rates (V4): "users may respond to new models by providing more challenging presentations" — testable around the Opus 4.5/4.6 release straddled by V5.
5. Income vs workforce composition as adoption driver: strong cross-country (0.7 elasticity), null within Australia (8 states) and Canada (provinces), composition explains two-thirds of US-state variance.
6. Convergence slowdown (2–5 → 5–9 years) — was the V4 estimate attenuated by sampling noise (their 2SLS concern) or is diffusion decelerating?
7. Artifact paradox (Education report): direction ↑, evaluation ↓ when artifacts are produced; unresolved whether evaluation moves off-platform. Links to V6 finding that 93% of conversations produce artifacts.
8. Task value drift: C falling ($48.9 → $47.9 since V1), A rising — is the "adoption curve" story (later adopters, cheaper tasks) separable from coding migration?
