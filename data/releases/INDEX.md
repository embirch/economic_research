# Economic Index release index

Enumeration of every folder and file of the Hugging Face dataset `Anthropic/EconomicIndex`,
verbatim from the tree API. Enumeration only: no file was opened or profiled here; schemas,
grains, facets, metrics, thresholds and traps go in `data/releases/<release>.md`, one per folder.

- Repository: <https://huggingface.co/datasets/Anthropic/EconomicIndex>
- Revision enumerated: commit `2ea58ff75e4247d26810c37f10c179edc2466cac` (`x-repo-commit` on `resolve/main`), dataset `lastModified` `2026-06-26T23:21:00.000Z`
- Enumerated: 2026-09-16
- Licence: the dataset card body says "Data released under CC-BY, code released under MIT License."; the card's YAML front matter and the API `cardData.license` say `mit` only (see Discrepancies)
- Totals: 8 folders with files (7 data folders + repository root), 18 directories, **83 files, 663,867,600 bytes** (633.1 MiB). 40 of the 83 files are Git-LFS pointers; the tree API `size` field equals the real content size (`lfs.size`) for those, so the sizes below are content sizes, not pointer sizes.

## Folders

| release | folder path | report it accompanies (from the dataset card) | files | total bytes | data files (csv/tsv/parquet) | code and notebooks (py/ipynb) | documentation (md/pdf) | notes |
|---|---|---|---:|---:|---:|---:|---:|---|
| — (repository root) | `/` | — (card itself) | 3 | 8,344 | 0 | 0 | 1 (`README.md`) | plus `.gitattributes` (LFS rules), `.gitignore` (`.DS_Store`) |
| labour-market impacts | `labor_market_impacts/` | "Labor market impacts: Job exposure and task penetration data" → <https://www.anthropic.com/research/labor-market-impacts> | 2 | 1,926,998 | 2 | 0 | 0 | **no documentation file in the folder**; not dated, not versioned |
| 2025-02-10 (1st) | `release_2025_02_10/` | "Initial release with O\*NET task mappings, automation vs. augmentation data, and more" → 1st report <https://www.anthropic.com/news/the-anthropic-economic-index> | 14 | 5,239,526 | 6 | 1 (`plots.ipynb`) | 1 (`README.md`) | plus 6 `.png` figures in `plots/` |
| 2025-03-27 (2nd) | `release_2025_03_27/` | "Updated analysis with Claude 3.7 Sonnet data and cluster-level insights" → 2nd report <https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7>; paper arXiv:2503.04761 | 16 | 10,308,805 | 9 | 2 (`v2_report_replication.ipynb`, `cluster_level_data/cluster_level_example_analysis.ipynb`) | 2 (`README.md`, `cluster_level_data/README.md`) | plus 3 `.png`; only release with a published replication notebook |
| 2025-09-15 (3rd) | `release_2025_09_15/` | "Updated analysis with geographic and first-party API data using Sonnet 4" → 3rd report <https://www.anthropic.com/research/anthropic-economic-index-september-2025-report> | 38 | 60,997,757 | 19 | 10 (`code/`: 6 py + 4 ipynb) | 2 (`README.md`, `data_documentation.md`) | plus 2 `.xlsx`, 2 `.txt`, 3 `.json`; only release with a `code/` library and with `data/input`, `data/intermediate`, `data/output` |
| 2026-01-15 (4th) | `release_2026_01_15/` | "Updated analysis with economic primitives and Sonnet 4.5" → 4th report <https://www.anthropic.com/research/anthropic-economic-index-january-2026-report> | 4 | 141,659,531 | 2 | 0 | 2 (`data_documentation.md`, `aei_v4_appendix.pdf`) | raw files only, under `data/intermediate/`; only release with a PDF appendix |
| 2026-03-24 (5th) | `release_2026_03_24/` | "Updated analysis with Opus 4.5/4.6 and learning curves" → 5th report <https://www.anthropic.com/research/economic-index-march-2026-report> | 3 | 147,262,094 | 2 | 0 | 1 (`data_documentation.md`) | raw files under `data/` (no `intermediate/` level) |
| 2026-06-26 (6th) | `release_2026_06_26/` | "Updated analysis with Artifacts and monthly aggregates" → 6th report <https://www.anthropic.com/research/economic-index-june-2026-report> | 3 | 296,464,545 | 2 | 0 | 1 (`data_documentation.md`) | largest folder; file names carry the release date, not a data window |

