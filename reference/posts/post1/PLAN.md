# Post 1 · Culture or cohort · Research plan

Written 15 Sep 2026. Seven working days, 15–22 Sep. This file is the plan of record; deviations are logged in `notes/lab-notebook.md`, never silently.

## 1. Where everything lives

```
Desktop/Anthropic/research/post1/
  PLAN.md                 this file
  prereg/                 the OSF pre-registration text (written day 2, frozen before step 6)
  data/
    raw/                  untouched inputs: symlinks to bible/data/ei/… plus Hofstede, GLOBE, population files
    processed/            every table we build, as CSV, one per script, never edited by hand
  scripts/
    00_env.py             checks Python and packages, prints versions
    01_load_threshold.py  loads the four waves, applies the 200-conversation rule, writes country lists
    02_replicate.py       runs Anthropic's function on the Aug 2025 file; must return slope ≈ −3.11, R² ≈ 0.39
    03_repeat_waves.py    the same on Nov 2025, Feb 2026, Apr/May 2026
    04_build_table.py     one row per country per wave: outcome, residual, AUI, income, coding share, use domain, language group, Hofstede, GLOBE
    05_ceiling.py         the newness arithmetic
    06_main_test.py       the cross-country regression (H1 vs H3), MDE, robust SEs
    07_robustness.py      directive outcome, GLOBE, other dimensions, request-cluster adjustment, English-only
    08_panel.py           within-country test with country and wave fixed effects; Super Bowl test
    09_extension.py       June 2026 within-occupation-group test
    10_figures.py         the four figures
    run_all.sh            runs 01–10 in order; the release must reproduce from this alone
  outputs/
    tables/               regression tables as CSV and Markdown
    figures/              PNG and SVG
    checks/               each script's printed check block, saved
  notes/
    lab-notebook.md       dated entries in Emily's words: what was run, what it showed, what was decided
  README.md               how to reproduce; written last
```

Rules: raw data is never modified; every script reads from `raw/` or `processed/` and writes to `processed/` or `outputs/`; every script ends with a **check block** that prints the numbers we expect and stops with an error if they are wrong.

## 2. Tools

- Python 3.9 (installed) in a virtual environment at `research/.venv`, so nothing touches the system Python. Packages: pandas, numpy, statsmodels, scipy, matplotlib.
- Scripts, not notebooks, while learning: a script is a list of instructions read top to bottom, run with one command, and its output is a file. A notebook comes at the end, as the released artefact.
- VS Code (free) to read scripts with syntax colouring; the terminal in the Claude app to run them. Every script is annotated line by line.
- git in `research/`, one commit per completed step, so every version is recoverable. Pushed to GitHub at release.
- OSF for the pre-registration.

## 3. How each step runs

1. Claude writes the script and a plain-English explanation of what it does and why.
2. Emily reads the explanation, then the script, and asks anything unclear before running.
3. Emily runs it: `python3 scripts/0X_name.py`.
4. We read the check block together. If it fails, we find out why before touching anything else.
5. Emily writes the lab-notebook entry in her own words (three to six lines). Commit.

Nothing moves to the next step until the check block passes and the notebook entry exists.

## 4. The steps, with what "done" means

| Day | Step | Done means |
|---|---|---|
| 1 (Mon 15) | 00 environment; 01 load and threshold | Versions printed; four waves loaded; country counts match the audit (115 / 119 / 119 / 114 above threshold) |
| 1–2 | 02 exact replication | Slope within ±0.05 of −3.11, R² within ±0.01 of 0.394, same N as the report's figure. If not, stop and diagnose |
| 2 | 03 repeat on later waves; 04 build the table | Four slopes reported; the country table has one row per country-wave with no unexplained missing values; merge counts logged (how many countries have Hofstede, GLOBE, income, language) |
| 2 (evening) | Pre-registration written and frozen on OSF | Primary test, threshold for support, what counts against, controls, sample rule, MDE method, all fixed |
| 3 | 05 ceiling; 06 main test | Ceiling number; power-distance coefficient with robust SE, interval and MDE; income and adoption coefficients |
| 4 | 07 robustness | Table of the coefficient across specifications; VIFs |
| 5 | 08 panel and Super Bowl; 09 extension | Within-country coefficient with and without June; the US number against the pre-stated comparator set; the learning-heavy vs routine contrast |
| 6 | 10 figures; write-up from the skeleton | Four figures; placeholders replaced by real numbers; branch points resolved |
| 7 (Mon 22) | Rules check; README; release | Nine rules ticked; `run_all.sh` reproduces everything from raw; repo public; post published on the site |

## 5. Decisions fixed now, before data

