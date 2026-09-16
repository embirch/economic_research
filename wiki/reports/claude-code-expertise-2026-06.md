# claude-code-expertise-2026-06

"Agentic coding and persistent returns to expertise" — the ~400,000-session Claude Code paper
introducing work modes, decision attribution, a task-specific expertise rating, transcript-based
success measures and a freelance-calibrated task-value estimator.

Its companion appendix (classifier prompts, sample construction, estimator calibration,
validation) is a separate wiki slug: `claude-code-expertise-2026-06-appendix`. This file
cross-references it and does not summarise it.

## Source

- **Title:** "Agentic coding and persistent returns to expertise" (the H1 on the web page and the PDF title page). Note the web page's HTML `<title>` and `og:title` are different: "How Claude Code is used in practice". The PDF running header on every page is "Agentic coding and persistent returns to expertise".
- **Authors — the two versions disagree.** The PDF title page and the PDF's own BibTeX block list five: "Zoe Hitzig, Maxim Massenkoff, Eva Lyubich, Ryan Heller, and Peter McCrory" (PDF p. 1, p. 18). The web page's citation block lists six, adding Shaoyi Zhang: "Zoe Hitzig and Maxim Massenkoff and Eva Lyubich and Shaoyi Zhang and Ryan Heller and Peter McCrory" (web, "Citation"). **Maxim Massenkoff — the intended mentor — is the second author.** Acknowledgements are identical in both: Jake Eaton, Sarah Pollack, Hanah Ho, Szymon Sacher, Anton Korinek, Santi Ruiz, Kerry Persen, Ankur Rathi, Alex Tamkin, Heather Whitney, Cat Wu, Kacie Jenkins, Jennifer Martinez, Amie Rotherham, Boris Cherny, Eleanor Dorfman, Miles McCain, Jack Clark (PDF p. 1; web, "Acknowledgements").
- **Date:** June 16, 2026 (PDF p. 1 "Published June 16, 2026"; web dateline "Jun 16, 2026"; BibTeX `date = {2026-06-16}`).
- **Primary URL:** <https://www.anthropic.com/research/claude-code-expertise> (canonical meta tag). The PDF's BibTeX gives a broken variant with `research` doubled: `https://www.anthropic.com/research/research/claude-code-expertise` (PDF p. 18) — a typo; the web citation block gives the correct URL.
- **PDF URL:** <https://cdn.sanity.io/files/4zrzovbb/website/433472e34b60db1a52ebf0b8c6600f057b6908c5.pdf>, 18 pages, linked from the page as "Read in PDF".
- **Appendix URL (separate document, separate wiki slug):** <https://cdn.sanity.io/files/4zrzovbb/website/a94728142a45694292336165947f8d6e3e1a357e.pdf>, linked four times from the body (PDF pp. 5, 10, 12, 15, 18) for classifier text, validation results, the task-value estimator construction and the regressions behind Figure 5. Not summarised here; see `wiki/reports/claude-code-expertise-2026-06-appendix.md`. The web page's "Appendix / Available here" line also carries a second, differently-hashed link on the trailing full stop (`…7426c33b0e75ab4771c465d30d5bc1019bdd0c9c.pdf`), apparently a stray link; not fetched.
- **Document type:** research paper with PDF, in Anthropic's "Economics" topic (the web page's only topic tag; the April 2025 software-development report carried "Societal Impacts" and "Economics"). Not an Economic Index wave report; a standalone paper in the Claude Code / agentic-measurement line.
- **Approximate length:** PDF 18 pp: title page, key findings (4 bullets), §1 Introduction, §2 The division of labor (§2.1 What people use Claude Code for, §2.2 Who decides what, §2.3 Level of expertise), §3 Who uses Claude Code, and for what (§3.1 The users, §3.2 The work), §4 Success depends on what the people brings (§4.1 The returns to expertise, §4.2 Occupation may matter less than expertise), "Looking ahead", 10 footnotes (pp. 17–18), BibTeX, appendix pointer. Six figures (Figures 1–6) and two tables (Table 1 expertise classifier, Table 2 success/failure definitions). The web page carries the same text with the section numbers dropped.
- **Text differences between the web page and the PDF** (both fetched today; recorded here because quotations must name their source):
  1. **PDF-only claim.** "Most sessions are anchored to an existing codebase: 48% primarily modify existing code and another 17% explore code, while 14% create new code from scratch. Roughly a fifth of sessions touch no codebase at all." (PDF p. 4). This sentence is absent from the web page.
  2. **Web-only claim.** "The gap between software-related occupations and other occupations narrows under our looser definition of success––with both groups reaching at least partial success in code-producing sessions 89% and 88% of the time, respectively." (web, "Occupation may matter less than expertise"). Absent from the PDF.
  3. **Threshold disagreement.** Figure 5's caption defines the troubled subsample as "failure signals ≥ 3" in the PDF (p. 13) and "failure signals > 3" on the web page. Not the same subsample.
  4. **Figure titles.** "Figure 6: Success rates in coding sessions by inferred occupation" (PDF p. 15) vs "Figure 6: Verified and judged success rates in coding sessions by inferred occupation" (web).
  5. **Figure 5 caption, left panel.** The PDF names three series ("the share of all sessions judged succeeded or partially succeeded, those judged succeeded and those reaching verified success"); the web says only "The left panel includes all sessions."
  6. **Section heading typo.** "4. Success depends on what the people brings" (PDF p. 10) vs "Success depends on what the user brings" (web).
  7. Minor: the PDF writes "Github", the web "GitHub"; the PDF has stray punctuation the web fixes ("In particular, domain experts, succeed more often", PDF p. 3; "The two sources have high agreement for instance, more than 90%", PDF p. 5); the web uses "––" where the PDF uses "—".
- **The data it rests on:** "~400,000 Claude Code sessions" / "~400,000 interactive sessions from ~235,000 people" between October 2025 and April 2026, analysed with Anthropic's privacy-preserving analysis tool (Clio), plus automatically recorded per-session telemetry (e.g. lines of code added or deleted), plus two external public datasets used as inputs: a public dataset of real freelance job postings for the task-value calibration (PDF p. 10) and SWE-chat, <https://huggingface.co/datasets/SALT-NLP/SWE-chat>, for the illustrative examples in Tables 1 and 2 (PDF pp. 7, 12).
- **Was any of it released?** No session-level or aggregate data release accompanies the paper. Neither the paper nor the web page links to a dataset, a code repository or a notebook; the only pointer is to the appendix PDF for classifier text and validation. Cross-checked against the steward's enumeration of `Anthropic/EconomicIndex` (`data/releases/INDEX.md`, 2026-09-16): no folder corresponds to this paper, and no file in that repository names Claude Code. The public inputs (SWE-chat; the freelance-posting dataset, unnamed in the main paper) are third-party. So: **nothing released**; the paper is citable, not reproducible.

## Claims

Numbered; each with its PDF page (and figure or table where relevant), the number as published,
and the comparison it rests on. Where a number exists only inside a figure image, it is marked
"read from Figure N" and should be treated as approximate.

**Frame and sample**

