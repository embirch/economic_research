# Referee verdict (second read) · post1 (LL-07) · results, revised · 2026-09-17

Second read, narrow by design. Read only: `posts/post1/notes/referee-results.md` (the first verdict, at
`1b621c0` — PASS WITH CHANGES, zero blocking), `room/referee-2026-09-17-results-post1-verdict.md`,
`room/analyst-2026-09-17-results-post1-revised.md`, `git diff 1b621c0 698a2f1 -- posts/post1/` (the whole
change set, +1,813 / −106 over 18 files), the new CORRECTION block of `posts/post1/notes/lab-notebook.md`
(lines 477–645), `posts/post1/data/processed/results.json`, `posts/post1/outputs/figures.json` and the
`posts/post1/outputs/checks/*.out.txt`. The brief, the pre-registration, `notes/feasibility.md` and
`notes/replication.md` were **not** re-opened; Anthropic's sources were not re-read. No number was
re-derived except the ones the revision moved or introduced, and those only from files already in the
record. **No statistic was computed from the release cache** — the cache is not present in this session
(`posts/post1/data/` holds `processed/` only), which is also the limit on what could be re-run (see "What I
could not verify"). Matching of the first verdict's exact-text items was done on whitespace-normalised
strings, so a line break inside a quoted sentence counts as a match and a changed word does not.

## Verdict

**SIGN OFF** (PASS). Gate 2b can be recorded.

All eleven "should" items — 3, 6, 7, 8, 9, 10, 11, 13, 14, 17, 18 — are applied, nine of them **in the
referee's exact words**, and in every case the defective text is gone. The two that are not verbatim are
equivalent and preserve the number and the rule: item 11 is a computation, not a sentence, and its three
estimates land on my supplement's figures to four decimals including all six interval bounds; item 14
substitutes "this leg's set" for "the work-dominant set" because the sentence is now a template that also
had to serve February, and it fixes February's identical defect, which item 14 did not name. All four
"could" items are addressed: 12, 15 and 16 are applied as written; 5's suggestion (10,000 trials) is
superseded by a better fix the analyst found himself.

The guard is clean, and mechanically so. A leaf-by-leaf comparison of `results.json` at `1b621c0` and
`698a2f1` (490 leaves added, **0 removed**, 32 existing leaves changed) shows that **the only numbers
anywhere in the file that moved are the eighteen placebo leaves** — permutation mean, sd, band and
two-sided p in three waves. Not one estimate, standard error, interval bound, MDE, count, mass share or
fact value changed: D, Δ_W, the slope, all eight legs and their SEs, the corrected-rule D's, the declared
owner (**O-A** under both quartile readings) and the H3 declaration (**declared**, 6 of 8, legs (a) 3/3
and (b) 3/3, (e) 0/2) are identical to the last decimal to the figures I verified in the first read. No
`prereg_rule` string changed. The placebo's movement is within Monte Carlo error and touches no decision
rule. `claims.md` carries no stale number.

Three things are left for later, none a condition of sign-off: a fifth prose mis-transcription in the
notebook (item 17's own CORRECTION entry, below), two residual estimates that lack an SE under empirical
standard 6 (§(f)), and two stale "4.93%" references — one of them in my own first verdict (§(c)).

## Items

### (a) The eleven "should" items

**1. Item 3 — the boundary occupation is named. APPLIED, exact string, with a computed block beside it.**
`facts.quartile_boundaries_<wave>.boundary_occupation` reads, in all three waves, `"15-1199 Computer
Occupations, All Other ($90,270 ÷ 2,080 = $43.40/hr)"` — the verdict's string character for character.
`02_build.py` additionally computes `boundary_occupations`, which records for each of the three boundaries
the annual salary, the number of detailed codes sitting exactly on it and their titles. The arithmetic of
every entry reproduces the committed quartile bounds: 53,630 / 2,080 = 25.78365, 73,960 → 35.55769,
72,510 → 34.86538, 71,650 → 34.44712, 49,930 → 24.00481, 90,270 → 43.39904. The third boundary is
**thirteen** `15-1199.xx` codes at one salary against 1–4 codes at the other two, which is the fact the
item existed for: the tie sits inside the coding family. `boundary_tie_mass.b3_43.40` (99 / 106 / 111
tasks; 10.60 / 8.36 / 7.95 pp) and `q4_mass_from_boundary_tie` (7.33 / 4.93 / 6.14) are untouched.
*One caution for the draft:* the `titles` list is truncated at four entries (`02_build.py`, `[:4]`) while
`detailed_codes` reads 13, so a reader of `results.json` must not take the four titles for the whole set.

**2. Item 6 — the fourth mis-transcription. APPLIED.** A dated CORRECTION entry
("*2026-09-17 · CORRECTION (item 6) — the fourth mis-transcription: leg (b) identifies 10 / 10 / 9 groups,
not 9 / 9 / 9*") records that the `05_legs.py` entry and open question (ii) of the close said
"9 / 9 / 9 … 71–76%" and that the record has always been **10 / 10 / 9** at **80.04 / 80.31 / 75.52%**, and
states that no estimate moves because the leg was computed from the identified-group mask itself. It goes
one step further than the item asked, correctly: the recorded expectation in `feasibility.md` §4 is
10 / 10 / 8, so the divergence from the record is February only (9 against 8), and open question (ii) is
to be read that way. `results.json` confirms `coverage.n_identified` = 10 / 10 / 9 and
`identified_mass_share_q1_q4` = 80.0379 / 80.3139 / 75.5174, unchanged by the revision.

**3. Item 7 — figure 3's group counts. APPLIED, verbatim.** The caption now reads "…over the **ten
(August, November) or nine (February)** major groups that hold analysis-set tasks in both the global
bottom and the global top quartile, each group weighted by its usage mass in those two quartiles; the
other **twelve or thirteen** groups are reported as not identified, never as zeros." The verdict's
sentence, word for word; "the nine major groups … the other thirteen groups" is gone. The notebook entry
also records the reason it slipped through — script 09's verifier checks numerals only, so a word-number
in a caption passes it — which is the right thing to have written down.

**4. Item 8 — figure 4 and February's Δ_W. APPLIED, verbatim.** "**Weighting the published automation
share by the wage of the work moves it by less than a fifth of a point in two windows and by eight tenths
of a point in the third, and not in the same direction as the quartile gap in two of the three.**" The
verdict's sentence exactly. Checked against the data it describes, which did not move: Δ_W = −0.0222 /
+0.8352 / −0.1466, so "less than a fifth" is true of August and February and "eight tenths" of November,
and D is positive in all three while Δ_W is negative in two — "two of the three" holds.

**5. Item 9 — figure 1's bold sentence. APPLIED, verbatim.** "**In all three Claude.ai windows the
delegated share is higher on top-quartile than on bottom-quartile tasks; the difference clears a
percentage point in two windows on the pre-registered quartile rule and in none once the boundary wage is
shared, and it does not clear a point in every window under either rule.**" Word for word; the garbled
clause is gone. All three captions are identical in `outputs/figures.json` and in `results.json`'s
`figures` block, and their word counts (371 / 202 / 317 / 213) are exactly what the committed
`09_results_and_figures.out.txt` prints — see §(e).

**6. Item 10 — the second wage source is the SOC-15 exclusion in disguise. APPLIED, verbatim, and
recomputed rather than pasted.** `06_robustness.py` now derives the diagnostics from the build table
(`c7_diag`, five shares) and `09` lifts them into `facts.C7_sign_agreement`. All four triples the item
specified reproduce my own to the printed precision: `c7_share_of_soc15_analysis_mass`
10.888 / 10.489 / 11.646 (mine 10.9 / 10.5 / 11.6); `c7_share_of_q4_mass` 26.358 / 27.670 / 31.810
(26.4 / 27.7 / 31.8); `soc15_share_of_c7_priced_q4` 7.562 / 6.422 / 5.913 (7.6 / 6.4 / 5.9);
`c7_leg_a_retained_fraction` 0.9685 / 0.9267 / 0.9811 (identical). Two further triples are right too:
`soc15_share_of_c7_q4_redrawn` 8.545 / 7.004 / 6.347 (mine 8.5 / 7.0 / 6.3) and `soc15_share_of_c6_q4`
73.065 / 71.263 / 65.463 (73.1 / 71.3 / 65.5). The `rob_C7_*` verdict is the verdict's exact sentence in
all three waves — "…BLS-EP (SOC-2018) does not price the renumbered computer occupations, so C7's top
quartile is 92–94% non-coding and this rebuild is the Computer & Mathematical exclusion of leg (a) on
55–62% of the mass, not an independent second source; the owner is unchanged" — and the old "C7's coverage
… is the reason it is not decisive" string is gone from all three. A `mechanism` line states it in prose.
The P6 obligation on the post's first sentence is recorded in the notebook.

**7. Item 11 — the P3(b) all-four side-estimate. APPLIED, and it matches my supplement exactly.**
`05_legs.py` now takes a `subset` argument and `leg_row` computes the side-estimate whenever it builds the
primary leg (b). `results.json`, `leg_b_<wave>.estimates.D_L_all_four_subset`:

| wave | analyst | mine (first verdict) |
|---|---|---|
| Aug | −4.054133 [−4.570322, −3.537944], SE 0.263367 | −4.0541 [−4.5703, −3.5379] |
| Nov | −1.794014 [−2.351962, −1.236065], SE 0.284673 | −1.7940 [−2.3520, −1.2361] |
| Feb | −6.085129 [−6.561527, −5.608731], SE 0.243065 | −6.0851 [−6.5615, −5.6087] |

Every point estimate and all six interval bounds agree to the four decimals I printed. `fired` is `true`
in all three, so the leg fires under both readings and H3's declaration does not depend on which
identified set is used — as the item said it would. `n_groups` 8 / 9 / 8, `mass_share_q1_q4` 75.42 /
79.39 / 74.74, and `r`, `se`, `mde` are carried. A notebook entry records it. *Carried to the draft:* the
realised all-four counts are 8 / 9 / 8 against the pre-registration's expected 7 / 8 / 6 (within the
check block's ±2 tolerance, and unchanged by this revision), so a post that cites the subset must say
8 / 9 / 8.

**8. Item 13 — the Δ_W verdict string. APPLIED, verbatim.** `verdict_DW` now branches. August reads
"contains zero; |Δ_W| = 0.0222 pp, below the separate 1 pp materiality line, so the weighting of a
published automation share is small and, in this window, of undetermined sign" — the verdict's sentence
exactly. "signed and small, never wrong" survives only on the excludes-zero branch, which is where I put
it and which is correct for November and February; `claims.md` already forbids the post from generalising
it across windows.

**9. Item 14 — leg (e)'s non-firing verdict. APPLIED; one word not verbatim, equivalent, and the same
defect fixed in February too.** November now reads "did not fire on the point estimate; D_L retains 0.50
of D and the contrast D_L − ½D is +0.02 [-0.33, +0.37] pp, so whether **this leg's set** retains more or
less than half of D is undetermined at this precision; not composition excluded". The only departure from
my text is "this leg's set" for "the work-dominant set", forced by the string now being a template; every
number and the whole of the rule statement is mine. Both figures check against the unmoved data:
r = 3.7160 / 7.3854 = 0.5031 and D_L − ½D = +0.0233 [−0.3264, +0.3730]. The wrong null sentence ("nothing
bigger than the MDE of 0.6058 pp is shown") is gone. February, which item 14 did not name but which
carried the identical defect, now reads "…D_L retains 4.17 of D and the contrast D_L − ½D is +2.46
[+2.02, +2.89] pp, which excludes zero, so D_L keeps more than half of D at this precision" — and
4.174 = 2.7916 / 0.6689 and +2.4571 are right. This is the item applied and its class closed.

**10. Item 17 — P2's constant-D assumption. APPLIED; the two numbers it turns on are re-derived and
right; the notebook's prose for it is not.** `facts.rule_power.notes` now says that "every P2 probability
assumes a **constant** true D across the three windows … so that assumption is falsified by the data:
none of these probabilities is the probability of this outcome, and no probability under a non-constant
true D has been computed. This resolves the referee's carried item 15(c)." A new fact,
`facts.between_window_dispersion_of_D`, carries `value` 3.6888119, `mean_within_window_se` 0.1415547 and
`ratio` 26.0593, with the consequence spelled out. These are the only derived numbers the revision
introduced that I had not already computed, so I re-derived them from the three D's and three SEs in
`results.json`: SD (ddof = 1) of {1.3836455, 7.3854128, 0.6688743} = 3.6888119 and the mean of
{0.1444212, 0.1403538, 0.1398891} = 0.1415547, ratio 26.0593. Exact.
**But the notebook is wrong about it.** `lab-notebook.md` line 616 (item 17's own CORRECTION entry) and
the analyst's room note both read "**3.6928 pp**"; the computed value is **3.6888 pp**. Nothing citable
carries the wrong figure — `results.json`, the check output and `claims.md`'s "SD 3.69 pp" are all right —
so this is not blocking, but it is a fifth prose mis-transcription, in the entry that resolves the fourth.
**For the analyst:** one dated line correcting 3.6928 → 3.6888 in `notes/lab-notebook.md`.

**11. Item 18 — the realised generalisation bound. APPLIED.** `facts.generalisation_sentence` keeps
`value` 20.1578 and gains `realised_mde_by_wave` [14.0720, 20.1578, 16.1181], `prereg_mde_by_wave`
[12.5, 17.4, 16.1] and a `sentence` field: "the post's generalisation sentence carries the **realised**
bound: a design that resamples tasks resolves nothing below about fourteen to twenty points — never
'about twelve', which was the pre-registered figure". Figure 1's caption already said "about 14 to 20"
and still does. `claims.md` sentence 7 and its forbidden-sentence counterpart already match.

### (b) The four "could" items

**12. Item 12 — the numbers the post might cite. APPLIED in full.** Seven new `facts` keys
(`X7_none_node_variant`, `A1_allocation_variants_of_the_legs`, `C7_legs`,
`leg_e_substantive_cell_denominator`, `leg_table_2010_grouping`, `composition_of_the_top_quartile`,
`seychelles_worst_case_bound`), taking the file from 29 facts to **37**; the test count is unchanged at
60 and the figure count at 4. Every figure the item listed is present and matches what I derived: X7's
wave share 51.2001 → 51.7424 with D unchanged; leg (a) under A1 equal-split / modal −13.713 / −14.070,
−11.075 / −11.400, −12.374 / −12.617; the C7 legs; leg (e) on the substantive denominator +3.8538 /
+2.7392, not firing; the 2010 leg table, 6 of 6 fired, same H3 verdict; and the four referee-derived
composition figures — the two "modify existing software to correct errors…" tasks at **6.527 / 8.541 /
5.980** pp of Q4 (**11.399 / 12.214 / 8.826** pp with "write new programs…" third), the within-SOC-15
contrast **−0.1421 [−0.7180, +0.4339] / +6.4656 [+5.8658, +7.0654] / +0.8039 [+0.1631, +1.4447]** pp, and
the residual Q4 after the SOC-15 exclusion at **286 / 327 / 355** tasks, **6.101 / 6.470 / 7.775** pp,
Kish **97.95 / 85.46 / 83.25**, share **38.69 / 34.75 / 36.02** against a residual Q1 of **51.72 / 45.22 /
47.91**. The Seychelles bound is the one I would single out: `06_robustness.py` implements the algebra from
scratch (p_clean = (p − s·p_SC)/(1 − s), p_SC = 1 on Q4 and 0 on Q1, weights netted) and returns
**+4.5038** pp against my +4.50 — an independent reproduction of my supplement, not a copy of its number.
Each new fact is labelled description or bound and says it is in no decision rule; no new test was run,
and the test counts confirm it.

**13. Item 15 — the two expectation-assertions. APPLIED.** `03_headline.py`'s
`assert abs(dw["coef"]) < max(1.0, 0.5*abs(D))` is now a print, with the reason in a comment that says
what the item said: a Δ_W larger than the arithmetic predicts would have been a finding, not a bug. The
printed ratios (−0.0160 / +0.1131 / −0.2192 pp per point of gap) appear in `03_headline.out.txt` and match
`claims.md`'s forbidden-sentence figures exactly. `05_legs.py`'s "SOC-15 is the largest leave-one-out
mover" assertion is likewise a print of the three largest movers per wave, in `05_legs.out.txt`. Every
other assertion in both scripts is retained, and both check blocks still pass.

**14. Item 16 — SE and MDE on citable estimates. APPLIED as worded, with two residuals under the
standard.** All three groups the item named now carry both: `exp_a_api_surface` slopes (and a new
`Delta_W_<wave>` term beside each D), `exp_c_jobzone`'s `D_<wave>`, and every `rob_*` Δ_W (W1 equal-split
×3, W1 modal ×3, C7 ×3). I checked the additions are computed, not pasted: across the whole file **186
estimates carry both `se` and `mde` and every one satisfies mde = 2.8 × se to 1e-9; 194 carry both `se`
and `ci` and every one satisfies ci = coef ± 1.959964 × se to 5e-6**, with zero exceptions. Residuals, for
the draft stage rather than now: `desc_slope_work_share_<wave>` carries `ci` (and for two of three slopes
an `mde`) but no `se`, and `claims.md` sentence 21 permits the post to cite it; and
`rob_fourth_window_<wave>.D_classified_weights` carries a `ci` only. Neither was named by item 16;
`desc_pattern_shares_*` is the same shape but `claims.md` routes pattern claims to
`exp_b_pattern_split`, which does carry SEs.

**15. Item 5's suggestion (10,000 trials). NOT APPLIED, and rightly superseded.** The analyst found the
real problem instead: see §(c). The trials stayed at 1,500 for the recovery test and 10,000 for the
placebo, and DEVIATION 3's widened ±2 pp size band stays logged, which is correct — but note that the
reproducible size, 4.87%, is inside the **registered** ±1 pp band, so the deviation is no longer load
bearing. The check block's tolerance (`abs(size − 5.0) ≤ 2.0`, `04_second_implementation.py` L798) is
unchanged and passes with a margin of 0.13 pp.

### (c) The extra CORRECTION: the seeded placebo made reproducible

**16. Legitimate, correctly diagnosed, and it explains an inconsistency I missed.** `permutation_null`
built its group index from `set(group)`, whose iteration order over strings differs between processes, so
the per-group permutations consumed the seeded stream in a different order each run; `sorted(set(group))`
fixes it. The notebook entry states the cause, the fix, that two consecutive runs now agree exactly, and
that every other loop over group labels was already sorted — which is why nothing else in the pipeline is
run-dependent, and which the leaf comparison in §(d) confirms from the other side.

This also explains a discrepancy in the pre-revision record that I did not catch: `lab-notebook.md` lines
249 and 280 recorded the permutation size as **4.93%** while the committed
`04_second_implementation.out.txt` said **5.33%**. Both were true of some run. There is now one value,
**4.87%** (73 of 1,500), in `second_implementation.json`, the check output and
`facts.synthetic_recovery.source_check`. Moves of 0.47 pp against a Monte Carlo SE of 0.56 pp.

**Within Monte Carlo error, and no decision rule touched.** The three two-sided p's move 0.8313 → 0.8304,
0.6712 → 0.6689 and 0.9459 → 0.9494. The p is (1 + #{|perm| ≥ |obs|}) / (B + 1) at B = 10,000, so its
Monte Carlo SE is 0.0038 / 0.0047 / 0.0022: the three moves are 0.24, 0.49 and 1.6 SEs. The band means
move 0.031 / 0.060 / 0.011 pp against Monte Carlo SEs on the mean of 0.033 / 0.045 / 0.037 pp. The
observed D is unchanged in all three waves and still sits inside the band in all three; the verdict
sentence is the same but for the quoted p; the placebo is in no decision rule and is not cited by
`claims.md`. Nothing else in the file moved (§(d)).

**Two stale references, neither citable.** `lab-notebook.md` lines 249 and 280 still read "4.93%" and the
new CORRECTION does not name them — *for the analyst:* add the cross-reference. And my own
`referee-results.md` items 5 and 20 quote "4.93%", which is now superseded by 4.87% — **mine to fix**, and
I record it here rather than editing the first verdict, so that the two reads stay separable.

### (d) The guard: did any headline number move?

**17. No. Verified leaf by leaf, not by eye.** I flattened `results.json` at `1b621c0` and at `698a2f1`
to leaf paths and compared: **490 leaves added, 0 removed, 32 existing leaves changed.** Of the 32, the
only numeric changes in the entire file are the **eighteen placebo leaves** (mean, sd, band coef and two
band bounds, two-sided p, in three waves). The other fourteen are strings: `generated`; the five verdicts
the items required (`DeltaW_aug2025`, `leg_e_nov2025`, `rob_C7_×3`); `leg_e_feb2026`'s verdict (item 14's
class, §(a)9); the three placebo verdicts (the quoted p); `facts.synthetic_recovery.source_check` (the
4.87%); and the three captions. **No `prereg_rule` string changed anywhere.** The added leaves fall only
in the locations items 3, 10, 11, 12, 16, 17 and 18 specify.

Read directly from the committed `results.json`, against the first verdict's table: D +1.3836455 /
+7.3854128 / +0.6688743 with SEs 0.1444212 / 0.1403538 / 0.1398891; D on the corrected rule +0.5434 /
+7.1793 / +0.3387; Δ_W −0.0221835 / +0.8351685 / −0.1466288; slope −0.0507177 / +1.7657102 / −0.2843058;
leg (a) −13.0318575 / −10.4701482 / −11.8951838 (SEs 0.2225512 / 0.2093665 / 0.1944636); leg (b)
−4.1988994 / −1.8716301 / −6.2168875 (SEs 0.2604871 / 0.2821091 / 0.2425653); leg (e) +3.7160106 /
+2.7915683; MDEs 0.4044 / 0.3930 / 0.3917; Kish 94.4 / 83.4 / 125.7 and Q4 10.64 / 8.87 / 16.45;
`facts.declared_owner` **O-A** and `facts.declared_owner_corrected_quartile_rule` **O-A**;
`facts.H3_declaration` **true**, `k_of_8_fired` **6**, legs firing in every testable wave **a, b**,
literal rule agreeing; `facts.owner_under_robustness` O-A with the same eight cuts and the same three
moves (X3 → H1, W1 modal → O-B, X5 >10% → O-B). Every one identical to what I verified at `1b621c0`.

**18. The check outputs correspond to the committed scripts — proved for 09, matched line by line for
02–06.** I extracted `698a2f1` to a scratch tree (`git archive`, so the shared tree was never written)
and ran `posts/post1/scripts/09_results_and_figures.py` there. It exits 0, the check block passes, and the
regenerated files are **byte-identical** to the committed `results.json` (modulo the `generated`
timestamp), the committed `outputs/figures.json`, and the committed
`outputs/checks/09_results_and_figures.out.txt`. That proves the committed `results.json` and captions are
what the committed script 09 produces from the committed upstream JSONs — including the four caption word
counts, 371 / 202 / 317 / 213. Scripts 02–06 cannot be re-run in this session (no cache), so for those I
matched every print statement added in the diff to its line in the committed `.out.txt`: 03's three Δ_W/D
ratios; 04's "size 4.87%"; 05's three all-four side-estimate lines, three composition lines and three
mover lines; 06's three C7 diagnostic lines, the X4 Seychelles bound line and the three re-drawn
permutation lines. All present, all carrying the values the 09 re-run independently confirms are in
`legs.json` and `robustness.json`. Every check output ends `CHECK BLOCK PASSED`.

### (e) `claims.md`

**19. No claims.md number is stale.** I grepped the keys `claims.md` cites and compared them to the
committed `results.json` wherever the diff touched the key. Every one holds: sentence 4's
`boundary_tie_mass.b3_43.40` (99 / 106 / 111; 10.60 / 8.36 / 7.95) and `q4_mass_from_boundary_tie`
(7.33 / 4.93 / 6.14); sentence 6's "SD 3.69 pp against mean SE 0.142" (now also a fact, 3.6888 / 0.14155,
ratio 26.06); sentence 7's 14.07 / 20.16 / 16.12 and `facts.generalisation_sentence` 20.16; sentence 8's
X5 −4.5815 and X4 +6.5463; sentence 9's modal-holder −0.1701 and the owner moves; sentence 12's slopes;
sentences 14 and 15's legs with `n_identified` 10 / 10 / 9 and `identified_mass_share_q1_q4` 80.04 /
80.31 / 75.52; sentence 19's leg (e) figures; sentence 22's three Δ_W; sentences 25–27's facts; sentences
29 and 30's exploratory D's (−2.40 / −2.47 / −5.15) and Job-Zone slopes (−6.70 / −6.02 / −6.77); the
forbidden list's Δ_W/D ratios (−0.016 / +0.113 / −0.219) and C7 sentence ("about 11%", −15.6 / −11.9 /
−16.7). The item-11 addition does not disturb `identified_mass_share_q1_q4`, which is still populated on
the primary subset.

**Three conditional lines of `claims.md` are now satisfied and are mine to update** — not stale numbers,
spent conditions: line 39 ("the occupation from referee item 3 once the analyst adds the fact" — added);
lines 57–58 (the two software tasks' 8.5 pp "may be cited only once the analyst adds it" — added, 8.5413);
and lines 177–178, which forbid "any number from `robustness.json` or `legs.json` that is not in
`results.json` (A1 leg variants, C7 legs, the substantive-cell leg (e), the 2010 leg table, X7's wave
share) until the analyst adds it" — all five are now in `results.json`, so the general rule stands but the
parenthetical list no longer names exclusions. I will fold these into the draft-stage claims list.

### (f) Carried to the draft review

1. The two estimates without an SE under empirical standard 6 (§(b)14), one of which `claims.md`
   sentence 21 permits the post to cite.
2. The all-four subset's realised counts, 8 / 9 / 8 against the pre-registration's 7 / 8 / 6 (§(a)7).
3. `facts.rule_power.notes` and `facts.generalisation_sentence.sentence` state their numbers as prose
   inside the string rather than reading them from the arrays beside them; harmless while nothing moves,
   but they would not go stale visibly if anything did.
4. The `boundary_occupations.titles` truncation at four (§(a)1).
5. My own two "4.93%" references and the three spent `claims.md` conditions (§(c), §(e)).

## Independent re-derivations

By scope this read re-derives only what the revision moved or introduced. No cache statistic was computed.

| quantity | why checked | source | result |
|---|---|---|---|
| between-window SD of D and its ratio to the mean SE | introduced by item 17 | the three D's and three SEs in `results.json` | 3.6888119 and 26.0593 — matches `facts.between_window_dispersion_of_D` exactly; the notebook's 3.6928 does not |
| the three all-four D_(b), their intervals | introduced by item 11 | my first-read supplement | identical to 4 dp, all nine figures |
| item 10's six C7 shares | introduced by item 10 | my first-read re-derivation | all six match to the printed precision |
| item 12's fourteen figures (X7, A1, C7 legs, leg (e) substantive, software tasks, within-SOC-15, residual Q4, Seychelles) | introduced by item 12 | my first verdict and supplement | all match; Seychelles +4.5038 against my +4.50, recomputed by the analyst from the algebra |
| the boundary-occupation arithmetic (six salaries ÷ 2,080) | introduced by item 3 | the committed quartile bounds | all six reproduce the bounds |
| mde = 2.8 × se and ci = coef ± 1.959964 × se | item 16's additions | whole of `results.json` | 186 / 186 and 194 / 194, zero exceptions |
| placebo movement against Monte Carlo error | the extra CORRECTION | the committed band sds and B = 10,000 / 1,500 | 0.24 / 0.49 / 1.6 SEs on p; ≤ 1.3 SEs on the band means |
| `results.json`, `figures.json`, `09_*.out.txt` | correspondence of outputs to scripts | re-run of script 09 in a scratch extraction of `698a2f1` | byte-identical but for the timestamp |

## Assumptions sweep

Not a sweep stage. Carried unchanged from `referee-brief-2.md` and `referee-results.md`; the revision
strengthens item (3), composition, since `facts.C7_sign_agreement` now states that the second wage source
is the SOC-15 exclusion rather than an independent source, and weakens none of the four.

## What I could not verify

- **The release cache is not present in this session** (`posts/post1/data/` contains `processed/` only),
  so scripts 02–06 could not be re-run and no number was recomputed from raw files. The first read did
  that work at `1b621c0`; what this read establishes is that the revision did not move any of it (§(d)17)
  and that the committed `results.json` is exactly what script 09 makes of the committed upstream JSONs
  (§(d)18). Whether `legs.json`, `robustness.json` and `build_facts.json` are themselves what the
  committed 02–06 produce rests on the analyst's reported clean re-run plus the line-by-line match of
  their new prints to their committed check outputs.
- The 10,000-draw permutation and the 1,500-trial size study were not re-run; I checked only that the
  movement is of the size Monte Carlo error predicts and that the estimand, the band construction and the
  decision-rule status did not change.
- By scope I did not re-open the brief, the pre-registration, the feasibility or replication notes, or
  Anthropic's sources, and I did not re-read the analyst's scripts outside the diff. Deviations 1–4 and
  the test counts were judged in the first read and the diff does not touch them: the test counts are
  unchanged at 17 + 3 confirmatory / exploratory, 8 leg tests, 24 robustness, 16 descriptive.
- Whether the analyst changed anything in files he owns beyond those in this diff was not audited; only
  `posts/post1/` was diffed, and `room/` only for the two notes named at the top.
