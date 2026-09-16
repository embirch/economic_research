"""Variance models / MDE, SOC major groups for H3, API exploratory cut, wage top-coding.
Writes /tmp/p1/c_out.txt."""
import pandas as pd, numpy as np

ROOT = '/workspace/economic_research/'
import os as _os; _os.makedirs('/tmp/p1', exist_ok=True)
OUT = open('/tmp/p1/c_out.txt', 'w')
def p(*a):
    print(*a); print(*a, file=OUT)

AUTO = {'directive', 'feedback loop'}
AUG = {'learning', 'task iteration', 'validation'}
CLASSIFIED = AUTO | AUG
RESID = {'none', 'not_classified'}
WAVES = {
 'aug2025': (ROOT+'data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv', 'csv',
             ROOT+'data/cache/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv', 'csv'),
 'nov2025': (ROOT+'data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet', 'pq',
             ROOT+'data/cache/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet', 'pq'),
 'feb2026': (ROOT+'data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet', 'pq',
             ROOT+'data/cache/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet', 'pq'),
}
def load(path, kind):
    if kind == 'csv':
        df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
    else:
        df = pd.read_parquet(path)
        for c in df.columns:
            if c != 'value':
                df[c] = df[c].astype(str)
    df['value'] = pd.to_numeric(df['value'])
    return df[df.geography == 'global']
def kish(x):
    x = np.asarray(x, float); x = x[x > 0]
    return x.sum()**2/(x**2).sum() if len(x) else np.nan

on = pd.read_csv(ROOT+'data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv',
                 keep_default_na=False, na_values=[], dtype=str)
on['key'] = on['Task'].str.lower().str.strip()
maj = on.groupby('key')['soc_major_group'].apply(lambda s: sorted(set(s)))
wg = pd.read_csv(ROOT+'data/cache/release_2025_02_10/wage_data.csv', keep_default_na=False, na_values=[])
p('C6 top-coding: MedianSalary max %.0f ; rows at the max %d ; distinct top values %s'
  % (wg.MedianSalary.max(), (wg.MedianSalary == wg.MedianSalary.max()).sum(),
     sorted(wg.MedianSalary.unique())[-4:]))

