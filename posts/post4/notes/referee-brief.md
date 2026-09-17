# Referee verdict · post4 (LL-09) · brief · 2026-09-16

Reviewed: `posts/post4/BRIEF.md` at `0e058a1` (`git show origin/main:`), the steward's
`posts/post4/notes/feasibility.md` (`7a083a6`) and `room/steward-2026-09-16-feasibility-post4.md`, the
editor's `room/editor-2026-09-16-brief-post4.md`, the lead's `room/lead-2026-09-16-brief-post4-status.md`,
`room/director-2026-09-16-gate-1a.md`, and post2's first referee verdict (`aa1c9f7`, item 1) as the pairs
ruling requires. Anthropic's definitions and caveats were re-read in the verbatim sections of
`wiki/reports/economic-index-2026-01-report.md` and `-2026-03-report.md` (page references as recorded
there; PDFs not re-fetched — see *What I could not verify*). `reference/` was grepped only for an inherited
framing (none: no reference post touches task success). Room notes between analyst and director were not
read. The uncommitted dead-thread draft at this path was used as a checklist only; every number below is
from my own code in `posts/post4/notes/rederivation/` (two scripts, outputs beside them), run today on the
cache. **No relation between the November success rate and any share change was computed**; the null
simulation uses synthetic success independent of share.

## Verdict

**BLOCK.** Seven blocking items, four of them design changes (items 1–4) and three on text that freezes at
Gate 1b (items 5–7). The brief goes back to the lead once. The question, the thread, the §2 stake, the
construct mapping and every §8 cut are sound, and every steward number the brief carries re-derives
exactly. The block is on what the confirmatory design can deliver: as written its headline test is decided
by a handful of tasks (item 1), its H1 signature is shared by three rivals and its pre-period falsifier
points the wrong way (item 2), its sample is selected on success at the privacy floor (item 3), and its H4
comparison is settled by that floor before any data are seen (item 4).

## Items