Ordinals ("1st"…"6th") come from the card's citation blocks, matched to folders by date; the
card's "Data Releases" list does not state ordinals. Report URLs are the card's, not fetched here.

Components visible from the enumeration alone: Claude.ai and first-party API files (2025-09-15
onward), O\*NET/SOC/BLS/wage reference files (2025-02-10, 2025-03-27, 2025-09-15 `data/input`),
the labour-market files, and one released analysis library plus notebooks (2025-09-15,
2025-03-27, 2025-02-10). **No folder or file whose name mentions Claude Code, and no survey
file other than `release_2025_09_15/data/input/BTOS_National.xlsx`** (Census Business Trends and
Outlook Survey input). Whether Claude Code or survey content sits inside a column of the
Claude.ai files is a profiling question for the per-release notes, not settled here.

### (root)  (3 files, 8344 bytes)

| bytes | path |
|---:|---|
| 3299 | `.gitattributes` |
| 10 | `.gitignore` |
| 5035 | `README.md` |

### labor_market_impacts  (2 files, 1926998 bytes)

| bytes | path |
|---:|---|
| 37176 | `labor_market_impacts/job_exposure.csv` |
| 1889822 | `labor_market_impacts/task_penetration.csv` |

### release_2025_02_10  (14 files, 5239526 bytes)

| bytes | path |
|---:|---|
| 2981 | `release_2025_02_10/README.md` |
| 77176 | `release_2025_02_10/SOC_Structure.csv` |
| 197 | `release_2025_02_10/automation_vs_augmentation.csv` |
| 1132 | `release_2025_02_10/bls_employment_may_2023.csv` |
| 461306 | `release_2025_02_10/onet_task_mappings.csv` |
| 3592256 | `release_2025_02_10/onet_task_statements.csv` |
| 25886 | `release_2025_02_10/plots.ipynb` |
| 38030 | `release_2025_02_10/plots/automation_vs_augmentation.png` |
| 141804 | `release_2025_02_10/plots/occupational_category_distribution.png` |
| 230300 | `release_2025_02_10/plots/occupational_category_distribution_bls.png` |
| 104710 | `release_2025_02_10/plots/occupations_distribution.png` |
| 221631 | `release_2025_02_10/plots/task_distribution.png` |
| 214070 | `release_2025_02_10/plots/wage_distribution.png` |
| 128047 | `release_2025_02_10/wage_data.csv` |

### release_2025_03_27  (16 files, 10308805 bytes)

| bytes | path |
|---:|---|
| 3205 | `release_2025_03_27/README.md` |
| 77176 | `release_2025_03_27/SOC_Structure.csv` |
| 672136 | `release_2025_03_27/automation_augmentation_by_occupation.png` |
| 149993 | `release_2025_03_27/automation_augmentation_comparison.png` |
| 561368 | `release_2025_03_27/automation_vs_augmentation_by_task.csv` |
| 197 | `release_2025_03_27/automation_vs_augmentation_v1.csv` |
| 198 | `release_2025_03_27/automation_vs_augmentation_v2.csv` |
| 2917 | `release_2025_03_27/cluster_level_data/README.md` |
| 947989 | `release_2025_03_27/cluster_level_data/cluster_level_dataset.tsv` |
| 280733 | `release_2025_03_27/cluster_level_data/cluster_level_example_analysis.ipynb` |
| 854296 | `release_2025_03_27/normalized_automation_by_category.png` |
| 3592256 | `release_2025_03_27/onet_task_statements.csv` |
| 461306 | `release_2025_03_27/task_pct_v1.csv` |
| 435372 | `release_2025_03_27/task_pct_v2.csv` |
| 372332 | `release_2025_03_27/task_thinking_fractions.csv` |
| 1897331 | `release_2025_03_27/v2_report_replication.ipynb` |

