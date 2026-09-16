# work-at-anthropic-2025-12

"How AI is transforming work at Anthropic" — the firm-level study of Anthropic's own engineers and
researchers: a 132-person survey, 53 interviews with survey respondents, and ~200,000 internal
Claude Code transcripts from February and August 2025.

The only supporting document is the survey instrument, "Claude at Work Survey" (5 pp), released so
that "others can evaluate our approach and adapt it for their own research" (web, "Survey data").
Both were fetched and read in full for this entry.

## Source

- **Title:** "How AI is transforming work at Anthropic" (the H1, the HTML `<title>`, the `og:title`
  and the `twitter:title` all agree). The BibTeX block title-cases it: "How AI Is Transforming Work
  at Anthropic".
- **Authors (BibTeX block):** "Saffron Huang and Bryan Seethor and Esin Durmus and Kunal Handa and
  Miles McCain and Michael Stern and Deep Ganguli" — seven. **Maxim Massenkoff, the intended mentor,
  is not an author and is not thanked.** This is a Societal Impacts piece, not an Economics-team
  piece; of the Economic Index authors only Peter McCrory appears, in the acknowledgements.
- **Contribution statement, and a gap in it.** "Saffron Huang led the project, designed and executed
  the surveys, interviews, and data analysis, plotted figures and wrote the blog post. Bryan Seethor
  co-designed the surveys and interviews, co-led survey and interview data collection, analyzed
  interview themes, contributed to writing, and managed the project timeline. Esin Durmus contributed
  to experiment design and provided detailed direction and feedback throughout. Kunal Handa
  contributed infrastructure for the interviewing process. Deep Ganguli provided critical guidance
  and organizational support. All authors provided detailed guidance and feedback throughout."
  (web, "Acknowledgments"). Two of the seven BibTeX authors — Miles McCain and Michael Stern — have
  no described contribution.
- **Acknowledgements:** Ruth Appel, Sally Aldous, Avital Balwit, Drew Bent, Zoe Blumenfeld, Miriam
  Chaum, Jack Clark, Jake Eaton, Sarah Heck, Kamya Jagadish, Jen Martinez, Peter McCrory, Jared
  Mueller, Christopher Nulty, Sasha de Marigny, Sarah Pollack, Hannah Pritchett, Stuart Ritchie,
  David Saunders, Alex Tamkin, Janel Thamkul, Sar Warner, Heather Whitney; figures illustrated by
  Casey Yamaguma; "productive comments and discussion from Anton Korinek, Ioana Marinescu, Silvana
  Tenreyro, and Neil Thompson" (web, "Acknowledgments"). The four commenters are academic economists;
  no economist is an author.
- **Date:** December 2, 2025 (page dateline "Dec 2, 2025"; BibTeX `date = {2025-12-02}`). The data
  are older than the publication date: the survey and interviews were fielded in **August 2025** and
  the transcript comparison uses **February and August 2025**.
- **Primary URL:** <https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic>
  (canonical meta tag). The BibTeX gives the same URL with a trailing slash and no `www`.
- **Survey instrument URL:**
  <https://assets.anthropic.com/m/6cd21f7d4f82afcb/original/Claude-at-Work-Survey.pdf> — 5 pages,
  24 numbered questions, linked once from the body as "our survey questions".
- **Document type.** Web-only research post; **there is no PDF of the post itself** and no arXiv
  version. Its topic tag is "Societal Impacts" — not "Economics". `wiki/INDEX.md` types it `paper`;
  read as a document it is a long research blog post with an appendix, in the same family as the
  Economic Index reports but outside the Index's numbered series and outside its data releases.
