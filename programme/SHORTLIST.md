# Short-list — scoring and sketches

Session 1.3, Step 2. Owner: programme lead. Input: the 39 surviving candidates in
`programme/LONGLIST.md` at commit `2eff78a`, each carrying a steward feasibility line verbatim.
Nothing here changes any surviving entry's question or contribution; where scoring exposed a defect it
is named in that candidate's rationale and left for the referee (director's Step 2 instruction).

## 1. The rubric, fixed before scoring

Six dimensions, each 1–5, anchors below. **Aggregation: unweighted sum**, maximum 30. Unweighted is
chosen deliberately: any weighting would embed a judgement about what this programme is for that the
referee cannot audit from the file, whereas an unweighted sum lets a reader re-derive the ranking
from the six columns and disagree about one column at a time. Weighting was considered and rejected
for that reason.

**Stated tie-break order**, applied before any diversity consideration: (1) *What it teaches*,
(2) *Feasibility*, (3) *Foundation in usage data*. Only if all three tie may the diversity
tie-breaker be used, and only within two points of the cut line, and every use is written down in
§4.

### ORG — originality against the corpus
- **5** The question is asked nowhere in the corpus and nowhere in the external literature checked, and the measure it needs does not yet exist in either.
- **4** The corpus poses it and leaves it open; no external work does it on comparable data.
- **3** An Anthropic publication or an external work does something adjacent on different data or a different platform.
- **2** A close external analogue exists on comparable data; our version is a variation.
- **1** Substantially done somewhere already.

### FIT — fit with the threads map and the mentor's stated interests
- **5** Sits on a thread the stream is actively pursuing **and** on a quoted ⟨mentor⟩ passage in one of his own Anthropic publications.
- **4** Active thread, with a mentor passage that is adjacent rather than central.
- **3** Active thread, mentor interests "none".
- **2** A quiet corner of a thread.
- **1** Off the map.

### FOUND — foundation in usage data
- **5** Stands entirely on the Economic Index releases; no external series needed.
- **4** Index releases plus a reference file shipped **inside** a release (population, GDP, O\*NET, wages).
- **3** Index releases plus one external series, with the Index carrying the comparison.
- **2** Index plus several externals, or an external series carries the comparison.
- **1** The Index is decoration.

### FEAS — feasibility, read off the steward's line
- **5** FEASIBLE, with a generous unit count and no convention in doubt.
- **4** FEASIBLE with a modest unit count, or FEASIBLE-WITH-CAVEAT where the caveat does not touch the test.
- **3** WITH CAVEAT that constrains the design but leaves the test intact.
- **2** WITH CAVEAT that bites power, resolution or interpretability.
- **1** WITH CAVEAT that removes the test (nothing scored 1 survives; LL-34 was deleted at this point).

### TEACH — what an Institute economist learns, either way
- **5** Moves a published Anthropic number or a load-bearing construct in either direction, and changes a decision, a model input or a measurement practice.
- **4** Bounds a load-bearing construct, or supplies a measure the stream says it needs.
- **3** Adds a measurement the corpus lacks, without moving a published number.
- **2** Adds detail to something already understood.
- **1** Internal interest only.

### RISK — inverted, so lower risk scores higher
- **5** The main risk is data-shaped and the steward has already measured or bounded it.
- **4** Risk named and bounded; the post survives it intact.
- **3** Risk material; mitigation pre-registered and sufficient.
- **2** Risk could turn the post into an awkward null, or shift its object mid-flight.
- **1** Risk could invalidate the design.

## 2. Scores, all 39 survivors

Columns: ORG · FIT · FOUND · FEAS · TEACH · RISK · **Σ** (max 30). Rationale names the decisive
dimension.

| ID | question (short) | ORG | FIT | FOUND | FEAS | TEACH | RISK | Σ | decisive dimension, and why |
|---|---|---|---|---|---|---|---|---|---|
| LL-07 | Is AI delegated more on cheap or expensive work? | 5 | 5 | 4 | 5 | 5 | 4 | **28** | FEAS+RISK: the ledger says the wage × collaboration cross is published nowhere, and the steward found 99% wage coverage over three waves with the multi-holder worry bounded at ≤0.17 pp. Nothing else scores this well on both feasibility and stakes. |
| LL-11 | Do tasks growing on the API shrink on the consumer surface? | 5 | 5 | 5 | 5 | 5 | 2 | **27 (ref.)** | FIT: it is the mentor's own stated leading indicator, asserted in two reports and measured nowhere, and 1,241 tasks appear in all six frames. Risk is the share-versus-level accounting. |
| LL-09 | Does measured success predict what people keep bringing to AI? | 5 | 4 | 5 | 4 | 5 | 2 | **25 (ref.)** | TEACH: Anthropic named prediction as the validation that counts for its primitives and never ran it; a 2,427-task panel carrying 92% of mass makes it runnable. |
| LL-31 | Does what people take away from AI depend on where they are? | 5 | 4 | 4 | 5 | 4 | 3 | **25 (ref.)** | ORG+FEAS: no other provider publishes an artifact taxonomy, the sixth report declined its own cut, and 114 countries plus 536 subregions carry all 32 metrics in both months. |
| LL-36 | Is coding still the leading edge of AI use, or just its largest share? | 4 | 5 | 4 | 5 | 4 | 4 | **26 (ref.)** | FEAS: the reconstruction reproduces the published facet to 0.02 pp and both published bases come out, so the corpus's most-quoted series can be decomposed with the base named. |
| LL-01 | Do places using AI more use it more autonomously, or is that income? | 1 | 5 | 5 | 4 | 2 | 3 | **20 (ref.)** | **ORG (ref. 5 → 1): out as an inherited framing.** The referee found that `reference/posts/post1` ran this exact test on this wave — the AUI on the task-mix residual with log GDP, reporting 0.10 (−0.76, 0.97) in the full model and 0.39 (−0.20, 0.98) with income alone, and reproducing Fig 2.11 on five waves — and that `economic-index-2026-01-report` App. Fig 10 also went unmentioned. The "first test" language in my entry was false as written. Director's ruling 1: out, not re-sketched. |
| LL-22 | How much of a month's local AI-use pattern is real? | 2 | 4 | 5 | 3 | 3 | 4 | **21 (ref.)** | **ORG (ref. 5 → 2): out as an inherited framing.** The referee found that `reference/posts/post2` H1 is this question on this wave (45% April→May recurrence, r = 0.62, the small-state reading and the two-window reporting rule), that post2's brief announced a companion post doing the same for countries, and that both legs' key numbers already sit in the atlas at log (f) 8. Director's ruling 1: out, not re-sketched. |
| LL-39 | When the ruler changed, did AI use change with it? | 5 | 4 | 5 | 4 | 3 | 2 | **23 (ref.)** | TEACH: the appendix's own load-bearing omission, and the steward supplied a three-tier list of which metrics cross the June boundary, which is the post's spine. |
| LL-02 | Does observed use support the automation share the scenario model assumes? | 3 | 4 | 5 | 4 | 3 | 3 | **22 (ref.)** | **ORG and TEACH (ref. 4 → 3, 5 → 3): out on score after the permitted rewrite.** Correction 9 applied: the closest existing answer is **not** that nobody has put the two numbers on one page — `econ-scenarios-paper-2026-09` pp.27–28 already does so in prose ("about half … Claude.ai … about three quarters … on the API. So 0.5 describes chat use today"), its Table 2 compares a survey-implied ψ of 0.47 against the presets, and the answer columns of `L-2026-09-SCPA-24` and `L-2026-09-SCEX-25` already carry the steward's observed maximum of 0.511. What would remain is a decision rule for 0.511 against a preset of 0.50 and a statement of the Claude.ai June break, which is a paragraph, not a post. Rewritten once and re-scored honestly at 22; leaves on score, per director's ruling 2. |
| LL-18 | Where is AI doing work people could not do alone? | 5 | 4 | 4 | 5 | 4 | 3 | **25** | ORG: the corpus's one substitution primitive, measured at three grains and used in nothing; 115 countries clear the floor in both waves. |
| LL-12 | Is AI use getting broader, or is the same work recurring? | 4 | 4 | 4 | 5 | 4 | 4 | **25** | FEAS: identical privacy floors and denominators within 3.7% make the three long waves like-for-like, so the first paper's fork can be scored without the cumulative artefact. |
| LL-16 | Does AI's own description of requests match the taxonomy used to measure it? | 5 | 4 | 4 | 4 | 4 | 3 | **24 (ref.)** | ORG: an 18-month-old promised comparison that only Anthropic's file enables; the steward settled the flag and measured the gap (49.2% of v2 mass reached). |
| LL-20 | Does AI work less well where it is used most? | 4 | 4 | 4 | 5 | 4 | 3 | **24** | FEAS: success exists at country grain in both waves for 115 countries; the 21–27% `not_classified` share is the thing that could drive the gradient. |
| LL-24 | Do retraining programmes train people for the work AI already does? | 5 | 5 | 3 | 3 | 5 | 3 | **24** | FIT+TEACH: the mentor's own review never asks it and the $200M Fund's Priority 2 turns on it; FOUND and FEAS are held down by a hand-coded destination list against a 54%-zero distribution. |
| LL-30 | Is the work AI does for work the same work it does for study? | 5 | 4 | 4 | 3 | 5 | 3 | **24** | TEACH: every occupational claim rests on a corpus more than half of which is not work, and the work-only occupational mix is published nowhere; the cut is global-only. |
| LL-33 | What is the tenth of enterprise AI use that is neither delegated nor collaborative? | 4 | 4 | 5 | 4 | 4 | 3 | **24** | TEACH: the API residual runs 10.21 → 11.04 → 15.19, the same order as the automation fall the fifth report reports, which matters to every external user of that ratio. |
| LL-37 | What would an early-warning signal built on usage data fire on? | 5 | 5 | 4 | 3 | 3 | 2 | **22 (ref.)** | RISK is the binding column: the Institute's most repeated promise, but no outcome series ships, so predictive validity is unreachable and the post can only measure persistence. |
| LL-41 | Does the threshold behind the published productivity number survive being moved? | 4 | 4 | 5 | 4 | 4 | 3 | **24** | TEACH: the steward's sweep already shows near-invariance (11.93× → 11.59×), which relocates the published 1.8pp → ~5pp swing to the weighting step — a finding, but a narrower one than the entry first supposed. |
| LL-42 | Is the income gradient in AI use about intensity or about mix? | 4 | 4 | 4 | 4 | 4 | 3 | **23 (anchor)** | FOUND: everything sits inside one wave at N = 116 after the steward corrected the entry's premise; the two components are jointly determined, which caps TEACH. |
| LL-05 | Is the geography of Claude usage the geography of AI usage? | 4 | 4 | 3 | 4 | 5 | 3 | **23** | TEACH: it tests whether every ranking claim in the geography thread is about AI or about Claude; FOUND is 3 because the external series carries half the comparison. |
| LL-08 | Is AI used most for the work it speeds up most? | 4 | 4 | 5 | 4 | 4 | 2 | **23** | RISK: both variables come from the same estimator on the same transcripts, so a positive elasticity has an estimator reading the placebo may not separate. |
| LL-10 | How fast is AI use converging across US states, and how wide is the band? | 4 | 5 | 4 | 3 | 5 | 2 | **23** | RISK: four windows and 51 units, with the fourth an unweighted mean of two unweightable months; the band may span "no convergence" to "two years" — reportable, but an awkward headline. |
| LL-23 | Do Anthropic's own exclusion rules change its published geography? | 4 | 4 | 4 | 3 | 4 | 3 | **22 (anchor)** | FEAS: five of six quantities reproduce under both samples, but no AUI or Gini carries a sampling interval, so only movements above the 0.7–0.9 pp rebuild error can be read. |
| LL-29 | Do people do one thing at a time with AI, and does it change what they get? | 4 | 3 | 5 | 5 | 3 | 3 | **23** | FEAS: clean at every grain in both waves; TEACH is 3 because it bounds a unit ambiguity rather than moving a published number. |
| LL-35 | Do places that started using AI earlier get more out of it? | 4 | 5 | 4 | 4 | 4 | 2 | **23** | RISK: the early-adoption proxy is collinear with income and with the tech-worker share, so a positive result has three readings on 113 countries. |
| LL-03 | Does usage-based exposure rank occupations as workers' own reports do? | 4 | 5 | 3 | 2 | 5 | 3 | **22** | FEAS: the rank test collapses to 90 SOC minor groups with a median of 60 respondents, and the broad-group version is excluded by rule — high stakes, thin instrument. |
| LL-21 | Does enterprise AI use respond to price, or to what the model costs to run? | 5 | 4 | 5 | 2 | 4 | 2 | **22** | FEAS+RISK: the indices are re-based to mean 1.0 within each wave and only the first wave ships counts, so no level travels and the design collapses to three cross-sections. |
| LL-27 | Is AI delegated the same way everywhere inside one country? | 4 | 4 | 5 | 2 | 4 | 3 | **22** | FEAS: the decomposition's real N is 32–36 countries with five or more surviving sub-national units, not the 109–125 the grain suggests. |
| LL-38 | Which of the scenario model's parameters can usage data discipline? | 4 | 4 | 4 | 3 | 5 | 2 | **22** | RISK: the steward named two further observable dials, taking the post to six, which is exactly the sprawl lesson 5 records; the audit table is worth having, the scope is not yet safe. |
| LL-06 | Did AI use spread to new tasks, or to new countries? | 4 | 4 | 5 | 2 | 4 | 2 | **21** | FEAS: a country's named task mix covers only about 30% of its conversations, with the residual at a median 66–71%, so the within-country component may be measuring classifiability. |
| LL-13 | Do the economic primitives predict where AI use grows next? | 4 | 3 | 5 | 4 | 3 | 2 | **21** | TEACH: the only available outcome is usage growth itself, which is a weak test of the validation Anthropic asked for, on one three-month step. |
| LL-26 | Has AI use moved up or down the occupational wage ladder? | 4 | 5 | 4 | 2 | 4 | 2 | **21** | FEAS: the published $49.3 level does not reproduce under any of five wage constructions, so the post becomes a change decomposition whose first result is the non-reproduction. |
| LL-04 | Are the tasks people bring to AI the tasks workers say AI helps with? | 5 | 4 | 3 | 2 | 4 | 2 | **20** | FEAS: only 64.4% of task mass reaches an RPS-covered DWA and the median survey cell holds 13 respondents, so the comparison may reduce to a coverage statement. |
| LL-19 | Does AI bring more schooling to the work than the person asking does? | 4 | 4 | 5 | 2 | 3 | 2 | **20** | FEAS: the residual is 0.196 ± 0.209 years against CI half-widths of 0.17, i.e. about the size of its own measurement error — the null branch is the likely branch. |
| LL-28 | Does the autonomy measure capture what happens when AI can act? | 4 | 4 | 3 | 3 | 4 | 2 | **20** | RISK: two instruments with no common unit, sample or window; admissible on the never-merge rule, but the claim can only ever be about the measure. |
| LL-14 | Have official employment forecasts begun to price AI exposure? | 3 | 5 | 3 | 3 | 3 | 2 | **19** | ORG+FEAS: the neighbourhood is now crowded (NY Fed and Stanford DEL both use this file), and only one projections vintage is reachable, so a difference cannot be attributed to forecaster updating. |
| LL-17 | Does AI think longer on the work it is handed outright? | 4 | 3 | 5 | 2 | 3 | 2 | **19** | FEAS: two marginals on a release with no counts, 415 tasks with a positive thinking fraction, and 9.8 points of mass lost to `filtered`. |
| LL-15 | Is AI use broad across people or deep among a few? | 3 | 3 | 5 | 2 | 3 | 2 | **18** | ORG: the steward has already computed the answer (ρ = 0.9932, ratio range 0.978–1.087), so the post is a ±9% bound — the weakest survivor, as its own entry says. |
| LL-40 | How much of the world's AI use can the Index actually show? | 3 | 3 | 2 | 3 | 3 | 2 | **16** | FOUND: the internal half is our own atlas restated and the surviving contribution is carried by three external providers' disclosure practices, not by the Index. |

