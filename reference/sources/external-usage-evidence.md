# External usage evidence: other providers and key academic papers

Evidence log for posts extending Anthropic's Economic Index. Compiled 7 September 2026.
Every number below was read from the source text (PDF converted with pdftotext, or the HTML page) unless
marked [NOT FETCHED]. Quotes are verbatim; paraphrases are marked as such. Where two versions of a paper
give different numbers, both are logged with their dates.

Local copies of every PDF read for this log are in the session scratchpad
(`/private/tmp/claude-501/-Users-emilybirch-Desktop-Anthropic/d0dd900a-348c-43aa-b607-a2f548570fae/scratchpad/pdf/`).

Legend for the five evidence dimensions requested:
(a) cross-country use and income; (b) gender; (c) occupation exposure/applicability and data availability;
(d) automation vs augmentation / asking vs doing; (e) stated limitations.

---

## 1. Chatterji, Cunningham, Deming, Hitzig, Ong, Shan, Wadman — "How People Use ChatGPT"

- **Authors:** Aaron Chatterji (Duke/OpenAI), Thomas Cunningham (OpenAI), David J. Deming (Harvard/NBER), Zoe Hitzig (OpenAI/Harvard), Christopher Ong (Harvard/OpenAI), Carl Yan Shan (OpenAI), Kevin Wadman (OpenAI)
- **Date:** NBER Working Paper 34255, September 2025
- **URL:** https://www.nber.org/papers/w34255 (PDF: https://www.nber.org/system/files/working_papers/w34255/w34255.pdf) — fetched, 64 pp.
- **Data:** consumer plans only (Free, Plus, Pro; excludes Business/Enterprise/Edu). Growth dataset Nov 2022–Sept 2025. Classified sample: "approximately 1.1 million conversations", one message each, 15 May 2024–26 June 2025 (some analyses to 31 July 2025), excluding opted-out users, self-reported under-18s, deleted/banned accounts and logged-out users. Employment/education for "approximately 130,000" users via a data clean room with a 100-user aggregation floor; regressions use "approximately 40,000 users" with a non-blank public occupation. Classifiers: gpt-5-mini (gpt-5 for Interaction Quality), validated against WildChat. "No member of the research team ever saw the content of user messages."
- **Scale:** "By July 2025, 18 billion messages were being sent each week by 700 million users, representing around 10% of the global adult population." "more than 2.5 billion messages per day, or about 29,000 messages per second."

### (a) Cross-country use and income
- Measure: "the proportion of weekly consumer ChatGPT users among the internet enabled population of countries with populations larger than 1 million", excluding countries where ChatGPT is blocked; countries ranked into GDP-per-capita deciles (World Bank 2023), May 2024 vs May 2025 (Figure 21).
- Finding (text; the figure carries no printed values): "Comparing May 2024 to May 2025, we see that the adoption of ChatGPT grew dramatically, but also that there was disproportionate growth in low to middle-income countries ($10,000–40,000 GDP-per-capita). Overall, we find that many low-to-middle income countries have experienced high growth in ChatGPT adoption."
- Abstract wording: "we find higher growth rates in lower-income countries". Conclusion wording: "ChatGPT usage has grown especially fast over the last year in low- and middle-income countries."
- Note: growth is measured as change in penetration share, not as delegation/task mix; no country-level task or intent breakdown is reported.

### (b) Gender
- Method: first names of "a global random sample of over 1.1 million ChatGPT users" classified with the World Gender Name Dictionary, US Social Security names, and Brazilian/Latin American name lists; ambiguous names "classified as Unknown" and excluded from the denominator.
- "Excluding Unknown, a significant share (around 80%) of the weekly active users (WAU) in the first few months after ChatGPT was released were by users with typically masculine first names. However, in the first half of 2025, we see the share of active users with typically feminine and typically masculine names reach near-parity. By June 2025 we observe active users are more likely to have typically feminine names."
- Introduction: "that number declined to 48% as of June 2025, with active users slightly more likely to have typically feminine first names." Conclusion: "As of July 2025, more than half of weekly active users had typically female first names."
- Topic differences: "Users with typically female first names are relatively more likely to send messages related to Writing and Practical Guidance. By contrast, users with typically male first names are more likely to use ChatGPT for Technical Help, Seeking Out Information, and Multimedia (e.g., modifying or creating images)." (Figure 19; no magnitudes printed in text.)
- Caveat flagged by Cranney/Delecourt/Koning (item 5): the unknown-name share is "roughly 20–30% of active accounts over much of the sample", the sample is consumer accounts only, and parity among consumer accounts "does not imply parity in the broader population".

### (c) Occupation
- Occupation groups (privacy-coarsened): nonprofessional (SOC 31–53), computer-related (SOC 15), engineering and science (SOC 17, 19), management and business (SOC 11, 13), other professional (SOC 21–29).
- Work share of messages by occupation (unadjusted): "57% for computer-related occupations; 50% for management and business; 48% for engineering and science; 44% for other professional occupations; and only 40% for all non-professional occupations."
- Work share by education: "37% of messages are work-related for users with less than a bachelor's degree, compared to 46% for users with exactly a bachelor's degree and 48% for those with some graduate education. Those differences are cut roughly in half after adjusting for other characteristics".
- Topic within work by occupation: Writing "52% of all work-related messages" for management and business; 50% nonprofessional; 49% other professional. Technical Help "37% of all work-related messages for users employed in computer-related occupations, compared to 16% in engineering and science and only about 8% for all other categories."
- Age: "around 46% of the messages in our dataset are accounted for by users 18-25" (among self-reporters). Work share "approximately 23% of messages for users under age 26", rising with age, except 66+ at 16%.
- O*NET GWAs, all messages: Getting Information 19.3%, Interpreting the Meaning of Information for Others 13.1%, Documenting/Recording Information 12.8%, Providing Consultation and Advice 9.2%, Thinking Creatively 9.1%, Making Decisions and Solving Problems 8.5%, Working with Computers 4.9% (seven = 76.9%).
- Work-related messages (approx. 366,000): Documenting/Recording Information 18.4%, Making Decisions and Solving Problems 14.9%, Thinking Creatively 13.0%, Working with Computers 10.8%, Interpreting the Meaning of Information for Others 10.1%, Getting Information 9.3%, Providing Consultation and Advice 4.4% ("nearly 81%").
- "Making Decisions and Solving Problems is one of the two most common GWAs in every single occupation group where at least two GWAs can be reported."
- Downloadable data: no occupation-level file released; "A repository containing all code run to produce the analyses in this paper is available on request." Appendix D gives GWA x 2-digit SOC counts. A 100,000-message WildChat classification is in the replication package.