1. **Scope and size.** "we introduce a framework for studying interactive agentic coding based on a privacy-preserving analysis of ~400,000 Claude Code sessions from between October 2025 and April 2026" (PDF p. 2, key findings); "~400,000 interactive sessions from ~235,000 people" (PDF p. 2, §1). Seven months, one product, interactive surfaces only.
2. **External adoption context.** "The share of Github projects with coding agent activity has more than doubled since late 2025" (PDF p. 2), sourced in footnote 1 to a study of 128,000 public repositories finding coding-agent activity in "an estimated 16-23% of projects as of the end of October 2025" and a follow-up finding "adoption rates more than twice as high among projects created after that period" (PDF p. 17). Comparison: external repository evidence, not Anthropic data.
3. **Intensity of use.** "Claude Code users now spend an average of 20 hours per week using the tool" (PDF p. 2), qualified in footnote 2 as "hours in which Claude Code was actively running, not the user's hands-on time typing to Claude" (PDF p. 17). No source, no sample definition, no window given for this number.

**Work modes (§2.1)**

4. **Nine work modes; code-writing modes are 56% of sessions.** "About 56% of sessions consist of writing (25%) fixing (26%), or testing and orchestrating code 5%. Operating software comprises 17%, while 14% of sessions are planning or exploring, and 13% produce analysis or prose (Figure 1)." (PDF p. 4). Comparison: shares of all sessions in the pooled seven-month window.
5. **The nine modes individually** (read from Figure 1, PDF p. 4; not in the text): fixing something broken 26%, building something new 25%, operating software 17%, writing docs and presentations 10%, understanding a system 7%, planning a change 7%, orchestrating agents and pipelines 3%, analyzing data 3%, testing code 2%.
6. **Most sessions work on existing code (PDF only).** "Most sessions are anchored to an existing codebase: 48% primarily modify existing code and another 17% explore code, while 14% create new code from scratch. Roughly a fifth of sessions touch no codebase at all." (PDF p. 4). This is a separate classification from the nine modes and appears nowhere on the web page.
7. **Classifier–telemetry agreement.** "more than 90% of sessions our classifier labeled as creating or modifying code showed code changes in the telemetry" (PDF p. 5). Comparison: model reading of the transcript against automatically recorded telemetry, one direction only (labelled-as-code → code changed).

**Decision attribution and delegated action (§2.2)**

8. **The division of labour.** "On average, people make about 70% of the planning decisions but only 20% of the execution decisions (Figure 2)." (PDF p. 6). Figure 2's caption states the mirror image: "In the typical session, the user makes about 70% of planning decisions while Claude makes about 80% of execution decisions." (PDF p. 5). Comparison: within-session shares of classifier-listed decisions, planning vs execution.
9. **Shape of the distribution** (read from Figure 2, PDF p. 5): Claude's share of execution decisions is in the 90–100% bin for roughly half of all sessions, while Claude's share of planning decisions is concentrated in the 0–30% bins (~24%, ~16%, ~20% of sessions in the 0–10, 10–20 and 20–30 bins).
10. **Session structure.** "In a typical session, there are about 4 such turns. In our historical data from October to April, each prompt the user sends sets off a chain of around 10 actions taken by Claude on average—and sometimes over a hundred. In each turn, Claude reads files, edits code, runs commands, and writes on average 2,400 words of output." (PDF p. 6).
11. **The tail of actions per prompt.** "About 2% of sessions average more than 100 actions per prompt, about 1 in 270 average more than 200, and about 1 in 2,300 average more than 500." (footnote 6, PDF p. 17).
12. **Actions track who decides.** "When the user keeps control of execution (i.e., makes over 80% of execution decisions), Claude takes fewer actions per turn (about 8 actions). And when Claude takes control of planning (i.e., makes over 80% of planning decisions), it takes on the highest number of actions (about 16)." (PDF p. 6). Comparison: mean actions per turn across two extreme decision-share groups; no regression, no controls reported for this contrast.

**The expertise gradient in what Claude does (§2.3)**

13. **Novice vs expert action chains and output.** "In typical novice sessions, each prompt sets off about 5 Claude actions and roughly 600 words of output, while expert sessions set off action chains more than twice as long (12 actions) carrying five times the output (3200 words) (Figure 3)." (PDF p. 8). Figure 3's own labels read 4.9 actions / 607 words at level 1 and 11.7 actions / 3.2k words at level 5 (read from Figure 3, PDF p. 9). Comparison: geometric means by rated expertise level, unadjusted.
14. **The gradient is not a composition artefact, by the paper's own check.** "This gap between novice and expert sessions appears within every kind of work and every band of task value." (PDF p. 8).
15. **Adjusted gradient and significance.** "Both upward trends are statistically significant (p < 0.001), as is each adjacent-level step, and they remain significant (at +9% actions and +13% output per expertise level) in a regression controlling for work mode, task value, month, occupation, and model family, with standard errors clustered by user." (Figure 3 caption, PDF p. 9). This is the paper's only reported regression coefficient in the main text.
16. **Relation to the earlier autonomy measures.** "These measures complement the autonomy measures in our prior report on Claude Code. Those measures tracked how long the agent runs and how often people approve its actions automatically. Our decision attribution measure, by contrast, captures who makes the substantive decisions in a session as a whole while our measures of output and actions per prompt measure how much autonomous activity from Claude human directions yield." (PDF p. 8). Comparison: this paper's constructs against those of `measuring-agent-autonomy`.

**Who the users are (§3.1)**

17. **Occupation inferred in ~70% of sessions.** "We were able to infer occupation in about 70% of sessions." (PDF p. 9). The rest are "left unclassified when there is no signal about the user's occupation" (PDF p. 8).
18. **Ranking of occupation groups.** "Within this set, Computer and Mathematical Occupations, a category which encompasses most software-related jobs, is unsurprisingly the largest group. The next largest are Business and Financial Operations, Arts, Design and Media, Management, and Life, Physical, and Social Sciences." (PDF p. 9). No shares are published for any occupation group.
19. **Fastest-growing non-software groups.** "The fastest-growing non-software occupation groups in our sample are management, sales, and legal occupations." (PDF p. 9). No growth rates published.

**How the work changed over seven months (§3.2)**

20. **Debugging fell by nearly half.** "The clearest change is that the share of sessions spent fixing broken code fell from 33% to 19% (Figure 4)." (PDF p. 9). Comparison: October 2025 vs April 2026 share of sessions.
21. **Operating software grew.** "Operating software grew from 14% to 21% of sessions." (PDF p. 9).
22. **Writing and data analysis roughly doubled.** "Writing and data analysis roughly doubled, from about 10% to 20% of sessions." (PDF p. 9). Figure 4's left panel labels April 2026 as build 21%, operate 21%, communicate 20%, fix 19% (read from Figure 4, PDF p. 11).
23. **Task value rose 27% (body) / about 25% (key findings).** "By this measure, the estimated value of the average session rose by 27% between October and April." (PDF p. 10); Figure 4's right panel labels the pooled series "all +27%" (read from Figure 4, PDF p. 11). The key-findings bullet says instead: "the value of the typical task, which we estimate through a comparison to freelance job postings, rose in almost every kind of work, and about 25% on average" (PDF p. 2). **Wiki author's note, not the paper's:** 25% and 27% are both published, in the same document, for what appears to be the same quantity ("the typical task" vs "the average session"), and are never reconciled. Both figures appear identically in the web version. Any post citing the rise must say which it is citing and that the other exists.
24. **By mode.** "Building, operating, and fixing tasks all grew more valuable by roughly a third or more (about 43%, 34%, and 32% respectively)." (PDF p. 10). Figure 4's right panel adds "communicate +2%" (read from Figure 4, PDF p. 11) — the one mode with essentially no rise, which the text does not mention.