## 3. Ranking (adopted scores, after the referee's audit)

**28** LL-07 · **27** LL-11 · **26** LL-36 · **25** LL-09, LL-12, LL-18, LL-31 · **24** LL-16, LL-20,
LL-24, LL-30, LL-33, LL-41 · **23** LL-05, LL-08, LL-10, LL-29, LL-35, LL-39, LL-42 · **22** LL-02,
LL-03, LL-21, LL-23, LL-27, LL-37, LL-38 · **21** LL-06, LL-13, LL-22, LL-26 · **20** LL-01, LL-04,
LL-19, LL-28 · **19** LL-14, LL-17 · **18** LL-15 · **16** LL-40.

Fourteen rows carry the referee's re-scores, marked `(ref.)` in §2. Two further rows, LL-23 and
LL-42, carry `(anchor)`: the referee found the FOUND anchor applied inconsistently — a file shipped
inside a release scores 4, not 5 — and fixing only the audited rows would have left the
inconsistency in the file, so I applied the same anchor to the two unaudited rows where it plainly
bites. Neither moves the cut. The referee may reverse both; they are the only scores in this file
that are neither mine as first written nor the referee's.

## 4. The cut line, rerun on the adopted scores

**Step 1 — inherited framings removed before scoring is consulted.** LL-01 and LL-22 are out on the
director's ruling 1: each re-dresses a `reference/` post, which the short-list standard forbids
whatever the score. Their re-scores (20 and 21) are recorded in §2 and their sketches are removed.
Neither is re-sketched.

**Step 2 — candidates at Σ ≥ 25.** Seven: LL-07 (28), LL-11 (27), LL-36 (26), LL-09, LL-12, LL-18
and LL-31 (25). LL-12 enters on score, as the referee said it would. Seven is below the permitted
range of eight to ten, so the tie group immediately below is opened.

**Step 3 — the tie at Σ = 24, run on the stated order (TEACH → FEAS → FOUND).** Six candidates sit
at 24: LL-16, LL-20, LL-24, LL-30, LL-33, LL-41. The referee's description of this tie named
LL-16/LL-24/LL-30/LL-37; **LL-37 cannot enter it**, because the referee's own re-score puts it at 22
— its TEACH fell to 3 on the binding defect that no outcome series exists in any release, so
predictive validity is unreachable. That defect is noted here rather than worked around. The other
two at 24 that the referee did not name, LL-20 and LL-33, are included, because any candidate at the
tied score belongs in the tie.

- *TEACH.* LL-24 and LL-30 score 5; LL-16, LL-20, LL-33 and LL-41 score 4. The four fall out here.
- *FEAS.* LL-24 and LL-30 both score 3. Undecided.
- *FOUND.* LL-30 scores 4 (Index intersections plus a reference file shipped inside a release);
  LL-24 scores 3 (a hand-coded destination list and an external projections table carry part of the
  comparison). **LL-30 is taken first, LL-24 second.**

**Step 4 — where to stop, and why it is not a diversity judgement.** Taking LL-30 gives eight;
taking LL-24 as well gives nine; the next in the stated order would be LL-20 on FEAS 5. I stop at
**nine**, at the natural break the stated order itself produces: LL-24 and LL-30 exhaust the
candidates scoring TEACH 5, and everything below them in the tie is a TEACH 4 whose entry would rest
on the third tie-break rather than on what it teaches. The permitted range is eight to ten, so nine
is a choice of list size, not a promotion or an exclusion. **The diversity tie-breaker was not used
at all in this rerun** — its single earlier use, LL-18 over LL-12, is now moot because both are in on
score.

**Short-list, nine:** LL-07, LL-09, LL-11, LL-12, LL-18, LL-24, LL-30, LL-31, LL-36.
**Reserves, in order (correction 18):** LL-20 (24, FEAS 5), then **LL-33 and LL-41** (24, FOUND 5),
then LL-16 (24, FOUND 4). The order runs down the stated tie-break chain: all four tie at TEACH 4,
LL-20 leads on FEAS 5, and FOUND separates the remaining three.

**What this rerun cost.** Four of my ten are gone: LL-01 and LL-22 as inherited framings, LL-02 on
score after the permitted rewrite, and **LL-39 at 23**, which the referee's TEACH 3 and RISK 2 put
below the tie group. I had ranked LL-39 eighth; on the adopted scores it does not reach the cut, so
its sketch is removed and correction 8 is not applied to anything. If the director meant LL-39 to be
retained "at the line" rather than at its adopted total, that is a one-line ruling and its effect is
exact: LL-39 re-enters at rank eight and LL-24 becomes the first reserve. I have not assumed it.

Thread spread of the nine, for information and not as a criterion: T1 in five, T4 in five, T8 in
three, T3 in two, T2 in two, T5 in two, T10 in one, T7 in one. **T5 and T10 now appear**, through
LL-24, and they appear on score rather than on theme, which is the outcome I said at Step 2 I would
prefer to a diversity promotion. T6, T9 and T11 are absent; T9's absence remains structural.

## 5. Pairs among the short-listed that could not both be posts

Two of the five pairs I listed at Step 2 dissolve with LL-01 and LL-22; the referee's four additions
are adopted, and one carries over.

1. **LL-11 and LL-36 — hard pair (carried over).** Separable as questions — migration between
   surfaces; composition inside a category — but both would headline the same series, coding's share
   on Claude.ai against the API across the three long waves. Pick one; the other's frame appears
   inside it.
