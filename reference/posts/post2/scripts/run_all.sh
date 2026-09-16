#!/bin/zsh
# Reproduces every table and figure from raw data. Run from research/post2:  zsh scripts/run_all.sh
set -e
PY=../.venv/bin/python
for s in 01_load_states 02_replicate 03_stage1_selection 04_stage2_mix 05_place 06_catchup 07_providers 08_figures 09_outliers 10_leisure 11_mechanisms 12_after_jobs 13_figures_outliers; do
  echo "=== $s"; $PY scripts/$s.py 2>&1 | grep -v "Warning\|cols=\[c for" | tee outputs/checks/${s%%_*}.txt | tail -2
done
echo "ALL STEPS PASSED"
