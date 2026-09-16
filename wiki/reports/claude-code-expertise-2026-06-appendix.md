# Appendix to "Agentic Coding and Persistent Returns to Expertise"

The companion methodology appendix to the ~400,000-session Claude Code paper. It is where the
classifier prompts are printed in full, where the sample is given exact counts, where the
task-value estimator is calibrated and validated, and where the regressions behind the paper's
central claim are tabulated.

Its parent paper is a separate wiki slug, `claude-code-expertise-2026-06`. This file
cross-references it and does not summarise it. Where the appendix settles or contradicts something
in the parent, that is recorded here and flagged.

## Source

| Field | Value |
|---|---|
| Slug | `claude-code-expertise-2026-06-appendix` |
| Title (from page 1) | Appendix to "Agentic Coding and Persistent Returns to Expertise" |
| Date (from page 1) | June 2026 |
| Type | Appendix (standalone 27-page PDF; not bound into the paper) |
| Publisher | Anthropic |
| Primary URL (copy I, the URL in `wiki/INDEX.md`) | https://cdn.sanity.io/files/4zrzovbb/website/a94728142a45694292336165947f8d6e3e1a357e.pdf |
| Second copy (copy H) | https://cdn.sanity.io/files/4zrzovbb/website/7426c33b0e75ab4771c465d30d5bc1019bdd0c9c.pdf |
| Parent paper | "Agentic coding and persistent returns to expertise", 2026-06-16, https://www.anthropic.com/research/claude-code-expertise (separate wiki entry `claude-code-expertise-2026-06`) |
| Length | 27 pages in both copies |
| Authors, acknowledgements, citation block | **None.** The appendix carries no author list, no acknowledgements, no BibTeX and no references. Every attribution has to be taken from the parent paper. |

**Page map.** p.1 title page; p.2 "Sample"; p.3 "Classifier Prompts" and "Work Mode"; pp.3–5 the
work-mode prompt and its nine options; pp.5–7 "User expertise" and its six options; pp.7–10
"Occupation (user profile)" and its 24 options; pp.10–11 "Occupation (work performed)" and its 23
options; pp.11–14 "Session outcome (judged success)" and its four options; pp.14–16 "Success
signal" and its six options; pp.16–17 "Failure signal" and its six options; pp.17–18 "Estimated
task value (freelance-equivalent price)" and its two prompts; p.18 "Validation on a stratified
holdout"; p.19 the tier-by-tier validation table, two notes, and "Choice of calibration examples";
p.20 "Choosing the pricing model", the model-grid table and "Derived measures and definitions";
p.21 the remaining derived measures, "Classifier validation and cross-check", "Classifiers versus
telemetry" and Figure A1; p.22 "Internal outcome validation", Figure A2 and "Classifier validation
via strong-model agreement"; pp.22–24 the strong-model agreement section; p.24 "Robustness of the
expertise-success gradient" and "Verified success and expertise under cumulative controls"; p.25
Table A1 with its caption, the paragraph continuation, and "Verified success by expertise level
(step function)"; p.26 blank apart from the running footer; p.27 Table A2 with its caption.

**The two copies.** Both are linked live from the parent paper's web page: copy I from six rendered
links (every in-text "Appendix" anchor, and the word "here" in the "Available here" line under Data
availability), copy H from exactly one — the trailing full stop after that "here", which is the
stray link already noted in `wiki/reports/claude-code-expertise-2026-06.md`. Copy I is the later
build and is treated here as the governing text. The two are identical in every figure,
every table and every classifier prompt; they differ in exactly one character, a doubled full stop
on p.2 in copy H ("analysis infrastructure.." against copy I's "analysis infrastructure."). The CDN
serves them under the filenames `CCEconReport-Appendix-I.pdf` and `CCEconReport-Appendix-H.pdf`
respectively; the letters are build labels, not volume numbers — there is no Appendix II. See
`## Verification` for the timestamps and the byte-level comparison. Because the divergence is a
typo and not a number or a cross-reference, the `room/director-2026-09-16-pdf-web-ruling.md`
requirement to record both versions side by side is satisfied by this paragraph alone; all
quotations below are copy I and are word-for-word identical in copy H.

## Claims

Numbered, each with its page and, where relevant, its table or figure. Numbers are given as
published. Values inside Tables A1 and A2 and the two unnumbered tables are printed text that the
PDF happens to rasterise (the pages carry no text layer for them); they were read from 200 dpi
renderings of both copies and agree between the copies. Values plotted in Figures A1 and A2 carry
no printed data labels; where the body text states them, the body text is cited, and nothing is
read off an axis.

**The sample, exactly**

1. **398,198 sessions from 234,751 users, uniformly randomly sampled, October 2025 to April 2026
   inclusive.** "The analysis covers 398,198 sessions uniformly randomly sampled from Claude Code
   traffic. These sessions come from 234,751 users." (p.2). The parent paper rounds these to
   "~400,000 interactive sessions from ~235,000 people" (`claude-code-expertise-2026-06`, PDF p.2);
   the appendix is where the exact figures appear. Comparison: none — this is the sample frame.
2. **The panel is thin but not trivial.** "73,066 users appear more than once in the sample, 6,382
   users appear more than 5 times and 1,413 users appear more than 10 times." (p.2). This is the
   only repeat-use distribution published anywhere in the release, and it is new information
   relative to the parent paper, which reports no within-user structure at all. Comparison: within
   the sample, users by session count.
3. **Internal Anthropic usage is excluded from the main sample.** "We exclude internal Anthropic
   usage." (p.2). The same internal sessions are then used as a separate validation sample (claim
   19), so the exclusion is from the measurement sample only.
4. **Sessions with zero human turns are excluded, and that is what "headless" means
   operationally.** "Sessions with zero human turns are excluded—these excluded sessions are
   non-interactive calls in "headless" mode i.e., via claude -p "<prompt>"." (p.2). The parent
   paper states the exclusion as a category ("headless" mode, third-party IDEs, SDKs); the appendix
   gives the rule that implements it. No count or share is published for the excluded sessions.
5. **Every classifier sees at most 25,000 characters of a session.** "For each classifier call, the
   model is shown the session transcript (human, assistant, and system turns) with each turn
   middle-truncated at 5,000 characters and the transcript as a whole truncated at 25,000
   characters." (p.2). This constraint appears nowhere in the parent paper. It sits directly against
   the appendix's own description of the object being classified: "a single session can span
   hundreds of turns, files, and tool calls, and hours (or even days) of work" (p.22).
6. **Model and decoding settings.** "Almost every classifier below is a single call to Claude Sonnet
   4.6 at temperature 0.2 that must answer with exactly one of the listed options—the exception is
   the estimated task value classifier which uses Claude Haiku 4.5 for an initial summarizer prompt
   and Opus 4.7 for an estimation prompt." (p.2). The parent paper says only "All classifiers in
   this report use Claude Sonnet 4.6 unless otherwise noted" (footnote 5); the appendix supplies the
   temperature, the single-call structure, the forced-choice constraint and the two-model exception.
7. **The telemetry inventory, including one field never used in a reported result.** "The telemetry
   we use here includes the number of human prompts ("turns"), model calls (API requests),
   successful tool calls, output tokens, lines of code added and removed and the age of the user's
   account (days since signup with Anthropic, not with Claude Code specifically)." (p.2). Account
   age is disclosed as available and appears in no published table, figure or regression in either
   document.
8. **Privacy machinery: cell suppression on distinct users.** "Researchers never read individual
   sessions or transcripts, and every number in this report is an aggregate over a cell of sessions
   that is suppressed unless it contains a minimum number of distinct users." (p.2). The threshold
   value is not published. Table A1's caption shows the rule binding in practice: "columns (4)-(6)
   have fewer due to cells that fell under the aggregation limit" (p.25).

**What the classifiers actually are**

9. **The nine work modes are forced-choice with no abstention.** "There is NO 'Unclear' option —
   pick the BEST fit from the nine, even when evidence is thin." (p.3). The nine labels are verbs:
   "Plan, Build, Fix, Understand, Test, Operate, Analyze, Orchestrate, or Communicate" (p.3). The
   parent paper's Figure 1 labels are prose glosses of these ("fixing something broken", "building
   something new"); the appendix gives the label set the classifier actually returns.
10. **Work mode is assigned by volume of work, not by stated intent.** "Pick by DOMINANT activity,
    measured by volume of meaningful work, NOT by the user's stated intent in turn 1." (p.3). Seven
    explicit pairwise tie-break rules are printed (Build vs Fix, Build vs Analyze, Build vs Test,
    Build vs Operate, Plan vs Understand, Understand vs Analyze, Understand vs Fix), plus rules for
    Orchestrate and Communicate (p.3).
11. **The expertise scale has a sixth option the parent paper never mentions: Unclear.** "Pick
    EXACTLY ONE of these labels: 1, 2, 3, 4, 5, or Unclear, where 1 = Novice, 2 = Beginner, 3 =
    Intermediate, 4 = Advanced, 5 = Expert, and Unclear when evidence is too thin." (p.5). The
    parent paper describes a "five-point scale from novice to expert" with no abstention (PDF p.6).
    No share of Unclear-rated sessions is published anywhere, and Table A2 (p.27) reports only
    levels 1–5.
12. **The three expertise signals are declared co-equal, and two of them are explicitly narrowed.**
    "Weigh these three signals TOGETHER — they are co-equal, not ranked" (p.6). Setup specificity
    excludes what is visible on screen: "Naming files or paths that are visible on screen is NOT
    domain knowledge — anyone using Claude Code does that." (p.6). Verification is rated by type,
    not presence: "Generic asks ('please double-check', 'are you sure?', 'verify your work') are
    EPISTEMIC HUMILITY, not expertise — a careful novice does this." (p.6). Direction of correction
    is symmetric and can be neutral (p.6).
13. **The expertise prompt explicitly forbids rating on Claude's performance or on difficulty.**
    "Rate domain expertise, NOT general intelligence, NOT Claude's performance, and NOT task
    difficulty." (p.5). This is the appendix's answer to the dependence worry the parent paper does
    not raise; it is an instruction, not a test. Note that the instruction coexists with a level-1
    definition resting on Claude's behaviour ("Does not notice when Claude produces wrong output.
    Claude has to supply or correct basic domain concepts the user did not bring", p.6) and a level-5
    definition resting on the same ("Direction of correction is user→Claude, never Claude→user on
    domain matters", p.7).
14. **There are two occupation classifiers, not one.** "Occupation (user profile)" guesses the
    user's own profession from side signals and may return Unclear (pp.7–10); "Occupation (work
    performed)" assigns the occupation whose workers would typically do the session's work and has
    no Unclear option (pp.10–11). The parent paper describes only the first. The second is what
    Table A1's "Task-occupation FE" control is built from, which means the parent paper's phrase
    "the same task subject" (Figure 5 caption, PDF p.13) denotes a second SOC classification, not a
    topic taxonomy. Comparison: the two classifiers share the same 23 SOC major groups and differ in
    exactly three respects (see `## Definitions (verbatim)`).
15. **The judged-success classifier is a two-step procedure with a stated default.** "This is a
    TWO-STEP judgment — do both steps before you output a label" (p.12); step 1 identifies the
    primary objective, step 2 judges the outcome. The default on thin evidence is asymmetric:
    "When the transcript is thin and you cannot tell from explicit signals, default to Succeeded if
    the trajectory is clean and the agent is on-task" against "pick Failed only if the trajectory
    looks broken" (p.13). Comparison: none published — the asymmetry is not quantified.
16. **Judged success deliberately folds verifiable and inferred wins together.** "It does NOT
    measure how verifiable the outcome was — verifiable wins (commits, test passes, explicit 'ship
    it') and inferred wins (clean ending with no complaint) both belong in 'Succeeded'." (p.12).
    This is why the separate signal classifiers exist.
17. **The truncation marker is explicitly ruled out as outcome evidence.** "if the transcript shows
    a `[TRANSCRIPT TRUNCATED FOR LENGTH]` marker, the cut is NOT outcome evidence" (p.12), with a
    fallback instruction to "judge from the trajectory: clean / agent-on-task → Succeeded; loop /
    error / complaint → Failed; mixed → Partially Succeeded" (pp.12–13). So truncated sessions are
    judged, not dropped.
18. **The success and failure signal scales are 1–5 with NONE as an explicit zero, and the modal
    short session is a 2.** "The 1-5 scale (with NONE as the explicit zero)" (pp.15, 16); success
    signal 2 is "soft signal: clean ending, no complaint, no commit/test/explicit affirmation (the
    modal short CC session)" (p.15). Since verified success requires signal 4 or 5 (claim 24), the
    modal session is by construction excluded from verified success.

