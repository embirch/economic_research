# Appendix to "Anthropic Economic Index report: Learning curves"

## Source

| Field | Value |
|---|---|
| Slug | `economic-index-2026-03-appendix` |
| Title (from page 1) | Appendix to "Anthropic Economic Index report: Learning curves" |
| Date (from page 1) | March 2026 |
| Type | Appendix (standalone 6-page PDF; not bound into the report) |
| Publisher | Anthropic |
| Primary URL (copy A, the URL in `wiki/INDEX.md`) | https://cdn.sanity.io/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf |
| Second copy (copy B) | https://cdn.sanity.io/files/4zrzovbb/website/a3cdcd9e67c3c4c51440429dd016cacba514b35b.pdf |
| Parent report | The Anthropic Economic Index report: Learning curves, 2026-03-24, https://www.anthropic.com/research/economic-index-march-2026-report (separate wiki entry `economic-index-2026-03-report`) |
| Length | 6 pages in both copies |
| Contents | p.1 title; p.2 "Methodology"; p.3 "Key terms"; p.4 Table A.1 "Economic primitives overview"; p.5 "Additional figures and results" (Figures A.1, A.2); p.6 Figure A.3 and footnote 1 |

Both copies are linked from the parent report page. Copy A is linked from in-text anchors in Chapter 1 ("than in previous reports", the privacy-system footnote); copy B is linked from the "Appendix — Available here" line under Data availability and from the in-text anchors that name Figures A.2 and A.3. Copy B is the later build (see `## Verification`). Where the two differ, the wording of both is given below.

## Claims

The appendix is predominantly definitional and illustrative. Its substantive assertions are the sample description on p.2, three figures, and one footnote. Numbers are given as published; where a figure carries no printed data label, that is stated.

1. **Both samples are 1 million records each and cover one week.** "a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations" and "1M transcripts from our first-party (1P) API traffic"; "Both samples come from February 5, 2026, to February 12, 2026." (p.2, "Methodology", paragraphs 1–2). The comparison this rests on: none — it is the sample frame for the whole report. Note that the same 1M/1M figures are stated for both surfaces, so the two samples are equal in record count and not in proportion to the traffic behind them.

2. **A 1P API record is a prompt-response pair, not a session.** "For 1P API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions." (p.2, "Methodology", paragraph 2). Rests on no comparison; it is the unit-of-observation statement, and it makes the Claude.ai unit (a conversation) and the 1P API unit (a prompt-response pair) non-equivalent.

3. **Privacy thresholds are applied before estimation, and cells below them are dropped.** "we rely on statistical models in which minimum aggregate thresholds for both unique accounts and conversations are satisfied for any reported statistics. For example, in our regression analysis we only estimate fixed effects for groupings that satisfy our privacy requirements—otherwise such cells are dropped prior to estimation." (p.2, "Methodology", paragraph 3). No threshold value is published. The scope of the sentence differs between the two copies: copy A scopes it to "the analysis described in Chapter 2", copy B scopes it to "When we analyze log-level data".