### release_2025_09_15  (38 files, 60997757 bytes)

| bytes | path |
|---:|---|
| 2640 | `release_2025_09_15/README.md` |
| 76365 | `release_2025_09_15/code/aei_analysis_functions_1p_api.py` |
| 92526 | `release_2025_09_15/code/aei_analysis_functions_claude_ai.py` |
| 8079 | `release_2025_09_15/code/aei_report_v3_analysis_1p_api.ipynb` |
| 22150 | `release_2025_09_15/code/aei_report_v3_analysis_claude_ai.ipynb` |
| 18565 | `release_2025_09_15/code/aei_report_v3_change_over_time_claude_ai.py` |
| 85914 | `release_2025_09_15/code/aei_report_v3_preprocessing_claude_ai.ipynb` |
| 11748 | `release_2025_09_15/code/preprocess_gdp.py` |
| 3226 | `release_2025_09_15/code/preprocess_iso_codes.py` |
| 5279 | `release_2025_09_15/code/preprocess_onet.py` |
| 13542 | `release_2025_09_15/code/preprocess_population.py` |
| 63052 | `release_2025_09_15/data/input/BTOS_National.xlsx` |
| 2176 | `release_2025_09_15/data/input/Population by single age _20250903072924.csv` |
| 197 | `release_2025_09_15/data/input/automation_vs_augmentation_v1.csv` |
| 198 | `release_2025_09_15/data/input/automation_vs_augmentation_v2.csv` |
| 1663 | `release_2025_09_15/data/input/bea_us_state_gdp_2024.csv` |
| 1485 | `release_2025_09_15/data/input/census_state_codes.txt` |
| 31667 | `release_2025_09_15/data/input/geonames_countryInfo.txt` |
| 265358 | `release_2025_09_15/data/input/imf_gdp_raw_2024.json` |
| 1204658 | `release_2025_09_15/data/input/onet_task_statements_raw.xlsx` |
| 818707 | `release_2025_09_15/data/input/sc-est2024-agesex-civ.csv` |
| 77176 | `release_2025_09_15/data/input/soc_structure_raw.csv` |
| 461306 | `release_2025_09_15/data/input/task_pct_v1.csv` |
| 435372 | `release_2025_09_15/data/input/task_pct_v2.csv` |
| 22974 | `release_2025_09_15/data/input/working_age_pop_2024_country_raw.csv` |
| 7027019 | `release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv` |
| 18894517 | `release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv` |
| 4115 | `release_2025_09_15/data/intermediate/gdp_2024_country.csv` |
| 2179 | `release_2025_09_15/data/intermediate/gdp_2024_us_state.csv` |
| 4564 | `release_2025_09_15/data/intermediate/iso_country_codes.csv` |
| 3650862 | `release_2025_09_15/data/intermediate/onet_task_statements.csv` |
| 78834 | `release_2025_09_15/data/intermediate/soc_structure.csv` |
| 6321 | `release_2025_09_15/data/intermediate/working_age_pop_2024_country.csv` |
| 1079 | `release_2025_09_15/data/intermediate/working_age_pop_2024_us_state.csv` |
| 26840881 | `release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv` |
| 302699 | `release_2025_09_15/data/output/request_hierarchy_tree_1p_api.json` |
| 438531 | `release_2025_09_15/data/output/request_hierarchy_tree_claude_ai.json` |
| 20133 | `release_2025_09_15/data_documentation.md` |

### release_2026_01_15  (4 files, 141659531 bytes)

| bytes | path |
|---:|---|
| 6036245 | `release_2026_01_15/aei_v4_appendix.pdf` |
| 41518256 | `release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv` |
| 94086309 | `release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv` |
| 18721 | `release_2026_01_15/data_documentation.md` |