- **Structure.** Untitled framing section; "Key findings" (three blocks of numbered bullets: four
  survey findings, five interview findings, three Claude Code findings); "Survey data" (§"What
  coding tasks are people using Claude for?", §"Usage and productivity", §"Claude enabling new work",
  §"How much work can be fully delegated to Claude?"); "Qualitative interviews" (§"AI delegation
  approaches" with "Trust but verify" and "What tasks do people keep for themselves?"; §"Skill
  transformations" with "New capabilities…", "…and less hands-on practice", "Will we still need those
  hands-on coding skills?", "The craft and meaning of software engineering"; §"Changing social
  dynamics in the workplace"; §"Career uncertainty and adaptation"); "Claude Code usage trends"
  (§"Tackling harder problems with less oversight", §"Distribution of tasks", §"Fixing papercuts",
  §"Task variation across teams"); "Looking forward"; BibTeX; Acknowledgments; "Appendix" whose only
  sub-section is "Limitations". Five figures, all rendered images; one table (the delegation-criteria
  table in "AI delegation approaches").
- **Where the numbers live.** Every published number in this file is in prose or in a figure caption.
  The five figure images carry alt text **identical** to their bold captions, so there are no
  alt-text-only numbers here (contrast `economic-index-2025-02-report`). No values were read off any
  chart image, per `room/director-2026-09-16-alt-text-ruling.md`; consequently the full distributions
  in Figures 1, 2, 4 and 5 are recorded below only to the extent the prose states them.
- **The data it rests on.** (i) A 132-response internal survey of "Anthropic engineers and
  researchers", August 2025; (ii) 53 in-depth interviews with survey respondents; (iii) "200,000
  internal transcripts from Claude Code from February and August 2025", analysed with Clio, "our
  [privacy-preserving analysis tool](https://www.anthropic.com/research/clio)". One external number
  is imported: a "67% increase in merged pull requests … per engineer per day", cited to a
  third-party newsletter, not to an Anthropic analysis.
- **Was anything released?** **No microdata, no aggregates, no code.** The instrument PDF is the only
  artefact. The transcripts are internal-employee Claude Code sessions and are not part of
  `Anthropic/EconomicIndex`; the survey and interview responses were not anonymous (question 1 asks
  the respondent's name) and are not released. The study is citable and, for the survey portion,
  *replicable elsewhere* by design — the instrument is public — but not reproducible.
- **Relation to the rest of the corpus.** The opening paragraph positions it against the Economic
  Index: "Our [previous research](https://www.anthropic.com/economic-index) on AI's economic impacts
  looked at the labor market as a whole, covering a variety of different jobs. But what if we studied
  some of the earliest adopters of AI technology in more detail—namely, us?" It links forward to the
  policy post `economic-policy-responses-2025-10` and to the AI fluency framework. It is in turn
  named as prior work by `claude-code-expertise-2026-06`, which cites it as "the internal-Anthropic
  study" (see `wiki/reports/claude-code-expertise-2026-06.md`, Data and methods). Whether the later
  publications answer its open questions is for `programme/LEDGER.md`; the candidates are
  `anthropic-interviewer-2025-12` (published two days later), `skill-formation-rct-2026-01` and
  `claude-code-expertise-2026-06`.

## Claims

Numbered. Each carries its section (and figure, where relevant), the number **as published**, and
the comparison it rests on. `S` = survey, `I` = interviews, `CC` = Claude Code transcripts.

**Design and sample**

1. **Three instruments, one firm, August 2025** (S, I, CC). "Turning the lens inward, in August 2025
   we surveyed 132 Anthropic engineers and researchers, conducted 53 in-depth qualitative interviews,
   and studied internal [Claude Code](https://www.anthropic.com/claude-code) usage data to find out
   how AI use is changing things at Anthropic." (web, framing section). Comparison: none — this is the
   design statement. The unit of study is one employer, not a labour market.
2. **How the 132 were recruited** (Appendix, "Limitations"). "We posted the survey across multiple
   internal Slack channels, yielding 68 responses, and we also selected 20 diverse teams across
   research and product functions from the organizational chart and directly messaged 5-10
   individuals per team (n=207 total outreach), getting a 31% response rate for the final 64
   responses. We interviewed the first 53 people who responded." 68 + 64 = 132; 31% of 207 = 64.2.
   Comparison: two sampling arms — convenience (Slack) and purposive (outreach) — whose results are
   never reported separately.
3. **The transcript corpus** (CC). "Because survey respondents reported Claude Code as the majority
   of their usage, we used our [privacy-preserving analysis
   tool](https://www.anthropic.com/research/clio) to analyze 200,000 internal transcripts from Claude
   Code from February and August 2025." (web, "Claude Code usage trends"). Comparison: two single
   months six months apart, not a continuous series.
4. **Model era** (framing section; Appendix). "At the time this data was collected, Claude Sonnet 4
   and Claude Opus 4 were the most capable models available, and capabilities have continued to
   advance."

**Survey: what Claude is used for**

5. **Daily-use ranking** (S, Figure 1). "Most employees (55%) used Claude for debugging on a daily
   basis. 42% used Claude everyday for code understanding, and 37% used Claude everyday for
   implementing new features." (web, "What coding tasks are people using Claude for?"). Comparison:
   share of respondents selecting "Daily" for each task category, across the 11 categories of
   instrument question 9. Figure 1's caption: "**Figure 1: Proportion of daily users (x-axis) for
   various coding tasks (y-axis).**" The other eight categories' daily shares are in the image only
   and are not recorded here.
6. **The least frequent tasks, with the paper's own explanation** (S, Figure 1). "The less-frequent
   tasks were high level design/planning (likely because these are tasks people tend to keep in human
   hands), as well as data science and front-end development (likely because they are overall less
   common tasks)." No numbers are given for these three.
7. **Self-report and usage data agree on the ranking** (S vs CC). "This roughly aligns with the
   Claude Code usage data distribution reported in the “Claude Code usage trends” section." (web,
   "What coding tasks are people using Claude for?"); restated as "The overall task frequency
   distribution estimated from usage data roughly aligns with the self-reported task frequency
   distribution." (web, "Distribution of tasks"). Comparison: two differently-constructed task
   distributions (11 self-reported categories vs the transcript classifier's categories), asserted to
   "roughly align" with no agreement statistic.

**Survey: usage and productivity — the headline**

8. **Usage and productivity, then and now** (S). "Employees self-reported that 12 months ago, they
   used Claude in 28% of their daily work and got a +20% productivity boost from it, whereas now,
   they use Claude in 59% of their work and achieve +50% productivity gains from it on average." …
   "The year-on-year comparison is quite dramatic—this suggests a more than 2x increase in both
   metrics in one year." (web, "Usage and productivity"). Comparison: **within-respondent recall** —
   the same person's estimate of August 2024 against their estimate of August 2025, both given in
   August 2025. No contemporaneous 2024 measurement exists.
9. **The key-findings version of claim 8 differs** (S). "Employees self-report using Claude in 60% of
   their work and achieving a 50% productivity boost, a 2-3x increase from this time last year."
   (web, "Key findings", survey bullet 2). 60% against the body's 59%, and "a 2-3x increase" against
   the body's "more than 2x". Nothing reconciles them; 28→59 is 2.1× and 20→50 is 2.5×, so "2-3x"
   spans the two and "more than 2x" is true of both. **Wiki author's note:** a post citing this must
   say which of 59% / 60% it is citing.
10. **Power users** (S). "Usage and productivity are also strongly correlated, and at the extreme end
    of the distribution, 14% of respondents are increasing their productivity by more than 100% by
    using Claude—these are our internal “power users.”" (web, "Usage and productivity"). "Strongly
    correlated" is asserted without a coefficient, an n, or a scatter. The 14% is the share choosing
    the top, open-ended band of instrument question 16 ("I get >100% more done in the same time").
11. **An external corroboration, from a newsletter** (not Anthropic analysis). "(This roughly
    corroborates the 67% increase in merged pull requests—i.e. successfully incorporated changes to
    code—per engineer per day we saw when we adopted Claude Code [across our Engineering
    org](https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built).)" (web, "Usage and
    productivity"). Comparison: a self-reported +50% productivity gain against a +67% merged-PR rate
    whose only citation is a third-party newsletter post about how Claude Code is built. No window,
    no denominator, no engineer count, and no internal replication of the PR figure is given.
12. **Time down, output up** (S, Figure 2). "Across almost all task categories, we see a net decrease
    in time spent, and a larger net increase in output volume". Figure 2's caption: "**Figure 2:
    Impact on time spent (left panel) and output volume (right panel) by task (y-axis). The x-axis on
    each plot corresponds to either a self-reported decrease (negative values), increase (positive
    values) or no change (vertical dashed line) in time spent or output volume for categories of
    Claude-assisted tasks, compared to not using Claude. Error bars show 95% confidence intervals.
    Circle area is proportional to the number of responses at each rating point. Only respondents who
    reported using Claude for each task category are included.**" Comparison: per-task-category means
    of a five-point subjective change scale (instrument questions 11 and 13), against a "no change"
    reference line. This is the study's only figure with confidence intervals.
13. **The time-saving distribution is bimodal** (S, free text). "However, when we dig deeper into the
    raw data, we see that the time saving responses cluster at opposite ends—some people spend
    significantly *more* time on tasks that are Claude-assisted." No share is given for the
    time-increasing group. The reasons are respondents' own: more debugging and cleanup of Claude's
    code ("when I vibe code myself into a corner"), "cognitive overhead for understanding Claude's
    code since they didn't write it themselves", and enabling effects — "persist on tasks that I
    previously would've given up on immediately".
14. **The mechanism claim** (S). "Productivity is very hard to measure directly, but this
    self-reported data suggests that AI enables increased productivity at Anthropic primarily through
    greater output volume." (web, "Usage and productivity"). Comparison: the output-volume panel of
    Figure 2 against the time-spent panel.
15. **Design and planning gain least** (S, Figure 2; stated in the interviews section). "This is
    reflected in our survey data, which showed the least productivity gains for design and planning
    tasks (Figure 2)." (web, "What tasks do people keep for themselves?").

**Survey: new work, enjoyment, delegation**

16. **27% would not otherwise have been done** (S). "Employees estimated that 27% of their
    Claude-assisted work wouldn't have been done without it." (web, "Claude enabling new work"); in
    the key findings, "**27% of Claude-assisted work consists of tasks that wouldn't have been done
    otherwise**, such as scaling projects, making nice-to-have tools (e.g. interactive data
    dashboards), and exploratory work that wouldn't be cost-effective if done manually." Comparison:
    a self-assessed counterfactual (instrument question 17), banded 0-20% … 80-100%. Named examples:
    scaling projects, nice-to-haves, documentation and testing, exploratory work, "papercuts".
17. **The transcript corroboration of claim 16** (CC). "We looked for this in our usage data analysis
    as well, and found that 8.6% of Claude Code tasks involve ‘papercut fixes.’" (web, "Claude
    enabling new work"). **Wiki author's note:** 27% (of *work*, self-assessed, counterfactual) and
    8.6% (of *transcripts*, classifier-assigned, "papercut" category) are different constructs on
    different denominators; the text offers the second as evidence for the first.
18. **44% of Claude-assisted work is work they would not have enjoyed** (S; reported inside the
    interviews table). "In our survey, on average people said that 44% of Claude-assisted work
    consisted of tasks they wouldn't have enjoyed doing themselves." (web, "AI delegation approaches",
    "Repetitive or boring" row). Instrument question 19, same banding.
19. **Full delegation stays low** (S). "Although engineers use Claude frequently, more than half said
    they can “fully delegate” only between 0-20% of their work to Claude." (web, "How much work can be
    fully delegated to Claude?"), i.e. more than half chose the *lowest* band of instrument question
    20. Key-findings version: "**Most employees use Claude frequently while reporting they can “fully
    delegate” 0-20% of their work to it.**" Comparison: frequency of use against a self-defined
    ceiling on hand-off. The interpretation offered: "This suggests that engineers tend to collaborate
    closely with Claude and check its work rather than handing off tasks without verification, and
    that they set a high bar for what counts as “fully delegated.”"

**Interviews: themes (no theme counts are published, with one exception)**

20. **Delegation criteria** (I). Six named categories, each evidenced by quotation in a one-column
    table: "Outside the user's context *and* low complexity"; "Easily verifiable"; "Well-defined or
    self-contained"; "Code quality isn't critical"; "Repetitive or boring"; "Faster to prompt than
    execute". Comparison: the criteria are then matched to METR's — "These factors mentioned by our
    employees in their decisions about delegation were similar to those found to explain AI-related
    productivity slowdowns (such as high developer familiarity with codebase, large and complex
    repositories) in an [external study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
    from METR."
21. **Trust progression** (I). "Many users described a progression in their Claude usage that involved
    delegating increasingly complex tasks over time". The Google Maps analogy is the extended
    illustration.
22. **Engineers split on using Claude inside vs outside their expertise** (I). "Engineers are split on
    whether to use Claude within or outside their expertise." No split count.
23. **What people keep** (I). "People consistently said they didn't use Claude for tasks involving
    high-level or strategic thinking, or for design decisions that require organizational context or
    “taste.”" With the boundary described as "a “moving target,” though, regularly renegotiated as
    models improve".
24. **Capability expansion — "more full-stack"** (I). "Many employees report completing work
    previously outside their expertise—backend engineers building UIs; researchers creating
    visualizations." Comparison: the same pattern is claimed in the survey (claim 16) and in the
    transcripts (claim 32).
25. **Skill atrophy and lost incidental learning** (I). "At the same time, some were worried about
    “skills atrophying as [they] delegate more”, and losing the incidental (or “collateral”) learning
    that happens during manual problem-solving". No share of interviewees is given.
26. **The paradox of supervision** (I). "One reason that the atrophy of coding skills is concerning is
    the “paradox of supervision”—as mentioned above, effectively using Claude requires supervision,
    and supervising Claude requires the very coding skills that may atrophy from AI overuse." This is
    the study's own coinage and its most-cited conceptual contribution.
27. **Divergence on craft and meaning** (I). "​​Engineers diverge sharply on whether they miss
    hands-on coding." … "Whether people embrace AI assistance or mourn the loss of hands-on coding
    seems to depend on what aspects of software engineering they find most meaningful."
28. **Claude displaces colleague questions** (I). "One of the more prominent themes was that Claude
    has become the first stop for questions that once went to colleagues." Evidence is quotation: "I
    ask way more questions [now] in general, but like 80-90% of them go to Claude"; "It has reduced my
    dependence on [my team] by 80%, [but] the last 20% is crucial and I go and talk to them". These
    are individual respondents' numbers, not measurements.
29. **The one quantified interview theme.** "About half reported unchanged team collaboration
    patterns." (web, "Changing social dynamics in the workplace"). Half of the 53, on an
    interviewer-coded judgement; no coding protocol or reliability check is reported.
30. **Mentorship effects** (I). "Several pointed out the impact on traditional mentorship dynamics,
    because “Claude can provide a lot of coaching to junior staff” instead of senior engineers."
31. **Role shift towards managing agents** (I). "Many engineers describe their role shifting from
    writing code to managing AIs. Engineers increasingly see themselves as “manager[s] of AI
    agents”—some already “constantly have at least a few [Claude] instances running.” One person
    estimated their work has shifted “70%+ to being a code reviewer/reviser rather than a net-new code
    writer”". And: "In the longer term, career uncertainty is widespread."

**Claude Code transcripts: February vs August 2025**

32. **Task complexity rose 3.2 → 3.8** (CC, Figure 3). "We estimated task complexity of each
    transcript on a 1-5 scale where 1 corresponds to “basic edits” and 5 is “expert-level tasks
    requiring weeks/months of human expert work”. Task complexity increased from 3.2 to 3.8 on
    average.  To illustrate the difference between the scores: tasks averaging 3.2 included
    “Troubleshoot Python module import errors” while tasks averaging 3.8 included “Implement and
    optimize caching systems.”" Comparison: mean classifier rating, February 2025 vs August 2025.
33. **Maximum consecutive tool calls rose 9.8 → 21.2, +116%** (CC, Figure 3). "**The maximum number
    of consecutive tool calls Claude Code makes per transcript increased by 116%.** Tool calls
    correspond to actions Claude takes using external tools like making edits to files or running
    commands. Claude now chains together 21.2 independent tool calls without need for human
    intervention versus 9.8 tool calls from six months ago." Comparison: mean of the per-transcript
    **maximum**, two months. (21.2 / 9.8 = 2.16.)
34. **Human turns fell 6.2 → 4.1, −33%** (CC, Figure 3). "**The number of human turns decreased by
    33%.** The average number of human turns decreased from 6.2 to 4.1 per transcript, suggesting
    that less human input is necessary to accomplish a given task now compared to six months ago."
    Figure 3's caption: "**Figure 3. Changes in Claude Code usage between August 2025 and February
    2025 (x-axes). Average task complexity increased over time (left panel), average maximum
    consecutive tool calls per transcript increased over time (middle panel), and number of human
    turns decreased over time (right panel). Error bars show 95% confidence intervals. The data
    suggest people are increasingly delegating more autonomy to Claude over time.**" (Note the
    caption names the two periods in reverse chronological order.)
35. **The key-findings gloss of claims 33–34 changes the statistic.** "**Claude is handling
    increasingly complex tasks more autonomously**. Six months ago, Claude Code would complete about
    10 actions on its own before needing human input. Now, it generally handles around 20, needing
    less frequent human steering to complete more complex workflows (Figure 3)." (web, "Key
    findings", Claude Code bullet 1). **Wiki author's note:** the measured quantity is the *maximum*
    consecutive tool-call chain per transcript (9.8 → 21.2); the key finding renders it as what Claude
    "generally handles", i.e. as typical. The two are not the same quantity, and the typical chain
    length is never published. This is the number most often quoted from this study
    (e.g. "~21 consecutive actions before human input"), so the distinction matters.
36. **Task mix shifted towards features and design** (CC, Figure 4). "The most striking change between
    February and August 2025 is that there now are proportionately many more transcripts using Claude
    to implement new features (14.3% → 36.9%) and do code design or planning (1.0% → 9.9%)."
    Figure 4's caption: "**Figure 4. Distribution of various coding tasks (y-axis) as a percentage of
    the overall number of records (x-axis). We compare the distribution 6 months ago (pink) to
    present day (purple). The y-axis is ordered by frequency in Feb 2025.**" Comparison: share of
    transcripts, multi-label ("one or more types of coding tasks"), two months. The key-findings
    version rounds: "code design/planning (1% to 10% of usage) and implementing new features (14% to
    37%)".
37. **The shift's interpretation is left open by the authors.** "This shift in the relative
    distribution of Claude Code tasks may suggest that Claude has become better at these more complex
    tasks, though it could also reflect changes in how teams adopt Claude Code for different
    workflows rather than increases in absolute work volume (see Appendix for more limitations)."
38. **Papercut fixes are 8.6% of current tasks** (CC). "We found from the survey that engineers now
    spend more time making small quality-of-life improvements; in line with this, 8.6% of current
    Claude Code tasks are classified as “papercut fixes”. These include larger tasks such as creating
    performance visualization tools and refactoring code for maintainability, as well as smaller
    tasks like creating terminal shortcuts." Comparison: none — the 8.6% is August-only; no February
    papercut share is published, so the "now spend more time" framing rests on the survey, not on the
    transcripts.
39. **Team-level task mixes** (CC, Figure 5, August only). "The **Pre-training** team (who help to
    train Claude) often uses Claude Code for building new features (54.6%), much of which is running
    extra experiments." — "The **Alignment & Safety** and **Post-training** teams do the most
    front-end development (7.5% and 7.4%) with Claude Code, often for creating data visualizations."
    — "The **Security** team often uses Claude Code for code understanding (48.9%), specifically
    analyzing and understanding the security implications of different parts of the codebase." —
    "**Non-technical** employees often use Claude Code for debugging (51.5%), such as troubleshooting
    network issues or Git operations, as well as for data science (12.7%); Claude appears to be
    valuable for bridging gaps in technical knowledge." Figure 5's caption: "**Figure 5. Each
    horizontal bar represents a team (y-axis) with segments showing the proportion of that team's
    Claude Code usage for different coding tasks (x-axis), color-coded by coding task (legend). Top
    bar (“All Teams”) represents the overall distribution.**" Comparison: each team's single-label
    task distribution against the "All Teams" baseline. Only the five teams named above have
    published numbers; the rest are in the image only. Note this is a **different classification**
    from Figure 4 — "we refined our classification approach to assign each August transcript to a
    single primary coding task".
40. **The overall August mix** (CC, Figure 5). "The "All Teams" bar shows the overall distribution,
    with the most common tasks being building new features, debugging, and code understanding. This
    provides a baseline for team-specific comparisons." No shares published in prose.
41. **The full-stack claim, from the transcripts** (CC). "And whereas the data suggests that teams do
    use Claude for their core tasks (for instance, the Infrastructure team most commonly uses Claude
    Code for infrastructure and DevOps work), Claude often also augments their core tasks (for
    instance, researchers use Claude for front-end development to better visualize their data). This
    suggests that Claude is enabling everyone to become more full-stack in their work." Comparison:
    each team's own core-task share against its off-core shares, within August.
42. **The triangulation claim** (CC vs S). "These usage data corroborate the survey data: engineers
    delegate increasingly complex work to Claude and Claude requires less oversight. It seems
    plausible that this is driving the observed productivity gains." (web, "Tackling harder problems
    with less oversight"). This is the study's only causal statement about productivity, and it is
    hedged to "seems plausible".
43. **The generalisation claim, hedged both ways.** "We recognize that studying AI's impact at a
    company building AI means representing a privileged position—our engineers have early access to
    cutting-edge tools, work in a relatively stable field, and are themselves contributing to the AI
    transformation affecting other industries. Despite this, we felt it was on balance useful to
    research and publish these findings, because what's happening inside Anthropic for engineers may
    still be an instructive harbinger of broader societal transformation." (framing section), against
    "It's still early days—Anthropic has many early adopters internally, the landscape is rapidly
    changing, and our findings likely don't generalize to other organizations or contexts right now"
    (web, "Looking forward").

## Definitions (verbatim)

Quoted in full with the source named. Curly quotation marks, em dashes and the sources' own
punctuation are reproduced.

**Population and sample rules**

- **Who was studied** — "in August 2025 we surveyed 132 Anthropic engineers and researchers,
  conducted 53 in-depth qualitative interviews, and studied internal Claude Code usage data to find
  out how AI use is changing things at Anthropic." (web, framing section).
- **How the survey was distributed** — "We surveyed 132 Anthropic engineers and researchers from
  across the organization about their Claude use, to better understand how exactly they were using it
  day-to-day. We distributed our survey through internal communication channels and direct outreach to
  employees across diverse teams representing both research and product functions." (web, "Survey
  data").
- **The sampling design, in full** — "We selected respondents through both convenience sampling and
  purposive sampling (to ensure broad organizational representation). We posted the survey across
  multiple internal Slack channels, yielding 68 responses, and we also selected 20 diverse teams
  across research and product functions from the organizational chart and directly messaged 5-10
  individuals per team (n=207 total outreach), getting a 31% response rate for the final 64 responses.
  We interviewed the first 53 people who responded." (Appendix, "Limitations").
- **Who the interviewees were** — "we conducted in-depth interviews with 53 of the Anthropic engineers
  and researchers who responded to the survey, to get more insight into how they're thinking and
  feeling about these changes in the workplace." (web, "Qualitative interviews").
- **The transcript sample** — "Because survey respondents reported Claude Code as the majority of
  their usage, we used our privacy-preserving analysis tool to analyze 200,000 internal transcripts
  from Claude Code from February and August 2025." (web, "Claude Code usage trends").
- **The transcript sampling rule** — "Our Claude Code analysis uses proportionate sampling across time
  periods, which means we can only measure relative changes in task distribution, not absolute changes
  in work volume." (Appendix, "Limitations").
- **The model era** — "this research was conducted in August 2025 when Claude Sonnet 4 and Claude Opus
  4 were our state-of-the-art models." (Appendix, "Limitations"); and "At the time this data was
  collected, Claude Sonnet 4 and Claude Opus 4 were the most capable models available, and
  capabilities have continued to advance." (framing section).

**Task categories, as glossed on the page**

- **The four illustrated categories** — "We asked the surveyed engineers and researchers to rate how
  often they used Claude for various types of coding tasks, such as “debugging” (using Claude to help
  fix errors in code), “code understanding” (having Claude explain existing code to help the human
  user understand the codebase), “refactoring” (using Claude to help restructure existing code), and
  “data science” (e.g. having Claude analyze datasets and make bar charts)." (web, "What coding tasks
  are people using Claude for?").
- **Figure 1's unit** — "Figure 1: Proportion of daily users (x-axis) for various coding tasks
  (y-axis)." (Figure 1 caption).

**The survey's own constructs**

- **"Fully delegate", and its acknowledged ambiguity** — "(It's worth noting that there is variation
  in how respondents might interpret “fully delegate”—from tasks needing no verification at all to
  those that are reliable enough to require only light oversight.)" (web, "How much work can be fully
  delegated to Claude?").