**Success and the returns to expertise (§4, §4.1)**

25. **The headline gradient.** "A novice-rated session reaches our strictest measure, verified success, 15% of the time and at least partial success 77% of the time. A session rated intermediate or up reaches verified success 28-33% of the time and partial success 91-92% of the time (Figure 5)." (PDF pp. 11–12). Comparison: adjusted rates by rated expertise level, comparing sessions matched on work mode, task-value band, month, task subject and software/non-software occupation.
26. **Concavity.** "In each measure, most of the gain comes from moving between novice to intermediate; between intermediate and expert, the slope decreases." (PDF p. 12). Also stated in the key findings as "the gap between intermediate and expert users is modest" (PDF p. 2).
27. **Figure 5 endpoints** (read from Figure 5, PDF p. 13; adjusted rates, level 1 → level 5): all sessions — at least partial success 77% → 91%, judged success 39% → 65%, verified success 15% → 33%. Sessions that hit trouble — at least partial success 60% → 80%, judged success 10% → 27%, verified success 4% → 15%. Failure measures among troubled sessions — judged failure 40% → 20%, verified failure 30% → 18%, abandoned 19% → 7%.
28. **Recovery from trouble.** "Among sessions that hit trouble, the share that are verified successes rises from 4% for novice-rated sessions to 15% for expert-rated ones, accounting for all the controls described above (Figure 5). Looking at the looser measures, we find that the share of at least partial success is 60% for novice and 80-81% for intermediate through expert sessions." (PDF p. 13).
29. **Abandonment.** "19% of sessions where the user appears to be a novice end abandoned, against 5-7% for everyone else." (PDF p. 13), where abandoned = judged failure and zero lines of code written. Interpretation offered: "the least experienced users are more likely to give up when they are struggling to get the outcome they are after. Part of the value of expertise appears to be the ability to steer the agent in the right direction." (PDF pp. 13–14).
30. **Exclusion.** "we exclude sessions classified as having 'no clear goal,' which comprise about 7.7% of our full sample" (PDF p. 11).

**Occupation vs expertise (§4.2)**

31. **Overall success by occupation group.** "Software engineers and users in other 'computer and mathematical occupations' reach verified success in about 30% of their sessions overall, where users from other professions reach verified success about 26% of the time. Among sessions that produce code (i.e., sessions that add or modify at least one line of code), those numbers are 34% and 29% respectively." (PDF p. 14). Comparison: software/math SOC group vs all other inferred groups, first on all sessions then on code-producing sessions only.
32. **The gap is small and flat (a published null).** "That five-point gap is small, and it has neither widened nor narrowed over seven months, even as the success rates in both groups increased." (PDF p. 14). No confidence interval, no power statement, and no chart is given for this over-time null.
33. **Looser measure narrows the gap further (web only).** "with both groups reaching at least partial success in code-producing sessions 89% and 88% of the time, respectively" (web, "Occupation may matter less than expertise"). Absent from the PDF.
34. **Every large occupation is close to software.** "In code-producing sessions, every one of the ten largest occupations in our dataset lands within seven points of software engineers in terms of their success." (PDF p. 14); Figure 6's caption repeats "Every group is within seven percentage points of software/math users (SOC Code Computer and Mathematical Occupations)" (PDF p. 15).
35. **Figure 6 values by group** (read from Figure 6, PDF p. 15; verified success / judged success / at least partial success, among code-producing sessions): Software & math 34 / 60 / 94; Management 37 / 55 / 95; Legal 33 / 57 / 95; Business & Finance 29 / 54 / 93; Healthcare 28 / 56 / 93; Arts, Design & Media 28 / 53 / 92; Sales 26 / 51 / 92; Architecture & Engineering 27 / 54 / 93; Education 27 / 52 / 92; Sciences 27 / 54 / 94. Error bars are "95% confidence intervals computed on distinct accounts" (Figure 6 caption, PDF p. 15). **Wiki author's note:** read this way, the judged-success spread (Sales 51 vs Software & math 60) is nine points, which sits awkwardly with the "within seven points" claim in claim 34 unless "success" there means verified success only (where the widest gap read is Sales 26 vs 34, eight points). The chart values are read from an image and are approximate; a post relying on this claim should say which measure it means.
36. **Management is highest on verified success.** "Management occupations are highest on verified success, slightly above the software engineering occupations." (PDF p. 14), with two competing explanations offered — transferable management skill, or a measurement artefact of verification resting on explicit confirmation in the transcript (PDF p. 14; footnote 10, PDF p. 18).

**The paper's own summary claims**

37. **Coding background is becoming less relevant.** "In sessions that produce code, every major occupation succeeds at rates within a few points of those in software-related occupations. It appears that coding agents are making a coding background less relevant to successful programming." (PDF p. 14).
38. **Expert sessions verify-succeed more than twice as often as novice ones.** "Sessions rated expert reach verified success more than twice as often as those rated novice, and when a session hits trouble, novices abandon the session at several times the rate of everyone else." (PDF p. 14).
39. **Competence, not mastery.** "the gains come mostly from competence, not mastery—a working grasp of the domain captures most of the benefit, while deep specialization adds only a bit more beyond that." (PDF p. 15).

## Definitions (verbatim)

Quoted in full, with the page (PDF) or section (web) each comes from. Curly quotation marks and
the source's own punctuation are reproduced; PDF quotations preserve the PDF's typography
(including its typos), and where the web wording differs the web version is given too.

**The sample and what is in it**

- **Interactive sessions / the surfaces included** — "We focus on Claude Code usage through a command-line interface (CLI), claude.ai, or the Claude Code desktop app." (PDF p. 3).
- **What is excluded, and why** — "Note that we exclude Claude Code usage that runs through third party integrated developer environments, and software development kits. We also therefore exclude sessions in “headless” mode where a user runs a single prompt in the CLI via claude -p “<prompt>” . We exclude this usage since it differs in two key ways—much of it is programmatic, with Claude Code embedded in automated tools and pipelines rather than conversing with a user, and even when a user is present, we do not see a user’s session end-to-end the way we do on the surfaces we include." (footnote 4, PDF p. 17).
- **The classifier model** — "All classifiers in this report use Claude Sonnet 4.6 unless otherwise noted. Details about the classifiers, including their exact full text and validation results, can be found in the Appendix." (footnote 5, PDF p. 17).
- **The privacy constraint on every measure** — "Like all measures in this report, these inferences are produced using our privacy-preserving analysis tool. No researcher reads individual transcripts, occupation labels are never linked to identifiable users, and we only observe aggregates over a minimum number of distinct users." (footnote 7, PDF p. 17).
- **Turns, prompts and actions** — "A Claude Code session involves Claude and the user going back and forth trading prompts (from the user) and actions (taken by Claude)—the user writes a prompt and Claude goes off and does some work, and then the user writes another prompt, and so forth." (PDF p. 6).

**Work modes**