### release_2026_03_24  (3 files, 147262094 bytes)

| bytes | path |
|---:|---|
| 43957174 | `release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv` |
| 103287181 | `release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` |
| 17739 | `release_2026_03_24/data_documentation.md` |

### release_2026_06_26  (3 files, 296464545 bytes)

| bytes | path |
|---:|---|
| 77282477 | `release_2026_06_26/data/aei_1p_api_2026-06-26.csv` |
| 219174671 | `release_2026_06_26/data/aei_claude_ai_2026-06-26.csv` |
| 7397 | `release_2026_06_26/data_documentation.md` |

## Directories with no files of their own

`release_2025_02_10/plots`, `release_2025_03_27/cluster_level_data`, `release_2025_09_15/code`,
`release_2025_09_15/data`, `release_2025_09_15/data/{input,intermediate,output}`,
`release_2026_01_15/data`, `release_2026_01_15/data/intermediate`, `release_2026_03_24/data`,
`release_2026_06_26/data` all appear as `type: directory` entries in the tree; the 18 directory
entries are listed by the first command in Verification. No folder other than the eight above
contains files.

## Discrepancies

1. **Card config points at a file that does not exist.** The card's YAML declares
   `config_name: release_2026_01_15` with `split: raw_1p_api` at
   `release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv`. That path
   is absent from the tree and `resolve/main` returns **404**; the November 2025 API file is at
   `release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv` (HTTP 206
   on a range request). The folder prefix in the card is wrong. Anything that loads the dataset
   through `datasets`/the viewer config for that split will fail; fetch by explicit path.
2. **Licence stated twice, differently.** Card body: data CC-BY, code MIT. Card YAML and API
   `cardData.license`: `mit`. Repo tags carry `license:mit` only. Treat data as CC-BY (attribute
   Anthropic) and code as MIT; cite the body text, and do not rely on the HF licence tag.
   The `economic-index-data` skill says "CC-BY 4.0" — the card says "CC-BY" without a version.
3. **No `config_name` for any release except 2026-01-15**, so the HF viewer covers one release
   only; the other five releases and `labor_market_impacts/` are files-only.
4. **Releases 2026-01-15, 2026-03-24, 2026-06-26 ship no code**, although the reports they
   accompany describe derived quantities (AUI, adjusted automation, buckets). Only 2025-09-15
   (`code/`), 2025-03-27 (`v2_report_replication.ipynb`) and 2025-02-10 (`plots.ipynb`) do.
   Replication of the later reports must re-implement from the 2025-09-15 library plus the
   `data_documentation.md` of the wave.
5. **`labor_market_impacts/` has no README, no documentation file and no date** in the folder or
   in any file name; its vintage cannot be established from the enumeration.
6. **Path-shape drift between waves** (matters for fetch scripts): 2025-09-15 uses
   `data/{input,intermediate,output}/`; 2026-01-15 uses `data/intermediate/`; 2026-03-24 and
   2026-06-26 use `data/` flat; 2025-02-10 and 2025-03-27 put data files at the folder root.
   File-name drift too: `aei_raw_*` in 2025-09-15 → 2026-03-24, but `aei_*` (no `raw`) in
   2026-06-26, and 2026-06-26 names the file by release date while earlier waves name it by the
   data window.
7. Per-release `README.md` exists only for 2025-02-10, 2025-03-27 and 2025-09-15;
   `data_documentation.md` only for 2025-09-15 onward. 2025-09-15 is the only folder with both.

## Verification

All commands run 2026-09-16 from this sandbox; the tree API is reachable without a token.

