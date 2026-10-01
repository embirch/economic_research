# UK DSIT: first v1 source check

Codex, 1 October 2026. Proposed source ID `UK_DSIT_USE`; family `UK_DSIT_PES_2025_2026`. This is a coordinator audit note, not approval of a comparable international indicator or a new deep-dive study.

The [DSIT release](https://www.gov.uk/government/statistics/dsit-public-engagement-survey-20252026), published 16 July 2026, supplies public aggregate AI tables. The [report](https://www.gov.uk/government/statistics/dsit-public-engagement-survey-20252026/dsit-public-engagement-survey-20252026) describes UK adults aged 16+, surveyed November 2025–March 2026, using an address-based, stratified random sample and web/paper questionnaires. It reports 30,698 final respondents; individual table bases differ. This check acquired aggregates, not respondent data. The GOV.UK publication carries OGL v3 subject to stated exceptions; retain attribution and review any exceptions before a release.

## Cells checked

[Artificial intelligence workbook](https://assets.publishing.service.gov.uk/media/6a58999031fb6daf314137c5/DSIT_Public_Engagement_Survey_2025_2026_artificial_intelligence_tables.ods), `Table_E5`, columns B–F:

| Source category | Use in previous three months (%) | Unweighted base | Row |
|---|---:|---:|---:|
| Male | 63.2 | 13,902 | 38 |
| Female | 55.5 | 15,953 | 39 |
| Identify in another way | 49.2 | 99 | 40 |
| Prefer not to say | 45.0 | 671 | 41 |

These reproduce published weighted estimates; we have not estimated a new gender gap. The source includes text/speech generators, image/video/music tools **and autonomous workplace AI** in its use definition (`Notes!B16`). It is therefore not automatically equivalent to Eurostat's measure. UK coverage includes ages above 74.

The [online questionnaire](https://www.gov.uk/government/statistics/dsit-public-engagement-survey-20252026/dsit-public-engagement-survey-20252026-online-questionnaire), `GENDER`, asks respondents to describe themselves. Preserve the provider's categories; the third category cannot be relabelled as all nonbinary people. Its much smaller base needs visible precision caveats.

`Table_E7` purpose questions are multi-response and online-only, with separate weights (`Notes!B7`, `B17:B18`); they cannot inherit E5's all-adult denominator. Bases are item-specific. Suppression applies below 30 respondents or five responses (`Notes!B10`). No confidence interval is supplied in inspected E5 cells; do not derive survey precision from base counts alone.

## Reproduction and next checks

The local workbook is outside Git at `/private/tmp/gender-index-v1-coordinator/dsit-ai-2025-2026.ods`. It has 325,288 bytes and SHA-256 `a34ed705b6f8c2966d82586917befaae975fee8f61206ef3a2d679cc95c4610a`. The standard-library extractor verifies this exact vintage, headers, labels and selected coordinates; it preserves displayed precision and fails if the file changes.

From this directory:

```sh
python3 check_dsit.py /private/tmp/gender-index-v1-coordinator/dsit-ai-2025-2026.ods
```

Output is retained in [dsit-published-cells.json](dsit-published-cells.json). It contains only the selected published aggregates and provenance. A later download needs a fresh check if its hash differs.

Before v1 integration: inspect technical weighting/variance documentation and paper-questionnaire consistency, establish whether finer joint gender/age cells or permitted microdata exist, and review the proposed source card. Use a national module with its definition attached; cross-country ordering is unsupported. Acquisition and benchmark checking are not original empirical research; questions for later reanalysis remain open.

### Subsequent coordinator check

The [technical report](https://www.gov.uk/government/statistics/dsit-public-engagement-survey-20252026/dsit-public-engagement-survey-20252026-technical-report), sections 7.5–8.2, was checked later on 1 October. It describes design, response and calibration weighting, with separate mixed-mode and web weights. It says logit confidence intervals were produced using R's survey package. Those limits are not present in the E5 cells extracted here; their release location remains unresolved. The reported overall weighting design effect of 1.67 is not a verified variance for a gender difference and must not be used as one. Raking matches selected margins and does not establish unbiased relationships between variables. The paper-instrument and microdata checks remain open.