4. **Usage shares across the eight largest occupational groups moved in opposite directions on the two surfaces for Computer and Mathematical work, and the API series begins only in August 2025.** Figure A.1, p.5, titled on the plot "Task usage share trends by occupation group (V1-V5, 2019 O*NET-SOC)"; caption "Shifts in the usage across occupational categories" (copy A) / "Shifts in usage across occupational categories" (copy B), "This plot shows changes in usage shares across the largest occupational categories in our data, splitting by Claude.ai and 1P API." Eight panels: Computer and Mathematical; Arts, Design, Entertainment, Sports, and Media; Educational Instruction and Library; Office and Administrative Support; Life, Physical, and Social Science; Business and Financial Operations; Architecture and Engineering; Management. Five x-axis points: Jan 2025, Mar 2025, Aug 2025, Nov 2025, Feb 2026 (V1–V5). The Claude.ai series is plotted at all five points; the 1P API series only from Aug 2025 (V3) onward, in every panel.
   **No data labels are printed on Figure A.1.** The values below are the wiki author's reading off the panel axes at 400 dpi, in usage-share percentage points, accurate to roughly ±0.2 pp; they are *not* published numbers and must not be quoted as such.

   | Panel (y-axis max) | Series | Jan 2025 | Mar 2025 | Aug 2025 | Nov 2025 | Feb 2026 |
   |---|---|---|---|---|---|---|
   | Computer and Mathematical (60) | Claude.ai | 40.2 | 42.2 | 42.3 | 38.8 | 34.5 |
   | | 1P API | — | — | 53.7 | 59.6 | 61.6 |
   | Arts, Design, Entertainment, Sports, and Media (10) | Claude.ai | 10.4 | 9.6 | 9.0 | 10.6 | 10.4 |
   | | 1P API | — | — | 6.0 | 6.3 | 5.3 |
   | Educational Instruction and Library (16) | Claude.ai | 9.4 | 11.2 | 13.4 | 16.2 | 13.5 |
   | | 1P API | — | — | 4.1 | 4.1 | 3.1 |
   | Office and Administrative Support (7) | Claude.ai | 4.4 | 5.0 | 5.4 | 5.3 | 6.5 |
   | | 1P API | — | — | 6.7 | 7.2 | 7.2 |
   | Life, Physical, and Social Science (8) | Claude.ai | 6.4 | 6.9 | 7.8 | 5.8 | 6.3 |
   | | 1P API | — | — | 8.1 | 4.6 | 4.4 |
   | Business and Financial Operations (6) | Claude.ai | 6.25 | 4.8 | 3.8 | 3.9 | 5.25 |
   | | 1P API | — | — | 4.3 | 4.0 | 3.9 |
   | Architecture and Engineering (4) | Claude.ai | 4.4 | 3.75 | 2.45 | 1.95 | 1.95 |
   | | 1P API | — | — | 1.9 | 1.2 | 1.55 |
   | Management (4) | Claude.ai | 4.6 | 3.3 | 3.0 | 3.6 | 4.65 |
   | | 1P API | — | — | 3.6 | 3.6 | 3.6 |

   Each panel has its own y-axis scale; the panels are not on a common axis. The parent report page (fetched 2026-09-16) attaches published numbers to this figure that the appendix itself does not print: "tasks associated with Computer and Mathematical occupations accounting for 35% of conversations on Claude.ai (see Appendix)" and "Since August 2025, the share of tasks in this category has increased by 14% in the API and decreased by 18% in Claude.ai." Those are report claims, not appendix claims; the readings above are consistent with them (42.3 → 34.5 is −18.4% relative; 53.7 → 61.6 is +14.7% relative).

5. **Cumulative occupational coverage was 49% at the ≥25% threshold, 24% at ≥50% and 7% at ≥75% as of February 2026, and all three curves have flattened.** Figure A.2, p.5, plot title "Occupation coverage thresholds (claude.ai + API, cumulative)"; caption "Cumulative job coverage", "This plot shows changes in the cumulative share of occupations with task coverage at or exceeding 25%, 50%, or 75%." The three February 2026 endpoints carry printed data labels: **49%**, **24%**, **7%**. Earlier points carry no labels; the wiki author reads the Jan 2025 starts as roughly 36%, 11.5% and 4%, and the Nov 2025 points as roughly 49%, 22.7% and 6.4% (axis reading, not published). The comparison the claim rests on: the same three thresholds at the four earlier data pulls, pooled across Claude.ai and the 1P API — the series is a single pooled line per threshold, not split by surface. The parent report page states the comparison the figure is used for: "In our previous report, we noted that 49% of jobs had seen at least a quarter of their tasks performed using Claude. In this data pull, that cumulative estimate barely changed (Appendix Figure A.2)."

6. **Automation fell and augmentation rose in 1P API traffic across the last three data pulls.** Figure A.3, p.6, plot title "Automation vs augmentation over time (1P API)"; caption "Collaboration mode share, 1P API", "This plot shows changes in the share of automation vs. augmentation in 1P API traffic." Every point carries a printed data label:

   | Series | Jan 2025 | Mar 2025 | Aug 2025 | Nov 2025 | Feb 2026 |
   |---|---|---|---|---|---|
   | Automation | no data point | no data point | **77%** | **75%** | **68%** |
   | Augmentation | no data point | no data point | **12%** | **14%** | **17%** |

   The x-axis is drawn with Jan 2025 and Mar 2025 tick labels and an axis break, but no 1P API points are plotted before Aug 2025. The comparison the claim rests on: Aug 2025 against Feb 2026 within the 1P API only — 9 percentage points off automation, 5 percentage points onto augmentation. The two published shares do not sum to 100% at any point (89%, 89%, 85%); the appendix does not name what the residual 11, 11 and 15 percentage points are. A note under the plot gives the composition: "Automation = Directive + Feedback loop. Augmentation = Validation + Task iteration + Learning."