2. **LL-09 and LL-11 — hard pair (referee).** They share an outcome variable: the November→February
   change in a task's Claude.ai share, and therefore the same exposure to the February Super Bowl
   inflow. Two posts resting on one series' movement would be one finding told twice.
3. **LL-07, LL-36 and LL-30 — construction triple (referee, correction 19).** All three build the
   task → SOC join and all three must fix the multi-holder rule; LL-30's reconstruction leg uses
   exactly the same join, though its direct leg reads the occupation off the June node and needs
   none. Not a duplication of question, but whichever is written first states the construction and
   the others cite it rather than re-deriving it.
4. **LL-12 and LL-36 — soft pair (referee).** Both work the global `onet_task` concentration frame;
   LL-12 on the whole task universe, LL-36 inside one occupational category. Written together they
   would read as one concentration post.
5. **LL-18 and LL-31 — soft pair (referee).** The same shape as the old LL-01/LL-18 pair: a measure
   across places against income and adoption. Separable if one is written on the primitive at
   country grain and the other on artifact shares at country and state grain, which is how the
   entries stand.
6. **LL-24 and LL-30 — no overlap**, and worth saying so: the two sit on different files (the
   labour-market folder; the June `soc_occupation` nodes and the long-wave intersections) and answer
   different questions. Of the nine, **LL-36 is the most entangled**, appearing in three pairs, and
   LL-07, LL-11 and LL-30 in two each.

Dissolved: LL-22/LL-39 and LL-02/LL-39 (all three candidates are out) and LL-01/LL-18 (LL-01 is out).
One consequence survives its pair: LL-31 must now state the both-month and 0.5-floor admission rules
itself rather than citing LL-22, which is correction 6 and is applied in its sketch.

## 6. One-page sketches

Nine sketches follow, each in the fixed section order the director set: first the six survivors of
the first round in ID order, revised under corrections 1–10 and the editor's WITH A CHANGE notes,
then the three new entrants — LL-12, LL-30 and LL-24 — which have had neither a referee audit nor an
editor note yet. No hypothesis appears here that is not already in the candidate's
`programme/LONGLIST.md` entry, and no assumptions sweep is attempted: that is the brief's job. The
sketches of LL-01, LL-02, LL-22 and LL-39 are removed, not amended.

---

### LL-07 (Σ 28, rank 1) — Is AI delegated more on cheap work or on expensive work?

**Question.** Does the share of AI use that is delegated rather than collaborative rise or fall with
the wage of the work being done?

**Thread and ledger items.** T3, with T4. `L-2025-02-R1-16` *partially answered* (occupation and
category delivered; "the wage cross is published nowhere"); `L-2025-02-P1-22` *partially answered*
(automation share by wage or Job Zone was one join away and is never shown);
`L-2026-09-SCPA-27` *open* (whether the exposure anchor is employment- or wage-bill-weighted is not
stated).

**Why it matters.** Whether delegation rises or falls with the price of the work is the sign of the
first-order labour-share effect in Anthropic's own framework: automating expensive tasks moves a
large wage bill, automating cheap ones moves a small one. `economic-index-2026-03-report` prices the
work (Fig 1.4 p.8) and `economic-index-2026-06-report` prices its compute (Fig 2.3 p.13), and neither
says whether the expensive work is the delegated work. It informs the weighting of every
automation-share input to a forward model, and it moves the prior of anyone who reads "automation
share" as if all tasks were the same size.

**Contribution.** *If it holds* (delegation rises with wage): the automation share understates the
wage bill at stake, and the post supplies the wage-weighted version. *If it fails* (delegation falls
with wage): high-wage work is the collaborative work, the observable form of the mentor's
labour-augmenting reading. *If null*: the post publishes the first wage-by-collaboration table in the
corpus with its MDE and states what a global-only intersection can resolve.

**Design in brief.** Take the task × collaboration intersection at global in three waves, attach a
wage to each task through the shipped O\*NET statements and wage file, and estimate the
usage-weighted gradient of the automation share in the task's wage, repeating it in all three waves
so persistence is shown rather than asserted. A task's automation share is computed on the
**five classified patterns**, with the `none` share reported beside it in every table so the base is
never implicit. The comparison that carries the finding is the gradient in the same wave's own task
mix, not across waves. Key number: the automation-share difference between the top and bottom wage
quartile of tasks, usage-weighted. Rough detectable effect: the nominal task counts are 2,617 /
3,169 / 3,259, but the estimate is usage-weighted, so the **effective sample is Kish's**
n/(1+cv²) on the `onet_task_pct` weights, which the concentration of usage will put well below the
nominal count; the post reports the effective N beside the nominal one and computes the MDE from
the effective figure (correction 2).

