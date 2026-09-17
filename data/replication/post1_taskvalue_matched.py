"""post1 · the published task-value series on MATCHED windows, and the level non-reproduction.

Target: `economic-index-2026-03-report` Fig. 1.4 (p. 8), the Claude.ai "average value of
tasks" series — "the average hourly wage of US workers who perform that task" (p. 8) — read
from the figure as $49.3 (Jan 2025), $48.5 (Mar 2025), $48.9 (Aug 2025), $48.3 (Nov 2025),
$47.9 (Feb 2026). Anthropic ships **no code** for reports 4-6, so the specification here is
re-implemented from the released 2025-09-15 library's conventions plus each wave's
`data_documentation.md`, and stated as such.

What reproduces and what does not, on the three matched windows (Aug 2025 / Nov 2025 /
Feb 2026):
  * the LEVEL does not: $35.34 / $35.08 / $34.36 on `wage_data.csv` (C6) and
    $37.64 / $37.69 / $37.55 on BLS-EP (C7) against $48.9 / $48.3 / $47.9;
  * the CHANGES are close: Nov->Feb published -$0.40 against a rebuilt -$0.72,
    Aug->Feb published -$1.00 against -$0.98.
Four causes of the level gap (posts/post1/BRIEF.md §8(iv)): a 2019 O*NET website scrape
against OEWS May 2024; an unstated deflator; no time-on-task weights; equal-split or
employment weights in place of Anthropic's employment-and-time weights. This script also
bounds the first two: on the 2,042 / 2,534 / 2,593 tasks priced by BOTH sources, BLS-EP
sits 24.1-25.2% above the 2019 scrape, which closes about three quarters of the level gap
and leaves ~$5/hr.

Specification of record, per wave, all at `geography == 'global'`:
  weights  = `onet_task_pct` over NAMED task nodes (`none`/`not_classified` dropped),
             renormalised over the tasks that carry a wage;
  task->SOC = `release_2025_09_15/.../onet_task_statements.csv` (O*NET DB 20.1) on the
             lower-cased stripped task text, de-duplicated on that key (C5);
  wage     = C6 `wage_data.csv` `MedianSalary` (annual, > 100 filter) / 2080 on the FULL
             10-character `O*NET-SOC Code` -> `SOCcode` key, equal-split mean over the
             occupations holding the task; C7 = BLS-EP `Median Annual Wage 2025` / 2080 on
             the 7-character SOC, equal-split.
Nothing here touches the collaboration facet: no automation share, no quartile, no D.

Run from the repository root:  python data/replication/post1_taskvalue_matched.py
Output: data/replication/results/post1_taskvalue_matched.txt
"""

import numpy as np
import pandas as pd

ROOT = '/workspace/economic_research/'
OUTPATH = ROOT + 'data/replication/results/post1_taskvalue_matched.txt'
OUT = open(OUTPATH, 'w')


def p(*a):
    print(*a)
    print(*a, file=OUT)


RESID = {'none', 'not_classified'}
WAVES = {
    'aug2025': (ROOT + 'data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv', 'csv'),
    'nov2025': (ROOT + 'data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet', 'pq'),
    'feb2026': (ROOT + 'data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet', 'pq'),
}
# Fig. 1.4, economic-index-2026-03-report p. 8, Claude.ai series, read off the figure
PUBLISHED = {'aug2025': 48.9, 'nov2025': 48.3, 'feb2026': 47.9}
EP_HTML = ROOT + 'data/cache/supplementary/bls_employment_projections/occupationProj.html'


def load_global(path, kind):
    if kind == 'csv':
        df = pd.read_csv(path, keep_default_na=False, na_values=[], dtype=str)
    else:
        df = pd.read_parquet(path)
        for c in df.columns:
            if c != 'value':
                df[c] = df[c].astype(str)
    df['value'] = pd.to_numeric(df['value'])
    return df[df.geography == 'global']


# ---------- C5: task -> O*NET-SOC, de-duplicated on the lower-cased stripped key ----------
on = pd.read_csv(ROOT + 'data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv',
                 keep_default_na=False, na_values=[], dtype=str)
on['key'] = on['Task'].str.lower().str.strip()
on['soc7'] = on['O*NET-SOC Code'].str[:7]
h10 = on.groupby('key')['O*NET-SOC Code'].apply(lambda s: sorted(set(s)))
h7 = on.groupby('key')['soc7'].apply(lambda s: sorted(set(s)))
p('C5  O*NET 20.1 statements: %d rows -> %d keys ; %d 10-char codes ; %d 7-char SOCs'
  % (len(on), len(h10), on['O*NET-SOC Code'].nunique(), on.soc7.nunique()))

# ---------- C6: wage_data.csv on the full 10-character key ----------
wg = pd.read_csv(ROOT + 'data/cache/release_2025_02_10/wage_data.csv', keep_default_na=False, na_values=[])
wgf = wg[wg.MedianSalary > 100]
w10 = (wgf.set_index('SOCcode').MedianSalary / 2080.0)
p('C6  wage_data.csv: %d rows, %d after MedianSalary>100 ; 10-char key matches %d of %d O*NET codes'
  % (len(wg), len(wgf), len(set(on['O*NET-SOC Code']) & set(w10.index)), on['O*NET-SOC Code'].nunique()))