7. **Figure A.1 uses a different O\*NET vintage from earlier reports.** Footnote 1, p.6: "This figure uses 2019 O\*NET-SOC codes, while previous reports use the 2010 vintage." This is the only statement in the appendix about comparability with the earlier Index releases, and it is scoped to Figure A.1 alone ("This figure").

8. **The Economic Primitives are nine classifier questions grouped into five dimensions.** Table A.1, p.4, "Economic Primitives Overview", "This table provides definitions for the Economic Primitives we study in this report." Groups, in the order printed: Task complexity (Human time estimate; Human with AI time estimate; Multitasking), Human and AI skills (Human ability to complete task alone; Human education years; AI education years), Use case (Work vs. coursework vs. personal), AI autonomy (no sub-row label), Task success (no sub-row label). The p.3 text states the dimension count: "Our Economic Primitives cover five dimensions relevant to AI's economic impact: user and AI skills, how complex tasks are, the degree of autonomy afforded to Claude, how successful Claude is, and whether Claude is used for personal, educational, or work purposes."

## Definitions (verbatim)

All quotations below are from copy A unless a copy-B variant is given. Quotation marks are the wiki file's; the "smart" quotation marks inside the quoted text are Anthropic's.

### Sample and surface definitions (p.2, "Methodology")

> "Our analysis is based on privacy-preserving analysis. Throughout the report we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations (we also refer to this as "consumer data" since it mostly represents consumer use) and 1M transcripts from our first-party (1P) API traffic (we also refer to this as "enterprise data" since it mostly represents enterprise use)." (p.2)

Copy B, same position, first sentence only: > "Our results are based on privacy-preserving analysis." (p.2)

> "Both samples come from February 5, 2026, to February 12, 2026. We continue to manage data according to our privacy and retention policies, and our analysis is consistent with our terms, policies, and contractual agreements. For 1P API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions." (p.2)

> "In the analysis described in Chapter 2, we rely on statistical models in which minimum aggregate thresholds for both unique accounts and conversations are satisfied for any reported statistics. For example, in our regression analysis we only estimate fixed effects for groupings that satisfy our privacy requirements—otherwise such cells are dropped prior to estimation." (p.2, copy A)

Copy B, same position: > "When we analyze log-level data, we rely on statistical models in which minimum aggregate thresholds for both unique accounts and conversations are satisfied for any reported statistics. For example, in our regression analysis we only estimate fixed effects for groupings that satisfy our privacy requirements—otherwise such cells are dropped prior to estimation." (p.2, copy B)

### Key terms (p.3)

> "1P API: First-party API. This traffic represents users accessing Claude programmatically, rather than through a web user interface (as with Claude.ai)." (p.3)

> "Log-level data: This refers to analysis performed at the log level, as opposed to aggregated task groupings. This is necessary for estimating the correlation between two primitives, for example." (p.3)

> "Request clusters: A bottom-up taxonomy of what people ask Claude to do, generated using a privacy-preserving method that groups semantically similar conversations." (p.3)

> "Automation and augmentation:
> - Automation encompasses interaction patterns focused on task completion:
>   - Directive: Users give Claude a task and it completes it with minimal back-and-forth
>   - Feedback Loops: Users automate tasks and provide feedback to Claude as needed
> - Augmentation focuses on collaborative interaction patterns:
>   - Learning: Users ask Claude for information or explanations about various topics
>   - Task Iteration: Users iterate on tasks collaboratively with Claude
>   - Validation: Users ask Claude for feedback on their work" (p.3)

> "Economic Primitives: Simple measures of how Claude is used generated by asking Claude specific questions about anonymized conversations and transcripts. Our Economic Primitives cover five dimensions relevant to AI's economic impact: user and AI skills, how complex tasks are, the degree of autonomy afforded to Claude, how successful Claude is, and whether Claude is used for personal, educational, or work purposes." (p.3)

> "See Table A.1 for additional details for each Economic Primitive." (p.3)

