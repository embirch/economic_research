# Referee verdict · gender1 · results · 2026-09-21

Reviewed from the record at `9b54be0`: `scripts/02_build.py` … `08_results_and_figures.py` and `gender1_common.py`
(read, not run); `data/processed/results.json`, `power_rules.json`, `second_implementation.json`;
`outputs/figures.json` and the five PNGs (viewed); `notes/lab-notebook.md` (the analysis-run entry and D1, D2);
`prereg/prereg.md` at revision 2 (content 6050e38), which governs; my own `notes/referee-prereg.md` and
`referee-prereg-2.md`; `BRIEF.md` v1.1 §4, §7, §9, §16; the director's figure-values ruling
(`room/director-2026-09-16-figure-values-ruling.md`) for D2; Henseke (2026), arXiv 2604.18849v3, re-read for D2.
Raw data: the official TSV refetched here with `data/fetch/eurostat_isoc_ai_iaiu.py` (sha256 `7f668f7b…`, the
pre-registration's hash; `results.json` records the same), `demo_pjan_EU27_2025.json` (flag `ep`), and the OpenAI
Signals bundle refetched from `cdn.openai.com` (sha256 `83b49feb…`, the data profile's hash). No room note between
the analyst and the director was read. **Re-derivation code, importing nothing from the analyst's scripts:**
`notes/rederivation/referee_results_gender1.py` → `referee_results_gender1.out.txt` (186 quantities against
`results.json`) and `referee_results_gender1_supp.py` → `referee_results_gender1_supp.out.txt` (the two readings of
the class rule, the class rule under a null, H-work in ratios, rule (a)'s clauses).

## Verdict

**PASS WITH CHANGES.** Every confirmatory number in `results.json` reproduces from the raw TSV with my own code:
the EU27 headline and purpose gaps, H-age (a) 20 of 26 and (b) 9 of 26 with distinguishable 8 and 1, H-education
14 of 26 with the monotone count 8, the standardised gaps for all 26 (DE 4.13, IT 2.28, MT −3.63; EU27 3.36),
H-composition 3 of 26 (CZ, FR, LV) with 0 distinguishable, the class table 6 / 7 / 0 / 13 / IE with the marks
DK, PL and EE, HR, LT, SI, H-work 4 of 27 with 0 distinguishable in favour and 9 against, the purpose sign counts,
the internet-composition medians, the Signals Spearman −0.174 over 26. 185 of 186 checks match to 1e-9; the one
mismatch is a mislabelled cut value (item 4). Both logged deviations are legitimate (items 2, 3). The results may
go to the claims list and the editor **after** the three blocking items below are fixed, because two of them put
a wrong or unregistered number in front of the editor (a mislabelled figure; a tercile-change count whose
registered reading is 2, not 3) and one puts p-values in `results.json` that the pre-registration said would not
exist.

## Items

### Blocking (fix before the draft; none changes a verdict)

**1. Figure 3's country labels are wrong in two of its three panels. `scripts/08_results_and_figures.py`,
Figure 3 block; `outputs/figures/fig3_purposes.png`.** The three axes are created with `sharey=True`; each panel
sorts its own countries (`gs = sorted(part, key=...)`) and calls `set_yticklabels` on its own axis, so the last
call — the education panel's order — labels all three. In the private panel the top row, labelled Germany, is
Ireland (16.0 of all individuals, 21.5 of users); the bottom row, labelled Ireland, is Croatia (−0.7, 1.8). In the
work panel the top row, labelled Germany, is Denmark (10.1, 11.8) and the second, labelled Poland, is Ireland.
Only the education panel is labelled correctly. *Fix:* one common order for all three panels (the overall gap, as
Figures 1 and 2 use) with the labels set once, or `sharey=False` with per-panel labels. The caption needs no
change. Verified against `results.json countries.*.purposes` (`.out.txt` §G and my check above).

**2. H-composition's tercile-change count is 3 under the analyst's reading of the class rule and 2 under the
registered text's literal reading; the reading was not logged. `scripts/05_standardise.py` lines 27–30;
`notes/lab-notebook.md`; `results.json tests.H_composition`; Figure 4 caption and title.** The class rule defines
the per-measure tercile over "the EU27 geographies with a usable value" for that measure — 27 for the crude gap,
26 for the standardised gap — and the class-changes paragraph counts differences "on the intersection of the two
usable sets". Read literally, France is 10th of 27 on the crude gap (the cut is its own value, 4.53; tercile
middle) and middle on the standardised gap: no change, and the count is **2 (CZ, LV)**. Script 05 instead re-cuts
the crude tercile on the 26 with a standardised gap, where France is 9th (cut AT 4.25) and top: **3 (CZ, FR,
LV)**. The same script applies the *other* reading to ratio-vs-standardised (ratio tercile over 27 against
standardised over 26: 8; re-cut on 26 it would be 7), so the implementation is internally inconsistent. The
analyst's reading is the better-designed comparison (a tercile change should reflect standardisation, not
Ireland's absence), but it is not the registered one, and the pre-registration's own rule for this case is "the
registered rule and the corrected rule are both run and both reported". The verdict is "supported" under either
(≤ 8); the distinguishable count is 0 under either (France's 4.53 is 0.28 from the cut against a half-width of
1.77). *Fix:* log **D3** in the notebook with both counts and the reason for preferring the re-cut; add
`tercile_changes_registered_reading: 2` (and `changed_registered_reading: ["CZ","LV"]`) beside the existing keys in
`results.json`; state which reading `ratio_vs_standardised` uses (and report the other, 7); amend the Figure 4
title and caption to "two or three of 26, depending on whether the crude tercile is cut on all 27 or on the 26
with a standardised gap". `.out.txt` §D and `_supp.out.txt` §1.

**3. Two p-values and one unregistered correlation sit in `results.json`. `scripts/07_triangulation.py`;
`results.json triangulation.leg_i`.** The pre-registration says "No p-value is computed anywhere, so there is no
multiple-testing correction" and registers one Spearman for leg (i): the Eurostat overall gap against the feminine
message share. Script 07 computes two (gap and ratio against the share) and stores `p_value_gap` 0.396 and
`p_value_ratio` 0.847. The ratio correlation is harmless and arguably implied by §3's definitions, but it is a
second exploratory test and must be labelled as an unregistered addition (a dated line in the notebook); the
p-values must go, or be renamed `scipy_p_not_for_citation` — the post may not cite them, and their presence in the
file the verifier binds to is the risk. The Spearman values themselves reproduce to 1e-9 (my own rank code, no
scipy).

### Should (fix in the same commit; no number in the post changes)

**4. `results.json classes.cuts.gap` is `[4.25, 2.51]`, which is the crude cut on the 26-set, not the gap cut on
the 27-set the class table's gap tercile uses (`[4.53, 2.51]`).** Script 05 reuses `tc_top` from H-composition
for the class table's distinguishable mark on large-gap (`abs(gv - tc_top) > hw`). The registered mark is
"further than its half-width from the (k+1)-th value on the gap measure", i.e. 4.53. No mark changes (DE 0.77 and
1.05 both < 1.63; HU, SE, SK fail both; DK, PL pass both), but the value is mislabelled and the mark is computed
against the wrong cut. *Fix:* compute the large-gap mark against the 27-set cut and write both cuts under
distinct keys (`cuts.gap_27`, `cuts.crude_26`). The extension placements (`place(...)`) also use the 26-set cut;
against 4.53 + 0.1 every extension placement is unchanged (XK 4.65 stays top by 0.02 — say so).

**5. Figure 1 caption's lead sentence is a raw-sign statement and needs the bound beside it.** "In every EU
country but five, men were more likely than women…": at the published rates, yes (22 of 27). At the country's own
SRS half-width the male lead is distinguishable from zero in **17** of those 22 (not BE, BG, EL, FI, LV), and
**none** of the five female leads (EE, HR, LT, MT, SI: −1.3 to −1.7 against half-widths of 2.9 to 4.7) is. The
● marks on the small-gap bars mean "distinguishable from the tercile cut", not "women's lead distinguishable from
zero", and a reader will take them for the latter. *Fix:* add to the caption "the male lead exceeds the country's
sampling bound in 17 of the 22; none of the five female leads does; ● marks distance from the tercile cut, not from
zero". These counts are not in `results.json`; add `classes.sign_beyond_bound: {male: 17, female: 0, neither: 10}`.

**6. Figure 1's legend covers Malta's bars.** Left panel, `loc="lower right"`: the women bar for Malta is hidden.
*Fix:* `loc="upper right"` or place the legend outside. Cosmetic but it hides a data row of the reversed set.

**7. Figure 2 caption: "band half-widths under simple random sampling are 4 to 8 points".** Those are the
**medians** over the 26 (3.5 at 65–74 to 7.5 at 16–24 on this set; 3.7 to 7.8 over the 33 with a bound); the
per-country range is 1.4 (Italy, 65–74) to 12.6 (Malta, 16–24). *Fix:* "median band half-widths … run from about
4 points at 65–74 to 8 at 16–24; for the smallest samples they exceed 10". Also the cells print "−0" and "+0" for
values inside ±0.5; format zero as "0".

**8. Figure 5's y-axis label is truncated at the top of the PNG** ("…, poin"). Shorten or wrap. And the caption
must not let the reader take the negative values for composition — see item 12.

**9. Script 04 does not recompute the persistent class table, the distinguishable marks or H-work.** The
pre-registration commits to "every gap, ratio, standardised rate, tercile **and class** … computed twice".
Script 04 reproduces gaps, ratios, band gaps, standardised gaps, terciles and the H-age / H-education /
H-composition counts (236 quantities, max difference 0.0) but not the class assignments, the marks, or the H-work
counts. My re-derivation now supplies the second implementation for those (all match), so this does not hold the
results; *fix* for the record by adding them to script 04 so the repository's own check covers the registered
list.

**10. H-work's `reading` applies the 19-of-27 threshold symmetrically without saying so.** The registered text
defines 19 or more of 27 as "beyond the 0.026 chance threshold" for *support*. Script 06 also returns that reading
when the count is ≤ 8 (23 or more against), which is the same one-sided tail and is right, but the sentence in the
post must say "23 or more of 27 the other way arises under an even split with the same probability, 0.026; the
realised 23 of 27 has one-sided probability 0.0002". Add the symmetric clause to the notebook.

**11. Two vacuous assertions in check blocks.** `03_gaps.py` line 96 (`for g in list(t_gap)[:0]`, a placeholder)
and `05_standardise.py` line 109 (`… or True`). Delete them; a check block that reads as checking something it does
not is worse than a shorter one.

### Could

**12. The "internet-composition share" is a difference of gaps on two denominators and, where internet use is
below 100 %, its sign is mechanical.** With `r` the implied internet-use rate (`p_IND / p_IU3`, by sex and band),
`gap_IND = r̄ (q_M − q_F) + q̄ (r_M − r_F)`: the first term is the internet-user gap rescaled, the second is the
internet-use gap by sex. At the EU27 level the second term is within ±0.3 in every band (−0.27 at 16–24, +0.09 at
65–74) because `r_F` and `r_M` are within one point of each other in every band (0.786 vs 0.796 at 65–74). The
registered share of −0.98 at 65–74 is almost entirely `(r̄ − 1)(q_M − q_F)`: a 4-point gap among 79 % internet
users is a 5-point gap among internet users. The registered quantity is what the post reports (I do not ask for a
new one), but the caption and the post must say the values are a denominator rescaling, not an internet
composition that favours women, and the strong form of the finding is the one the decomposition gives: the sex
difference in recent internet use is negligible in every band, so none of the AI gap is an internet-use gap. My
computation is in this verdict only (the re-derivation prints it under §F3 of the supplementary output).

**13. Medians of even-length sets are taken as `sorted[N//2]` (the upper middle value).** `median_change_pp`
−1.30 (true median −1.31), `internet_composition.band_medians.Y65_74` −0.82 (true −0.87), the extension median
over 8. Every caption rounding survives, but use the true median or say "upper median".

**14. EU27 band ratios are not in `results.json`.** The band rates are (`eu27.age_profile_rates`), and the
red-team memo uses their ratios (16–24: 1.03; 65–74: 0.53). Add `eu27.age_profile_ratio` so the post can state
them with a binding; they are disclosed EU27 cells re-expressed, no new test.

## The two logged deviations

**D1 (class-rule precedence): legitimate.** The registered rule lists large-gap, small-gap, reversed, not
classifiable and "otherwise not distinguishable" without saying which governs when a geography is bottom-tercile
on all three measures *and* `p_F > p_M` on both denominators. Four are (EE, HR, MT, SI); LT is reversed on
`PC_IND` only (+0.46 on `PC_IND_IU3`). The analyst applied the listed order (small-gap first, the reversed flag
beside). Under the other order the table would read small-gap 3 (BE, LT, PT), reversed 4. No hypothesis depends
on the choice, both sets are in `results.json` (`classes.small_gap`, `classes.reversed_on_both_denominators`), and
the rule itself is unchanged. Not a rule rewritten to fit. One consequence for the post: the registered
Interpretation says "the reversed geographies are named as a class, not ranked", so the post must still name EE,
HR, MT, SI as reversed on both denominators, and it may not present the class table's "reversed: 0" as a finding
that no country is reversed.

**D2 (Henseke leg dropped): legitimate, with the reason stated more exactly.** I re-read Henseke (2026), arXiv
2604.18849v3. The country gender gaps appear only in Figure 2 ("male minus female adoption rate by country");
there is no table of them in the text or the appendices (A: country coverage; B: measurement; C: alternative
exposure; D: gradients by country, individual-level impacts). The programme's figure-values ruling is narrower
than the notebook says — a value printed as a data label may be recorded as published text; a value read from
axis position may be recorded only as the reader's own reading and "never treated as published" — so the accurate
reason is that the leg would rest on 27 values that are the analyst's own readings, which the ruling forbids
treating as published and which an exploratory rank correlation would then present as data. Dropping the leg is
the conservative choice and removes an exploratory item, not a rule. The post must say leg (ii) was not run and
why, and may still cite Henseke's aggregate (4.1 points among workers, EWCS 2024; 13.8 % vs 9.7 %) as context on a
different population. Henseke also cites Bick et al. (2026) as finding "substantially smaller gender differences in
generative AI use by late 2025" — a fact the red team uses.

**D3 (unlogged): the re-cut of the crude tercile on 26 for H-composition.** Item 2 above. It must be logged; it is
not a rule rewritten to fit (the verdict is the same under both readings), but the count in the caption is the
unregistered one.

## Tests run against tests registered

- **Confirmatory, registered five, run five, each once:** H-work (1), H-age (a) and (b) (2), H-education (1),
  H-composition (1). Outcomes: against; partly declared (a yes, b no); supported; supported. Every distinguishable
  companion count is present (H-work 0 / 9; H-age 8 / 1; H-composition 0; H-education none by rule).
- **Descriptive, registered and run:** the class table with both marks; the three pairwise tercile-change counts
  (gap–ratio 6, crude–standardised 3, ratio–standardised 8); the internet-composition share by band; purposes on two
  denominators with sign counts; the education profile and monotone count (8 of 26); EU27 against extension and
  all 35; the flagged-cell appendix (0 rows: no overall pair has a value with a `u` flag, so the appendix is empty
  and the post should say so rather than promise it).
- **Exploratory, registered one, run two:** Signals Spearman gap–share (−0.17, N 26, registered) and ratio–share
  (+0.04, unregistered; item 3). Leg (ii) not run (D2). Two p-values computed against the pre-registration's
  statement (item 3).
- **Unregistered, descriptive, harmless:** `purposes.*.sign_flips` between denominators; `H_work.among_users`
  is registered as the secondary form.
- **Multiple-testing exposure:** five count rules and one exploratory correlation on one dataset; no p-value is
  used for any verdict. For the reader's calibration (not for the post unless the analyst adds them to
  `results.json`): under the registered nulls, H-work's 23 of 27 against has one-sided probability 0.0002;
  H-education's 14 of 26 is the minimum majority and has probability 0.025 under the ⅓ null — one country fewer and
  it fails; H-age (a)'s 20 of 26 is far outside its null (expected ≈ 6); H-age (b)'s 9 of 26 is the null
  expectation (P ≈ 0.5 under two-of-six); H-composition's "at most 8" could not realistically fail at the realised
  dispersion of shifts (if the observed shifts were reassigned at random across countries the expected change count
  is 4.5 and P(≤ 8) ≈ 0.99) — the rule is satisfied, but "supported" carries almost no information beyond the shifts
  themselves (red-team memo, item 6).

## Independent re-derivations

Code: `notes/rederivation/referee_results_gender1.py` (reads the TSV with `csv`, indexes the JSON-stat cube
itself for the weights, applies the registered tercile and tie rule from the pre-registration's text, takes the
half-widths from `power_rules.json` as the pre-registration directs) and `referee_results_gender1_supp.py`.
Output: `referee_results_gender1.out.txt`, `referee_results_gender1_supp.out.txt`.

1. **EU27 headline and purpose gaps.** Mine: total 32.66, women 30.45, men 34.91, gap 4.46; private 5.51, work
   3.00, education 0.05; among users 6.23, 2.74, −3.76; internet users 4.71; age profile −1.67, 4.67, 4.83, 2.84,
   4.24, 4.14; education 3.76, 4.61, 6.97; standardised 3.3627 (weights from my own indexing of `demo_pjan`,
   identical to `power_rules.json` to 1e-9). **All match `results.json eu27.*`.**
2. **H-age.** Usable set 26 (IE out). Rule (a) raw **20** — every one of the 20 has a negative 16–24 gap; 14 also
   have it smallest of six; none is smallest without being negative — distinguishable **8** (AT, BE, DE, EL, FI,
   HR, IT, SI). Rule (b) raw **9**, distinguishable **1** (HU). Verdict partly declared. The largest gap sits at
   65–74 in 9 of 26, 25–34 in 5, 35–44 in 4, 45–54 and 55–64 in 3 each, 16–24 in 2 (PL +13.8 against a band
   half-width of 5.2; RO +3.3 against 4.3). **Match.**
3. **H-education.** Usable set 26 (HR out: its `M_I0_2` cell is flagged `u`). High largest in **14**; monotone
   **8**; high smallest in 4; medians 3.23 / 4.81 / 7.28. **Match.**
4. **Standardisation and H-composition.** DE 5.30 → 4.1258; IT 3.12 → 2.2832; MT −1.71 → −3.6332; all 26 match
   to 1e-9. Lowered in 25 of 26 (CZ +0.95 the exception); median change −1.31 (script's upper median −1.30); range
   −4.03 (LT) to +0.95. k = 9; crude cuts on the 26: 4.25 / 2.51; standardised cuts 3.194 / 1.226; changes **3**
   (CZ middle→top, FR top→middle, LV middle→bottom) under the analyst's reading, **2** under the literal reading
   (item 2); distinguishable **0** either way. Tie-rule exclusions: LV on the crude gap (2.42 within 0.1 of the cut
   2.51), EL on the ratio. **Match on the analyst's reading; discrepancy of reading logged as item 2.**
5. **Class table.** Gap tercile over 27 (cuts 4.53 / 2.51), ratio over 27 (0.8661 / 0.9309, ascending), standardised
   over 26. Large-gap DE, DK, HU, PL, SE, SK (6); small-gap BE, EE, HR, LT, MT, PT, SI (7); reversed 0 (D1);
   not distinguishable 13; IE not classifiable. Marks: DK (7.87 − 4.53 = 3.34 > 3.15) and PL (2.76 > 1.64) large;
   EE, HR, LT, SI small (distance from 2.51 of 4.07, 3.85, 3.86, 4.01 against half-widths 3.15, 3.14, 2.86, 3.55);
   MT not (4.22 < 4.71). Every country's class and mark matches `results.json countries.*.class`. The gap cut in
   `results.json` is the 26-set value (item 4). Gap–ratio changes 6 (BG, FI, IT, LU, NL, RO); ratio–standardised 8.
   **Match except the cut label.**
6. **H-work.** N 27; work gap > private gap in **4** (AT, DK, EL, HR); distinguishable in favour **0**, against
   **9** (ES, FR, IE, IT, LU, PL, PT, RO, SK); among users 7 of 27; EU27 work − private −2.51; median across
   countries −2.26. **Match.** Purpose sign counts, internet-composition medians (26; IE out), sets medians (EU27
   3.57, extension 4.65 with MK reversed, all 35 3.96), flagged rows 0, Signals N 26 (MT missing) and both
   Spearmans: **match.**

## Figure captions against `results.json` (`.out.txt` §G)

- **fig1:** "every EU country but five" ✓ (5 reversed on `PC_IND`); "about −2 to +9" ✓ (−1.71 to +9.32); "class is
  stable across measures for only 13 of 27" ✓ as large + small = 13, but the same number is the not-distinguishable
  count and the sentence will be misread — say "13 of 27 sit in the same tercile on all three measures (6 large-gap,
  7 small-gap)". Bound qualification missing (item 5). Colour legend matches the plot.
- **fig2:** "women lead in 20 of 26 at 16–24" ✓ (20 negative 16–24 gaps; note this is the same 20 as rule (a), which
  the caption should not conflate with the rule); "from 25 upward men lead in 17 to 22 of 26" ✓ (17, 18, 18, 20,
  22); "no single band holds the largest gap in a majority" ✓ (max 9 of 26); "4 to 8 points" is the median range
  (item 7).
- **fig3:** every sentence ✓ (education participation negative 21 of 27, among users 26 of 27; private positive 25,
  work 23) — but the plot's labels are wrong (item 1).
- **fig4:** "lowers the gap in 25 of 26" ✓; "moves three across a tercile cut" is the unregistered reading (item 2).
- **fig5:** "under a point at the median in every band" ✓ (largest |median| 0.87); "more than a point in ten
  countries only at 65–74" ✓ (|share| > 1 in 3, 1, 2, 1, 5, 10 by band — "only" is not literally true: three
  countries at 16–24 and five at 55–64 also exceed a point; say "in ten countries at 65–74 and in five or fewer in
  every other band"). Interpretation caveat (item 12).

## What I could not verify

- The EIGE mirror's agreement with the official TSV (not in this sandbox).
- Whether Henseke's Figure 2 carries printed data labels (the HTML renders it as an image; the PDF was not opened).
  If it does, the leg could have run under the ruling with the values marked "(figure label)"; the analyst should
  say whether it checked.
- The Signals bundle's licence (`README.pdf` in the zip, not read); the data profile flags it as to-be-read before
  use, and the post cites the leg.
- Anything about the 2025 fieldwork beyond Eurostat's metadata (the bound assumes SRS and equal sex split; the
  design-effect list in `power_rules.json` says where it is loose: AT, BG, HR, RO, SK).

