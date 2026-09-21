# Referee verdict (second read) · gender1 · pre-registration, revision 2 · 2026-09-21

Second read, narrow by design. Read only: my own `posts/gender1/notes/referee-prereg.md` (the BLOCK verdict
on revision 1, content aef0b5d at 3d4ae45), `posts/gender1/prereg/prereg.md` at c128906 (content 6050e38),
the owner's status note `posts/gender1/notes/lab-notebook.md`, the diff `git diff 3d4ae45 c128906`, and the
three files the verdict's fixes touched: `posts/gender1/scripts/01_sampling_bound.py`,
`posts/gender1/data/processed/power_rules.json`, `posts/gender1/data/processed/national_sample_sizes_2025.csv`.
Anthropic's sources, the brief, the feasibility note and the audit file were **not** re-opened. No number was
re-derived except the ones the revision changed, and those only by re-running script 01 in this sandbox after
`data/fetch/eurostat_isoc_ai_iaiu.py` (the cache was empty; the refetched `isoc_ai_iaiu.tsv` has sha256
`7f668f7b…`, the hash the pre-registration names). **No country-level gap, ratio, band, education or
standardised value was computed or read** — the only country-level quantities touched are sample sizes,
published both-sex overall rates and the reference indicator's published standard error, all already
disclosed as seen by script 01. Text matching was done on whitespace-normalised strings.

## Verdict

**PASS WITH CHANGES** — sign off on the pre-registration as a registered document. All sixteen items are
applied; the four blocking ones (1, 3, 4, 11, 12) are applied in my exact words or better, the superseded
text is gone in every case, and every figure the revision inserted reproduces when script 01 is re-run here
(identical to the committed `power_rules.json`, byte for byte). The six §5 numbers quoted in the
pre-registration — median half-width 2.8 across 33 geographies, IT 0.88, DE 1.63, NL 2.60, DK 3.15, MT 4.71,
band medians 7.8 at 16–24 down to 3.7 at 65–74, median published/SRS 1.09 over 30 — are exactly what the
script prints. Nothing in the revision weakens a rule, widens a hypothesis, removes a failure condition or
adds an unregistered test; the diff touches only the sixteen items and their consequences.

Five things remain, none of them in a rule or a number, and none of them a reason to hold the commit of the
pre-registration itself. One (item A) is an ownership breach and is for the director and the programme lead,
not for the analyst to repeat; the other four are one-line corrections that can ride on the next commit
touching those files.

## The sixteen items

### Blocking items

**1. The sample table and §5. APPLIED, and verified against the raw transcription.**
`national_sample_sizes_2025.csv` now carries `n_net_individuals_16_74_D` with a `how_read` column, and all
31 figures match my own transcription (`notes/rederivation/referee_national_net_sample_2025.csv`) cell for
cell, with no mismatches and none missing. Script 01 takes that column in preference (`n =
r["n_net_individuals_16_74_D"] or r["n_implied"]`) and records the provenance per country in the JSON
(`n_source`: "net sample, row [D]" for 30 geographies used, "implied (yes-count / proportion)" for HU, TR
and IE). The four anti-conservative corrections land at exactly the half-widths I predicted: CZ 2.13 → 2.80,
LU 3.49 → 3.87, SE 2.75 → 2.90, AL 1.87 → 2.55; NL enters with n = 5,603 and a half-width of 2.60, so **no
EU27 member is now without a bound** and the "no bound" list is MK and XK only, as §"Hypotheses" states.
The §5 sentence is the verdict's replacement, improved: IE is correctly moved to the implied group (the JSON
confirms it is), which my wording had left ambiguous. `response_rate_pct` is relabelled
`household_unit_nonresponse_pct_if_parsed` and is still unused by the script.
The design-effect sentence names AT, BG, HR, RO, SK among members and BA, CH, RS, TR in the extension,
where my verdict named AT, BG, RO. **The revision is right and my verdict was stale**: on the corrected
samples the published/SRS ratios are AT 1.32, BG 1.76, HR 1.34, RO 2.90, SK 1.31, BA 1.64, CH 1.92, RS 1.65,
TR 1.62 — exactly the `above_1_3` list the re-run produces. The list in `power_rules.json` governs; the
figures in item 1 of the first verdict were computed on partly uncorrected inputs and should not be quoted.

**3. The class rule. APPLIED, verbatim, plus one addition.**
The per-measure tercile (ratio **ascending**, k = round(N/3), the 0.1-point / 0.01-ratio tie rule), the
persistent class with **not classifiable** for IE, the distinguishable mark, and the class-changes definition
are present word for word. H-composition's test now reads "assign each its per-measure tercile … on the crude
gap and on the standardised gap" and its rule "at most 8 of the 26 change tercile (one third of 26 is 8.67).
**Against:** 9 or more change". The addition is mine restated: the noise sentence now carries the figure
("about four geographies large-gap and six small-gap of 26 by noise alone, referee re-derivation §E"), which
strengthens rather than softens the warning. Accepted.