**The task-value estimator**

19. **The estimator is a two-call pipeline: rewrite the session as a job posting, then price the
    posting.** The first call (Claude Haiku 4.5) rewrites the transcript as "an equivalent
    Upwork-style job posting" returning a JSON title, 3–5 sentence description and 3–8 skill tags
    (pp.17–18); the second (Opus 4.7) "prices that posting against a calibration corpus of 200 real
    freelance postings with their actual prices—a tier-balanced sample drawn from a public
    job-postings datasets from 2024-2026" (p.18). The parent paper says only that value is
    "calibrated against a public dataset of real postings" (PDF pp.9–10); the appendix gives the
    pipeline, the marketplace ("Upwork-style"), the calibration size and the vintage. The dataset
    is still not named in either document.
20. **The posting corpus and its filters.** "Postings are eligible for the calibration sample if
    they are fixed-price, priced between $10 and $50,000, and have a description of at least 50
    characters. About 23,000 postings survive these filters." (p.18). Comparison: none stated — no
    pre-filter count is published, so the selectivity of the filters cannot be assessed.
21. **The estimator's headline accuracy is log R² = 0.38 on a 999-posting stratified holdout.** "In
    a holdout study with 999 job postings, the task value estimator reaches log R² = 0.38. To
    construct the holdout, we gathered 250 examples from four price tiers ($10–200, $200–1,000,
    $1,000–5,000, and $5,000–50,000), drawn from the same filtered corpus described above." (p.18).
    Metrics are defined as "log R² (Pearson R² between log actual and log predicted price), level R²
    (the same in raw dollars), and multiplicative bias (the geometric mean of predicted/actual)",
    with "1,000-draw bootstraps" for the intervals (p.18).
22. **Within-tier accuracy is near zero, and the headline number is mostly cross-tier ordering.**
    The unnumbered tier table on p.19 (read from the rendered page; the page has no text layer for
    it):

    | Tier | n | log R² [95% CI] | level R² [95% CI] | Bias | Median pred. | Median actual |
    |---|---|---|---|---|---|---|
    | Overall | 999 | 0.38 [0.32, 0.44] | 0.38 [0.32, 0.44] | 0.66 | $500 | $900 |
    | $10–200 | 250 | 0.16 [0.08, 0.25] | 0.16 [0.08, 0.25] | 2.39 | $150 | $50 |
    | $200–1,000 | 250 | 0.07 [0.02, 0.14] | 0.07 [0.02, 0.14] | 1.10 | $400 | $300 |
    | $1,000–5,000 | 249 | 0.06 [0.02, 0.13] | 0.06 [0.02, 0.13] | 0.53 | $1,000 | $1,500 |
    | $5,000–50,000 | 250 | .01 [0.00, 0.03] | .01 [0.00, 0.03] | 0.14 | $2,000 | $8,000 |

    The appendix's own reading: "the overall 0.38 largely reflects cross-tier ordering—because the
    holdout weights all four tiers equally, the pricer earns credit for placing $50 jobs below
    $8,000 jobs even where it cannot rank jobs within a tier. Within-tier discrimination is
    concentrated at the low end and is essentially zero above $5,000." (p.19). **Wiki author's note,
    not the appendix's:** the log R² and level R² columns carry identical values and identical
    intervals in all five rows, which cannot both be true of the two metrics as defined on p.18
    ("the same in raw dollars"). One of the two columns is almost certainly a production error. Any
    post citing a level R² from this table must say so.
23. **Bias reverses across the price range, by roughly an order of magnitude at each end.** "Note
    also that bias reverses across the range. Small jobs are over-priced about 2.4x, the largest
    under-priced about 7x. So, we generally use these task value estimates ordinally rather than
    using them to get aggregate task values." (p.19). Comparison: the $10–200 tier's bias of 2.39
    against the $5,000–50,000 tier's 0.14, both in the p.19 table. This is the strongest constraint
    published on the parent paper's "+27%" task-value series, and it is published only here.
24. **The corpus is dominated by small jobs, and the calibration set was rebalanced because of it.**
    "The filtered corpus of job postings is heavily skewed toward small jobs (the distribution across
    the four tiers is roughly 62% / 27% / 9% / 2%)." (p.19). With a uniform calibration draw the
    pricer "under-priced $5,000+ jobs by roughly 12x (median prediction $800)"; balancing to 50
    examples per tier "raised the prediction level for larger jobs (median prediction for $5,000+
    jobs rose to $2,000) and gave the best overall accuracy. On small jobs, ranking accuracy was
    statistically unchanged, at the cost of somewhat more over-pricing." (p.19). Comparison: two
    calibration variants on the same holdout.
25. **The model-and-calibration grid, with the shipped variant highlighted.** The unnumbered table
    on p.20 (read from the rendered page; the shipped row is printed in bold on a shaded ground):

    | Pricing model | Calibration examples | Log R² | Level R² | Bias (geomean) |
    |---|---|---|---|---|
    | Sonnet 4.6 | uniform | 0.33 | 0.11 | 0.56 |
    | Sonnet 4.6 | tier-balanced | 0.33 | 0.09 | 0.86 |
    | Opus 4.7 | uniform | 0.36 | 0.06 | 0.46 |
    | **Opus 4.7** | **tier-balanced** | **0.38** | **0.09** | **0.66** |

    Framing: "Holdout accuracy for this task is model-dependent, so the cited validation numbers are
    specific to the exact model and prompt the pipeline runs." (p.20). Comparison: four
    model × calibration cells on the same stratified holdout. **Wiki author's note:** the shipped
    cell's Level R² here is 0.09, while the p.19 table's Overall level R² is 0.38 for what is the
    same configuration on the same holdout. The two published tables disagree, which is further
    reason to treat the level R² column on p.19 as an error rather than a result.

**Derived measures, and the threshold the parent paper got wrong**

26. **Verified success = judged Succeeded AND success signal 4 or 5.** "A session reaches verified
    success when the outcome classifier judges it Succeeded AND the success-signal classifier scores
    4 or 5—i.e., the transcript carries at least one hard verifiable signal (a matching commit, a
    passing test suite, a command completing with output matching the objective, or explicit user
    confirmation)." (p.20). Identical in substance to the parent paper's Table 2.
27. **"Hits trouble" is failure signal 3 or higher — which resolves the parent paper's PDF/web
    disagreement in favour of the PDF.** "A session hits trouble when the failure-signal classifier
    scores 3 or higher" (p.20). The parent paper's Figure 5 caption reads "failure signals ≥ 3" in
    the PDF and "failure signals > 3" on the web page (recorded in `claude-code-expertise-2026-06`).
    The appendix's ≥ 3 agrees with the PDF; the web page is the outlier. Comparison: the definition
    against its two published statements.
28. **Abandoned, and wrote code.** "A troubled session is abandoned when the outcome classifier
    judges it Failed AND telemetry records zero lines of code added." (p.20). "A session wrote code
    when telemetry records at least one line of code added." (p.21).
29. **Software/math versus other professions is built on the user-profile classifier, and about 30%
    of sessions are excluded from every occupation analysis.** "A user is counted in software-related
    occupations when the user-profile occupation classifier returns Computer and Mathematical; "other
    identified professions" are all other SOC major groups. Sessions whose user profile is Unclear
    are excluded from occupation analyses (about 30% of sessions)." (p.21). The parent paper states
    the positive side ("about 70% of sessions"); the appendix states the exclusion.

**Validation**

30. **The two signal classifiers track the independent outcome judgment monotonically.** "the share
    of sessions judged Succeeded rises from 13% at success-signal 1 to 90% at success-signal 5, and
    falls from 85% at failure-signal 1 to 3% at failure-signal 5 (Figure A1)." (p.21). Figure A1's
    plot title is "Outcome-classifier internal consistency (398K sessions)" (figure label, p.21);
    its panels are labelled "Convergent: success signal vs outcome" and "Discriminant: failure
    signal vs outcome" (figure labels, p.21). No data labels are printed on the bars; the five
    values per panel are stated in the body text quoted above, and error bars are drawn but not
    defined. Comparison: P(judged succeeded) across the five levels of each signal classifier, on
    the full sample. **Note on what this is:** three classifiers reading the same transcript,
    compared with each other — the plot title calls it "internal consistency", the body text calls
    the outcome judgment "independent", and no external referent enters.
31. **Decision attribution converges with harness telemetry on planning, and execution share does
    not.** "Sessions the classifier scores as more Claude-led on planning show more model calls per
    human prompt and more tool calls per human prompt, convergence between a transcript-based
    judgment and harness-recorded telemetry. Execution share is near-orthogonal to these (Figure
    A2)." (pp.21–22). Figure A2's plot title is "Claude's share of decisions versus actions and
    words per prompt"; panels "Claude actions per prompt" and "Claude output words per prompt
    (thousands)"; three series, "Planning share", "Overall share", "Execution share"; x-axis bands
    0-20, 20-40, 40-60, 60-80, 80-100 "% of decisions attributed to Claude" (figure labels, p.22).
    No data labels are printed and no values are recorded here. Comparison: telemetry means by
    decision-share band, by attribution dimension.
32. **The expertise–success gradient replicates on internal Anthropic sessions, within engineer, and
    against an outcome that is not a classifier.** "We ran the same classifier prompts on internal
    Anthropic Claude Code sessions, where session IDs can be joined to observable engineering
    outcomes (whether the session's commits landed on the main branch). The expertise–success
    gradient replicates on this sample, including within-engineer (comparing sessions of the same
    person at different rated expertise levels): judged success rises by roughly 3–5 percentage
    points per expertise level with author fixed effects, and sessions at higher rated expertise are
    more likely to produce code that lands." (p.22). This is the single most consequential result in
    the appendix: it is the only place in the release where the gradient is estimated with person
    fixed effects and the only place where it is checked against an outcome observed outside the
    transcript. Comparison: within-engineer, across that engineer's own sessions at different rated
    expertise levels. No sample size, no standard error, no table, and no figure are published for
    it; the 3–5 pp range is per level on judged success, not on verified success, so it is not
    directly comparable with Table A1's +0.0379.
33. **Classifier agreement with a strong reference model, on 198 public sessions.** "We re-ran the
    report's classifiers (using the models used in the report) on 198 sessions from SWE-chat, a
    public dataset of real coding-agent sessions recorded from public GitHub repositories across
    several harnesses. We then used a strong reference model (Mythos Preview) to label the same
    sessions, treating the reference model labels as reliable and consistent proxies for
    ground-truth." (p.23). Disagreements were adjudicated blind by the same reference model, and
    "one of the authors of this report blindly re-adjudicated all concerning disagreements" (p.23).
    Results: "The report's classifier and the reference agree on 78-98% of sessions on the
    categorical classifiers. On the classifiers with ordinal scales, the report's classifier and the
    reference agree on 78-99% counting adjacent scale points as agreement, and 53-68% counting only
    exact matches as agreement. The judge rated a vast majority of the disagreements as genuinely
    ambiguous—concerning disagreements are 0-3% of sessions per classifier (at most 5 of 198). In
    the final step, a human reviewer audited the 15 disagreements the judge had flagged as concerning
    and concurred with the judge in 11 of 15 sessions." (p.23). Comparison: report classifier against
    reference model, per classifier, on 198 sessions. No per-classifier breakdown is published — only
    the ranges — so which classifier sits at 53% exact agreement and which at 68% is not knowable
    from the document.
34. **The appendix states the condition under which its comparisons survive its own measurement
    error, and says it did not check it.** "most of the report's conclusions rest on relative
    comparisons, i.e., differences between groups and changes over time, and on those, the classifier
    is more reliable. As long as the classifier's mistakes are similar across groups (which we did
    not extensively verify here), those mistakes cancel each other out when making comparisons."
    (p.23).

**The regressions behind the paper's central claim**