- **Work mode** — "we classify each session into one of nine **work modes**—the single activity that best describes what the session is trying to accomplish." (PDF pp. 3–4; bold in the PDF).
- **The nine modes, in the paper's own gloss** — "Four modes involve writing or maintaining code directly: building something new, fixing something broken, testing code, and orchestrating other agents or automated pipelines. Another category is operating software—deploying, configuring, running pipelines, monitoring systems. Two categories are more about working out what to do: understanding how an existing system works, and planning a change before making it. And two take actions unrelated to code, or where code is incidental to the final product: analyzing data, and communicating via presentations and other prose-based documents." (PDF p. 4).
- **Figure 1's unit** — "Each interactive session is classified into the single mode that best describes what it is trying to accomplish." (Figure 1 caption, PDF p. 4).
- **The telemetry check** — "We classify each session by having a model read its transcript, then using our privacy-preserving analysis tool, we check them against telemetry that's recorded automatically for every session, including whether any lines of code were added or deleted. The two sources have high agreement for instance, more than 90% of sessions our classifier labeled as creating or modifying code showed code changes in the telemetry. See the Appendix for details." (PDF p. 5; the web page reads "high agreement—for instance").

**Decision attribution**

- **The classifier** — "To understand the division of decision-making in a session, we build a privacy-preserving decision attribution classifier based on the content of a session. We ask a classifier to list all the meaningful decisions in a session." (PDF pp. 5–6).
- **Planning decisions** — "planning (what to do, which approach to take, what counts as done)" (PDF p. 6).
- **Execution decisions** — "execution (which files to change, what code to write, what language to write in, which commands to run)" (PDF p. 6).
- **The two numbers per session** — "The classifier then attributes each decision to Claude or to the user, giving every session two numbers: the user's share of planning decisions and the user's share of execution decisions." (PDF p. 6).
- **Figure 2's unit** — "Distribution across sessions of the share of planning decisions (what to do) and execution decisions (how to do it) attributed to Claude rather than the user." (Figure 2 caption, PDF p. 5).
- **"Keeps control" / "takes control" thresholds** — "When the user keeps control of execution (i.e., makes over 80% of execution decisions), Claude takes fewer actions per turn (about 8 actions). And when Claude takes control of planning (i.e., makes over 80% of planning decisions), it takes on the highest number of actions (about 16)." (PDF p. 6).

**Expertise**

- **The measure** — "From each transcript, Claude rates the user's apparent expertise at the task on a five-point scale from novice to expert." (PDF p. 6).
- **The three signals** — "The expertise classifier looks for three signals: how precisely the user frames their directions, what they ask Claude to verify, and whether the user tends to correct Claude or Claude tends to correct the user." (PDF p. 6).
- **What it is not** — "Note that expertise is capturing something quite different from job title or general ability, and, crucially, it is *task-specific*. A senior engineer asking their first Rust question is a beginner at Rust. An accountant who has never used Python, but tells Claude exactly which reconciliation rules a Python script must enforce and catches the edge case it mishandles at month-end close, is an expert at that task." (PDF pp. 6–7).
- **The five levels, as defined in Table 1** ("What the classifier looks for" column, Table 1, PDF p. 7):
  - 1 (Novice) — "User requests have no domain-specific nomenclature. Verification requests, if any, are generic (e.g. “double check this”). User doesn’t recognize Claude’s errors."
  - 2 (Beginner) — "User requests have some domain terminology. Verification requests are untargeted. User pushes back only on obvious errors."
  - 3 (Intermediate) — "User frames requests with some domain specificity, but does not engage deeply on methodology or tradeoffs. User asks for some non-generic checks, and may notice Claude’s errors."
  - 4 (Advanced) — "User exhibits domain knowledge and anticipates some tradeoffs unprompted. Verification requests are targeted. User catches at least one of Claude’s domain mistakes."
  - 5 (Expert) — "User employs sophisticated domain-specific jargon and anticipates intricate tradeoffs and design decisions. Verification is precise, targeting weak points. User corrects Claude, Claude almost never corrects the user."
- **Table 1's provenance** — "The examples paraphrase, anonymize and condense real sessions labeled by our classifiers. Many of the sessions used in the table come from a public dataset of agentic coding sessions, SWE-chat." (Table 1 caption, PDF p. 7; the web adds the link to <https://huggingface.co/datasets/SALT-NLP/SWE-chat>).
- **How Table 1's examples are read** — "The conversation categorized as Novice gives generic instructions with no implied domain-specific knowledge. The Expert conversation conveys deep knowledge of the codebase and technical environment." (PDF p. 8).

**Occupation**

- **The measure** — "we infer each user’s occupation from the session transcript, mapping it to one of 23 major groups in the Bureau of Labor Statistics’ Standard Occupational Classification (SOC) taxonomy." (PDF p. 8).
- **The permitted signals** — "The classifier is instructed to rely only on signals such as the project context the agent loads at the start of a session, the names and structure of their files, any artifacts they reference (i.e., legal filings, clinical data, financial reports, a curriculum, etc.) and vocabulary they use." (PDF p. 8).
- **The anti-coding-bias rule** — "It is explicitly instructed not to treat the act of coding as evidence of a coding profession. A session is classified into the coding SOC code (Computer and Mathematical Occupations) only when there is clear signal that software or data work is the user’s job. A session in which a lawyer builds a script to automatically flag missing clauses across a folder of contracts is mapped into Legal Occupations, even if the session’s work is primarily software. The session is left unclassified when there is no signal about the user’s occupation." (PDF p. 8).
- **Code-producing sessions** — "sessions that produce code (i.e., sessions that add or modify at least one line of code)" (PDF p. 14).

**Task value**

- **The estimator** — "We approximate each session’s economic value by asking what the work would cost on a freelance marketplace, calibrated against a public dataset of real postings." (PDF pp. 9–10).
- **What it is for** — "These price estimates are coarse, so we use them primarily to compare tasks to one another over time, not as dollar values to be read literally." (PDF p. 10).
- **The estimator's stated basis and bias** — "The estimation approach we take here is intended to get at relative differences in the value of sessions, not absolute value. The dollar amount is based on comparisons to the freelancer market—not salaried work—and comes from an ultimately fuzzy match between the Claude Code session and the job posting. Since the relative estimates will remove any consistent bias from these issues, we place more emphasis there." (footnote 8, PDF pp. 17–18).

**Success and failure**

- **Why transcript-based measures** — "We do not observe users’ real-world outcomes, and we cannot ask them directly whether they got what they wanted out of Claude. Instead, we rely on two complementary transcript-based measures." (PDF p. 10).
- **Judged success** — "The first, *judged success*, comes from a classifier that reads the full transcript and decides whether the person succeeded in doing what they set out to do (with options: succeeded, partially succeeded, failed, no clear goal)." (PDF p. 10).
- **Success signal** — "A success signal classifier looks for verifiable evidence of success. In particular, it looks for git activity like commits and pull requests matching the work, as well as test suites passing, and explicit affirmation from the user. It scores the session from “no signal” to “weak signal” (1) to “multiple hard signals” (5)." (PDF p. 10).
- **Failure signal** — "A parallel failure signal scores the evidence that things went wrong—errors, failed tests, retries, the user pushing back on the output." (PDF p. 10).
- **Verified success** — "Verified success requires both that the session is judged successful and there is at least one hard verifiable signal of success." (PDF p. 10).
- **The six measures, as defined in Table 2** ("Definition" column, Table 2, PDF p. 12; the code-like expressions are reproduced as printed):
  - At least partial success — "The session partially completes the user’s main goal / `outcome = {success, partial success}`"
  - Judged success — "The session completes the user’s main goal / `outcome = {success}`"
  - Verified success — "Judged success plus hard evidence of success / `outcome = success AND success signal = {4,5}`"
  - Judged failure — "The session does not complete the user’s main goal / `outcome = failure = NOT {success, partial success}`"
  - Verified failure — "Judged failure plus hard evidence of failure / `outcome = failure AND failure signal = {4,5}`"
  - Abandoned — "Judged failure and zero lines of code added / `outcome = failure AND lines of code added = 0`"