### (d) Asking / Doing / Expressing; work vs non-work
- Definitions (classifier prompt): Asking = "seeking information or advice that will help the user be better informed or make better decisions"; Doing = "request that ChatGPT perform tasks for the user ... output that is created primarily by the model"; Expressing = "neither asking for information, nor for the chatbot to perform a task". Framing: "Doing conversations are delivering output that can be plugged into a production process, while Asking conversations support decision-making but do not produce output directly".
- Overall split (May 2024–June 2025 sample): "49% of user messages are Asking, 40% are Doing, and 11% are Expressing."
- Trend: "In July 2024, usage was evenly split between Asking and Doing, with just under 8% of messages classified as Expressing ... by late June 2025 the split was 51.6% Asking, 34.6% Doing, and 13.8% Expressing."
- Work-related messages: "Doing constitutes nearly 56% of work-related queries, compared to 35% for Asking and 9% for Expressing. Nearly 35% of all work-related queries are Doing messages related to Writing."
- Occupation gradient in Asking at work: "47% of the work-related messages sent by users employed in computer-related occupations are Asking messages, compared to only 32% for non-professional occupations." Education: graduate-degree users "about two percentage points more likely" to send Asking messages after adjustment (5% level) and "about 1.6 percentage points less likely to send Doing messages" (10% level).
- Quality: "Asking messages are substantially more likely to receive a good rating than Doing or Expressing messages." Good:bad ratio rose from about 3 (late 2024) to "more than four times" (July 2025).
- Work vs non-work (Table 1, 7-day averages): June 2024: non-work 238M/day (53%), work 213M/day (47%), total 451M; June 2025: non-work 1,911M (73%), work 716M (27%), total 2,627M. "The decrease in the share of work-related messages is primarily due to changing usage within each cohort of users rather than a change in the composition of new ChatGPT users."
- Topics: Practical Guidance, Seeking Information, Writing = "about 77%" of all conversations (abstract: "nearly 80%"; conclusion: "nearly 78%"). Practical Guidance ~29% throughout; Writing fell from 36% (July 2024) to 24% (July 2025); Seeking Information rose 14% to 24%; Technical Help fell 12% to ~5%; Multimedia rose 2% to just over 7%. Computer Programming 4.2% of all messages (vs "33% of work-related Claude conversations Handa et al. (2025)"); Relationships and Personal Reflection 1.9%; Games and Role Play 0.4%; Tutoring or Teaching 10.2%. Within work: Writing ~40% (July 2025; "42%" in conclusion), Practical Guidance 24%, Technical Help down from 18% to just over 10%. "About two-thirds of all Writing messages ask ChatGPT to modify user text ... rather than creating new text from scratch."

### (e) Stated limitations
- Consumer plans only; business/enterprise/edu users excluded (footnote 27).
- Employment data "only available for a subset of users the results may not be representative of the full pool of users."
- Classifiers infer intent: "we never directly observe the ground truth."
- Gender is imputed from first names; "Unknown" excluded.
- Logged-out users dropped for consistency.
- Cohort growth attributed to "(1) improvements in the capabilities of the models, and (2) users slowly discovering new uses" — an interpretation, not an identification.

---

## 2. Tomlinson, Jaffe, Wang, Counts, Suri (Microsoft) — "Working with AI: Measuring the Applicability of Generative AI to Occupations"

- **Authors:** Kiran Tomlinson, Sonia Jaffe, Will Wang, Siddharth Suri (Microsoft Research); Scott Counts (Microsoft)
- **Date:** arXiv:2507.07935, first posted July 2025; version read is v6, 22 December 2025 (title changed from "...Occupational Implications..." to "...Applicability of Generative AI to Occupations")
- **URL:** https://arxiv.org/abs/2507.07935 (PDF fetched, 40 pp.); data: https://github.com/microsoft/working-with-ai (fetched)
- **Data:** "200k anonymized conversations with Microsoft Bing Copilot", US only, 1 January–30 September 2024: ~100k uniform sample plus ~100k sampled from conversations with a thumbs up/down. O*NET 29.0 IWAs; BLS OEWS May 2023 employment/wages; CPS 2024.

### User goal vs AI action (the paper's core distinction)
- "First, the user is seeking assistance with a task they are trying to accomplish; we call this the user goal ... Second, the AI itself performs a task in the conversation, which we call the AI action." Example: user goal "operate office equipment", AI action "train others to use equipment".
- "these sets of IWAs are disjoint in 40% of conversations, and in 96%, there are more IWAs unique to a side than in common." "for every work activity matched to a user goal the AI performs an average of two work activities" (about 3 user-goal IWAs and 6 AI-action IWAs per conversation).
- Most common user goals: "learning, communicating, teaching/explaining, and writing". AI actions: "Provide, Explain, Teach, Assist, and Respond ... A majority of AI-side activity is devoted to communicating and teaching/explaining information to the user."
- Interpretation: high AI-action applicability = "delegating some tasks to AI"; high user-goal applicability = "performing the same tasks but in collaboration with AI". Media and financial operations occupations "more likely to delegate tasks to AI"; food preparation and serving more "assistive". "Occupations with high AI applicability to user goals, such as computer and mathematical occupations, may see more active AI usage by workers".
- Explicit warning: "It is tempting to conclude that occupations that have high AI action applicability score will be automated and thus experience job or wage loss ... This would be a mistake". ATM/bank-teller example given.

### AI applicability score construction
- Three success metrics: completion (LLM classifier; "Completion is highly correlated with direct user feedback (weighted r > 0.75)"), user feedback (thumbs), scope (six-point scale none/minimal/limited/moderate/significant/complete; share of conversations at "moderate or higher").
- Coverage: an IWA is "covered" if its activity share is at least 0.05% (threshold 0.0005) — "chosen ... to minimize the number of occupations with no or all IWAs covered"; ranking "robust to the chosen coverage threshold".
- Equation (1): a_i^user = sum over IWAs j of 1[f_j^user >= 0.0005] * c_j^user * s_j^user * w_ij, where f = activity share, c = completion rate, s = share with scope >= moderate, w_ij = importance/relevance weight (weight_ik = 2^importance * relevance summed over tasks). AI-action side uses non-physical task weights (GPT-5 labels whether a task requires "touching or moving people or objects"). Reported score = (a^user + a^AI)/2.
- The authors argue against "x% of tasks impacted" headline numbers: "by picking different usage thresholds, we can conclude that either ~0% or ~100% of the workforce has 50% of its importance-weighted tasks represented in our data" — so use the score for relative comparisons only.