35. **Table A1: the expertise coefficient falls by about 11% as controls are added and remains
    highly significant.** Table A1, p.25, "Verified success and expertise under controls", read from
    the rendered page. The coefficient is "the change in the probability of verified success per step
    on the five-point expertise scale" (p.25).

    | Row | (1) | (2) | (3) | (4) | (5) | (6) |
    |---|---|---|---|---|---|---|
    | Expertise (per level, 1–5) | +0.0426 | +0.0507 | +0.0443 | +0.0442 | +0.0379 | +0.0364 |
    | (standard error) | (0.0008) | (0.0008) | (0.0008) | (0.0008) | (0.0009) | (0.0009) |
    | Work mode × task-value band FE | | ✓ | ✓ | ✓ | ✓ | ✓ |
    | Month FE | | | ✓ | ✓ | ✓ | ✓ |
    | Task-occupation FE | | | | ✓ | ✓ | ✓ |
    | User-occupation FE | | | | | ✓ | ✓ |
    | Model-tier × session-length-band FE | | | | | | ✓ |
    | ln(model calls), ln(human turns) | | | | | | ✓ |
    | Sessions | 359,586 | 359,586 | 359,586 | 353,347 | 351,603 | 302,647 |
    | Fixed-effect cells | — | 36 | 252 | 615 | 1,130 | 4,438 |
    | R² | 0.009 | 0.066 | 0.081 | 0.083 | 0.088 | 0.136 |

    Caption: "OLS with fixed effects. 375,687 sessions, columns (4)-(6) have fewer due to cells that
    fell under the aggregation limit. Standard errors in parentheses, clustered by user. Column (5)
    is the preferred specification. It compares sessions doing the same kind of work, at the same
    estimated value, in the same month, on the same type of task, from users in the same occupational
    group. Column (6) additionally conditions on choices made during the session (model, length).
    Excludes sessions with no clear goal." (p.25). Comparison: six cumulative specifications on the
    same dependent variable, each adding one control. Each column is described as testing a named
    alternative: "that expert-rated users pick different kinds of work (column 2), work in different
    months (3), work on different subjects (4), hold different occupations (5), or run longer
    sessions on stronger models (6)" (pp.24–25). **Wiki author's note:** the caption says 375,687
    sessions, while the Sessions row reads 359,586 in columns (1)–(3) — and no column reports 375,687.
    The two are not reconciled anywhere in the document. Any post citing the regression sample must
    quote both.
36. **Table A2: the gradient is concave, and most of it is between novice and intermediate.** Table
    A2, p.27, "Verified success versus expertise, as a step function", read from the rendered page.
    Coefficients are in percentage points against Novice; standard errors in parentheses.

    | Expertise | Sessions | Unadjusted rate | Coefficient (vs. Novice) | Adjusted rate |
    |---|---|---|---|---|
    | 1 (Novice) | 5,911 | 13.2% | — | 14.5% |
    | 2 (Beginner) | 73,858 | 20.9% | +6.4 (0.7) | 20.9% |
    | 3 (Intermediate) | 96,516 | 28.0% | +13.8 (0.7) | 28.3% |
    | 4 (Advanced) | 146,879 | 29.3% | +15.0 (0.7) | 29.5% |
    | 5 (Expert) | 36,422 | 34.7% | +18.4 (0.7) | 32.9% |

    Caption: "OLS with the Column (5) fixed effects from Table A1. Standard errors in parentheses,
    clustered at the user level. Novice is the reference category, so its coefficient is not defined.
    The unadjusted rate is the raw share of sessions at each expertise level ending in verified
    success, with no controls. The adjusted rate holds the fixed effects constant. Excludes sessions
    with no clear goal." (p.27). Comparison: each expertise level against Novice, under the column-(5)
    fixed effects. Three things this adds to the parent paper, which publishes only the adjusted
    series as a chart: the per-level sample sizes; the unadjusted series beside the adjusted one; and
    the standard errors. The distribution is heavily weighted to level 4 — Advanced is the largest
    cell, Novice the smallest by an order of magnitude.
37. **The expertise scale is linear by assumption in Table A1 and only relaxed in Table A2.** "Table
    A1 assumes that expertise is a linear scale, i.e., that each step of the expertise scale is worth
    the same. Table A2 instead uses an indicator for each level of the expertise scale, under the
    Table A1 column-(5) fixed effects, with Novice as the omitted category." (p.25).
38. **A cross-reference error in the parent-paper pointer.** p.25 says of Table A2: "It is the
    construction behind Figure 6." In the parent paper, Figure 5 is the expertise–success chart and
    Figure 6 is the occupation chart (`claude-code-expertise-2026-06`, PDF pp.13, 15). Table A2's
    content — verified success by expertise level, adjusted — is the construction behind Figure 5,
    not Figure 6. Recorded per `room/director-2026-09-16-pdf-web-ruling.md`: both the appendix's
    pointer and the parent's figure numbering are reproduced here and neither is treated as
    governing.
39. **Wiki author's consistency check on published table values, not a claim of the appendix.** The
    five per-level Sessions entries in Table A2 total 359,586, the figure printed in Table A1 columns
    (1)–(3). So Table A2's five rows exhaust the column-(1) estimation sample, which means sessions
    rated Unclear on expertise (claim 11) are outside it, as are the "no clear goal" sessions both
    captions exclude. Neither exclusion is counted in the document.

## Definitions (verbatim)

All quotations are copy I and are word-for-word identical in copy H, with one exception noted at the
point of use (the doubled full stop in the p.2 privacy sentence). The curly quotation marks, arrows,
em dashes, literal `**` markers, capitalisation and internal punctuation inside the quotations are
Anthropic's; the outer quotation marks and the Markdown list markers are this file's. Where the
appendix uses a bolded run-in head before a definition ("Verified success.", "Hits trouble." and the
rest on pp.20–21), the head is named outside the quotation rather than reproduced inside it, because
its bold is typographic and not an asterisk in the source; the `**` markers that *are* literal
characters in the classifier prompts are reproduced. The PDF's typographic bullets (•) are
reproduced as `•` where they are bullets in the source and as Markdown hyphens where the source uses
a hyphen. Three source errors are reproduced rather than corrected and marked *[sic]* or noted where
they occur.

### Sample (p.2)

> "Our sample covers interactive Claude Code sessions between October 2025 and April 2026
> (inclusive). This includes sessions conducted through the Claude Code command-line interface, the
> Claude Code desktop app, and claude.ai. This excludes Claude Code usage via third party integrated
> developer environments as well as via software development kits. Sessions with zero human turns
> are excluded—these excluded sessions are non-interactive calls in "headless" mode i.e., via claude
> -p "<prompt>"." (p.2)

> "The analysis covers 398,198 sessions uniformly randomly sampled from Claude Code traffic. These
> sessions come from 234,751 users. 73,066 users appear more than once in the sample, 6,382 users
> appear more than 5 times and 1,413 users appear more than 10 times. We exclude internal Anthropic
> usage." (p.2)

> "All classifications ran through our privacy-preserving analysis infrastructure. Researchers never
> read individual sessions or transcripts, and every number in this report is an aggregate over a
> cell of sessions that is suppressed unless it contains a minimum number of distinct users." (p.2)

This is the one sentence where the two copies differ: copy H reads "…analysis infrastructure.." with
a doubled full stop. The rest of the sentence is identical.

> "For each classifier call, the model is shown the session transcript (human, assistant, and system
> turns) with each turn middle-truncated at 5,000 characters and the transcript as a whole truncated
> at 25,000 characters. Almost every classifier below is a single call to Claude Sonnet 4.6 at
> temperature 0.2 that must answer with exactly one of the listed options—the exception is the
> estimated task value classifier which uses Claude Haiku 4.5 for an initial summarizer prompt and
> Opus 4.7 for an estimation prompt." (p.2)

> "Alongside the classifiers, we use telemetry recorded automatically for every session. The
> telemetry we use here includes the number of human prompts ("turns"), model calls (API requests),
> successful tool calls, output tokens, lines of code added and removed and the age of the user's
> account (days since signup with Anthropic, not with Claude Code specifically)." (p.2)

### Work Mode (pp.3–5)

The appendix's own gloss, outside the prompt box:

> "This classifier categorizes each session into one of nine work modes that best describes what the
> session is trying to accomplish." (p.3)

The prompt, in full:

> "Classify the WORK MODE of this Claude Code session. Pick EXACTLY ONE of: Plan, Build, Fix,
> Understand, Test, Operate, Analyze, Orchestrate, or Communicate. Each label is a verb describing
> what the user is doing." (p.3)

> "There is NO 'Unclear' option — pick the BEST fit from the nine, even when evidence is thin. If
> the session is short or ambiguous, pick the verb that best fits the small amount of evidence rather
> than abstaining." (p.3)

> "**Pick by DOMINANT activity, measured by volume of meaningful work, NOT by the user's stated
> intent in turn 1.** If a session opens with planning but then spends most turns writing code,
> that's Build, not Plan. The triggering intent doesn't decide the label — the bulk of the work
> does." (p.3)

> "Key distinctions:
> **Build vs Fix**: Build adds, evolves, refactors, optimizes WORKING code. Fix is reactive — the
> trigger is something broken.
> **Build vs Analyze**: Build = code is the deliverable for ongoing use. Analyze = code is
> INSTRUMENTAL; the artifact is an insight, chart, or model.
> **Build vs Test**: writing tests is Test. Fixing app code revealed broken by tests is Fix.
> Building test infrastructure itself is Build.
> **Build vs Operate**: shipped code is Build. Deploy / config / CI / env / monitoring is Operate.
> **Plan vs Understand**: Plan looks forward (designing). Understand looks at what exists.
> **Understand vs Analyze**: Understand is about code / systems / concepts. Analyze is about data.
> **Understand vs Fix**: investigation with no fix = Understand. Investigation that resolves into a
> code change to make broken behavior correct = Fix.
> **Orchestrate**: meta-AI work. Apps that happen to call an LLM are Build.
> **Communicate**: deliverable is human-readable words / slides. Pairs with codebase_context = 'Not
> in a codebase'." (p.3)

The nine options, in full (pp.4–5):

> "- Plan: Pre-implementation strategy. The user is figuring out HOW to do something before doing
> it: architecture, specs, design docs, tradeoff analysis, sequencing, scoping. The deliverable is a
> plan / spec / decision, NOT working code. If the session starts with planning but then transitions
> into building, classify by the dominant activity." (p.4)

> "- Build: Write, refactor, migrate, or extend code. The user is producing or evolving code that is
> ITSELF the deliverable — a service, library, CLI, script, endpoint, component, ETL pipeline,
> configuration consumed by software. Subsumes new code, feature additions, refactors,
> optimizations, dependency updates, and migrations. Use Build whenever the primary output of the
> session is delivered or maintained code." (p.4)

