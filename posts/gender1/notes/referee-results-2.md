# Referee verdict (second read) · gender1 · results · 2026-09-21

Second read, narrow by design. Read only: my own `posts/gender1/notes/referee-results.md` (the PASS WITH
CHANGES verdict at 46666e5), the owner's status note `posts/gender1/notes/lab-notebook.md` (entry
"2026-09-21 · referee results verification … items applied"), the diff `git diff 9b54be0 a13ac3e --
posts/gender1`, and the files the revision touched: `scripts/03_gaps.py`, `04_second_implementation.py`,
`05_standardise.py`, `06_denominators_and_purposes.py`, `07_triangulation.py`,
`08_results_and_figures.py`, `data/processed/results.json`, `standardise.json`,
`denominators_purposes.json`, `triangulation.json`, `second_implementation.json`, `outputs/figures.json`
and the five PNGs (viewed). Anthropic's sources, the brief, the pre-registration and Henseke (2026) were
**not** re-opened. No number was re-derived except the ones the revision changed or added, and those only
from `results.json`, `power_rules.json` and the chain's own re-run.

**Chain re-run.** `data/cache` was empty in this sandbox: `data/fetch/eurostat_isoc_ai_iaiu.py` refetched
`isoc_ai_iaiu.tsv` (sha256 `7f668f7b…`, the registered hash) and the Signals bundle was refetched from
`cdn.openai.com` (sha256 `83b49feb…`, the hash in the data profile) and unzipped. In a worktree at a13ac3e
the scripts ran in the notebook's order — 02, 03, 05, 06, 07, 04, 08 — and every check block printed
CHECKS PASSED. The regenerated `results.json` matches the committed file on all **4,296 leaves** except
`generated` (a timestamp) and one float ULP in `scipy_p_not_for_citation_gap` (0.39591601168364476 against
0.3959160116836446, a scipy build difference in a value that may not be cited). The five PNGs regenerate
with the same content; their byte differences are font rasterisation (checked by eye on Figure 4).

**Nothing moved that the verdict did not ask to move.** Leaf-by-leaf against 9b54be0: 4,243 → 4,296 leaves;
no hypothesis verdict, no count, no country class and no distinguishable mark changed. The only changed
values are the six medians item 13 asked for, `second_implementation.checked` (236 → 293), three reading /
deviation strings, and the keys items 2, 3, 4, 5, 10, 12 and 14 asked to add.

## Verdict

