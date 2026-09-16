#!/usr/bin/env python3
"""post3 (LL-36) feasibility checks: every cut in posts/post3/BRIEF.md section 8, at column level.

Run from the repository root:  python data/checks/post3_feasibility.py
Writes /tmp/post3_feasibility.json and data/checks/results/post3_feasibility.csv; prints the audit.
Reads only data/cache/; never modifies a raw file.

Inputs
  global `onet_task` level-0 rows (`onet_task_pct`, `onet_task_count`), both surfaces, the three
  long waves; the shipped O*NET DB 20.1 statements (2010 O*NET-SOC); the O*NET Center 2010->2019
  crosswalk (data/fetch/supplementary_onet.py).
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np, pandas as pd

FRAMES = {
 ('aug2025','ai'):  'data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv',
 ('aug2025','api'): 'data/cache/release_2025_09_15/data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv',
 ('nov2025','ai'):  'data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet',
 ('nov2025','api'): 'data/cache/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet',
 ('feb2026','ai'):  'data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet',
 ('feb2026','api'): 'data/cache/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet',
}
STATEMENTS = 'data/cache/release_2025_09_15/data/intermediate/onet_task_statements.csv'
CROSSWALK  = 'data/cache/supplementary/onet_soc_2019_crosswalk/2010_to_2019_onet_soc_crosswalk.csv'
ENRICHED   = 'data/cache/release_2025_09_15/data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.parquet'
RESID = ['none','not_classified','']
OUT: dict = {}

def load(path: str) -> pd.DataFrame:
    if path.endswith('.parquet'):
        df = pd.read_parquet(path)
    else:
        df = pd.read_csv(path, keep_default_na=False, na_values=[])
    df['level'] = df['level'].astype(str)
    df['value'] = pd.to_numeric(df['value'])
    return df

def global_onet(path: str) -> pd.DataFrame:
    d = load(path)
    g = d[(d.geography=='global') & (d.facet=='onet_task') & (d.level=='0')]
    p = g[g.variable=='onet_task_pct'][['cluster_name','value']].rename(columns={'value':'pct'})
    c = g[g.variable=='onet_task_count'][['cluster_name','value']].rename(columns={'value':'cnt'})
    w = p.merge(c, on='cluster_name', how='outer', validate='1:1')
    w['key'] = w.cluster_name.str.lower().str.strip()
    w.attrs['platform'] = d.platform_and_product.iloc[0]
    w.attrs['window'] = (d.date_start.iloc[0], d.date_end.iloc[0])
    return w

# ---------------------------------------------------------------- holder maps
def holder_pairs() -> pd.DataFrame:
    st = pd.read_csv(STATEMENTS, keep_default_na=False)
    st['key'] = st['Task'].str.lower().str.strip()
    return st

def weights(vintage: str, unit: str) -> pd.DataFrame:
    """key x SOC major group -> weight summing to 1 per key.
    vintage: '2010' (shipped codes) or '2019' (crosswalked).
    unit: 'occ' (split over distinct O*NET-SOC codes), 'major' (over distinct major groups),
          'title' (over distinct occupation Titles), 'modal' (largest-employment holder: not
          available without BLS; approximated by the first code -- reported for shape only)."""
    st = holder_pairs()
    pairs = st[['key','O*NET-SOC Code','Title']].drop_duplicates().rename(columns={'O*NET-SOC Code':'c2010'})
    if vintage == '2019':
        walk = pd.read_csv(CROSSWALK)
        walk.columns = ['c2010','t2010','c2019','t2019']
        pairs = pairs.merge(walk[['c2010','c2019']], on='c2010', how='left').dropna(subset=['c2019'])
        pairs['code'] = pairs['c2019']
    else:
        pairs['code'] = pairs['c2010']
    pairs['maj'] = pairs['code'].str[:2]
    if unit == 'occ':
        h = pairs[['key','code','maj']].drop_duplicates()
        n = h.groupby('key')['code'].nunique().rename('n')
    elif unit == 'major':
        h = pairs[['key','maj']].drop_duplicates(); h['code'] = h['maj']
        n = h.groupby('key')['maj'].nunique().rename('n')
    elif unit == 'title':
        h = pairs[['key','Title','maj']].drop_duplicates().rename(columns={'Title':'code'})
        n = h.groupby('key')['code'].nunique().rename('n')
    elif unit == 'dup':   # Anthropic's released rule: full value to each major group
        h = pairs[['key','maj']].drop_duplicates(); h['code'] = h['maj']
        n = h.groupby('key')['maj'].nunique().rename('n'); n[:] = 1
    h = h.join(n, on='key'); h['w'] = 1.0/h['n']
    return h.groupby(['key','maj'])['w'].sum().reset_index()

def mix(w: pd.DataFrame, W: pd.DataFrame):
    named = w[~w.cluster_name.isin(RESID)].copy()
    m = named.merge(W, on='key', how='inner')
    m['alloc'] = m.pct * m.w
    by = m.groupby('maj')['alloc'].sum()
    audit = dict(nodes_in=int(len(named)), keys_in=int(named.key.nunique()),
                 keys_matched=int(m.key.nunique()),
                 unmatched=int(named.key.nunique()-m.key.nunique()),
                 named_mass=float(named.pct.sum()), matched_mass=float(by.sum()),
                 all_mass=float(w.pct.sum()),
                 unmatched_names=sorted(set(named.key)-set(m.key))[:8])
    return by, m, audit

# ---------------------------------------------------------------- 1. the cuts
print('='*78); print('1. CUTS: global onet_task L0, both surfaces, three waves'); print('='*78)
W2010, W2019 = weights('2010','occ'), weights('2019','occ')
frames, cuts = {}, {}
for (wave,surf), path in FRAMES.items():
    w = global_onet(path); frames[(wave,surf)] = w
    resid = w[w.cluster_name.isin(RESID)]
    cuts[f'{wave}_{surf}'] = dict(
        file=path, platform=w.attrs['platform'], window=list(w.attrs['window']),
        nodes=int(len(w)), named_nodes=int((~w.cluster_name.isin(RESID)).sum()),
        residual_labels=sorted(resid.cluster_name), residual_pct=float(resid.pct.sum()),
        pct_sum=float(w.pct.sum()), count_sum=float(w.cnt.sum()),
        count_min=float(w.cnt.min()), count_max=float(w.cnt.max()))
    print(f"  {wave:8}{surf:4} {w.attrs['platform']:28} {w.attrs['window'][0]}..{w.attrs['window'][1]} "
          f"nodes {len(w):5} named {int((~w.cluster_name.isin(RESID)).sum()):5} "
          f"pct sum {w.pct.sum():8.4f} residual {resid.pct.sum():7.4f} "
          f"counts {w.cnt.sum():10.0f} min {w.cnt.min():.0f}")
OUT['cuts'] = cuts

# ------------------------------------------------- 2. join audits and multi-holder exposure
print(); print('='*78); print('2. JOIN AUDIT  task text -> O*NET 20.1 statements'); print('='*78)
st = holder_pairs()
per_key = st.groupby('key').agg(n_soc=('O*NET-SOC Code','nunique'), n_title=('Title','nunique'),
                                n_maj=('O*NET-SOC Code', lambda s: s.str[:2].nunique())).reset_index()
join = {}
for (wave,surf), w in frames.items():
    named = w[~w.cluster_name.isin(RESID)].merge(per_key, on='key', how='left')
    multi = named[named.n_maj > 1]
    join[f'{wave}_{surf}'] = dict(
        rows_in=int(len(named)), matched=int(named.n_soc.notna().sum()),
        unmatched=int(named.n_soc.isna().sum()),
        unmatched_mass=float(named[named.n_soc.isna()].pct.sum()),
        multi_major_tasks=int(len(multi)), multi_major_mass_pct_of_named=float(100*multi.pct.sum()/named.pct.sum()),
        multi_soc_tasks=int((named.n_soc>1).sum()))
    j = join[f'{wave}_{surf}']
    print(f"  {wave:8}{surf:4} rows in {j['rows_in']:5} matched {j['matched']:5} unmatched {j['unmatched']:3} "
          f"| >1 major group: {j['multi_major_tasks']:3} tasks = {j['multi_major_mass_pct_of_named']:.2f}% of named mass "
          f"| >1 SOC code: {j['multi_soc_tasks']:4}")
OUT['join_audit'] = join

# ------------------------------------------------- 3. S, both vintages, both bases, three rules
print(); print('='*78); print('3. SOC-15 SHARE S  (allocation rules x vintages x bases)'); print('='*78)
S = {}
for vint in ('2010','2019'):
    for unit in ('occ','major','title','dup'):
        Wt = weights(vint, unit)
        for (wave,surf), w in frames.items():
            by, m, aud = mix(w, Wt)
            s15 = float(by.get('15', 0.0))
            S[(vint,unit,wave,surf)] = dict(
                mass=s15, classified=100*s15/by.sum(), named_base=100*s15/aud['named_mass'],
                allconv=100*s15/aud['all_mass'], matched_mass=aud['matched_mass'],
                named_mass=aud['named_mass'], unmatched=aud['unmatched'])
rows = []
for k, v in S.items():
    rows.append(dict(vintage=k[0], rule=k[1], wave=k[2], surface=k[3], **{q: v[q] for q in
                ('classified','allconv','named_base','matched_mass')}))
Sdf = pd.DataFrame(rows)
for vint in ('2010','2019'):
    for unit in ('occ','major','title','dup'):
        sub = Sdf[(Sdf.vintage==vint)&(Sdf.rule==unit)].set_index(['surface','wave'])
        line = []
        for surf in ('ai','api'):
            a,n,f = (sub.loc[(surf,w),'classified'] for w in ('aug2025','nov2025','feb2026'))
            line.append(f"{surf}: {a:7.4f} -> {n:7.4f} -> {f:7.4f}  Aug->Feb {100*(f/a-1):+7.3f}%")
        print(f"  {vint} split-over-{unit:6} | " + ' | '.join(line))
OUT['S'] = {f'{k[0]}|{k[1]}|{k[2]}|{k[3]}': v for k, v in S.items()}

# ------------------------------------------------- 4. published-facet and Figure A.1 checks
print(); print('='*78); print('4. REPLICATION'); print('='*78)
e = pd.read_parquet(ENRICHED)
e = e[(e.geography=='global') & (e.facet=='soc_occupation')].copy()
e['value'] = pd.to_numeric(e['value'])
pub = e[e.variable=='soc_pct'].set_index('cluster_name')['value']
pub_named = pub.drop(index=[i for i in ('none','not_classified') if i in pub.index])
pub_cm_all, pub_cm_cls = float(pub['Computer and Mathematical']), float(100*pub['Computer and Mathematical']/pub_named.sum())
print(f"  published soc_occupation facet (Aug 2025, Claude.ai, global): "
      f"all-conversation {pub_cm_all:.4f} | classified {pub_cm_cls:.4f}")
for unit in ('occ','major','title','dup'):
    r = S[('2010',unit,'aug2025','ai')]
    print(f"    rebuild 2010 split-over-{unit:6}: all-conv {r['allconv']:.4f} (gap {r['allconv']-pub_cm_all:+.4f} pp)"
          f" | classified {r['classified']:.4f} (gap {r['classified']-pub_cm_cls:+.4f} pp)")
# 22-group MAE against the published facet
SOC_NAME = {'11':'Management','13':'Business and Financial Operations','15':'Computer and Mathematical',
 '17':'Architecture and Engineering','19':'Life, Physical, and Social Science','21':'Community and Social Service',
 '23':'Legal','25':'Educational Instruction and Library','27':'Arts, Design, Entertainment, Sports, and Media',
 '29':'Healthcare Practitioners and Technical','31':'Healthcare Support','33':'Protective Service',
 '35':'Food Preparation and Serving Related','37':'Building and Grounds Cleaning and Maintenance',
 '39':'Personal Care and Service','41':'Sales and Related','43':'Office and Administrative Support',
 '45':'Farming, Fishing, and Forestry','47':'Construction and Extraction','49':'Installation, Maintenance, and Repair',
 '51':'Production','53':'Transportation and Material Moving'}
for unit in ('occ','major','title','dup'):
    by, _, aud = mix(frames[('aug2025','ai')], weights('2010', unit))
    rec = {SOC_NAME[g]: 100*v/by.sum() for g, v in by.items() if g in SOC_NAME}
    common = [k for k in rec if k in pub_named.index]
    mae = np.mean([abs(rec[k]-100*pub_named[k]/pub_named.sum()) for k in common])
    print(f"    22-group MAE against the published facet, split-over-{unit:6}: {mae:.4f} pp over {len(common)} groups")
FIGA1 = {('ai','aug2025'):42.3,('ai','nov2025'):38.8,('ai','feb2026'):34.5,
         ('api','aug2025'):53.7,('api','nov2025'):59.6,('api','feb2026'):61.6}
print("  Figure A.1 (2019 O*NET-SOC), axis readings vs the 2019 recode, classified base:")
for surf in ('ai','api'):
    for wave in ('aug2025','nov2025','feb2026'):
        v = S[('2019','occ',wave,surf)]['classified']
        print(f"    {surf:4}{wave:9} rebuild {v:7.4f}  reading {FIGA1[(surf,wave)]:5.1f}  diff {v-FIGA1[(surf,wave)]:+.2f} pp")
rep = {}
for surf in ('ai','api'):
    for vint in ('2010','2019'):
        a = S[(vint,'occ','aug2025',surf)]['classified']; f = S[(vint,'occ','feb2026',surf)]['classified']
        aa = S[(vint,'occ','aug2025',surf)]['allconv'];   fa = S[(vint,'occ','feb2026',surf)]['allconv']
        rep[f'{surf}_{vint}'] = dict(classified_rel=100*(f/a-1), allconv_rel=100*(fa/aa-1),
                                     aug=a, feb=f)
        print(f"  Aug->Feb relative change, {surf:4} {vint} vintage: classified {100*(f/a-1):+7.3f}% "
              f"| all-conv {100*(fa/aa-1):+7.3f}%   (published: API +14%, Claude.ai -18%)")
OUT['replication'] = dict(published_facet_aug_ai=dict(allconv=pub_cm_all, classified=pub_cm_cls),
                          figA1_readings={f'{k[0]}_{k[1]}': v for k, v in FIGA1.items()}, rel=rep)


# --- 4b. Anthropic's own released function ------------------------------------------------
print('  Anthropic released code: aei_analysis_functions_1p_api.map_to_occupational_categories')
print('    (rule: full value to each holder major group, `none`/`not_classified` -> "Not Classified",')
print("     then renormalise the whole table to 100 -- an all-conversation base with duplication)")
rel = {}
try:
    sys.path.insert(0, 'data/cache/release_2025_09_15/code')
    import aei_analysis_functions_1p_api as AEI
    ts = pd.read_csv(STATEMENTS, keep_default_na=False)
    socs = pd.read_csv('data/cache/release_2025_09_15/data/intermediate/soc_structure.csv', keep_default_na=False)
    walk = pd.read_csv(CROSSWALK); walk.columns = ['c2010','t2010','c2019','t2019']
    ts19 = ts.merge(walk[['c2010','c2019']], left_on='O*NET-SOC Code', right_on='c2010', how='left').dropna(subset=['c2019']).copy()
    ts19['O*NET-SOC Code'] = ts19['c2019']; ts19['soc_major_group'] = ts19['c2019'].str[:2].astype(int)
    for (wave,surf), path in FRAMES.items():
        d = load(path)
        g = d[(d.facet=='onet_task') & (d.geography=='global') & (d.variable=='onet_task_pct')].copy()
        for vint, stmts in (('2010', ts.copy()), ('2019', ts19.copy())):
            o = AEI.map_to_occupational_categories(g, stmts, socs)
            by = o.groupby('occupational_category')['value'].sum()
            s15 = float(by.get('Computer and Mathematical Occupations', by.get('Computer and Mathematical', float('nan'))))
            nc = float(by.get('Not Classified', float('nan')))
            rel[f'{vint}|{wave}|{surf}'] = dict(allconv=s15, not_classified=nc, classified=100*s15/(100-nc))
    for vint in ('2010','2019'):
        for surf in ('ai','api'):
            a,n,f = (rel[f'{vint}|{w}|{surf}'] for w in ('aug2025','nov2025','feb2026'))
            print(f"    {vint} {surf:4} all-conv {a['allconv']:7.4f} -> {n['allconv']:7.4f} -> {f['allconv']:7.4f} "
                  f"({100*(f['allconv']/a['allconv']-1):+7.3f}%) | classified {a['classified']:7.4f} -> "
                  f"{n['classified']:7.4f} -> {f['classified']:7.4f} ({100*(f['classified']/a['classified']-1):+7.3f}%)")
except Exception as exc:                                        # plotly is an import-time dependency
    print('    released code not runnable here:', exc)
OUT['released_code'] = rel

# ------------------------------------------------- 5. C, HHI, node counts, TVD, effective N
print(); print('='*78); print('5. WITHIN-CATEGORY CONCENTRATION C'); print('='*78)
def soc15_tasks(w, vint, unit='occ'):
    Wt = weights(vint, unit)
    named = w[~w.cluster_name.isin(RESID)].copy()
    m = named.merge(Wt[Wt.maj=='15'], on='key', how='inner')
    m['mass'] = m.pct * m.w
    m['cmass'] = m.cnt * m.w
    return m.sort_values('mass', ascending=False)

Cres = {}
for vint in ('2010','2019'):
    for (wave,surf), w in frames.items():
        t = soc15_tasks(w, vint)
        S15 = t.mass.sum(); top10 = t.mass.head(10).sum()
        C = 100*top10/S15
        hhi = float(((t.mass/S15*100)**2).sum())
        n15 = float(t.cmass.sum())
        se_C = 100*float(np.sqrt((C/100)*(1-C/100)/n15))
        Cres[(vint,wave,surf)] = dict(C=C, S15_mass=float(S15), nodes=int(len(t)), hhi=hhi,
                                      eff_n=n15, se_C=se_C, top10_names=list(t.cluster_name.head(10)))
        if vint=='2019' or True:
            pass
for vint in ('2010','2019'):
    for surf in ('ai','api'):
        a,n,f = (Cres[(vint,w,surf)] for w in ('aug2025','nov2025','feb2026'))
        print(f"  {vint} {surf:4} C {a['C']:7.4f} -> {n['C']:7.4f} -> {f['C']:7.4f} | dC(Aug->Feb) {f['C']-a['C']:+6.3f} pp "
              f"dC(Aug->Nov) {n['C']-a['C']:+6.3f} pp | nodes {a['nodes']}/{n['nodes']}/{f['nodes']} "
              f"| eff N {a['eff_n']:.0f}/{n['eff_n']:.0f}/{f['eff_n']:.0f} | SE(C) {a['se_C']:.4f}/{n['se_C']:.4f}/{f['se_C']:.4f}")
OUT['C'] = {f'{k[0]}|{k[1]}|{k[2]}': {kk: vv for kk, vv in v.items() if kk != 'top10_names'} for k, v in Cres.items()}
OUT['C_top10_names'] = {f'{k[0]}|{k[1]}|{k[2]}': v['top10_names'] for k, v in Cres.items()}

# fixed-August-basket variant and TVD on the name-matched SOC-15 set
print('  fixed-August-basket C (the August top ten, carried forward) and SOC-15 TVD:')
tvd = {}
for vint in ('2010','2019'):
    for surf in ('ai','api'):
        base = soc15_tasks(frames[('aug2025',surf)], vint)
        basket = list(base.cluster_name.head(10))
        for wave in ('aug2025','nov2025','feb2026'):
            t = soc15_tasks(frames[(wave,surf)], vint)
            fixedC = 100*t[t.cluster_name.isin(basket)].mass.sum()/t.mass.sum()
            Cres[(vint,wave,surf)]['C_fixed_aug'] = fixedC
        a = soc15_tasks(frames[('aug2025',surf)], vint).set_index('cluster_name').mass
        f = soc15_tasks(frames[('feb2026',surf)], vint).set_index('cluster_name').mass
        n = soc15_tasks(frames[('nov2025',surf)], vint).set_index('cluster_name').mass
        for lab, x, y in (('aug->feb', a, f), ('aug->nov', a, n), ('nov->feb', n, f)):
            common = x.index.intersection(y.index)
            xs, ys = x[common]/x[common].sum(), y[common]/y[common].sum()
            tvd[f'{vint}|{surf}|{lab}'] = dict(tvd_pp=float(50*np.abs(xs-ys).sum()),
                common_nodes=int(len(common)), x_nodes=int(len(x)), y_nodes=int(len(y)),
                x_mass_kept=float(100*x[common].sum()/x.sum()), y_mass_kept=float(100*y[common].sum()/y.sum()))
        print(f"    {vint} {surf:4} fixed-basket C "
              f"{Cres[(vint,'aug2025',surf)]['C_fixed_aug']:.3f} -> {Cres[(vint,'nov2025',surf)]['C_fixed_aug']:.3f} -> "
              f"{Cres[(vint,'feb2026',surf)]['C_fixed_aug']:.3f} | TVD Aug->Feb {tvd[f'{vint}|{surf}|aug->feb']['tvd_pp']:.2f} pp "
              f"on {tvd[f'{vint}|{surf}|aug->feb']['common_nodes']} common nodes")
OUT['tvd'] = tvd
OUT['C_fixed'] = {f'{k[0]}|{k[1]}|{k[2]}': v.get('C_fixed_aug') for k, v in Cres.items()}

# allocation-rule robustness on S and C
print('  allocation-rule robustness (split over SOC codes / major groups / Titles):')
alloc = {}
for vint in ('2010','2019'):
    for surf in ('ai','api'):
        for wave in ('aug2025','nov2025','feb2026'):
            vals = {}
            for unit in ('occ','major','title','dup'):
                t = soc15_tasks(frames[(wave,surf)], vint, unit)
                s = S[(vint,unit,wave,surf)]['classified']
                vals[unit] = (s, 100*t.mass.head(10).sum()/t.mass.sum())
            sspread = max(v[0] for v in vals.values()) - min(v[0] for v in vals.values())
            cspread = max(v[1] for v in vals.values()) - min(v[1] for v in vals.values())
            alloc[f'{vint}|{wave}|{surf}'] = dict(S_spread_pp=sspread, C_spread_pp=cspread,
                                                  S=dict((u, v[0]) for u, v in vals.items()),
                                                  C=dict((u, v[1]) for u, v in vals.items()))
            print(f"    {vint} {wave:8}{surf:4} S spread {sspread:.4f} pp   C spread {cspread:.4f} pp")
OUT['allocation'] = alloc

# ------------------------------------------------- 6. taxonomy checks
print(); print('='*78); print('6. TAXONOMY / NODE-SET CHECKS'); print('='*78)
for surf in ('ai','api'):
    a = set(frames[('aug2025',surf)].cluster_name) - set(RESID)
    n = set(frames[('nov2025',surf)].cluster_name) - set(RESID)
    f = set(frames[('feb2026',surf)].cluster_name) - set(RESID)
    for lab, x, y, wx, wy in (('aug~nov', a, n, 'aug2025','nov2025'), ('nov~feb', n, f, 'nov2025','feb2026'),
                              ('aug~feb', a, f, 'aug2025','feb2026')):
        inter = x & y
        mx = frames[(wx,surf)]; my = frames[(wy,surf)]
        print(f"  {surf:4}{lab}: {len(inter):5} of {len(x)}/{len(y)} names match, carrying "
              f"{100*mx[mx.cluster_name.isin(inter)].pct.sum()/mx[~mx.cluster_name.isin(RESID)].pct.sum():.2f}% / "
              f"{100*my[my.cluster_name.isin(inter)].pct.sum()/my[~my.cluster_name.isin(RESID)].pct.sum():.2f}% of named mass")
        OUT.setdefault('name_match', {})[f'{surf}|{lab}'] = dict(
            common=len(inter), x_nodes=len(x), y_nodes=len(y),
            x_mass=float(100*mx[mx.cluster_name.isin(inter)].pct.sum()/mx[~mx.cluster_name.isin(RESID)].pct.sum()),
            y_mass=float(100*my[my.cluster_name.isin(inter)].pct.sum()/my[~my.cluster_name.isin(RESID)].pct.sum()))

# ------------------------------------------------- 7. Seychelles / country-grain recovery (Nov)
print(); print('='*78); print('7. NOVEMBER COUNTRY-GRAIN RECOVERY (the Seychelles bound)'); print('='*78)
nov = load(FRAMES[('nov2025','ai')])
cg = nov[(nov.geography=='country') & (nov.facet=='onet_task') & (nov.level=='0')]
cc = cg[cg.variable=='onet_task_count'][['geo_id','cluster_name','value']].rename(columns={'value':'cnt'})
cc['key'] = cc.cluster_name.str.lower().str.strip()
glob_named_cnt = frames[('nov2025','ai')]
glob_named_cnt = glob_named_cnt[~glob_named_cnt.cluster_name.isin(RESID)]
W = weights('2010','occ'); W15 = W[W.maj=='15']
cc15 = cc[~cc.cluster_name.isin(RESID)].merge(W15, on='key', how='inner')
cc15['mass'] = cc15.cnt * cc15.w
g15 = glob_named_cnt.merge(W15, on='key', how='inner'); g15['mass'] = g15.cnt * g15.w
tot15 = g15.mass.sum()
rec = 100*cc15.mass.sum()/tot15
syc = cc15[cc15.geo_id=='SC']
usage = nov[(nov.geography=='country') & (nov.facet=='country') & (nov.variable.isin(['usage_count','usage_pct']))]
syc_usage = usage[usage.geo_id=='SC'].set_index('variable')['value'].to_dict()
print(f"  global SOC-15 conversation mass (Nov, Claude.ai): {tot15:,.0f}")
print(f"  recoverable from country rows: {cc15.mass.sum():,.0f} = {rec:.2f}% of it, over "
      f"{cc15.geo_id.nunique()} countries and {cc15.cluster_name.nunique()} task names")
print(f"  Seychelles: country totals {syc_usage} ; published SOC-15 task rows {len(syc)}, "
      f"mass {syc.mass.sum():,.1f} = {100*syc.mass.sum()/tot15:.4f}% of the global SOC-15 mass")
allc = cc[~cc.cluster_name.isin(RESID)]
print(f"  all-task country coverage: {allc.cnt.sum():,.0f} of {glob_named_cnt.cnt.sum():,.0f} named conversations "
      f"= {100*allc.cnt.sum()/glob_named_cnt.cnt.sum():.2f}%; Seychelles all-task rows {len(allc[allc.geo_id=='SC'])}, "
      f"{allc[allc.geo_id=='SC'].cnt.sum():,.0f} conversations")
OUT['seychelles'] = dict(global_soc15_conv=float(tot15), recoverable_pct=float(rec),
    countries=int(cc15.geo_id.nunique()), syc_soc15_rows=int(len(syc)), syc_soc15_mass=float(syc.mass.sum()),
    syc_soc15_pct_of_global_soc15=float(100*syc.mass.sum()/tot15), syc_country_totals=syc_usage,
    country_all_task_coverage_pct=float(100*allc.cnt.sum()/glob_named_cnt.cnt.sum()),
    syc_all_task_rows=int(len(allc[allc.geo_id=='SC'])), syc_all_task_conv=float(allc[allc.geo_id=='SC'].cnt.sum()))


# ------------------------------------------------- 8. check block (empirical-standards 3)
print(); print('='*78); print('8. CHECKS'); print('='*78)
assert all(abs(c['pct_sum']-100) < 1e-6 for c in cuts.values()), 'onet_task_pct must sum to 100 at global'
assert all(c['count_min'] == 15 for c in cuts.values()), 'privacy floor is 15 conversations per task cell'
assert all(j['unmatched'] == 0 for j in join.values()), 'every named task must join to O*NET 20.1'
_d = S[('2010','dup','aug2025','ai')]          # released rule: duplicated table renormalised to 100
_released_style = 100*_d['mass']/(_d['matched_mass'] + 100 - _d['named_mass'])
assert abs(_released_style - pub_cm_all) < 0.001, \
    f'released rule must reproduce the published soc_occupation facet ({_released_style:.4f} vs {pub_cm_all:.4f})'
if rel:
    assert abs(rel['2010|aug2025|ai']['allconv'] - pub_cm_all) < 0.0005, 'released code vs published facet'
    assert abs(rel['2019|feb2026|api']['classified']/rel['2019|aug2025|api']['classified']*100-100 - 14.38) < 0.05, \
        'the +14% API leg must reproduce on the 2019 recode'
assert 0 < OUT['seychelles']['syc_soc15_pct_of_global_soc15'] < 100
print('  all checks passed')

Path('data/checks/results').mkdir(parents=True, exist_ok=True)
Sdf.to_csv('data/checks/results/post3_S_series.csv', index=False)
pd.DataFrame([dict(vintage=k[0], wave=k[1], surface=k[2], **{q: v[q] for q in ('C','S15_mass','nodes','hhi','eff_n','se_C')},
                   C_fixed_aug=v.get('C_fixed_aug')) for k, v in Cres.items()]).to_csv(
    'data/checks/results/post3_C_series.csv', index=False)
json.dump(OUT, open('/tmp/post3_feasibility.json','w'), indent=1, default=float)
print('\nwritten: data/checks/results/post3_S_series.csv, post3_C_series.csv, /tmp/post3_feasibility.json')