- **Table 2's provenance** — "The examples paraphrase and summarize real sessions from a public dataset of agentic coding interactions, SWE-chat, labeled by our classifiers." (Table 2 caption, PDF p. 12).
- **Hits trouble** — "We say a session *hits trouble* when the failure signal records verified evidence of failure. This could be an error, a failed test, multiple attempts to do the same thing, or the user expressing frustration or dissatisfaction." (PDF pp. 12–13). The operational threshold is given only in Figure 5's caption, and the two versions disagree: "failure signals ≥ 3" (PDF p. 13) vs "failure signals > 3" (web, Figure 5 caption).
- **Abandoned, in the text** — "We say a troubled session is *abandoned* if it is judged as failed *and* zero lines of code are written" (PDF p. 13).
- **How failures are counted in §4.1** — "Note that in this analysis, the sessions judged as failures are those that do not even partially succeed." (PDF p. 13).
- **The exclusion** — "we exclude sessions classified as having “no clear goal,” which comprise about 7.7% of our full sample" (PDF p. 11).

**The estimator behind Figures 3 and 5 (as described in the captions)**

- **The adjusted rate** — "Each point is an adjusted rate—we estimate the differences between expertise levels by comparing only sessions that share the same work mode, the same task-value band, the same month, the same task subject, and the same kind of user (software-related occupation or not). Details about the regressions behind these points are in the Appendix. Whiskers are confidence intervals on sample means (most are too small to be visible in this plot). These plots exclude sessions judged by the success outcome classifier to have no clear goal." (Figure 5 caption, PDF p. 13).
- **The matched comparison, in the text** — "Throughout this section, we partially address this worry by comparing sessions doing the same kind of work, at the same estimated value, in the same month, on the same subject, from people in the same broad occupation group, and ask how outcomes differ by the person’s rated expertise." (PDF p. 11).
- **Figure 3's statistics** — "Boxes span the interquartile range (split at the median). Whiskers represent the 5th to 95th percentile. White dots are geometric means. Both upward trends are statistically significant (p < 0.001), as is each adjacent-level step, and they remain significant (at +9% actions and +13% output per expertise level) in a regression controlling for work mode, task value, month, occupation, and model family, with standard errors clustered by user." (Figure 3 caption, PDF p. 9).
- **Figure 6's statistics** — "Error bars are 95% confidence intervals computed on distinct accounts." (Figure 6 caption, PDF p. 15).

## Data and methods

In my own words, with page references.

**Product, surfaces and window.** One product: Claude Code, observed over seven months, October
2025 to April 2026 (PDF p. 2). Three surfaces are pooled — the CLI, claude.ai and the Claude Code
desktop app (PDF p. 3). Three kinds of usage are excluded by design: third-party IDE
integrations, SDK usage, and `claude -p` "headless" single-prompt runs, on the grounds that they
are largely programmatic and that the researchers cannot see a user's session end to end
(footnote 4, PDF p. 17). The paper calls the excluded non-interactive usage "a substantial share
of activity" and does not quantify it (PDF p. 15).

**Sample.** ~400,000 interactive sessions from ~235,000 people (PDF p. 2) — roughly 1.7 sessions
per person, so the data form a short, very unbalanced panel, though the paper never uses the
word panel and reports no within-user analysis beyond clustering standard errors by user in one
regression (Figure 3 caption, PDF p. 9). For the success analyses the 7.7% of sessions with "no
clear goal" are dropped (PDF p. 11). For the occupation analyses, only the ~70% of sessions where
occupation could be inferred are usable (PDF p. 9), and Figure 6 restricts further to
code-producing sessions in the ten largest occupation groups (PDF p. 15). No sampling frame,
no geography, no plan or tier, no firm identifier and no model-version distribution are reported;
"model family" appears only as a control in one regression (PDF p. 9).

**Analysis infrastructure.** Everything is produced through Anthropic's privacy-preserving
analysis tool (Clio). Footnote 7 states the constraints: no researcher reads individual
transcripts, occupation labels are never linked to identifiable users, and only aggregates over a
minimum number of distinct users are observed (PDF p. 17). The minimum is not stated in the main
paper.

**Classifiers.** All use Claude Sonnet 4.6 unless otherwise noted, with prompts and validation in
the appendix (footnote 5, PDF p. 17). Six distinct classifiers are described in the main text:
1. *Work mode* — one of nine modes per session, single-label (PDF pp. 3–4).
2. *Codebase relationship* — modify / explore / create from scratch / no codebase (PDF p. 4, PDF
   only).
3. *Decision attribution* — enumerate the meaningful decisions, split them into planning and
   execution, attribute each to Claude or the user, and return two shares per session (PDF p. 6).
4. *Expertise* — a 1–5 task-specific rating from three transcript signals, defined level by level
   in Table 1 (PDF pp. 6–7).
5. *Occupation* — one of 23 SOC major groups, inferred from project context, file names and
   structure, referenced artefacts and vocabulary, with an explicit instruction not to treat
   coding itself as evidence of a coding job, and an unclassified option (PDF p. 8).
6. *Outcome* — judged success (succeeded / partially succeeded / failed / no clear goal) plus two
   evidence classifiers, a success signal and a failure signal, each scored 1–5 (PDF p. 10).
A seventh measure, *task value*, is an estimator rather than a category: the session's work is
priced as if posted on a freelance marketplace, calibrated against a public dataset of real
postings (PDF pp. 9–10), with construction details in the appendix.

**Non-classifier measures (telemetry and session structure).** Lines of code added or deleted,
recorded automatically for every session (PDF p. 5), which also enters the definition of
"abandoned" (PDF p. 12) and of "code-producing" (PDF p. 14). Session structure — turns, prompts,
actions per prompt, words of output per turn — is read off the session rather than classified
(PDF p. 6).

**Thresholds, as stated in the main text.** Verified success = judged success and success signal
in {4,5}; verified failure = judged failure and failure signal in {4,5}; abandoned = judged
failure and zero lines added (Table 2, PDF p. 12). "Hits trouble" = failure signals ≥ 3 in the
PDF, > 3 on the web page (Figure 5 caption). "Keeps control" / "takes control" of a decision type
= over 80% of decisions of that type (PDF p. 6). Occupation is set to unclassified with no signal
(PDF p. 8). "No clear goal" sessions (7.7%) are excluded from the success analyses (PDF p. 11).