```bash
# 1. Full recursive tree of the repository root (101 entries: 83 files, 18 directories).
curl -sS 'https://huggingface.co/api/datasets/Anthropic/EconomicIndex/tree/main?recursive=true' -o /tmp/hf_root.json
python3 -c "import json;d=json.load(open('/tmp/hf_root.json'));print(len(d),sum(e['type']=='file' for e in d),sum(e['type']=='directory' for e in d))"
#   -> 101 83 18
python3 -c "import json;d=json.load(open('/tmp/hf_root.json'));[print(e['type'][:1],e['size'],e['path']) for e in sorted(d,key=lambda x:x['path'])]"
#   -> the per-folder tables above, verbatim

# 2. Single page, so the listing is complete: the response carries no Link header.
curl -sS -D - -o /dev/null 'https://huggingface.co/api/datasets/Anthropic/EconomicIndex/tree/main?recursive=true' | grep -i '^link:'   # no output

# 3. Cross-check: each top-level folder enumerated on its own, union compared with (1).
for d in labor_market_impacts release_2025_02_10 release_2025_03_27 release_2025_09_15 \
         release_2026_01_15 release_2026_03_24 release_2026_06_26; do
  curl -sS -o "/tmp/tree_$d.json" -w "$d %{http_code}\n" \
    "https://huggingface.co/api/datasets/Anthropic/EconomicIndex/tree/main/$d?recursive=true"
done
#   -> all 200; union = 80 files, identical paths and identical sizes to (1); zero mismatches
#   -> per-folder (files, bytes): labor_market_impacts (2, 1926998); 2025_02_10 (14, 5239526);
#      2025_03_27 (16, 10308805); 2025_09_15 (38, 60997757); 2026_01_15 (4, 141659531);
#      2026_03_24 (3, 147262094); 2026_06_26 (3, 296464545); root files (3, 8344)

# 4. LFS sizes are content sizes, not pointer sizes (40 files carry an "lfs" block whose
#    lfs.size equals the "size" field; pointerSize is ~130 bytes).
python3 -c "import json;d=json.load(open('/tmp/hf_root.json'));f=[e for e in d if e['type']=='file'];print(sum('lfs' in e for e in f), all(e['lfs']['size']==e['size'] for e in f if 'lfs' in e))"
#   -> 40 True

# 5. Dataset card and metadata (licence, config list, revision).
curl -sSL 'https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/README.md' -o /tmp/hf_readme.md   # 200, 5035 bytes
curl -sS  'https://huggingface.co/api/datasets/Anthropic/EconomicIndex' -o /tmp/hf_meta.json
python3 -c "import json;m=json.load(open('/tmp/hf_meta.json'));print(m['sha'],m['lastModified'],m['cardData']['license'],m['tags'])"
#   -> 2ea58ff75e4247d26810c37f10c179edc2466cac 2026-06-26T23:21:00.000Z mit ['language:en','license:mit','arxiv:2503.04761','region:us',...]

# 6. Discrepancy 1: the card's config path 404s, the real path is live.
curl -sSIL -o /dev/null -w '%{http_code}\n' 'https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv'   # 404
curl -sSL -r 0-0 -o /dev/null -w '%{http_code}\n' 'https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv'  # 206

# 7. Revision pinned from a data request, not only from the API.
curl -sSIL 'https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2026_06_26/data_documentation.md' | grep -i 'x-repo-commit'
#   -> x-repo-commit: 2ea58ff75e4247d26810c37f10c179edc2466cac

# 8. Repository .gitignore content (one line, 10 bytes).
curl -sSL 'https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/.gitignore'   # -> .DS_Store
```

Rate limit observed on the tree API: `ratelimit-policy: "fixed window";"api";q=500;w=300`
(500 requests per 5 minutes, unauthenticated) — ample for a full re-enumeration.

## Dated log

- **2026-09-16** — First enumeration, at commit `2ea58ff`. 8 folders with files, 83 files,
  663,867,600 bytes. Seven discrepancies recorded above; the card's `raw_1p_api` config path is
  the one that will bite a loader. No Claude Code file and no survey file beyond
  `BTOS_National.xlsx` exist anywhere in the tree. Per-release profiling notes
  (`data/releases/<release>.md`) and `data/ATLAS.md` still to be written.