### (c) Top and bottom occupations; downloadability
- Top detailed occupations (Figure 2 / CSV): Interpreters and Translators 0.492; Historians 0.462; Writers and Authors 0.454; Sales Representatives of Services 0.449; CNC Tool Programmers 0.419; Broadcast Announcers and Radio DJs 0.409; Customer Service Representatives 0.408; Telemarketers 0.404; Political Scientists 0.391; Mathematicians 0.386; then Journalists 0.383, Passenger Attendants 0.376, Technical Writers 0.373, Concierges 0.372, Proofreaders 0.369, Editors 0.367, Business Teachers 0.367, Web Developers 0.353, Geographers 0.352, Brokerage Clerks 0.35.
- Bottom (from CSV, score 0.0): Orderlies; Floor Sanders and Finishers; Pile Driver Operators; Rail-Track Laying and Maintenance Equipment Operators; Foundry Mold and Coremakers; Water and Wastewater Treatment Plant and System Operators; Bridge and Lock Tenders; Dredge Operators; then Motorboat Operators 0.003, Logging Equipment Operators 0.005.
- SOC minor groups (Table 1): top Media and Communication Workers 0.38, Sales Representatives (Services) 0.35, Information and Record Clerks 0.33, Mathematical Science 0.32, Tour and Travel Guides 0.32, Postsecondary Teachers 0.31; Computer Occupations 0.29; Top Executives 0.11; bottom Personal Appearance Workers 0.06, Agricultural Workers 0.06, Other Construction and Related Workers 0.06, Firefighting 0.07, Construction Trades 0.07, Material Moving 0.07.
- **Downloadable: YES.** `ai_applicability_scores.csv` (columns `SOC Code, title, ai_applicability_score`; 785 detailed 2018 SOC codes covering "149.8 million workers"; e.g. Chief Executives 0.1555). Also `soc_metrics.csv` (completion, impact_scope, feedback, coverage, user/AI sub-scores), `iwa_metrics.csv`, `soc_iwa_weights.csv`, `soc_iwa_nonphysical_weights.csv`, `soc_to_iwas.csv`, `physical_tasks.csv`. Licence CC BY 4.0 per GitHub page. v1.1 matches arXiv v6; v1.0 tag matches v1–v5. Military SOC 55-xxxx and 74 SOC codes without O*NET task data omitted. Raw conversations not released.

### Correlation with prediction-based measures; wages/education
- "The employment-weighted occupation-level correlation between their [Eloundou et al. (2024) E1] predictions and our AI applicability score is r = 0.73 (Figure S12)."
- Wage: "only a weak relationship between AI applicability score and wage (employment-weighted r = 0.13; Figure S13A), while previous work found strong positive correlations". Without employment weighting r rises to "0.17 for user goals and 0.32 for AI actions". "a broad range of AI applicability across educational requirements".
- Scope correlates with log user activity share, r = 0.64.

### (d) Automation vs augmentation
- The user-goal/AI-action split is their operationalisation; no employment claims. See quote above.

### (e) Stated limitations
- "Our task completion and scope metrics are measures of AI's utility towards an IWA, but they do no[t] capture the productivity impact"; work activities may mean different things in an occupation vs in Copilot; "only one slice of the AI market"; task decomposition omits "the connecting glue between tasks"; O*NET is "U.S.-centric", "may lag", and excludes non-occupational work (home, volunteering).
- (Not stated as such, but material) No user demographics; US-only; free Bing Copilot in Jan–Sept 2024.

---

## 3. Bick, Blandin, Deming — "The Rapid Adoption of Generative AI"

- **Authors:** Alexander Bick (FRB St. Louis & CEPR), Adam Blandin (Vanderbilt), David J. Deming (Harvard Kennedy School & NBER)
- **Versions:** NBER Working Paper 32966, September 2024, revised February 2025 (NBER page fetched; PDF not read); FRB St. Louis Working Paper 2024-027F, revision dated 27 October 2025 (PDF fetched, 53 pp.) — this is the version logged in detail; also SSRN 4965142; Management Science (doi 10.1287/mnsc.2025.02523) [NOT FETCHED]. 2026 quarterly RPS update cited by Federal Reserve FEDS Note "Monitoring AI Adoption in the U.S. Economy", 3 April 2026 (fetched).
- **URLs:** https://www.nber.org/papers/w32966 ; https://s3.amazonaws.com/real.stlouisfed.org/wp/2024/2024-027.pdf ; https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html
- **Data:** Real-Time Population Survey (RPS), ages 18–64, August and November 2024 waves, "more than 10,000 respondents"; questions adapted from the CPS Computer and Internet Use supplement. Cross-check via SWAA December 2024 (46.5% overall vs 45.5% RPS; 33.3% vs 32.1% work).

### Headline adoption
- NBER Sept 2024/Feb 2025 abstract: "Nearly 40 percent of the U.S. population age 18-64 uses generative AI"; "23 percent of employed respondents had used generative AI for work at least once in the previous week"; "9 percent used it every work day"; "Between 1 and 5 percent of all work hours are currently assisted"; "time savings equivalent to 1.4 percent of total work hours". Footnote in Chatterji et al.: "Bick et al. (2024) report that 28% of US adults used ChatGPT in late 2024".
- Oct 2025 version (pooled Aug+Nov 2024): "45.5% of respondents report using genAI either at work or at home: 10.4% used it every day, 26.7% used it some but not all days, and 8.3% did not use it in the last week." Work: "32.1% of workers used genAI at work: 10.5% used it every work day and 16.7% on some but not all workdays, bringing total weekly usage to 27.2%." Home: 37.7% overall, 5.6% daily. Abstract: "Between 1 and 7% of all work hours are currently assisted by generative AI"; "the average genAI user would need to work 5.2% more hours ... implying 1.4% time savings across all workers".
- 2026 update (FEDS note citing Bick, Blandin, Deming 2026, RPS GenAI module quarterly since Aug 2024): November 2025 work-related adoption 40.7% ("about 41 percent of the workforce"; +9.7 pp, +31.3% YoY); "at least once last week" 35.2% (+8.9 pp); daily 12% (+2.9 pp); non-work use "about 50 percent of the population" (+10.4 pp, +26% YoY). No demographic split in the note.

### Comparison with PC and internet (Figure 2, Oct 2025 version)
- Reference dates: IBM PC August 1981 -> CPS CIU 1984 (three years); ChatGPT November 2022 -> RPS fall 2024 (two years).
- GenAI 2024 vs PC 1984: Overall 45.5% vs 19.7%; At Work 32.1% vs 25.1%; At Home 37.7% vs 5.5%. Internet: "in 1995 the internet was opened to commercial traffic ... Two years later, 21% of US adults reported access to the internet according to the International Telecommunication Union". Abstract: "work adoption of generative AI has been as fast as the personal computer (PC), and overall adoption has been faster than either PCs or the internet."

### (b) Gender, age, education (work adoption, employed 18–64, N = 6,935; Figure 3, Oct 2025 version)
- Men 35.0% (11.8 daily / 18.1 weekly / 5.1 not last week); Women 29.0% (9.2 / 15.2 / 4.6). Text: "genAI adoption is 6 percentage points higher for men."
- Age 18–29 34.6%; 30–39 36.9%; 40–49 35.7%; 50–64 22.6%.
- Less than college 23.7%; Bachelor's 41.1%; Graduate 47.5% ("roughly twice the rate of non-college educated workers").
- Regression (Table 1, use last week): Female coefficient −0.070*** (demographics only) -> −0.048*** (adding occupation and Eloundou exposure) -> −0.018* (adding employer encouragement). Demographics explain 8% of variation; occupation + exposure raise it to 12%.
- Cranney et al. (item 5) quote the 2024 NBER version as "29.1% of employed men versus 23.5% of employed women used generative AI for their job" — not verified in the Oct 2025 text; log as quoted-by-secondary.

