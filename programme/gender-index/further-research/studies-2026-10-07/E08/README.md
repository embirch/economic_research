# E08 execution package

Revised author-review draft, 8 October 2026, with the original 7 October calculations unchanged. The study follows the reviewed selected E08 protocol and discloses substantial prior outcome inspection. Separate numerical reconstruction and automated scientific and editorial review are complete. These are not human peer review or approval to publish. No public deployment, commit, push or paid service was used.

Start with `manuscript.md`. `METHODS.md` gives measures, exact targets, design-based public bootstrap, support diagnostics, quality and interpretation. `literature-review.md` records primary-source reading and the limit on access to the latest Jiang full text. `CLAIMS.csv` maps claims to stable estimates or source documentation. `DEVIATIONS.md` preserves the original execution record; the 8 October revision record is held in the parent publication-review package.

Reproduce with Python 3 and numpy/pandas:

```sh
python /path/to/E08/analysis.py --cache /path/to/E08-cache
python /path/to/E08/verify_outputs.py
```

The cache contains the five exact files in `source-manifest.json`; their hashes are checked before analysis. The project's active ignored cache is `data/cache/selected-studies/E08` relative to the repository. The script accepts any directory containing the pinned files. No old analysis helpers are imported. It recomputes all 1,000 replicate paths and writes no respondent records, identifiers, fitted records or weights.

The analytical script remains unchanged. The shared `build_site.py --study E08` presentation step reapplies `presentation-copy.json` to regenerated figure specifications before producing the revised HTML and SVGs. This preserves the reviewed labels and optional full-frequency view without modifying numerical rows. In an extracted reproduction bundle, run that command from the bundle's top-level directory after the analysis. The PDF builder uses the same presentation specification.

Public-safe aggregate layers are `public-tables.csv`, `support-summary.csv`, `percentile-sensitivity.csv` and `figure-specs.json`, subject to retaining their warnings and suppression. The frequency profile uses ordered dot rows with pointwise intervals. Source acknowledgement must accompany all rendered artifacts. Adapted from Statistics Canada, Canadian Survey on Working Conditions, 2024–2025. This does not constitute an endorsement by Statistics Canada of this product.

`results.json` is full-precision internal verification material, including failed-target diagnostics. Do not expose it as a public download. `environment.json` records versions and script SHA256. `verification.json` records output-integrity checks. A separate implementation has reconstructed the adjustment/common-composition paths from the pinned files, including joint covariance of same-support changes, without importing this estimator. Its 776 comparisons passed; those completed scientific checks are reused for this prose/presentation revision.

The complete core result is more frequent unpaid job work among users of either gender, with gender interaction sensitivity across descriptive targets. Primary raw interaction +3.4 points [0.5, 6.3]; additive +2.7 [−0.2, 5.6]; common occupation/sector −1.7 [−5.2, 1.7]; occupation/sector/education −1.0 [−4.5, 2.5]. The latter retains 99.4% of weight. Its restriction change rounds to 0.0 points and its composition change is −4.3 [−7.2, −1.4]. These are not AI treatment effects.

The bounded contribution is a Canadian comparison of reported use and a work-related outcome, with alternative job distributions explicit. It is not the first study of AI and working time, and it does not identify whether AI causes unpaid work or improves economic welfare.


## Unpaid-work-focused edition, 8 October 2026

At Emily’s request, the article and methods now focus on unpaid job-work frequency, its association with reported AI use, and gender comparisons at observed and common job compositions. The time-off outcome is no longer part of the article or its narrative argument. Original analytical outputs, source pins, script and complete released tables remain unchanged, including the previously calculated secondary outcome. Its source-quality suppression remains in place. The earlier full edition is preserved in `../../canada-focus-2026-10-08/before/`. This is a post-analysis change to the presentation scope, not a newly preregistered analysis or selective alteration of results.

## Approved editorial pass, 9 October 2026

The current article adds an earlier answer and a more explicit contribution, with the original analysis and results preserved. Prior versions are archived in `../../approved-revision-2026-10-09/before`.

Run `python export_scale.py` after the original analysis to reproduce the descriptive ratio explanation. The separate bounded influence diagnostic and its private-output rules are documented in Methods; it does not replace any original estimate.
