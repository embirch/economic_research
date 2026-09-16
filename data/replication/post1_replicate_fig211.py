"""Run Anthropic's OWN released code (release_2025_09_15/code/aei_analysis_functions_claude_ai.py)
to reproduce Figure 2.11 and its per-task automation rates -- the estimator post1 extends.
geopandas is not installed in this sandbox and is imported at module scope but not used by the
functions called here, so a stub module is injected. Writes /tmp/p1/d_out.txt.
"""
import sys, types, os
import pandas as pd, numpy as np

ROOT = '/workspace/economic_research/'
import os as _os; _os.makedirs('/tmp/p1', exist_ok=True)
OUT = open('/tmp/p1/d_out.txt', 'w')
def p(*a):
    print(*a); print(*a, file=OUT)

for name in ('geopandas', 'plotly', 'plotly.express', 'plotly.graph_objects'):
    if name not in sys.modules:
        m = types.ModuleType(name); m.__dict__['__getattr__'] = lambda k: None
        sys.modules[name] = m

code_dir = ROOT + 'data/cache/release_2025_09_15/code'
sys.path.insert(0, code_dir)
cwd = os.getcwd(); os.chdir(code_dir)          # the library hard-codes ../data/... paths
import aei_analysis_functions_claude_ai as A
p('released library imported: %s' % A.__file__)
p('constants: MIN_OBSERVATIONS_COUNTRY=%s MIN_OBSERVATIONS_US_STATE=%s EXCLUDED_COUNTRIES=%d'
  % (A.MIN_OBSERVATIONS_COUNTRY, A.MIN_OBSERVATIONS_US_STATE, len(A.EXCLUDED_COUNTRIES)))

enr = ROOT + 'data/cache/release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv'
df = pd.read_csv(enr, keep_default_na=False, na_values=[])
df['value'] = pd.to_numeric(df['value'])
p('enriched file rows %d' % len(df))

res = A.collaboration_task_regression(df, geography='country')
p('collaboration_task_regression(geography="country") -> slope %.6f  partial_r2 %.6f  p %.3e  '
  'n_countries %s  n_tasks %s'
  % (res['partial_slope'], res['partial_r2'], res['partial_pvalue'], res['n_countries'], res['n_tasks']))
p('  published (report Fig 2.11): -3.112 / 0.394 / N 111')

# --- the per-task automation rates the released code builds, and the global usage-weighted mean
tc = A.filter_df(df, facet='onet_task::collaboration', geography='global', geo_id='GLOBAL',
                 variable='onet_task_collaboration_pct').copy()
tc['task_name'] = tc['cluster_name'].str.split('::').str[0]
tc['collab_type'] = tc['cluster_name'].str.split('::').str[1]
p('released parser uses .split("::").str[0]/[1]: cluster_names with more than one "::": %d'
  % (tc.cluster_name.str.count('::') > 1).sum())
def is_automation(c):
    if c in ['directive', 'feedback loop']: return True
    if c in ['validation', 'task iteration', 'learning']: return False
    return None
tc['is_automation'] = tc['collab_type'].apply(is_automation)
valid = tc[tc.task_name != 'not_classified']
rates = {}
for t in valid.task_name.unique():
    d = valid[(valid.task_name == t) & (valid.is_automation.notna())]
    if d.empty or d.value.sum() == 0:
        continue
    rates[t] = d[d.is_automation].value.sum() / d.value.sum() * 100
p('per-task automation rates built by the released spec: %d tasks (includes the `none` task node: %s)'
  % (len(rates), 'none' in rates))

gt = A.filter_df(df, facet='onet_task', geography='global', geo_id='GLOBAL', variable='onet_task_pct').copy()
p('global onet_task_pct rows %d' % len(gt))
for drop in (['not_classified'], ['not_classified', 'none']):
    w = gt[~gt.cluster_name.isin(drop)]
    num = tot = 0.0
    for _, r in w.iterrows():
        if r.cluster_name in rates:
            num += r.value * rates[r.cluster_name]; tot += r.value
    p('  usage-weighted global automation, released rule, dropping %s: %.4f  (weight covered %.4f pp)'
      % (drop, num/tot, tot))

col = A.filter_df(df, facet='collaboration', geography='global', geo_id='GLOBAL', variable='collaboration_pct')
s = col.set_index('cluster_name').value
AUTOS = ['directive', 'feedback loop']; CL = AUTOS + ['learning', 'task iteration', 'validation']
p('published wave values from the same file: all-pattern %.4f  five-pattern %.4f'
  % (s[AUTOS].sum()/s.sum()*100, s[AUTOS].sum()/s[CL].sum()*100))
aa = A.filter_df(df, facet='collaboration_automation_augmentation', geography='global', geo_id='GLOBAL',
                 variable='automation_pct')
p('the file\'s own automation_pct variable at global: %.4f' % aa.value.iloc[0])
os.chdir(cwd); OUT.close()
