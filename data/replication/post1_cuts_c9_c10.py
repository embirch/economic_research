"""post1 C9 (onet_task::use_case, Nov 2025 / Feb 2026) and C10 (release_2025_03_27 task-level
collaboration) confirmed at column level against post1's analysis set.

Analysis set is rebuilt exactly as in data/replication/post1_joins_c5_c7.py: a named global
`onet_task` node whose lower-cased stripped text joins O*NET DB 20.1, that carries a
`wage_data.csv` MedianSalary>100 on the full 10-character O*NET-SOC code, and that has at least
one classified-pattern cell in `onet_task::collaboration`.

Writes data/replication/results/post1_cuts_c9_c10.txt.
"""
import numpy as np
import pandas as pd

ROOT = '/workspace/economic_research/'
OUT = open(ROOT + 'data/replication/results/post1_cuts_c9_c10.txt', 'w')


def p(*a):
    print(*a)
    print(*a, file=OUT)


AUTO = {'directive', 'feedback loop'}
AUG = {'learning', 'task iteration', 'validation'}
CLASSIFIED = AUTO | AUG
RESID = {'none', 'not_classified'}
WAVES = {
    'aug2025': (ROOT + 'data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv', 'csv'),
    'nov2025': (ROOT + 'data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet', 'pq'),
    'feb2026': (ROOT + 'data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet', 'pq'),
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
    return df


def split_cluster(s):
    parts = s.str.rsplit('::', n=1)
    return parts.str[0], parts.str[1]


# ---------------------------------------------------------------- analysis set
on = pd.read_csv(ROOT + 'data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv',
                 keep_default_na=False, na_values=[], dtype=str)
on['key'] = on['Task'].str.lower().str.strip()
holders = on.groupby('key')['O*NET-SOC Code'].apply(lambda s: sorted(set(s)))

wg = pd.read_csv(ROOT + 'data/cache/release_2025_02_10/wage_data.csv', keep_default_na=False, na_values=[])
wgf = wg[wg.MedianSalary > 100]
w10 = (wgf.set_index('SOCcode').MedianSalary / 2080.0)


def wage_of(key):
    if key not in holders.index:
        return np.nan
    v = [float(w10[h]) for h in holders[key] if h in w10.index]
    return float(np.mean(v)) if v else np.nan


aset, weights, named_mass = {}, {}, {}
p('=' * 78)
p('ANALYSIS SET (rebuilt; must equal feasibility.md \u00a74: 1,802 / 2,075 / 2,188 tasks)')
for w, (path, kind) in WAVES.items():
    g = load(path, kind)
    g = g[g.geography == 'global']
    bp = g[(g.facet == 'onet_task') & (g.variable == 'onet_task_pct')]
    wt = bp[~bp.cluster_name.isin(RESID)].set_index('cluster_name').value
    ix = g[g.facet == 'onet_task::collaboration'].copy()
    ix['task'], ix['pattern'] = split_cluster(ix.cluster_name)
    ixn = ix[(~ix.task.isin(RESID)) & (ix.variable.str.endswith('_count'))]
    tab = ixn.pivot_table(index='task', columns='pattern', values='value', aggfunc='sum').fillna(0.0)
    c5 = [c for c in tab.columns if c in CLASSIFIED]
    has_cell = set(tab.index[tab[c5].sum(1) > 0])
    wage = pd.Series({t: wage_of(t.lower().strip()) for t in wt.index})
    sel = [t for t in wt.index if t in has_cell and np.isfinite(wage[t])]
    aset[w] = set(sel)
    weights[w] = wt
    named_mass[w] = wt.sum()
    p('  %s: named nodes %d ; analysis-set tasks %d ; mass %.4f pp of wave = %.2f%% of named'
      % (w, len(wt), len(sel), wt[sel].sum(), wt[sel].sum() / wt.sum() * 100))

# ---------------------------------------------------------------- C9
p('=' * 78)
p('C9  onet_task::use_case at geography == global')
for w, (path, kind) in WAVES.items():
    g = load(path, kind)
    gg = g[g.geography == 'global']
    uc = gg[gg.facet == 'onet_task::use_case'].copy()
    nonglobal = (g.facet == 'onet_task::use_case').sum() - len(uc)
    p('-' * 78)
    p('  [%s] rows at global %d ; rows at other geographies %d' % (w, len(uc), nonglobal))
    if not len(uc):
        p('      -> facet absent in this wave; facets containing "use_case": %s'
          % sorted({f for f in g.facet.unique() if 'use_case' in f}))
        continue
    uc['task'], uc['cat'] = split_cluster(uc.cluster_name)
    p('      variables %s ; level values %s' % (sorted(uc.variable.unique()), sorted(uc.level.unique())))
    p('      categories present: %s' % sorted(uc.cat.unique()))
    p('      base tasks %d (named %d)' % (uc.task.nunique(), uc.loc[~uc.task.isin(RESID), 'task'].nunique()))
    cnt = uc[(uc.variable.str.endswith('_count')) & (~uc.task.isin(RESID))]
    tab = cnt.pivot_table(index='task', columns='cat', values='value', aggfunc='sum').fillna(0.0)
    for c in tab.columns:
        nz = tab[c] > 0
        p('      count column %-14s cells %5d  min %5.0f  max %9.0f'
          % (c, nz.sum(), tab.loc[nz, c].min(), tab[c].max()))
    pct = uc[(uc.variable.str.endswith('_pct')) & (~uc.task.isin(RESID))]
    ptab = pct.pivot_table(index='task', columns='cat', values='value', aggfunc='sum').fillna(0.0)
    rs = ptab.sum(1)
    p('      per-task _pct row sum: min %.4f median %.4f max %.4f' % (rs.min(), rs.median(), rs.max()))
    # counts partition the base onet_task_count?
    bc = gg[(gg.facet == 'onet_task') & (gg.variable == 'onet_task_count')]
    base = bc[~bc.cluster_name.isin(RESID)].set_index('cluster_name').value
    both = tab.index.intersection(base.index)
    diff = (tab.sum(1).reindex(both) - base.reindex(both)).abs()
    p('      counts vs base onet_task_count over %d shared nodes: max |diff| %.0f ; exact on %d'
      % (len(both), diff.max(), (diff == 0).sum()))
    # publication patterns
    pat = tab.gt(0).apply(lambda r: tuple(sorted(r.index[r])), axis=1)
    p('      publication patterns (top 6): %s' % pat.value_counts().head(6).to_dict())
    # coverage of the analysis set
    A = aset[w]
    wt = weights[w]
    inset = sorted(A & set(tab.index))
    p('      COVERAGE of analysis set: %d of %d tasks carry a use_case row (%.4f of %.4f pp)'
      % (len(inset), len(A), wt[inset].sum(), wt[sorted(A)].sum()))
    split_cols = [c for c in ('work', 'coursework') if c in tab.columns]
    ws = tab.reindex(inset)
    both_cell = ws[split_cols].gt(0).all(axis=1) if len(split_cols) == 2 else pd.Series(False, index=ws.index)
    p('      of those: published `work` cell %d ; published `coursework` cell %d ; both %d'
      % (int(ws.get('work', pd.Series(0, index=ws.index)).gt(0).sum()),
         int(ws.get('coursework', pd.Series(0, index=ws.index)).gt(0).sum()),
         int(both_cell.sum())))
    p('      named-task mass, work AND coursework cell both published: %.4f of %.4f pp of the wave'
      % (wt[list(tab.index[tab[split_cols].gt(0).all(axis=1)])].sum(), named_mass[w]))
    p('      named-task mass, work OR coursework cell published: %.4f of %.4f pp of the wave'
      % (wt[list(tab.index[tab[split_cols].gt(0).any(axis=1)])].sum(), named_mass[w]))
    subst = [c for c in tab.columns if c != 'not_classified']
    p('      named-task mass with ANY substantive use_case cell: %.4f of %.4f pp of the wave'
      % (wt[list(tab.index[tab[subst].gt(0).any(axis=1)])].sum(), named_mass[w]))
    # work share over published cells, and the work-dominant set of BRIEF s9(3)(e)
    wsh = (ws['work'] / ws.sum(1).replace(0, np.nan)) if 'work' in ws.columns else pd.Series(np.nan, index=ws.index)
    substc = [c for c in ws.columns if c != 'not_classified']
    only_nc = ws[substc].sum(1) == 0
    wsh_sub = ws['work'] / ws[substc].sum(1).replace(0, np.nan)
    p('      analysis-set tasks whose ONLY published use_case cell is `not_classified`: %d (%.4f pp of the wave)'
      % (int(only_nc.sum()), wt[list(ws.index[only_nc])].sum()))
    p('      work share of published cells over the analysis set: defined %d ; median %.4f ; mean %.4f'
      % (wsh.notna().sum(), wsh.median(), wsh.mean()))
    p('      WORK-DOMINANT, brief\'s rule (work / all published cells >= 0.50): %d tasks, %.4f pp of the wave = %.2f%% of the analysis-set mass'
      % (int((wsh >= 0.5).sum()), wt[list(wsh.index[wsh >= 0.5])].sum(),
         wt[list(wsh.index[wsh >= 0.5])].sum() / wt[sorted(A)].sum() * 100))
    p('      WORK-DOMINANT, substantive-cell denominator (the rival rule): %d tasks, %.4f pp ; tasks flipping between the two rules %d'
      % (int((wsh_sub >= 0.5).sum()), wt[list(wsh_sub.index[wsh_sub >= 0.5])].sum(),
         int(((wsh >= 0.5) != (wsh_sub.fillna(-1) >= 0.5)).sum())))
    ncp = ptab.reindex(sorted(A))['not_classified'] if 'not_classified' in ptab.columns else pd.Series(np.nan, index=sorted(A))
    p('      bound width = published `not_classified` _pct on the analysis set: median %.4f pp ; max %.4f pp'
      % (float(ncp.median()), float(ncp.max())))
    p('      named-task mass by published cell: %s'
      % {c: round(float(wt[list(tab.index[tab[c] > 0])].sum()), 4) for c in tab.columns})
    p('      global share of the intersection\'s counts by category: %s'
      % {c: round(float(100 * tab[c].sum() / tab.sum().sum()), 4) for c in tab.columns})
    # BRIEF s9(3)(d): the mix per usage-weighted wage quartile
    wage = pd.Series({t: wage_of(t.lower().strip()) for t in sorted(A)})
    sub = pd.DataFrame({'w': wt[sorted(A)].values, 'wage': wage.values}, index=sorted(A)).sort_values('wage')
    cw = sub.w.cumsum() / sub.w.sum()
    sub['q'] = np.minimum(np.searchsorted([0.25, 0.5, 0.75], cw, side='left') + 1, 4)
    for q in (1, 2, 3, 4):
        idx = list(sub.index[sub.q == q])
        t = tab.reindex(idx).fillna(0.0)
        tot = t.sum().sum()
        p('         Q%d  tasks %4d  mass %6.3f pp  use_case rows on %4d  counts %9s  mix %s'
          % (q, len(idx), sub.w[idx].sum(), int(t.sum(1).gt(0).sum()), f'{tot:,.0f}',
             {c: round(float(100 * t[c].sum() / tot), 2) for c in t.columns}))
    nc = ws['not_classified'] if 'not_classified' in ws.columns else pd.Series(0.0, index=ws.index)
    p('      folded `not_classified` on the analysis set: cells %d ; max count %.0f ; median share of node %.4f'
      % (int(nc.gt(0).sum()), nc.max(), float((nc / ws.sum(1)).median())))

# ---------------------------------------------------------------- C10
p('=' * 78)
p('C10  release_2025_03_27, task-level collaboration (Feb-Mar 2025 window)')
C = ROOT + 'data/cache/release_2025_03_27/'
R = lambda f: pd.read_csv(C + f, keep_default_na=False, na_values=[])
bt = R('automation_vs_augmentation_by_task.csv')
v2 = R('task_pct_v2.csv')
th = R('task_thinking_fractions.csv')
p('  files present: %s' % sorted(f for f in __import__('os').listdir(C) if f.endswith('.csv')))
p('  automation_vs_augmentation_by_task.csv shape %s' % (bt.shape,))
p('    COLUMNS: %s' % list(bt.columns))
p('    a column literally named "collaboration": %s ; columns containing "collab": %s'
  % ('collaboration' in bt.columns, [c for c in bt.columns if 'collab' in c.lower()]))
p('    any *_count / *_pct column: %s'
  % [c for c in bt.columns if c.endswith('_count') or c.endswith('_pct')])
num = bt.drop(columns=['task_name'])
p('    dtypes %s ; row sums: max |sum-1| %.2e ; filtered median %.4f ; rows at filtered==1.0 %d'
  % (sorted(set(map(str, num.dtypes))), float((num.sum(1) - 1).abs().max()),
     float(bt.filtered.median()), int((bt.filtered == 1.0).sum())))
p('  task_pct_v2.csv shape %s columns %s ; pct sum %.12f ; `none` pseudo-task pct %.6f'
  % (v2.shape, list(v2.columns), v2.pct.sum(), float(v2.loc[v2.task_name == 'none', 'pct'].iloc[0])))
p('  task_thinking_fractions.csv shape %s columns %s' % (th.shape, list(th.columns)))
m = v2.merge(bt, on='task_name', how='inner')
p('  MERGE AUDIT task_pct_v2 -> by_task: %d rows in, %d matched, unmatched %s'
  % (len(v2), len(m), sorted(set(v2.task_name) - set(bt.task_name))))
p('    matched tasks carry %.4f of 100 pct ; v2-only is the `none` pseudo-task'
  % m.pct.sum())
cls = ['directive', 'feedback_loop', 'learning', 'task_iteration', 'validation']
p('    pct weighted by the five classified ratios: %.4f of 100 (usage-weighted filtered %.6f)'
  % (float((m.pct * m[cls].sum(1)).sum()), float((m.pct * m.filtered).sum() / m.pct.sum())))
auto = (m.pct * (m.directive + m.feedback_loop)).sum()
base = (m.pct * m[cls].sum(1)).sum()
p('    usage-weighted automation share on the five-classified base: %.4f%%' % (100 * auto / base))
p('  three task files: task_pct_v2 %d rows ; by_task %d ; thinking %d ; by_task set == v2 minus `none`: %s'
  % (len(v2), len(bt), len(th), set(bt.task_name) == set(v2.task_name) - {'none'}))

p('-' * 78)
p('  INTERSECTION with post1\'s analysis set (task keys lower-cased stripped on both sides)')
btkeys = set(bt.task_name.str.lower().str.strip())
p('    by_task distinct lower-stripped keys %d (of %d rows)' % (len(btkeys), len(bt)))
for w in WAVES:
    A = sorted(aset[w])
    wt = weights[w]
    keys = {t: t.lower().strip() for t in A}
    hit = [t for t in A if keys[t] in btkeys]
    p('      %s: %d analysis-set tasks in, %d matched in the Mar-2025 file, %d unmatched ; matched mass %.4f of %.4f pp of the wave (%.2f%%)'
      % (w, len(A), len(hit), len(A) - len(hit), wt[hit].sum(), wt[A].sum(),
         wt[hit].sum() / wt[A].sum() * 100))
    sub = bt.set_index(bt.task_name.str.lower().str.strip()).reindex([keys[t] for t in hit])
    p('         of the matched: filtered == 1.0 on %d tasks (%.4f pp of the wave) ; filtered median %.4f'
      % (int((sub.filtered == 1.0).sum()),
         wt[[t for t in hit if float(bt.set_index(bt.task_name.str.lower().str.strip()).loc[keys[t], 'filtered']) == 1.0]].sum(),
         float(sub.filtered.median())))
    usable = [t for t, f in zip(hit, sub.filtered.values) if f < 1.0]
    p('         with a usable five-pattern split (filtered < 1): %d tasks, %.4f pp of the wave'
      % (len(usable), wt[usable].sum()))

p('-' * 78)
p('  `none` AT TASK LEVEL DOES NOT EXIST IN THIS RELEASE (the brief\'s \u00a79(1) requires the `none`')
p('  share beside every automation share). Arithmetic:')
g5 = R('automation_vs_augmentation_v2.csv')
gp = dict(zip(g5.interaction_type, g5.pct))
p('    global v2 file: rows %s ; total %.6f ; `none` %.6f ; five classified %.6f'
  % (sorted(gp), sum(gp.values()), gp['none'], sum(gp.values()) - gp['none']))
p('    per-task file: no `none` column (%s); filtered mass over the 100-pct task base %.4f pp'
  % ([c for c in bt.columns if c == 'none'] or 'confirmed absent', 100 - (100 - m.pct.sum()) - base))
p('    so `filtered` (%.4f pp of the task base) exceeds the global `none` share (%.4f pp) by about'
  % (m.pct.sum() - base, gp['none']))
p('    %.2f pp of conversations, and the two components cannot be separated from the files.'
  % (m.pct.sum() - base - gp['none']))
three = sorted(set.intersection(*[aset[w] for w in WAVES]))
tri = [t for t in three if t.lower().strip() in btkeys]
p('    three-wave analysis-set intersection %d tasks ; also in the Mar-2025 file %d'
  % (len(three), len(tri)))
OUT.close()
