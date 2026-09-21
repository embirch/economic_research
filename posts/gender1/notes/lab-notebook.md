# Lab notebook · gender1

Dated entries; deviations from the pre-registration are marked **Deviation** and carry the registered rule beside the corrected one.

## 2026-09-21 · pre-registration revision 1 (content aef0b5d, commit 3d4ae45)

Written from BRIEF v1.1 after script 01. Sent to the referee in a direct session (sesn_016KhWjfXPeHZcwrE3cyHmg3, $7.08). Verdict: BLOCK, sixteen items, all with fixes written out (`notes/referee-prereg.md`).

## 2026-09-21 · pre-registration revision 2, applying the verdict

1. **Sample sizes (item 1).** The national metadata's row [D] net sample of individuals 16–74 replaces the achieved/implied figures where the row gives it (30 geographies; the referee's transcription `notes/rederivation/referee_national_net_sample_2025.csv` merged into `data/processed/national_sample_sizes_2025.csv` as `n_net_individuals_16_74_D`). Corrections in the anti-conservative direction: CZ 7,705 → 4,494; LU 3,086 → 2,514; SE 4,938 → 4,450; AL 8,749 → 4,702. NL added (5,603). HU and TR stay on the implied figure (row [D] gives households); IE stays implied with its 2022–23 caveat. The `response_rate_pct` column was the household unit non-response rate where it matched anything and is relabelled `household_unit_nonresponse_pct_if_parsed`; it is not used.
2. **Band variance (item 2).** Script 01 now uses the EU27 both-sex band rate for each band's binomial variance instead of the country's overall rate; band half-widths change from a flat 6.3–7.6 to 7.8 (16–24) down to 3.7 (65–74). Assumption A4 rewritten as the referee specified.
3. **Design-effect list.** After the corrections the published-over-SRS ratio exceeds 1.3 for AT, BG, HR, RO, SK and for BA, CH, RS, TR; the median over 30 is 1.09. CZ falls to 1.01 once its n is corrected, as the referee predicted.
4. **Class rule (item 3).** Ratio now ranked ascending; per-measure tercile with k = round(N/3) and a 0.1-point (ratio 0.01) tie rule; persistent class over three measures; "not classifiable" for a geography lacking a measure (IE); distinguishable mark from the bound; class changes defined per pair of measures. BRIEF §4's "top tercile of the male-to-female ratio" and §7's `p_F / p_M` were inconsistent; §4 corrected to "the tercile of the largest male lead on the ratio" with a note that the pre-registration governs.
5. **Distinguishable counts (item 4).** Defined per rule; raw count is the registered verdict; both reported together; no-bound geographies listed by name.
6. **Expected resolution (items 5–6).** H-work's coin-flip null and the 19-of-27 threshold; H-age (a)/(b) simulation figures; H-education's ⅓ null and 0.025.
7. **Counts (items 7–8).** "At most 24" corrected to 26 of 27; coverage at commit added to §4; robustness item 8 omitted by rule (7 usable geographies per purpose).
8. **Disclosure (items 11–12).** The whole audit pairs file treated as seen; the referee's EU27 standardised gap (3.36 against 4.46) added.
9. **Smaller (items 13–16).** Root-sum-square wording; Signals leg is Spearman only; H-education renamed to "high is the largest" with the monotone count descriptive; commit hash recorded in the commit message rather than inside the file.

**Fact for the assumptions sweep (referee item 12):** at the EU27 level the sex difference in age structure alone accounts for about 1.1 of the 4.5-point gap.

## 2026-09-21 · second read (sesn_01Y8aLQVf6cTBsdHDNffWezw, $2.24): PASS WITH CHANGES, sign off

Five non-blocking opens, applied in the same commit: (B) script 01's docstring no longer says "achieved"; (C) the free-text columns of the sample-size table are quoted and stripped of thousands separators, no figure changed; (D) H-work's expected count corrected to "about 2.6 of 27"; (E) the pointer to `notes/brief-review.md` restored in the header. (A) The edit to `BRIEF.md` §4 (ratio direction) was made by the human's assistant acting for the human, who owns the brief at this stage of the pivot and approved it at Gate 1b; it is recorded here as the human's own correction, not the analyst's, and the pre-registration's class rule is the binding text either way.

## What the data cannot show (running list)

No sex within employment, occupation or urbanisation; no trend; no intensity; no confidence intervals; no gender beyond female and male; no age-by-education by sex; the household population differs from the resident population used for weights; no education-cell sampling bound.

## 2026-09-21 · analysis run (scripts 02–08), after Gate 2a approval (a95c100)

- Scripts run in the order 02, 03, 05, 04, 06, 07, 08 (04, the independent second implementation, needs 05's outputs to compare against; the registered names are unchanged).
- **Deviation D1 (class-rule precedence).** The registered class rule lists large-gap, small-gap, reversed, not classifiable and not distinguishable without saying which applies when a geography meets both "bottom tercile on all three" and "reversed on both denominators". Resolved as listed: small-gap first, with the reversed flag reported beside it. No count changes; both sets are in results.json (`classes.small_gap`, `classes.reversed_on_both_denominators`).
- **Deviation D2 (triangulation leg ii).** Henseke (2026) publishes the country gender gaps only as Figure 2, an image; under the figure-values ruling no number is read off a chart, and no table exists. Leg (ii) is dropped; leg (i) (OpenAI Signals) runs as registered.
- Purpose-specific standardisation omitted by rule (7 usable EU27 geographies per purpose; floor 15), as pre-registered.

## 2026-09-21 · referee results verification (sesn_01J46cb6JHXZWzA3d9jpA64H, $12.55): PASS WITH CHANGES; items applied

- **Deviation D3 (H-composition reading).** The registered class-changes text cuts the crude tercile over all 27 usable geographies and compares on the intersection with the 26 that have a standardised gap; script 05 re-cut the crude tercile on the 26. Both are now computed and reported: 3 changes (CZ, FR, LV) on the re-cut, 2 (CZ, LV) on the registered reading; verdict "supported" and distinguishable 0 under either. The re-cut is preferred for the headline count because a tercile change should reflect standardisation rather than Ireland's absence; the registered count is beside it everywhere, including the Figure 4 title and caption. The ratio-versus-standardised count uses the registered reading (8) with the re-cut (7) reported.
- **Deviation D4 (unregistered exploratory addition).** Script 07 also correlated the ratio with the feminine message share; it is labelled an unregistered addition in results.json. The scipy p-values are stored under not-for-citation keys; no p-value may be cited.
- **H-work symmetric clause.** The 19-of-27 threshold is one-sided; 23 or more of 27 the other way arises under an even split with the same probability, 0.026. The realised 4 of 27 in favour (23 against) has one-sided probability 0.0002 under an even split; results.json carries it.
- Figure 3's per-panel sorting mislabelled two panels under a shared y-axis; all three panels now use the overall-gap order with labels set once. Figure 1's legend moved off Malta's bars; its caption carries the sign-beyond-bound counts and says what the ● marks mean. Figure 2's caption gives median band half-widths and the small-sample range; zeros print as "0". Figure 5's caption states that the negative values are a denominator rescaling and that the sex difference in implied internet use is within a point in every band (the decomposition is in results.json). The class table's large-gap mark and the extension placements now use the 27-set gap cut (cuts.gap_27); no mark or placement changed (XK stays top by 0.02). Script 04 now recomputes the class table, the marks and H-work. Medians of even-length sets are true medians. Two vacuous assertions removed. EU27 band ratios added to results.json.
- Run order for the record: 02, 03, 05, 06, 07, 04, 08.