> "- Fix: Reactive fault diagnosis and bug fix. The session is triggered by code or behavior that is
> BROKEN — produces wrong output, errors, crashes, fails tests, returns the wrong thing, regresses
> an earlier behavior. The work is finding the cause and making it right. NOT this: code that works
> correctly but is slow / suboptimal / ugly (that's Build). NOT this: writing tests for working code
> (that's Test)." (p.4)

> "- Understand: Explore, investigate, root-cause-for-comprehension, audit-for-understanding.
> Primary output is KNOWLEDGE about a system, code, or concept — not a code change. Code review for
> understanding, tracing how a flow works, learning a new framework, investigating WHY something
> behaves a certain way without intent to change it, onboarding to a codebase. NOT this:
> investigation that resolves into a fix (that's Fix). NOT this: data analysis (that's Analyze).
> Hallmark: knowledge in the user's head at the end, not code in the repo." (p.4)

> "- Test: Test, code review, QA, security audit. Deliverable is VERIFICATION of correctness —
> writing new tests, fixing or extending the test suite, security or vulnerability review, QA /
> acceptance checking, formal-method-style verification. Includes test infra, fixtures, mocks,
> coverage tooling. NOT this: fixing application code revealed broken by tests (that's Fix). NOT
> this: code review aimed primarily at learning the codebase (that's Understand)." (p.4)

> "- Operate: Deploy, configure, monitor, on-call, CI/CD, env / dependency setup. The session works
> on the SCAFFOLDING around code rather than the code itself: Dockerfiles, k8s manifests, Terraform,
> GitHub Actions / CI workflows, deploy scripts, env-var management, package install, on-call
> paging, log triage, monitoring dashboards, infra provisioning, rolling out a release. NOT this:
> writing infra-as-code as part of building a new infra TOOL (that's Build). Hallmark: operational /
> lifecycle work." (p.4)

> "- Analyze: Data analysis, research coding, analytics. Primary output is analytical artifacts —
> numbers, tables, plots, reports, models — where any code is INSTRUMENTAL (one-shot scripts,
> notebooks, exploratory queries) rather than the deliverable. Examples: computing summary
> statistics, building plots, running a regression, exploring a dataset, training a one-off ML model
> for analysis, writing a SQL query for a report. NOT this: production ETL pipelines or recurring
> data services (that's Build). NOT this: code review of analysis code (that's Test or Understand).
> Hallmark: the artifact at the end is an INSIGHT, not running software." (pp.4–5)

> "- Orchestrate: Orchestrate Claude or other AI agents — meta-work where the deliverable is an AI
> artifact. Prompt engineering, designing agent workflows, building eval harnesses for LLMs, tuning
> agent behavior, debugging an agent, drafting agent system prompts, writing classifiers powered by
> Claude, building tool-use loops, constructing few-shot or many-shot examples. NOT this: writing
> application code that happens to call an LLM as a feature (that's Build with an LLM/Agents
> domain). Hallmark: the session's primary intellectual work is on the AI system itself." (p.5)

> "- Communicate: Non-code knowledge work for a HUMAN AUDIENCE. The user is using Claude Code as a
> general assistant to produce, refine, or work out PROSE / SLIDES / MESSAGES / NOTES intended for
> human readers: business writing (memos, emails, briefs, slides, reports), drafting / editing essays
> or narratives, synthesizing external research into a writeup, personal knowledge management (notes,
> summaries, journaling, organizing thinking), planning a meeting / trip / decision in prose,
> brainstorming captured as text, conversational math or finance done for a writeup. Hallmark:
> deliverable is words / slides / human-readable artifacts, NOT code, NOT analytical numbers, NOT
> AI-system tuning." (p.5)

### User expertise (pp.5–7)

The appendix's own gloss:

> "This classifier measures the strength of the user's expertise exhibited in a session, on a
> five-point scale." (p.5)

The prompt, in full:

> "Classify the user's apparent EXPERTISE in the specific domain/task they are attempting in this
> session. Pick EXACTLY ONE of these labels: 1, 2, 3, 4, 5, or Unclear, where 1 = Novice, 2 =
> Beginner, 3 = Intermediate, 4 = Advanced, 5 = Expert, and Unclear when evidence is too thin." (p.5)

> "This measures domain-specific familiarity with the WORK being done — command of the terminology,
> structures, and conventions of whatever they are doing in this session. Someone can be a senior
> software engineer but a beginner at Rust, SOC coding, or differential privacy — rate them on the
> task AT HAND, not their career. Rate domain expertise, NOT general intelligence, NOT Claude's
> performance, and NOT task difficulty." (p.5)

> "Weigh these three signals TOGETHER — they are co-equal, not ranked:" (p.6)

> "SETUP SPECIFICITY — does the user frame the problem using named entities and constraints that
> require domain knowledge to even reach for? 'analyze this data' vs. 'compute the IRR over the
> cohort tagged _2024H2' sit at different ends. Naming files or paths that are visible on screen is
> NOT domain knowledge — anyone using Claude Code does that. Weight things the user could only say
> if they already knew the domain." (p.6)

> "VERIFICATION TYPE — what kind of verification does the user ask for? Generic asks ('please
> double-check', 'are you sure?', 'verify your work') are EPISTEMIC HUMILITY, not expertise — a
> careful novice does this. Targeted asks ('show me how you set the config for X', 'did you actually
> call commit()?', 'what is the cardinality of that join?') require knowing WHAT to check, which is
> expertise. Rate the TYPE, not the presence." (p.6)

> "DIRECTION OF CORRECTION — who corrects whom on domain matters? If Claude has to correct the
> user's terminology, mental model, or approach ('actually, X doesn't work that way — you probably
> want Y'), that pulls the rating DOWN toward 1-2. If the user catches Claude's domain mistakes or
> steers away from a wrong approach Claude proposed, that pulls UP toward 4-5. If neither side
> corrects the other on domain matters, this signal is neutral." (p.6)

The six options, in full (pp.6–7):

> "- 1: Novice. Framing is generic or imprecise; does not use domain-specific names for the things
> being worked on. Verification asks are absent or entirely generic ('please double-check'). Does
> not notice when Claude produces wrong output. Claude has to supply or correct basic domain concepts
> the user did not bring. May be articulate in prose, but the words are in service of asking for
> help, not directing a piece of domain work." (p.6)

> "- 2: Beginner. Framing uses some correct terminology, but loosely or with occasional mis-use.
> Verification asks are mostly generic with at most occasional targeted ones. Pushes back on
> obviously wrong outputs but misses subtle ones. Claude corrects or reframes the user's approach or
> terminology at least once. Specifies WHAT they want at a high level but not the specific shape,
> constraints, or invariants. A fluent technologist working OUTSIDE their domain — articulate, names
> the files in front of them, states goals clearly, but lacks the domain-specific mental model —
> lands here, not at 3 or 4." (p.6)

> "- 3: Intermediate. Framing is precise at a directive level — names the files, the outputs, the
> categories, the libraries — but does not engage with methodology or tradeoffs. Mix of generic and
> targeted verification. Catches meaningful mistakes but does not routinely invoke specific technical
> reasoning when correcting. Neither side is consistently correcting the other on domain matters. A
> domain expert delegating a routine task they do not need to think hard about can also land here."
> (pp.6–7)

> "- 4: Advanced. Framing shows structural domain knowledge in at least one way that is NOT readable
> off the screen: names a specific edge case, non-obvious constraint or invariant, version-specific
> behavior, or known failure mode; describes the problem in domain-precise terms beyond what a
> beginner would reach for. Merely naming files, paths, or visible APIs does NOT count — those are
> available to anyone looking at the codebase. Verification or correction is moderately specific —
> points to a particular mechanic or asks for a specific piece of state ('did you actually...', 'show
> me the config for...') at least once. The user catches at least one of Claude's domain mistakes or
> steers away from a wrong approach; Claude does not have to correct the user's domain model." (p.7)

> "- 5: Expert. Framing or steering shows ANY of: insider-only naming (jargon / conventions / library
> internals that only a practitioner uses), unprompted discussion of tradeoffs, surgical verification
> asks ('what's the blocking factor on dim 2 of that kernel?', 'is the policy evaluating
> principal.group or request context?'), authoritative corrections invoking specific technical
> reasoning, preemptive edge-case handling, or test designs targeting specific failure modes. One or
> two of these in a session is enough — do not require all of them. Direction of correction is
> user→Claude, never Claude→user on domain matters. The defining vibe is 'insider talking to an
> equal' even when the session is short." (p.7)

> "- Unclear: Reserve for sessions where the user's contribution is so thin that NO
> direction-of-expertise signal exists — almost entirely tool calls / retry requests with no
> substantive framing at all. When ANY framing is present, even sparse, pick the best-fit 1-5 level
> rather than abstaining." (p.7)

### Occupation (user profile) (pp.7–10)

The appendix's own gloss:

> "This classifier guesses the user's likely occupation given the available signals in the session,
> such as hints from claude.md files and project memory, specific technical or industry jargon, and
> referenced artifacts. It chooses one of 23 major groups of the BLS Standard Occupational
> Classification, or, if there are not enough signals to make a solid guess, the classifier returns
> "Unclear."" (p.7)

The prompt:

> "Pick the SOC (Standard Occupational Classification, U.S. BLS) MAJOR GROUP that describes the
> USER'S own most likely real-world profession — NOT the occupation of whoever would typically
> perform THIS SESSION's work." (p.8)

> "The distinction matters: a lawyer using Claude Code to build a weekend side project is, for THIS
> question, 'Legal Occupations' — the side signals (their language, their references, their files,
> their context) point to law, even if the work they are doing in this session is something else
> (e.g. Python coding)." (p.8)

> "What to look at:
> • CLAUDE.md files the agent loads (any path). They often encode the user's professional context —
> 'this is a research repo for computational biology work', 'this repo is a trading strategy
> backtester', 'this is a law firm's document-automation tooling'. These are strong signals about the
> user's background.
> • Memory files / directory names / repo structure referenced in the session. A user directory
> containing clinical_trial_loader.py, econ_analysis.py, or contract_review/ reveals the user's
> professional world.
> • The user's vocabulary in their messages — technical shorthand, jargon only an insider would use,
> references to tools/frameworks/conventions from a specific field.
> • Referenced artifacts — do they mention patents? legal filings? clinical data? financial reports?
> an instrument? a classroom? a shipping schedule? These leak profession.
> • Domains mentioned in passing that the user doesn't explain — fluent name-dropping reveals
> professional background." (p.8)

> "What NOT to use:
> • Do NOT classify on the task being performed in this session. If the only signal is 'they are
> writing Python', that is not user-profile evidence, that is task evidence.
> • Do NOT classify on the language/tools Claude Code itself uses. CC uses Bash/Read/Write for any
> user." (p.8)

> "Use 'Unclear' when there is no affirmative side signal beyond the act of coding. The fact that
> someone is writing code in Claude Code is NOT evidence they are a software developer by profession
> — every CC user writes code. Only pick 'Computer and Mathematical' when there is a specific signal
> that software/data IS their profession: CLAUDE.md describing a software product or engineering
> team, professional dev vocabulary, references to deploy/CI/review process, etc. Otherwise,
> Unclear." (p.8)

The 24 options, in full (pp.9–10):

> "- Management Occupations: Business/organizational leadership, strategic planning, general
> operations management, HR leadership.
> - Business and Financial Operations: Analysts, accountants, buyers, HR specialists, compliance,
> market research, fundraising.
> - Computer and Mathematical: Software developers, data scientists, network architects,
> statisticians, researchers in computing or mathematics. Only pick this when there is an affirmative
> signal that software/data is the user's PROFESSION, not just what they are doing in this session.
> - Architecture and Engineering: Engineers (hardware, civil, mechanical, electrical, chemical,
> industrial), architects, drafters.
> - Life, Physical, and Social Science: Scientists in biology, chemistry, physics, economics,
> psychology; lab researchers.
> - Community and Social Service: Counselors, social workers, clergy, community health workers.
> - Legal Occupations: Lawyers, paralegals, judges, legal support.
> - Educational Instruction and Library: Teachers, professors, tutors, librarians, instructional
> designers, curriculum developers.
> - Arts, Design, Entertainment, Sports, and Media: Writers, editors, designers, artists, musicians,
> journalists, translators, technical writers.
> - Healthcare Practitioners and Technical: Doctors, nurses, therapists, pharmacists, diagnostic
> technicians.
> - Healthcare Support: Aides, orderlies, medical assistants.
> - Protective Service: Police, firefighters, security guards, correctional officers.
> - Food Preparation and Serving: Chefs, cooks, servers, bartenders.
> - Building and Grounds Cleaning and Maintenance: Custodians, groundskeepers, pest control.
> - Personal Care and Service: Hairstylists, childcare, fitness trainers, funeral services.
> - Sales and Related: Sales reps, retail associates, real estate agents, insurance agents.
> - Office and Administrative Support: Admin assistants, secretaries, billing clerks, receptionists,
> office operations.
> - Farming, Fishing, and Forestry: Farmers, ranchers, agricultural workers, loggers.
> - Construction and Extraction: Construction trades, carpenters, electricians, plumbers, miners.
> - Installation, Maintenance, and Repair: Mechanics, technicians, repair of machinery or vehicles.
> - Production: Manufacturing workers, assemblers, machinists, printers.
> - Transportation and Material Moving: Drivers, pilots, logistics, warehouse workers.
> - Military Specific: Military-only occupations (combat specialists, special forces).
> - Unclear: Use this when there is NO affirmative side signal about the user's professional world
> beyond the act of coding itself. The fact that the user is writing code in Claude Code is NOT
> evidence of profession — every CC user writes code. If the only signals are 'writes Python', 'uses
> git', 'edits files', pick Unclear, do NOT default to Computer and Mathematical." (pp.9–10)

### Occupation (work performed) (pp.10–11)

The appendix's own gloss:

> "This classifier categorizes the occupation that the work performed in the session is typically
> associated with, choosing one of 23 major groups of the BLS Standard Occupational Classification."
> (p.10)

The prompt:

> "Pick the SOC (Standard Occupational Classification, U.S. BLS) MAJOR GROUP whose workers would
> typically perform the kind of work the user is doing in this Claude Code session. Match on the WORK
> ITSELF, not on the session's topic — a session about drafting a contract might still be performed
> by a paralegal, a product manager, or a writer; only pick 'Legal Occupations' if the user is doing
> lawyer-style legal analysis. Pick EXACTLY ONE of the 23 SOC major groups — there is no Unclear
> option. If signal is thin, pick the best-fit group from whatever the transcript shows." (p.10)

Its option list is the same 23 SOC major groups printed for the user-profile classifier, in the same
order and with the same glosses, with exactly three differences (verified by comparing the two
lists character by character):

1. "Computer and Mathematical" drops the user-profile caveat, reading only: > "- Computer and
   Mathematical: Software developers, data scientists, network architects, statisticians, researchers
   in computing or mathematics." (p.10)
2. "Legal Occupations" gains a qualifier: > "- Legal Occupations: Lawyers, paralegals, judges, legal
   support — actual legal analysis and drafting, not just touching a legal topic." (pp.10–11)
3. There is no "Unclear" option.

### Session outcome (judged success) (pp.11–14)

The appendix's own gloss:

> "This classifier judges whether the user, overall, accomplished what they set out to do. It first
> identifies the user's primary objective in the session and then judges the outcome." (p.11)

The prompt, in full:

> "Judge the OUTCOME of this Claude Code session — did the user accomplish what they set out to do?"
> (p.12)

> "Pick EXACTLY ONE of: Succeeded, Partially Succeeded, Failed, or No clear goal. There is NO 'Cannot
> Judge' option — pick the best fit from the four, even when evidence is thin." (p.12)

> "This facet measures ONE THING: the outcome (succeeded / partially succeeded / failed / no clear
> goal). It does NOT measure how verifiable the outcome was — verifiable wins (commits, test passes,
> explicit 'ship it') and inferred wins (clean ending with no complaint) both belong in 'Succeeded'.
> Verifiable failures (errors, explicit 'didn't work') and inferred failures (looping agent, silent
> abandonment) both belong in 'Failed'." (p.12)

> "This is a TWO-STEP judgment — do both steps before you output a label:
> **Step 1 — Identify the user's PRIMARY OBJECTIVE.**
> Read the whole transcript and infer what the user was trying to accomplish overall. This is usually
> set by the first few user messages but may evolve over the session. If the user had multiple
> sub-tasks, pick the most significant one (or the only unifying one). Some sessions have no clear
> objective — pure exploration, chat, open-ended 'what do you think' — in which case the objective is
> genuinely absent and the answer is 'No clear goal'." (p.12)

> "Long sessions evolve through phases (plan → execute → verify). Identify the dominant operational
> objective by what the bulk of the session WORK serves, not by the first message's framing alone. If
> the user opens with a planning question ('can you suggest a plan?', 'how would you approach
> this?') BUT the session then pivots to executing on the planned work, the goal IS the planned work
> — pick that. 'No clear goal' is reserved for sessions that stay exploratory throughout, with no
> execution phase. If the agent committed code, ran a successful build, or produced a final artifact,
> the goal is whatever produced that artifact." (p.12)

> "**Truncation note:** if the transcript shows a `[TRANSCRIPT TRUNCATED FOR LENGTH]` marker, the cut
> is NOT outcome evidence — it just means there was more content than fit. Default to the strongest
> signal you can see in the visible head + tail. If neither side is visible, judge from the
> trajectory: clean / agent-on-task → Succeeded; loop / error / complaint → Failed; mixed → Partially
> Succeeded." (pp.12–13)

> "**Step 2 — Judge the OUTCOME.**
> Read the whole transcript and decide which label best describes what happened, using whichever
> signals are available — hard or soft." (p.13)

> "Signals pointing toward SUCCEEDED (any of these — hard or soft):
> • A git commit / PR open / PR merge that matches the objective
> • A test suite passing on the change, or a command running successfully to completion producing the
> requested output
> • Explicit user affirmation — 'thanks', 'ship it', 'perfect', 'this works', 'exactly right'
> • The final artifact exists and the user doesn't complain
> • The session ends cleanly with the agent having done what was asked, no errors, no complaints, no
> goal-reframing" (p.13)

> "Signals pointing toward FAILED (any of these — hard or soft):
> • User explicitly says it didn't work / is wrong / nevermind / 'this is broken'
> • Final tool calls error out and are not recovered
> • Tests fail at the end
> • The agent loops, gives up, or apologizes without fixing
> • The user abandons mid-task in a way that signals the goal was not met" (p.13)

> "Pick the label that best fits:
> • Succeeded — outcome signals point toward the goal being met. The modal short CC session that ends
> cleanly with the agent having done what was asked belongs here. Don't downgrade just because no
> commit or test confirmed it. When the transcript is thin and you cannot tell from explicit signals,
> default to Succeeded if the trajectory is clean and the agent is on-task.
> • Partially Succeeded — some sub-tasks done, others not; user accepted reduced scope; outcome is
> genuinely mixed.
> • Failed — outcome signals point toward the goal NOT being met, whether by explicit error/complaint
> or by quiet abandonment / looping / clearly-fell-short work. When the transcript is thin and you
> cannot tell from explicit signals, pick Failed only if the trajectory looks broken (errors, looping,
> complaints).
> • No clear goal — no operational objective in the first place; success frame doesn't apply." (p.13)

> "DO NOT confuse 'the agent worked competently' with 'the user's goal was achieved'. The agent can
> write clean code that does the wrong thing. Judge OUTCOME vs. goal, not agent quality." (p.14)

The four options, in full (p.14):

> "- Succeeded: The user's primary objective was accomplished. Use this whenever the best read of the
> transcript is that the user got what they wanted — whether that judgment rests on HARD signals (a
> git commit matching the work, a test passing, a PR opened/merged, the user saying 'thanks' /
> 'perfect' / 'ship it', a command running to completion with output matching the objective, an
> artifact the user confirms) or SOFTER signals (the agent produced what was asked, the session ended
> cleanly, the user did not push back). This bucket folds together the modal short CC session that
> ended without complaint AND the longer session that ended with explicit verification — both are
> 'Succeeded'." (p.14)

> "- Partially Succeeded: Some but not all of the primary objective was achieved. The user accepted a
> reduced scope, moved goalposts mid-session, acknowledged one piece worked and another didn't, or
> the agent made progress on parts of the task but hit a wall on a specific sub-task. Use when the
> outcome is genuinely mixed — neither a clean success nor a clean failure." (p.14)

> "- Failed: The user's primary objective was NOT achieved. Use this whenever the best read of the
> transcript is that the user did not get what they wanted — whether that judgment rests on HARD
> signals (final commands errored out and weren't recovered, tests failed at the end, the user
> explicitly said 'this didn't work' / 'nevermind' / expressed frustration) or SOFTER signals (the
> agent looped or gave up, the work clearly fell short of the ask, the user abandoned mid-task in a
> way that signals the goal was not met). Like 'Succeeded', this folds verifiable and inferred
> failures into one outcome bucket." (p.14)

> "- No clear goal: The user did not have a single discernible primary objective — exploratory chat,
> wandering conversation, open-ended 'what do you think' with no operational outcome requested.
> Success is not the right frame for this session. Use when the frame doesn't apply." (p.14)

### Success signal (pp.14–16)

The appendix's own gloss — note the mismatch, reproduced as printed:

> "This classifier looks for signals of success across the session such as git activity, successful
> tests, and user affirmation. It is used in conjunction with the session outcome classifier
> throughout the report, e.g., in the definition of verified success. If there are no observable
> failure signals, it returns "None."" (p.14) *[sic — the success-signal classifier's own prompt
> defines NONE as "no observable success-shaped signal at all" (p.15); the gloss says failure]*

The prompt, in full:

> "Judge how STRONGLY the transcript verifies that success-shaped work happened in this Claude Code
> session — on a 1-5 ordinal scale, or NONE if there is no success-shaped signal at all. This
> measures evidence strength on the success side, regardless of whether the session actually
> succeeded." (p.15)

> "The 1-5 scale (with NONE as the explicit zero):
> • NONE — no observable success-shaped signal at all
> • 1 — barely any signal; faint trace; nothing verifiable
> • 2 — soft signal: clean ending, no complaint, no commit/test/explicit affirmation (the modal short
> CC session)
> • 3 — moderate signal: clean ending + at least one concrete piece of corroborating evidence
> (successful command output, artifact whose content matches ask, neutral user acknowledgement)
> • 4 — strong signal: at least one HARD verifiable signal (commit / test pass /
> command-completion-with-matching-output / explicit user affirmation / user-confirmed artifact)
> • 5 — very strong signal: MULTIPLE corroborating hard signals" (p.15)

> "Pick the highest tier that the transcript supports. The scale is ordinal — moving up requires MORE
> evidence, not different evidence." (p.15)

> "DO NOT confuse 'the agent worked competently' with 'success was verified'. The agent can write
> clean code that does the wrong thing — that is at most a 2 or 3. A high score here just means strong
> EVIDENCE on the success side." (p.15)

The six options, in full (pp.15–16):

> "- 1: Very weak. Barely any success-shaped signal — a stray polite remark, a minor 'ok', the agent
> producing something inconsequential. Nothing verifiable; nothing the user actively endorsed. Use
> when you can detect the faintest positive trace but don't want to call it 'NONE'." (p.15)

> "- 2: Soft. Agent produced what was asked and the artifact exists at session end; session ended
> cleanly with no errors, no complaints, no goal-reframing; user did not push back. No commit / test /
> explicit affirmation. The MODAL pattern for many short CC sessions." (p.15)

> "- 3: Moderate. Clean ending PLUS at least one concrete piece of corroborating evidence — a
> successful command running to completion, an artifact whose content visibly matches the ask, a
> neutral user acknowledgement that the work was received. Stronger than 'Soft' because there is
> concrete evidence the work hit the target, but no single HARD signal yet." (p.15)

> "- 4: Strong. At least one HARD verifiable success signal: a git commit whose message matches the
> work, a PR opened or merged, a test suite passing on the change, a command running to completion
> with output matching the stated objective, an explicit user affirmation ('thanks', 'perfect', 'ship
> it', 'this works', 'exactly right', concrete praise), OR a final artifact the user explicitly
> confirms. One hard signal, on its own." (pp.15–16)

> "- 5: Very strong. MULTIPLE corroborating hard signals — e.g., commit + passing test, OR explicit
> 'ship it' + a confirmed artifact, OR PR merged + user thanks, OR test pass + explicit verification
> by the user. The transcript leaves no room to doubt that the success happened." (p.16)

> "- NONE: No observable success-shaped signal at all. The session may have failed (errors,
> abandonment, explicit complaints), may have been cut off before any work could complete, may be
> pure exploration / open-ended chat where success isn't the right frame, or may be so
> tool-noise-dominated that no user-facing artifact is observable." (p.16)

### Failure signal (pp.16–17)

The appendix's own gloss — the mirror-image mismatch, reproduced as printed:

> "This classifier looks for signals of failure across the session such as user concern or
> frustration, failing tests, or looping. If there are no observable success signals, it returns
> "None."" (p.16) *[sic — the failure-signal classifier's own prompt defines NONE as "no observable
> failure-shaped signal at all" (p.16); the gloss says success]*

The prompt, in full:

> "Judge how STRONGLY the transcript verifies that failure-shaped work happened in this Claude Code
> session — on a 1-5 ordinal scale, or NONE if there is no failure-shaped signal at all. This
> measures evidence strength on the failure side, regardless of whether the session actually failed."
> (p.16)

> "The 1-5 scale (with NONE as the explicit zero):
> • NONE — no observable failure-shaped signal at all
> • 1 — barely any signal; faint trace; immediately recovered
> • 2 — soft signal: agent looped briefly, work mildly off-target, user expressed mild concern
> • 3 — moderate signal: agent gave up on a sub-task, work clearly fell short on one dimension, user
> pushed back without explicit rejection
> • 4 — strong signal: at least one HARD verifiable signal (unrecovered final error, failing test at
> end, explicit user complaint or rejection, expressed frustration)
> • 5 — very strong signal: MULTIPLE hard failure signals" (p.16)

> "Pick the highest tier that the transcript supports. The scale is ordinal — moving up requires MORE
> evidence, not different evidence." (p.17)

> "Two traps to avoid: (1) a single intermediate tool error that the agent recovers from is at most a
> 1 — the FINAL state is what counts. (2) Polite user disengagement at the end of a clean session is
> NOT a failure signal — silence after success-shaped work is just silence." (p.17)

The six options, in full (p.17):

> "- 1: Very weak. Barely any failure-shaped signal — a fleeting agent apology that was immediately
> recovered, a transient retry, a minor user nitpick. Use when you can detect the faintest negative
> trace but don't want to call it 'NONE'." (p.17)

> "- 2: Soft. Agent looped briefly, OR work is mildly off-target, OR user expressed mild concern that
> the agent addressed. The session reads as imperfect but not failure-shaped overall." (p.17)

> "- 3: Moderate. Agent gave up on a sub-task, OR work clearly fell short on one dimension, OR user
> pushed back without explicitly rejecting the work. There is concrete evidence of friction but no
> hard final failure." (p.17)

> "- 4: Strong. At least one HARD verifiable failure signal: final tool calls error out and are not
> recovered, a test suite fails at the end of the session, the user explicitly says it didn't work /
> 'this is broken' / 'nevermind' / expresses concrete frustration, or the user explicitly rejects the
> work the agent produced. One hard signal, on its own." (p.17)

> "- 5: Very strong. MULTIPLE hard failure signals — errors + explicit complaint + abandonment, OR
> multiple failed sub-tasks without recovery, OR the user repeatedly rejecting work. The transcript
> leaves no room to doubt that the failure happened." (p.17)

> "- NONE: No observable failure-shaped signal. The session may have succeeded (cleanly or
> verifiably), may be open-ended chat where failure isn't the right frame, or may be cut off before
> any outcome could form." (p.17)

### Estimated task value (freelance-equivalent price) (pp.17–18)

> "The task-value estimate is produced in two model calls. The first call (Claude Haiku 4.5) rewrites
> the session as a freelance job posting:" (p.17)

The first prompt, in full:

> "Read this Claude Code session transcript and describe it as an equivalent Upwork-style job posting
> — as if a client were hiring a freelancer to perform the work Claude actually did in the session."
> (p.18)

> "Write as the client would, not the freelancer. Focus on scope and deliverables. Do not mention
> Claude, AI, or that this came from a Claude Code session." (p.18)

> "Output a single JSON object only, no commentary:
> {
>     "title": "short listing-style title, 80 chars or less",
>     "description": "3-5 sentences describing the work and deliverables",
>     "skills": ["3-8 skill tags"]
> }
> <transcript>
> {TRANSCRIPT}
> </transcript>" (p.18)

The second call and the calibration corpus:

> "The second call (Opus 4.7) prices that posting against a calibration corpus of 200 real freelance
> postings with their actual prices—a tier-balanced sample drawn from a public job-postings datasets
> from 2024-2026. Postings are eligible for the calibration sample if they are fixed-price, priced
> between $10 and $50,000, and have a description of at least 50 characters. About 23,000 postings
> survive these filters." (p.18) *[sic — "a public job-postings datasets"]*

> "Below, we discuss the development and validation of this classifier in more detail." (p.18)

The validation metrics, defined:

> "We report three metrics: log R² (Pearson R² between log actual and log predicted price), level R²
> (the same in raw dollars), and multiplicative bias (the geometric mean of predicted/actual).
> Confidence intervals are 1,000-draw bootstraps." (p.18)

### Derived measures and definitions (pp.20–21)

Under the bolded run-in head "Verified success.":

> "A session reaches verified success when the outcome classifier judges it
> Succeeded AND the success-signal classifier scores 4 or 5—i.e., the transcript carries at least one
> hard verifiable signal (a matching commit, a passing test suite, a command completing with output
> matching the objective, or explicit user confirmation)." (p.20)

Under the run-in head "Hits trouble.":

> "A session hits trouble when the failure-signal classifier scores 3 or higher:
> concrete evidence of struggle—an error, a failed test, an abandoned sub-task, repeated attempts, or
> the user pushing back." (p.20)

Under the run-in head "Abandoned.":

> "A troubled session is abandoned when the outcome classifier judges it Failed AND
> telemetry records zero lines of code added." (p.20)

Under the run-in head "Wrote code.":

> "A session wrote code when telemetry records at least one line of code added." (p.21)

Under the run-in head "Software/math vs. other professions.":

> "A user is counted in software-related occupations when the
> user-profile occupation classifier returns Computer and Mathematical; "other identified professions"
> are all other SOC major groups. Sessions whose user profile is Unclear are excluded from occupation
> analyses (about 30% of sessions)." (p.21)

### Figure and table captions (pp.21, 22, 25, 27)

> "Figure A1. Success outcome versus success and failure signals
> The left panel shows the probability that the success outcome classifier records "succeeded" for
> sessions of each success signal strength. The right panel shows the probability that the success
> outcome classifier records "succeeded" for sessions of each failure signal strength." (p.21)

> "Outcome-classifier internal consistency (398K sessions)" (p.21, plot title of Figure A1)

> "Figure A2. Claude's share of decisions versus actions The left panel shows Claude's average
> actions per prompt for each band of decision share attributed to Claude. The right panel shows
> Claude's average words per prompt for each decision share band." (p.22)

> "Claude's share of decisions versus actions and words per prompt" (p.22, plot title of Figure A2)

> "Table A1. Verified success and expertise under controls
> OLS with fixed effects. 375,687 sessions, columns (4)-(6) have fewer due to cells that fell under
> the aggregation limit. Standard errors in parentheses, clustered by user. Column (5) is the
> preferred specification. It compares sessions doing the same kind of work, at the same estimated
> value, in the same month, on the same type of task, from users in the same occupational group.
> Column (6) additionally conditions on choices made during the session (model, length). Excludes
> sessions with no clear goal." (p.25)

> "Table A2: Verified success versus expertise, as a step function
> OLS with the Column (5) fixed effects from Table A1. Standard errors in parentheses, clustered at
> the user level. Novice is the reference category, so its coefficient is not defined. The unadjusted
> rate is the raw share of sessions at each expertise level ending in verified success, with no
> controls. The adjusted rate holds the fixed effects constant. Excludes sessions with no clear
> goal." (p.27)

### Section headings, verbatim and in order

"Sample" (p.2) · "Classifier Prompts" (p.3) · "Work Mode" (p.3) · "User expertise" (p.5) ·
"Occupation (user profile)" (p.7) · "Occupation (work performed)" (p.10) · "Session outcome (judged
success)" (p.11) · "Success signal" (p.14) · "Failure signal" (p.16) · "Estimated task value
(freelance-equivalent price)" (p.17) · "Validation on a stratified holdout" (p.18) · "Choice of
calibration examples" (p.19) · "Choosing the pricing model" (p.20) · "Derived measures and
definitions" (p.20) · "Classifier validation and cross-check" (p.21) · "Classifiers versus
telemetry" (p.21) · "Internal outcome validation" (p.22) · "Classifier validation via strong-model
agreement" (p.22) · "Robustness of the expertise-success gradient" (p.24) · "Verified success and
expertise under cumulative controls" (p.24) · "Verified success by expertise level (step function)"
(p.25).

## Data and methods

In the wiki author's words, with page references. This section says what the appendix adds to, or
changes about, the parent paper's method; the parent's own account is in
`wiki/reports/claude-code-expertise-2026-06.md`.

**Sample, with exact numbers.** 398,198 interactive Claude Code sessions, uniformly randomly
sampled from Claude Code traffic, October 2025 to April 2026 inclusive, from 234,751 users, with
internal Anthropic usage excluded (p.2). Included surfaces: the CLI, the desktop app and claude.ai.
Excluded: third-party IDEs, SDKs, and any session with zero human turns (the operational definition
of headless `claude -p` use). The repeat-use distribution is published for the first time here:
73,066 users appear more than once, 6,382 more than five times, 1,413 more than ten times (p.2). So
about 31% of users contribute more than one session, and the panel is deep enough for the
within-person estimation the appendix itself performs on the internal sample (p.22) but not on the
public one.

**What the classifier sees.** Every classifier call is shown the transcript — human, assistant and
system turns — with each turn middle-truncated at 5,000 characters and the whole transcript
truncated at 25,000 characters (p.2). Almost every classifier is a single Sonnet 4.6 call at
temperature 0.2 with forced choice among the listed options (p.2). The truncation appears nowhere in
the parent paper and is the appendix's most consequential undisclosed-until-now constraint: the
population being measured includes sessions of "hundreds of turns" and "hours (or even days) of
work" (p.22), and the classifier sees 25,000 characters of them. The outcome classifier is
instructed to judge truncated sessions anyway, from "the visible head + tail" or, failing that, from
trajectory (pp.12–13).

**The eight classifiers.** Where the parent paper describes six, the appendix prints eight: work
mode (nine forced-choice verbs, no abstention); user expertise (1–5 plus Unclear); occupation (user
profile) (23 SOC major groups plus Unclear); occupation (work performed) (the same 23 groups, no
Unclear); session outcome (Succeeded / Partially Succeeded / Failed / No clear goal); success signal
(NONE, 1–5); failure signal (NONE, 1–5); and the two-call task-value estimator. Decision attribution
— one of the parent paper's headline constructs, and the subject of Figure A2 — has **no prompt
printed in the appendix**; it is validated (pp.21–22) but not defined here. The codebase-relationship
classifier behind the parent paper's PDF-only 48/17/14 split also has no prompt here, though the
work-mode prompt references a `codebase_context = 'Not in a codebase'` field (p.3), which implies
such a classifier exists.

**Two occupation measures, and what they are each used for.** The user-profile classifier asks what
the person does for a living, from side signals only, with an explicit instruction that coding is not
evidence of a coding job; it may answer Unclear, and about 30% of sessions do (pp.7–10, p.21). The
work-performed classifier asks which occupation's workers would typically do the session's work, has
no Unclear option, and is forced to answer on thin evidence (pp.10–11). Table A1 uses both: the
work-performed measure as "Task-occupation FE" (column 4) and the user-profile measure as
"User-occupation FE" (column 5) (p.25). This resolves an ambiguity in the parent paper, whose Figure
5 caption speaks of comparing sessions "on the same task subject" — the subject is a second SOC
classification of the work, not a topic taxonomy.

**Measure construction.** Verified success = judged Succeeded and success signal in {4,5}; hits
trouble = failure signal ≥ 3; abandoned = judged Failed and zero lines of code added; wrote code = at
least one line added (pp.20–21). Three of these four thus combine a transcript judgment with either a
second transcript judgment or telemetry; none rests on telemetry alone. Note the construction that
follows from the scale definitions: success signal 2 is described as "the modal short CC session"
(p.15), and verified success requires 4 or 5, so the modal session cannot be a verified success by
construction — which is the mechanical reason verified success rates sit near 30% while "at least
partial success" sits above 90% in the parent paper.

**The task-value estimator, end to end.** Call 1 (Haiku 4.5) rewrites the transcript as an
Upwork-style job posting in a fixed JSON schema, instructed not to mention Claude or AI (p.18). Call
2 (Opus 4.7) prices that posting against 200 real postings with known prices, tier-balanced across
four price bands, drawn from an unnamed public postings dataset covering 2024–2026 and filtered to
fixed-price listings between $10 and $50,000 with descriptions of at least 50 characters — about
23,000 postings survive (p.18). Validation is on a 999-posting stratified holdout from the same
filtered corpus, 250 per tier, with 1,000-draw bootstrap intervals (p.18). The headline is log R² =
0.38, but the appendix decomposes it: within-tier discrimination is 0.16 at the bottom and 0.01 at
the top, so the headline is largely cross-tier ordering, and bias reverses from 2.4× over-pricing at
the bottom to about 7× under-pricing at the top (p.19). The calibration set was chosen by grid search
over two models and two weightings on the same holdout (p.20). The appendix's own instruction
follows: "we generally use these task value estimates ordinally rather than using them to get
aggregate task values" (p.19).

**The regressions.** OLS linear-probability models of verified success on the 1–5 expertise scale,
with standard errors clustered by user, adding fixed effects cumulatively: work mode × task-value
band; month; task-occupation; user-occupation; model-tier × session-length band together with
ln(model calls) and ln(human turns) (Table A1, p.25). Column 5 is the stated preferred
specification. Sessions with no clear goal are excluded. R² rises from 0.009 to 0.136 across the six
columns; the expertise coefficient moves from +0.0426 to +0.0379 in the preferred column and +0.0364
in the most saturated one, with standard errors of 0.0008–0.0009 throughout. Table A2 replaces the
linear scale with level indicators under the column-5 fixed effects and publishes, for the first time
in the release, both the unadjusted and the adjusted success rate at each level together with the
cell sizes (p.27).

**Validation, in four pieces.** (i) Internal consistency: the two signal classifiers track the
independent outcome judgment monotonically across their five levels, 13%→90% and 85%→3% (Figure A1,
p.21) — three classifiers reading the same transcript. (ii) Convergence with telemetry: planning
share tracks model calls and tool calls per human prompt; execution share does not (Figure A2,
pp.21–22). (iii) Internal outcome validation: the same prompts run on internal Anthropic sessions,
where session IDs join to whether the session's commits landed on main; the gradient replicates,
including within-engineer with author fixed effects, at roughly 3–5 pp of judged success per
expertise level (p.22). This is the only place in the whole release with person fixed effects and the
only place with an outcome observed outside the transcript. (iv) Strong-model agreement: the
report's classifiers and a reference model (Mythos Preview) both label 198 SWE-chat sessions;
disagreements are adjudicated blind by the reference model and the concerning ones re-adjudicated
blind by an author; agreement is 78–98% on categorical classifiers, 78–99% adjacent and 53–68% exact
on ordinal ones, with concerning disagreements at 0–3% per classifier and a human concurring with
the judge on 11 of 15 (pp.22–23). The appendix explains why it abandoned human ground truth: "It is
not clear that humans, with their limited working memory and limited understanding of unfamiliar
codebases and agentic tool traces, can label sessions more consistently than a powerful model"
(p.23).

**What is not in the appendix at all.** No standard errors or intervals for any figure or any
validation number outside Tables A1 and A2 and the two pricing tables. No sample sizes for Figure A1
beyond the "398K sessions" in its plot title, and none for Figure A2 or the internal-validation
sample. No aggregation-threshold value. No count or share for any of the four exclusions it defines
(headless sessions, internal Anthropic usage, Unclear expertise, no-clear-goal sessions) except
Unclear occupation at "about 30%". No prompt for the decision-attribution classifier. No released
data, no code and no replication package; the appendix links nothing.

## Limitations (verbatim)

The appendix carries no section, heading or paragraph headed "Limitations", and no sentence in it is
framed as a limitation of the parent paper. What follows is the whole of what it says that bears on
the scope, reliability or interpretation of its own numbers, quoted in full. Nothing has been added
or paraphrased, and no candidate passage has been left out.

**On the task-value estimator**

> "Note that the overall 0.38 largely reflects cross-tier ordering—because the holdout weights all
> four tiers equally, the pricer earns credit for placing $50 jobs below $8,000 jobs even where it
> cannot rank jobs within a tier. Within-tier discrimination is concentrated at the low end and is
> essentially zero above $5,000." (p.19)

> "Note also that bias reverses across the range. Small jobs are over-priced about 2.4x, the largest
> under-priced about 7x. So, we generally use these task value estimates ordinally rather than using
> them to get aggregate task values." (p.19)

> "With a uniformly weighted draw, the pricer anchors to the small-job range and compresses
> everything above it: on the validation holdout it under-priced $5,000+ jobs by roughly 12x (median
> prediction $800)." (p.19)

> "Since the report uses the estimates comparatively rather than as dollar levels, we took the
> variant with the best overall ranking and the least price-dependent distortion." (pp.19–20)

> "Holdout accuracy for this task is model-dependent, so the cited validation numbers are specific to
> the exact model and prompt the pipeline runs." (p.20)

**On classifier validation**

> "It is challenging to validate classifiers on Claude Code sessions—a single session can span
> hundreds of turns, files, and tool calls, and hours (or even days) of work." (p.22)

> "But the length and complexity of Claude Code sessions call into question whether such an approach
> is feasible and reliable. It is not clear that humans, with their limited working memory and
> limited understanding of unfamiliar codebases and agentic tool traces, can label sessions more
> consistently than a powerful model." (pp.22–23)

> "Taken together, the results of our validation are encouraging. They do caution against over-reading
> any particular label, but most of the report's conclusions rest on relative comparisons, i.e.,
> differences between groups and changes over time, and on those, the classifier is more reliable. As
> long as the classifier's mistakes are similar across groups (which we did not extensively verify
> here), those mistakes cancel each other out when making comparisons." (p.23)

> "This validation approach is far from perfect, but we do think it is promising to use a strong
> reference model alongside blind adjudication of disagreements, with human review reserved for
> spot-checking the judge's calls (less as ground truth and more as a way for the authors to build
> intuition for what the disagreements actually look like)." (pp.23–24)

**On the sample and the estimation samples**

> "Sessions whose user profile is Unclear are excluded from occupation analyses (about 30% of
> sessions)." (p.21)

> "375,687 sessions, columns (4)-(6) have fewer due to cells that fell under the aggregation limit."
> (Table A1 caption, p.25)

> "Excludes sessions with no clear goal." (Table A1 caption, p.25; Table A2 caption, p.27)

> "every number in this report is an aggregate over a cell of sessions that is suppressed unless it
> contains a minimum number of distinct users" (p.2)

> "For each classifier call, the model is shown the session transcript (human, assistant, and system
> turns) with each turn middle-truncated at 5,000 characters and the transcript as a whole truncated
> at 25,000 characters." (p.2)