# ---------- C7: BLS Employment Projections (data/fetch/supplementary_bls_ep.py) ----------
ep = max(pd.read_html(EP_HTML), key=len)
ep.columns = [c[0] if isinstance(c, tuple) else c for c in ep.columns]
ep = ep.loc[:, ~ep.columns.duplicated()]
ep['occ_code'] = ep['Occupation Code'].astype(str).str.strip()
ep['ep_wage'] = pd.to_numeric(ep['Median Annual Wage 2025'].astype(str).str.replace(r'[^0-9.]', '', regex=True), errors='coerce')
ep['ep_emp'] = pd.to_numeric(ep['Employment 2025'].astype(str).str.replace(r'[^0-9.]', '', regex=True), errors='coerce')
ep = ep[ep.occ_code.str.match(r'^\d\d-\d{4}$')]
ep_wage = ep.set_index('occ_code').ep_wage.dropna() / 2080.0
ep_emp = ep.set_index('occ_code').ep_emp.dropna()
p('C7  BLS-EP: %d detailed-SOC rows, %d with a median wage ; soc7 -> occ_code matches %d of %d'
  % (len(ep), len(ep_wage), len(set(on.soc7) & set(ep_wage.index)), on.soc7.nunique()))


def equal_split(holders, series):
    vals = [float(series[h]) for h in holders if h in series.index]
    return float(np.mean(vals)) if vals else np.nan


def holder_rule(holders, series, how):
    """`how` in {'empw', 'modal'}: BLS-EP employment (7-char) over the holder wages."""
    vals, wts = [], []
    for h in holders:
        if h in series.index:
            vals.append(float(series[h]))
            wts.append(float(ep_emp.get(h[:7], np.nan)))
    if not vals:
        return np.nan
    vals, wts = np.array(vals), np.array(wts, float)
    if how == 'modal':
        return float(vals[np.nanargmax(wts)]) if np.isfinite(wts).any() else float(vals[0])
    m = np.isfinite(wts) & (wts > 0)
    return float(np.average(vals[m], weights=wts[m])) if m.any() else float(vals.mean())


variants = {}

res = {}
for w, (path, kind) in WAVES.items():
    g = load_global(*(path, kind))
    bp = g[(g.facet == 'onet_task') & (g.variable == 'onet_task_pct')]
    wt = bp[~bp.cluster_name.isin(RESID)].set_index('cluster_name').value
    named = wt.sum()
    keys = pd.Index(wt.index.str.lower().str.strip())
    matched = keys.isin(h10.index)
    tk = pd.DataFrame({'task': wt.index, 'key': keys, 'w': wt.values})[matched].copy()
    tk['c6'] = [equal_split(h10[k], w10) for k in tk.key]
    tk['c7'] = [equal_split(h7[k], ep_wage) for k in tk.key]
    p('=' * 70)
    p('[%s] named task nodes %d (mass %.4f of 100) ; C5 MERGE AUDIT: %d in, %d matched, %d unmatched'
      % (w, len(wt), named, len(wt), int(matched.sum()), int((~matched).sum())))
    r = {}
    for src in ('c6', 'c7'):
        pr = tk[src].notna()
        mass = tk.loc[pr, 'w'].sum()
        mean = float(np.average(tk.loc[pr, src], weights=tk.loc[pr, 'w']))
        r[src] = mean
        r[src + '_mass'] = mass / named * 100
        r[src + '_tasks'] = int(pr.sum())
        p('  %s: %d tasks priced, mass %.4f pp = %.2f%% of named ; usage-weighted mean hourly wage $%.4f'
          % (src.upper(), int(pr.sum()), mass, mass / named * 100, mean))
    both = tk.c6.notna() & tk.c7.notna()
    r['common_n'] = int(both.sum())
    r['common_c6'] = float(np.average(tk.loc[both, 'c6'], weights=tk.loc[both, 'w']))
    r['common_c7'] = float(np.average(tk.loc[both, 'c7'], weights=tk.loc[both, 'w']))
    r['uplift'] = r['common_c7'] / r['common_c6']
    p('  common set (priced by both): N %d ; C6 $%.4f vs C7 $%.4f -> BLS-EP is %+.2f%% on the same tasks'
      % (r['common_n'], r['common_c6'], r['common_c7'], (r['uplift'] - 1) * 100))
    p('  vintage-adjusted C6 level (C6 full set x that uplift): $%.2f against published $%.1f -> residual $%.2f'
      % (r['c6'] * r['uplift'], PUBLISHED[w], PUBLISHED[w] - r['c6'] * r['uplift']))

    # specification search on the level: does any available aggregation approach $48?
    bc = g[(g.facet == 'onet_task') & (g.variable == 'onet_task_count')].set_index('cluster_name').value
    tk['cnt'] = bc.reindex(tk.task).values
    tk['empw'] = [holder_rule(h10[k], w10, 'empw') for k in tk.key]
    tk['modal'] = [holder_rule(h10[k], w10, 'modal') for k in tk.key]
    pr = tk.c6.notna()
    cap = tk.loc[pr, 'c6'].max()
    v = {
        'equal-split (primary)': float(np.average(tk.loc[pr, 'c6'], weights=tk.loc[pr, 'w'])),
        'employment-weighted holders': float(np.average(tk.loc[tk.empw.notna(), 'empw'], weights=tk.loc[tk.empw.notna(), 'w'])),
        'modal holder': float(np.average(tk.loc[tk.modal.notna(), 'modal'], weights=tk.loc[tk.modal.notna(), 'w'])),
        'weights = onet_task_count': float(np.average(tk.loc[pr, 'c6'], weights=tk.loc[pr, 'cnt'])),
        'unweighted task mean': float(tk.loc[pr, 'c6'].mean()),
        'top-coded tasks excluded': float(np.average(tk.loc[pr & (tk.c6 < cap), 'c6'], weights=tk.loc[pr & (tk.c6 < cap), 'w'])),
    }
    variants[w] = v
    p('  specification search on the C6 level: %s'
      % ' ; '.join('%s $%.2f' % (k, x) for k, x in v.items()))
    res[w] = r

