# economic-index-2025-04-software-development

Anthropic Economic Index: AI's impact on software development — the special report comparing
Claude Code with Claude.ai coding conversations.

## Source

- **Title:** "Anthropic Economic Index: AI's impact on software development" (page `<title>`: "Anthropic Economic Index: AI's impact on software development \ Anthropic").
- **Authors:** none named anywhere on the page. No author byline, no acknowledgements, no author list. The page carries Anthropic's topic tags "Societal Impacts" and "Economics" and closes with a recruiting block for the "Economist" and "Data Scientist (Policy)" roles, which is the only signal of the team behind it.
- **Date:** Apr 28, 2025 (dateline on the page: "Apr 28, 2025").
- **Primary URL:** <https://www.anthropic.com/research/impact-software-development> (canonical, per the page's own `canonical` meta tag).
- **Other URLs:** no separate PDF, no arXiv version, no appendix file. The appendix is a section of the same web page. Linked Anthropic sources from the body: the first Economic Index report <https://www.anthropic.com/news/the-anthropic-economic-index>, the education report <https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude>, the Clio paper page <https://www.anthropic.com/research/clio>, the Claude Code docs, and the Artifacts support article.
- **Document type:** web-only research report ("report", not a paper). A special / off-cycle Economic Index release: it is not one of the numbered Economic Index waves and has no accompanying data folder.
- **Approximate length:** short — roughly 1,900 words of body text (excluding site navigation, footer and "Related content"), organised as an untitled opening, a numbered three-item summary, four H3 sections, a Limitations section, a "Looking ahead" close, an Appendix and three footnotes. Five exhibits: one hero illustration and four data figures (a stacked bar chart of collaboration patterns; two charts labelled "Line graph" in their alt text but described in the captions as bars, for top coding use cases and top programming languages; a dot-gap chart of project types), plus one appendix table image.
- **The data it rests on:** 500,000 coding-related Claude interactions from Claude.ai (Free and Pro only) and Claude Code (first-party API sessions only), all from April 6–13, 2025, classified with Clio. Per-platform counts are not given beyond "The initial sample was split evenly across Claude.ai and Claude Code" (Footnote 1).
- **Was any of it released?** No. No dataset, no code, no notebook, no figure data accompanies this report. Cross-checked against the steward's enumeration of the Hugging Face dataset `Anthropic/EconomicIndex` (`data/releases/INDEX.md`, 2026-09-16): there is no `release_2025_04*` folder and no file anywhere in the repository whose name mentions Claude Code. Every number in this report is therefore a published figure with no public microdata behind it.

## Claims

Each claim is given with the section heading (or figure/footnote) it appears under, the number as
published, and the comparison it rests on.