**On the measures' own scales**

> "Table A1 assumes that expertise is a linear scale, i.e., that each step of the expertise scale is
> worth the same." (p.25)

> "DO NOT confuse 'the agent worked competently' with 'success was verified'. The agent can write
> clean code that does the wrong thing — that is at most a 2 or 3. A high score here just means strong
> EVIDENCE on the success side." (p.15)

## Open questions, conjectures and promised follow-ups (verbatim)

The appendix contains exactly one forward-looking passage and one invitation to the field. There is
no sentence in the fetched text of either copy containing "future work", "further research", "more
research", "we plan", "we hope", "remains an open question", "we do not know", or "leave for". The
whole of what there is:

**A promised follow-up, and a named gap in the present work**

> "We are actively developing methods of validation that take seriously that human labels may no
> longer be the gold standard for complex sessions and also that some human review may still be
> valuable for interpretation." (p.24)

> "As long as the classifier's mistakes are similar across groups (which we did not extensively
> verify here), those mistakes cancel each other out when making comparisons." (p.23) — the parenthesis
> is the appendix's own statement of an unperformed check on which its comparative results depend.

**An invitation to the research community**

> "We encourage others in the research community to take up this methodological challenge alongside
> us." (p.24)

**A methodological conjecture**

> "This validation approach is far from perfect, but we do think it is promising to use a strong
> reference model alongside blind adjudication of disagreements, with human review reserved for
> spot-checking the judge's calls (less as ground truth and more as a way for the authors to build
> intuition for what the disagreements actually look like)." (pp.23–24)