## Confirmation at acda4f7 (2026-09-21, closing session)

Checked without re-deriving: `git diff 4ec7b45 acda4f7 -- posts/gender1`, the three PNGs viewed, `outputs/figures.json`
and `results.json internet_composition` read. Every open item of `referee-results-2.md` landed as worded:

- **Fig 1 legend** — `loc="lower center", bbox_to_anchor=(0.5, -0.115), ncol=2, frameon=False`; the legend sits
  below the axis, Ireland's men bar (49.6) and Malta's bars are both fully visible.
- **Fig 2 zero cells** — formatter `"0" if round(M[i, j]) == 0 else f"{M[i, j]:+.0f}"`; Belgium at 25–34 (−0.50)
  prints "0"; no "−0" or "+0" cell in the 27 × 6 matrix.
- **Fig 5 caption and `internet_composition.reading`** — "at most 1.1 points in any age band and moves the gap by
  under 0.3 points", exactly the prescribed sentence; the decomposition key gives 1.10 at 55–64 and 1.08 at 65–74
  and terms of −0.27 to +0.09.
- **Fig 1 caption, 13 of 27** — "13 of 27 countries sit in the same tercile on all three measures (6 large-gap,
  7 small-gap)", as prescribed.
- **`internet_composition.over_one_point_by_band`** — {3, 1, 2, 1, 5, 10}, the counts the caption's "ten countries"
  now binds to; computed in script 08 as |composition_share| > 1 over the EU27 members with the band usable.