**1. The "unweighted" H1 test on the percentage-point outcome cannot deliver the |r| ≈ 0.0569 bound §9 and
§12 promise — blocking (design change).** *Checked:* the distribution of §8 row 1's outcome, "Δ percentage
points on the all-conversation base", over sample B (N 2,427). *Found* (`rederivation/referee_brief_checks.txt`
§6): sd 0.0540 pp, excess kurtosis **592**; the single largest mover carries **46.6%** of the outcome's
sum of squares, the top five 78.2%, the top ten 86.9%, the top fifty 97.0%; the 1,478 tasks with fewer
than 100 November conversations together carry **0.12%**. The variance-effective N of the outcome,
(Σz²)²/Σz⁴, is **4.1**. Because a pp change scales with the task's level, an unweighted pp regression is
implicitly a level²-weighted regression: Kish N with weights s² is **5.9** on the 2,886-task matched panel,
against **88.4** with weights s on the same panel (86.5 on B, the steward's figure) for the usage-weighted
estimate §9 demotes to robustness for having too few effective observations. The
"unweighted" test is therefore *more* concentrated than the weighted one, not less, and the Fisher-z MDE
from 1/√(N−3) says nothing about what it can detect: whatever the nominal N, a Pearson correlation of this
outcome is a statement about five to ten tasks — the largest of which is the coding task "modify existing
software to correct errors…" (−1.8160 pp, 47% of the variance alone), whose fall Anthropic attributes to
coding "shift[ing] to the API" (`economic-index-2026-03-report`, p.8). In log change the same outcome is
well behaved: sd 0.3205, excess kurtosis 1.7, top ten 8.7% of the sum of squares, sd nearly flat in node
size (0.324 for n 15–50, 0.268 for n ≥ 1,000), so each task counts about once and Poisson noise does not
dominate. *Must change* (§8 row 1, §9 test 1, §10, §12): the confirmatory outcome becomes one for which the
stated MDE is informative — the log (or a symmetric relative) change of the task's share — with the pp
change kept as a descriptive display that states its variance-effective N; the MDE for the confirmatory
rule comes from the count-based bootstrap or a permutation null under the chosen outcome and sample rule
(§10 already requires the bootstrap), not from 1/√(N−3); the "top-minus-bottom success quartile" headline
is in the same relative terms; §12's null paragraph is rewritten at the MDE the redesigned test delivers.
Robust standard errors do not repair this: the estimate itself, not its error, is the problem.

**2. H1's signature is shared by three rivals the brief does not test, its pre-period falsifier is
inverted, and the "instrument" identifies nothing about success — blocking (design change).** *Checked* (the
director's three questions): the exclusion logic; whether the design is a correlation dressed as an IV;
whether the composition story that blocked post2 defeats post4's identification.

*(a) The instrument.* The variable of interest, the November success rate, is never instrumented. The
August share instruments the November *level*, a nuisance control, to purge the sampling error that
enters the outcome with the opposite sign — the mechanism the steward measured and I reproduce:
corr(Aug→Nov, Nov→Feb) = **−0.4251** on the 2,140 instrumented tasks (−0.1213 in logs). Against that
sampling error the exclusion logic is defensible (August's sampling noise is independent of November's;
this is the same argument Anthropic makes for its state-convergence 2SLS, `economic-index-2026-01-report`,
pp.16–17, though Anthropic chose an instrument outside the series). Against persistent task trends it is
not: any task trending across the three windows — the coding migration is one — gives August a direct path
to the Nov→Feb change conditional on the November level. It does not need to be defensible, because
nothing about success is identified either way. Entering log s_Nov and log s_Aug both as controls (or
equivalently the pre-period change) is the reduced form that needs no exclusion argument. So: not a
correlation *dressed* as an IV — the brief states exclusion is "arguable, not testable" — but a
conditional correlation *described* in IV vocabulary ("instrumented", "first stage", "exclusion
restriction", "not as an over-identification test": §6 H1, §7.3, §8 row 3, §9 test 1, §10), which invites
the reader to look for an identification argument that is not there. That wording came from my own
shortlist correction 3 (`room/referee-2026-09-16-shortlist-audit.md`); I withdraw it.

*(b) The pre-period falsifier.* §6 H1 makes "absent in the pre-period placebo" part of the signature and
"a pre-period gradient of the same sign and comparable magnitude" a counter-result. That is backwards. The
November label is a task attribute measured once; if it predicts growth, it predicts growth in every
window, and H1's own mechanism — users returning to what Claude completes — operated Aug→Nov as much as
Nov→Feb. A gradient in both windows is consistent with H1; a gradient present *only* in Nov→Feb is what a
February-specific shock (item 2c) looks like. The rule as written would fail a genuine predictor and pass
a shock. What the pre-period regression can do is expose the within-window channel — Aug→Nov growth
changes the November instance mix and hence the November label — so that the main coefficient is read as
incremental to lagged growth.

*(c) Composition.* Post2 was blocked because two anti-aligned inflows produce its correlation with nothing
moving. Post4 needs only one. The February inflow of first-time users brought "an increase in simple
factual questions (e.g., sports outcomes, weather)" (`-2026-03-report`, p.8) — simple work, which the
label rates highest (70% below high-school level vs 66% college, `-2026-01-report`, p.39) — so
high-success tasks gain share with no one returning to anything. The outflow of coding to the API
(software cluster success 61% vs 67% global, Fig 2.2, p.25) shrinks below-mean-success tasks on
Claude.ai — a positive gradient with no return behaviour, and neither H2 nor H3. The published complexity
drift (12.21 → 11.92 years, Table 1.1) is H3. And the label already embeds user selection — "observed
success rates reflect not just model capability but also user judgment about what will work" (p.42) — so
success and share can share a cause with no prediction running between them. **Plainly: the composition
story defeats identification of the behavioural claim in the title and §5 ("people keep bringing",
"predictive validation"). It does not defeat a bounded association: the design can state whether the
November label co-moves with the subsequent share change conditional on level, lagged growth, education
and use-case mix, with the four rivals named as indistinguishable in these aggregates.** H2 bounds the
inflow (a split on the published work share) but does not separate it — returning consumer users
concentrate in the same consumer-like tasks — and the brief already concedes H2 "tests only the
interaction pattern". H1's "signature only it predicts" must lose the word *only*.

*Must change* (§6 H1, §8 row 3, §9 test 1, §10): H1 stated as a conditional correlation of the Nov→Feb
share change (item 1's outcome) with the November `yes` `_pct`, controlling for log s_Nov, log s_Aug (or
the Aug→Nov change) and education-years, on the instrumented subset, with the 2SLS variant as robustness
and the words instrument / first stage / exclusion replaced by "lagged-level controls that absorb the
sampling error in the November level"; the rule that can fail is a partial correlation of the stated
sign above the bootstrap MDE with all controls in; the pre-period regression kept as a *comparison* with
its reading pre-stated for both outcomes (present → the main coefficient is read as incremental to lagged
growth; absent → window-specific, to be reconciled with the February shocks), never as a falsifier;
the four rivals in (c) named in §6 as what a positive coefficient cannot exclude, with item 9's coding cut
as the one that can be tested.

**3. The privacy floor selects the sample on success in small nodes; a minimum-size rule and a synthetic
null that includes the floor are required — blocking (design change).** *Checked:* the steward's remark
that folding error is "correlated with the instrumented level" (§7.2), and what the ≥ 15 rule does to a
node's published `yes` `_pct`. *Found:* a node of n November conversations publishes a `yes` cell only if
yes ≥ 15, i.e. only if its success rate is at least 1500/n — **100% at n = 15, 75% at n = 20, 50% at
n = 30**. Sample B is therefore selected on success for small tasks, and the data show it
(`referee_brief_checks.txt` §7): mean published `yes_pct` **86.34** for n 15–20 (N 76), **73.80** for
21–30 (N 324), 69.64 for 31–50, then flat at 66–68 above 50. A null simulation with true success drawn
independent of share, Poisson counts, binomial `yes`, the ≥ 15 publication rule and Nov∩Feb survival, on
the real node sizes (`rederivation/null_floor_simulation.txt`) reproduces that gradient (88.2 / 76.3 /
68.6 / 67.2 / 66.4 / 66.7 by the same bins) and, with the log outcome and no size rule, gives a **null
correlation of +0.030 (sd 0.019)** — more than half the nominal MDE, positive by construction, and *not*
removed by a level control (+0.033 partialling on log s_Nov). With n_Nov ≥ 30 it is −0.007 / −0.003; at
≥ 50 and ≥ 100 it is zero to three decimals. In pp the artefact is invisible (+0.003 to +0.007) only
because small nodes carry no variance — item 1. Anthropic's own rule for task-level primitive correlations
is a floor of **100**: "When we study the correlation between primitives with the O\*NET, we restrict to
tasks appearing in at least 100 conversations to reduce measurement error" (`-2026-01-report`, fn1,
p.52). The brief's "near-floor sensitivity on `onet_task_count` 15–20" (§8 row 2, §10) is far too narrow.
*Must change* (§8 rows 1–2, §9 test 1, §10): pre-register a minimum November node size for the
confirmatory sample — n_Nov ≥ 30 is the smallest at which both cells can publish (B loses 358 nodes) —
with n ≥ 100 as the required robustness cut and the 15–29 band shown separately; the §10 synthetic
recovery must simulate binomial success counts, the ≥ 15 publication rule and survival, and show that a
zero gradient comes out at zero *under the chosen outcome and size rule*.

**4. H4's confirmatory comparison is decided by the floor before any data are seen, and the numbers the
brief carries for it rest on the zero-imputation §7.2 withdrew — blocking (design change).** *Checked:*
the 86 "labelled exits", 140 "labelled entrants", their means 73.44 / 75.45 and the survivor means
66.60 / 69.25 (§6 H4, §9 test 4). *Found* (`referee_brief_checks.txt` §8): 213 of 282 exits and 264 of 372
entrants have ≤ 20 conversations, so any published `yes` cell among them carries `yes_pct` ≥ 75 by
construction (item 3). Of exits with a `yes` cell (**78**, not 86) **79.5%** have `yes_pct` ≥ 75, mean
**80.97**; of entrants with one (**130**, not 140) **77.7%**, mean **81.25**. The steward's 86 / 140 count
nodes with *any* label and set `yes_pct` = 0 for the 8 / 10 nodes publishing only a `no` cell:
78 × 80.97 / 86 = 73.44 and 130 × 81.25 / 140 = 75.45 reproduce the brief's means exactly. The survivor
means likewise: 66.60 is sample A's 2,524 with the 97 only-`no` nodes at zero (published-`yes` mean on B
is **69.26**); 69.25 is the February `yes_pct` over the same 2,524 with **every** missing value — including
93 nodes with no February label at all — set to zero (published mean **72.66**). Under the brief's own
construct the "signature" *entrants above survivors* (81.25 vs 72.66) is guaranteed by the floor and *exits
below survivors* is contradicted by it (80.97 vs 69.26); the MDEs of 7.70 / 5.98 pp measure nothing about
success, since the comparison is one of node size. *Must change* (§6 H4, §9 test 4, §12): H4 leaves the
confirmatory set. It may survive as a descriptive statement of the censoring (how many marginal nodes
publish `yes`, `no` or neither, against what survivors' size-matched success distribution implies under a
binomial with the ≥ 15 rule) or be dropped; in neither case may the post compare marginal nodes' published
success to survivors'. §9 then has three confirmatory tests and §12's null loses "the sample's own edges
move more than its middle" as evidence about success. The steward should correct
`posts/post4/notes/feasibility.md` §4 H4 (room note to follow from the lead or director; I do not edit it).

**5. The title's "which work people keep bringing to it" is not tested by the design — blocking (title
freezes at Gate 1b).** *Checked:* each title word against what the design measures. "AI's" (the question
says AI), "self-assessed" (p.21; `-2026-03-report` p.18: "Success is Claude's assessment of whether the
conversation was successful"), "success rate", "predict" (temporal precedence), "which work" (an O\*NET
task) — tested. "**People keep bringing**" asserts that the same users return: the unit is a conversation
(fn2, p.36), no release carries a user, tenure or account column (steward, cuts 26/26a), and Anthropic
says of this very window that it "brought many first-time users" (`-2026-03-report`, ch.2 endnote 3,
p.18) and "increasing signups beginning around February brought more casual AI users" (p.6). A share can
grow with no one returning. I confirm the editor's (c). The brief's own §7.1 rule — share growth
"described as what users brought back" — repeats the claim it means to avoid. *Must change* (title, §1,
§7.1, §12): a title with no retention claim — the editor's "which work grows as a share of use", or
"which work people bring it more of" — and the same rule for every "brought back" / "return" in the brief.