### Table A.1, "Economic primitives overview" (p.4) — the classifier prompts in full

The table is printed as a three-column grid: dimension, primitive name, prompt. The prompt cell for the two time estimates is laid out as a two-column bullet list; the bullets are transcribed here in reading order (left column first, then right column), which is the order the PDF's own text layer uses for "Human with AI time estimate" and the reverse of it for "Human time estimate". The bullet text itself is verbatim.

**Dimension: Task complexity**

Primitive "Human time estimate":

> "Estimate how many hours a competent professional would need to complete the tasks done by the Assistant. Assume they have:
> - The necessary domain knowledge and skills
> - All relevant context and background information
> - Access to required tools and resources
> - No access to AI tools to assist with the work" (p.4, Table A.1)

Primitive "Human with AI time estimate":

> "Estimate how many minutes the User spent completing the tasks in the prompt with the Assistant. Consider:
> - Number and complexity of User messages
> - Time reading Assistant's responses
> - Time thinking and formulating questions
> - Time reviewing outputs and iterating
> - Realistic typing/reading speeds
> - Time implementing suggestions or running code outside of the conversation (only if directly relevant to the tasks)" (p.4, Table A.1)

Primitive "Multitasking":

> "Did the User multitask in this conversation? Choose from these options:
> - Yes: the User was working on multiple tasks over the course of the conversation
> - No: the User was working on a single task over the course of the conversation" (p.4, Table A.1)

**Dimension: Human and AI skills**

Primitive "Human ability to complete task alone":

> "Could the User have completed this task by themselves? Choose from these options:
> - Yes: the User would have been able to complete the task without the Assistant, even if it would have taken more time
> - No: the User would not have been able to complete the task without the Assistant, even with more time" (p.4, Table A.1)

Primitive "Human education years":

> "Estimate how many years of formal education someone would need to understand the User prompts in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20." (p.4, Table A.1)

Primitive "AI education years":

> "Estimate how many years of formal education someone would need to understand the Assistant responses in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20." (p.4, Table A.1)

**Dimension: Use case**

Primitive "Work vs. coursework vs. personal":

> "Analyze whether the conversation between the User and the Assistant primarily focuses on work, coursework, or personal use. Analyze the use case according to these categories:
> - Work: professional use to accomplish tasks that are part of the User's job
> - Coursework: use to help the User complete coursework in educational contexts
> - Personal: use for any domain that is not work or coursework" (p.4, Table A.1)

**Dimension: AI autonomy** (no separate primitive-name cell)

> "Estimate how much autonomy the Assistant had to make decisions in this conversation (a discrete number ranging from 1 - 5, where 1 is none and 5 is extreme)." (p.4, Table A.1)

**Dimension: Task success** (no separate primitive-name cell)

> "Did the Assistant complete the task provided by the User successfully? Choose from these options:
> - Yes: the Assistant completed the task provided by the User successfully
> - No: the Assistant did not complete the task provided by the User successfully" (p.4, Table A.1)

Table caption:

> "Table A.1: Economic Primitives Overview
> This table provides definitions for the Economic Primitives we study in this report." (p.4)

### Figure captions and in-plot notes (pp.5–6)

> "Figure A.1: Shifts in the usage across occupational categories
> This plot shows changes in usage shares across the largest occupational categories in our data, splitting by Claude.ai and 1P API.¹" (p.5, copy A)

Copy B, same caption: > "Figure A.1: Shifts in usage across occupational categories
> This plot shows changes in usage shares across the largest occupational categories in our data, splitting by Claude.ai and 1P API.¹" (p.5, copy B)

> "Task usage share trends by occupation group (V1-V5, 2019 O*NET-SOC)" (p.5, plot title of Figure A.1, both copies)

> "Figure A.2: Cumulative job coverage
> This plot shows changes in the cumulative share of occupations with task coverage at or exceeding 25%, 50%, or 75%." (p.5, both copies)

> "Occupation coverage thresholds (claude.ai + API, cumulative)" (p.5, plot title of Figure A.2, both copies)

> ">=25% tasks covered" / ">=50% tasks covered" / ">=75% tasks covered" (p.5, Figure A.2 legend entries, both copies)

> "Figure A.3: Collaboration mode share, 1P API
> This plot shows changes in the share of automation vs. augmentation in 1P API traffic." (p.6, both copies)