Nothing else in `results.json` changed between 4ec7b45 and acda4f7 except `generated`; the two remaining keys the
claims list asks for (`tests.H_age.men_lead_by_band`, `tests.H_age.largest_band_counts`) are still absent and are
marked **[key missing]** in `notes/claims.md`; until they exist the two sentences in Figure 2's caption that rest on
them may not be carried into the post, and the caption itself is bound to the same rule at the draft review.

`notes/claims.md` and `notes/red-team.md` refreshed to acda4f7 in this session: the registered-reading count 2 beside
3 and the renamed `tercile_changes` keys; the extension median 4.4; the band medians 0.00 to −0.87; the true median
−1.31; `classes.sign_beyond_bound`, `eu27.age_profile_ratio`, `eu27_decomposition` and `over_one_point_by_band`
bound by key; the internet-use sentence as "at most 1.1 points … under 0.3 points"; the second implementation at
293; the fieldwork-timing correction (mostly late March to early August 2025, Serbia February, Greece July to
September; the country comparison is not a common calendar window) carried into the permitted sentences, the
forbidden sentences, required caveat 1, limitation 7 and the opening claim ("In 2025", not "In early 2025").

**SIGN OFF — results, gender1, at acda4f7 — 2026-09-21.** The results may go to the editor with `notes/claims.md`
as the boundary document. Conditions carried to the draft review: the two **[key missing]** items above; the
deviations list order (D1–D4) when script 08 is next touched; the four unverified items under "What I could not
verify" stand.
