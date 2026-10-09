# Editorial notes: E08 Canada developmental redraft

Managed Claude Editor v5, Canadian editorial pilot of 9 October 2026. These notes cover the proposed article only. No live study input, builder, analysis, figure, result, project instruction, ledger, other study or previous version was edited.

## 1. Input provenance and the mid-task branch correction

**Authoritative input.** Branch `work/canada-editorial-pilot-2026-10-09-safe`, commit `276710dfe307af6242f8f951585d879c0202f030`. The pilot `input-manifest.json` on that commit has sha256 `7475e992af94cb0fb642a71a34f16c820dc1a68eed25f144e759c3981f49133d`, matching the value supplied with the correction. Its recorded `base_commit` is `0ed7e4787f89360522ed1a70a67aff982dddd011`.

All 52 manifest entries were verified by sha256 and byte length before drafting. Zero mismatches.

**Correction acknowledged.** Work began against the initial branch `work/canada-editorial-pilot-2026-10-09` (commit `29557e4f4fd6660c551482b64f381e9bc06fe1d1`, 53 manifest entries, manifest sha256 `f21750f7ea147d34948ff8fd692c22c5641a76962a6f84c12f8bf9dd2d9adb49`). That branch was withdrawn because `E08/results.json` contained a suppressed time-off aggregate that should not have been shared. The checkout was moved to the safe branch. The superseded branch has not been merged, pushed or reused, and `results.json` has not been recreated, copied or quoted.

**What had already been read from the initial input.** `AGENTS.md`, `CLAUDE.md`, `PROJECT.md`, `programme/DECISIONS.md`, `team/SETUP.md`, `HANDOVER.md`, `programme/HANDOVER-2026-10-09.md`, the pilot `ASSIGNMENT.md` / `EDITOR-ASSIGNMENT.md` / `input-manifest.json`, `editorial-method-2026-10-09/PROPOSED-METHOD.md`, `approved-revision-2026-10-09/CANADA-INFLUENCE.md`, `reviews/E08-NUMERICAL-REVIEW.md`, `.claude/skills/anthropic-style/SKILL.md`, and from `E08/`: `manuscript.md`, `presentation-copy.json`, `figure-specs.json`, `METHODS.md`, `CLAIMS.csv`, `public-tables.csv`, `scale-comparison.csv`, `influence-summary.json`, `literature-review.md`.

**`E08/results.json` was never opened at any point.** No value from it was read, inferred, transcribed or used. The suppressed quantities concern two Men+ user time-off response categories; both appear in `public-tables.csv` with empty estimate, interval and event fields, and no suppressed quantity is reproduced anywhere in these four outputs. Time-off is outside the article entirely and was not reintroduced.

**No evidential rework was required by the correction.** Comparing the two snapshots, the only differences are the deletion of `results.json`, the branch names in `ASSIGNMENT.md` and `EDITOR-ASSIGNMENT.md`, and the removal of the `results.json` line from `REMOTE-ALLOWLIST.txt`. Every evidence file listed above is byte-identical across the two commits, so the reading done before the correction remains valid against the authoritative input. Figure and numerical evidence used in the redraft comes from `public-tables.csv`, `figure-specs.json`, `scale-comparison.csv` and `influence-summary.json`.

No estimator was run and no respondent data were fetched.

## 2. Owned outputs

All four are inside `programme/gender-index/further-research/canada-editorial-pilot-2026-10-09/editor/`:

- `argument-brief.md`, the developmental argument and paragraph/figure plan.
- `manuscript.md`, the complete proposed article.
- `presentation-copy.json`, the complete compatible copy file.
- `editorial-notes.md`, this file.

**Relative links.** `manuscript.md` is a drop-in replacement for `E08/manuscript.md`, so its relative links (`figures/frequent-work.csv`, `public-tables.csv`, `scale-comparison.csv`, `influence-summary.json`, `influence_check.py`, `methods.html`, `analysis.py`, `literature-review.md`) are relative to the E08 study directory, exactly as in the current master. They resolve when the file is placed there, and were confirmed to resolve in the scratch build described in section 7.

## 3. The diagnosis, and what the redraft does about it