- **New work** — "One thing we were curious about: Is Claude enabling qualitatively new kinds of work,
  or would Claude-assisted work have been done by employees eventually (albeit potentially at a slower
  rate)?" (web, "Claude enabling new work").
- **Figure 2's unit and scale** — "Figure 2: Impact on time spent (left panel) and output volume
  (right panel) by task (y-axis). The x-axis on each plot corresponds to either a self-reported
  decrease (negative values), increase (positive values) or no change (vertical dashed line) in time
  spent or output volume for categories of Claude-assisted tasks, compared to not using Claude. Error
  bars show 95% confidence intervals. Circle area is proportional to the number of responses at each
  rating point. Only respondents who reported using Claude for each task category are included."
  (Figure 2 caption).

**The Claude Code measures**

- **Task complexity** — "We estimated task complexity of each transcript on a 1-5 scale where 1
  corresponds to “basic edits” and 5 is “expert-level tasks requiring weeks/months of human expert
  work”." (web, "Tackling harder problems with less oversight"). The three intermediate anchors are
  not published.
- **Tool calls** — "Tool calls correspond to actions Claude takes using external tools like making
  edits to files or running commands." (same section).
- **The autonomy statistic** — "The maximum number of consecutive tool calls Claude Code makes per
  transcript increased by 116%." … "Claude now chains together 21.2 independent tool calls without
  need for human intervention versus 9.8 tool calls from six months ago." (same section).