**A treatment adopted as an assumption, stated as such**

> "We then used a strong reference model (Mythos Preview) to label the same sessions, treating the
> reference model labels as reliable and consistent proxies for ground-truth." (p.23)

Nothing else in this section: the appendix names no other conjecture and promises no other
follow-up. The parent paper's forward agenda — the falling-returns-to-expertise test, the promise to
develop a framework for non-interactive usage — is in
`wiki/reports/claude-code-expertise-2026-06.md`, not here, and ledger entries for it should be taken
from there.

## What it did not test

*This section is the wiki author's inference, not the appendix's own text.* Each item is something
the appendix's own material makes checkable and that it did not check, or a construct it prints and
does not validate. Items the parent paper leaves open and the appendix answers are not repeated here
(they are marked in `## Claims`); this is the residue after reading both documents.

**The dependence between the expertise rating and the outcome measures — still the central untested
threat, now narrowed.** The appendix does three things the parent paper did not: it instructs the
expertise classifier not to rate on Claude's performance (p.5), it runs the classifiers as separate
single calls so that no one call sees another's answer (p.2), and it replicates the gradient
within-engineer against commits landing on main (p.22). What it still does not do is break the shared
input. All eight classifiers read the same truncated transcript; the expertise definitions at levels
1 and 5 are written in terms of who corrects whom (pp.6–7), and the failure-signal definitions are
written in terms of errors, push-back and looping (pp.16–17). The one decisive test remains
unavailable from the published material and unrun: rate expertise from the first prompt or first turn
alone, before any outcome is observable, and re-estimate Table A1. The internal validation goes
furthest — a landed commit is not a classifier output — but its result is reported as a one-sentence
range (3–5 pp per level, on judged success) with no table, no n, no standard error, and on a sample
of Anthropic engineers that is the least representative population available.