> "Automation vs augmentation over time (1P API)" (p.6, plot title of Figure A.3, both copies)

> "Automation = Directive + Feedback loop. Augmentation = Validation + Task iteration + Learning." (p.6, note printed under the Figure A.3 axes, both copies)

> "Additional figures and results" (p.5, section heading, both copies)

### Footnote (p.6)

> "¹ This figure uses 2019 O*NET-SOC codes, while previous reports use the 2010 vintage." (p.6, footnote 1, both copies)

## Data and methods

In the wiki author's words, with page references.

**Sample.** Two samples of one million records each, both drawn from the week 5–12 February 2026 (p.2). The Claude.ai sample is drawn at random from Free, Pro and Max conversations and is called "consumer data"; the first-party API sample is drawn from 1P API traffic and is called "enterprise data" (p.2). The unit of observation differs between them: a Claude.ai record is a conversation, a 1P API record is a prompt-response pair, and that pair may be taken from the middle of a longer multi-turn session (p.2). No sampling weights, no per-surface record counts by month, and no account counts are reported.

**Privacy machinery.** Minimum aggregate thresholds on both unique accounts and conversations must be met before any statistic is reported; in the regression work, fixed effects are estimated only for groupings that clear the thresholds, and non-clearing cells are dropped before estimation rather than pooled into a residual category (p.2). The threshold values are not published. The scope of this rule is stated differently in the two copies: copy A applies it to "the analysis described in Chapter 2", copy B to log-level analysis generally.

**Measurement.** Everything measured in the report comes from Claude classifying anonymised conversations and transcripts against a fixed set of questions — nine prompts grouped into five dimensions, printed in full in Table A.1 (p.4). Three of the nine primitives are free numeric estimates (hours, minutes, years of education 0–20), one is a 1–5 discrete scale (AI autonomy), three are binary Yes/No (multitasking, human ability to complete the task alone, task success), and one is a three-way categorical (work / coursework / personal). Request clusters are a separate, bottom-up taxonomy built by grouping semantically similar conversations, as distinct from the top-down O\*NET task mapping (p.3). Collaboration modes are the five patterns of the earlier releases, grouped two-and-three into automation and augmentation (p.3, and the note under Figure A.3 on p.6).

**Time series construction.** The three figures are all comparisons across the five Economic Index data pulls, labelled V1–V5 on the Figure A.1 plot title and dated Jan 2025, Mar 2025, Aug 2025, Nov 2025, Feb 2026 on the axes (pp.5–6). The 1P API only enters from Aug 2025 (V3) in Figures A.1 and A.3; the x-axes still carry the two earlier tick labels, with an axis break drawn between Mar 2025 and Aug 2025 in Figures A.2 and A.3. Figure A.1 is split by surface; Figure A.2 pools the two surfaces ("claude.ai + API"); Figure A.3 is the 1P API alone.

**Occupational classification.** Figure A.1 is built on 2019 O\*NET-SOC codes, and the footnote states that previous reports used the 2010 vintage (p.6). The eight panels are described as "the largest occupational categories in our data" (p.5); no size rule for "largest" is given and the remaining major groups are not shown.

**Coverage measure.** Figure A.2 counts occupations whose O\*NET task list has been covered at or exceeding 25%, 50% or 75% by tasks Claude has been observed performing, and the count is cumulative — it accumulates across data pulls rather than being recomputed within each pull (p.5, plot title and caption). The denominator (how many occupations) is not printed on the figure or stated in the text.

**No statistics of inference.** The appendix reports no standard errors, no confidence intervals, no sample sizes per cell, and no test statistics for any of the three figures.

## Limitations (verbatim)

The appendix carries no section, heading or paragraph headed "Limitations", and no sentence in it is framed as a limitation of the analysis. The three passages below are the whole of what the appendix says that bears on the scope or comparability of its own numbers. They are quoted here in full because they are the only candidates; nothing has been added or paraphrased.

> "For 1P API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions." (p.2)

> "In the analysis described in Chapter 2, we rely on statistical models in which minimum aggregate thresholds for both unique accounts and conversations are satisfied for any reported statistics. For example, in our regression analysis we only estimate fixed effects for groupings that satisfy our privacy requirements—otherwise such cells are dropped prior to estimation." (p.2, copy A; copy B opens "When we analyze log-level data, we rely on statistical models in which")