**6. §5 overstates in two words that freeze — blocking.** *Checked:* the contribution against Anthropic's
account of the measure. *Found:* "the first **predictive validation** of Anthropic's task-success
primitive" and "how much … share growth a point of self-assessed success **buys**". The p.42 selection
statement (item 2c) means a success–share association can be selection predicting selection and validates
nothing about capability; "buys" is causal (editor's (d)). *Must change* (§5): "the first test of whether
the primitive carries forward information about a subsequent observable, and the size of the
association"; "is associated with". The two-outcome structure of §5 is otherwise right.

**7. §12 has no ending for H2 winning or H3 winning, and its H1 ending restates the untested return —
blocking (Gate 1a: "section 12 written for every outcome").** *Checked:* the four hypotheses against the
three §12 paragraphs. *Found:* the editor is right on H3 — a raw gradient that vanishes once
education-years enters, the image of the 12.21 → 11.92 complexity decline, is the most quotable outcome
and has no sentence; H2 winning (a gradient confined to consumer-like tasks, the image of the February
inflow) has none either; "If H1 fails" describes neither. "If H1 holds" opens "People bring back the work
Claude says it completed" (item 5) and claims "the first evidence that the primitive tracks something
outside its own output", which item 2c allows only as "co-moves with". *Must change* (§12): endings for
H1 holds (with item 2c's concession), H2 wins, H3 wins, null at the redesigned MDE, each a sentence about
Claude, plus the H4 descriptive line if H4 is kept.

**8. §7(4) omits the Anthropic results that most directly bound the framing — should (text).** To add,
quoted in the sweep below: the p.42 selection statement; the fourth report's forecast that "tasks that
prove automatable may graduate from interactive chat to API deployment" (p.54), which predicts a
*negative* gradient on Claude.ai for exactly the tasks the label rates highest; the fifth report's coding
migration with the software cluster's 61% (Fig 2.2, p.25) — a positive gradient with no return; and the
fifth report's statement of this post's headline mechanism as the confound of its own tenure result:
"Those who continue using Claude could be those with tasks that it is distinctly well-equipped to do"
(pp.19–20). §3 or §7 must say the post's mechanism is Anthropic's named survivorship bias.

**9. Coding migration needs a signature the design can see — should (§6, §10).** Without a SOC join the
brief cannot flag Computer-and-Mathematical tasks, and the ten-largest leave-one-out does not cover a
category of hundreds of tasks. Add a pre-specified robustness cut that flags software task statements by
text (a rule such as `software|code|program|debug|database|application`, fixed in the pre-registration)
and state whether the gradient survives it; if not, the finding belongs to post2/post3 and the post says so.

**10. H2 and H3 share half a signature — should (§6).** Consumer-like (low work share) and low-education
tasks overlap; a gradient concentrated in both is claimed by both. State the separating test (work-share
split within education terciles, or the education coefficient within the work-dominant half) or state that
the two are not fully separable on these columns.

**11. Seychelles is abusive traffic, not a departed geography — should (§7.3(c), §10).** "We exclude the
Seychelles from all geographic analyses because a large fraction of usage we saw during the sampling dates
was abusive traffic" (`-2026-01-report`, fn5, p.37). Its 6,790 conversations in the largest task (11.37%,
reproduced) sit in the November regressor's numerator and denominator with labels of unknown meaning.
Name the reason; it strengthens the netted run and adds a sentence to the regressor's limitation.

**12. The confirmatory N is not one number — should (§6 H1, §9 test 1, §10, §12).** §6 says the instrument
is "available for 2,140 of the 2,524"; §9 runs "sample B (2,427 tasks; instrument for 2,065)"; §12 says
"across the 2,427 tasks"; the placebo runs on the 2,140 of sample A. A regression with an instrumented or
lagged level control runs only where the lag exists — 2,065 on B, MDE 2.8/√2,062 = 0.0617 before item 3's
size rule. Fix one confirmatory sample and carry its N and MDE through §9, §10 and §12.

**13. The success–education correlation is quoted on the wrong construct — should (§6 H3, §7.4, §9
test 3).** The brief's −0.0703 / −0.1752 "across the 2,524 tasks" reproduces only with the 97 only-`no`
nodes of sample A set to `yes_pct` = 0 (the imputation §7.2 withdrew). On sample B, published `yes` only,
the unweighted correlation is **−0.1492**. Still weak, but the number in the brief is attached to a
construction the brief rejects; restate on B (the steward's note carries the same figure and should be
corrected).

**14. Coordination with post2 on the shared series — should (§4).** If post4 adopts a relative-change
outcome (item 1) while post2 keeps percentage points, the two posts no longer share one series in one
metric; §4 must say which metric each uses and why. The Super Bowl exposure and the shared Nov→Feb
Claude.ai series are otherwise named in §4 and §7 as the pairs ruling requires.

**15. Three data facts for the construct paragraph — could.** (a) The privacy rule is "fewer than 15
conversations and 5 unique user accounts" (fn1, p.36), so the folding rule has a second trigger the
aggregates cannot show. (b) The judge is Sonnet 4.5 (fn7, p.18) reading transcripts produced by whatever
model the user was on; "self-assessed" is Anthropic's own gloss (p.21) for an Anthropic model judging
Claude's transcripts, and the brief should say so once. (c) `platform_and_product` reads "Claude AI (Free
and Pro)" in the August and November files and "Claude AI (Free, Pro, and Max)" in February; `data/ATLAS.md`
§Components records the November label as wrong (the sample is Free, Pro and Max per fn1, p.17); whether
the August instrument wave includes Max is not recorded and should be stated as unknown.