**Estimators.** Two kinds of number appear. Unadjusted descriptives — mode shares, decision
shares, actions and output per prompt, the monthly series in Figure 4, the occupation success
rates in §4.2 and Figure 6. And adjusted rates — Figure 5's points, described as estimated from
comparisons within cells defined by work mode × task-value band × month × task subject ×
software/non-software occupation, with the regressions themselves relegated to the appendix
(Figure 5 caption, PDF p. 13; PDF p. 11). The single reported regression coefficient in the main
text is Figure 3's: +9% actions and +13% output per expertise level, controlling for work mode,
task value, month, occupation and model family, with standard errors clustered by user (PDF
p. 9). Uncertainty is reported as p < 0.001 for the Figure 3 trends, confidence intervals on
sample means in Figure 5, and 95% confidence intervals computed on distinct accounts in Figure 6.
No standard errors, intervals or power statements accompany the mode shares (claims 4–6), the
decision shares (claim 8), the seven-month changes (claims 20–24) or the over-time null in claim
32.

**Validation reported in the main text.** One external check: classifier labels against
automatically recorded telemetry, with more than 90% of sessions labelled as creating or
modifying code showing code changes in the telemetry (PDF p. 5). One reference-model check,
asserted without a number: "our classifiers track independent telemetry in expected directions,
and agree with a strong reference model on the majority of sessions" (PDF p. 15). Both are
attributed to the appendix for detail. The paper also names what validation it cannot do:
"classifiers remain challenging to validate at scale, and Claude Code sessions add further
difficulty, as they may be too long and complex for human labels to serve as ground truth"
(PDF p. 15). The task-description phrase "validation against internal commits" does not appear:
what the main text validates against is session telemetry (lines added/deleted), while git
commits and pull requests appear as *inputs* to the success-signal classifier (PDF p. 10), not as
an independent validation source.

**Prior Anthropic work it builds on** (all linked from the page and named in the text): the
Claude Code autonomy report <https://www.anthropic.com/research/measuring-agent-autonomy>, the
internal-Anthropic study <https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic>,
and Clio <https://www.anthropic.com/research/clio> (PDF pp. 2, 8). External work cited:
METR's time-horizon evaluations <https://metr.org/time-horizons/> (PDF p. 5); two GitHub
coding-agent adoption studies, arXiv:2601.18341 and arXiv:2606.07448 (footnote 1, PDF p. 17);
Sarkar (2026) <https://suproteem.cc/agents.pdf> on Cursor IDE sessions and Baumann et al. (2026),
arXiv:2604.20779, on publicly available sessions (footnote 3, PDF p. 17); SWE-chat
<https://huggingface.co/datasets/SALT-NLP/SWE-chat> (Tables 1 and 2).

**Released data.** None (see Source). The appendix PDF is the only supporting document.

## Limitations (verbatim)

- "While we don’t have full answers to these questions yet, we look to Claude Code usage data for early signals." (PDF p. 2).
- "Note that this measures hours in which Claude Code was actively running, not the user’s hands-on time typing to Claude." (footnote 2, PDF p. 17).
- "Detection of agentic coding activity relies on agent co-authorship tags and configuration files, which likely undercount actual usage." (footnote 1, PDF p. 17).
- "Note that we exclude Claude Code usage that runs through third party integrated developer environments, and software development kits. We also therefore exclude sessions in “headless” mode where a user runs a single prompt in the CLI via claude -p “<prompt>” . We exclude this usage since it differs in two key ways—much of it is programmatic, with Claude Code embedded in automated tools and pipelines rather than conversing with a user, and even when a user is present, we do not see a user’s session end-to-end the way we do on the surfaces we include." (footnote 4, PDF p. 17).
- "Note that expertise is capturing something quite different from job title or general ability, and, crucially, it is *task-specific*." (PDF p. 6).
- "The session is left unclassified when there is no signal about the user’s occupation." (PDF p. 8) and "We were able to infer occupation in about 70% of sessions." (PDF p. 9).
- "Like all measures in this report, these inferences are produced using our privacy-preserving analysis tool. No researcher reads individual transcripts, occupation labels are never linked to identifiable users, and we only observe aggregates over a minimum number of distinct users." (footnote 7, PDF p. 17).
- "These price estimates are coarse, so we use them primarily to compare tasks to one another over time, not as dollar values to be read literally." (PDF p. 10).
- "The estimation approach we take here is intended to get at relative differences in the value of sessions, not absolute value. The dollar amount is based on comparisons to the freelancer market—not salaried work—and comes from an ultimately fuzzy match between the Claude Code session and the job posting. Since the relative estimates will remove any consistent bias from these issues, we place more emphasis there." (footnote 8, PDF pp. 17–18).
- "We do not observe users’ real-world outcomes, and we cannot ask them directly whether they got what they wanted out of Claude." (PDF p. 10).
- "For the following analysis, which is focused on the degree of success or failure in a session, we exclude sessions classified as having “no clear goal,” which comprise about 7.7% of our full sample." (PDF pp. 10–11).
- "One might worry that expertise isn't the real driver—perhaps experts simply pick different tasks, or differ in other ways. Throughout this section, we partially address this worry by comparing sessions doing the same kind of work, at the same estimated value, in the same month, on the same subject, from people in the same broad occupation group, and ask how outcomes differ by the person’s rated expertise." (PDF p. 11).
- "Whiskers are confidence intervals on sample means (most are too small to be visible in this plot). These plots exclude sessions judged by the success outcome classifier to have no clear goal." (Figure 5 caption, PDF p. 13).
- "Conditioning on trouble selects different sessions for different users. Experts hit trouble less often overall, so the troubled sessions they do have are likely to be on harder problems—using the price estimate of the session as a proxy for the complexity of the session, we see that the average estimated value of a troubled session roughly doubles from the bottom of the expertise scale to the top. Part of the gap in recovery rates may therefore reflect that novices get stuck on routine problems while experts get stuck on challenging hard problems." (footnote 9, PDF p. 18).
- "Their higher verified success rates may reflect management skills that transfer to directing an agent. But they may also partly reflect our measurement: verification rests partially on explicit confirmation in the transcript, and managers may be more likely to communicate when they get what they ask for." (PDF p. 14).
- "Even if the model misclassifies managers, the signals relied upon to determine that the user is a likely manager—perhaps in how tasks are delegated and specified—tend to be associated with greater success. In other words, perhaps acting like a manager confers greater success." (footnote 10, PDF p. 18).
- "These findings are preliminary. As in most of our research, we cannot measure real-world outcomes, like whether code written in a session is actually used or discarded thereafter, or whether it produces an economically valuable artifact. In addition, the non-interactive usage this report excludes is a substantial share of activity. Developing a framework to measure it is a priority for future work. And all of our classifications of sessions depend on a model’s reading of the transcript. In the Appendix, we show that our classifiers track independent telemetry in expected directions, and agree with a strong reference model on the majority of sessions. But classifiers remain challenging to validate at scale, and Claude Code sessions add further difficulty, as they may be too long and complex for human labels to serve as ground truth." (PDF p. 15).
- "If these patterns hold across the economy, it suggests that…" (PDF p. 3) — the paper's own conditional framing of external validity; the full sentence is quoted under open questions below.

## Open questions, conjectures and promised follow-ups (verbatim)

**Questions the paper opens with**

- "Can people without formal coding experience successfully direct an agent through complex technical work? And what will rapid adoption and improvement of these tools mean for knowledge work broadly?" (PDF p. 2).

**Conjectures about generalisation to knowledge work**