### (c) Occupation and predicted exposure
- Work adoption by occupation: computer and mathematical 54%, management 52%, business and finance 48%; blue collar 26%, office and administration 23%, personal services 16%; "genAI adoption exceeds 20% in all but one occupation groups".
- Correlation of occupation-group adoption with Eloundou et al. (2024) predicted exposure "ρ = 0.65"; with Felten et al. (2021) "ρ = 0.71". Correlation with share saying "GenAI cannot help me with my job" −0.88 (7% in computer/math vs 30% in personal services); with share citing adoption barriers −0.30. "office and administrative occupations and managers are predicted to be similarly exposed to genAI, but actual adoption by managers is more than double that of office and administrative workers."
- Employer encouragement: "86% of respondents whose employer encourages genAI use report adopting it, compared to just 13% among those whose employer does not."

### (d) Automation vs augmentation
- Not measured; the survey asks about tasks assisted and time saved, not intent type.

### (e) Stated limitations
- "our measurement approach ... will only capture genAI use that respondents are aware of ... we interpret our estimates a lower bound".
- Self-reported adoption (Chatterji et al. note "there are reasons to expect bias in self-reports").
- Introduction dates for PC/internet chosen "based in part on ChatGPT's answers"; earlier PC dates "would imply slower adoption rates".

---

## 4. Humlum & Vestergaard — "The Adoption of ChatGPT" / "The unequal adoption of ChatGPT exacerbates existing inequalities among workers"