**PASS WITH CHANGES.** All three blocking items are applied as worded. Of the eight "should" items, six are
applied, one (6, Figure 1's legend) moved the occlusion instead of removing it, and one (7) is applied in
its caption half but still prints one "−0" cell. Of the three "could" items, two are applied and one (12)
is applied as a key but has introduced a sentence into Figure 5's caption and into `results.json` that the
new key itself contradicts — the error is mine in origin (my item 12 said "within one point"), and it is
the one thing here that puts a wrong statement of fact in front of the editor. Three fixes below, all in
the analyst's files, none touching a number the post reports; two further corrections are owed in my own
first-read files (`notes/claims.md`, `notes/red-team.md`), which the revision has made stale. No sign off
until the three are applied; after that the results are ready for the claims list and the editor.

## Item by item

**1. Figure 3's country labels — APPLIED.** `08_results_and_figures.py`: `gs = order   # one common order
for all three panels: the overall gap, as Figures 1 and 2 (referee item 1)`, with the labels set once
(`ax[0].set_yticks(yy); ax[0].set_yticklabels([NAME[g] for g in gs], fontsize=7)`) and missing values
passed as `part.get(g, np.nan)`. Viewed: the top row is Ireland with private 16.0 / 21.5 and work 9.9 /
11.8; Denmark second (work 10.1 / 11.8); Croatia's private points sit at −0.7 and +1.8 against its own
label. All three panels now carry the same order as Figures 1 and 2. Caption unchanged, as prescribed.

**2. H-composition's two readings and D3 — APPLIED.** Notebook: "**Deviation D3 (H-composition reading).**
… Both are now computed and reported: 3 changes (CZ, FR, LV) on the re-cut, 2 (CZ, LV) on the registered
reading; verdict 'supported' and distinguishable 0 under either." `results.json` carries
`tests.H_composition.tercile_changes_registered_reading: 2`, `changed_registered_reading: ["CZ","LV"]`, and
both `reading` and `registered_reading` strings; `classes.tercile_changes` now has
`crude_vs_standardised_analyst_reading: 3`, `crude_vs_standardised_registered_reading: 2`,
`ratio_vs_standardised_registered_reading: 8` and `ratio_vs_standardised_recut_26: 7`. Figure 4's title
reads "Age standardisation moves 2 or 3 of 26 countries across a tercile cut (red: either reading)" and the
caption "moves two or three across a tercile cut, depending on whether the crude tercile is cut on all 27
countries or on the 26 with a standardised gap". Script 04 now asserts the registered count too. *Note, not
a fix:* the plain keys `crude_vs_standardised` and `ratio_vs_standardised` were renamed rather than kept
beside the new ones. The names are clearer and nothing else in the repository reads the old ones, but
`notes/claims.md` line 63 still binds to `ratio_vs_standardised` — mine to correct.

**3. p-values and the unregistered correlation — APPLIED.** `07_triangulation.py` now writes
`scipy_p_not_for_citation_gap`, `scipy_p_not_for_citation_ratio`,
`spearman_ratio_vs_feminine_share_UNREGISTERED_ADDITION` and a `note` ("no p-value is registered and none
may be cited"); the script's own print no longer shows a p-value; D4 is logged in the notebook with the
date and appears in `results.json deviations`. The registered Spearman is unchanged (−0.1738, N 26).

**4. The class table's gap cut — APPLIED.** `cuts.gap_27: [4.53, 2.51]` and `cuts.crude_26: [4.25, 2.51]`
are now distinct keys; the large- and small-gap marks and the extension placements use `g27_top/g27_bot`.
Confirmed against the leaf comparison: no country's class, no mark and no extension placement changed, and
the notebook says so ("XK stays top by 0.02").

**5. Figure 1's caption and the sign counts — APPLIED.** Caption: "The male lead exceeds the country's
sampling bound in 17 of the 22 countries where men lead; none of the five female leads does … ● marks a
class whose gap lies further than the bound from the tercile cut, not a lead distinguishable from zero."
`classes.sign_beyond_bound: {male: 17, female: 0, neither: 10, male_lead_countries: 22,
female_lead_countries: 5}`. Recomputed from `countries.*.overall.gap` against
`power_rules.json countries.*.gap_halfwidth95_pp`: 17 / 0 / 10, 22 / 5. Match.

**6. Figure 1's legend — PARTLY APPLIED; STILL OPEN.** `loc="lower right"` became `loc="upper right"`.
Malta's bars are now visible, but the legend box now sits over the right end of Ireland's men bar (49.62 %,
the top row of the left panel), so the fix moved the occluded row rather than removing it. *Exact fix:* put
the legend outside the data area, e.g. `ax[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.115),
ncol=2, frameon=False, fontsize=8)`, or keep `loc="upper right"` and widen the axis
(`ax[0].set_xlim(0, 62)`) so no bar runs under it. Severity: should.

**7. Figure 2's caption and the zero cells — CAPTION APPLIED; ZERO FORMAT PARTLY APPLIED, STILL OPEN.** The
caption now reads "median band half-widths under simple random sampling run from about 4 points at 65–74 to
8 at 16–24, and exceed 10 for the smallest samples" — recomputed medians over the 26 plotted countries are
3.54 at 65–74 and 7.50 at 16–24, with two countries above 10 at 16–24 (maximum 12.55); the sentence holds.
The cell formatter is `("0" if abs(M[i, j]) < 0.5 else f"{M[i, j]:+.0f}")`, which still prints "−0" for
Belgium at 25–34, whose gap is exactly −0.50 (the only such cell in the matrix; verified over all 27 × 6
published cells). *Exact fix:* `abs(M[i, j]) <= 0.5`, or test the rounded value
(`"0" if round(M[i, j]) == 0 else …`). Severity: should.

**8. Figure 5's y-axis label — APPLIED.** `set_ylabel("gap (all individuals) minus\ngap (internet users),
points", fontsize=9)`; the label is wrapped and fully inside the PNG. The caption half of the item is
item 12 below.

**9. Script 04's coverage — APPLIED.** The second implementation now recomputes the 27-set tercile, the
persistent class for all 27, both distinguishable marks and H-work's three counts from its own reads
(`n_checked += 27 * 2 + 3`; the file reports 293 quantities, max difference 0.0, and the run printed "class
table, marks and H-work 4/0/9 reproduced"). It also asserts the registered-reading change count. The only
input it shares with script 05 is `power_rules.json`'s half-widths, which the pre-registration makes the
source of record — acceptable.

**10. H-work's symmetric clause — APPLIED.** `reading` now reads "beyond the 0.026 chance threshold (19 or
more of 27 in favour, or 23 or more against, each one-sided 0.026 under an even split)" and
`one_sided_probability_of_realised_count_under_even_split` is 0.00015537440776824…; my own
`P(X ≤ 4 | n = 27, p = ½)` is 0.0001553744077682495. Match. The notebook carries the clause.

**11. The two vacuous assertions — APPLIED.** `03_gaps.py`'s `[:0]` placeholder and `05_standardise.py`'s
`… or True` are both gone; both scripts still pass their check blocks.

**12. The internet-composition decomposition — KEY APPLIED; ONE SENTENCE NOW WRONG; STILL OPEN.**
`internet_composition.eu27_decomposition` gives, per band, `implied_internet_use_F`, `implied_internet_use_M`,
`rescaling_term` and `internet_use_gap_term`; the two terms sum to the registered composition share in all
six bands to 1e-12 (65–74: −1.0702 + 0.0902 = −0.98), so the identity is exact and the substantive point —
the internet-use term moves the gap by at most 0.27 points in any band — is now in the file. But Figure 5's
bold caption sentence and `internet_composition.reading` both say the sex difference in recent internet use
is "within a point in every age band", and the new key says otherwise: the implied rates differ by **1.10
points at 55–64** (0.9152 against 0.9261) and **1.08 points at 65–74** (0.7963 against 0.7856). My own item
12 wrote "within one point"; that was loose, and the revision inherited it. *Exact fix,* in
`08_results_and_figures.py` and in the `reading` string: replace "the sex difference in recent internet use
is within a point in every age band" with "the sex difference in recent internet use is at most 1.1 points
in any age band and moves the gap by under 0.3 points". The rest of the caption (the rescaling sentence,
"about a fifth of people are not recent internet users" at 65–74 — implied rates 0.786 / 0.796) is right.
Severity: should, before the caption reaches the editor.