for w, (cpath, ckind, apath, akind) in WAVES.items():
    tk = pd.read_csv(f'/tmp/p1/tk_{w}.csv')
    tk['maj1'] = [maj[k][0] if len(maj[k]) == 1 else 'MULTI' for k in tk.key]
    ok = tk.autom.notna() & tk.c6_equal.notna()
    sub = tk[ok].sort_values('c6_equal').copy()
    cw = sub.w.cumsum()/sub.w.sum()
    sub['q'] = np.minimum(np.searchsorted([0.25, 0.5, 0.75], cw, side='left')+1, 4)
    p('='*70); p('[%s] analysis set %d tasks, %.3f pp' % (w, len(sub), sub.w.sum()))
    # wage top-coding inside the analysis set
    cap = sub.c6_equal.max()
    p('  tasks at the wage cap ($%.2f/hr = $%.0f/yr): %d ; %.3f pp (%.2f%% of analysis mass) ; Q4 mass share %.1f%%'
      % (cap, cap*2080, (sub.c6_equal >= cap-1e-9).sum(), sub.loc[sub.c6_equal >= cap-1e-9, 'w'].sum(),
         sub.loc[sub.c6_equal >= cap-1e-9, 'w'].sum()/sub.w.sum()*100,
         sub.loc[(sub.q == 4) & (sub.c6_equal >= cap-1e-9), 'w'].sum()/sub[sub.q == 4].w.sum()*100))
    # --- three variance models for the top-minus-bottom difference
    rng = np.random.default_rng(3)
    q1, q4 = sub[sub.q == 1], sub[sub.q == 4]
    def wmean(s): return np.average(s.autom, weights=s.w)
    # (a) conversation-level binomial on the classified counts
    def binse(s):
        n = s.b5.sum(); phat = np.average(s.autom, weights=s.b5)/100
        return np.sqrt(phat*(1-phat)/n)*100
    sea = np.sqrt(binse(q4)**2 + binse(q1)**2)
    # (b) design-based: resample tasks equal-prob with replacement, recompute usage-weighted mean
    db = []
    for _ in range(800):
        s4 = q4.iloc[rng.integers(0, len(q4), len(q4))]; s1 = q1.iloc[rng.integers(0, len(q1), len(q1))]
        db.append(wmean(s4) - wmean(s1))
    seb = float(np.std(db, ddof=1))
    # (c) the brief's literal spec: resample tasks with p proportional to w, unweighted mean
    dc = []
    p4 = (q4.w/q4.w.sum()).values; p1 = (q1.w/q1.w.sum()).values
    for _ in range(800):
        s4 = q4.iloc[rng.choice(len(q4), len(q4), True, p=p4)]; s1 = q1.iloc[rng.choice(len(q1), len(q1), True, p=p1)]
        dc.append(s4.autom.mean() - s1.autom.mean())
    sec = float(np.std(dc, ddof=1))
    p('  SE(top-minus-bottom): (a) conversation-binomial %.3f pp | (b) task bootstrap, usage-weighted mean %.3f pp'
      ' | (c) brief\'s spec (p prop. w, unweighted mean) %.3f pp' % (sea, seb, sec))
    p('  MDE(80%%, two-sided 5%%) = 2.8 x SE: (a) %.2f pp | (b) %.2f pp | (c) %.2f pp ; resolves the +-3 pp band: a=%s b=%s c=%s'
      % (2.8*sea, 2.8*seb, 2.8*sec, 2.8*sea < 3, 2.8*seb < 3, 2.8*sec < 3))
    p('  task-level sd of automation share: Q1 %.2f pp, Q4 %.2f pp ; Kish N Q1 %.1f Q4 %.1f -> sd/sqrt(Kish): Q1 %.2f Q4 %.2f'
      % (q1.autom.std(), q4.autom.std(), kish(q1.w.values), kish(q4.w.values),
         q1.autom.std()/np.sqrt(kish(q1.w.values)), q4.autom.std()/np.sqrt(kish(q4.w.values))))
    # --- H3: SOC major groups
    g = sub.groupby('maj1').agg(tasks=('task', 'size'), mass=('w', 'sum')).sort_values('mass', ascending=False)
    p('  SOC major groups represented: %d (of 22) ; MULTI-holder bucket: %s'
      % (g.index.nunique(), 'yes' if 'MULTI' in g.index else 'no'))
    p('  groups with >=20 tasks: %d ; >=1 pp of analysis mass: %d ; >=0.1 pp: %d'
      % ((g.tasks >= 20).sum(), (g.mass >= 1).sum(), (g.mass >= 0.1).sum()))
    top = g.head(4)
    p('  four largest groups by mass: %s' % [(i, int(r.tasks), round(r.mass, 2)) for i, r in top.iterrows()])
    soc15 = [i for i in g.index if i.startswith('15')]
    p('  SOC-15 rows: %s ; mass %.3f pp = %.2f%% of analysis mass'
      % (soc15, g.loc[soc15, 'mass'].sum(), g.loc[soc15, 'mass'].sum()/sub.w.sum()*100))
    # within-group: groups with tasks in both the bottom and top wage quartile
    both = sub.groupby('maj1').q.agg(lambda s: set(s))
    p('  groups containing both Q1 and Q4 tasks: %d ; groups spanning all four quartiles: %d'
      % (sum(1 for s in both if {1, 4} <= s), sum(1 for s in both if {1, 2, 3, 4} <= s)))
    # --- exploratory (a): 1P API intersection
    api = load(apath, akind)
    ai = api[api.facet == 'onet_task::collaboration'].copy()
    parts = ai.cluster_name.str.rsplit('::', n=1)
    ai['task'] = parts.str[0]
    abase = api[(api.facet == 'onet_task') & (api.variable == 'onet_task_pct')]
    p('  EXPLORATORY (a) 1P API: onet_task::collaboration rows %d ; base tasks %d (named %d) ; onet_task_pct nodes %d ; variables %s'
      % (len(ai), ai.task.nunique(), ai[~ai.task.isin(RESID)].task.nunique(),
         abase.cluster_name.nunique(), sorted(ai.variable.unique())))
    an = set(ai[~ai.task.isin(RESID)].task)
    common = an & set(sub.task)
    p('     API named intersection tasks also in the Claude.ai analysis set: %d' % len(common))
OUT.close()