The rejected opening failed because it described a mechanism without naming the technology, the actor, the condition or the consequence, and because its motivation concerned working hours while the data measure the frequency of unpaid job work. Repairing the paragraph alone would have left an article whose motivation and evidence were still joined by an unstated step. The redraft rebuilds the argument.

**The four named defects.**

| Defect | Repair |
|---|---|
| AI absent from the opening | The first sentence names generative AI and states the economic question: AI makes tasks faster, and what happens to the saved time is the consequential separate question. |
| "Working less" ambiguous | The phrase is gone. The three destinations are named separately as a shorter day, more tasks of the same kind, and work the person could not previously take on. The article then fixes on one measured outcome and keeps it named throughout. |
| Non-equivalent alternatives presented as alternatives | The three destinations are stated as distinct outcomes, with an explicit sentence that more than one can happen to the same person. |
| "Depends on demand for output" standing in for a mechanism | Replaced by evidence of who does what. Most surveyed users who named a beneficiary of their own productivity gains named themselves; one in ten said employers or clients were asking for and getting more work. The consequence for the worker follows directly. |

**The bridge from motivation to measure.** The Introduction now states that unpaid job work during personal time is one directly observable part of the destination question, defines it with two concrete examples, and says what should happen to it under each destination. That is followed by the statement that the measure is a frequency and never an hours count, and that a cross-section cannot establish that AI raised or lowered the demands. The bridge is one short passage, not a list of disclaimers.

## 4. Substantive editorial changes

**New title.** From "Generative AI use and unpaid job work: a gender comparison in Canada" to "Generative AI users more often report unpaid job work in their own time: a gender comparison of Canadian employees". The previous title named a topic. The new one states the finding, names the precise outcome, and keeps the gender comparison as the secondary clause, which is where the evidence puts it.

**New central organising claim.** The previous draft presented the association and then four gender contrasts, leaving the reader to work out their relationship. The redraft separates a result that survives every comparison from one that does not, and explains why they differ. That distinction is the article's spine, appears in the headline answer, both section headings, the chart titles and the Discussion.

**The proportional comparison is promoted from an aside to an explanation.** The published ratios of about 2.6 for Women+ and 2.7 for Men+ previously appeared as a qualification. They now carry explanatory weight: because the two proportional associations are close and the Women+ nonuser rate is already higher at 6.2% against 3.9%, a similar proportional association on a higher starting rate produces a larger difference in percentage points. This is reasoning over four published rates and the published ratio table, not a new computation, and it is the only passage in the article that explains the +3.4-point result rather than reporting it. Supported by `scale-comparison.csv` and claim E08-27, whose qualification that no ratio equality test exists is respected: the article says "almost identical" and "close to identical", never "equal" or "the same".

**New explanation of why the common-mix contrast differs.** The article now states that applying the pooled job mix moves the Women+ user rate from 16.3% to 10.6% while the Men+ user rate moves from 10.6% to 11.0%, and that Women+ who report using AI are therefore concentrated in broad job categories where frequent unpaid job work is more common. All four values are published in `public-tables.csv` (claims E08-02 and E08-25). The sentence immediately following states that this does not establish that those occupations cause the unpaid work, and that the 16 categories contain jobs with very different responsibilities. Previously the reader was given two numbers and no account of what moved.

**Concrete explanation of the common mix.** The construct is now explained with its actual dimensions, eight broad occupational groups by two sectors giving 16 combinations, and a labelled illustration using a named combination without an invented number. The previous explanation did not tell the reader how many categories there were.

**The full frequency distribution is promoted into the results.** Its figure marker moves from the Methodology section into the first results section, where it answers the first objection a quantitative reader will raise: that the finding is an artefact of the daily-or-weekly threshold. The supporting prose now states what it shows, that the never category falls from 81.4% to 56.2% among Men+ and from 75.8% to 53.4% among Women+, and that both intermediate categories rise for users in both groups. The figure keeps its `optional: true` flag and renders as a disclosure, which matches its supporting role.

**Discussion rewritten to carry an answer.** The previous Discussion opened with a claim about coexistence and closed with a list of better measurements. The new one leads with the supported insight: participation and working conditions are measured here on the same respondents and do not line up the way a benefits reading of adoption predicts, so participation cannot stand in for workers' experience. The gender finding is then stated at its actual strength. The selection interpretation and the Dillon contrast follow as the honest reading of direction, and the note on what would settle it is explicitly subordinated to the statement that the present finding does not depend on it.