**Checks that pass.** Each hypothesis has a stated counter-result (§6) — H1's needs rewriting per item 2,
H4's is void per item 4. Contribution stated for both outcomes (§5), wording per item 6. §2 is something
an economist would care about: the success-adjusted 1.8 → 1.2 / 1.0 pp revision (p.48; p.38's "about 1.0"
correctly separated as the API figure) and effective coverage (p.43) rest on this label; the editor's (a)
stands. No framing is inherited from `reference/`; the IV wording is inherited from my own shortlist
correction, withdrawn in item 2. §8 matches the steward's column-level confirmations, every caveat
carried: three categories, `yes` `_pct` as published, inert threshold moved, 2,140 / 2,065, 1,782 work
split, 1,686 / 1,428 API leg, Seychelles netting, "91.95 of 100", "19.4% of all conversations, 20.9% of
named". The steward's MDEs and N_eff are carried (0.0569; 0.31 / 0.25; 86.5 / 128.2; 7.70 / 5.98) — but
§12's null is not deliverable at 0.0569 (item 1) and the 7.70 / 5.98 comparisons are void (item 4). §9
states the exploratory allowance (three tests, barred from the headline). The question says AI; findings
and axes say Claude. Anchor verified: Fig 2.2 p.25 task success 67%, N = 999,875; p.26 67% vs 49%.