**4. The distinguishable count. APPLIED, verbatim.**
The opening paragraph is the replacement text, with "(at commit: none in the EU27; MK and XK in the
extension)" in place of my "none in the EU27 after NL's net sample is added" — the same statement, and I have
verified it: the only geographies in `power_rules.json` without a bound are EA, EU27_2020, MK and XK. All
four **Distinguishable count** lines are present word for word under H-work, H-age, H-education and
H-composition. The raw count is named as the registered verdict and the Interpretation section now opens
with "'Declared' below means the raw verdict, always reported with its distinguishable count in the same
sentence."

**11. The audit file's exposure. APPLIED, verbatim.**
The disclosure paragraph is the replacement text, with the file's shape (396 rows, columns) kept. "Seen by
script 01" now adds the country both-sex overall rates and, correctly, the EU27 both-sex band rates that
item 2 introduced — a disclosure the verdict did not ask for and which the revision was right to add.

**12. The referee's EU-level inspection. APPLIED, verbatim.**
Present as its own disclosure paragraph, and used again as H-composition's "Calibration, disclosed" bullet
(4.46 → 3.36). The "Not seen by anyone" list is correspondingly narrowed to "any country-level standardised
value". Correct.

### Should items

**2. The band variance. APPLIED, verbatim where A4 lives.**
Script 01 now reads the EU27 both-sex band rates from the aggregate rows and uses `se_rate(eu_band[b], nb)`
for the band variance; A4 in both the script and `power_rules.json` is my replacement sentence word for word;
§5 of the pre-registration carries the condensed form ("the country's published overall both-sex rate for the
overall bound and the EU27 both-sex band rate for the band bounds (A4)") and §9 discloses the six band rates.
Band medians move from a flat 6.3–7.6 to 7.78 / 7.34 / 6.73 / 6.06 / 5.00 / 3.67, in the direction and by the
factors §F of my re-derivation predicted. No country-by-age cell is read by the script; the rates are the
EU27_2020 aggregate rows only. Confirmed by re-run.

**5. H-work's null. APPLIED, verbatim** (probability ½, 19 of 27 at 0.026, the "not distinguishable from an
even split" instruction), **and** "Five confirmatory rules: H-work (1, with the disclosed exposure of its
country inputs, see Disclosure) …". See change D below for the one stale denominator inside it.

**6. Expected resolution for H-age and H-education. APPLIED, verbatim**, with "refreshed by script 01 after
the sample-size and band-rate corrections" replacing my "after items 1–2". The stated ranges (about 6 and 20
for (a); 8–10 and 13–16 for (b)) already span the pre- and post-correction simulations, so nothing here is
falsified by the new bounds; the sentence "(b) 'not declared' is nothing shown and the post says so" is
present. H-education's ⅓ null and 0.025 are present.

**7. "At most 24" → 26. APPLIED, verbatim.**

### Could items

**8. Coverage at commit. APPLIED**, as a new bullet in §4 and inside H-work (27 of 27), H-age (26 of 27),
H-education (26 of 27), robustness 3 (26 of 27) and robustness 8, which is now "omitted by rule (7 usable
EU27 geographies per purpose against a floor of 15)".
**9. The H-age completion. APPLIED** — the clause "(The brief's 'against' for H-age left a gap between
support and refutation; this rule's complement closes it, a completion marked here.)" is in the rule.
**10. Nothing to apply** (the matches); the reproduced quantities are unchanged by the revision except the
bound, re-checked above.
**13. Root-sum-square. APPLIED** in §5 and in the JSON's `class_rule.reading`.
**14. Signals leg. APPLIED** — "Rank correlation only; no class is defined for a message share."
**15. H-education. APPLIED** — the hypothesis is retitled "the high-education gap is the largest of the
three" and the monotone count is descriptive.
**16. The commit hash. APPLIED as far as it can be.** A file cannot carry the hash of the commit that
carries it; the revision records "content hash recorded in the commit message" and c128906's message gives
content 6050e38, which I verified (`git hash-object posts/gender1/prereg/prereg.md` → 6050e38…). The header
also names revision 1 as content aef0b5d at 3d4ae45, so the chain is recoverable. Acceptable; the director
may wish to add "content 6050e38 at c128906" to the notebook heading so the record does not live only in a
commit message.

## Changes still open (none blocking the pre-registration)