> "¹ This figure uses 2019 O*NET-SOC codes, while previous reports use the 2010 vintage." (p.6)

## Open questions, conjectures and promised follow-ups (verbatim)

The appendix contains none. There is no sentence in the fetched text of either copy containing "future work", "further research", "more research", "we plan", "we hope", "remains an open question", "we cannot", "we do not know", "leave for", or any equivalent. The only forward- or outward-pointing sentence in the document is a cross-reference within the document itself:

> "See Table A.1 for additional details for each Economic Primitive." (p.3)

Nothing else in this section: the appendix names no conjecture and promises no follow-up. Ledger entries for the March 2026 release therefore have to be taken from the parent report (`wiki/reports/economic-index-2026-03-report.md`), not from here.

## What it did not test

The wiki author's inference, not the appendix's own words. Each item is something the appendix's own material makes checkable, and did not check.

**Robustness checks the appendix could have run and did not**

1. **The O\*NET vintage change is asserted, not bounded.** Footnote 1 says Figure A.1 uses 2019 O\*NET-SOC while previous reports used 2010. The appendix does not show the same figure on the 2010 vintage, does not report a crosswalk, and does not quantify how much of any level shift or any change between Aug 2025 and Feb 2026 is attributable to the recode rather than to behaviour. Because the earlier pulls (Jan 2025, Mar 2025, Aug 2025) were published on 2010 codes and are re-plotted here on 2019 codes, the whole of Figure A.1 is a re-coded series whose re-coding is unquantified.
2. **The vintage footnote is scoped to Figure A.1 only.** It says "This figure". Whether Figure A.2's occupation denominator and coverage counts were also moved to the 2019 vintage is not stated. If they were, the "barely changed" comparison the report draws from Figure A.2 spans a recode; if they were not, Figures A.1 and A.2 use different occupation universes. Neither possibility is addressed.
3. **Figure A.2's cumulative construction is never separated from its substantive claim.** A cumulative, ever-observed coverage count cannot fall. Its flattening is therefore consistent with two very different worlds — saturation of the reachable task space, or a smaller/less diverse February pull adding few new tasks — and the appendix runs no within-pull (non-cumulative) version that would distinguish them.
4. **Figure A.2 pools Claude.ai and the 1P API and is never split.** The plot title says "claude.ai + API". Given Figure A.1 shows the two surfaces moving in opposite directions across several occupational groups, the pooled coverage curve could be flat because both surfaces are flat or because one is still expanding while the other contracts. No split version is shown.
5. **The residual in Figure A.3 is left unexplained.** Automation and augmentation sum to 89%, 89% and 85% at the three plotted points. Whether the remaining 11, 11 and 15 percentage points are an unclassified/none category, a directive-vs-feedback-loop coding gap, or records dropped by the privacy thresholds is not stated, and the appendix does not test whether the apparent 9-point fall in automation is instead a rise in the residual.
6. **Figure A.3 has no Claude.ai counterpart in the appendix.** The figure is 1P API only, and the appendix does not put the two surfaces on one axis, so the reader cannot see whether the automation fall is an API-specific phenomenon or a platform-wide one.
7. **No uncertainty is attached to any figure.** With 1M records per surface per pull, standard errors on the aggregate shares would be small, but the per-panel per-pull cells in Figure A.1 — eight occupational groups by two surfaces by five pulls — are not sized, and the appendix reports no cell counts, no intervals and no minimum-detectable-difference. The 3.1% vs 4.1% movement in the Educational Instruction and Library API panel cannot be assessed.
8. **The privacy threshold is never stated numerically, and its selection effect is never bounded.** Cells are "dropped prior to estimation"; the appendix does not report how many cells were dropped, on which dimensions, or how the reported aggregates shift when the drop rule binds.
9. **"The largest occupational categories" is not defined.** Eight of O\*NET's major groups are shown; the appendix gives no size rule, does not name the excluded groups, and does not report what share of usage the eight shown account for. Whether the eight are the largest on Claude.ai, on the 1P API, or on the pool is not said.
10. **Per-panel y-axis scaling is not flagged.** Each Figure A.1 panel has its own maximum (4 to 60), so slopes are not visually comparable across panels, and the appendix adds no caption note to that effect.
11. **No cross-surface reconciliation of the unit of observation.** The appendix states the Claude.ai unit is a conversation and the 1P API unit is a prompt-response pair, sometimes mid-session, and then plots "usage share" for both on the same panel without testing whether the differing unit biases the shares — for example whether long API sessions are over-represented relative to long Claude.ai conversations.
12. **The equal 1M/1M sample sizes are not reweighted to traffic.** Figure A.2 pools the two surfaces. If one surface carries far more real traffic than the other, the pooled coverage curve implicitly weights them equally. No weighting or sensitivity is shown.