## Independent re-derivations

Not the results stage; the steward numbers the brief carries were re-run from the raw files with my own
code, `posts/post4/notes/rederivation/referee_brief_checks.py` (output `.txt`), independent of
`data/replication/post4_feasibility_checks.py`. **Match:** global `task_success` `yes` `_pct` 66.9060,
`_count` 999,875 (Nov Claude.ai); 69.9385, 1,000,000 (Feb); 49.3638, 971,525 (Nov API). Panel 2,886 matched,
282 Nov-only, 372 Feb-only, 2,282 in August too. Samples A / B / C = 2,524 / 2,427 / 1,553; instrument
2,140 / 2,065 / 1,493; B mass 91.9470 of 100 = 98.32% of named; instrumented A mass 98.60%. Kish N_eff
87.1 / 86.5 / 80.4 (Nov), 129.6 / 128.2 / 118.2 (Feb); MDE 0.0558 / 0.0569 / 0.0711 nominal, 0.3052 /
0.3064 / 0.3184 weighted. First stage 0.9167 (levels), 0.8753 (logs). Aug→Nov sd 0.08373; Nov→Feb sd
0.05297; corr −0.4251. Ten largest 19.4410 pp = 20.9% of named. 971 folded nodes in A, median 22.73 pp,
max 48.28. Partition 3,168 of 3,168 named. Education `_mean` 2,524 of 2,524, range 1.009–17.512; `work`
published 1,782, medians 59.91 / 41.37. Seychelles 67 nodes, 24,715 = `usage_count`, 0 February rows; 65
in A, 23,173; largest task 6,790 / 59,739 = 11.37%; −1.8160 → −1.2712 pp under the steward's convention
(netting numerator and base; −1.1370 if only the numerator is netted). **Discrepancies, both a matter of
construct:** the H4 means (item 4) and the success–education correlation (item 13) reproduce only under
zero-imputation of folded `yes` cells. **New numbers** (items 1, 3, 4): outcome kurtosis and concentration;
`yes_pct` by node size; the null simulation with the floor (`null_floor_simulation.py`, `.txt`, seed
20260916, 400 draws per cell).

