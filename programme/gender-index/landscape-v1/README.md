# Gender & AI landscape v1

Working research edition, 1 October 2026. Open [the local evidence explorer](index.html). This directory assembles the broad source/literature audit before selection of new deep-dive papers. It is not a worldwide prevalence estimate, a composite ranking, or a public launch.

## Reading order

1. [Explorer](index.html): findings, selected measures, geographic coverage, filterable source cards and emerging questions.
2. [Foundational report note](../FOUNDATION.md): Cranney, Delecourt and Koning's May 2026 synthesis and its role in our contribution.
3. [Research synthesis](research/SYNTHESIS.md) and [claims/evidence table](research/claims-evidence.csv).
4. [Source audit](../evidence/v1-audit-2026-10-01/AUDIT-REPORT.md), [source register](../evidence/v1-audit-2026-10-01/source-register.csv) and [pilot corrections](../evidence/v1-audit-2026-10-01/pilot-corrections.md).
5. [Coordinator review and inclusion decisions](REVIEW.md): what was independently checked and what remains limited. Read this alongside the specialist outputs.
6. [Emerging questions](research/emerging-questions.md), including Emily's [SimilarWeb candidate](coordination/emerging-questions.md). No new paper has been selected by this edition.

## Reproduce the presentation

From this directory, using Python 3's standard library:

```sh
python3 build_explorer.py
```

The build validates the reviewed `edition-data.json`, checks the European and UK displays against their saved extracts and writes `index.html` plus `build-manifest.json`. All display data are embedded; the explorer needs no server, account, network connection or external JavaScript library. Source links require connectivity. The filterable register can be exported as CSV from the page. Building the presentation does not constitute a new scientific review.

The template is `explorer.template.html`. Edit reviewed content in `edition-data.json`, record substantive decisions in `REVIEW.md`, then rebuild. Do not edit generated `index.html` alone. Rebuilding must not fetch live observations or silently replace source vintages.

## Recheck source extracts

The read-only European adapter consumes immutable Git objects from the first paper's local repository. It checks the pinned input hashes, source cells, flags, eligible coverage and existing descriptive differences. It writes only into this repository:

```sh
python3 coordination/import_europe.py /path/to/gender-gap-generative-ai
```

The article commit and source hashes are in `coordination/europe-published-cells.json`. The adapter imports the EU27 plus EU aggregate, with four use measures on the all-individuals denominator. It does not regenerate manuscripts or figures, import arbitrary article code, change the source repository, or silently follow a later article revision. The first paper's non-EU extension, age/education analyses and sensitivity results are outside this display. Current article GitHub access limitations do not prevent building this edition from the committed extract.

Additional checks use local copies of permitted public aggregate tables/pages:

```sh
python3 coordination/check_dsit.py /path/to/dsit-ai-2025-2026.ods
python3 coordination/check_public_tables.py /path/to/snapshot-directory
```

The latter expects `canada-cswc.html`, `pew-gender.html` and `brazil-m1.html`. URLs and hashes are recorded in the scripts and `published-table-checks.json`; the DSIT record is in `dsit-published-cells.json`. Source copies are outside Git in coordinator scratch, not redistributed with the edition. Pages may change, including dynamic HTML: a hash mismatch requires an explicit new-vintage audit rather than bypassing the pin. The DSIT script prints an extract; compare it with the saved JSON. The HTML-page script rewrites its checked extract only after all pinned-cell checks pass. No new gaps, confidence intervals or models are estimated by these two source checks.

## Evidence and updates

The explorer combines existing European calculations with clearly attributed published results elsewhere. Raw respondent data, restricted material, provider archives and credentials are excluded. Source-specific reuse terms remain attached to the underlying records; the repository's visibility does not waive those terms.

Country, aggregate and study/sample-family identifiers serve different purposes. In particular, the HBS synthesis and its constituent surveys are not independent replications, and three Eurostat indicator records come from the same source family. Gender-category labels and survey populations remain source-specific. Occupational composition and inferred platform demographics cannot become self-reported individual gender.

Next iterations should be driven by the findings and explicit gaps: resolve specific access/measurement blockers, define a distinct original question, assess its feasible data and methods, and then commission a bounded study. Feed reviewed findings back into the landscape and propose warranted revisions to the living European paper while preserving author edits.

AI assistance: existing deployed Claude specialists provided source audit and literature synthesis; Codex coordinated, checked selected primary evidence, imported existing results, assembled the explorer and reviewed it. Emily retains scientific and editorial ownership. Internal checks do not substitute for external peer review or author approval of a public release.