1. **Computer-related occupations are heavily over-represented in Claude use (restated from earlier work).** Opening (untitled): "we found very disproportionate use of Claude by US workers in computer-related occupations: that is, there were many more conversations with Claude about computer-related tasks than one would predict from the number of people working in relevant jobs." No number given here; the comparison is conversation share against employment share, and the citation is to the first Economic Index report.
2. **The same over-representation appears in education.** Opening: "Computer Science degrees—which involve large amounts of coding—show highly disproportionate AI use." No number given; cited to the education report.
3. **Sample size: 500,000 interactions.** Opening and "How we analyzed conversations on Claude Code and Claude.ai": "we conducted an analysis of 500,000 coding-related interactions across Claude.ai … and Claude Code"; "We analyzed the 500,000 total Claude interactions (split between Claude Code and Claude.ai)". The 500,000 is the total across both surfaces, not per surface.
4. **Claude Code is 79% automation; Claude.ai coding is 49%.** "Three key patterns", item 1: "79% of conversations on Claude Code were identified as “automation”—where AI directly performs tasks—rather than “augmentation,” where AI collaborates with and enhances human capabilities (21%). In contrast, only 49% of Claude.ai conversations were classified as automation." Repeated in "How do developers interact with Claude?": "79% of conversations involved some form of automation, compared to 49% on Claude.ai." Comparison: Claude Code vs Claude.ai, automation share of conversations, within coding-related conversations only.
5. **Feedback Loop is nearly twice as common on Claude Code: 35.8% vs 21.3%.** "How do developers interact with Claude?": "“Feedback Loop” patterns … were nearly twice as common on Claude Code (35.8% of interactions) as Claude.ai (21.3%)." Comparison: share of interactions on each surface. (35.8/21.3 = 1.68, so "nearly twice" is generous; the wiki author notes this, the report does not.)
6. **Directive is higher on Claude Code: 43.8% vs 27.5%.** Same section: "“Directive” conversations, where Claude completed a task with minimal user interaction, were also higher on Claude Code (43.8%, versus 27.5% on Claude.ai)."
7. **Every augmentation subtype is lower on Claude Code.** Same section: "All the patterns of augmentation—including “Learning,” where the user acquires knowledge from the AI model—were substantially lower on Claude Code than on Claude.ai." No per-subtype numbers are given in the text for Task Iteration, Learning or Validation; they appear only inside the stacked bar chart image.
8. **Humans remain in the loop even inside automation.** Same section: "our results do show that even within automation, humans are still very often involved: “Feedback Loop” interactions still require user input (even if that input is simply pasting error messages back to Claude)." The claim rests on the qualitative content of the Feedback Loop category, not on a separate measurement.
9. **No single language dominates, but web languages lead.** "What are developers building with Claude?": "Although no single language dominated, the primarily web-focused development languages of JavaScript and TypeScript together accounted for 31% of all queries". Comparison: share of queries pooled across both platforms with equal platform weights.
10. **HTML and CSS add a further 28%.** Same section: "HTML and CSS (other languages for user-facing code) together added another 28%." Carries Footnote 2 on Artifacts inflating HTML for Claude.ai.
11. **Python is 14% of queries; SQL 6%.** Same section: "notably, Python was at 14% of queries"; "Combined with SQL (another data-focused language, making up 6% of queries)". The report immediately qualifies the interpretation: "Python serves dual purposes—both for back-end development and data analysis", so these "likely included many data science and analytics applications beyond traditional back-end development."
12. **Two of the top five coding tasks are user-facing app work: 12% and 8%.** Same section: "Two of the top five tasks were focused on user-facing app development: “UI/UX Component Development” and “Web & Mobile App Development” each accounted for 12% and 8% of conversations, respectively." Pooled across platforms.
13. **Generic engineering tasks are common on both surfaces.** Same section: "Conversations that related to more generic uses, such as “Software Architecture & Code Design” and “Debug and Performance Optimization” were also highly represented in both Claude.ai and Claude Code." No numbers in the text; the split sits in the figure.
14. **Startups are the early adopters of Claude Code; enterprises lag — summary version: 33% vs 13%.** "Three key patterns", item 3: "In a preliminary analysis, we estimated that 33% of conversations on Claude Code served startup-related work, compared to only 13% identified as enterprise-relevant applications."
15. **Startups vs enterprises — body version: 32.9% startup and 23.8% enterprise on Claude Code, against 25.9% enterprise on Claude.ai.** "Who is using Claude for coding?": "Startup work accounted for 32.9% of Claude Code conversations (nearly 20% higher than their Claude.ai usage), whereas enterprise work represented only 23.8% of Claude Code conversations (slightly below their 25.9% share on Claude.ai)." Carries Footnote 3 on Claude For Work exclusion. **Wiki author's note, not the report's:** claims 14 and 15 disagree. The summary's enterprise figure for Claude Code is 13%; the body's is 23.8%. Also, "nearly 20% higher" is consistent only with a Claude.ai startup share of about 13% (32.9 − 13 ≈ 20 percentage points), which suggests the summary's "13%" may be the Claude.ai *startup* share mislabelled as the enterprise share. The page as fetched on 2026-09-16 contains both numbers; no erratum or revision note appears on the page. Any post that quotes an enterprise share from this report must say which of the two it is quoting.
16. **Individuals, not only businesses, are half the coding usage.** Same section: "uses involving students, academics, personal project builders, and tutorial/learning users collectively represent half of the interactions across both platforms. In other words, individuals—not just businesses—are significant adopters of coding assistance tools."
17. **Adoption pattern read as a repeat of earlier technology shifts.** Same section: "These adoption patterns mirror past technology shifts, where startups use new tools for competitive advantage while established organizations move more cautiously and often have detailed security checks in place before adopting new tools company-wide." Interpretive, offered without new evidence.
18. **Unclassifiable project types: 5% of Claude.ai and 2% of Claude Code conversations, dropped and renormalised.** "Limitations": "we included an option for ‘Could Not Classify’, which Claude opted for in 5% of Claude.ai conversations and 2% of Claude Code conversations. We excluded this category from analysis and renormalized the results."
19. **Coding is more automative than non-coding use within Claude.ai, and Feedback Loop drives it: +18.3% against -11.2% Directive.** "Appendix": "Compared to use cases that don’t involve software, software development is more automative. A significant increase in Feedback Loops (+18.3%) drives this and, notably, offsets a clear *decrease* in Directive behaviors (-11.2%)." Comparison: software vs non-software conversations, within Claude.ai only, "because Claude Code specializes in software applications." The signs are software minus non-software, and the report does not say whether they are percentage points or relative changes (wiki author's note: percentage points is the reading consistent with the Claude.ai subtype shares reported above). The report's gloss: "AI-assisted coding currently requires a lot of human reviewing and iteration relative to non-coding tasks, even when Claude does the bulk of the work."
20. **Weighting rule behind every pooled percentage.** Footnote 1 and both language/task figure captions: the Claude.ai side was filtered for coding, and "To account for the filter, we renormalized analyses to equally weight Claude Code and Claude.ai interactions, where applicable." The captions restate it: "Because Claude Code and Claude.ai are equally weighted, the portions of the bars that correspond to each of the platforms represent half of that platform's usage." Every pooled number (claims 9–13, 16) is therefore a 50/50 platform average, not a usage-weighted population share.

## Definitions (verbatim)

All quotations from the page as fetched 2026-09-16; curly quotation marks are reproduced as they
appear in the source.

- **Claude.ai** — "Claude.ai (the “default” way that most people interact with Claude)" (opening).
- **Claude Code** — "Claude Code (our new specialist coding “agent” that can independently accomplish chains of complex tasks using a variety of digital tools)" (opening).
- **Automation** — "79% of conversations on Claude Code were identified as “automation”—where AI directly performs tasks" ("Three key patterns", item 1); and "we separated out “automation,” where AI directly performs tasks, from “augmentation,” where AI collaborates with a user to perform a task" ("How do developers interact with Claude?").
- **Augmentation** — "“augmentation,” where AI collaborates with and enhances human capabilities" ("Three key patterns", item 1); and "“augmentation,” where AI collaborates with a user to perform a task" ("How do developers interact with Claude?").
- **Directive** — "Directive: Complete task delegation with minimal interaction" (caption to the first figure); and "“Directive” conversations, where Claude completed a task with minimal user interaction" ("How do developers interact with Claude?").
- **Feedback Loop** — "Feedback Loop: Task completion guided by environmental feedback" (caption to the first figure); and "“Feedback Loop” patterns, where Claude completes tasks autonomously but with help of human validation (for example, where the user sends any errors back to Claude)" ("How do developers interact with Claude?").
- **Task Iteration** — "Task Iteration: Collaborative refinement process" (caption to the first figure).
- **Learning** — "Learning: Knowledge acquisition and understanding" (caption to the first figure); and "“Learning,” where the user acquires knowledge from the AI model" ("How do developers interact with Claude?").
- **Validation** — "Validation: Work verification and improvement" (caption to the first figure).
- **The analysis tool (Clio)** — "our privacy-preserving analysis tool, which distills user conversations into higher-level, anonymized insights. Here, we used it to identify the topic of the conversation (e.g. “UI/UX component development”), or—as we’ll explain below—to categorize a conversation as focusing on “augmentation” versus “automation”" ("How we analyzed conversations on Claude Code and Claude.ai").
- **Back-end development languages** — "Back-end development languages (used for behind-the-scenes logic, databases, and infrastructure, as well as API and AI development)" ("What are developers building with Claude?").
- **Web-focused / user-facing languages** — "the primarily web-focused development languages of JavaScript and TypeScript"; "HTML and CSS (other languages for user-facing code)" ("What are developers building with Claude?").
- **Vibe coding** — "a phenomenon known as “vibe coding”—where developers of varying levels of experience describe their desired outcomes in natural language and let AI take the wheel on implementation details" ("What are developers building with Claude?").
- **Project type (the startup / enterprise / personal measure)** — "We used our analysis system to identify the type of project (e.g. a personal project vs. a project done for a startup) that best described users’ coding-related interactions" ("Who is using Claude for coding?").
- **"Could Not Classify"** — "we included an option for ‘Could Not Classify’, which Claude opted for in 5% of Claude.ai conversations and 2% of Claude Code conversations" ("Limitations").
- **The unit behind pooled language and task percentages** — "Percentages represent total percentages of coding-related tasks across both platforms. Because Claude Code and Claude.ai are equally weighted, the portions of the bars that correspond to each of the platforms represent half of that platform's usage." (captions to the coding-use-case and programming-language figures; the language caption opens "Percentages of coding language uses represent total percentages across both platforms.").
- **The project-type figure's encoding** — "The distance between the dots indicates the gap in the prevalence of each type of project on Claude.ai (blue) and Claude Code (orange)." (caption to the project-type figure).
- **The appendix table's contents** — "Breakdown of automation and augmentation by software versus non-software use cases in Claude.ai. For a description of each pattern, see the caption to the first figure above." (appendix figure caption).
- **The sample (Claude.ai side, Claude Code side, window, filter, weighting)** — "Claude.ai conversations were specifically those from Claude.ai Free and Pro. This sample only includes Claude Code sessions powered by the first-party API (Claude Code can be powered by Anthropic first-party APIs or third party cloud provider APIs). All conversations used in our analysis across Claude.ai and Claude Code were from April 6-13, 2025. The initial sample was split evenly across Claude.ai and Claude Code and for Claude.ai, we applied a Claude-based filter to select conversations related to coding. To account for the filter, we renormalized analyses to equally weight Claude Code and Claude.ai interactions, where applicable." (Footnote 1).
- **Artifacts treatment inside the HTML figure** — "While we filter out Artifacts that are unrelated to coding, we don’t explicitly filter out Artifacts that contain coding-related content from the analysis because significant coding usage happens within Artifacts." (Footnote 2).
- **What "Claude.ai" excludes for the enterprise measure** — "Claude.ai usage does not include Claude For Work (Team and Enterprise plans) usage" (Footnote 3).

## Data and methods

In my own words, with references to the section each fact comes from.

**Products and surfaces.** Two surfaces, compared head to head: Claude.ai and Claude Code
(opening; "How do developers interact with Claude?"). The Claude.ai side is consumer only —
Free and Pro plans, explicitly excluding Claude For Work (Team and Enterprise) — and the Claude
Code side covers only sessions powered by Anthropic's first-party API, not Claude Code running
through third-party cloud provider APIs (Footnote 1; Footnote 3; "Limitations", first bullet).
Team, Enterprise and general API usage are outside the sample altogether.

**Window.** A single eight-day window, April 6–13, 2025 (Footnote 1). No other period is
analysed, so nothing in the report is a trend; every comparison is cross-sectional across
surfaces, languages, tasks or project types.

**Sample and sample construction.** 500,000 coding-related interactions in total across both
surfaces ("How we analyzed…"). The initial draw was split evenly between Claude.ai and Claude
Code; the Claude.ai half was then passed through a Claude-based filter that kept conversations
related to coding (Footnote 1). Because that filter shrinks the Claude.ai side only, the report
renormalises so that Claude Code and Claude.ai carry equal weight in pooled statistics (Footnote
1; both figure captions). No per-surface n, no per-cell n, no confidence interval and no
significance test appears anywhere in the report. The unit of analysis is described
interchangeably as an "interaction", a "conversation", a "session" (Claude Code) and a "query"
(languages) — the report does not reconcile these.

**Classifiers.** All classification is done with Clio, Anthropic's privacy-preserving analysis
tool, which turns conversations into aggregated, anonymised categories ("How we analyzed…").
Four classification tasks are visible:
1. *Coding relevance*, on the Claude.ai side only, as the filter (Footnote 1).
2. *Collaboration pattern* — the automation/augmentation split and its five subtypes, carried
   over from the earlier Economic Index reports ("How do developers interact with Claude?").
   The report never states the arithmetic, but the published subtypes sum to the published
   headline shares if automation = Directive + Feedback Loop and augmentation = Task Iteration
   + Learning + Validation (Claude Code 43.8 + 35.8 = 79.6 ≈ 79%; Claude.ai 27.5 + 21.3 =
   48.8 ≈ 49%) — wiki author's arithmetic, consistent with the earlier reports' framework.
3. *Topic* — the conversation's coding task, e.g. "UI/UX component development"; and programming
   language ("How we analyzed…"; "What are developers building with Claude?").
4. *Project type* — startup, enterprise, personal project, student, academic, tutorial/learning,
   inferred from conversation content, with a "Could Not Classify" escape option ("Who is using
   Claude for coding?"; "Limitations").

**Thresholds and exclusions.** The only explicit rule is the treatment of "Could Not Classify":
5% of Claude.ai and 2% of Claude Code conversations, excluded and the remainder renormalised
("Limitations"). Artifacts are partially filtered: Artifacts unrelated to coding are removed,
coding-related Artifacts are kept, which the report says probably inflates HTML on the Claude.ai
side (Footnote 2). No minimum-cell threshold, no privacy floor, no aggregation rule is stated —
unlike the numbered Economic Index releases, this report publishes no data, so no such
thresholds are needed.

**Methods.** Descriptive shares and differences in shares only. No regression, no reweighting to
an external population, no O\*NET or SOC mapping, no geography, no model-version comparison, no
uncertainty quantification. The one auxiliary analysis is the appendix's software vs non-software
comparison of collaboration patterns, run inside Claude.ai only "because Claude Code specializes
in software applications" ("Appendix").

**Released data and code.** None. The report links to no dataset and no notebook, and the
Hugging Face `Anthropic/EconomicIndex` repository has no folder for it (see Source). The
implication for us: nothing in this report can be reproduced from public data; it can only be
cited, or tested indirectly against later releases that do publish data.

## Limitations (verbatim)

From the "Limitations" section unless another reference is given.

- Preamble: "Our analysis is grounded in real-world AI use—how developers are actually using Claude in their workflows. Although this approach gives our findings practical relevance, it also brings inherent limitations."
- "We analyzed data from Claude.ai and Claude Code only. We excluded Team, Enterprise, and API usage that might show different patterns, particularly in professional settings;"
- "The boundary between automation and augmentation becomes increasingly blurred with agentic tools like Claude Code. For example, the “Feedback Loop” pattern differs qualitatively from traditional automation, because it still requires user supervision and input. We will likely need to extend the automation/augmentation framework to account for new agentic capabilities;"
- "Our categorization of who is using Claude for coding relied on inference from limited context. When categorizing conversations as “startup” versus “enterprise” work, or “personal” versus “academic” projects, our analysis tool made educated guesses based on incomplete information. Some classifications might therefore be incorrect. Additionally, we included an option for ‘Could Not Classify’, which Claude opted for in 5% of Claude.ai conversations and 2% of Claude Code conversations. We excluded this category from analysis and renormalized the results;"
- "Our dataset likely captures early adopters. These users might not represent the broader developer population, and this self-selection could skew usage patterns towards more experienced or technically adventurous users;"
- "Due to privacy considerations, we only analyzed data within a specific retention window, potentially missing cyclical patterns in software development (such as sprint cycles or release schedules);"
- "The representativeness of Claude usage is unclear, relative to overall AI coding assistance adoption. Many developers use multiple AI tools beyond Claude, meaning we present only a partial view of their AI engagement patterns;"
- "We only studied what developers delegate to AI—not how they ultimately use AI outputs in their codebase, the quality of the resulting code, or whether these interactions effectively improved productivity or code quality."
- "Who is using Claude for coding?": "Because we don’t know the real-world context in which Claude’s responses were being used, these analyses rely on uncertain inferences from incomplete data. We therefore treat these findings as more preliminary than the ones described above."
- "Three key patterns", item 3: "In a preliminary analysis, we estimated that…"
- "What are developers building with Claude?": "However, Python serves dual purposes—both for back-end development and data analysis. Combined with SQL (another data-focused language, making up 6% of queries), these languages likely included many data science and analytics applications beyond traditional back-end development."
- "What are developers building with Claude?": "Speculatively, these findings suggest that jobs that center on making simple applications and user interfaces might face earlier disruption from AI systems if increasing capabilities cause “vibe coding” to shift more into mainstream workflows."
- Footnote 2: "The HTML numbers for Claude.ai are likely inflated slightly because Artifacts leverage HTML. While we filter out Artifacts that are unrelated to coding, we don’t explicitly filter out Artifacts that contain coding-related content from the analysis because significant coding usage happens within Artifacts."
- Footnote 3: "Claude.ai usage does not include Claude For Work (Team and Enterprise plans) usage, which implies that enterprise numbers for Claude.ai specifically are likely undercounted because a significant amount of enterprise usage on Claude.ai occurs within the Claude For Work product."
- "Looking ahead": "Although we can’t assume that the lessons we draw from software development will directly carry over to other types of occupation, software development might be a leading indicator that gives us useful information about how other occupations might change with the rollout of increasingly capable AI models in the future."

## Open questions, conjectures and promised follow-ups (verbatim)

**Conjectures attached to the three key patterns** (each is the italicised sentence that closes
the numbered item):

- Item 1: "*This might imply that as AI agents become more commonplace, and as more agentic AI products are built, we should expect more automation of tasks.*"
- Item 2: "*This suggests that jobs that center on making simple applications and user interfaces may face disruption from AI systems sooner than those focused purely on backend work*."
- Item 3: "*The adoption gap suggests a divide between nimbler organizations using cutting-edge AI tools, and traditional enterprises.*"

**From "How do developers interact with Claude?"**

- "As more agentic products are released, we might see differences in the way AI is integrated into people’s jobs. At least in the case of coding, this might involve more automation of tasks."
- "This raises questions about the extent to which developers will still be involved as AI use becomes more common."
- "But it’s by no means certain that this pattern will persist into the future, when more capable agentic systems will likely require progressively less user input."

**From "What are developers building with Claude?"**

- "As AI increasingly handles component creation and styling tasks, these developers might shift toward higher-level design and user experience work."

**From "Who is using Claude for coding?"**

- "AI's general-purpose nature could accelerate this dynamic: If AI agents provide significant productivity gains, the gap between early and late adopters could translate into substantial competitive advantages."

**A promised methodological follow-up, from "Limitations"**

- "We will likely need to extend the automation/augmentation framework to account for new agentic capabilities;"

**From "Looking ahead"**

- "Our findings raise many questions. Will the prevalence of “feedback loops,” where humans are still involved in the process, persist as AI capabilities advance, or will we see a shift toward more complete automation?"
- "As AI systems become capable of building larger-scale pieces of software, will developers shift to mostly managing and guiding these systems, rather than writing code themselves?"
- "Which software development roles will change the most, and which might disappear entirely?"
- "The increasing coding skills of AI might also be especially consequential for AI development itself. Since so much of AI research and development relies on software, it’s possible that advancements in AI-assisted coding help to speed up breakthroughs, creating a positively-reinforcing cycle that accelerates AI progress even further."
- "In the grand scheme of things, AI systems are extremely new. But in a relative sense, coding is among the most developed uses of AI in the economy. That makes it worth watching."

**A stated recruiting interest, from "Work With Us"** — relevant to the threads map as a signal
of what the team wanted next: "If you’re interested in working at Anthropic to research the
effects of AI on the labor market, we encourage you to apply for our Economist and Data
Scientist (Policy) roles."

## What it did not test

*This section is the wiki author's inference, not the report's own text.* It lists adjacent
questions the report plainly had the data to answer but did not report, and constructs it used
without validating.

**Cross-tabulations it had in hand and did not report.** Every conversation in the sample was
labelled by at least three classifiers (collaboration pattern, topic/language, project type),
yet no two labels are ever crossed:

1. **Collaboration pattern × task type.** Is "UI/UX Component Development" more Directive than
   "Debug and Performance Optimization"? The report's own story — that user-facing work is the
   most exposed — would be far stronger if the exposed tasks were also the automated ones. Not
   reported.
2. **Collaboration pattern × language.** Whether the web languages carry the automation share,
   or whether the automation gap between surfaces survives holding language constant. Not
   reported, and this is the obvious test of whether Claude Code's 79% is a surface effect or a
   composition effect.
3. **Collaboration pattern × project type.** Do startup conversations automate more than
   enterprise ones? Key patterns 1 and 3 sit side by side without ever being crossed, so the
   report cannot say whether the agentic surface or the startup user is doing the work.
4. **Task type × project type.** Whether startups' Claude Code use is the user-facing work or
   the back-end work — the difference between the report's disruption conjecture applying to
   small firms or to large ones.
5. **Reweighting Claude.ai's coding conversations to Claude Code's task mix** (or vice versa), a
   one-line decomposition that would separate "the agent automates more" from "the agent is used
   for different jobs". Not attempted.
6. **Within-surface day-of-week variation.** The report names sprint cycles as a blind spot
   because of the retention window, but it had eight consecutive days and never reports whether
   the shares move across them — the cheapest available check on the stability of its headline.
7. **The appendix comparison on the other margins.** The software vs non-software appendix is run
   on collaboration patterns only; the same contrast on project type (are coding conversations
   more startup-weighted than non-coding ones?) is not run, though the classifier existed.

**Measures of the agentic surface it did not take.** The report's central object is an agent
that "can independently accomplish chains of complex tasks", but nothing in it measures depth of
autonomy: no turn counts, no session lengths, no number of tool calls, no task duration, no
count of human interventions per session. "Feedback Loop" is used as a proxy for human
involvement without ever quantifying how much involvement. The AI-autonomy construct that later
Economic Index work uses is absent here.

**Joins to the rest of the Index it did not make.** No O\*NET task or SOC occupation mapping, so
these coding conversations cannot be placed inside the Index's occupation series; no geography,
so nothing on whether the Claude Code automation gap differs by country or US state; no model
version comparison, though the window sits between the Claude 3.7 Sonnet wave and later ones; no
first-party API comparison, even though the Claude Code side *is* first-party API traffic and the
Claude.ai side is not — meaning surface and access route are confounded and never separated.

**Constructs used without validation.**

- *The automation/augmentation classifier applied to an agentic surface.* The report itself says
  the boundary "becomes increasingly blurred" with tools like Claude Code, and then reports a
  79% automation share from that same framework. No agreement statistic, no human audit, no
  re-labelling exercise is offered to show the framework still separates cleanly on Claude Code.
  The comparison it headlines is exactly the comparison its own limitation undermines.
- *The project-type classifier.* Called preliminary and based on "educated guesses", with no
  human-validated accuracy rate, no confusion matrix, and no sensitivity analysis on the
  excluded 5%/2% "Could Not Classify" bucket. Whether the unclassifiable conversations look like
  enterprises (plausibly the most context-poor) is untested, yet they are dropped and the rest
  renormalised.
- *The Claude.ai coding filter.* No precision or recall is reported for the filter that defines
  the entire Claude.ai comparison group, so the 49% automation share is conditional on an
  unmeasured selection step.
- *Language attribution.* Percentages are "of all queries" by language, with no statement of
  whether a conversation can carry more than one language, and therefore whether the shares are
  a partition or overlapping. The language shares quoted (31 + 28 + 14 + 6 = 79%) leave a
  residual that is never described.
- *The equal-weighting choice.* Pooled percentages are 50/50 platform averages by construction.
  No unweighted or usage-weighted alternative is shown, so the reader cannot tell how much of
  "JavaScript and TypeScript = 31%" is a statement about developers and how much about the
  weighting rule.
- *The unit of analysis.* "Interaction", "conversation", "session" and "query" are used
  interchangeably across the text, figures and footnote, with no statement that they are the
  same denominator. A Claude Code session and a Claude.ai conversation are very unlikely to be
  comparable units of work, and the report does not argue that they are.

**An internal inconsistency it did not reconcile.** The enterprise share of Claude Code
conversations is 13% in key pattern 3 and 23.8% in "Who is using Claude for coding?" (see claim
15). The page carries no erratum. This is a trap for anyone citing the report.

## Verification

- **URLs fetched on 2026-09-16:** <https://www.anthropic.com/research/impact-software-development> — fetched in full, including the appendix, all figure captions and all three footnotes. This is the only source used for every quotation in this file.
- **Also queried on 2026-09-16:** the Internet Archive availability API for this URL at timestamp 20250501 (<http://archive.org/wayback/available?url=anthropic.com/research/impact-software-development&timestamp=20250501>). It returned no 2025 snapshot; the closest archived capture is 20260826. The 13% / 23.8% inconsistency noted in claim 15 therefore could **not** be checked against a contemporaneous April 2025 capture — it is recorded as it stands in the live page today.
- **Could not be fetched:** nothing that was sought. There is no PDF, no arXiv version and no separate appendix or methodology document for this report; the appendix is part of the page. The numeric contents of the four data figures (the per-subtype augmentation shares for Task Iteration, Learning and Validation; the full top-task and top-language rankings; the full project-type list; the appendix table's cell values) exist only inside images and are not machine-readable from the page, so only the numbers stated in the body text or captions are recorded above. Figure alt text was captured and is quoted where it defines an exhibit.
- **Released data cross-check:** `data/releases/INDEX.md` (steward, 2026-09-16) — no `release_2025_04*` folder in `Anthropic/EconomicIndex`, and no file in the repository names Claude Code. Used only to support the statement that nothing was released; not a source for any claim.
- **Quotation check:** every quotation in the "Definitions (verbatim)", "Limitations (verbatim)" and "Open questions, conjectures and promised follow-ups (verbatim)" sections, and every quoted fragment in "Claims", was checked character-for-character against the fetched text of the page, including its curly quotation marks, hyphens and em dashes. The verbatim sections contain no interpretation; all inference is confined to "What it did not test" and to the passages in "Claims" and "Data and methods" explicitly marked as the wiki author's note.