## Assumptions sweep

**(1) Value judgement in the framing — needs a design change (title; item 5), otherwise handled.**
"Self-assessed" is Anthropic's own qualifier and handles "success"; the title-form paragraph and §7.1 do
this well. "Keep bringing" is not handled: it asserts return, which no column observes and which
Anthropic's account of this window contradicts as a default reading. §7.1's own rule ("what users brought
back") must become "what grew as a share of conversations".

**(2) Construct mapping — handled, with two additions newly flagged.** Verbatim, `economic-index-2026-01-report`,
2026-01-15, p.21: "Task success measures Claude's assessment of whether Claude completes tasks
successfully." Prompt, Table 2.1, p.20: "Did the Assistant complete the task provided by the User
successfully? … Yes … No". Validation, p.22: the nine classifiers are "directionally accurate even if they
may deviate somewhat from human ratings"; no statistic. `-2026-03-report`, 2026-03-24, p.18: "Success is
Claude's assessment of whether the conversation was successful." The brief's mapping to the published
`yes` `_pct` of `onet_task::task_success`, with `not_classified` as the folded sub-15 residual, is correct
and I verified the partition. What the label measures: one binary judgement per transcript, by Sonnet 4.5
(fn7, p.18), of whether the Assistant completed what the User asked — no human rating, no user feedback, no
outcome. What "self-assessed" adds: an Anthropic model judging Claude's transcripts. *Newly flagged:*
(a) by Anthropic's own account the label is a joint product of capability and user selection (p.42, quoted
in (4)), so regressor and outcome share a cause; (b) the ≥ 15 cell rule censors the label upward in nodes
under 30 conversations (item 3). *Direction of the sign:* positive under H1, H2 (casual inflow toward simple
work), H3 (simplicity drift), coding migration off Claude.ai, and the floor artefact; negative under the
graduation forecast (p.54) and the fifth report's Table 2.1 (returning users bring higher-education,
higher-success tasks — a return-driven February would move share toward harder work). The brief states
the last two; the migration and graduation mechanisms must be added.