**The internal validation is reported too thinly to bear the weight put on it.** It is the only
person-fixed-effects estimate and the only external-outcome check in the release, and it is given
six lines of prose (p.22). Not reported: the number of internal sessions or engineers; the standard
error on the 3–5 pp; whether the range is across specifications or across levels; the verified-success
version of the same regression, which would be directly comparable with Table A1's +0.0379; the rate
at which commits land, by expertise level, as a level rather than a direction; and whether the
expertise *distribution* among Anthropic engineers overlaps the public sample's at all. Given that
this one paragraph is the closest thing in the release to a causal design, its under-reporting is the
single largest gap in the appendix.

**Truncation is never tested as a source of bias.** Turn-level truncation at 5,000 characters and
transcript-level truncation at 25,000 characters (p.2) bind hardest on exactly the sessions the
paper's story is about — long, agentic, expert-led sessions, which Figure 3 of the parent paper shows
carry five times the output words of novice sessions. So the classifier sees proportionally less of an
expert session than of a novice one. The appendix does not report what share of sessions were
truncated at all, does not report the truncated share by expertise level or work mode, and does not
re-run any classifier at a larger window on a subsample to bound the effect. The outcome prompt's
truncation instruction (pp.12–13) tells the model how to behave when truncated but supplies no
estimate of how often it does.

**The four exclusions are defined and never counted.** Sessions with zero human turns (p.2), internal
Anthropic usage (p.2), Unclear-expertise sessions (p.5), and no-clear-goal sessions (Table A1 and A2
captions) are each removed by rule. Only one exclusion in the document carries a share — Unclear
occupation, "about 30%" (p.21). In particular the Unclear expertise share is never published, and
Table A2's levels 1–5 account for the whole column-(1) sample, so Unclear-rated sessions sit outside
every regression without ever being sized. No characterisation of any excluded group, and no bounding
exercise, is offered.

**The two occupation classifiers are never compared with each other.** The appendix prints a
user-profile classifier and a work-performed classifier over the same 23 groups, and uses both as
fixed effects in the same regression (p.25). The cross-tabulation of the two — how often a lawyer's
session is doing software work, how often a software professional's session is doing something else
— is the natural descriptive output of having built both, is immediately available, and appears
nowhere. It is also the measure that would let a reader judge the parent paper's claim that coding
agents make a coding background less relevant.

**The decision-attribution classifier is validated but not defined.** Figure A2 validates it against
telemetry (pp.21–22) and the parent paper builds its headline 70/20 division-of-labour claim on it,
yet the appendix prints no prompt for it — the only construct in the release for which the promise
"including their exact full text" (parent paper, footnote 5) is not kept. Nor is there a prompt for
the codebase-relationship classifier behind the parent's PDF-only 48/17/14 split, although the
work-mode prompt refers to a `codebase_context` field (p.3).

**The task-value estimator's stability over time is never checked — and this is the one that matters
most.** The appendix establishes that the estimator's bias is strongly price-dependent (2.4× over at
the bottom, ~7× under at the top, p.19) and that within-tier discrimination above $5,000 is
essentially zero. The parent paper's "+27% over seven months" is a comparison of estimates across
time. If the mix of sessions drifted up the price range over those seven months — which is precisely
what the paper claims happened — then the measured rise is partly the estimator's own bias gradient
being traversed, not a change in value. The appendix does not report the estimator's performance by
month, does not re-run the holdout with the calibration sample drawn from a different period, and
does not show the task-value trend under an alternative calibration variant even though it has three
alternatives already estimated on the holdout (p.20). The 12× and 7× figures make this a
first-order, not a second-order, concern.

**The holdout is a posting-pricing holdout, not a session-pricing holdout.** Everything on pp.18–20
validates call 2 — can Opus price a job posting whose true price is known. Nothing validates call 1,
the Haiku rewrite of a Claude Code session into a posting, which is where the "ultimately fuzzy
match" the parent paper concedes (footnote 8) actually happens. No human or reference-model check on
whether the generated postings faithfully describe the sessions; no test of rewrite stability across
runs at temperature; no check of whether the rewrite's length or specificity correlates with session
length, which would import a session-length gradient straight into the price.

**The strong-model agreement study reports only ranges.** Agreement is given as 78–98% categorical,
78–99% adjacent and 53–68% exact (p.23), with no per-classifier table. Since the classifiers do very
different work — a nine-way forced choice, a 1–5 rating, a 23-way occupation guess — a reader cannot
tell whether the expertise rating, on which the paper's central claim rests, sits at the top or the
bottom of those ranges. 198 sessions is also small enough that a per-classifier confidence interval
would be wide, and none is given. Further: SWE-chat is a public-repository, multi-harness dataset,
not Claude Code traffic, so the agreement study is run on a different population from the
measurement sample, and no test of that difference is offered.