- **Human turns** — "The average number of human turns decreased from 6.2 to 4.1 per transcript,
  suggesting that less human input is necessary to accomplish a given task now compared to six months
  ago." (same section).
- **The Figure 4 classification (multi-label)** — "We classified Claude Code transcripts into one or
  more types of coding tasks, studying how the uses for different tasks have evolved over the last six
  months" (web, "Distribution of tasks"), with the unit "Distribution of various coding tasks (y-axis)
  as a percentage of the overall number of records (x-axis)." (Figure 4 caption).
- **The Figure 5 classification (single-label, August only)** — "To study how tasks currently vary
  across teams, we refined our classification approach to assign each August transcript to a single
  primary coding task, and split the data by internal teams (y-axis)." (web, "Task variation across
  teams").
- **"Papercut fixes"** — in the interviews, "they can now fix more “papercuts” that previously damaged
  quality of life, such as refactoring badly-structured code, or building “small tools that help
  accomplish another task faster.”" (web, "Claude enabling new work"); in the transcripts, "8.6% of
  current Claude Code tasks are classified as “papercut fixes”. These include larger tasks such as
  creating performance visualization tools and refactoring code for maintainability, as well as
  smaller tasks like creating terminal shortcuts." (web, "Fixing papercuts"). The classifier
  definition itself is not published.
- **"Fixing papercuts", as summarised in the key findings** — "8.6% of Claude Code tasks involve
  fixing minor issues that improve quality of life, like refactoring code for maintainability (that
  is, “fixing papercuts”) that people say would typically be deprioritized." (web, "Key findings").

**The study's own coinages**

- **The paradox of supervision** — "One reason that the atrophy of coding skills is concerning is the
  “paradox of supervision”—as mentioned above, effectively using Claude requires supervision, and
  supervising Claude requires the very coding skills that may atrophy from AI overuse." (web, "…and
  less hands-on practice").
- **Collateral learning** — "losing the incidental (or “collateral”) learning that happens during
  manual problem-solving" (web, "…and less hands-on practice"), illustrated by the respondent's own
  definition: "If you were to go out and debug a hard issue yourself, you're going to spend time
  reading docs and code that isn't directly useful for solving your problem—but this entire time
  you're building a model of how the system works. There's a lot less of that going on because Claude
  can just get you to the problem right away."
- **Becoming "full-stack"** — "Engineers report “becoming more full-stack… I can very capably work on
  front-end, or transactional databases, or API code, where previously I would've been scared to touch
  stuff I'm less of an expert on.”" (web, "New capabilities…").
- **The delegation criteria, verbatim from the table** (web, "AI delegation approaches"):
  - "**Outside the user's context *and* low complexity**: “I use Claude for things where I have low
    context, but think that the overall complexity is also low.”"
  - "**Easily verifiable:** “It's absolutely *amazing* for everything where validation effort isn't
    large in comparison to creation effort.”"
  - "**Well-defined or self-contained:** “If a subcomponent of the project is sufficiently decoupled
    from the rest, I'll get Claude to take a stab.”"
  - "**Code quality isn't critical:** “If it's throwaway debug[ging] or research code, it goes straight
    to Claude. If it's conceptually difficult or needs some very specific type of debug injection, or
    a design problem, I do it myself.”"
  - "**Repetitive or boring:** “The more excited I am to do the task, the more likely I am to not use
    Claude. Whereas if I'm feeling a lot of resistance… I often find it easier to start a conversation
    with Claude about the task.”"
  - "**Faster to prompt than execute:** “[For] a task that I anticipate will take me less than 10
    minutes... I'm probably not going to bother using Claude.”"
- **The cold-start problem** (respondent's definition, quoted in the same table) — "“The cold start
  problem is probably the biggest blocker right now. And by cold start, I mean there is a lot of
  intrinsic information that I just have about how my team's code base works that Claude will not have
  by default… I could spend time trying to iterate on the perfect prompt [but] I'm just going to go
  and do it myself.”"

**The survey instrument, quoted in full**

Source throughout: "Claude at Work Survey",
<https://assets.anthropic.com/m/6cd21f7d4f82afcb/original/Claude-at-Work-Survey.pdf>, 5 pp, fetched
2026-09-16. Six section headings: "Basic Information", "AI Usage - 12 Months Ago", "Current AI Usage
and Impact", "Work Delegation and Preferences", "AI Usage Patterns", "Future Projections (12 Months
From Now)". Twenty-four numbered items; the page each appears on is given.

*Basic Information (p. 1)*

- Q1 — "Name"
- Q2 — "Approx. how many years of experience do you have in software engineering?" Options: "Less than
  3 years" / "3-5 years" / "5-10 years" / "10-15 years" / "15+ years"
- Q3 — "How many direct reports do you have?" — "Scale: 0 to 10 (or more) direct reports"
- Q4 — "What team are you on?"
- Q5 — "Do you have more of a research or an engineering role?" Options: "All research" / "Mostly
  research" / "50/50 split" / "Mostly engineering" / "All engineering"
- Q6 — "When did you start work at Anthropic?"

*AI Usage - 12 Months Ago (pp. 1–2), preceded by the instruction* "Please answer these questions as of
12 months ago. We are specifically interested in AI use at work."

- Q7 — "Estimate what percentage of your work involved Claude/other AI tools 12 months ago" Options:
  "0-20%" / "20-40%" / "40-60%" / "60-80%" / "80-100%"
- Q8 — "How did Claude/other AI tools affect your productivity 12 months ago?" Options: "I get less
  done than before" / "No significant change" / "I get 0-20% more done in the same time" / "I get
  20-40% more done in the same time" / "I get 40-60% more done in the same time" / "I get 60-80% more
  done in the same time" / "I get 80-100% more done in the same time" / "I get >100% more done in the
  same time"

*Current AI Usage and Impact (pp. 2–3), preceded by* "Please answer these questions as of today. These
are questions about your current habits and use-cases with Claude."

- Q9 — "What do you currently use Claude for? (select all that apply and indicate frequency)" —
  "Frequency options: Never, Monthly, Weekly, Few times a Week, Daily". The eleven task categories:
  "Implementing New Features" / "Debugging" / "Refactoring" / "Data Science (e.g. matplotlib code)" /
  "Frontend Development" / "Code understanding/exploration" / "Testing (writing tests, mocking)" /
  "Documentation (writing READMEs, comments)" / "Infrastructure/DevOps" / "Learning (new languages,
  best practices)" / "High level design/planning"