**(3) Composition and selection — needs a design change (items 3 and 4), otherwise handled.** Units are
conversations, not users (fn2, p.36); Claude.ai users are the Free, Pro and Max tiers (fn1, p.17), the API
leg is enterprise and Claude Code traffic (`-2026-03-report`, fn1, p.11); occupation is not used (no SOC
join) and the brief says so. Mixes that produce the pattern without the mechanism: the brief names the
Super Bowl first-time-user inflow, winter breaks and Seychelles. *Newly flagged:* (a) the same week is
Super Bowl week and Anthropic attributes the task-value fall to "an increase in simple factual questions
(e.g., sports outcomes, weather)" (p.8) — an event-driven demand shock to specific simple, high-success
tasks, not absorbed by `use_case` or education controls; the leave-one-out and item 9's text cut speak to
it; (b) selection into the published sample by success at the floor (item 3) and of the marginal nodes by
success (item 4), both mechanical; (c) the coding outflow to the API (item 2c); (d) Seychelles is abusive
traffic (item 11). Task churn between waves is correctly handled as floor-crossing (absent ≠ zero).

**(4) Anthropic's own results that cut against or bound the framing — newly flagged; text change (item 8).**
"In our data, users choose which tasks to bring to Claude. This means observed success rates reflect not
just model capability but also user judgment about what will work, the cost of setting up the problem for
Claude, and the expected time savings if the task succeeds" (`-2026-01-report`, p.42). "As AI capabilities
advance, Claude's success rate may increase … and tasks that prove automatable may graduate from
interactive chat to API deployment" (p.54). "When we study the correlation between primitives with the
O\*NET, we restrict to tasks appearing in at least 100 conversations to reduce measurement error" (fn1,
p.52). "Those who continue using Claude could be those with tasks that it is distinctly well-equipped to
do. But carefully controlled regressions rule out simple versions of this confounding" (`-2026-03-report`,
pp.19–20) — the post's mechanism is the confound Anthropic names and claims to rule out within task.
"a decrease in coding as it shifts to the API" (p.8) with the software cluster's 61% success against 67%
(Fig 2.2, p.25). The brief's existing items — the 70% / 66% education gradient (p.39), Table 1.1's
12.21 → 11.92, Table 2.1's tenure profile, the Super Bowl and winter-break endnotes — are correctly quoted.

## What I could not verify

- Anthropic's PDFs were not re-fetched; every quotation above is from the verbatim sections of
  `wiki/reports/economic-index-2026-01-report.md` and `-2026-03-report.md`, whose page references were
  checked against the PDF by the post2 review earlier today. The brief's p.21 and Table 2.1 quotations match
  the wiki's verbatim blocks character for character.
- The Institute agenda `Share 1` line, the Claude Code paper's judged/verified distinction, Tomlinson et
  al.'s r > 0.75 and the long-list's r = 0.64 were checked against `wiki/reports/` and `programme/` only.
- Whether the 5-unique-account trigger (fn1, p.36) ever folds a cell of ≥ 15 conversations cannot be told
  from the aggregates; the steward's finding that every published cell is ≥ 15 is consistent with either.
- Whether the August 2025 Claude.ai sample includes the Max tier (its file label says "Free and Pro").
- The API-leg counts 1,930 / 1,686 / 1,428 and the steward's Feb Kish figures beyond B were not re-run.
- I computed no relation between the November success rate and any share change, and the null
  simulations use no real success data; the pre-registration must state the same.
