#!/bin/zsh
# Reproduces every table and figure from raw data. Run from research/post1:  zsh scripts/run_all.sh
set -e
PY=../.venv/bin/python
for s in 00_env 01_load_threshold 02_replicate 03_repeat_waves 04_build_table 05_ceiling 06_main_test 07_robustness 08_panel 09_extension 10_figures 11_unbundle 12_unbundle_checks 13_which_pattern 14_all_groups 15_institutions 16_activities 17_composition_within_groups 18_education_systems 19_wvs 20_us_states 21_june_subregions 22_fig7; do
  echo "=== $s"; $PY scripts/$s.py 2>&1 | grep -v Warning | tee outputs/checks/${s%%_*}.txt | tail -3
done
echo "ALL STEPS PASSED"