**Measurement questions the appendix's own definitions raise and leave open**

13. **No classifier validation.** Table A.1 prints nine prompts in full but reports no human agreement rate, no inter-rater or inter-model reliability, no test-retest stability across model versions, and no calibration for the two time estimates (hours for the human-alone counterfactual, minutes for the human-with-AI actual) or for the 0–20 education-years scales. The prompts are asked of Claude about Claude's own transcripts, and no self-assessment bias check is offered — most pointedly for "Task success", where Claude judges whether Claude succeeded.
14. **Prompt-version drift is not addressed.** The prompts are given as a single fixed set "we study in this report", with no statement of whether they are word-for-word the prompts used in the January 2026 release that introduced the primitives. Any wording change would break the V4–V5 comparison, and the appendix neither asserts nor tests identity.
15. **The two time-estimate prompts are on different units and are not reconciled.** "Human time estimate" asks for hours; "Human with AI time estimate" asks for minutes. The appendix does not say how the pair is combined into a time-saving measure, nor whether the hours estimate is truncated, capped or winsorised.
16. **AI autonomy's 1–5 scale is unanchored past its endpoints.** Only 1 ("none") and 5 ("extreme") are labelled; 2, 3 and 4 are not, and no anchoring examples are given.
17. **"Multitasking" and the collaboration modes are both conversation-level, and their interaction is untested.** If a conversation spans multiple tasks, which task the single collaboration-mode label and the single O\*NET task mapping refer to is not specified.
18. **Request clusters appear in Key terms but nowhere in the appendix's own results.** The term is defined and then not used in any of the three figures, so the appendix gives no mapping between the bottom-up cluster taxonomy and the top-down O\*NET task shares that Figures A.1 and A.2 rest on.
19. **The two copies of the appendix differ in the scope of the privacy-threshold sentence and neither is marked as superseding the other.** Both are linked live from the report page. The appendix carries no version number, revision date or errata note that would let a reader know which sentence governs.

## Verification

**Fetch record — 2026-09-16.**

| URL | Method | Result |
|---|---|---|
| https://cdn.sanity.io/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf | `web_fetch` | **Failed** — `url_not_allowed` from the fetch service. Retrying variants does not help. |
| https://cdn.sanity.io/files/4zrzovbb/website/a3cdcd9e67c3c4c51440429dd016cacba514b35b.pdf | `web_fetch` | **Failed** — same `url_not_allowed` error. |
| https://cdn.sanity.io/files/4zrzovbb/website/f065d6e6f92c65df8244042c83d48872ea308c3a.pdf | `curl` to `/tmp/app1.pdf` | HTTP 200, 846,979 bytes, 6 pages. ETag `bc085cc0c65f12dd6139db7b96b9cb29`; `last-modified: Tue, 24 Mar 2026 01:01:08 GMT`; PDF `/CreationDate D:20260323201954-04'00'`, InDesign 21.2 (Macintosh). Called **copy A** above. |
| https://cdn.sanity.io/files/4zrzovbb/website/a3cdcd9e67c3c4c51440429dd016cacba514b35b.pdf | `curl` to `/tmp/app2.pdf` | HTTP 200, 641,935 bytes, 6 pages. ETag `6a9cf6083ac33fec95a073d26d02e31f`; `last-modified: Tue, 24 Mar 2026 22:03:04 GMT`; PDF `/CreationDate D:20260324102622-07'00'`, InDesign 21.2 (Macintosh). Called **copy B** above. |
| https://www.anthropic.com/research/economic-index-march-2026-report | `curl` to `/tmp/rep.html` | HTTP 200. Fetched only to establish which appendix URLs the report page links and in what role, and for the two report-side numbers quoted under Claim 4 and Claim 5. The report itself is covered by `wiki/reports/economic-index-2026-03-report.md`, not here. |