- Q10 — "Are there other tasks you currently use Claude for? How frequently?"
- Q11 — "For tasks where you currently use Claude, how does it affect your time spent on the task?" —
  "Note: Leftmost columns = less time spent, i.e. more productive." — "Options: Significant decrease,
  Slight decrease, No change, Slight increase, Significant increase, I don't use Claude for this" —
  "(Same task list as question 9)"
- Q12 — "[Optional] If Claude is increasing your time spent on any task(s), could you briefly explain
  why?"
- Q13 — "For tasks where you currently use Claude, how does it affect your output volume?" — "Some
  illustrative examples of output volume: lines of code written (although this is not always the
  perfect proxy!), number of docs written, plots made per unit of time" — "Note: Leftmost columns =
  less output volume, i.e. less productive." — "Options: Significant decrease, Slight decrease, No
  change, Slight increase, Significant increase, I don't use Claude for this" — "(Same task list as
  question 9)"
- Q14 — "If there are tasks above where Claude significantly impacts time spent or output volume
  currently: Could you elaborate and provide one (or more) detailed examples?"
- Q15 — "Estimate what percentage of your work currently involves Claude" Options: "0-20%" / "20-40%"
  / "40-60%" / "60-80%" / "80-100%"
- Q16 — "How does Claude currently affect your productivity?" Options: "I get less done than before" /
  "No significant change" / "I get 0-20% more done in the same time" / "I get 20-40% more done in the
  same time" / "I get 40-60% more done in the same time" / "I get 60-80% more done in the same time" /
  "I get 80-100% more done in the same time" / "I get >100% more done in the same time"

*Work Delegation and Preferences (pp. 3–4)*