**Reader-facing Methodology rewritten.** Same substantive content, reordered so that a reader meets the population and measures before the diagnostics. Retained in full: survey weights and 1,000 bootstrap replicate sets; intervals as sampling uncertainty only; dependence handled in the paired change; frame exclusions; the 4.9% whole-sample reference-job figure and the absent identifying variable; the 16-stratum support and the education extension at 20,413 respondents and 99.4% of weight; three-respondent and one-respondent smallest components with their rates unpublished; the additive projection as a linear projection without causal content; the influence check as restricted populations with concentrated contributions; the failed age-saturated diagnostic retained as a failure. Added: the published 22.1% whole-file benchmark is flagged as including self-employed respondents and not being the employee adoption rate, and the deletion range for the observed-workforce contrast (0.0 to 4.9 points, 14 of 16 intervals excluding zero) is reported alongside the common-mix range, because reporting the fragility of only one of the two contrasts would be selective.

**Removed.** The sentence "This survey provides a benchmark for that evaluation" and similar process framing; the paragraph structure that listed research-agenda items as a conclusion.

**Not changed.** Every estimate, interval, respondent count and source link. The three research questions are reproduced verbatim and appear once. Discussion precedes Methodology. No em dashes, no first person. Time-off is not reintroduced.

## 5. Changes to `presentation-copy.json`

Only `figure.title` and `figure.description` fields were edited, on three entries. A structural comparison against the current master confirmed that figure identifiers and their order, every `rows` block, `row_order`, every footnote, `unit`, `type`, `source_label`, `source_url`, `reference_line`, `section_label`, `optional` and `optional_label` are unchanged, and that the `time-off` entry is byte-for-byte identical.

| Figure | Field | From | To |
|---|---|---|---|
| `frequent-work` | title | Generative AI users report unpaid job work during personal time more often | Frequent unpaid job work is more common among generative AI users in both gender groups |
| `frequent-work` | description | ...by reported GenAI use. | Share reporting... by reported GenAI use **and gender**. |
| `composition` | title | The larger absolute gap for Women+ depends on the comparison | Four comparisons of the same survey give four different gender contrasts |
| `composition` | description | (unchanged first two sentences) | plus "Only the observed-workforce estimate has an interval excluding zero." |
| `frequency-profile` | title | GenAI users are less likely to report never doing unpaid job work | GenAI users are **much** less likely to report never doing unpaid job work, **in both gender groups** |

Reasons. The first chart plots four rates, so its title now names the comparison the rates support rather than restating the section heading. The second chart's previous title asserted the finding the chart is meant to let the reader judge, and also duplicated the new section heading; the replacement states what the chart contains and the added sentence tells the reader the one thing about the intervals that is not visible at a glance. The third title adds the group scope, because the claim holds in both gender groups and the figure shows that.

The `time-off` entry is retained unchanged because it is required: `build_site.py` indexes `presentation-copy.json` by every figure identifier in `figure-specs.json` and fails if one is absent.

## 6. Sources: version, read depth, and what each supports

**Fetched as originals by this editor, during this task.** Full web text retrieved and read.