- **Sample rule:** countries with ≥200 conversations in the wave, as in Anthropic's code. Micro-states are not excluded separately; a leave-one-out check reports any country that changes the coefficient by more than 25%.
- **Outcome:** task-mix-adjusted automation share, computed by Anthropic's function. Directive share is robustness only.
- **Primary test:** OLS of the residual automation share on standardised power distance, log GDP per working-age adult, AUI, coding share, personal-use share, and language-group dummies; HC3 robust standard errors; wave = August 2025 (the wave with GDP in-file). Support for H1 = power-distance coefficient positive with 95% interval excluding zero AND larger than the MDE. Against H1 = coefficient inside the MDE.
- **MDE:** the effect detectable at 80% power and 5% two-sided significance given the realised residual variance and N, computed from the fitted model.
- **Panel:** country and wave fixed effects, automation share on AUI; clustered SEs by country; run with and without the June 2026 waves.
- **Super Bowl test:** change in US task-mix-adjusted automation from Nov 2025 to Feb 2026, minus the same change averaged over the comparator set fixed now: Canada, UK, Australia, Ireland, New Zealand (English-majority, high-adoption, no comparable advertising event). Support for cohort = US change exceeds comparators by more than the comparator standard deviation.
- **Language groups:** majority language from the Stanford file with a 60% threshold; countries below it form an "other" group.
- **Culture merge:** Hofstede 2015 file on ISO-3; countries missing a power-distance score are dropped from the main test and listed.
- **No peeking:** the main test is run once, after the pre-registration is frozen. Exploration before that is limited to steps 01–04, which build inputs and do not touch power distance.

## 6. Things that could go wrong, and what we do

- Replication does not match: check threshold, the "none"/"not_classified" handling, the task list; if still off, report the discrepancy and use our number, stating both.
- Hofstede coverage leaves N < 80: report N, widen with GLOBE where Hofstede is missing only as a robustness run, never in the primary.
- Power distance and income are highly correlated: report VIFs; if VIF > 5, present the two-variable comparison as well as the joint model and say why.
- Panel coefficient is noisy: report it as suggestive; the cohort verdict rests on the ceiling and the Super Bowl test, and the write-up says so.
- June 2026 breaks comparability: the within-wave adjustment handles level shifts; the panel runs with and without it.

## 7. Stress tests, built into every step

Accuracy is checked by doing things twice in different ways, never by trusting one pass.

- **Two implementations of every key number.** The task-mix adjustment is computed with Anthropic's function and again with our own independent shift-share code; the two must agree to the decimal. The main regression is fitted with statsmodels and re-fitted with a hand-written least-squares calculation; the coefficients must match.
- **Expected-value check blocks.** Every script ends by asserting known facts from the audit and the reports (country counts, global shares, the published slope). A wrong number stops the script; nothing downstream runs on bad inputs.
- **Manual spot checks.** For three countries chosen in advance (India, Denmark, Singapore), the merged row is checked by hand against the raw file, the Hofstede CSV and the population file: same code, same value, same unit.
- **Merge audits.** After every merge, the script prints how many rows came in, how many matched, and which did not, by name. Unmatched country codes are resolved by hand, never dropped silently. Namibia's "NA" code is the known trap.
- **Unit and range checks.** Shares between 0 and 100 and summing to about 100; AUI positive; log income finite; power distance 0 to 100. Any value outside its range is printed.
- **Plot everything before modelling.** A histogram of each variable and a scatter of the outcome against each control, so a coding error shows up as a shape before it becomes a coefficient.
- **Synthetic-data test of the regression code.** Generate fake data with a known power-distance effect, run the same script, and confirm it recovers the effect. Then generate data with no effect and confirm it reports none.
- **Sign and magnitude sanity.** Before reading any coefficient as a finding, ask whether its size is plausible against the published numbers (the 8.7-point tenure gap, the 25-point spread). An implausibly large effect is treated as a bug until proven otherwise.
- **Leave-one-out and leave-one-wave-out.** Every headline coefficient is re-estimated dropping each country and each wave in turn; any single unit that moves it by more than 25% is named in the post.
- **Placebo outcome.** The main model run on an outcome culture should not predict (the share of conversations with unclassified collaboration). If power distance "predicts" that, something is wrong with the design.
- **Source re-check before citation.** Every number quoted from a report is re-read in the PDF on the day it is written into the post, and the page number is recorded in the notebook.
- **Red-team pass before writing.** Claude writes the strongest case against each finding as if reviewing for a journal; the write-up answers each point or concedes it.
- **Fresh-eyes reproduction.** On day 7, `run_all.sh` is executed from a clean folder; if any number in the post differs from the fresh output, the post is wrong, not the script.
