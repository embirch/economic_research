# Lab notebook · post1 (LL-07)

Dated entries, newest last. One entry per step. Each entry: what was run (script), what it showed
(two lines, numbers), what was decided. Every deviation from the pre-registration is its own entry
beginning DEVIATION, with the reason. Every mistake found is its own entry beginning CORRECTION,
with what changed downstream.

---

## 2026-09-17 · Stage 2 step 2 — pre-registration drafted (P1–P9)

**Read, in full, from the record:** `posts/post1/BRIEF.md` (`8fbffbd`, all twelve sections),
`posts/post1/notes/referee-brief-2.md`, `posts/post1/notes/feasibility.md` (§4 and §7 in full),
`posts/post1/notes/replication.md` (§4 and §5 in full),
`room/steward-2026-09-17-replication-post1.md`, `team/templates/PREREG.md`, and the
`empirical-standards`, `economic-index-data` and `room-protocol` skills. Room notes addressed to the
analyst: nine, all `needs-reply: no`, recorded in `room/analyst-answered.txt`. `reference/` was not
opened. No file owned by another agent was edited.

**Run:** `posts/post1/scripts/01_power_rules.py` — the only script run before the pre-registration
commit, and it loads no data: its inputs are the three standard errors the steward has already
published (`feasibility.md` §4 model (a): 0.151 / 0.148 / 0.154 pp) and the referee's
0.151 / 0.149 / 0.151 pp. Output `posts/post1/data/processed/power_rules.json`.