**The reference-model design has an unexamined circularity.** The reference model labels the
sessions, and the same reference model then adjudicates blind the disagreements between itself and
the report's classifier (p.23). The appendix notes the human re-adjudication step but does not
report the obvious check — what a second, different reference model would conclude, or how often the
judge sided with its own earlier labels versus the report's classifier. "concurred with the judge in 11 of
15 sessions" (p.23) means a human disagreed with the adjudicator in 4 of 15, which is not discussed.

**Figure A1 is internal consistency and is not distinguished from validation.** Three classifiers
reading the same transcript agreeing with each other is a coherence check; the body text calls the
outcome judgment "independent" (p.21) and the plot title calls the exercise "internal consistency"
(p.21). No statistic is offered that would separate genuine convergent validity from shared
transcript-reading error, and the obvious available comparison — success signal against the
telemetry the appendix already has (lines added, successful tool calls) rather than against another
classifier — is not shown, even though lines added is used in the definition of "abandoned".

**Figure A2's near-orthogonality result is asserted, not measured.** "Execution share is
near-orthogonal to these" (p.22) carries no correlation coefficient, no regression and no interval;
the figure has no printed data labels. Since execution share is the half of the decision measure that
the parent paper uses for its most-quoted number (Claude makes ~80% of execution decisions), a
finding that it does not move with observable agent activity deserves a statistic.

**Nothing in the appendix tests the classifiers for drift across the seven months.** Sessions span
October 2025 to April 2026 and the model used to classify them is fixed (Sonnet 4.6 at temperature
0.2). The appendix does not report classification stability by month, nor re-run any classifier on a
sample from each month, nor test whether the changing model mix within the sessions themselves
(which Table A1 column 6 controls for) changes how transcripts read to the classifier. Every
over-time claim in the parent paper depends on the classifier behaving identically on an October
transcript and an April one.

**Temperature 0.2 is not zero, and no re-run variance is reported.** Every classification is a single
call at temperature 0.2 (p.2). No test-retest exercise is reported for any classifier — not even on
the 198 SWE-chat sessions where re-running was already part of the design. The intra-classifier
variance is therefore unknown and is not propagated into any standard error, including Table A1's,
which treats the classifier output as measured without error.

**Table A1's specification questions.** The outcome is binary and estimated by OLS with fixed
effects; no logit or marginal-effects comparison is shown. The preferred column (5) is chosen by
argument rather than by a test. Sessions drop from 359,586 to 302,647 as fixed effects are added
(p.25) and the changing sample is never held constant, so the coefficient movement from +0.0442 to
+0.0364 mixes added controls with a changing estimation sample — a fixed-sample version across all
six columns is the standard robustness table and is not shown. Clustering is by user throughout, with
no alternative (two-way by user and month, say) reported.

**The published sample-size inconsistency is not reconciled.** Table A1's caption says 375,687
sessions while its own Sessions row reads 359,586 in columns (1)–(3) (p.25). Neither the appendix nor
the parent paper reconciles them or issues an erratum.

**The level R² column is internally contradictory and is left standing.** The p.19 table prints log
R² and level R² as identical in all five rows, which contradicts the definition on p.18; and the
p.20 grid gives the shipped configuration a level R² of 0.09 against p.19's 0.38. No erratum, no
footnote.

**Two classifier glosses have their success and failure conditions transposed.** The success-signal
gloss says it returns "None" when there are no observable *failure* signals (p.14); the failure-signal
gloss says it returns "None" when there are no observable *success* signals (p.16). Both contradict
the prompts printed immediately beneath them. The error is presentational rather than
methodological — the prompts are what ran — but it is uncorrected in both copies, and it is the kind
of thing a reader building on these definitions must not copy.

**The blank page.** p.26 is blank apart from the running footer, between the Table A1 section and
Table A2. Nothing in the document refers to missing content there, and the two copies are identical
on it, so it is most likely a layout artefact rather than a dropped exhibit — but a reader cannot
verify that from the document.

## Verification

**Fetch record — 2026-09-16.**

| URL | Method | Result |
|---|---|---|
| https://cdn.sanity.io/files/4zrzovbb/website/a94728142a45694292336165947f8d6e3e1a357e.pdf | `curl` to `/tmp/cce-app.pdf` | HTTP 200, 560,586 bytes, 27 pages. ETag / `x-sanity-md5` `0465f720af321f07e8ba81f3beb12675`; `content-disposition: inline;filename="CCEconReport-Appendix-I.pdf"`; `last-modified: Mon, 22 Jun 2026 21:47:00 GMT`; PDF `/CreationDate D:20260622174509-04'00'`, Adobe InDesign 21.4 (Macintosh), Adobe PDF Library 18.0. Called **copy I** above; this is the URL in `wiki/INDEX.md`. |
| https://cdn.sanity.io/files/4zrzovbb/website/7426c33b0e75ab4771c465d30d5bc1019bdd0c9c.pdf | `curl` to `/tmp/cce-app-H.pdf` | HTTP 200, 560,584 bytes, 27 pages. `content-disposition: inline;filename="CCEconReport-Appendix-H.pdf"`; `last-modified: Mon, 22 Jun 2026 21:41:30 GMT`; PDF `/CreationDate D:20260622173917-04'00'`. Called **copy H** above. |
| https://www.anthropic.com/research/claude-code-expertise | `curl` to `/tmp/cce.html` | HTTP 200. Fetched only to establish which appendix URLs the parent page links and how many times, and to confirm the parent paper's figure numbering for the cross-reference note in Claim 38. The parent paper itself is covered by `wiki/reports/claude-code-expertise-2026-06.md`, not here. |

`web_fetch` was not attempted on the Sanity CDN URLs: the note in
`wiki/reports/claude-code-expertise-2026-06.md` records that the fetch service refuses them with
`url_not_allowed`, and `room/director-2026-09-16-session-1-2-kickoff.md` directs the use of `curl`
and a PDF-to-text tool. The parent page was fetched with `curl` for the same reason of consistency.

**How the document was read.** Both copies in full, twice over. (i) Text layer: `pdftotext -layout`
page by page, all 27 pages of both copies. (ii) Visually: pages rendered with `pdftoppm` at 100 dpi
(both copies, for the comparison below) and at 200 dpi (copy I, pp.18–22 and pp.25–27) for the
tables and figures, which have no text layer.

**Which copy governs.** Copy I on every available signal: PDF creation timestamp 2026-06-22 17:45
(−04:00) against copy H's 17:39, CDN `last-modified` 21:47:00 GMT against 21:41:30 GMT, and the
parent page carries six rendered links to copy I against one to copy H — and that one is the stray
link on a trailing full stop. Copy I is also the URL in
`wiki/INDEX.md`, so no re-pointing is needed. Both remain live.

**Differences between the two copies — one character.** A `diff` of the two `pdftotext -layout`
outputs returns exactly one differing line, on p.2: copy H reads "All classifications ran through our
privacy-preserving analysis infrastructure.." (doubled full stop) and copy I reads "…analysis
infrastructure." A pixel-level comparison of the two renderings at 100 dpi returns *identical* for
pp.19, 20, 21, 22, 25 and 27 — the six pages carrying the four tables and the two figures — so no
table value, figure, caption or axis label differs between the copies. The CDN filenames differ
(`…-Appendix-I.pdf` / `…-Appendix-H.pdf`); both documents are the same 27-page appendix, and neither
contains a volume label, version number, revision date or errata note.

**Quotation check.** Every quotation in `## Definitions (verbatim)`, `## Limitations (verbatim)` and
`## Open questions, conjectures and promised follow-ups (verbatim)`, and every quoted fragment in
`## Claims`, `## Source` and `## Data and methods`, was checked mechanically against the `pdftotext
-layout` text layer of copy I and then of copy H, comparing with all whitespace removed and
typographic quotation marks folded to ASCII — whitespace-insensitively, because the PDF's line
breaking splits words at hyphens and em dashes and would otherwise produce false failures. 118 block
quotations were checked this way; all 118 matched copy I and 117 matched copy H, the exception being
the p.2 privacy sentence whose doubled full stop is the copies' only difference and which is flagged
at the point of use. Every inline quoted fragment was checked the same way; the fragments that do not
appear in this appendix's text layer are, in every case, one of four things, each marked as such
where it occurs: a quotation from the parent paper, a value or label read from a rasterised table or
figure (see below), an HTTP header value, or a phrase quoted in order to say that it is *absent*
from the appendix.

Reproduced as printed: Anthropic's curly single and double quotation marks, the em dashes, the `→`
arrow in the expertise level-5 definition and in the outcome prompt, the superscript ² in "log R²",
the `**` markers that appear as literal characters in the classifier prompt text, the `1-5`
hyphenation, the en dashes in the price tiers (`$10–200`), and three source errors, each marked
*[sic]* or noted at the point of use: "a public job-postings datasets", and the two transposed
success/failure glosses on pp.14 and 16. Three editorial changes inside quotations, all mechanical
and all disclosed in `## Definitions (verbatim)`: the PDF's typographic bullets are rendered as `•`
where the source uses a bullet and as `-` where it uses a hyphen; words the PDF's line-breaking
splits across lines at a hyphen or underscore are rejoined ("non-interactive",
"audit-for-understanding", "econ_analysis.py", "name-dropping", "many-shot", "non-obvious"), each
confirmed against the rendered page image rather than assumed from the text layer; and the bolded
run-in heads on pp.20–21 are named outside their quotations rather than reproduced inside them.

**Two quotations span a page break in reading order but not in the text layer**, because the PDF
places an exhibit between their halves: the decision-attribution sentence (pp.21–22, interrupted by
Figure A1 and its caption) and the column-by-column sentence in the Table A1 section (pp.24–25,
interrupted by Table A1 and its caption). Each half was matched separately against the text layer
and the join confirmed against the 200 dpi renderings of pp.21–22 and pp.24–25.

**Absence checks.** The statement opening `## Limitations (verbatim)` that the appendix has no
section or sentence framed as a limitation, and the statement opening `## Open questions…` about its
forward-looking vocabulary, were tested case-insensitively against the whole text layer. None of the
following appears anywhere in the 27 pages: "limitation", "future work", "further research", "more
research", "we plan", "we hope", "open question", "we do not know", "leave for", "caveat", "we
cannot", "next step".

**Table and figure values.** Tables A1 and A2 and the two unnumbered pricing tables are rasterised in
the PDF — the pages carry no text layer for the grids themselves, though the captions beneath them do
have one and were verified against it like any other quotation. Their cell values and row labels, as
recorded in Claims 22, 25, 35 and 36, were read from 200 dpi renderings of copy I and confirmed
against copy H by the pixel-identity check above. They are printed text, not chart readings, and are
recorded as published values. The same applies to text drawn *inside* the two figure images — plot
titles, panel titles, legend entries and axis titles — which likewise have no text layer, were read
from the 200 dpi renderings, and are marked "(p.N, plot title…)" or "(figure labels, p.N)" where they
occur.
Figures A1 and A2 carry **no printed data labels**. Per
`room/director-2026-09-16-figure-values-ruling.md`, no value is read off their axes and none is
recorded here; the five values per panel in Figure A1 are recorded only because the body text on p.21
states them in prose, and Figure A2's values are not recorded at all.

**Cross-checks against the parent paper.** The parent paper's entry
(`wiki/reports/claude-code-expertise-2026-06.md`) was read but not re-fetched; where this file says
the appendix settles, extends or contradicts the parent (Claims 1, 4, 5, 6, 11, 14, 19, 27, 29, 38),
the parent's wording was taken from that entry's verbatim sections and the parent page was
re-fetched today only to confirm its figure numbering. No number in this file is sourced from the
parent paper.

**Not attempted.** The parent paper's own PDF (`433472e3…`, 18 pp) was not re-fetched; it belongs to
`claude-code-expertise-2026-06`. The SWE-chat dataset card, the unnamed public freelance-postings
dataset, and the "Mythos Preview" reference model were not looked up; none is a source for anything
in this file, and the appendix names no URL for any of them. `data/` was not opened and no arithmetic
was performed on any released file; the one arithmetic statement in this file (Claim 39) is a
consistency check on two values printed in the appendix's own tables and is marked as the wiki
author's, not the appendix's.