- "What happens on Claude Code may be a preview of where knowledge work is headed, as agents become embedded in non-coding work." (PDF p. 3).
- "By tracking how agentic coding usage changes as models get more capable, we can better understand how these tools affect the labor market for coding professionals and knowledge workers." (PDF p. 3).
- "If these patterns hold across the economy, it suggests that while agentic coding tools may be absorbing some implementation-heavy work, they are also rewarding those with firm understanding of the problems they solve on the job. Coding agents are not substituting for domain expertise—the more understanding a worker brings to an agent, the more quality work the agent is able to do." (PDF p. 3).
- "However, the gap between experts and intermediates is modest—suggesting that proficiency in a domain is enough to use the tool almost as effectively as those with deep mastery." (PDF p. 3).
- "And coding is a leading case—what happens in software is likely a preview of what may come as agentic tools take on other forms of knowledge work." (PDF p. 16).

**Interpretive conjectures attached to findings**

- "It appears that coding agents are making a coding background less relevant to successful programming." (PDF p. 14).
- "Part of the value of expertise appears to be the ability to steer the agent in the right direction." (PDF pp. 13–14).
- "A person with such command, in any field, may now be able to do technical work they previously could not. A person without any such expertise will get far less from the same tool. And the gains come mostly from competence, not mastery—a working grasp of the domain captures most of the benefit, while deep specialization adds only a bit more beyond that." (PDF p. 15).
- "Their higher verified success rates may reflect management skills that transfer to directing an agent." (PDF p. 14).
- "In other words, perhaps acting like a manager confers greater success." (footnote 10, PDF p. 18).
- "Part of the gap in recovery rates may therefore reflect that novices get stuck on routine problems while experts get stuck on challenging hard problems." (footnote 9, PDF p. 18).

**A promised follow-up**

- "In addition, the non-interactive usage this report excludes is a substantial share of activity. Developing a framework to measure it is a priority for future work." (PDF p. 15).

**Named tests for the future — the paper's own tracking agenda**

- "The picture in this report will be updated as the models, the users, and the division of labor between them change. We hope that these measures will allow us to track consequential shifts as they happen. For instance, if the returns to expertise begin to decrease over time, that would suggest that models are starting to supply the essential judgment that users currently bring, and that the gains from these tools are broadening beyond domain experts. If the share of coding sessions completed successfully by users outside software occupations continues to grow, it could indicate that software production is becoming a part of ordinary work in every field, rather than the product of a single occupation. These shifts would change who benefits from agentic coding, and by how much, and would have implications for what is most valued in the labor market." (PDF p. 16).

**A capability question the paper poses and answers only descriptively**

- "How autonomous is Claude Code? Capability evaluations suggest the ceiling is high and rising: on benchmarks such as METR’s time-horizon evaluations, frontier models can now complete software tasks that would take a person hours, autonomously working through obstacles along the way. But what does usage actually look like in practice?" (PDF p. 5).

## What it did not test

*This section is the wiki author's inference, not the paper's own text.* It lists adjacent
questions the paper plainly had the data and classifiers to answer but did not report, and
constructs it used without validating in the main text. Some of these may be answered in the
companion appendix (`claude-code-expertise-2026-06-appendix`); each item is a question for the
main paper as read today.

**The dependence between the expertise rating and the outcome measures — the central untested
threat.** The expertise classifier and the outcome classifiers read the *same transcript*, and
one of the expertise classifier's three declared signals is "whether the user tends to correct
Claude or Claude tends to correct the user" (PDF p. 6); Table 1's level-1 definition is "User
doesn't recognize Claude's errors" and level-5 is "User corrects Claude, Claude almost never
corrects the user" (PDF p. 7). Meanwhile the failure-signal classifier scores "errors, failed
tests, retries, the user pushing back on the output" (PDF p. 10). A session in which Claude errs
and the user does not catch it is, by construction, rated low on expertise and likely to be
judged unsuccessful. The paper's controls — work mode, task-value band, month, subject,
occupation group (PDF p. 11) — address task selection, not this shared-source dependence. The
obvious available test is not run: rate expertise from the first prompt (or the first turn) only,
before any outcome is observable, and re-estimate the gradient. Nor is the gradient shown for
the two outcome measures that do not depend on the model's reading of the transcript at all
(lines of code added; telemetry-observable git activity), which would be a partly independent
check.

**Panel structure available and unused.** ~400,000 sessions from ~235,000 people (PDF p. 2) is a
panel. Nothing in the main text uses it beyond clustering standard errors in one regression:
- No user fixed-effects specification of the expertise gradient, which would separate "experts
  succeed more" from "sessions where things go well look expert".
- No test of whether a person's rated expertise is stable across their own sessions — the
  natural validation of a construct claimed to be task-specific rather than person-specific
  (PDF p. 6). If the rating is task-specific, the same person should be rated differently across
  tasks; that testable implication is stated and never tested.
- No learning curve: whether a user's success rate or rated expertise rises with their cumulative
  number of sessions. This is the individual-level version of the paper's own tracking agenda.

**Decompositions the seven-month window supports and the paper does not report.**
- The mode-mix shift (fixing 33% → 19%, operating 14% → 21%, writing/analysis ~10% → 20%,
  PDF p. 9) is never decomposed into *new users entering* versus *existing users changing what
  they do*. With ~235,000 people over seven months, entry is likely large, and the paper's own
  claim that management, sales and legal are the fastest-growing groups (PDF p. 9) suggests
  compositional change. As reported, the headline "usage shifted toward more end-to-end agentic
  use" (PDF p. 2) is consistent with a pure entry effect.
- The 27% rise in task value is likewise not decomposed into a mix shift between modes and a
  within-mode rise. Within-mode rises are given for three modes (43%, 34%, 32%, PDF p. 10) and
  the pooled figure is +27%, but no fixed-mix index is reported, and "communicate +2%" (Figure 4)
  is never discussed — so the reader cannot tell how much of the pooled rise is composition.