| Source | Version | Passage used | What it supports in the article | What it does not support |
|---|---|---|---|---|
| Tamkin and McCrory, [Estimating AI productivity gains from Claude conversations](https://www.anthropic.com/research/estimating-productivity-gains) | Published 25 Nov 2025, page modified 25 Aug 2026 | Overview and "Estimating task length and time savings"; the overview states that Claude speeds up individual tasks by about 80%, and the time-savings section lists prior randomised results of 56%, 40%, 26%, 14% and negative | The single sentence that AI assistance cuts the time a task requires by about 80% on this measure, and that randomised trials in narrower settings report smaller savings including one with no saving at all | Not a population estimate. The article names the tool, the sample of 100,000 Claude.ai conversations and the fact that the estimates are the model's own judgements, and adds that both Anthropic sources describe self-selected users of one product |
| Massenkoff and Huang, [What 81,000 people told us about the economics of AI](https://www.anthropic.com/research/81k-economics) | Published 22 Apr 2026 | "Who benefits from AI?" and "Scope and speed"; the recipient of gains is named in about a quarter of interviews, most of those name themselves through faster tasks, expanded scope and freed-up time, and 10% of those naming a recipient say employers or clients were asking for and getting more work. The quoted developer line is in the opening of "Who worries about job displacement?" | The mechanism bridge: that saved task time has more than one destination and that both the worker-retaining and the employer-absorbing destination are reported in practice | Not an identified effect and not representative. Occupation and sentiment are inferred by classifiers from open-ended answers, and respondents are self-selected personal-account users. The article presents these as reported experience, not as measured outcomes |
| Massenkoff and McCrory, [Labor market impacts of AI](https://www.anthropic.com/research/labor-market-impacts) | Published 5 Mar 2026, modified 9 Sep 2026 | Introduction, "Counterfactuals", "Prioritizing outcomes" | Explanatory technique only. "Prioritizing outcomes" justifies an outcome choice before presenting it, which the redraft imitates by explaining why unpaid personal-time job work is the outcome worth measuring before any rate appears. "Counterfactuals" states an identification problem in plain language without hedging the result, which the Discussion's treatment of selection follows | Nothing substantive. Not cited in the article. No identification claim is borrowed |

**Inherited readings, carried from `E08/literature-review.md` and the programme record. Not re-fetched by this editor.**

| Source | Recorded depth | Use here |
|---|---|---|
| Goldin, [A Grand Gender Convergence](https://www.aeaweb.org/articles?id=10.1257/aer.104.4.1091), AER 104(4), 2014 | **Journal abstract only.** Not a verified full-paper reading | Motivation for the gender comparison. The article attributes the argument to Goldin, states it as her account, and makes no use of any specific result, magnitude or mechanism from the paper. Claim E08-26 |
| Dillon, Jaffe, Immorlica and Stanton, [Shifting Work Patterns](https://arxiv.org/html/2504.11436v4) | Full HTML read in the earlier execution; v4 header with an inconsistent rendered date, retained rather than resolved | The contrasting randomised result in the Discussion. The article states that the measure is recorded activity in digital applications outside normal hours, that it captures telemetry rather than all work, and that it cannot establish whether the work was paid. Claim E08-22 |
| Hahmann and Lovei, [workplace AI use](https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm), Statistics Canada, 17 June 2026 | Full main text read in the earlier execution | Prior Canadian description of adoption, occupation and gender. The article states twice that it does not claim to have found the adoption gap. Claim E08-20 |
| Jiang, Park, Xiao and Zhang | August and October 2025 drafts read. **The February 2026 revision full text remains inaccessible** | Prior work on occupational exposure and diary time. The article describes their measures as different from these and makes no first-ever claim. Claim E08-21 |
| Cranney, Delecourt and Koning, [May 2026 review](https://www.hbs.edu/ris/Publication%20Files/25-023_be8fb517-3dd5-40aa-97f9-4e42e1c8e6ff.pdf) | Fully read in the programme's 1 October record, reused | The interpretation the article qualifies. The literature note records that reading a participation gap as a benefits gap requires assumptions about who receives time or income gains. The Introduction states the review's reading and the assumption it rests on; the Discussion returns to it. No HBS section, no pooled adoption rate and no test of their pooled result |

## 7. Verification performed

**Every quantitative claim in the proposed article was checked against the released aggregate records** by a script comparing each in-text value against `public-tables.csv`, `scale-comparison.csv` and `influence-summary.json`. Thirteen rate, gap, contrast and interval claims matched their `result_id` estimate and interval endpoints exactly. The influence-check claims matched `leave_one_stratum_out.summary`: common-mix point range −2.6 to +0.1 with all 16 intervals including zero; composition change negative in all 16; observed-workforce contrast positive in all 16 with range 0.0 to 4.9 and 14 of 16 intervals excluding zero; concentration shares 46.8% and 67.0%; 10 of 16 categories with a group under 75 respondents covering 41.5% of pooled target weight. Sample counts, collection dates, the 4.9% and 22.1% figures and the 1,000 replicate sets were checked against `METHODS.md`.

**Scratch render.** `build_site.build_study('E08')` was run in `/tmp` against a copy of the study directory with the two proposed files substituted, never against the live tree, because the builder rewrites `figure-specs.json` in place. The build succeeds. The article renders with the three intended figure markers in the intended order and no time-off figure in the body. The research questions render as an ordered list. All 18 links resolve to their intended targets. The three figure SVGs were inspected: axis labels, row labels, values, interval marks and the two Men+ daily use-with-caution markers are unchanged, and the new titles appear in the caption and in the accessible title element. No generated page, SVG or CSV is committed.

**Continuous prose read.** The full article was read as rendered text from start to finish. Six wording corrections followed and were applied: the overstated "all three occur in practice"; a vague per-hundred comparison without its referent; a second-person construction in the Discussion; an informal "the main thing this study adds"; "in some cases none" sharpened to the single trial with no saving; and the headline answer given an explicit "The short answer is" transition after the question list. A sentence was also added noting that both Anthropic sources describe self-selected users of one product rather than a national workforce.

**Consistency.** Title, both section headings, all three chart titles and the Discussion make the same two claims at different levels of detail: the association is large and shared by both gender groups, and the gender ranking depends on which job distribution is described. No heading claims more than its section shows.

## 8. Scientific boundaries, and where the draft stops

Checked line by line against the boundaries in the assignment. The article does not state that AI raises hours, unpaid work, output or pay; does not state that women receive fewer benefits; does not say occupation explains away the gender difference; does not present the negative common-mix estimate as a reversal, and says so explicitly; does not treat an interval containing zero as equality, and says so explicitly; does not claim methodological novelty or a first finding; does not promise a causal answer; and does not conclude with a call for better data. Restricted-population deletions are described as restricted populations and not as alternative national estimates. No private fine-cell result is exposed.

## 9. Unresolved weaknesses

1. **Goldin is the load-bearing motivation and is read at abstract level only.** The gender comparison rests on the claim that jobs reward long and particular hours. The article attributes this to Goldin and uses no magnitude from her paper, but a full-paper reading would be needed before any stronger statement about the mechanism. The article does not test it.
2. **The explanation of the +3.4-point result relies on close but untested ratios.** The point ratios of 2.6 and 2.7 have no published uncertainty, so the article can say they are almost identical but cannot say the proportional associations are equal. A reader could reasonably ask for an interval on the ratio contrast. Producing one would be new analysis and is outside this assignment.
3. **"Women+ who report using AI are concentrated in broad job categories where frequent unpaid job work is more common"** is an inference from four published standardised and four published raw rates. It is sound as composition arithmetic, but the underlying stratum-level pattern is private, so the reader cannot inspect it and must take the aggregate movement on trust.
4. **The latest Jiang full text is still inaccessible**, so the contribution statement remains deliberately narrow and cannot be strengthened.
5. **The Dillon comparison relies on an inherited reading** with a known version-date inconsistency in the source. The article's use of it is limited to the design and the direction of the out-of-hours result.
6. **Reporting behaviour is not addressed in the article body.** Employees who use AI for work may be more conscious of, or more willing to report, work done in their own time. It is listed in the argument brief as an interpretation that would change the meaning of the association, and it is covered only generically in Methodology under measurement limits. A referee may reasonably ask for one explicit sentence in the Discussion; it was left out to keep that section an argument rather than a list, and this is flagged as a deliberate, reviewable omission.
7. **The article asserts that the three destinations of saved time all have evidence behind them** on the strength of one self-selected survey. The in-text qualification states the limitation, but the claim would be better supported by a representative source if one exists.
8. **Two Anthropic sources appear in the Introduction of an article whose own evidence is a Canadian government survey.** This is proportionate to the explanatory job they do and both are named with their populations, but the balance is a judgement an author may want to revisit.

## 10. Status, spend and stopping point

This is a proposed article for Emily's review. It is not approved, reviewed or publication-ready. The numerical reconstructions and the completed all-16-stratum influence check were reused and not rerun. No reviewer agent, paid session or second opinion was commissioned, and no new analysis, data acquisition or novelty search was performed.

**Spend.** No per-session cost figure is exposed to this editor at runtime, so an actual dollar amount cannot be reported honestly. The work was a single session within the authorised $13.50 service limit, with no cap increase requested and no additional paid session started. Three external web fetches were made, all to the public Anthropic research pages named in the assignment. The authoritative spend figure is the platform's record for this session and should be entered in `team/RUNS.csv` by the coordinator.

The editor stops here. The referee stage has not been started.