**13. True medians — APPLIED.** `statistics.median` throughout scripts 05 and 06. Changed values:
`median_change_pp` −1.3067 (was −1.3015), `band_medians` Y25_34 −0.135, Y35_44 −0.215, Y55_64 −0.455,
Y65_74 −0.870 (was −0.820), `sets.extension.median` 4.365 (was 4.65). I recomputed the extension median
from the eight published gaps (…, 4.08, 4.65, …): (4.08 + 4.65) / 2 = 4.365. Match. No purpose median and
neither odd-length set median (EU27 3.57, all 35 3.96) moved, as expected.

**14. EU27 band ratios — APPLIED.** `eu27.age_profile_ratio` 1.027 at 16–24 falling to 0.525 at 65–74;
recomputed from `eu27.age_profile_rates` — identical in all six bands.

### The unnumbered caption remarks in the first-read verdict

- **Figure 1, "class is stable across measures for only 13 of 27" — NOT APPLIED** (could). 13 is also the
  not-distinguishable count and will be misread. *Fix:* "13 of 27 sit in the same tercile on all three
  measures (6 large-gap, 7 small-gap)".
- **Figure 5, "only at 65–74" — REWORDED, and now literally true** ("only at 65–74 … does the rescaling
  exceed a point in ten countries"): the per-band counts are 3, 1, 2, 1, 5, 10, so ten countries is reached
  only in the last band. Accepted in place of my wording. But "ten countries" still has no key to bind to.
  *Fix (should, for the editor's verifier):* add
  `internet_composition.over_one_point_by_band: {Y16_24: 3, Y25_34: 1, Y35_44: 2, Y45_54: 1, Y55_64: 5,
  Y65_74: 10}` — `notes/claims.md` line 143 already asks for exactly this key.
- **Figure 2, "20 of 26 at 16–24"** — caption unchanged and does not name rule (a); no conflation. Accepted.

### Deviations

- **D1, D2 — rulings unchanged**, both legitimate, both still logged and now carried in
  `results.json deviations`.
- **D3 — now logged** (notebook and `results.json`), with both counts, the reason for preferring the re-cut
  and the note that the verdict is "supported" under either. This closes the unlogged deviation.
- **D4 — newly logged** for the unregistered ratio correlation. Correctly described as adding nothing
  citable. Legitimate.
- *Cosmetic:* `results.json deviations` lists them D3, D4, D1, D2. Reorder to D1–D4 when something else
  touches script 08; not a fix on its own.

## Knock-on corrections owed in my own first-read files (not the analyst's)

1. `notes/claims.md` line 64–65: "the median published gap is 4.6 points" — with the true median the
   extension figure is **4.4** (`sets.extension.median` 4.365). Line 142: "(0.00 to −0.82)" is now 0.00 to
   **−0.87**. Line 128's "−1.30, an upper median" is now −1.3067; the sentence's "about 1.3" survives.
   Line 63 binds to the renamed key `ratio_vs_standardised` (now `…_registered_reading`).
2. `notes/claims.md` line 147 and `notes/red-team.md` line 152 repeat "within one point" for the implied
   internet-use rates; both need item 12's corrected wording (at most 1.1 points; the term under 0.3).

These are stale bindings in the boundary document, so they must be corrected before the editor works from
it; they are the first-read referee's files, and this second read does not edit them.

## What I could not verify

- Nothing in the prior verdict's "could not verify" list changed here: the EIGE mirror, Henseke's Figure 2
  labels, the Signals `README.pdf` licence and the 2025 fieldwork design remain unchecked. The analyst has
  not said whether it opened Henseke's PDF; D2's ruling does not depend on it.
- The re-derivations behind the untouched numbers were not repeated; this read relies on the first verdict's
  185-of-186 match for everything the revision did not move.

## Postscript: 4ec7b45, landed after this read

`4ec7b45` (after a13ac3e, the revision reviewed here) changes Figure 1's caption opening from "in early
2025" to "in the three months before their 2025 interview", adds the fieldwork-timing note to the notebook
and re-runs script 08 (timestamp only in `results.json`). The frame correction is right and nothing in it
touches the three open items above, which are all still open at 4ec7b45: Figure 1's legend over Ireland's
bar, Belgium's "−0" cell at 25–34, and Figure 5's "within a point". The unnumbered fig1 remark ("13 of 27")
is also still as it was.