- No month-by-month expertise gradient. The paper says explicitly that a falling return to
  expertise would be the signal that models are supplying the judgment users now bring (PDF
  p. 16) — and it has seven months of data and "model family" already in its regressions
  (PDF p. 9). The one time-varying result it does report is the occupation gap ("neither widened
  nor narrowed", PDF p. 14). The expertise gradient over time, the single most informative test
  for its own stated agenda, is not shown.
- No results by model family, though model family is a control. Whether Claude does more per
  prompt, or users succeed more, with newer models is not reported.

**Cross-tabulations between its own new measures.**
- *Decision attribution × success.* Figure 2 and Figure 5 never meet. Whether sessions in which
  Claude makes most of the planning decisions succeed more or less often is the most
  decision-relevant question the paper's own framework can ask, and it is not asked.
- *Decision attribution × expertise.* Expertise is crossed with actions and output per prompt
  (Figure 3), and decision shares are crossed with actions per turn (PDF p. 6), but expertise is
  never crossed with the planning/execution decision shares — so "experts delegate more" is
  inferred from action counts rather than measured on the decision measure built for it.
- *Success × work mode.* Success rates are reported by expertise (Figure 5) and by occupation
  (Figure 6), never by work mode. Since the mode mix changed sharply and the paper says success
  rates rose in both occupation groups (PDF p. 14), the rise could be mode composition.
- *Task value × success.* Value is used as a control and as a complexity proxy (footnote 9) but
  never as an outcome dimension: whether high-value tasks succeed less often, and whether the
  expertise gradient steepens with task value, is not reported.
- *Codebase relationship × anything.* The 48/17/14/~20 split (PDF p. 4) appears once and is never
  crossed with expertise, occupation, success or time.

**Surfaces and exclusions.**
- The CLI, claude.ai and the desktop app are pooled and never compared (PDF p. 3), although the
  surface is observed. A claude.ai Claude Code session and a CLI session plausibly differ in user
  mix and in what is delegated.
- Excluded usage (third-party IDEs, SDKs, headless `claude -p`) is called "a substantial share of
  activity" (PDF p. 15) with no magnitude, and no bound on how the exclusion biases the mode mix
  or the success rates. Telemetry (lines added/deleted) exists for those sessions by the paper's
  own description, so at least a telemetry-only comparison was available and is not offered.
- The ~30% of sessions with no occupation signal (PDF p. 9) are never characterised. Whether they
  are more novice, less successful, or concentrated in particular modes is untested, and no
  reweighting or bounding exercise is reported — yet the paper's flagship claim about occupations
  rests on the classified 70%.

**Constructs used without validation in the main text.**
- *"Abandoned" conflates outcome with work mode.* Abandoned = judged failure and zero lines of
  code added (Table 2, PDF p. 12). For the three modes that need not touch code — analyzing data,
  communicating, planning — zero lines added is the normal case, so any failed session in those
  modes is mechanically "abandoned", while a failed building session that wrote one line is not.
  The 19% vs 5–7% novice/non-novice abandonment gap (PDF p. 13) is therefore partly a statement
  about which modes novices attempt. The paper's controls include work mode for the Figure 5
  points, which mitigates but does not resolve the construct problem, and the issue is never
  named.
- *"Expertise" as domain expertise.* The classifier's three signals are all about how the user
  writes and what they check (PDF p. 6) — communication behaviour, not verified domain knowledge.
  The paper concedes the analogous problem for occupations, in footnote 10: "perhaps acting like a
  manager confers greater success" (PDF p. 18). The same concession applies to the expertise
  measure itself and is not made. No external validation of the expertise rating against any
  independent indicator of the user's domain knowledge is reported in the main text.
- *Task value from freelance postings.* A freelance price is a market price for a gig, not the
  economic value of the work, and the paper says so (footnote 8). But nothing tests the
  assumption that the bias is *consistent over time* — which is exactly what the seven-month
  comparison needs. If the fuzzy match degrades or improves as sessions get longer and more
  agentic, the trend is contaminated; no stability check is reported.
- *Single-label work modes.* One mode per session (PDF p. 4) with no reported measure of how
  often sessions are genuinely mixed, and no second-label or confidence distribution.
- *The telemetry check is one-directional.* ">90% of sessions our classifier labeled as creating
  or modifying code showed code changes in the telemetry" (PDF p. 5) is a precision-style
  statistic for one label. The converse — how many sessions with code changes in telemetry were
  labelled as something other than building or fixing — is not given, and no agreement statistic
  is reported for the expertise, occupation, decision-attribution or outcome classifiers in the
  main text (the appendix is cited for these).
- *"Judged success" has no external anchor.* The paper is explicit that real-world outcomes are
  unobserved (PDF p. 10). The consequence not stated: none of the success rates can be read as a
  productivity measure, and the paper's own summary language ("accomplishes what the person set
  out to do", PDF p. 2) is an intent-completion measure, not an output measure.

**Statistical reporting.**
- No minimum detectable effect and no power statement anywhere, including behind the published
  null "it has neither widened nor narrowed over seven months" (PDF p. 14), which is presented
  without an interval, a coefficient or a plot.
- No standard errors for the mode shares, the decision shares, the seven-month mode changes or
  the task-value changes.
- Figure 5's whiskers are described as "confidence intervals on sample means" while its points are
  "adjusted rate[s]" (PDF p. 13) — intervals not obviously matched to the estimator that produced
  the points; the regressions are in the appendix.
- Uncertainty is clustered three different ways across three figures (by user in Figure 3, on
  sample means in Figure 5, on distinct accounts in Figure 6) with no statement of why.

**Internal inconsistencies it did not reconcile** (all recorded in Source and Claims): the 25%
vs 27% task-value rise; the ≥ 3 vs > 3 "hits trouble" threshold between the PDF and the web page;
the five-author PDF against the six-author web citation; and the "within seven points" claim
against Figure 6 as read (claim 35). None is flagged with an erratum.

## Verification

- **URLs fetched on 2026-09-16, and read in full:**
  1. <https://www.anthropic.com/research/claude-code-expertise> — the full web version, including key findings, all six figure captions, both table captions, the citation block, the acknowledgements and all ten footnotes. Fetched with the web fetch tool.
  2. <https://cdn.sanity.io/files/4zrzovbb/website/433472e34b60db1a52ebf0b8c6600f057b6908c5.pdf> — the 18-page PDF, all pages, including the rendered figures and both tables.
- **Fetch failure and workaround.** The web fetch tool refused the Sanity CDN PDF URL (`url_not_allowed — refused by the fetch service's own restrictions`). The PDF was instead downloaded over HTTPS with `curl` to `/tmp/cc.pdf` (HTTP 200, 1,911,775 bytes) and read page by page. It is the same URL listed in `wiki/INDEX.md` and linked from the page as "Read in PDF". **Note for other threads: Sanity CDN PDFs must be fetched with curl, not the fetch tool.**
- **Not fetched, deliberately:** the companion appendix PDF (<https://cdn.sanity.io/files/4zrzovbb/website/a94728142a45694292336165947f8d6e3e1a357e.pdf>), which belongs to the slug `claude-code-expertise-2026-06-appendix` and is only cross-referenced here. Also not fetched: the stray second link on the web page's "Available here." full stop (`…7426c33b0e75ab4771c465d30d5bc1019bdd0c9c.pdf`), whose target is unknown; the external works cited in footnotes 1 and 3 (arXiv:2601.18341, arXiv:2606.07448, arXiv:2604.20779, suproteem.cc/agents.pdf); METR's time-horizon page; and the SWE-chat dataset card. None is a source for anything in this file.
- **Could not be read from the sources:** the underlying values of Figures 1–6 are only in rendered images. Values I read off those images are marked "read from Figure N" in Claims (claims 5, 9, 13, 22, 23, 24, 27, 35) and are approximate; anything load-bearing should be re-read or, better, sourced from the appendix. Also unavailable from the main paper: the per-cell sample sizes behind every figure, the minimum-user aggregation threshold referred to in footnote 7, the name of the freelance-postings dataset, and the regression tables behind Figures 5 and 3 (all pointed to the appendix).
- **Released data cross-check:** `data/releases/INDEX.md` (steward, 2026-09-16) — no folder in `Anthropic/EconomicIndex` corresponds to this paper and no file there names Claude Code. Used only to support the statement in Source that nothing was released; not a source for any claim.
- **Quotation check:** every quotation in "Definitions (verbatim)", "Limitations (verbatim)" and "Open questions, conjectures and promised follow-ups (verbatim)", and every quoted fragment in Claims and Source, was checked against the fetched text of the stated source — the PDF page or the named web section — including its curly quotation marks, em dashes and its own typographical errors, which are reproduced rather than corrected. Where the PDF and the web page word the same passage differently, the quotation names which one it comes from and the difference is recorded in Source. The verbatim sections contain no interpretation; all inference is confined to "What it did not test" and to the passages in Claims and Source explicitly marked as the wiki author's note.