- Q17 — "What % of the work that you currently do with Claude is work that you think wouldn't have
  happened otherwise (i.e. no one would have done it if Claude hadn't)?" Options: "0-20%" / "20-40%" /
  "40-60%" / "60-80%" / "80-100%"
- Q18 — "[Optional] Could you briefly explain your answer above?"
- Q19 — "What % of the work that you currently do with Claude is work that you would not have enjoyed
  doing yourself (vs. work you would have enjoyed doing yourself?)" Options: "0-20% work I would not
  have enjoyed doing myself" / "20-40%" / "40-60%" / "60-80%" / "80-100%"
- Q20 — "Estimate what percentage of your work you could currently fully delegate to Claude" Options:
  "0-20%" / "20-40%" / "40-60%" / "60-80%" / "80-100%"
- Q21 — "[Optional] Could you briefly explain your answer above?"

*AI Usage Patterns (p. 4)*

- Q22 — "What is the rough split between time spent using agentic (e.g. Claude Code) vs.
  conversational AI (e.g. Claude.ai, #ask-claude) for you currently?" Options: "100% agentic, 0%
  conversational" / "90% agentic, 10% conversational" / "80% agentic, 20% conversational" / "70%
  agentic, 30% conversational" / "60% agentic, 40% conversational" / "50% agentic, 50%
  conversational" / "40% agentic, 60% conversational" / "30% agentic, 70% conversational" / "20%
  agentic, 80% conversational" / "10% agentic, 90% conversational" / "0% agentic, 100% conversational"

*Future Projections (12 Months From Now) (pp. 4–5), preceded by* "Please answer these questions as of
12 months from now. We know this may be hard to answer, but please give your best estimate."

- Q23 — "Estimate what percentage of your work will involve Claude 12 months from now:" Options:
  "0-20%" / "20-40%" / "40-60%" / "60-80%" / "80-100%"
- Q24 — "Estimate what percentage of your work you could fully delegate to Claude 12 months from
  now:" Options: "0-20%" / "20-40%" / "40-60%" / "60-80%" / "80-100%"

The interview protocol is **not** released; the only published description of it is "we conducted
in-depth interviews with 53 of the Anthropic engineers and researchers who responded to the survey"
and the two topics named in the body: "We asked how people envision their future roles and whether
they have any adaptation strategies." (web, "Career uncertainty and adaptation").

## Data and methods

In my own words, with references.

**Design.** A three-instrument case study of a single employer, fielded in August 2025 and published
in December 2025. There is no control group, no randomisation, no pre-period measurement and no
external comparison sample. The year-on-year change in claim 8 is **recalled**: both the "12 months
ago" and the "today" answers were given at the same sitting (instrument questions 7–8 against 15–16).
The transcript comparison (claims 32–36) is a two-point cross-section, February 2025 and August 2025,
with no intervening months and no user-level panel.

**Survey.** n = 132 of an unknown population (Anthropic's engineering and research headcount is never
given, so no response rate for the firm as a whole can be computed). Two arms: 68 from open posting in
Slack channels (convenience) and 64 from direct messaging 5–10 people on each of 20 teams chosen from
the org chart (purposive, n = 207 contacted, 31% response). Results are never reported by arm. The
survey is **not anonymous** — question 1 asks for the respondent's name — and the Limitations section
names the consequence. Response formats are almost entirely **five-band percentage ranges** (0-20%,
20-40%, 40-60%, 60-80%, 80-100%) for usage, new work, enjoyment and delegation, and an eight-point
ordinal scale for productivity whose top category is open-ended (">100% more done in the same time").
Published point estimates — 28%, 59%, +20%, +50%, 27%, 44% — are therefore summaries of banded
categorical data; the aggregation rule (midpoints? something else?) is nowhere stated, and the value
assigned to the open-ended top band is not stated either. Per-item n is not published; Figure 2
restricts each task category to "respondents who reported using Claude for each task category".

**Interviews.** 53 semi-structured interviews with survey respondents, selected as "the first 53
people who responded". Analysis is thematic — Bryan Seethor "analyzed interview themes" — with no
codebook, no inter-coder reliability, and no theme frequencies published except "about half reported
unchanged team collaboration patterns" (claim 29). Evidence in the text is quotation, anonymised to
role level at most ("one senior engineer", "a security engineer", "a team lead").

**Claude Code transcripts.** 200,000 internal transcripts from February and August 2025, analysed
through Clio (`clio-insights-2024-12`), which is the study's only stated privacy mechanism; no
aggregation threshold, no exclusion rules and no surface definition are given (nothing says whether
CLI, IDE or SDK usage is included or excluded — contrast `claude-code-expertise-2026-06`, which
excludes IDE, SDK and headless usage by name). Sampling is "proportionate … across time periods",
which the Limitations section says permits only relative, not absolute, statements. Three classifier
or telemetry measures are used:
1. *Task complexity*, a 1–5 rating per transcript with anchors published only at 1 and 5.
2. *Maximum consecutive tool calls per transcript*, from telemetry — the count of Claude actions
   between human inputs, taken at its per-transcript maximum and then averaged.
3. *Human turns per transcript*, from telemetry.
And two task classifications, which are **not the same classification**:
4. *Multi-label coding-task categories* for the February-vs-August comparison (Figure 4), "one or
   more types of coding tasks" per transcript.
5. *Single primary coding task* per transcript, August only, for the by-team breakdown (Figure 5),
   described as a refinement of (4).
Plus a "papercut fixes" category, reported for August only (8.6%). No classifier model is named, no
prompt is published, and **no validation of any classifier is reported** — no human labels, no
agreement statistic, no reference-model check. This is the sharpest methodological difference from the
later Claude Code work.

**Estimators and uncertainty.** Everything is a mean or a share. Confidence intervals appear in
exactly two places, both figure captions: Figure 2 ("Error bars show 95% confidence intervals") and
Figure 3 ("Error bars show 95% confidence intervals"). No intervals accompany the headline survey
numbers (claims 8–10, 16, 18, 19), the transcript task shares (claims 36, 38), or any team-level
share (claim 39). No hypothesis test, no regression, no coefficient, no p-value and no minimum
detectable effect appears anywhere in the study. "Usage and productivity are also strongly correlated"
is the only relational claim and carries no statistic.

**Linkage.** The survey, the interviews and the transcripts are three separate datasets analysed in
parallel and compared narratively ("These usage data corroborate the survey data"). Nothing is linked
at the person level, although the survey collected names and the transcripts are internal — so the
linkage was, in principle, available and would have made the self-report-versus-behaviour comparison
individual rather than aggregate. The privacy constraint that would forbid it is not stated.

**External benchmarks used.** METR's July 2025 randomised study of experienced open-source developers
(<https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>), invoked twice — once as
a caution against self-reported productivity, once as convergent evidence on delegation criteria; and
the merged-pull-request figure from an external newsletter
(<https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built>). Both are third-party; neither
is reproduced here.

**Prior and adjacent Anthropic work linked from the page.** The Economic Index hub
(<https://www.anthropic.com/economic-index>) as the "previous research" this turns inward from; Clio
(<https://www.anthropic.com/research/clio>); Claude Code (<https://www.anthropic.com/claude-code>);
the policy post `economic-policy-responses-2025-10`
(<https://www.anthropic.com/research/economic-policy-responses>); the AI fluency framework
(<https://www.anthropic.com/learn/claude-for-you>). External organisation named in the follow-up
plans: CodePath.

**Released data.** None. The survey instrument is the only artefact, and is the reason this study is
replicable in other firms even though its own numbers are not reproducible.

## Limitations (verbatim)

The Appendix has exactly one sub-section, "Limitations", quoted here in full, followed by the caveats
that appear in the body.

**Appendix, "Limitations" (complete)**

- "Our survey findings are subject to several methodological limitations. We selected respondents
  through both convenience sampling and purposive sampling (to ensure broad organizational
  representation). We posted the survey across multiple internal Slack channels, yielding 68
  responses, and we also selected 20 diverse teams across research and product functions from the
  organizational chart and directly messaged 5-10 individuals per team (n=207 total outreach), getting
  a 31% response rate for the final 64 responses. We interviewed the first 53 people who responded.
  There is likely some selection bias here, as people who are particularly engaged with Claude or have
  strong opinions (positive or negative) may have been more likely to respond, while those with more
  neutral experiences may have been underrepresented."
- "Additionally, responses may be affected by social desirability bias (since responses were not
  anonymous and all participants are Anthropic employees, respondents may have inflated positive
  assessments of Claude's impact) and recency bias (asking participants to recall their productivity
  and usage patterns from 12 months ago is subject to memory distortion). Furthermore, as discussed,
  productivity is in general very difficult to estimate, so these self-reports should be taken with a
  grain of salt. These self-reported perceptions should be interpreted alongside our more objective
  Claude Code usage data, and future research would benefit from anonymous data collection and more
  robustly validated measurement instruments."
- "Our Claude Code analysis uses proportionate sampling across time periods, which means we can only
  measure relative changes in task distribution, not absolute changes in work volume. For example,
  when we report that feature implementation increased from 14% to 37% of Claude Code usage, this does
  not necessarily indicate that more total feature work is being done."
- "Finally, this research was conducted in August 2025 when Claude Sonnet 4 and Claude Opus 4 were our
  state-of-the-art models. Given the rapid pace of AI development, the patterns we observed may have
  already shifted as newer models become available."

**Caveats in the body**

- "We recognize that studying AI's impact at a company building AI means representing a privileged
  position—our engineers have early access to cutting-edge tools, work in a relatively stable field,
  and are themselves contributing to the AI transformation affecting other industries."
- "Our findings imply some challenges and considerations that may warrant early attention across
  sectors (though see the Limitations section in the Appendix for caveats)."
- "To caveat this finding (and other self-reported productivity findings below), productivity is
  difficult to precisely measure (see Appendix for more limitations). There is recent work from METR,
  an AI research nonprofit, showing that experienced developers working with AI on highly familiar
  codebases overestimated their productivity boost from AI. That being said, the factors that METR
  identified as contributing to lower productivity than expected (e.g. AI performing worse in large,
  complex environments, or where there's a lot of tacit knowledge/context necessary) closely
  correspond to the types of tasks our employees said they *don't* delegate to Claude (see AI
  delegation approaches, below). Our productivity gains, self-reported *across* tasks, might reflect
  employees developing strategic AI delegation skills—something not accounted for in the METR study."
- "It is also not clear from our data where reported time savings are being reinvested—whether into
  additional engineering tasks, non-engineering tasks, interacting with Claude or reviewing its
  output, or activities outside of work. Our task categorization framework does not capture all the
  ways engineers might allocate their time. Additionally, the time savings may reflect perception
  biases in self-reporting. Further research is needed to disentangle these effects."
- "Output volume increases are more straightforward and substantial; there is a larger net increase
  across all task categories. This pattern makes sense when we consider that people are reporting on
  task categories (like “debugging” overall) rather than individual tasks—i.e. people can spend
  slightly less time on debugging as a category while producing much more debugging output overall.
  Productivity is very hard to measure directly, but this self-reported data suggests that AI enables
  increased productivity at Anthropic primarily through greater output volume."
- "(It's worth noting that there is variation in how respondents might interpret “fully
  delegate”—from tasks needing no verification at all to those that are reliable enough to require
  only light oversight.)"
- "This shift in the relative distribution of Claude Code tasks may suggest that Claude has become
  better at these more complex tasks, though it could also reflect changes in how teams adopt Claude
  Code for different workflows rather than increases in absolute work volume (see Appendix for more
  limitations)."
- "It seems plausible that this is driving the observed productivity gains."
- "It's still early days—Anthropic has many early adopters internally, the landscape is rapidly
  changing, and our findings likely don't generalize to other organizations or contexts right now (see
  Appendix for more limitations). This research reflects that uncertainty: the findings are nuanced,
  with no single consensus or clear directives emerging."

## Open questions, conjectures and promised follow-ups (verbatim)

**The questions it opens with**

- "How is AI changing the way we work? Our previous research on AI's economic impacts looked at the
  labor market as a whole, covering a variety of different jobs. But what if we studied some of the
  earliest adopters of AI technology in more detail—namely, us?"
- "One thing we were curious about: Is Claude enabling qualitatively new kinds of work, or would
  Claude-assisted work have been done by employees eventually (albeit potentially at a slower rate)?"
- "While these survey findings reveal significant productivity gains and changing work patterns, they
  raise questions about how engineers are actually experiencing these changes day-to-day."

**Explicit calls for further research**

- "Further research is needed to disentangle these effects." (on where time savings are reinvested).
- "The convergence on these delegation criteria across our interviews suggests that appropriate task
  choice is an important factor in AI productivity gains (which should be carefully controlled for in
  future productivity studies)."
- "future research would benefit from anonymous data collection and more robustly validated
  measurement instruments."
- "Still, self-reported data only tells part of the story."

**The open question it names as the central one**

- "More capable AI brings productivity benefits, but it also raises questions about maintaining
  technical expertise, preserving meaningful collaboration, and preparing for an uncertain future that
  may require new approaches to learning, mentorship, and career development in an AI-augmented
  workplace."
- "As Claude becomes more autonomous and capable, engineers are discovering new ways to use AI
  delegation while also figuring out what skills they'll need in the future. These shifts bring clear
  productivity and learning benefits alongside genuine uncertainty about the longer-term trajectory of
  software engineering work. Will AI resemble past software engineering transitions—from lower- to
  higher-level programming languages, or from individual contributor to manager, as several engineers
  suggested? Or will it go further?"
- "But it does raise questions about how we can thoughtfully and effectively navigate these changes."

**Conjectures, flagged as such by the authors**

- "what's happening inside Anthropic for engineers may still be an instructive harbinger of broader
  societal transformation."
- "Our productivity gains, self-reported *across* tasks, might reflect employees developing strategic
  AI delegation skills—something not accounted for in the METR study."
- "It seems that generally, engineers experiencing time savings may be those who are scoping
  quickly-verifiable tasks for Claude, while those spending more time might be debugging AI-generated
  code or working in domains where Claude needs more guidance."
- "These small fixes could add up to larger productivity and efficiency gains."
- "This may contribute to engineers' reported productivity gains (addressing previously neglected
  quality-of-life improvements may lead to more efficiency over time) and potentially reducing friction
  and frustration in daily work."
- "This shift in the relative distribution of Claude Code tasks may suggest that Claude has become
  better at these more complex tasks, though it could also reflect changes in how teams adopt Claude
  Code for different workflows rather than increases in absolute work volume."
- "It seems plausible that this is driving the observed productivity gains."
- "This suggests that Claude is enabling everyone to become more full-stack in their work."
- "Perhaps software engineering is moving to higher levels of abstraction, which it has done in the
  past." … "Perhaps, in particular with the rise of “vibe coding”, we're now moving to English as a
  programming language."
- "This creates a filtering mechanism where Claude handles routine inquiries, leaving colleagues to
  address more complex, strategic, or context-heavy issues that exceed AI capabilities"
- "Claude appears to be valuable for bridging gaps in technical knowledge."

**Promised follow-ups**

- "We discuss some initial steps we're taking to explore these questions internally in the Looking
  Forward section below."
- "To follow up on this initial work, we're taking several steps. We're talking to Anthropic engineers,
  researchers, and leadership to address the opportunities and challenges raised. This includes
  examining how we bring teams together and collaborate with each other, how we support professional
  development, and/or how we establish best practices for AI-augmented work (e.g. guided by our AI
  fluency framework). We're also expanding this research beyond engineers to understand how AI
  transformation affects roles across the organization and supporting external organizations such as
  CodePath as they adapt computer science curricula for an AI-assisted future. Looking ahead, we're
  also considering structural approaches that may become increasingly relevant as AI capabilities
  advance, like new pathways for role evolution or reskilling within the organization."
- "We expect to share more concrete plans in 2026 as our thinking matures. Anthropic is a laboratory
  for responsible workplace transition; we want to not just study how AI transforms work, but also
  experiment with how to navigate that transformation thoughtfully, starting with ourselves first."
- "We also explored potential policy responses in our recent blog post on ideas for AI-related
  economic policy."

**Unresolved tensions the study itself names, in its own words**

- "This expansion in breadth also has people wondering about the trade-offs—some worry that this could
  mean losing deeper technical competence, or becoming less able to effectively supervise Claude's
  outputs, while others embrace the opportunity to think more expansively and at a higher level. Some
  found that more AI collaboration meant they collaborated less with colleagues; some wondered if they
  might eventually automate themselves out of a job."
- "But engineers are divided on whether this matters."
- "Perhaps most interestingly, one engineer challenged the premise: “The ‘getting rusty' framing relies
  on an assumption that coding will someday go back to the way it was pre-Claude 3.5. And I don't think
  it will.”"
- "Overall, many acknowledge deep uncertainty: “I have very low confidence in what specific skills I
  think will be useful in the future.”"

## What it did not test

*This section is the wiki author's inference, not the study's own text.* It lists tests the study's own
instruments and data supported but did not report, and constructs used without validation. Items are
about the published post and its released instrument as read today.

**The instrument collected six kinds of heterogeneity and the post reports none of them.** The survey
asks years of software-engineering experience (Q2, five bands), number of direct reports (Q3), team
(Q4), research-versus-engineering role (Q5), Anthropic start date (Q6), and the agentic-versus-
conversational usage split (Q22). Not one of these appears as a cut anywhere in the post. This is the
largest gap between what was collected and what was published, and it bites hardest exactly where the
study's own argument is most anxious:
- The "paradox of supervision" and the atrophy theme are explicitly about **seniority** — "One senior
  engineer said they'd be more worried about their skills if they were more junior" — yet the survey
  measured seniority twice (Q2, Q3) and never crosses it with the productivity, delegation or atrophy
  answers. Whether reported gains rise or fall with experience is the single most policy-relevant
  question the survey could have answered, and it is not asked of the data.
- Q5 separates researchers from engineers in a population described throughout as "engineers and
  researchers"; the two groups are pooled in every number.
- Q6 (start date) would identify recent hires, i.e. people whose "12 months ago" answers refer to a
  period partly or wholly before joining Anthropic. Nothing says whether such respondents were
  excluded from claim 8.
- Q22 is the only measure of *how* people use Claude (agentic vs conversational). It is used once,
  narratively and without a number, to justify studying Claude Code ("survey respondents reported
  Claude Code as the majority of their usage").

**Two questions were asked about the future and never reported.** Q23 ("percentage of your work will
involve Claude 12 months from now") and Q24 ("percentage of your work you could fully delegate to
Claude 12 months from now") were fielded in August 2025 and appear nowhere in the post. Since the post
publishes the *current* delegation ceiling (claim 19) and makes the moving-boundary argument
qualitatively ("delegation boundaries as a “moving target”"), the expected ceiling in 12 months was
available, quantified, and omitted. It is also, as of 2026, a forecast whose horizon has passed — an
external check that could be run against later data.

**The banding problem, and what it does to the headline numbers.** Q7, Q15, Q17, Q19, Q20, Q23 and
Q24 all have five 20-point bands; Q8 and Q16 have eight ordered categories topped by an open-ended
">100%". The post publishes point means (28%, 59%, 27%, 44%, +20%, +50%) without stating how bands
were converted to numbers. Three consequences are untested and unacknowledged:
1. With midpoints 10/30/50/70/90, the possible means are coarse and the reported "28%" and "59%" each
   correspond to a narrow range of band distributions; the uncertainty from banding alone is never
   quantified, and no interval is given for any of these numbers.
2. The +50% mean depends on what value is assigned to ">100% more done", the band holding 14% of
   respondents (claim 10). The choice is unstated and the mean is sensitive to it.
3. "More than half said they can “fully delegate” only between 0-20%" (claim 19) is a statement about
   the lowest band of a five-band item, so it is compatible with anything from 0% to 20% and cannot be
   compared with the 27% and 44% means, which are point estimates on the same banding.
A post building on any of these numbers must treat them as band-derived and say so.

**The construct changes between the "then" and "now" questions.** Q7 and Q8 ask about "Claude/other AI
tools" twelve months ago; Q15 and Q16 ask about "Claude" today. The headline year-on-year comparison
(claim 8) therefore compares a broader construct in the past with a narrower one in the present. If
respondents used any non-Claude AI tool in August 2024, the Claude-only past share was lower than 28%
and the true Claude growth is *larger* than the published "more than 2x"; if they read Q7 as
Claude-only anyway, the comparison is clean. Nothing in the post notices the wording change, and the
data to check it (the two items) are not reported separately. The Limitations section names recency
bias but not this.

**The productivity item measures output per unit time, and the "output volume" finding partly restates
it.** Q8/Q16 offer only "I get X% more done in the same time". The post's conclusion that "AI enables
increased productivity at Anthropic primarily through greater output volume" (claim 14) is drawn from
Figure 2's two panels, but the productivity construct respondents were given was itself defined as
more-done-per-time, so the instrument cannot distinguish "same work, faster" from "more work, same
time" at the level of the headline number. The direction of the finding is not thereby wrong; its
independence from the instrument's wording is untested.

**Self-report was never validated against the behaviour of the same person.** The survey collected
names (Q1) and the transcripts are internal. A person-level join was therefore technically available
and would have allowed the central test the post gestures at — whether the engineers who report the
largest productivity gains are the ones whose transcripts show more complex tasks, longer tool chains
or fewer human turns. Instead the two datasets are compared as aggregates ("These usage data
corroborate the survey data", claim 42), which cannot distinguish a real correlation from two
independent time trends. The post does not say whether the join was ruled out on privacy grounds.

**The 200k-transcript analysis has no validation and no classifier documentation.** No classifier
model is named, no prompt is published, no human-labelled subsample is reported, and no agreement
statistic of any kind appears — for task complexity, for the multi-label task categories, for the
single-label refinement, or for "papercut fixes". The 1–5 complexity scale publishes anchors only at
the endpoints, so "3.2 → 3.8" is a movement on an unanchored interior. Since the later Claude Code
work reports a telemetry cross-check and a reference-model check for its classifiers
(`claude-code-expertise-2026-06`), the absence here is a difference in standard, not in feasibility:
the same telemetry (lines added, commands run) existed.

**Composition is never separated from behaviour change, though both are plausible.** Between February
and August 2025, Claude Code was in rapid internal rollout. The February and August samples are two
independent proportionate draws, so every published change — complexity 3.2 → 3.8, tool calls 9.8 →
21.2, human turns 6.2 → 4.1, features 14.3% → 36.9%, design/planning 1.0% → 9.9% — can be produced by
a change in *who* is using Claude Code (new teams, new hires, non-technical employees) as well as by a
change in *how* existing users use it. The Limitations section makes the weaker point that absolute
volume is unidentified; it does not name the composition problem, and no cohort, team-fixed or
same-user analysis is reported even though team labels demonstrably exist (Figure 5). The "Non-
technical" team in Figure 5 is direct evidence that the user base broadened.

**Model capability and user behaviour are not separated.** Between February and August 2025 the
available models changed (the study names Sonnet 4 and Opus 4 as current at collection). Longer tool
chains and fewer human turns are equally consistent with better models and with bolder users; the post
offers both readings for the task mix (claim 37) but not for the autonomy measures, which are
presented as "people are increasingly delegating more autonomy to Claude" (Figure 3 caption) — a
statement about people, from data that cannot separate the two. Model version per transcript was
presumably recorded and is not used.

**The maximum is reported and the distribution is not.** Claim 33 averages a per-transcript *maximum*.
Nothing is published about the distribution of chain lengths — median, typical, tail — so the
key-findings gloss "it generally handles around 20" (claim 35) is unsupported by any published
statistic, and a heavy right tail in a minority of transcripts would produce the same headline. The
untested alternative reading: the maximum rose because sessions got longer, not because human
oversight per action fell. Session length and duration are never reported.

**No outcome measure anywhere.** Nothing in the study measures whether delegated work succeeded:
no success or failure classification, no review outcome, no revert rate, no defect rate, no
time-to-merge, no code-survival measure. The one outcome-like number in the post (+67% merged pull
requests) is imported from a newsletter. So "engineers are getting a lot more done" rests on
self-report plus volume proxies, and the study's own concern — "a potential risk of inexperienced
engineers shipping problematic code" — is raised in a quotation and never measured, although merged
PRs, reviews and reverts are exactly the internal data a firm has.

**The social and mentorship findings are the strongest qualitative claims and have no quantitative
counterpart.** "Claude has become the first stop for questions that once went to colleagues" (claim
28) is a claim about substitution between colleagues and Claude. An employer has the data to test it —
internal question channels, code-review assignments, mentorship pairings, meeting load — and none is
used. "About half reported unchanged team collaboration patterns" (claim 29) is the only number, and
it is an interviewer's coding of 53 interviews with no reliability check. The mentorship claim is made
about juniors by seniors, and no junior-versus-senior breakdown exists (see the heterogeneity gap
above).

**Skill atrophy is a conjecture with no measurement.** The study's most consequential idea — the
paradox of supervision — is supported entirely by quotation. Nothing measures skill, nothing measures
supervision quality, and no test of whether supervision quality declines with delegation intensity is
attempted. (Whether the later randomised work answers this is a question for `programme/LEDGER.md`;
the candidate is `skill-formation-rct-2026-01`.)

**The 27% counterfactual is an unvalidated self-assessment.** "Work that wouldn't have happened
otherwise" (Q17) asks respondents to price a counterfactual they cannot observe. The post offers the
8.6% papercut share as corroboration (claim 17), but the two numbers share neither denominator nor
definition, and no attempt is made to bound the 27% — for instance by asking about specific completed
projects, or by comparing project inventories before and after. Read strictly, 27% is a belief about
alternative histories, and it is the number most likely to be quoted as a fact.

**Interview selection and saturation are untested.** Interviewees were "the first 53 people who
responded" — the fastest responders to a survey about Claude, a selection the Limitations section
acknowledges in general terms for the survey but not specifically for the interview sample. No
saturation analysis, no report of themes that appeared in only one or two interviews, and no count of
how many interviewees expressed each theme — so "some", "many", "several" and "most" carry the
argument with no way to distinguish a majority view from a memorable quotation.

**The two sampling arms are never compared.** Slack self-selection (68) versus purposive outreach with
a 31% response rate (64) are the two arms most likely to differ in enthusiasm for Claude. Comparing
their answers is a free, internal test of the selection bias the study names, and it is not reported.

**Generalisation is asserted and bounded but never probed with data that exist.** The post says its
findings "likely don't generalize" while also calling them "an instructive harbinger". Anthropic had,
at publication, a public Claude Code measurement of external users
(`economic-index-2025-04-software-development`), so at least one comparison — is the internal task mix
unusual against the external one? — was available and is not made. Nothing in the study quantifies how
unrepresentative Anthropic's engineers are on any observable (tenure, seniority, tooling, codebase).

**Statistical reporting.** No hypothesis test, no regression, no effect size with an interval, no
correction for the many task-category comparisons in Figure 2, no minimum detectable effect anywhere,
and no n reported per survey item or per figure panel. With n = 132, and per-category subsets smaller
still, a claim like "net decrease in time spent" across eleven categories is a multiple-comparison
problem the post does not treat as one. Figure 2's and Figure 3's 95% intervals are the study's only
uncertainty statements.

**Internal inconsistencies left unreconciled** (recorded in Claims): 59% vs 60% and "more than 2x" vs
"2-3x" (claims 8, 9); the per-transcript maximum reported as the typical chain length (claims 33, 35);
Figure 4's multi-label classification against Figure 5's single-label refinement, with no statement of
how they relate (claim 39); the February-to-August comparison described in a caption as "between
August 2025 and February 2025"; and two BibTeX authors with no described contribution (Source).

## Verification

- **URLs fetched on 2026-09-16 and read in full:**
  1. <https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic> — the complete web
     page: framing section, all three key-findings blocks, all four body sections and their
     sub-sections, all five figure captions and their alt text, the delegation-criteria table, every
     block quotation, "Looking forward", the BibTeX block, the Acknowledgments, and the Appendix
     ("Limitations"). Fetched with the web fetch tool; HTTP 200, no truncation (the footer nav and
     "Related content" block were returned as well and are not sources).
  2. <https://assets.anthropic.com/m/6cd21f7d4f82afcb/original/Claude-at-Work-Survey.pdf> — all 5
     pages, all 24 questions and every response option, plus the six section headings and the three
     instruction paragraphs.
- **Fetch method and failures.** No fetch failed. The `anthropic.com` page returned cleanly through
  the fetch tool. The instrument PDF was downloaded with `curl` to `/tmp/survey.pdf` (HTTP 200, 73,816
  bytes) and read page by page; the fetch tool was not attempted on it, since a prior lead thread
  recorded that the Anthropic CDN PDF hosts must be fetched with `curl`
  (`wiki/reports/claude-code-expertise-2026-06.md`, Verification). The `assets.anthropic.com` host
  therefore has no confirmed fetch-tool status either way.
- **No other document exists to fetch.** There is no PDF of the post, no arXiv version, no appendix
  document beyond the on-page Appendix, and no dataset. The interview protocol and the classifier
  prompts are not published.
- **Alt text.** Each of the five figure images carries alt text identical to its bold caption, so
  nothing in this file is marked `(alt text)` and no number required that treatment. Confirmed by
  comparing each `![...]` alt string with the bold sentence beneath it in the fetched page.
- **Not read off any chart.** Per `room/director-2026-09-16-alt-text-ruling.md`, no value was taken
  from a figure image. The consequence is that this file does **not** record: the eight
  non-highlighted daily-use shares in Figure 1; any per-category mean in Figure 2 (only the
  qualitative pattern and its caption); the February and August levels for any task category in
  Figure 4 other than the two named in prose; and every team-by-task share in Figure 5 other than the
  five named in prose. Anything load-bearing from those figures would need the underlying values,
  which are not published.
- **Could not be determined from the sources:** the aggregation rule converting banded survey
  responses into the published means; the value assigned to the ">100%" productivity band; the per-item
  and per-figure sample sizes; Anthropic's engineering headcount, hence any firm-level response rate;
  the classifier model, prompts and any validation for the transcript analysis; the Clio aggregation
  threshold used; which Claude Code surfaces the 200k transcripts cover; the interview protocol and
  any theme counts; and the breakdown of any result by the demographics the instrument collected
  (Q2–Q6, Q22) or by the projections it collected (Q23–Q24).
- **Arithmetic checked against the published figures** (no data file opened; the programme lead does
  not open data files): 68 + 64 = 132 ✓ against "132"; 31% × 207 = 64.2 ✓ against "64 responses";
  21.2 / 9.8 = 2.16 ✓ against "increased by 116%"; 4.1 / 6.2 = 0.661 ✓ against "decreased by 33%";
  59 / 28 = 2.11 and 50 / 20 = 2.5, both consistent with "more than 2x" and spanned by the key
  findings' "2-3x".
- **Cross-corpus statements in this file and their basis.** That `claude-code-expertise-2026-06` cites
  this study as prior work is taken from `wiki/reports/claude-code-expertise-2026-06.md` (Data and
  methods), written from that paper. That this study's transcripts are not in the public Index
  releases is an inference from the study itself (internal employee data, nothing released) and from
  the steward's enumeration in `data/releases/INDEX.md` recording no Claude Code folder; I did not
  open any data file. All other slugs named here (`skill-formation-rct-2026-01`,
  `anthropic-interviewer-2025-12`, `economic-index-2025-04-software-development`,
  `economic-policy-responses-2025-10`, `clio-insights-2024-12`) are named as pointers for
  `programme/LEDGER.md` to check; **no claim is made here about their contents.**
- **Quotation check.** Every quotation in "Definitions (verbatim)", "Limitations (verbatim)" and "Open
  questions, conjectures and promised follow-ups (verbatim)", and every quoted fragment in Claims and
  Source, was checked character by character against the fetched text of the stated source — the named
  web section, figure caption, or instrument page — including curly quotation marks, em dashes, the
  page's own "everyday" for "every day", its doubled spaces (e.g. after "3.2 to 3.8 on average.") and
  the stray leading characters before "Engineers diverge sharply", which are reproduced rather than
  corrected. Inline markdown links inside quotations are reproduced where the link text is part of the
  sentence. The verbatim sections contain no interpretation; all inference is confined to "What it did
  not test" and to the passages in Claims and Source explicitly marked as the wiki author's note.