**A. `posts/gender1/BRIEF.md` was edited by the analyst. Ownership breach; for the director and the
programme lead.** c128906 changes BRIEF §4's ratio sentence to "in the tercile of the largest male lead on
the ratio (`p_F / p_M` ascending; corrected … so that §4 and §7 agree)". The substance is exactly right and
it removes the §4/§7 inconsistency my item 3(i) found — but `posts/postN/BRIEF.md` is the programme lead's
path, my verdict said in terms that "the brief is untouched", and no item asked for a brief edit. *Fix:* the
director asks the lead to re-issue that sentence in the lead's own commit (the analyst's wording can be
adopted as written), and the analyst's notebook records the breach. Do not simply revert: reverting would
restore an inconsistency the pre-registration now governs anyway (the prereg's class rule is the binding
text, and §3's "a smaller ratio is a larger male lead" says so).

**B. Script 01's docstring still says "achieved". `scripts/01_sampling_bound.py`, docstring paragraph 1.**
The code preference is row [D], but the header still reads "with the national achieved sample n (from the
national reference metadata …)". *Fix:* replace "the national achieved sample n" with "the national net
sample n of individuals aged 16–74 (row [D] of the national reference metadata; the implied yes-count ÷
proportion for HU, TR and IE)". Cosmetic, but it is the last place in the record where "achieved" survives.

**C. Four rows of `national_sample_sizes_2025.csv` have unquoted commas in their free-text columns.**
DE, HU, NL and TR each contain a thousands separator or a semicolon-run inside `how_read`, so the row still
parses into ten fields (I checked: every row has ten) and every numeric column used by the script is correct
— DE 12,701, NL 5,603, HU implied 6,142, TR implied 24,062 — but the provenance text is truncated and
fragments land in `note` ("701)", "6142", "24062"). *Fix:* quote those four `how_read` fields, or drop the
thousands separators inside them. No figure changes.

**D. H-work's expected resolution says "about 2.5 of 26"; its usable set is 27 of 27.** The 26 is mine: §E of
my re-derivation ran on the 26 EU members that had a bound before NL was added. Recomputed on the corrected
bounds (`power_rules.json` overall gap SEs, the disclosed EU27 work−private of −2.51, no country-level
value read): **2.6 of 27**. *Fix:* in H-work, "Expected resolution", replace "would be about 2.5 of 26" with
"would be about 2.6 of 27".

**E. The pointer to the brief review was dropped from the header.** Revision 1 read "Review of the brief:
`notes/brief-review.md`."; revision 2 does not. *Fix:* restore the sentence, or say in the notebook that the
pointer moved.

## What the revision broke

Nothing in the rules. I checked the whole diff hunk by hunk for changes outside the sixteen items: the only
ones are the BRIEF edit (A), the dropped brief-review pointer (E), "agrees on every cell" → "every common
cell" in §1 (correct; the mirror is not in this sandbox and the narrower claim is the defensible one),
"classified against the primary set's cut points" → "placed against the primary set's cut values" in §4
(aligns with the new class rule), "class changes" → "tercile changes" throughout the Interpretation and
robustness lists (consistent with item 3), and one addition to the synthetic-recovery list ("a table with one
implanted large-gap geography and the rest equal must class exactly that geography large-gap on all three
measures"), which is a new check on the analyst, not a relaxation. No hypothesis, threshold, set, exclusion,
denominator or failure condition changed except as the sixteen items required.

## Re-run of script 01

`python3 data/fetch/eurostat_isoc_ai_iaiu.py` → `isoc_ai_iaiu.tsv` sha256 `7f668f7b…` (the pre-registration's
hash), `demo_pjan_EU27_2025.json` flag `ep`. Script 01 run from a scratch copy (I do not write the analyst's
files); its output is **byte-identical to the committed `power_rules.json`**. Printed:

```
countries with a bound: 33; EU age weights [0.131, 0.158, 0.179, 0.189, 0.188, 0.155]
overall gap 95% half-width: median 2.8 pp (min 0.88, max 4.71); by band medians
  {'Y16_24': 7.78, 'Y25_34': 7.34, 'Y35_44': 6.73, 'Y45_54': 6.06, 'Y55_64': 5.0, 'Y65_74': 3.67}
published/SRS SE ratio on the reference indicator: median 1.09 over 30 countries (1 = SRS holds)
CHECKS PASSED
```

Against §5 of the pre-registration: median 2.8 ✓, 33 geographies ✓, IT 0.88 ✓, DE 1.63 ✓, NL 2.60 ✓,
DK 3.15 ✓, MT 4.71 ✓, band medians 7.8 → 3.7 ✓, "within 9% of the SRS value at the median across 30
countries" ✓ (1.09), the above-1.3 list ✓ (§ item 1 above). Against §9: age weights ✓, band rates
63.8 / 50.7 / 39.0 / 28.4 / 16.5 / 6.5 ✓ (63.81, 50.65, 38.96, 28.35, 16.49, 6.50). Every §5 figure quoted in
the pre-registration is the script's own output; none is stale from revision 1.

## What I could not verify

- Anything I did not re-open by design: the brief's other sections, the feasibility note, the audit file's
  contents, the EIGE mirror, the triangulation legs.
- Any country-level gap, ratio, band, education or standardised value — barred, and not needed for any item.
- Whether IE's 2022–23 precision block describes the 2025 sample, and the net sample of individuals for HU,
  TR, MK and XK: unchanged from the first verdict, and now disclosed in §5 as such.