# ---------- the matched-window comparison ----------
p('=' * 70)
p('MATCHED WINDOWS  (published: Fig. 1.4, economic-index-2026-03-report p. 8)')
p('  wave      published   C6 rebuilt   C7 rebuilt')
for w in WAVES:
    p('  %-8s  $%5.1f      $%6.2f      $%6.2f' % (w, PUBLISHED[w], res[w]['c6'], res[w]['c7']))
chg = {}
for label, a, b in (('nov->feb', 'nov2025', 'feb2026'), ('aug->feb', 'aug2025', 'feb2026')):
    chg[label] = dict(pub=PUBLISHED[b] - PUBLISHED[a],
                      c6=res[b]['c6'] - res[a]['c6'],
                      c7=res[b]['c7'] - res[a]['c7'])
    p('  %s change: published %+.2f ; C6 rebuilt %+.4f ; C7 rebuilt %+.4f'
      % (label, chg[label]['pub'], chg[label]['c6'], chg[label]['c7']))
p('  (the "-$1.40" of the first brief set a published Jan-2025->Feb-2026 change against a')
p('   Nov->Feb rebuild; on matched windows the pairs are -0.40 vs -0.72 and -1.00 vs -0.98)')

# ---------- check block: fails loudly ----------
p('=' * 70)
p('CHECKS')
EXPECT = {
    'aug2025': dict(c6=35.34, c7=37.64, c6_mass=99.35, c7_mass=55.66, c6_tasks=2607, c7_tasks=2042, common_n=2042),
    'nov2025': dict(c6=35.08, c7=37.69, c6_mass=98.98, c7_mass=58.52, c6_tasks=3154, c7_tasks=2534, common_n=2534),
    'feb2026': dict(c6=34.36, c7=37.55, c6_mass=99.30, c7_mass=62.22, c6_tasks=3244, c7_tasks=2593, common_n=2593),
}
fails = []
for w, e in EXPECT.items():
    for k, v in e.items():
        got = res[w][k]
        tol = 0.005 if isinstance(v, float) else 0
        ok = abs(got - v) <= tol
        p('  %-8s %-10s expected %-8s got %-10s %s' % (w, k, v, round(got, 4), 'OK' if ok else 'FAIL'))
        if not ok:
            fails.append((w, k, v, got))
for label, e in (('nov->feb', dict(pub=-0.40, c6=-0.72)), ('aug->feb', dict(pub=-1.00, c6=-0.98))):
    for k, v in e.items():
        got = chg[label][k]
        ok = abs(got - v) <= 0.005
        p('  %-8s %-10s expected %-8s got %-10s %s' % (label, k, v, round(got, 4), 'OK' if ok else 'FAIL'))
        if not ok:
            fails.append((label, k, v, got))
# the level must NOT reproduce: that is the recorded result, not an aspiration
for w in WAVES:
    gap = PUBLISHED[w] - res[w]['c6']
    p('  %-8s level gap to published: $%.2f (recorded non-reproduction, %s)'
      % (w, gap, 'OK' if gap > 10 else 'FAIL — the gap changed'))
    if not gap > 10:
        fails.append((w, 'level_gap', '>10', gap))
allv = [x for v in variants.values() for x in v.values()]
p('  specification search: %d variants over three waves, range $%.2f-$%.2f ; none within $10 of the'
  ' published level (%s)' % (len(allv), min(allv), max(allv), 'OK' if max(allv) < 38 else 'FAIL'))
if not max(allv) < 38:
    fails.append(('all waves', 'variant max', '<38', max(allv)))
OUT.close()
if fails:
    raise SystemExit('CHECK BLOCK FAILED:\n' + '\n'.join(
        '  %s %s: expected %s, got %s' % f for f in fails))
print('all checks passed -> %s' % OUTPATH)