**Data.** Steward line, verbatim: "**LL-07. FEASIBLE.** `onet_task::collaboration` exists at
`geography=global` in all three long waves with both `_pct` and `_count` over 2,617 / 3,169 / 3,259
tasks, with global `onet_task_pct` weights in the same wave. Wage coverage is near-total, not
marginal: through the shipped O\*NET 20.1 statements to `wage_data.csv` after `MedianSalary > 100`
(1,084 of 1,090 rows), **99.4% / 99.0% / 99.3%** of *named*-task usage mass carries a wage. State the
multi-holder rule (a task's wage is an aggregate over the occupations holding it). Log (e) 7."
Supplementary: `release_2025_09_15/data/intermediate/onet_task_statements.csv` and
`release_2025_02_10/wage_data.csv`, both shipped inside releases; join key is the lower-cased,
stripped task text, then `SOCcode`. BLS Employment Projections median annual wage on `occ_code` is
the second wage source.

**Overlap with existing work, stated.** `economic-index-2026-03-report` Fig 1.4 prices the task mix
and Fig 2.2 sorts model choice by wage; `economic-index-2026-06-report` Fig 2.3 sorts tokens by wage.
The collaboration facet is never crossed with wage in any wave. Externally, Chatterji et al. (2025)
report that work usage concentrates in highly paid occupations without regressing their Asking/Doing
split on a wage, and Tomlinson et al. (2025) correlate wage with an applicability score rather than
with delegation.

**Risks, ranked.** (1) The multi-holder rule: a task held by several occupations has no single wage —
observed as the gradient moving between the three aggregation rules, bounded by the steward at
≤0.17 pp on the SOC-15 share. (2) Wage vintage: a 2019 scrape and a 2025 projections series may
disagree — observed as the two wage sources giving different quartile cuts. (3) Occupation is
inferred from the task, so a task's wage is the wage of work that *resembles* it — observed as
implausible pairings surviving into the top quartile.

**What it teaches.** Which end of the wage distribution AI is being handed outright, and therefore
how much of the wage bill an automation share implies.

**The imaginable close.** *Holds*: that the work people hand over entirely is the expensive work,
and what that implies for who feels it first. *Fails*: that the expensive work is the work people
stay inside. *Null*: that delegation does not track the price of the work at all, which is itself
the answer to the question the corpus has been pricing around (editor's note: the join-failure
version read as a methods note and is dropped).

**Mentor and Institute hooks.** ⟨mentor⟩ task value as "the average hourly wage of US workers who
perform that task" (`economic-index-2026-03-report`, p.8, fn 5 p.11); ⟨mentor⟩ "more compute is
associated with more valuable artifacts" (`economic-index-2026-06-report`, pp.2–3). Institute:
`ED-7`, and the EPF's measurement ask.

---

### LL-09 (Σ 25 ref., rank 4=) — Does AI's measured success rate predict which work people keep bringing to it?

**Question.** Does a task's measured AI success rate in one window predict whether its share of use
grows by the next?

**Thread and ledger items.** T4, with T8. The gap is `L-2026-01-R4-37` *open* (task success has no
reported validation statistic and carries three headline results) and `L-2026-03-R5-29` *open* (a
model judging its own success could produce the tenure result with no learning); `L-2026-01-R4-25`
*open* is cited **only as the criterion this design approximates** — it asks for labour-market
outcomes, and task-share growth is not one (correction 3).

**Why it matters.** Task success is the most load-bearing and least validated primitive in the
corpus: it halves the published productivity number, reorders effective coverage and carries the
learning-curve result. Anthropic named prediction as the validation that counts and never ran it. If
the primitive has no predictive content, the statement that becomes unusable is the specific one an
outside economist quotes: the success-adjusted productivity revision from 1.8 to about 1.0
percentage points (`economic-index-2026-01-report`, p.38, p.48), because the adjustment is a
reweighting by a measure with no demonstrated relation to anything observable.

**Contribution.** *If it holds* (success predicts growth): the primitive earns its first predictive
validation and the post supplies the elasticity. *If it fails*: a measure the model computes about
its own work does not predict what users do next, and three published results inherit that. *If
null*: the post reports the MDE over the matched task set and how many waves the test would need — a
direct input to the Institute's cadence promise.

**Design in brief.** On the tasks common to November 2025 and February 2026, regress the change in a
task's usage share on its November success rate, weighting by usage. The split-sample instrument is
**dropped**: it is not implementable on published aggregates (correction 3). In its place the
August 2025 share instruments the November level, and August→November growth is the placebo, with
the education primitive as a second placebo. The February window carries the Super Bowl inflow the
fifth report names (fn 3, p.18) as a composition shock on the outcome, and the post flags it before
the estimate rather than after. The comparison that carries the finding is high- against
low-success tasks' subsequent share growth. Key number: the share-growth difference between the top
and bottom success quartile. Rough detectable effect: with 2,427 tasks in the regression sample a
correlation of about 0.06 is detectable at 80% power, so the test is sharp enough that a null would
be informative rather than merely quiet.

**Data.** Steward line, verbatim: "**LL-09. FEASIBLE.** `onet_task::task_success` at
`geography=global` (`_count`, `_pct`; `yes`/`no`) in both waves. Matching lower-cased task text:
**2,886** named tasks common to Nov 2025 and Feb 2026; **2,427** carry a Nov-2025 success rate and so
enter the regression (91.95% of Nov named mass); 2,608 carry a Feb rate. Unmatched: **282 Nov-only,
372 Feb-only** — report both. Log (e) 13." No supplementary source; the join is on lower-cased task
text within the Index.

**Overlap with existing work, stated.** The fourth report states the validation criterion at p.24 and
no publication runs it; the nearest thing in the corpus is a cross-sectional tenure–success
association. Externally, Tomlinson et al. (2025) run the closest analogue on another platform,
reporting that their scope measure correlates with the log share of user activity — which is why this
post's contribution is the Anthropic-data version and not the idea.

**Risks, ranked.** (1) Mean reversion: regressing growth on an initial level inherits a negative bias
— observed as a negative coefficient that disappears when the August 2025 share instruments the
November level. (2) Composition: the February window carries the Super Bowl inflow of first-time
users, so a task's share can move because the user base moved — observed as the placebo growth
window showing the same gradient. (3) Entry and exit: 282 tasks appear only in the first wave and
372 only in the second, and those margins are outcomes the regression conditions away — observed as
the result changing when the margin is included. (4) Circularity: the same model produces the
success label and the task label — observed as the education placebo moving with the outcome.

**What it teaches.** Whether the primitive that carries Anthropic's productivity revision has any
predictive content at all, on the only outcome the public data offers.

**The imaginable close.** *Holds*: that people bring back the work AI does well, which is the first
evidence that the success measure is measuring something. *Fails*: that what AI does well and what
people return with are different things. *Null*: that the tasks arriving and leaving the sample move
more than the tasks that stay, so the measure's predictive content cannot be read off a panel that
conditions on survival — which is a statement about what the next release would have to publish
(editor's note: "a single quarter cannot tell" was not available at this power and is dropped).

**Mentor and Institute hooks.** ⟨mentor⟩ interest 3, stating a design's power and publishing nulls
("differential increases in unemployment on the order of 1 percentage point would be detectable",
`labor-market-impacts-2026-03`, p.12). Institute: `ED-4`, `Share 1`.

---

### LL-11 (Σ 27 ref., rank 2) — Do the tasks that grow on the enterprise API shrink on the consumer surface?

**Question.** When a task's share of use rises on the enterprise interface, does its share fall on
the consumer one?

**Thread and ledger items.** T3, with T1. `L-2026-03-R5-17` *open* (the migration is asserted, never
measured as a migration); `L-2026-03-R5-18` *open* ("we expect that this migration … may signal more
imminent transformation of work"); `L-2026-01-R4-23` *open* (the promised API analysis of which tasks
enter production workflows).

**Why it matters.** The claim this tests is published and dated: "Coding tasks continue to migrate
from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic"
(`economic-index-2026-03-report`, p.7, 24 March 2026), with the mechanism at p.6 and the labour-market
reading at OQ 17, p.9 — "As tasks migrate to the API, they may become more exposed to automation."
It has never been measured as a migration. Whether the two surfaces' task series are negatively
related at task level decides whether that sentence describes a flow or two independent growth
stories, and therefore whether the Index has a leading indicator at all.

**Contribution.** *If it holds* (task shares move in opposite directions across surfaces): the
corpus's central leading-indicator conjecture has its first evidence and the post publishes the
measure. *If it fails*: the surfaces are growing independently, the mechanism claim needs restating
and the policy framing loses its anchor. *If null*: the post reports the correlation with its
interval and shows that three windows of two global cross-sections cannot separate migration from
independent growth.

**Design in brief.** First reproduce the published relative changes the migration claim rests on —
"Since August 2025, the share of tasks in this category has increased by 14% in the API and
decreased by 18% in Claude.ai" (`economic-index-2026-03-report`, p.7) — before any new number, as
criterion 3 requires. Then, on the tasks present in all six frames, correlate the change in a task's
Claude.ai share with the change in its API share across the three pre-June windows, with the
accounting identity stated and non-coding tasks as a control group. The February window carries the
Super Bowl inflow (ibid., fn 3, p.18), which moves the Claude.ai denominator and is flagged before
the estimate. The comparison that carries the finding is the cross-surface correlation of changes,
against zero and against the same statistic computed within each surface. Key number: that
correlation, with its confidence interval. Rough detectable effect: 1,241 tasks in all six frames
give a detectable correlation of about 0.08, so a weak but real migration signal would be visible
and a strong one unmistakable.

**Data.** Steward line, verbatim: "**LL-11. FEASIBLE.** Global `onet_task_pct` exists for both
surfaces in all three pre-June waves: named nodes 2,616 / 3,168 / 3,258 (Claude.ai) and 2,054 / 2,251
/ 2,297 (API); pairwise overlap 1,603 / 1,823 / 1,908; **1,241 tasks appear in all six frames**,
carrying **80.9%** of Claude.ai and **83.2%** of API Feb-2026 named mass. Shares only, and never past
2026-03-24, as your entry says. Log (e) 10." No supplementary source; the join is task text within
the Index, and the June wave is excluded because the API population changes at that boundary.

**Overlap with existing work, stated.** `economic-index-2026-03-report` p.7 states the migration and
p.6 gives the mechanism; both are statements about two independently moving share series, and the
ledger records the migration as never measured. Externally, Chatterji et al. (2025) exclude business
and enterprise plans by design and so cannot see this margin; Dillon et al. (2026) study within-firm
work patterns, not a cross-surface task flow. No provider has published it.

**Risks, ranked.** (1) Shares, not levels: a task's share can fall on one surface and rise on the
other with no conversation moving — observed as the correlation appearing even for tasks whose
absolute use rose on both. (2) Composition: the February window's first-time users move the
Claude.ai denominator for every task at once — observed as the correlation concentrating in the
November→February step and vanishing in August→November. (3) The report's own mechanism, one coding
job becoming many API calls, mechanically dilutes API shares — observed as the result concentrating
in coding tasks and vanishing in the non-coding control. (4) Three windows only, so a persistent
relationship cannot be distinguished from one window's shock — observed as the pairwise correlations
disagreeing in sign.

**What it teaches.** Whether the corpus's leading indicator is a measurable flow, and if so which
tasks are making the move.

**The imaginable close.** *Holds*: that work is visibly moving to the surface where people are not
watching, task by task. *Fails*: that the two surfaces are growing side by side and the migration
was a figure of speech. *Null*: that a share falling in one place and rising in another is not
evidence of movement between them, and that any future migration claim needs levels or a common
denominator before it can be made at all.

**Mentor and Institute hooks.** ⟨mentor⟩ "As tasks migrate to the API, they may become more exposed
to automation. API workflows are far more likely to be directive, with less need for a human in the
loop." (`economic-index-2026-03-report`, OQ 17, p.9.) Institute: `ED-7`, `Share 1`.

---

### LL-18 (Σ 25, rank 4=) — Where is AI doing work people say they could not do alone?

**Question.** Does the share of AI use that people could not have completed unaided rise or fall with
how much a place uses AI?

**Thread and ledger items.** T4. `L-2026-01-R4-39` *open* ("human could do alone", 88% globally, is
measured and never used in an analysis — the primitive most directly about substitution);
`L-2026-02-IND-16` *open* (two readings of the same figure sit unreconciled in one spotlight);
`L-2026-02-IND-06` *open* (the "at the frontier" conjecture never holds composition constant).

**Why it matters.** Substitution against complementarity is the question the third report calls
"perhaps the most important question that we hope our data will help answer", and the corpus has a
primitive built for it and uses it nowhere — a primitive that is a classifier's judgement about a
counterfactual, with no validation statistic published anywhere, which is the grade this evidence
carries in the same breath as the claim. Whether the share of unaided-impossible work is higher
where adoption is lower decides whether AI is closing a capability gap or widening one — the
distributional question `ED-5` asks, and the channel the scenario model's cognitive-wage result
turns on.

**Contribution.** *If it holds* (the share is higher where adoption is lower): AI is doing work that
would otherwise not be done in the places that use it least — stated composition-safe, as a
statement about **who Claude's users are in low-adoption countries** rather than about their
economies, since `reference/posts/post1` found those user bases to be professional and that finding
bounds this one (correction 5). *If it fails*: the frontier of unaided-impossible work sits in rich,
high-adoption economies, which sharpens the convergence worry. *If null*: the post publishes the
first cross-country distribution of the primitive with intervals and an MDE, showing the 88% global
figure hides no detectable geography.

**Design in brief.** Take the primitive at country grain in both 2026 waves, rebuild per-capita usage
for those waves, and estimate the gradient of the could-not-do-alone share in adoption and in income.
The task-mix adjustment runs on the global intersection and is **partial by construction**: a
country's published `onet_task` mix covers only about 30% of that country's conversations
(`ATLAS §Dated log (e) 2`), so the adjusted and unadjusted gradients are both reported and the
covered share is printed beside them. Counts in the 2026-03-24 wave are on a 1,000,000 sample base,
so "200 per country" means 200 per million (`ATLAS §Other bases`). The comparison that carries the
finding is the top against the bottom adoption tercile of countries. Key number: the
percentage-point difference between those terciles. Rough detectable effect: with 115 countries in
both waves a correlation of about 0.26 is detectable at 80% power, so a gradient worth a policy
sentence would be visible and a subtle one would not.

**Data.** Steward line, verbatim: "**LL-18. FEASIBLE.** `human_only_ability` exists at `global`,
`country` and `country-state` in both 2026 waves (938 / 1,082 sub-national units), plus
`onet_task::human_only_ability` at global over 3,169 / 3,259 tasks. **115** countries carry the facet
and clear 200 conversations in both waves. The residual is **`not_classified` in both waves** (never
`none`) at country and `country-state`, median **10.34% / 11.11%**; global publishes `yes`/`no` only,
summing to 100 (yes 87.9097 → 87.7599). Log (f) 5." Supplementary:
`release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` and `gdp_2024_country.csv`,
both shipped inside a release and used as static 2024 annuals; join key `iso_alpha_3` ↔ the ISO-2
`country_code` column in the same file.

**Overlap with existing work, stated.** `economic-index-2026-01-report` Fig 2.2 publishes the global
level and uses the primitive once as a control; the India brief quotes its own figure in two
directions without a comparison group. `reference/posts/post1` found that the user bases behind
low-AUI countries are professional rather than general-population; that is a bounding result this
post cites and does not re-derive. Externally, Humlum & Vestergaard (2025) report self-assessed time
savings and quality by occupation, Tomlinson et al. (2025) publish a capability "scope" rating, and
neither is a statement about what the user could have done. No geography of this construct exists
anywhere.

**Risks, ranked.** (1) Construct: the primitive is a classifier's judgement about a counterfactual,
with no validation statistic in the corpus — observed as the level being uninterpretable and only
ranks usable. (2) Language and prompt style vary by country, so the classifier may read the same work
differently — observed as the gradient tracking English-language share. (3) The country residual runs
at a median of about a tenth of conversations — observed as the gradient moving when the residual is
reported rather than renormalised away.

**What it teaches.** Where AI is doing work that would not otherwise get done, which is the only
observable form of the substitution question the corpus says matters most.

**The imaginable close.** *Holds*: that the places using AI least are the places where it does most
of the work that would not otherwise be done. *Fails*: that the work no one could have done alone is
concentrated where the technology is already densest. *Null*: that the first cross-country
distribution of this primitive is flat within its own floor and residual, which is what the corpus
should have said when it published the global figure.

**Mentor and Institute hooks.** ⟨mentor⟩ T4(e): lead author of the report that built the primitives
(`economic-index-2026-01-report`, p.1, ch.4) and of the first tracking of them
(`economic-index-2026-03-report`, Table 1.1 p.9). Institute: `ED-5`, `ED-1`.

---

### LL-31 (Σ 25 ref., rank 4=) — Does what people take away from AI depend on where they are?

**Question.** Does the mix of concrete outputs people get from AI vary systematically with a place's
income or its rate of use?

**Thread and ledger items.** T2, with T1. `L-2026-06-R6-30` *open* (no per-capita geography result at
all in the sixth report, though the index is released); `L-2026-06-R6-31` *open* (no subregion result,
though the grain exists); `L-2026-06-R6A-19` *open* ("Cowork" used as a surface name without
definition and no exhibit separating chat from Cowork).

**Why it matters.** Artifacts are the closest thing in the corpus to output: a document, a
spreadsheet, a piece of code. A geography of artifacts is the first observable answer to the
value-capture half of `ED-1` — whether richer places get different things from the same technology
rather than merely more of it. It also tests the sixth report's own silence: the release made the cut
available and the report published no geography at all.

**Contribution.** *If it holds* (the artifact mix varies with income or adoption): the post supplies
the first geography of AI output and names what poorer places produce more of. *If it fails* (mixes
are flat): what people take away is invariant to place, strengthening the case that usage differences
are about volume rather than kind. *If null*: the post reports the coverage of the artifact metrics
below global and which grains support any comparison.

**Design in brief.** Pool April and May as an unweighted mean, keep only units publishing all
thirty-two metrics in both months, apply a `pct ≥ 0.5` floor wherever a ratio is formed — both rules
stated in the post itself, not cited from elsewhere (correction 6) — and relate each place's
artifact mix to income and to the released per-capita index. **Primary outcomes are pre-specified**:
the sixth report's own three artifact groupings, or at most four named shares, fixed before
estimation; any statistic that maximises over the thirty-two shares carries a permutation null, so
that a "largest gradient" is scored against the distribution of largest gradients under
randomisation. The state leg is the 51 US units that carry the AUI; there is no income or AUI series
for subregions outside the US, so no subregion MDE is claimed. The comparison that carries the
finding is the top against the bottom income tercile's mix on the pre-specified outcomes, with
April–May agreement as the noise check on every claim. Key number: the income gradient in the
largest pre-specified share, with its permutation p-value. Rough detectable effect: 114 countries
give a detectable correlation of about 0.26.

**Data.** Steward line, verbatim: "**LL-31. FEASIBLE — the raggedness you feared is not in this
block.** At `category_name == overall` **every** published unit-month carries all 32
`artifact_*_pct` metrics: 235 of 235 country unit-months and 1,188 of 1,188 subregion unit-months.
**114 of 121** countries and **536** subregions (including all 52 US units) publish all 32 in **both**
months, and all 114 countries also carry the AUI; subregions **do** carry these metrics at `overall`
(the `pct`-only rule bites inside the ladders). No counts: pool as the unweighted April–May mean and
admit only both-month units, with a `pct` ≥ 0.5 floor wherever a ratio is formed. Log (g) 3."
Supplementary: `gdp_2024_country.csv` from `release_2025_09_15/data/intermediate/`, shipped inside a
release; join key `iso_alpha_3`, with the June wave's ISO-3 country ids and its ISO-2-prefixed
subregion ids handled per `ATLAS §Traps 4`. Naming, per the editor's standing ruling
(`room/editor-2026-09-16-room-catchup.md`): because this post cites `release_2026_06_26`, its first
mention of the per-capita index carries "(called the 'Anthropic Usage Index' in the June 2026
documentation)", with the house term AI Usage Index used thereafter.

**Overlap with existing work, stated.** `economic-index-2026-06-report` ch.2 publishes the taxonomy
and the global shares and no geography; the threads map records the absence as a tension — the
measure got finer and the reporting stopped. `reference/posts/post2` Stage 2 already decomposed the
US-state artifact mix, so the state leg of this post is a citation and an extension, not a new
finding; the country leg is the new object. Externally, Chatterji et al. (2025) and arXiv 2605.30685
publish topic and purpose mixes by country income, neither of which is a statement about what was
produced; no other provider releases an artifact taxonomy at all.

**Risks, ranked.** (1) A max-over-thirty-two statistic finds extremes in noise — the same defect
`L-2025-09-B3-17` records in the corpus's own overrepresentation stories — observed as the largest
gradient failing its permutation null. (2) Compositional shares rounded to two decimals, so a
distinctive small category in a small unit can be rounding — observed as gradients concentrated in
categories below the 0.5 floor. (3) No counts in the wave, so units cannot be sized and the pooling
rule is unweighted by necessity — observed as April and May disagreeing for the units that drive a
result. (4) Artifact classification has no published accuracy statistic — observed as a gradient
that tracks language or task mix rather than output type.

**What it teaches.** Whether the same technology yields different products in different economies,
measured rather than assumed.

**The imaginable close.** *Holds*: that where people work shapes not just how much AI they use but
what they take away from it. *Fails*: that the mix of things people take away is the same everywhere,
and the difference between economies is one of volume alone. *Null*: that the pre-specified shares
move together with income in April and apart in May, so a wave with no counts cannot yet carry a
geography of output.

**Mentor and Institute hooks.** ⟨mentor⟩ first named author of the wave that introduced artifacts
(`economic-index-2026-06-report`, p.1) and of its interpretive claim that compute and human
involvement move together (pp.13–14). Institute: `ED-1`, `ED-3`.

---

### LL-36 (Σ 26 ref., rank 3) — Is coding still the leading edge of AI use, or just its largest share?

**Question.** As coding's share of AI use falls on the consumer surface, is the coding work that
remains becoming narrower or staying the same?

**Thread and ledger items.** T7, with T1. The gap rests on `L-2025-03-R2-09` *open* (whether growth
in the other categories is diffusion, novel applications of coding, or capability — the three-way
fork, never tested). `L-2025-04-SWE-11` and `L-2025-04-SWE-14` are **touched, not addressed** by
this design (correction 7): a concentration statistic says nothing about which roles disappear or
about front-end work specifically. It also absorbs `L-2025-02-P1-28` from the deleted LL-32, as a
pre-registered robustness cut.

**Why it matters.** The Institute's headline evidence that "jobs like software engineering are
changing radically" is this thread, and the policy reading of the Index assumes coding is the
leading indicator for knowledge work. If coding's share is falling while the work inside it
concentrates, the series is saying something about the work; if the share is falling with
composition flat, the claim is about the denominator.

**Contribution.** *If it holds* (the top-ten share inside the category rises as the category's share
falls): what remains is **more concentrated**, and the post states the two readings that a
concentration statistic licenses — a narrowing leading edge, or casualisation of the surface as
routine coding leaves — without choosing between them on this evidence alone (correction 7). *If it
fails* (the share falls with concentration flat): coding is being diluted by diffusion elsewhere,
and the agenda's sentence is not what this series says. *If null*: the post publishes the first
within-category decomposition of the corpus's most-quoted share, with the taxonomy breaks marked.

**Design in brief.** Reproduce first: the published relative changes at
`economic-index-2026-03-report` p.7 — "increased by 14% in the API and decreased by 18% in
Claude.ai" — before any new number (criterion 3, correction 7). Then rebuild SOC major group 15 from
global task shares in the three long waves on both surfaces and compute, per wave, the share of the
category's own mass sitting in its ten largest tasks. The comparison that carries the finding is
within-category concentration against the category's total share, and Claude.ai against the API.
Key number: the change in within-category concentration between August 2025 and February 2026,
beside the change in the category share. Rough detectable effect: the category holds thousands of
task nodes, so sampling is not the constraint; what matters is that both published bases reproduce
(39.03 / 35.86 against the facet's 39.0412 / 35.8771), so a movement of a point or two is
interpretable rather than a reconstruction artefact.

**Data.** Steward line, verbatim: "**LL-36. FEASIBLE — and the reconstruction gap you feared is 0.02
pp.** Rebuilding SOC major group 15 from global `onet_task_pct` through the shipped O\*NET 20.1
statements gives, for August 2025, **39.03%** (classified base) and **35.86%** (all-conversation
base) against the published `soc_occupation` facet's **39.0412%** and **35.8771%**. Series: Claude.ai
39.03 → 36.02 → **32.23** (classified); 1P API 49.98 → 51.73 → 51.61, i.e. 45.67 / 46.60 on the
all-conversation base — the published "~46%" and "34–35%" both reproduce once the base is named.
Log (g) 5." Supplementary:
`release_2025_09_15/data/intermediate/onet_task_statements.csv`, shipped inside a release; join key
the lower-cased task text, then `O*NET-SOC Code` to major group.

**Overlap with existing work, stated.** The category share is the corpus's most-cited series and is
always reported as one number; the fifth report attributes its movement to call-splitting without
testing it inside the category. Externally, Chatterji et al. (2025) report programming as a small and
falling share of consumer messages — a sharply different picture that makes the within-category
question worth asking — and Tomlinson et al. (2025) note that Claude studies show more emphasis on
computer and mathematical tasks than theirs. No provider decomposes its own coding share.

**Risks, ranked.** (1) Base naming: the same series reads differently on the classified and
all-conversation bases and the corpus quotes both — observed as a reader comparing our number with a
published number computed on the other base. (2) The category is reconstructed through an external
task-to-SOC join in the waves that ship no occupation facet — observed as the reconstruction drifting
from the published facet in the waves where it cannot be checked. (3) The allocation rule for
multi-holder tasks — observed as the category share moving between rules, bounded by the steward at
≤0.17 pp.

**What it teaches.** Whether the Index's most-quoted series is about coding changing or about
everything else arriving.

**The imaginable close.** *Holds*: that the coding work left on the consumer surface is a more
concentrated thing than it was, and that the same fact reads as a narrowing frontier or as a
surface left with the routine, depending on which the next wave supports. *Fails*: that coding is
not shrinking so much as being surrounded. *Null*: that the category cannot be rebuilt on a stable
base across the waves that matter, so the corpus's most-quoted share is not yet a series anyone
should difference.

**Mentor and Institute hooks.** ⟨mentor⟩ T3(e), the migration of coding work to the API as his stated
leading indicator (`economic-index-2026-03-report`, OQ 17–19). Institute: `ED-7`, and the agenda's own
evidence claim (`institute-agenda-2026-05`, *Lead ¶4*).

---

---

### LL-12 (Σ 25, rank 4=) — Is AI use getting broader, or is the same work recurring? *(new entrant)*

**Question.** Within a single measurement window, is AI being used across a widening set of tasks,
or is the apparent widening an artefact of pooling windows together?

**Thread and ledger items.** T1. `L-2025-02-P1-17` *partially answered* (the branching hypothesis:
occupations evolve if the pattern persists, transition if breadth grows without saturation);
`L-2026-03-R5A-06` *open* (the cumulative construction cannot fall, so flattening is consistent with
saturation or with a smaller pull); `L-2025-02-P1-10` *partially answered* (fewer than 20% of the
~20k O\*NET tasks are recovered).

**Why it matters.** Breadth against depth is the fork the first paper hung two futures on — jobs
evolving or jobs transitioning — and `ED-7` restates it. The figure the corpus offers,
`economic-index-2026-03-appendix` Fig A.2, is cumulative across five pulls and therefore cannot
fall, so its flattening is equally consistent with saturation and with a smaller February sample.
An Institute economist choosing between the two futures is currently choosing on a statistic that
cannot express one of them.

**Contribution.** *If it holds* (within-wave breadth rising): breadth is growing and the post dates
the growth per wave, with the concentration series as a cross-check. *If it fails* (within-wave
breadth flat while the cumulative curve rises): the published coverage claim is an artefact of
pooling, and the post supplies the non-cumulative series. *If null*: the post reports how much of
the apparent flattening is taxonomy change rather than behaviour — a measurement result the corpus
needs before any later wave is compared.

**Design in brief.** For each of the three long waves separately, and on the **union of the
Claude.ai and 1P API named nodes** — because `economic-index-2026-03-appendix` Fig A.2 pools both
surfaces and a Claude.ai-only series would not be its like-for-like counterpart (correction 11) —
compute the share of occupations whose tasks are observed at 25%, 50% and 75% coverage **within that
one window**, and the Lorenz curve and Gini of task shares as a cross-check. The comparison that
carries the finding is the within-wave triple against the published cumulative 49 / 24 / 7. Key
number: the within-wave share of occupations at ≥25% task coverage, wave by wave, beside the
cumulative figure at the same dates. Because the privacy floor drops any cell below 15 conversations
in a sample of about a million, the public within-wave coverage is a **lower bound** on the internal
unfloored curve, so the three waves are compared on **shape and never on level** (correction 12).
Rough detectable effect: not a sampling question but a floor question — the post reports how many
nodes sit at counts of 15 to 20 in each wave, and bootstraps the coverage triple on the published
counts, rather than asserting that a few per cent cannot be an artefact (correction 13).

**Data.** Steward line, verbatim: "**LL-12. FEASIBLE.** Node counts are comparable across the three
long waves: the privacy floor is exactly **15** in all three and the denominators are 964,494 /
999,875 / 1,000,000 (within 3.7%), so 2,618 / 3,170 / 3,260 published nodes are like-for-like;
**2,284** appear in all three, and 3,258 of 3,260 Feb nodes join the shipped O\*NET 20.1 statements
for the per-occupation denominator. Keep `release_2026_06_26` separate (O\*NET 30.2, new
classifier). Log (e) 9." Supplementary:
`release_2025_09_15/data/intermediate/onet_task_statements.csv` (O\*NET DB 20.1, 19,530 rows, 974
O\*NET-SOC codes), shipped inside a release; join key the lower-cased, stripped task text.

**Overlap with existing work, stated.** The cumulative curve is Anthropic's own and is cited, not
replaced; the first paper's fork is quoted as the question. Externally, Bick, Blandin, Deming &
Schumacher (2026) answer the survey version — "adoption is widespread but shallow", with fewer than
3% of tasks above 50% adoption — on workers rather than conversations, which is the comparison this
post's discussion sets itself against rather than reproduces.

**Risks, ranked.** (1) The published node count is bounded by how many tasks a fixed sample can
reach, so breadth and sample size are not separable in levels — observed as node counts tracking
the denominators; mitigated by reading breadth off shape, off the 2,284 common tasks and off the
scale-free Lorenz curve. (2) **Churn, which is the third reading beside saturation and pooling**:
2,284 of 3,170 and 3,260 nodes are common to all three waves, so roughly 28% of the task set turns
over between waves, and a flat coverage series can hide a changing set of occupations
(correction 13) — observed as the common-node series and the all-node series diverging. (3) Taxonomy
movement: the fifth report recoded to 2019 O\*NET-SOC for one figure — observed as the
per-occupation denominators shifting between waves. (4) Suppression removes rare tasks first, which
is where breadth lives — observed as the coverage triple moving with the `none`/`not_classified`
mass.

**What it teaches.** Whether the Index's own evidence on the corpus's oldest fork says breadth is
growing, once the statistic can fall.

**The imaginable close.** *Holds*: that the reach of AI across the work of an occupation grows from
one window to the next, and that the published curve was right for a reason it could not
demonstrate. *Fails*: that the widening belongs to the way the curve is drawn rather than to the
work. *Null*: that a taxonomy which moves between waves cannot answer a question about breadth, and
what a stable one would cost.

**Mentor and Institute hooks.** ⟨mentor⟩ the adoption-curve reading — "early adopters favor specific
high-value uses like coding, and later adopters take on a much wider range of tasks"
(`economic-index-2026-03-report`, OQ 20, p.3) — and the task-value series that breadth mechanically
drives (claim 11, Fig 1.4 p.8). Institute: `ED-7`, `ED-3`.

---

### LL-30 (Σ 24, rank 8, entered on the TEACH tie-break) — Is the work AI does for work the same work it does for study? *(new entrant)*

**Question.** Does the occupational composition of AI use differ between work, coursework and
personal use?

**Thread and ledger items.** T1, with T4. `L-2025-02-P1-26` *partially answered* (the facet was run
and only two aggregate numbers reported; a use-case × occupation distribution is still published
nowhere); `L-2026-01-R4-49` *open* (speedup is never split by use case, though 54% of Claude.ai
conversations are not work); `L-2026-03-R5-06` *open* (educational tasks may be easier, or students
mindful of usage limits — offered and untested).

**Why it matters.** Every occupational claim in the Index is built on conversations of which more
than half are not work, and the occupational mapping does not know which is which. If the
occupational mix of coursework and personal use differs sharply from that of work use, the headline
occupational shares — and `observed_exposure`, which gates on work usage through the
`1{WorkUsage_t ≥ 100}` term — are averaging two different populations. What it decides is whether an
economist can read an Index occupation share as a statement about that occupation's labour market
at all.

**Contribution.** *If it holds* (the mixes differ): the post supplies the work-only occupational mix
the corpus has never published, and quantifies how much the headline shares move. *If it fails* (the
mixes are similar): the work gate is doing little, which simplifies the interpretation of every
occupational series. *If null*: the post publishes the global use-case × task intersection with its
suppression accounting — the first time that cut appears in any publication.

**Design in brief.** The **direct measurement** is the June 2026 cross, which the first draft of
this sketch missed (correction 14): `release_2026_06_26` publishes
`use_case_{work,personal,coursework}_pct` inside every `soc_occupation` node — global L0 (718
detailed occupations) and L1 (22 major groups), and country L1 (22 × 121) — so the occupational mix
under each use case is read off directly at detailed grain, with a 121-country leg at major-group
grain. The **fixed-instrument check** is the reconstruction from the long-wave intersections
(`onet_task::use_case`, `request::use_case`) in the two 2026 waves, whose classifier and taxonomy
are stable and where the cut is global-only; the two legs are reported side by side and **never
spliced**, because the June wave rebuilt the classifier and pools Cowork into the Claude.ai
population. The comparison that carries the finding is the work-only occupational share against the
published all-conversation share, occupation by occupation. Key numbers: the total-variation
distance between the two mixes, reported beside the largest single displacement, since a maximum
over twenty-two groups is a max-over-grid statistic (correction 15). Rough detectable effect: 718
occupational nodes at global and 22 groups across 121 countries; the binding limit on the
reconstruction leg is that it is global-only, so that leg is two cross-sections and not a geography.

**Data.** Steward line, verbatim: "**LL-30. FEASIBLE WITH CAVEAT: the residual label differs
*within* the February wave, and the whole cut is global-only.** `onet_task::use_case` (3,169 / 3,259
nodes) and `request::use_case` (737 / 730) both exist in both waves; `use_case` itself is at all
three grains. Global carries `not_classified` (0.0153) in Nov and `none` (0.0298) in Feb — but the
**Feb intersections carry both labels**, so neither may be hard-coded at either grain. Tasks with a
published work/coursework split hold **87.92 / 86.96** of the 93.51 / 92.97 named-task mass.
Log (g) 2." The "global-only" clause binds the **long-wave reconstruction leg only**: the June cross
is published at global L0 and L1 and at country L1 (`data/releases/release_2026_06_26.md` rows
187/196/197; `ATLAS §Which cuts exist at which grain`, Family C). Supplementary:
`release_2025_09_15/data/intermediate/onet_task_statements.csv`, shipped inside a release; join key
the lower-cased task text, then `O*NET-SOC Code`, for the reconstruction leg only — the June leg
needs no join, the occupation being the node.

**Overlap with existing work, stated.** `economic-index-2026-01-report` p.26 publishes the three-way
split and `economic-index-2026-03-report` Fig 1.2 its movement; `economic-index-2026-06-report`
Fig 1.3 shows work-related conversations by occupation **wage quartile**, which is the nearest
published cut and is coarser than an occupational mix. The June release carries the cross itself and
no publication uses it — which is the gap, and is now corrected in `programme/LEDGER.md`
`L-2025-02-P1-26`, whose answer column had said no release carries it (correction 14).
`reference/posts/post2` Stage 2 used the June within-group use-case mix, so that use is cited, not
inherited. Externally, Chatterji et al. (2025) publish the work/non-work split by topic and report
non-work growing to more than 70% of messages, on a different product and without an occupational
composition of non-work; arXiv 2605.30685 splits purposes by country income. The occupational
composition of non-work AI use is published nowhere.

**Risks, ranked.** (1) The two legs are on different instruments — the June wave rebuilt the
classifier and pools Cowork into Claude.ai — so they can disagree for reasons that have nothing to
do with use case; observed as the reconstruction and the direct cross ordering occupations
differently, which is reported rather than reconciled. (2) The reconstruction leg is global-only, so
it cannot be shown to travel; observed as two cross-sections with nothing to arbitrate them. (3) The
residual label differs between waves *and* within the February wave, so a hard-coded residual
silently drops or double-counts mass; observed as the covered mass diverging from the steward's
87.92 / 86.96. (4) Occupation is inferred from the task, so a coursework conversation about a task
belonging to an occupation is not a student's occupation; observed as the coursework mix loading on
the occupations whose tasks are most textbook-like.

**What it teaches.** How much of the Index's occupational picture is about work, and how different
the picture looks when only work is counted.

**The imaginable close.** *Holds*: that the occupational map of AI use changes shape when only the
working half of it is counted. *Fails*: that people bring the same kinds of work to AI whether or
not they are being paid for it. *Null*: that the work-only and all-conversation mixes differ by less
than the suppression accounting can carry, so the question is answered for this wave and reopens
only when a release publishes counts beside the cross.

**Mentor and Institute hooks.** ⟨mentor⟩ interest 5, pricing the work by the wage of the occupation
that performs it (`economic-index-2026-03-report`, p.8) — which the work/non-work split directly
qualifies. Institute: `ED-7`, `ED-11`.

---

### LL-24 (Σ 24, rank 9, entered on the TEACH tie-break) — Do retraining programmes train people for the work AI already does? *(new entrant)*

**Question.** Are the occupations that successful retraining programmes place people into more or
less exposed to AI than the average occupation?

**Thread and ledger items.** T10, with T5. `L-2026-08-WR-25` *open* (whether the trained occupations
are the exposed occupations is never asked; the sector destinations include occupations Anthropic's
own exposure work ranks as most exposed, and no exposure measure is joined);
`L-2026-08-WR-17` *open* (retraining for the highest-skilled may need a compressed mid-career degree,
handed to future research); `L-2026-07-EFRF-08` *partially answered* (Priority 2's evaluations and
pipeline experiments — reviewed, nothing run).

**Why it matters.** The Economic Policy Framework lists workforce training grants among Tier 1
interventions, the $200M Research Fund is paying for retraining evaluations under Priority 2, and
Anthropic's own review doubts current programmes are adequate. Four pages apart, the same review
names the sector programmes' destinations — IT support, medical assisting, bookkeeping, accounting —
and uses its own exposure measure to say that "college-educated workers—software developers,
paralegals, accountants—are most at risk". The two lists are never put side by side. A funder
deciding what to evaluate needs to know whether the destinations are themselves in the exposed
range.

**Contribution.** *If it holds* (destinations are more exposed than the average occupation): the
targeting problem is real and quantified, and the post gives the Fund a screening measure. *If it
fails*: retraining destinations are in the safer part of the exposure distribution and the review's
recommendation survives the check it never ran. *If null*: the post publishes the exposure
distribution of the named destinations with the merge audit and shows that four named occupations
cannot support a general claim.

**Design in brief.** Code the **complete** destination list the review names — p.2: nursing aides,
IT support technicians, welders; p.9: IT support and computer repair, software development, medical
assisting, nursing, medical billing, construction, building maintenance, manufacturing, accounting,
bookkeeping — to 2018 SOC, and publish the crosswalk, **before any exposure value is looked up**
(correction 16). The five destinations the steward priced omit software development at the high end
and the trades and nursing at the low end, so a subset would drive the answer. The sector families
are pre-specified with the list. Comparators are fixed ex ante (correction 17): each destination's
percentile in the employment-weighted distribution over all 756 occupations; its percentile among
the positive-exposure occupations only, since 411 of 756 are exactly zero; and its position against
the review's own at-risk list — software developers, paralegals, accountants. The statement is a
**quantile position, never a ratio** to a mean that is mostly zeros. Key number: the
employment-weighted percentile of the destination set, reported as a set with the crosswalk beside
it. Rough detectable effect: there is no sampling inference over a named list; what bounds the claim
is the coding, the 54% mass at zero by occupation and roughly 40% by employment, and a rule fixed in
advance for when a named set may carry a quantile statement at all.

**Data.** Steward line, verbatim: "**LL-24. FEASIBLE WITH CAVEAT: the comparison distribution is 54%
zeros.** All the named destinations are present: Computer User Support 15-1232 **0.4685**, Computer
Network Support 15-1231 0.2867, Accountants and Auditors 13-2011 **0.3478**,
Bookkeeping/Accounting/Auditing Clerks 43-3031 **0.3104**, Medical Assistants 31-9092 **0.0476**.
Against them, **411 of 756** occupations have exposure exactly 0 (median 0), so the
employment-weighted benchmark is mostly zeros and the comparison must be stated as a quantile
position, not a ratio. Of the 52 zero-exposure-but-positive-task occupations, **20 are in the
health, clerical and support families** (15 `29-*`, 3 `43-*`, 2 `31-*`). Log (f) 11."
Supplementary: the destination occupations named in `worker-retraining-2026-08` (pp.2, 9, 77), coded
by hand with the crosswalk published; BLS Employment Projections (`occupationProj`, 831 rows) for
employment weights, growth and pay; join key `occ_code`, merge audit 756 in / 755 matched.

**Overlap with existing work, stated.** `worker-retraining-2026-08` supplies both lists and joins
neither; `labor-market-impacts-2026-03` supplies the measure. Externally, Audoly, Guerin & Topa
(2026) and the Stanford Digital Economy Lab's June 2026 indicator note both join this same released
file to *outcomes* — postings and payroll employment — and neither joins it to programme
destinations; Brynjolfsson, Chandar & Chen (2026) find the employment gap concentrated in young
workers in exposed occupations, which is why where a programme places matters. Manning & Aguirre
(2026), as summarised by PIIE, combine exposure with demographics and places rather than with
programmes.

**Risks, ranked.** (1) The destination list is occupations named in prose, so the result rests on a
hand coding — observed as the percentiles moving when a title is coded to a neighbouring SOC;
mitigated by coding the complete list before any exposure is looked up, publishing the crosswalk,
and reporting the named set and the pre-specified sector families separately. (2)
`observed_exposure` is a **composite** — Eloundou capability, gated work usage, and the
automation-over-augmentation weighting (`labor-market-impacts-2026-03`, p.2) — not a usage measure,
so a destination's score is not a statement about how much Claude is used in it; observed as the
ranking moving if the capability input alone is substituted. (3) A zero means "no measured
exposure", not "no tasks used", and 20 of the 52 zero-exposure-but-positive-task occupations sit in
exactly the health and clerical families the programmes place into — observed as a destination
scoring zero while owning positive-penetration tasks. (4) The measure is Claude-only and dated to
the 2025 usage waves — observed as any claim about "AI exposure" being a claim about one provider's
traffic, which the post says in the sentence that carries the number. `L-2026-08-WR-17` is touched,
not addressed: nothing here speaks to what retraining the highest-skilled would require.

**What it teaches.** Whether the most promising thing in the retraining evidence base is pointed at
work that Claude is already doing, which is a fact a funder can act on this year.

**The imaginable close.** *Holds*: that the programmes with the best evidence behind them are
training people into the work Claude is already doing. *Fails*: that the destinations sit outside
what Claude is being used for, and the review's recommendation stands. *Null*: that the destination
set straddles the exposure distribution too widely to carry a single quantile statement under the
rule fixed in advance, so the targeting question needs a destination census rather than a reading
of two lists.

**Mentor and Institute hooks.** ⟨mentor⟩ "If current data on AI usage are any guide, college-educated
workers—software developers, paralegals, accountants—are most at risk (Massenkoff and McCrory 2026).
But this is highly uncertain." (`worker-retraining-2026-08`, p.4.) ⟨mentor⟩ "Impose a high
evidentiary standard" (ibid., p.5). Institute: `ED-5`, Research Fund Priority 2.

## 7. Verification

- **Written 2026-09-16**, from `programme/LONGLIST.md` at commit `2eff78a` (39 survivors, each with a
  steward feasibility line verbatim) and `programme/THREADS.md` and `programme/LEDGER.md` at
  `0f5c1c6`. Every ledger status quoted here was read from the LEDGER, not recalled.
- **The rubric was fixed and written before any candidate was scored**, in the order the file
  presents it: anchors, then aggregation, then tie-break order, then scores. No anchor was adjusted
  after a score was assigned.
- **Aggregation is an unweighted sum of six 1–5 dimensions**, maximum 30. The tie-break order
  (TEACH → FEAS → FOUND) was fixed in §1 and used in §4. In the first round the diversity
  tie-breaker was used once, to choose LL-18 over LL-12; **in the Step 3 rerun it was not used at
  all**, because both are now in on score and the tie at 24 resolved on TEACH and FOUND. The
  arithmetic of all 39 rows was re-verified by script after the re-scores were adopted.
- **No surviving entry's question or contribution was changed while scoring.** Three candidates whose
  contribution the steward's audit had already narrowed — LL-15, LL-41, LL-26 — are scored on their
  narrowed form, with the narrowing named in the rationale, and the entries themselves were amended
  at Step 1, not here.
- **Step 3 revision, 2026-09-16.** This file was revised in one pass against the director's ruling
  (c0df423), the referee's audit (0c77fbf) and the ten editor notes (768e1e8); everything that moved
  is in §8 with its authority. `reference/` was not opened by me at any point: every statement about
  `post1` and `post2` here is quoted from the referee's audit.
- **Defects found while scoring and left for the referee:** LL-37's risk column is the binding
  constraint rather than its score (no outcome series exists, so predictive validity is unreachable);
  LL-38 now carries six observable dials after the steward named two more, which is a scope defect its
  entry records; LL-14's originality fell to 3 during scoring because two external teams now use the
  same released file. None of the three is short-listed, so none of these defects affects the cut.
- **Sketch discipline.** Nine sketches, each in the director's fixed section order, each 400–600
  words of prose plus the steward's quoted line. No sketch introduces a hypothesis absent from its
  LONGLIST entry, and none contains an assumptions sweep. Four sketches were removed at Step 3
  rather than amended (LL-01, LL-02, LL-22, LL-39) and three were written fresh (LL-12, LL-30,
  LL-24).
- **What this file does not do.** It does not write a brief (that is `posts/postN/BRIEF.md`), it does
  not choose the final six posts (that is the human's, at Gate 1a), and it opens nothing in
  `reference/`.

## 8. Change log — Step 3 revision

One pass, on `room/director-2026-09-16-shortlist-ruling.md` (c0df423),
`room/referee-2026-09-16-shortlist-audit.md` (0c77fbf) and the ten editor notes
`room/editor-2026-09-16-sketch-LL-*.md` (768e1e8). Previous state of this file: commit `d353a12`.

| # | What moved | Why | Authority |
|---|---|---|---|
| 1 | **LL-01 out**, re-scored 26 → 20 (ORG 5→1, TEACH 4→2); sketch removed, not re-written | `reference/posts/post1` ran the same test on the same wave, including the AUI-with-income specification and the five-wave reproduction of Fig 2.11; my "first test" language was false as written | ruling 1; audit, inherited framing |
| 2 | **LL-22 out**, re-scored 26 → 21 (ORG 5→2, TEACH 5→3); sketch removed | `reference/posts/post2` H1 is the same question on the same wave, and both legs' key numbers are already in `ATLAS` log (f) 8; post2's brief announced the country companion | ruling 1; audit, inherited framing |
| 3 | **LL-02 out on score**, re-scored 25 → 22 (ORG 4→3, TEACH 5→3) after the one permitted rewrite; sketch removed | correction 9 applied in §2: the paper already places the two numbers side by side at pp.27–28 and compares a survey-implied ψ in Table 2, and the ledger's answer columns already carry the steward's 0.511. What remained was a decision rule and a break statement — a paragraph, not a post | ruling 2; correction 9 |
| 4 | **LL-39 out on score** at 23 (TEACH 5→3, RISK 3→2); sketch removed; **correction 8 therefore not applied to anything** | adopted re-scores put it below the 24 tie group | ruling 3; audit re-score. Flagged in §4 and in the status note: if "at the line" was meant literally, one line reinstates it at rank 8 and LL-24 becomes first reserve |
| 5 | Fourteen rows re-scored and marked `(ref.)`; two further rows, LL-23 and LL-42, marked `(anchor)` | the referee's re-scores are adopted wholesale; the FOUND anchor finding is extended to the two unaudited rows where it plainly bites, so the inconsistency does not survive in the file. Neither anchor row moves the cut | ruling 3; audit scoring section |
| 6 | §3 and §4 rewritten; the cut rerun step by step; **LL-12 enters on score**; the tie at 24 rerun over all six candidates at that score, with LL-37's inability to enter it (22, on the binding no-outcome-series defect) stated | the adopted scores changed the ranking | ruling 3 |
| 7 | **LL-30 and LL-24 enter** on the stated order (TEACH 5, then FOUND 4 against 3); list size set at nine at the TEACH 5 / TEACH 4 break; **diversity tie-breaker not used at all** in the rerun | the stated order resolved the tie without reaching diversity | §1 tie-break order |
| 8 | Three new sketches written: LL-12, LL-24, LL-30 | each new entrant gets one sketch | ruling 5 |
| 9 | Correction 1 applied: LL-18's steward line now cites "Log (f) 5"; LL-36's quoted line has its double quotation marks restored; the LL-01 header error is moot with the sketch removed | verbatim quotation must match the steward's note | correction 1 |
| 10 | Correction 2 applied to LL-07: effective N (Kish) under usage weights stated beside the nominal task counts, and the five-pattern base with `none` reported named in the design | the MDE was computed on nominal N under a weighted estimator | correction 2 |
| 11 | Correction 3 applied to LL-09: split-sample IV replaced by the August 2025 share as instrument with August→November growth as placebo; the February Super Bowl inflow flagged as a composition shock on the outcome; `R4-37`/`R5-29` cited as the gap and `R4-25` only as the criterion the design approximates | the IV was not implementable on published aggregates, and `R4-25` asks for labour-market outcomes, which task-share growth is not | correction 3 |
| 12 | Correction 4 applied to LL-11: the published "+14% API / −18% Claude.ai" reproduced before the correlation; the Super Bowl inflow flagged and added to the ranked risks | criterion 3, reproduce before building | correction 4 |
| 13 | Correction 5 applied to LL-18: the ~30% country task-mix coverage stated, the per-million count base stated, `reference/posts/post1`'s professional-user-base finding cited as bounding, and **the holds branch rewritten composition-safe** — the one place a contribution's wording changed | ruling 4 applies corrections 1–10 to surviving sketches; the substance of the branch is unchanged, the claim is now about who the users are rather than about the economies | correction 5 |
| 14 | Correction 6 applied to LL-31: primary outcomes pre-specified (the report's three groupings or ≤4 named shares), a permutation null attached to any max-over-32 statistic, the 536-subregion MDE sentence deleted, `reference/posts/post2` Stage 2 cited, the both-month and 0.5-floor rules stated in the sketch itself, April–May agreement made the noise check | the max-over-grid was the same defect the corpus's own overrepresentation stories carry, and no income or AUI series exists for subregions outside the US | correction 6 |
| 15 | Correction 7 applied to LL-36: the gap rests on `R2-09`, with `SWE-11`/`-14` marked touched-not-addressed; the published relative changes reproduced first; **the holds branch restated** as concentration, with casualisation named as the rival reading to "leading edge" | a concentration statistic does not license a leading-edge inference; second place where a contribution's wording changed | correction 7 |
| 16 | Correction 10 applied: §5 rebuilt — two pairs dissolve with LL-01 and LL-22, the referee's four additions adopted (LL-18/LL-31, LL-09/LL-11, LL-07/LL-36, LL-12/LL-36), and LL-36 noted as the most entangled at three pairs | | correction 10 |
| 17 | Editor WITH A CHANGE notes applied where they touch neither question nor contribution: LL-07 (publications named; null close is now "delegation does not track the price of the work"), LL-09 (the statement that becomes unusable named; null close rebuilt on entry and exit), LL-11 (stakes attributed to the published claim with page and date; null close now states an operating rule), LL-18 (evidence graded in the sentence that states the claim; flourishes dropped; null close is the distribution), LL-31 (holds close out of the second person and back on "take away"; null close re-described), LL-36 (null close is the reconstruction-and-base failure) | the editor's notes on register and on the imaginable close | ruling 4 |
| 18 | Editor **title-form** notes recorded and **not** applied: LL-09 ("measured success rate" presupposes the label measures success), LL-11 ("grow"/"shrink" are level words for a share design, and the question does not say AI), LL-18 ("say" attributes speech to a classifier judgement), LL-31 ("take away" reads as learning in this corpus), LL-36 ("leading edge" is not the corpus's term) | questions are frozen after Step 3 | ruling 4; flagged in the status note for the brief stage, where LL-11's missing "AI" is a criterion-6 defect that must be fixed |

**Not changed.** No surviving entry's question or contribution was changed except the two the
referee's corrections 5 and 7 require, both recorded above. No score was adjusted except the
fourteen adopted from the referee and the two anchor rows. Nothing in `reference/` was opened by me;
every statement about `post1` and `post2` in this file is quoted from the referee's audit.

### §8 continued — final pass, corrections 11–20

Second referee round `room/referee-2026-09-16-shortlist-audit-2.md` (c168b19) and the three editor
notes `room/editor-2026-09-16-sketch-LL-{12,24,30}.md` with
`room/editor-2026-09-16-sketch-notes-status-v2.md` (af583a4). Previous state: `8646d7c`.

| # | What moved | Why | Authority |
|---|---|---|---|
| 19 | **Cut confirmed and closed.** LL-39 stays out at 23 and LL-02 at 22; the referee states that his re-score is the record and that "at the line" was loose prose. The two `(anchor)` rows stand. No score in §2 changes in this pass | the one reading I flagged as open is now closed against me, which is the right outcome | audit-2 (b) |
| 20 | **LL-12**: the within-wave series is built on the **union of Claude.ai and API named nodes**, because Fig A.2 pools both surfaces; the key number becomes the within-wave share of occupations at ≥25/50/75% coverage beside the published 49 / 24 / 7, with the Gini as cross-check | a Claude.ai-only series is not the like-for-like counterpart of the published curve | correction 11 |
| 21 | **LL-12**: the privacy floor (15 in a sample of ~1M) is stated to make public within-wave coverage a **lower bound** on the internal unfloored curve, so the waves are compared on shape and never on level | the comparison as first written would have read a floor artefact as a level | correction 12 |
| 22 | **LL-12**: "more than a few per cent is not a sampling artefact" replaced by a near-floor sensitivity count (nodes at 15–20) and a count-based bootstrap; **churn named as the third reading** beside saturation and pooling (2,284 common of 3,170 / 3,260, ≈28% turnover per wave) and added to the ranked risks | the original sentence asserted what the design is supposed to establish, and two readings were listed where there are three | correction 13 |
| 23 | **LL-30**: the closest existing answer rewritten. The June wave **does** carry the cross — `use_case_{work,personal,coursework}_pct` inside every `soc_occupation` node, global L0 (718) and L1 (22) and country L1 (22 × 121) — so the June cross becomes the **direct measurement** and the long-wave intersections the **fixed-instrument reconstruction check**, never spliced. "Global-only" now binds one leg only. `reference/posts/post2` Stage 2 cited | my entry described the data wrongly, and the error came from the ledger | correction 14 |
| 24 | **`programme/LEDGER.md` `L-2025-02-P1-26` answer column corrected**: it had said no release carries the cross, citing `§Cuts 11`; it now records the June cross with its rows and notes that `§Cuts 11` rules out a cross of two *categories* and does not reach a metric published inside a category's nodes | a ledger error that had propagated into a sketch | correction 14 |
| 25 | **LL-30**: total-variation distance between the published and work-only mixes reported beside the largest single displacement (a max over 22 groups); "first time that cut appears anywhere" → "in any publication"; the exposure gate named as `1{WorkUsage_t ≥ 100}`; risks re-ranked with the two-instrument risk first | a max-over-grid needs a companion statistic, and the data now carries the cut even though no publication uses it | correction 15 |
| 26 | **LL-24**: the **complete** destination list from the review is coded before any exposure value is looked up — p.2 nursing aides, IT support technicians, welders; p.9 IT support and computer repair, software development, medical assisting, nursing, medical billing, construction, building maintenance, manufacturing, accounting, bookkeeping — with the sector families pre-specified | the steward's five omit software development at the high end and the trades and nursing at the low end, so a subset would have driven the answer | correction 16 |
| 27 | **LL-24**: comparators fixed ex ante (percentile over all 756; percentile among positive-exposure occupations; the review's own at-risk list); `observed_exposure` stated as a composite of capability, gated usage and the automation weighting rather than as usage; `L-2026-08-WR-17` marked touched-not-addressed | the comparator choice would otherwise have been made after seeing the numbers | correction 17 |
| 28 | **Reserve order** rewritten: LL-20, then LL-33 and LL-41 (FOUND 5), then LL-16 (FOUND 4) | the order runs down the stated tie-break chain | correction 18 |
| 29 | **§5**: LL-30 added to the construction pair, which becomes the **LL-07 / LL-36 / LL-30 triple**; the entanglement tally updated (LL-36 in three pairs; LL-07, LL-11 and LL-30 in two each) | all three build the task → SOC join and fix the multi-holder rule | correction 19 |
| 30 | Editor WITH A CHANGE items applied to the three new sketches, **no first person anywhere in an imaginable close**: LL-12's holds loses "each time we look" and no longer says the cumulative curve "was hiding" the growth, since a curve that cannot fall is uninformative rather than concealing; LL-30's null loses "cannot tell us" and becomes two mixes differing by less than the suppression accounting can carry; LL-24's holds says Claude rather than "the technology", and its null becomes the pre-registered rule for when a named set may carry a quantile statement | the editor's notes on register and on the imaginable close | ruling 4; editor notes |
| 31 | Correction 20's **optional re-sort of §2 by Σ declined**, with the reason recorded: the referee has verified the table row by row in its current order and §8 references it by that order; re-sorting at the final commit buys readability at the cost of re-verification. LL-11's missing "AI" stands flagged for the brief stage | optional item, declined on a stated ground rather than ignored | correction 20 |

**Editor title-form notes recorded and not applied**, questions being frozen: LL-12's "recurring"
(the second leg measures concentration within a window, not recurrence over time), LL-24's
"retraining programmes" (a class where the design has one review's destinations), LL-30's "work"
running in two senses and "study" standing in for `coursework`. With LL-11's missing "AI", these are
the four question-level defects the brief stage inherits.

**Final state.** Nine sketches, all nine steward lines verbatim, corrections 1–20 applied or
declined on a stated ground, one ledger correction made. This is the last commit of
`programme/SHORTLIST.md` before Gate 1a.
