"""C5-C7 joins, wage coverage, multi-holder rules, Kish N, MDE. Writes /tmp/p1/b_out.txt."""
import pandas as pd, numpy as np, re, os, subprocess

ROOT = '/workspace/economic_research/'
import os as _os; _os.makedirs('/tmp/p1', exist_ok=True)
OUT = open('/tmp/p1/b_out.txt', 'w')
def p(*a):
    print(*a); print(*a, file=OUT)

AUTO = {'directive', 'feedback loop'}
AUG = {'learning', 'task iteration', 'validation'}
CLASSIFIED = AUTO | AUG
RESID = {'none', 'not_classified'}
WAVES = {
 'aug2025': (ROOT+'data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv', 'csv'),
 'nov2025': (ROOT+'data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet', 'pq'),
 'feb2026': (ROOT+'data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet', 'pq'),
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
    return x.sum()**2 / (x**2).sum() if len(x) else np.nan

# ---------- C5 ----------
p('='*70); p('C5  release_2025_09_15/data/intermediate/onet_task_statements.csv (O*NET DB 20.1)')
on = pd.read_csv(ROOT+'data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv',
                 keep_default_na=False, na_values=[], dtype=str)
p('  shape %s  columns %s' % (on.shape, list(on.columns)))
p('  distinct O*NET-SOC Code %d ; Task ID %d ; Task text %d ; lower-stripped keys %d'
  % (on['O*NET-SOC Code'].nunique(), on['Task ID'].nunique(), on['Task'].nunique(),
     on['Task'].str.lower().str.strip().nunique()))
on['key'] = on['Task'].str.lower().str.strip()
on['soc7'] = on['O*NET-SOC Code'].str[:7]
p('  distinct soc7 %d ; soc_major_group values %d ; rows per key max %d'
  % (on.soc7.nunique(), on.soc_major_group.nunique(), on.groupby('key').size().max()))
h10 = on.groupby('key')['O*NET-SOC Code'].apply(lambda s: sorted(set(s)))
h7 = on.groupby('key')['soc7'].apply(lambda s: sorted(set(s)))
maj = on.groupby('key')['soc_major_group'].apply(lambda s: sorted(set(s)))
p('  keys with >1 holder: 10-char O*NET-SOC %d ; 7-char SOC %d ; SOC major group %d (of %d keys)'
  % ((h10.str.len() > 1).sum(), (h7.str.len() > 1).sum(), (maj.str.len() > 1).sum(), len(h10)))

# ---------- C6 ----------
p('='*70); p('C6  release_2025_02_10/wage_data.csv')
wg = pd.read_csv(ROOT+'data/cache/release_2025_02_10/wage_data.csv', keep_default_na=False, na_values=[])
p('  shape %s  columns %s' % (wg.shape, list(wg.columns)))
p('  SOCcode is 10-char O*NET-SOC (%s), unique %s ; MedianSalary>100: %d of %d ; removed values %s'
  % (wg.SOCcode.str.len().unique().tolist(), wg.SOCcode.is_unique,
     (wg.MedianSalary > 100).sum(), len(wg), sorted(wg.loc[wg.MedianSalary <= 100, 'MedianSalary'])))
p('  JobZone==-1 %d ; ChanceAuto==-1 %d' % ((wg.JobZone == -1).sum(), (wg.ChanceAuto == -1).sum()))
wgf = wg[wg.MedianSalary > 100].copy()
wgf['hourly'] = wgf.MedianSalary / 2080.0
w10 = wgf.set_index('SOCcode').hourly
p('  KEY TEST: O*NET-SOC[:7] -> SOCcode matches %d of %d onet soc7 codes  <-- the brief\'s stated key'
  % (len(set(on.soc7) & set(w10.index)), on.soc7.nunique()))
p('  KEY TEST: full 10-char O*NET-SOC Code -> SOCcode matches %d of %d onet occupation codes'
  % (len(set(on['O*NET-SOC Code']) & set(w10.index)), on['O*NET-SOC Code'].nunique()))
p('  KEY TEST: both sides truncated to 7 chars matches %d of %d ; wage rows per 7-char code max %d'
  % (len(set(on.soc7) & set(wgf.SOCcode.str[:7])), on.soc7.nunique(), wgf.SOCcode.str[:7].value_counts().max()))
p('  hourly (MedianSalary/2080) min %.2f median %.2f max %.2f ; annual median %.0f'
  % (w10.min(), w10.median(), w10.max(), wgf.MedianSalary.median()))
jz = wg.set_index('SOCcode').JobZone
jz = jz[jz > 0]

# ---------- C7 ----------
p('='*70); p('C7  BLS Employment Projections')
ep_path = '/tmp/p1/bls_ep.html'
if not os.path.exists(ep_path):
    r = subprocess.run(['curl', '-sL', '-w', '%{http_code}', '-o', ep_path,
                        'https://data.bls.gov/projections/occupationProj'], capture_output=True, text=True)
    p('  curl HTTP', r.stdout.strip())
p('  bytes %d' % os.path.getsize(ep_path))
ep = max(pd.read_html(ep_path), key=len)
ep.columns = [c[0] if isinstance(c, tuple) else c for c in ep.columns]
ep = ep.loc[:, ~ep.columns.duplicated()]
ep['occ_code'] = ep['Occupation Code'].astype(str).str.strip()
ep['ep_wage'] = pd.to_numeric(ep['Median Annual Wage 2025'].astype(str).str.replace(r'[^0-9.]', '', regex=True), errors='coerce')
ep['ep_emp'] = pd.to_numeric(ep['Employment 2025'].astype(str).str.replace(r'[^0-9.]', '', regex=True), errors='coerce')
ep = ep[ep.occ_code.str.match(r'^\d\d-\d{4}$')]
p('  detailed-SOC rows %d ; unique codes %d ; median wage non-null %d ; employment non-null %d'
  % (len(ep), ep.occ_code.nunique(), ep.ep_wage.notna().sum(), ep.ep_emp.notna().sum()))
ep_wage = (ep.set_index('occ_code').ep_wage.dropna() / 2080.0)
ep_emp = ep.set_index('occ_code').ep_emp.dropna()
p('  ep hourly min %.2f median %.2f max %.2f ; employment units = thousands, total %.1f'
  % (ep_wage.min(), ep_wage.median(), ep_wage.max(), ep_emp.sum()))
p('  MERGE AUDIT onet soc7 -> EP occ_code: %d in, %d matched, %d unmatched (sample %s)'
  % (on.soc7.nunique(), len(set(on.soc7) & set(ep_wage.index)),
     on.soc7.nunique() - len(set(on.soc7) & set(ep_wage.index)),
     sorted(set(on.soc7) - set(ep_wage.index))[:5]))

summary = []
for w, (path, kind) in WAVES.items():
    g = load(path, kind)
    bp = g[(g.facet == 'onet_task') & (g.variable == 'onet_task_pct')]
    bc = g[(g.facet == 'onet_task') & (g.variable == 'onet_task_count')]
    wt = bp[~bp.cluster_name.isin(RESID)].set_index('cluster_name').value
    cn = bc[~bc.cluster_name.isin(RESID)].set_index('cluster_name').value
    named = wt.sum()
    p('='*70); p('[%s] named task nodes %d ; named mass %.4f of 100 ; conversations %s'
                 % (w, len(wt), named, f'{cn.sum():,.0f}'))
    keys = wt.index.str.lower().str.strip()
    matched = pd.Index(keys).isin(h10.index)
    p('  C5 MERGE AUDIT (node text -> 20.1 lower-stripped key): in %d, matched %d, unmatched %d, mass unmatched %.4f pp'
      % (len(keys), matched.sum(), (~matched).sum(), wt[~matched].sum()))
    p('     node texts collapsing onto one 20.1 key: %d' % (len(keys) - pd.Index(keys).nunique()))
    tk = pd.DataFrame({'task': wt.index, 'key': keys, 'w': wt.values, 'cnt': cn.reindex(wt.index).values})
    tk = tk[matched].copy()
    tk['h10'] = [h10[k] for k in tk.key]
    tk['h7'] = [h7[k] for k in tk.key]
    tk['maj'] = [maj[k] for k in tk.key]
    # wage under three multi-holder rules, C6 (10-char key)
    def rule(hs, series, how, emp=None, keyfun=lambda x: x):
        vals, ws = [], []
        for hh in hs:
            k = keyfun(hh)
            if k in series.index:
                vals.append(float(series[k])); ws.append(float(emp.get(hh[:7], np.nan)) if emp is not None else 1.0)
        if not vals: return np.nan
        vals = np.array(vals); ws = np.array(ws, float)
        if how == 'equal': return vals.mean()
        if how == 'modal': return vals[np.nanargmax(ws)] if np.isfinite(ws).any() else vals[0]
        if how == 'empw':
            m = np.isfinite(ws) & (ws > 0)
            return float(np.average(vals[m], weights=ws[m])) if m.any() else vals.mean()
    tk['c6_equal'] = [rule(h, w10, 'equal') for h in tk.h10]
    tk['c6_empw'] = [rule(h, w10, 'empw', ep_emp) for h in tk.h10]
    tk['c6_modal'] = [rule(h, w10, 'modal', ep_emp) for h in tk.h10]
    tk['c7_equal'] = [rule(h, ep_wage, 'equal', keyfun=lambda x: x[:7]) for h in tk.h7]
    tk['nprice'] = [len([x for x in h if x in w10.index]) for h in tk.h10]
    tk['njz'] = [len([x for x in h if x in jz.index]) for h in tk.h10]
    tk['jobzone'] = [rule(h, jz, 'equal') for h in tk.h10]
    pr = tk.c6_equal.notna()
    p('  C6 coverage (10-char join, MedianSalary>100): %d of %d tasks priced ; mass %.4f pp = %.2f%% of named'
      % (pr.sum(), len(tk), tk.loc[pr, 'w'].sum(), tk.loc[pr, 'w'].sum()/named*100))
    pr7 = tk.c7_equal.notna()
    p('  C7 coverage (EP, 7-char): %d tasks ; mass %.4f pp = %.2f%% of named'
      % (pr7.sum(), tk.loc[pr7, 'w'].sum(), tk.loc[pr7, 'w'].sum()/named*100))
    p('  JobZone coverage (exploratory c): %d tasks ; mass %.2f%% of named'
      % (tk.jobzone.notna().sum(), tk.loc[tk.jobzone.notna(), 'w'].sum()/named*100))
    p('  multi-holder: >1 10-char holder %d tasks (%.2f pp of wave, %.2f%% of named) ; >1 soc7 %d (%.2f pp) ; >1 major group %d (%.2f pp)'
      % ((tk.h10.str.len() > 1).sum(), tk.loc[tk.h10.str.len() > 1, 'w'].sum(),
         tk.loc[tk.h10.str.len() > 1, 'w'].sum()/named*100,
         (tk.h7.str.len() > 1).sum(), tk.loc[tk.h7.str.len() > 1, 'w'].sum(),
         (tk.maj.str.len() > 1).sum(), tk.loc[tk.maj.str.len() > 1, 'w'].sum()))
    mh = tk[(tk.nprice > 1)]
    p('  multi-priced-holder tasks %d (%.2f pp) ; rule spread on them: max |equal-empw| $%.2f/hr, mean %.3f ; corr %.5f'
      % (len(mh), mh.w.sum(), (mh.c6_equal - mh.c6_empw).abs().max(),
         (mh.c6_equal - mh.c6_empw).abs().mean(), tk[['c6_equal', 'c6_empw']].corr().iloc[0, 1]))
    p('  EMPLOYMENT-WEIGHT IDENTIFICATION: of those, holders sharing one soc7 (so EP gives equal weights): %d'
      % sum(1 for _, r in mh.iterrows() if len(set(x[:7] for x in r.h10 if x in w10.index)) == 1))
    p('  C6 vs C7 wage agreement over tasks priced by both: Spearman %.4f ; Pearson %.4f ; N %d'
      % (tk[['c6_equal', 'c7_equal']].corr(method='spearman').iloc[0, 1],
         tk[['c6_equal', 'c7_equal']].corr().iloc[0, 1], (pr & pr7).sum()))

    # intersection automation
    ix = g[g.facet == 'onet_task::collaboration'].copy()
    parts = ix.cluster_name.str.rsplit('::', n=1)
    ix['task'] = parts.str[0]; ix['pattern'] = parts.str[1]
    ixn = ix[(~ix.task.isin(RESID)) & (ix.variable.str.endswith('_count'))]
    tab = ixn.pivot_table(index='task', columns='pattern', values='value', aggfunc='sum').fillna(0.0)
    c5c = [c for c in tab.columns if c in CLASSIFIED]; cac = [c for c in tab.columns if c in AUTO]
    b5 = tab[c5c].sum(1); a5 = tab[cac].sum(1)
    if 'not_classified' in tab:
        p('  intersection `not_classified` PATTERN: %.4f%% of named-task intersection counts, on %d tasks'
          % (tab['not_classified'].sum()/tab.sum().sum()*100, (tab['not_classified'] > 0).sum()))
    if 'none' in tab:
        p('  intersection `none` PATTERN: %.4f%% of counts' % (tab['none'].sum()/tab.sum().sum()*100))
    tk = tk.join((a5/b5.replace(0, np.nan)*100).rename('autom'), on='task')
    tk['b5'] = b5.reindex(tk.task).values
    ok = tk.autom.notna() & pr
    p('  ANALYSIS SET (C5+C6 wage AND >=1 classified pattern cell): %d tasks ; %.4f pp of wave ; %.2f%% of named mass ; %s conversations'
      % (ok.sum(), tk.loc[ok, 'w'].sum(), tk.loc[ok, 'w'].sum()/named*100, f'{tk.loc[ok, "b5"].sum():,.0f}'))
    p('  KISH effective N on onet_task_pct: all named %.1f (nominal %d) ; analysis set %.1f (nominal %d)'
      % (kish(wt.values), len(wt), kish(tk.loc[ok, 'w'].values), ok.sum()))
    p('  unweighted-count check: tasks with b5 cell but no wage %d (%.3f pp) ; wage but no b5 cell %d (%.3f pp)'
      % ((tk.autom.notna() & ~pr).sum(), tk.loc[tk.autom.notna() & ~pr, 'w'].sum(),
         (pr & tk.autom.isna()).sum(), tk.loc[pr & tk.autom.isna(), 'w'].sum()))

    sub = tk[ok].sort_values('c6_equal').copy()
    cw = sub.w.cumsum()/sub.w.sum()
    sub['q'] = np.minimum(np.searchsorted([0.25, 0.5, 0.75], cw, side='left') + 1, 4)
    for q in (1, 2, 3, 4):
        s = sub[sub.q == q]
        p('     Q%d  tasks %4d  mass %6.3f pp  Kish %6.1f  classified conversations %9s  hourly $%.2f-$%.2f'
          % (q, len(s), s.w.sum(), kish(s.w.values), f'{s.b5.sum():,.0f}', s.c6_equal.min(), s.c6_equal.max()))
    rng = np.random.default_rng(11)
    q1, q4 = sub[sub.q == 1], sub[sub.q == 4]
    d = []
    for _ in range(600):
        i4 = rng.choice(len(q4), len(q4), True, p=(q4.w/q4.w.sum()).values)
        i1 = rng.choice(len(q1), len(q1), True, p=(q1.w/q1.w.sum()).values)
        s4, s1 = q4.iloc[i4], q1.iloc[i1]
        d.append(np.average(s4.autom, weights=s4.w) - np.average(s1.autom, weights=s1.w))
    se = float(np.std(d, ddof=1))
    p('  WEIGHTED TASK BOOTSTRAP (B=600): SE(top-minus-bottom) %.3f pp ; 95%% half-width %.2f pp ; MDE(80%%) %.2f pp'
      % (se, 1.96*se, 2.8*se))
    summary.append((w, ok.sum(), kish(tk.loc[ok, 'w'].values), se, 2.8*se))
    tk.to_csv(f'/tmp/p1/tk_{w}.csv', index=False)

p('='*70); p('SUMMARY  wave | analysis tasks | Kish N | SE | MDE(80%) | resolves +-3pp')
for r in summary:
    p('  %s  %d  %.1f  %.3f  %.2f  %s' % (r[0], r[1], r[2], r[3], r[4], r[4] < 3.0))
OUT.close()