- **Authors:** Anders Humlum (University of Chicago Booth & IZA), Emilie Vestergaard (University of Copenhagen)
- **Versions:** IZA DP No. 16992, May 2024 (PDF fetched, 92 pp.; https://docs.iza.org/dp16992.pdf); PNAS 122(1), published January 2025, doi 10.1073/pnas.2414972121 (full text read via PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11725873/)
- **Data:** Denmark, Statistics Denmark survey of "100,000 workers from 11 exposed occupations" (accountants, customer support specialists, financial advisors, HR professionals, IT support specialists, journalists, legal professionals, marketing professionals, office clerks, software developers, teachers), November 2023–January 2024, linked to register data; IZA: "29% response rate"; PNAS: "about 18,000 valid and complete responses". Occupations = "21% of total employment in Denmark". Pre-registered RCT AEARCTR-0012527.

### Adoption levels
- IZA: "half of workers have used the technology, with adoption rates ranging from 79% for software developers to 34% for financial advisors"; "32% currently using it and 6% having a Plus subscription"; of users "72% have used it at work". PNAS: "41% of workers have used the tool for work" (per PMC extraction); "more than half of workers have used it".
- Extrapolation: "a lower bound on economy-wide use of ChatGPT is 10%"; using Eloundou et al. exposure ratios "implies 31% (22%) of workers in Denmark have used ChatGPT (at work)".

### (b) Gender gap — exact figures
- IZA (any use of ChatGPT): "women are 20 percentage points less likely to use ChatGPT than men in the same occupation." Table A.2 Female coefficients: −0.262 (raw, N 18,088) -> −0.204 (occupation FE) -> −0.191 (+ task-importance FE, 330 FEs) -> −0.170 (+ workplace FE, N 14,426) -> −0.170 (+ beliefs) -> −0.161 (+ worker characteristics). Text: "comparing workers within the same workplace and controlling for workers' detailed task mixes shrinks the gender gap from 20 to 17 percentage points". "The gender gap persists when we compare coworkers within the same workplace and control for workers' detailed task mixes." "Figure 1 shows the gender gap is pervasive across occupations."
- PNAS (use for work): "Women are 16 percentage points less likely to have used the tool for work" than men in the same occupation. PNAS Table 1: "Women are about 16 percentage points less likely to use ChatGPT than men in the same occupation." Controls: "controlling for workers' other characteristics in Column (6), the gender gap shrinks only slightly to 14 percentage points" and "comparing workers within the same workplace and controlling for workers' detailed task mixes in Column (7), the gender gap shrinks to 12 percentage points. Put differently, the lower use of ChatGPT among female workers is not primarily because they specialize in different job tasks". "The gender gap is pervasive in all occupations, exists in various adoption measures, and persists when comparing coworkers within the same workplace handling the same types of job tasks."
- Beliefs: "The gender gap in adoption does not reflect differences in beliefs, as women are about as optimistic as men about the productivity of ChatGPT". Women "are less confident in their priors about ChatGPT" and are more swayed by the information treatment: "women are 9.8 pp. and 13.6 pp. more responsive to the information than men with similar levels of prior confidence" (IZA, Table A.8). "the gender gap in adoption does not reflect women are less responsive to information about the technology. On the contrary, women respond more to the information but face barriers that prevent their further adoption."
- Barriers by gender: "women report they need training to use ChatGPT ... By contrast, men's use of ChatGPT is more limited by employer restrictions and data confidentiality." "men are more likely to sign up for our information sheets ... simply offering workers introductory material is unlikely to close the gender gap in adoption."

### Barriers and beliefs (all workers)
- IZA: "43% of workers report they need training to use ChatGPT, and 35% report employers actively restrict their usage"; existential fears "less than 10%". PNAS (PMC extraction): "42% of the workers report they need training", "36% report employers actively restrict their usage". "82% of financial advisors face an adoption friction, 37% of software developers".
- Productivity beliefs: "the average worker estimates that ChatGPT can halve working times in about a third of his job tasks" (IZA: "37% of the job tasks for the typical worker"); "38% reporting they will not perform more of the tasks ChatGPT saves time completing". PNAS: among non-users who believe in substantial savings, "only about 23% plan to use it within the next 2 wk".
- Age/experience: IZA "every year of age and experience is associated with a 1.0 and 0.7 percentage point lower likelihood"; PNAS "0.7 and 0.6 percentage point". Users "earned slightly more already before its arrival"; +1 SD high-school GPA +2.1 pp adoption.
- Information experiment: "shifts workers' beliefs and intentions but has limited impacts on actual adoption" (PNAS: "muted effects on workers' intended use" and "no effects on their actual use" within two weeks).

### (c)/(d)
- Exposure taken from Eloundou et al. (2023) adapted to Danish tasks; "Workers and experts agree on the exposure rankings of 78% of the job tasks." No automation/augmentation or asking/doing measure.

### (e) Stated limitations
- Eleven occupations only; self-reported use; short (2-week) follow-up for the experiment; sample representativeness handled by reweighting and randomized incentives ("robust to reweighing the sample ... and to using randomized participation incentives").

---

## 5. Cranney, Delecourt, Koning (earlier with Otis) — "Global Evidence on Gender Gaps and Generative AI (Over Time)"

- **Authors:** Original (October 2024): Nicholas G. Otis, Solène Delecourt, Katelyn Cranney, Rembrand Koning (per HKS CID listing). Revision (May 2026): Katelyn Cranney (Stanford), Solène Delecourt (Berkeley Haas), Rembrand Koning (HBS) — Otis no longer listed.
- **Versions/URLs:** HBS Working Paper 25-023. Original PDF https://www.hbs.edu/ris/Publication%20Files/25023_52957d6c-0378-4796-99fa-aab684b3b2f8.pdf [NOT FETCHED — server returned an error page]; abstract of the original read from https://www.hks.harvard.edu/centers/cid/publications/global-evidence-gender-gaps-and-generative-ai (fetched). Revision PDF https://www.hbs.edu/ris/Publication%20Files/25-023_be8fb517-3dd5-40aa-97f9-4e42e1c8e6ff.pdf (fetched, 65 pp., dated May 2026). SSRN 6880085 returned 403. HBS AI Institute summary page fetched.

### Original (October 2024) version — from abstract
- "18 studies covering more than 140,000 individuals worldwide"; "Women are adopting generative AI at roughly 20 percent lower rates than men" (HBS AI Institute/search summary); gaps "remain even when access to try this new technology is equalized"; hold "across nearly all regions, sectors, and occupations".

### May 2026 revision — meta-analytic numbers
- Systematic review: "76 sources from over 100 countries" (as of 28 May 2026); 58 report adoption by gender, 54 with exact denominators; "318,924 respondents or observed users".
- "sample-size-weighted men's adoption is 47.8% and women's is 39.3%, a gap of 8.5 percentage points. In relative terms, men are about 22% more likely than women to report using AI" (relative gap 21.7%; unweighted 54.2% vs 44.4%).
- Direction: "the raw gender gap is positive in 56 sources and negative in 2"; range "from a 23.6-percentage-point gap favoring men to a 3.0-percentage-point gap favoring women".
- Trend: 2023 gaps "from 5 percentage points to nearly 25"; March 2026 gaps "from around 3 to 13 percentage points". Since early 2025 (16 source-outcome entries, N = 113,981): men 39.8%, women 34.4%, "absolute gap is 5.4 percentage points and the relative gap is ... ≈ 15.7%" — "stabilized at roughly 16% since early 2025".
- Within-occupation/firm evidence cited: software engineers at one global tech firm 43% men vs 31% women used internal AI coding tool (Gai, Hou, Tu 2025); Swiss clinicians 37.4% vs 26.5% frequent LLM users; UK journalists 36% vs 30% weekly professional use; Norwegian business students 75.7% vs 60.7%; US liberal-arts undergraduates 88.7% vs 78.4%; Danish workers "16 percentage points less likely than men in the same occupation" (Humlum & Vestergaard 2025); Anthropic survey of quantitative social scientists Feb–Mar 2026: 81% male-name vs 78% female-name respondents ever used genAI for research, but "22% of respondents with typically male names reported using [coding agents] more than once a week, while only 9% of respondents with typically female names" (= "144% more likely").
- Web traffic (SimilarWeb, top-10 AI sites, Jan 2023–Jan 2026, 59 countries): female share "just under 35%" in Jan 2023 to "about 40%" by Jan 2026, "stable at 40% since October 2024". Largest gaps "Pakistan, India, Iraq, and South Korea, where women's share ... remain below 35%"; closest to parity "Hungary, Japan, Ukraine, Hong Kong, and New Zealand". US tool-level female share Aug 2025–Jan 2026: 26.7% (grok.com) to 44.1% (chatgpt.com); global chatgpt.com "approximately 45%".
- Intensity: women's visits shorter on chatgpt.com 8.9%, gemini 10.7%, grok 15.9%, perplexity 13.9%, copilot 4.9%, deepseek 8.9%; longer on character.ai (+9.8%) and polybuzz.ai (+11.6%). ChatGPT US Jan 2023–Jan 2026: women's visits "10.4% shorter ... about 33 fewer seconds per visit", "no consistent indication of narrowing". Zahs et al. (2026): women use genAI "about 17.5 fewer minutes per day at work".
- Mechanisms organised into five frictions: knowledge/familiarity; perceived usefulness; institutional support, training and confidence; social legitimacy and status costs; trust, privacy and risk. UK training pilot (Public First & Google 2025): women's daily and weekly use rose "sharply" after short hands-on training.
- Reconciliation with Chatterji et al.: consumer-account, active-week, name-classified sample "does not imply parity in the broader population"; illustrative calculation that omitted enterprise/logged-out users could make the population "only 41.7% female".

### (e) Stated limitations
- Sources differ in sampling frame, use definition and geography; SimilarWeb gender is imputed and smaller countries "have smaller traffic volume and therefore ... noisier gender estimates"; traffic data cannot see why a user avoids AI; potential publication bias toward early-adoption/high-income settings.

---

## 6. Brynjolfsson, Chandar, Chen — "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence"

- **Authors:** Erik Brynjolfsson (Stanford & NBER), Bharat Chandar (Stanford), Ruyu Chen (Stanford), Stanford Digital Economy Lab
- **Versions/URLs:** August 2025 original [NOT FETCHED as a distinct file — the 2025/08 URL now serves the 13 November 2025 revision, which was read, 65 pp.]; 13 November 2025 revision (https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf, fetched); August 2026 revision (https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf, fetched, 140 pp.). Landing page: https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
- **Data:** ADP payroll records; Nov 2025 version "monthly, individual-level payroll records through September 2025", "between 250,000 and 350,000 employed individuals in each month just between the ages of 22 and 25"; Aug 2026 version balanced firm panel Jan 2021–June 2026, "between 3.5 and 5 million employees per month", full-time under-70s. Occupations from ADP job-title taxonomy (2010 SOC); "Job titles are missing for roughly 30% of the sample".
- **Exposure measures:** Eloundou et al. (2024) GPT-4 β ratings; Anthropic Economic Index (Handa et al. 2025), March 2025 release for main results, with Sept 2025, Jan 2026 and April 2026 releases in appendix; alternatives from Brynjolfsson et al. 2018, Felten et al. 2021/2023, Tomlinson et al. 2025.

### The headline decline for 22–25-year-olds
- Version history stated in the Aug 2026 paper: "Earlier versions of this study headlined regression estimates adjusting for firm-level shocks (a 13% relative decline as of July 2025 data; 16% as of September 2025 data). We now emphasize the simpler descriptive divergence ... the kept-pace shortfall was 15% at the July 2025 data vintage and has since widened to 19% as of June 2026."
- Nov 2025 abstract: "Early-career workers (ages 22-25) in AI-exposed occupations experienced 16% relative employment declines, controlling for firm-level shocks, while employment for experienced workers remained stable." Levels: "workers aged 22 to 25 have experienced a 6% decline in employment from late 2022 to September 2025 in the most AI-exposed occupations, compared to a 6-9% increase for older workers." Firm-time event study: "a 15 log-point decline in relative employment for the most AI-exposed quintiles compared to the least exposed quintile".
- Aug 2026 abstract: "employment of young workers (ages 22–25) in AI-exposed occupations now stands 19% below where it would be had it kept pace with that of their less-exposed peers". Levels: "employment of 22–25-year-olds in the two most exposed quintiles fell about 11% between November 2022 and June 2026, while employment of the same age group in the three least-exposed quintiles grew about 10%." Operates "primarily through reduced hiring ... rather than increased separations". "(6) Adjustment is occurring through employment rather than base compensation."

### (d) Automation vs augmentation using the Anthropic Economic Index
- Definition used: AEI "reports estimates of the share of queries pertaining to that task that are 'automative,' 'augmentative,' or none of the above." Footnote: "Directive and Feedback Loop conversations are considered Automative; Task Iteration, Learning, and Validation are considered Augmentative. They also instruct the model to choose None of the above 'liberally.'" Aug 2026 version renames augmentative as "complementary usage" because "(labor-)augmenting technical change has a distinct formal meaning" in growth theory.
- Nov 2025 Fact 3: "the occupations with the highest estimated automation shares have experienced declining employment for the youngest workers. In contrast ... the occupations with the highest estimated augmentation shares have not experienced a similar pattern. Employment changes for young workers are not ordered by augmentation exposure, as the fifth quintile has among the fastest employment growth."
- Usage levels by quintile (both versions): first two augmentation quintiles "very low Claude usage (0.01% and 0.09% of conversations for the average occupation, respectively)"; third–fifth "0.47%, 0.39%, and 0.33%"; automation: lowest group 0.05%, highest 0.73%.
- Aug 2026 Table 3 (occupation-level long-difference, % change in employment Nov 2022–June 2026 on standardized exposures, March 2025 AEI): ages 22–25 automation −0.098*** (0.018), complementarity 0.016 (0.021), overall usage −0.029 (0.018); 26–30 automation −0.036***; 41–49 complementarity +0.024**; 50+ complementarity +0.015*, overall usage −0.037**. Pooled Sept 2025/Jan 2026/Apr 2026 releases: 22–25 automation −0.084*** (0.014), complementarity −0.010. Text: "only the automation coefficient is negative and statistically significant—about −0.10 per standard deviation for 22–25 year-olds—and it shrinks monotonically with age ... This age gradient—automation associated with declines for the young, complementarity with gains for the experienced—is the paper's most direct evidence on mechanism."

### (b) Gender (Aug 2026 only)
- "Women work in more AI-exposed occupations than men at every age, in the ADP analysis sample and in the CPS and ACS alike." Table D.1, share of each gender's employment in top-two Eloundou exposure quintiles, 2022, ages 22–25: ADP men 50.8% / women 65.8%; CPS 31.4% / 37.8%; ACS 34.0% / 41.4%. "we find steeper average declines for young women than young men consistent with greater concentration in declining high-exposure roles."

### (e) Stated limitations
- Aug 2026: "We interpret these facts as early, descriptive indicators—canaries in the coal mine—rather than causal estimates." "These patterns attenuate when controlling for education, show some divergent trends predating generative AI, and are more pronounced in the ADP analysis sample than in national survey benchmarks." ADP sample "overrepresents the manufacturing and wholesale sectors", "larger firms", and "occupations with higher AI exposure, for both men and women"; balanced panel conditions on firm survival. Nov 2025: "the facts we document may in part be influenced by factors other than generative AI."

---

## 7. Daepp & Slaughter — "How Early Adopters Used Generative AI Worldwide: Variation by Country Income and Language"

- **Authors:** Madeleine I. G. Daepp (Microsoft Research), Isaac Slaughter (University of Washington)
- **Date:** arXiv:2605.30685v1, 29 May 2026
- **URL:** https://arxiv.org/abs/2605.30685 (PDF fetched, 17 pp.)
- **Data:** Microsoft Bing Copilot (free), country-stratified sample of up to 250 users per country, 1 April–30 September 2024, users with at least 5 conversations, up to 20 conversations per user, countries with at least 50 users: "54,841 users and 686,722 conversations across 227 unique countries". Domain classifier adapted from Ramey and Francis (2009) time-use categories: Schooling, Market Work, Household Production, Personal Care, Leisure. Validation: Fleiss κ 0.605; AI–human agreement (73.8%) at least as high as human–human (69.8%).

### (a) Country income
- "Schooling is a major domain of use and is the modal domain for a majority of users in 66.7% of countries. There is an inverse relationship, however, between usage for schooling and logged country-level income (Spearman's ρ = −0.64). Market work similarly shows an inverse association (ρ = −0.38), but usage for leisure is strongly positively associated with log GDP (ρ = 0.69)." Household production and personal care "primary domains for fewer than 10% of users", with "some evidence of higher usage for these domains in higher income countries (r = 0.76 and 0.52, respectively)". All significant at p < 0.01 after Benjamini–Hochberg.
- Concentration: "Among users who ever use the chatbot for schooling, 57.8% devote the majority of their conversations to schooling ... Among users who ever use the chatbot for ... leisure ... just 31.4%".
- Discussion: "higher relative rates of usage for schooling and market work and lower rates of usage for leisure in low- and middle- versus high-income countries."
- Context cited (not their own data): low-income countries "less than 1% of visits to generative AI websites" in March 2024 (Liu and Wang 2026); "adoption was growing twice as fast in the Global North as in the Global South" in H2 2025 (Microsoft AI Economy Institute 2026a); countries with low-resource languages "average adoption rates that are 20% lower than predicted" (Misra et al. 2025b).

### Language
- "English is strongly overrepresented among AI users in Asian and African countries"; in the Americas and Europe, population English competency "generally exceeds the fraction of users for whom English is the modal language. By contrast, English disproportionately functions as the lingua franca of AI usage in Asia/Oceania and Africa".
- "The usage of non-English languages tends to be flat and generally infrequent (<1/100th the frequency of English even for languages like Arabic ...) until languages attain an MMLU score of approximately 65, at which point usage is higher and generally increasing". Mean MMLU-ProX across 15 LLMs: Americas & Europe 64.6 (12 languages), Asia & Oceania 58.1 (12), Africa 41.3 (5). "African languages are effectively missing from usage entirely".

### (b)/(c)/(d)
- No gender, occupation, or asking/doing measures. Market Work is a use domain, not an exposure score.

### (e) Stated limitations
- "Our study is subject to three major limitations. First, because we use a country-stratified sample, our results are not representative of overall use ... Second, we limited our data set to early adopters ... we excluded the large fraction of users who interact only a few times. Moreover, models have improved since this research was conducted, particularly with respect to performance across languages ... Finally, our study is descriptive, and we cannot make causal claims".

---

## 8. Aldasoro, Armantier, Doerr, Gambacorta, Oliviero (BIS) — "The gen AI gender gap"

- **Authors:** Iñaki Aldasoro (BIS), Olivier Armantier (FRB New York), Sebastian Doerr (BIS & CEPR), Leonardo Gambacorta (BIS & CEPR), Tommaso Oliviero (University of Naples Federico II)
- **Date/URL:** BIS Working Papers No 1197, July 2024, https://www.bis.org/publ/work1197.pdf (fetched, 20 pp.); also Economics Letters vol. 241 (2024), doi 10.1016/j.econlet.2024.111814 [journal version NOT FETCHED]
- **Data:** FRBNY Survey of Consumer Expectations, ad hoc module February 2024; 890 respondents (456 male, 434 female) of 1,024 invited (87% response); US household heads; use question: "How often have you used artificial intelligence tools (such as ChatGPT, Google Bard, DALL-E, ...) in the past 12 months?"

### (b) Gender gap
- "while 50% of men already use gen AI, only 37% of women do." Weekly use: men 19%, women 12% (Table 1; t-stats 3.77 and 2.95).
- Logit marginal effects (Table 3): raw −0.125; with demographics −0.104 ("differences in income, education, age, race or ethnicity explain only a small share"); + privacy/trust −0.075 (10% level); + risks/benefits −0.084; + knowledge −0.005 (insignificant).
- Gelbach decomposition: "gen-AI knowledge accounts for around 74% of the decline in the gender gap, while privacy/trust and opportunities/risk account for the remainder in roughly equal parts." Abstract: knowledge "explaining three-quarters of the gap".
- Underlying differences (1–7 or 0–100 scales): self-assessed knowledge men 3.40 vs women 2.71; relative trust in AI vs humans in medical 3.09 vs 2.45, education 3.93 vs 3.43, banking 3.02 vs 2.60; chance AI raises own productivity 26.40 vs 18.96; chance of job loss 11.05 vs 8.43. Data-breach/abuse concern identical (5.71 vs 5.71; 5.77 vs 5.79).
- Policy framing: "gen AI could amplify the gender pay gap ... privacy regulations as well as policies that promote AI-related knowledge and skills".

### (e) Stated limitations
- "knowledge and use go hand in hand, meaning that our findings are not necessarily causal"; sequencing of controls addressed via Gelbach; single cross-section of 890 US respondents.

---

## 9. Comin & Hobijn (AER 2010); Comin & Mestieri (AEJ: Macro 2018) — diffusion baseline

### 9a. Comin & Hobijn, "An Exploration of Technology Diffusion"
- **Authors:** Diego Comin (HBS & NBER), Bart Hobijn (FRB New York)
- **Published:** American Economic Review 100(5), December 2010, pp. 2031–59; AEA page fetched (https://www.aeaweb.org/articles?id=10.1257/aer.100.5.2031). Text read from HBS Working Paper 08-093, version 2, April 2008 (https://www.hbs.edu/ris/Publication%20Files/08-093_097fb722-e6dd-466d-aa1a-29733fa92757.pdf, fetched, 48 pp.); NBER w12314 [NOT FETCHED]. Published AER abstract (per AEA page): "countries have adopted technologies 45 years after their invention" and adoption gaps explain "at least 25 percent of per capita income differences". (The 2008 WP abstract says 47 years; its body says 45 mean.)
- **Data:** 15 technologies (transportation, telecommunication, IT, health care, steel, electricity), 166 countries, two centuries; precise estimates for "two thirds of the 1278 technology-country pairs".
- Adoption lags: "The average diffusion lag in our sample is 45 years with a median lag of 35"; "The standard deviation in adoption lags is 39 years"; variance decomposition "54% ... across technologies, 18% by cross-country variation, and 11% percent by the covariance ... The remaining 17% is unexplained." Steam/motor ships and railroads "took about a century before they were adopted in half of the countries"; PCs and the internet "less than 15 years for half of the countries".
- Acceleration: "technologies invented ten years later are on average adopted 4.3 years faster" and "the slope before and after 1950 is almost the same. Hence, the acceleration of the adoption of technologies seems to have started long before the digital revolution".
- Income: "cross-country differences in the timing of adoption of new technologies seems to account for at least a quarter of per capita income disparities." Sub-Saharan Africa's extra lag on recent technologies "between 1 and 2 years" vs 22–33 years for aviation.
- Two margins: extensive (adoption lag) and intensive (units demanded once adopted); diffusion curves with both margins "are not S-shaped".

### 9b. Comin & Mestieri, "If Technology Has Arrived Everywhere, Why Has Income Diverged?"
- **Authors:** Diego A. Comin (HBS/Dartmouth & NBER), Martí Mestieri (Toulouse/Northwestern)
- **Published:** AEJ: Macroeconomics 10(3), July 2018, pp. 137–78; AEA page fetched (https://www.aeaweb.org/articles?id=10.1257/mac.20150175). Text read from NBER Working Paper 19010, May 2013 (https://www.nber.org/system/files/working_papers/w19010/w19010.pdf, fetched, 66 pp.). Numbers below are from the 2013 WP; the AEA abstract carries the same two facts.
- **Data:** CHAT dataset, 25 technologies, 132 countries; plausible and precise lags for 67% of pairs; "average adoption lag across all technologies and countries is 44 years"; range "from 7 years for the internet to 121 years for steam and motor ships"; cross-country SD "from 3 years for PCs to 53 years for steam and motor ships" (Table 1: Internet mean 7, P10 1, P90 11; PCs mean 16, SD 3; Cellphones 13, SD 5).
- Convergence in adoption lags: "the rate of decline in adoption lags is almost a 40% higher in non-Western than in Western countries (i.e., 1.12% vs. .81%). Hence, there has been convergence in adoption lags between Western and non-Western countries." Robustness: convergence rate "-.44% per year" with non-homotheticities vs "-.31% per year" baseline. Example: UK–Indonesia ships lag gap 131 years vs US–Vietnam PCs 11 years.
- Divergence in intensity: "for non-Western countries, the intensive margin has declined at a .54% annual rate" relative to Western countries (no trend for Western); average intensive margin "-.62, which implies that the level of adoption of the average country is 54% of the Western countries". Vertical gap ships 0.9 vs computers 1.6. 1820 baseline: lag gap "49 years", log intensity gap "0.39".
- Great Divergence accounting: "Income per capita of Western countries relative to the rest of the world increases by a factor of 3.2 over the last 200 years. This represents 80% of the actual increase in the income gap"; with non-homothetic demand "a factor of 2.6 ... 67%". Mechanism: "Large cross-country differences in adoption lags explain much of the income divergence during the nineteenth century"; "The Great Divergence continued during the twentieth century because of the divergence in penetration rates (i.e., intensive margin of adoption)". Counterfactual with lag convergence but fixed intensity: income "almost equalized at pre-industrial levels by 2000". Half-lives: output gap 117 years, growth 145 years.

---

## What this changes for each post

### Post 1 — culture vs cohort vs development in delegation
- The best cross-provider anchor for "development" is not delegation but domain: Daepp & Slaughter (Copilot, 227 countries, Apr–Sept 2024) find schooling share falls with log GDP per capita (Spearman ρ = −0.64), market work falls (ρ = −0.38), leisure rises (ρ = 0.69). Any Economic-Index country result on directive/automation share must be checked against this composition effect: a low-income country's conversation mix is dominated by schooling, so a cross-country delegation gradient could be a use-domain gradient in disguise.
- Chatterji et al. show penetration growth was fastest in the "$10,000–40,000 GDP-per-capita" band (May 2024 to May 2025) but publish no country-level intent or task split; there is no external Asking/Doing-by-country series to compare against. The only external intent measure is global: 49% Asking / 40% Doing / 11% Expressing, with Asking rising to 51.6% and Doing falling to 34.6% by June 2025, and Doing at 56% of work messages. If the Index's directive share moves the opposite way over the same window, that is a real cross-provider divergence worth stating.
- Cohort: Chatterji et al. show within-cohort drift (non-work share rose inside every sign-up cohort; "earlier sign-ups have consistently had higher usage") — so a country's delegation level can reflect how long its users have been on the platform, not culture. Log the cohort caveat explicitly.
- Language is a candidate "development" mechanism with numbers: non-English use is "<1/100th the frequency of English" until a language reaches roughly MMLU-ProX 65; African languages average 41.3. Countries whose users must work in English may show different task mixes for reasons unrelated to culture.
- Diffusion baseline: Comin & Hobijn's acceleration (4.3 years faster per decade of invention; PCs/internet reached half of countries in under 15 years) and Comin & Mestieri's convergence in lags (non-Western lags falling 1.12%/yr vs 0.81%/yr) predict that arrival gaps for genAI should be small — consistent with Chatterji's fast low/middle-income growth. What history predicts to persist is the intensive margin (0.54%/yr relative decline for non-Western countries), so the post's claim should be framed as "arrival converges, intensity diverges", and delegation depth is an intensity-type measure.

### Post 3 — predicted vs observed exposure
- Two independent observed-usage measures now exist for comparison with Eloundou-type predictions: Microsoft's AI applicability score (785 SOC codes, downloadable CSV, CC BY 4.0) correlates with Eloundou et al. E1 at employment-weighted r = 0.73; Bick–Blandin–Deming's occupation-group adoption correlates with Eloundou at ρ = 0.65 and Felten at ρ = 0.71. An Economic-Index predicted-vs-observed correlation can be placed on this scale.
- Known residuals to test for: BBD find managers adopt at "more than double" the rate of office/administrative workers despite similar predicted exposure, and adoption tracks self-reported usefulness (−0.88) far more than barriers (−0.30); Microsoft find applicability is nearly uncorrelated with wages (employment-weighted r = 0.13) and spans all education levels. Microsoft's top occupations (Interpreters and Translators 0.492, Historians 0.462, Writers and Authors 0.454, Sales Representatives of Services 0.449, Customer Service Representatives 0.408) and bottom (physical/machine-operation occupations at 0.0) are a ready cross-check for the Index's occupation ranking.
- Method caveat to import: Microsoft's argument that "x% of the workforce has 50% of tasks covered" is threshold-driven ("either ~0% or ~100%" depending on 1% vs 0.01% coverage) — any Index headline of that form needs the threshold stated.
- Brynjolfsson–Chandar–Chen use the Index's own automative/augmentative shares (March 2025 release) as an exposure measure and find −0.098 per SD of automation for ages 22–25 (−0.084 with pooled later releases), no significant complementarity effect for the young, and +0.024 for ages 41–49. This is the first outside test of the Index's task-level classification against employment outcomes; the post should cite the version (Aug 2026) and the descriptive-not-causal framing.
- Occupation task similarity: Chatterji et al. find "Making Decisions and Solving Problems" among the two most common GWAs in every occupation group; if the Index shows sharper occupation-specific task mixes, that is a genuine provider difference (Claude's programming share was 33% of work conversations vs ChatGPT's 4.2% of all messages).

### Post 5 — gender delegation gap
- Adoption gap benchmarks: BIS Feb 2024, 50% men vs 37% women (weekly 19% vs 12%); BBD work adoption 35.0% vs 29.0% (6 pp); Humlum–Vestergaard Denmark 20 pp (any use, IZA 2024) or 16 pp (use for work, PNAS 2025), falling only to 17 pp / 12 pp within workplace and task mix; Cranney–Delecourt–Koning meta-estimate 47.8% vs 39.3% (relative gap 22%, 8.5 pp) across 318,924 people in 54 sources, stabilising at about 16% relative (5.4 pp) since early 2025.
- Direct conflict to address: Chatterji et al. report name-inferred parity ("more than half of weekly active users had typically female first names" by July 2025), while SimilarWeb shows chatgpt.com at 44.1% female (US) / ~45% (global) and survey gaps of 3–13 pp in March 2026. The post must state which population (consumer accounts, all traffic, or at-risk population) any Index gender figure refers to, and note that Chatterji's unknown-name share is 20–30%.
- Usage-type differences are documented in direction only: women more Writing and Practical Guidance, men more Technical Help, Seeking Information, Multimedia (Chatterji); women more represented on education/language-learning/personal-life tools, men on coding, website building, finance, analytics (Cranney et al.); women's ChatGPT visits 10.4% shorter (33 seconds), no narrowing. A "delegation gap" (directive share by gender) would be new — no external source measures it. The closest analogues are Gai–Hou–Tu (female engineers "send fewer prompts and copy fewer lines of AI-generated code") and the coding-agent gap (22% vs 9% weekly use).
- Mechanisms with numbers: BIS attributes 74% of the explained gap to self-assessed knowledge; Humlum–Vestergaard find beliefs equal by gender but women more often report needing training, men more often report employer restrictions; Cranney et al. list competence-penalty evidence (Gai–Hou–Tu). Brynjolfsson et al. add that women are more concentrated in high-exposure occupations (ADP 65.8% vs 50.8% for ages 22–25; CPS 37.8% vs 31.4%), with "steeper average declines for young women".
- Occupation-composition trap: Cranney et al. and Humlum–Vestergaard both show gaps persist within occupation and firm, so a gender delegation gap in the Index should be reported within-occupation where the data allow.

### Post 6 — convergence baseline
- Historical priors (Comin & Hobijn; Comin & Mestieri): mean adoption lag 44–45 years, median 35, SD 39; PCs 16 years (SD 3), cellphones 13, internet 7 (P10 1, P90 11); lags fall 4.3 years per decade of later invention; non-Western lags converge (1.12%/yr vs 0.81%/yr decline); intensive margin diverges (−0.54%/yr, average country at 54% of Western level); lag differences explain "at least a quarter" of income gaps and the two margins together 80% of the Great Divergence.
- GenAI against that baseline: BBD, overall adoption 45.5% two years after ChatGPT vs PC 19.7% three years after the IBM PC and internet 21% two years after 1995; work adoption 32.1% vs 25.1% for the PC. Chatterji: 700 million weekly users, "around 10% of the world's adult population", by July 2025; fastest growth in the $10k–40k GDP band. Both are extensive-margin facts, consistent with "technology has arrived everywhere".
- The intensive margin is where the external evidence points to persistent gaps: Daepp & Slaughter's domain gradients (schooling vs leisure), the language threshold (MMLU ~65), the Global North growing "twice as fast" in H2 2025 (Microsoft AI Economy Institute, cited), Cranney et al.'s stable 40% female traffic share since October 2024, and Humlum–Vestergaard's within-occupation gaps. A convergence claim for the Index should therefore separate "share of population using" (expected to converge fast, per history) from "depth or delegation per user" (expected to diverge, per history), and test each.
- The within-cohort drift in Chatterji et al. (non-work share 53% to 73% in one year, driven by existing cohorts) shows that per-user usage composition changes quickly even without new entrants; a convergence test must control for cohort age or it will confuse maturation with catch-up.