Both PDFs were read in full twice: through the text layer (`pypdf`, both copies, all 6 pages) and visually (page images rendered with `pdftoppm` at 150–400 dpi, both copies, all 6 pages, plus magnified crops of Table A.1 and of every Figure A.1 panel, Figure A.2 and Figure A.3).

**Differences between the two copies.** Four substantive, all textual; the three figures and Table A.1 are identical.

1. **Running footer.** Copy A prints "anthropic.com" bottom-left on pp.1–6. Copy B prints "anthropic.com" on p.1 only, and on pp.2–6 prints "Appendix to "Anthropic Economic Index report: Learning curves"" instead.
2. **p.2, first sentence.** Copy A: "Our analysis is based on privacy-preserving analysis." Copy B: "Our results are based on privacy-preserving analysis." (Copy A repeats the word "analysis"; copy B does not.)
3. **p.2, third paragraph, opening clause.** Copy A: "In the analysis described in Chapter 2, we rely on statistical models in which…". Copy B: "When we analyze log-level data, we rely on statistical models in which…". The rest of the paragraph is word-for-word identical. This changes the stated scope of the privacy-threshold rule from one chapter to a class of analysis.
4. **p.5, Figure A.1 caption title.** Copy A: "Shifts in the usage across occupational categories". Copy B: "Shifts in usage across occupational categories".

All other text differences between the extracted layers are line-wrap positions only. A pixel-level comparison at 150 dpi confirms p.4 (Table A.1) is identical between the copies outside the footer band (only image rows 1578–1594 of 1650 differ); pp.2–3 differ from the point where the reflowed lines begin; pp.5–6 differ in footer and in sub-pixel page placement, with no difference in plotted points, axis labels, data labels or legends on visual inspection of both copies at 220 dpi.

**Which copy governs.** Copy B is the later build on every available signal: PDF creation timestamp 2026-03-24 10:26 (−07:00) against copy A's 2026-03-23 20:19 (−04:00), and CDN `last-modified` 2026-03-24 22:03 GMT against 2026-03-24 01:01 GMT. On the report page, copy B is the target of the "Appendix — Available here" link under Data availability and of the anchors naming Figures A.2 and A.3; copy A is the target of two earlier Chapter 1 in-text anchors. Both remain live. This file treats copy B's wording as the governing text and records copy A's wording wherever it differs; the primary URL in `wiki/INDEX.md` is copy A, which the lead should consider re-pointing (a note to the INDEX owner, not an edit here, since this thread is not to touch `wiki/INDEX.md`).

**Quotation check.** Every quotation in `## Definitions (verbatim)`, `## Limitations (verbatim)` and `## Open questions, conjectures and promised follow-ups (verbatim)` was checked character-by-character against the `pypdf` text layer of the fetched files and, where the text layer showed kerning artefacts (the extractor renders "Validation" as "V alidation", "Yes" as "Y es", "Task" as "T ask", "Your" as "Y our"), against the rendered page image at 300–400 dpi. The kerning artefacts are extractor artefacts, not Anthropic's text; the quotations above use the correct spelling as printed. Em dashes, hyphens, the `>=` in the Figure A.2 legend, and the "1 - 5" spacing in the AI autonomy prompt are reproduced as printed. The only editorial change inside a quotation is the conversion of the PDF's typographic bullets to Markdown list markers, and the re-ordering noted in `## Definitions (verbatim)` of the two-column bullet list in the "Human time estimate" prompt cell.

**Claim check.** Claims 1, 2, 3, 7 and 8 are taken from the appendix text and are quoted in full in `## Definitions (verbatim)`. Claims 4, 5 and 6 are taken from the figures; the printed data labels (49%, 24%, 7%; 77%, 75%, 68%; 12%, 14%, 17%) were read from the 220 dpi and 400 dpi renderings of both copies and agree. The Figure A.1 table and the unlabelled Figure A.2 points are axis readings by the wiki author, marked as such at the point of use and not to be quoted as published numbers.

**Not attempted.** The parent report PDF (`4053bf34…`, 20 pp) and the third PDF linked from the report page (`a42bc3fc…`, reached from "In a previous report") were not fetched; they belong to other wiki entries.