**What it showed.** The power of each §9(1) rule, three waves conjoined, by exact normal calculation
and by Monte Carlo (400,000 triples, seed 20260917; the two agree to 0.0007 on every owner): H1 (and
H2 by symmetry) reaches 80% at a true |D| of **1.517 pp** and 0.000 at 1.0 pp (0.501 at 1.42 pp);
O-A-or-stronger reaches 80% from **0.517 pp**; step (4)'s clause holds with 80% probability up to
**0.483 pp**. The 41³ grid partition gives every one of 68,921 triples exactly one owner (H1 512,
H2 512, O-A 10,640, H4 3,125, O-B 54,132 — the O-A count matching the referee's 10,640), and the
named problem triples resolve as §9(1) says. Check block passed.

**Decided.** The pre-registration is written on the template's six headings with every referee item
P1–P9 under its own labelled heading or bullet; the §9 rules are reproduced, not redesigned; the
question, title, contribution and hypotheses are untouched. Three places where the brief is silent
are completed and marked in place, with the literal reading reported beside the completed one in each
(P4 leg persistence, P3(b) identified set, P2 declared power). Seventeen confirmatory estimates are
named and counted (3 D + 3 Δ_W + 3 slope + 3 leg (a) + 3 leg (b) + 2 leg (e)), of which eight are the
leg tests. `posts/post1/prereg/prereg.md` goes to the referee; the director commits it.

## 2026-09-17 · CORRECTION — §9(4)'s H4 power figure is step (4)'s clause, not the declaration probability

Item 23 of `referee-brief-2.md` and BRIEF §9(4) state that H4 "fires with 80% joint power at a true
|D| up to ≈ 0.49 pp" (and 0.14 at 0.70 pp). Those are the probabilities that **all three intervals
lie inside ±1 pp** — step (4)'s clause taken on its own, reproduced here exactly (0.483 pp at 80%;
0.133 at 0.70 pp). They are not the probability that **H4 is declared**, because step (3) takes
precedence whenever all three intervals exclude zero with one sign, which is likely at |D| near
0.5 pp. The declared-H4 probability is 0.810 at a true D of 0.32 pp and **0.228 at 0.49 pp**.
Downstream: the pre-registration reports both figures (P2), the brief is left as it stands (it is
frozen and not the analyst's file), and the point is raised for the lead and the referee in
`room/analyst-2026-09-17-prereg-post1.md`. No decision rule changes — the rule is the rule; only its
stated power does.

## 2026-09-17 · CORRECTION (printed precision, not a discrepancy) — 2.8 × 0.148 = 0.4144

`replication.md` §3 and `feasibility.md` §4 print SE 0.151 / **0.148** / 0.154 pp with
MDE(80%) 0.42 / **0.42** / 0.43 pp; on the SE rounded to three decimals the November MDE is 0.4144,
which rounds to 0.41. Any unrounded SE in [0.1482, 0.1518] prints 0.42, so this is the rounding of the
printed SE and not an arithmetic error — asserted as such in `01_power_rules.py`'s check block
(|2.8 × 0.148 − 0.42| ≤ 0.01). Downstream: script 03 recomputes the SE to four decimals and asserts
MDE = 2.8 × SE, so the published figure will carry its own precision.

## 2026-09-17 · Noted for the referee, not changed — two wordings the pre-registration had to resolve

(i) BRIEF §9(3)(b) names "the groups that span the global bottom and top quartile" in words and
"7 / 8 / 6 of 22 span all four" in its parenthesis; `feasibility.md` §4 gives **10 / 10 / 8** groups
containing tasks in both the bottom and the top quartile. The estimand needs only Q1 and Q4, so the
pre-registration takes the 10 / 10 / 8 set as primary and reports the 7 / 8 / 6 subset beside it.
(ii) BRIEF §9(3) does not say in how many waves a leg must fire for H3; the pre-registration mirrors
§9(1)'s persistence for D (a leg must fire in every wave in which it is testable) and reports the
literal any-wave reading beside it. Both are flagged in the room note; neither changes a rule.

## 2026-09-17 · What the data cannot show, recorded as it was met

The per-task automation rate is a usage-weighted blend over countries and cannot be cleaned at this
grain (intersections are global only), so no country statement is available and November's rates keep
a Seychelles share sitting behind 9.039 pp of the top quartile. August publishes no `use_case` facet
at any grain and has no substitute, so leg (e) is a two-wave statement and the work-mix rival is
asserted, not tested, for August. The March-2025 window publishes no counts, so it can carry no
conversation-level interval and no `none` share at task level. The wage is an occupational aggregate
for work that *resembles* the task, and its level does not reproduce Anthropic's published series —
which is why the design is rank-based and no wage level is reported as Anthropic's.

## 2026-09-17 · Stage 2 step 3b — referee's pre-registration items applied

**Read:** `posts/post1/notes/referee-prereg.md` (`f859206`, PASS WITH CHANGES, zero blocking) and
`room/referee-2026-09-17-prereg-post1-verdict.md`. **Applied to `posts/post1/prereg/prereg.md`,
exactly as the referee words them:** item **4** (P4's justification replaced: the persistent-leg rule
is primary for a reason of specification, not of text — the any-wave reading declares H3 with no
composition present in ≈60 / 50 / 27 / 12% of declared gradients at a true D of 0.5 / 0.6 / 0.8 /
1.0 pp against ≤1–2% for the persistent rule); item **5** (H3's "rule against" rewritten as the
complement of the support rule, so H3's space is a partition; "rule for support" now reads "when H1,
H2 or O-A has been declared (a declaration spans the three waves)"); item **6** (new bullet giving
the H3 *rule's* power and false-declaration rate under the referee's covariance model, and the
Interpretation table's last row now says a non-declaration under O-A is "nothing shown" and may not
say composition has been ruled out); item **7** (H1's and H2's "rule against" re-worded to the
every-wave leg language); item **9** (model (a)'s SE stated as a **lower bound** under unmeasurable
within-task dependence); item **11** (new P6 bullet under H1/H2, and the O-A bullet's consequence, for
a C7 sign disagreement: the owner is unchanged, the §12 first sentence carries the non-corroboration
with C7's coverage); item **14** (the work-share covariate listed, with the usage-weighted pairwise
correlation and VIF of wage and work share printed beside it).

**Also applied, as pure wording substitutions with exact text and no rule effect:** item **15(a)**
(O-A's expected-MDE line: O-A-or-stronger 80% from ≈0.5 pp; O-A as declared ≈1.00 near 1.0 pp and
yielding to H1 above ≈1.4 pp — both read off the committed `power_rules.json` curve: O-A 1.000 at
D = 1.0; H1 0.501 against O-A 0.499 at 1.42) and item **15(b)** ("(the figure BRIEF §9(4) quotes)"
on the P2 table's H4-clause row).

**Not applied, and why.** Item **10** (make the D_L − ½D interval the one read for the half judgement,
r_L descriptive with its instability named) and item **15(c)** (state that O-B's probability under a
non-constant true D is not computed) are "could" items with no exact replacement text; both require
new sentences rather than a substitution — item 10 would also shift which interval a reader is
directed to for the half judgement — so both are left for the director's call at the commit or for
Stage 3. No rule, hypothesis, threshold or exploratory test moved. `01_power_rules.py` was not changed
and was re-run: check block passes. "Committed as" left unfilled for the director.
