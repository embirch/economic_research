#!/usr/bin/env python3
"""E08 frozen descriptive CSWC analysis. Raw inputs stay in an external/ignored cache.

Usage: python analysis.py --cache PATH_TO_E08_CACHE
Only numpy and pandas are required. No pilot modules or network calls are used.
results.json is an INTERNAL full-precision aggregate verification layer, not a public download.
public-tables.csv and figure-specs.json are rounded release layers; no respondent data are saved.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ.setdefault(key, '1')
import argparse
import csv
import hashlib
import json
import platform
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SOURCE = 'https://www150.statcan.gc.ca/n1/pub/14-25-0001/142500012026001-eng.htm'
LABELS = ['Men+ nonusers', 'Men+ users', 'Women+ nonusers', 'Women+ users']
GROUPS = ['Men+', 'Men+', 'Women+', 'Women+']
COEFFICIENTS = np.array([1., -1., -1., 1.])
FREQUENCIES = ['Daily', 'Several times a week', 'Several times a month', 'Once a month or less', 'Never']
TIMEOFF = ['Very easy', 'Easy', 'Difficult', 'Very difficult']

def dump(name, obj):
    (HERE/name).write_text(json.dumps(obj, indent=2, allow_nan=False)+'\n')

def quality(n):
    return 'A' if n >= 150 else 'E' if n >= 75 else 'F'

def rounded(value):
    result = float(Decimal(str(value)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    return 0.0 if result == 0 else result

def summarize(values, n=None, events=None, percentile=False):
    values = np.asarray(values, float)
    assert values.shape == (1001,)
    point = float(values[0])
    ans = {'estimate': point, 'finite_replicates': int(np.isfinite(values[1:]).sum())}
    if np.isfinite(values).all():
        se = float(np.sqrt(np.mean((values[1:]-point)**2)))
        ans.update(se=se, interval_95=[point-1.96*se, point+1.96*se])
        if percentile:
            ans['percentile_95'] = np.quantile(values[1:], [.025, .975], method='linear').tolist()
            ans['percentile_method'] = 'numpy.quantile method=linear'
        ans['normal_interval_outside_unit_range'] = bool(point-1.96*se < 0 or point+1.96*se > 1)
        ans['degenerate_replicates'] = bool(np.ptp(values[1:]) == 0)
    else:
        ans.update(se=None, interval_95=None, failure='Undefined replicates retained; no variance computed')
    if n is not None:
        ans.update(n=int(n), domain_quality=quality(n))
    if events is not None:
        ans.update(events=int(events), event_quality=quality(events))
        ans['release_quality'] = quality(min(n, events))
        ans['boundary_event_count'] = bool(events in (0, n))
    return ans

def covariance(values):
    residual = values[1:]-values[0]
    return (residual.T @ residual/1000).tolist()

def ratio(W, y, mask):
    den = W[mask].sum(axis=0)
    assert (den > 0).all()
    return (W[mask].T @ np.asarray(y, float)[mask])/den

def group_values(W, y, group, eligible=None):
    if eligible is None:
        eligible = np.ones(len(group), dtype=bool)
    return np.column_stack([ratio(W, y, eligible & (group == g)) for g in range(4)])

def profile(W, y, group, percentile=False):
    v = group_values(W, y, group)
    rates = []
    for g in range(4):
        mask = group == g
        rates.append({'group': LABELS[g], **summarize(v[:, g], mask.sum(), np.asarray(y)[mask].sum(), percentile)})
    return {'rates': rates, 'rate_covariance': covariance(v),
            'men_user_minus_nonuser': summarize(v[:, 1]-v[:, 0]),
            'women_user_minus_nonuser': summarize(v[:, 3]-v[:, 2]),
            'interaction': summarize(v @ COEFFICIENTS)}, v

def common_composition(d, W, outcomes, group, strata, full_values):
    keys = d[strata].astype(str).agg('|'.join, axis=1)
    cross = pd.crosstab(keys, group).reindex(columns=range(4), fill_value=0)
    common = cross.index[(cross > 0).all(axis=1)]
    retained = keys.isin(common).to_numpy()
    pool = W[retained].sum(0)
    estimates = {name: np.zeros((1001, 4)) for name in outcomes}
    zeros = 0
    failed_reps = set()
    min_den = float('inf')
    min_rep_den = float('inf')
    qsum = np.zeros(1001)
    max_q_change = 0.
    for key in common:
        cell = (keys == key).to_numpy()
        q = W[cell].sum(0)/pool
        qsum += q
        max_q_change = max(max_q_change, float(np.max(np.abs(q[1:]-q[0]))))
        for g in range(4):
            mask = cell & (group == g)
            den = W[mask].sum(0)
            min_den = min(min_den, float(den[0]))
            min_rep_den = min(min_rep_den, float(den[1:].min()))
            zeros += int((den[1:] <= 0).sum())
            failed_reps.update((np.flatnonzero(den[1:] <= 0)+1).tolist())
            for name, y in outcomes.items():
                num = W[mask].T @ y[mask]
                mean = np.divide(num, den, out=np.full_like(num, np.nan), where=den > 0)
                estimates[name][:, g] += q*mean
    assert np.max(np.abs(qsum-1)) < 1e-12
    info = {'strata': strata, 'retained_n': int(retained.sum()), 'total_strata': int(len(cross)),
            'common_strata': int(len(common)), 'retained_weight_share': float(pool[0]/W[:, 0].sum()),
            'minimum_internal_group_cell_n': int(cross.loc[common].to_numpy().min()),
            'minimum_full_weight_cell_denominator': min_den,
            'minimum_replicate_cell_denominator': min_rep_den,
            'zero_replicate_cell_denominators': zeros, 'failed_replicate_numbers': sorted(failed_reps),
            'maximum_replicate_target_mix_change': max_q_change,
            'target_mix_max_sum_error': float(np.max(np.abs(qsum-1))),
            'support_fixed_across_replicates': True,
            'scope': 'Conditional on observed common support; sparse component estimates are not released',
            'groups': []}
    for g in range(4):
        mask = group == g
        gm = mask & retained
        info['groups'].append({'group': LABELS[g], 'retained_n': int(gm.sum()),
                               'retained_weight_share': float(W[gm, 0].sum()/W[mask, 0].sum())})
    out = {'support': info, 'outcomes': {}}
    for name, y in outcomes.items():
        raw = group_values(W, y, group, retained)
        std = estimates[name]
        raw_delta = raw @ COEFFICIENTS
        std_delta = std @ COEFFICIENTS
        full_delta = full_values[name] @ COEFFICIENTS
        restriction = raw_delta-full_delta
        composition = std_delta-raw_delta
        joint = np.column_stack([full_delta, raw_delta, std_delta, restriction, composition])
        outcome = {'standardized_rates': [dict(group=LABELS[g], **summarize(std[:, g],
                    int(((group == g) & retained).sum()), int(y[(group == g) & retained].sum()))) for g in range(4)],
                   'same_support_raw_rates': [dict(group=LABELS[g], **summarize(raw[:, g],
                    int(((group == g) & retained).sum()), int(y[(group == g) & retained].sum()))) for g in range(4)],
                   'same_support_raw_interaction': summarize(raw_delta),
                   'standardized_interaction': summarize(std_delta),
                   'restriction_change': summarize(restriction), 'composition_change': summarize(composition),
                   'joint_covariance_order': ['full_raw', 'same_support_raw', 'standardized', 'restriction_change', 'composition_change'],
                   'joint_covariance': covariance(joint) if np.isfinite(joint).all() else None,
                   'standardized_rate_covariance': covariance(std) if np.isfinite(std).all() else None,
                   'decomposition_max_error': float(np.nanmax(np.abs((std_delta-full_delta)-(restriction+composition))))}
        if zeros:
            outcome['release_status'] = 'Diagnostic only: invalid uncertainty, not a cleared estimate'
        out['outcomes'][name] = outcome
    return out

def additive(d, W, outcomes, group):
    female = group//2
    ai = group%2
    blocks = [np.ones((len(d), 1)), female[:, None], ai[:, None], (female*ai)[:, None]]
    names = ['intercept', 'Women+', 'use', 'Women+_x_use']
    for col in ['AGECAT', 'EDUC_G', 'NOC7', 'NAICS8', 'COWMAIN3']:
        dummy = pd.get_dummies(d[col].astype(str), drop_first=True)
        blocks.append(dummy.to_numpy(float))
        names += [col+'='+str(c) for c in dummy.columns]
    X = np.column_stack(blocks)
    rank = np.linalg.matrix_rank(X)
    assert X.shape[1] == rank == 25
    weights = W/W.sum(0)
    pairs = [(i, j) for i in range(25) for j in range(i, 25)]
    products = np.column_stack([X[:, i]*X[:, j] for i, j in pairs])
    normal = weights.T @ products
    gram = np.zeros((1001, 25, 25))
    for k, (i, j) in enumerate(pairs):
        gram[:, i, j] = gram[:, j, i] = normal[:, k]
    ranks = np.linalg.matrix_rank(gram)
    assert (ranks == 25).all()
    ev = np.linalg.eigvalsh(gram)
    info = {'columns': names, 'columns_n': 25, 'unweighted_design_rank': int(rank),
            'minimum_weighted_gram_rank': int(ranks.min()), 'replicates_refit': 1000,
            'maximum_gram_condition_number': float(np.max(ev[:, -1]/ev[:, 0])),
            'outcomes': {}}
    inv = np.linalg.inv(gram[0])
    leverage = weights[:, 0]*np.einsum('ij,jk,ik->i', X, inv, X)
    info['full_weight_leverage'] = {'maximum': float(leverage.max()), 'sum': float(leverage.sum()),
                                   'p99': float(np.quantile(leverage, .99))}
    for name, y in outcomes.items():
        rhs = weights.T @ (X*y[:, None])
        beta = np.linalg.solve(gram, rhs[:, :, None])[:, :, 0]
        assert np.isfinite(beta).all()
        pred = X @ beta[0]
        info['outcomes'][name] = {'interaction': summarize(beta[:, 3]),
            'coefficient_covariance': covariance(beta), 'coefficients': beta[0].tolist(),
            'max_normal_equation_residual': float(np.max(np.abs(np.einsum('bij,bj->bi', gram, beta)-rhs))),
            'full_fitted_range': [float(pred.min()), float(pred.max())],
            'full_fitted_outside_unit_range_n': int(((pred < 0) | (pred > 1)).sum())}
    return info

def public_rows(out):
    rows = []
    def add(result_id, label, x, unit='percent', note=''):
        flag = x.get('release_quality', 'A')
        if x.get('interval_95') is None:
            return
        suppressed = flag == 'F'
        rows.append({'result_id': result_id, 'label': label, 'unit': unit,
             'estimate': '' if suppressed else rounded(x['estimate']*100),
             'low': '' if suppressed else rounded(x['interval_95'][0]*100),
             'high': '' if suppressed else rounded(x['interval_95'][1]*100),
             'n': x.get('n', ''), 'events': '' if suppressed else x.get('events', ''),
             'quality': flag, 'note': 'Suppressed: unacceptable source quality' if suppressed else
             ('Use with caution; '+note if flag == 'E' else note)})
    add('benchmark', 'Whole file, including self-employment', out['benchmark'])
    for outcome, obj in out['raw'].items():
        for i, row in enumerate(obj['rates']):
            add(f'{outcome}.raw.rate.{i}', row['group'], row)
        for key in ['men_user_minus_nonuser', 'women_user_minus_nonuser', 'interaction']:
            add(f'{outcome}.raw.{key}', key, obj[key], 'percentage_points')
        for row in out['distributions'][outcome]:
            add(row['result_id'], row['group']+': '+row['category'], row)
        add(f'{outcome}.additive.interaction', 'Additive projection', out['additive']['outcomes'][outcome]['interaction'], 'percentage_points')
        for target in ['occupation_sector', 'occupation_sector_education']:
            o = out['common_composition'][target]['outcomes'][outcome]
            for key in ['same_support_raw_interaction', 'standardized_interaction', 'restriction_change', 'composition_change']:
                add(f'{outcome}.{target}.{key}', target+': '+key, o[key], 'percentage_points', 'Conditional on observed common support; sparse components')
            for kind in ['standardized_rates', 'same_support_raw_rates']:
                for i, x in enumerate(o[kind]):
                    add(f'{outcome}.{target}.{kind}.{i}', target+': '+kind+': '+x['group'], x, note='Pooled estimate; sparse component estimates omitted')
    # The released difficult/very-difficult binary would reveal an F-category
    # through its other component. Apply companion suppression within that pair.
    for g in range(4):
        paired = [r for r in rows if r['result_id'] in
                  [f'difficult.distribution.{g}.3', f'difficult.distribution.{g}.4']]
        if any(r['quality'] == 'F' for r in paired):
            for r in paired:
                if r['quality'] != 'F':
                    r.update(estimate='', low='', high='', events='',
                             note='Companion suppression prevents recovery of an F-quality category from the combined binary outcome')
    return rows

def figures(out, rows):
    index = {r['result_id']: r for r in rows}
    def row(result_id, label, group, n=None):
        r = index[result_id]
        assert r['quality'] != 'F'
        return {'label': label, 'group': group, 'value': r['estimate'], 'low': r['low'], 'high': r['high'],
                'n': r['n'] if n is None else n, 'result_id': result_id, 'quality': r['quality']}
    base = {'type': 'dot', 'source_label': 'Statistics Canada, CSWC 2024–2025 PUMF; author calculations', 'source_url': SOURCE}
    commonnote = 'Reference-job employees aged 15–69 in ten provinces. Users report any GenAI use over the relevant 12 months. Intervals are pointwise 95% public-bootstrap normal intervals. Reported gender uses the source Men+/Women+ categories. Counts are unweighted respondents.'
    fs = [{**base, 'id': 'frequent-work', 'title': 'GenAI users report frequent unpaid job work more often in both gender groups',
       'description': 'Daily or several-times-a-week unpaid work during free time to meet job demands.', 'x_label': 'Frequent unpaid job work (%)', 'unit': 'percent',
       'rows': [row(f'frequent.raw.rate.{i}', LABELS[i], GROUPS[i]) for i in range(4)], 'footnote': commonnote},
       {**base, 'id': 'composition', 'title': 'The gender difference in the user–nonuser gap changes with the comparison target',
        'description': 'Women+ user–nonuser difference minus Men+ user–nonuser difference in frequent unpaid job work.',
        'x_label': 'Women+ minus Men+ user–nonuser difference (pp)', 'unit': 'percentage_points',
        'rows': [row('frequent.raw.interaction', 'Raw: all 20,538 employees', 'neutral', 20538),
                 row('frequent.additive.interaction', 'Additive projection: all employees', 'neutral', 20538),
                 row('frequent.occupation_sector.standardized_interaction', 'Common occupation/sector mix: 100.0% weight', 'neutral', 20538),
                 row('frequent.occupation_sector_education.standardized_interaction', 'Common occupation/sector/education mix: 99.4% weight', 'neutral', 20413)],
        'footnote': 'Different descriptive targets, not competing estimates of one causal effect. Same-support raw interactions and restriction/composition changes appear in the text and public table. Common-mix estimates use sparse components; component estimates are not released. 95% intervals use all 1,000 shared replicates. Counts are unweighted respondents.'},
       {**base, 'id': 'frequency-profile', 'title': 'GenAI users are less likely to report never doing unpaid job work',
        'description': 'Complete five-category distribution of unpaid personal-time work, shown as point estimates and intervals.',
        'x_label': 'Share of each gender/use group (%)', 'unit': 'percent',
        'rows': [row(f'frequent.distribution.{g}.{c}', LABELS[g]+': '+FREQUENCIES[c-1], GROUPS[g]) for g in range(4) for c in range(1, 6)],
        'footnote': commonnote+' Five categories sum to 100% before rounding; frequency categories are not hours. Use with caution (E): both Men+ daily-frequency estimates have 75–149 contributing outcome records.'},
       {**base, 'id': 'time-off', 'title': 'GenAI users report less difficulty taking personal or family time off',
        'description': 'Difficult or very difficult to take one or two hours off during working hours.',
        'x_label': 'Difficulty taking time off (%)', 'unit': 'percent',
        'rows': [row(f'difficult.raw.rate.{i}', LABELS[i], GROUPS[i]) for i in range(4)],
        'footnote': commonnote+' This item has no explicit 12-month recall window. A separate dimension of working conditions, not unpaid-work hours.'}]
    return {'figures': fs, 'preferred_main_figures': ['frequent-work', 'composition', 'frequency-profile'], 'appendix_figures': ['time-off']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, required=True)
    args = parser.parse_args()
    pins = json.loads((HERE/'source-manifest.json').read_text())
    checks = []
    for source in pins['source_files']:
        p = args.cache/source['filename']
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        assert h == source['sha256'], 'Source hash mismatch: '+source['filename']
        checks.append({'filename': p.name, 'sha256': h, 'matches_pin': True})
    print('Source hashes verified; reading and validating the two SAS files.', flush=True)
    d = pd.read_sas(args.cache/'cswc2024_2025_pumf.sas7bdat', encoding='utf8')
    b = pd.read_sas(args.cache/'cswc2024_2025_pumf_bsw.sas7bdat', encoding='utf8')
    assert len(d) == len(b) == 23314 and d.PUMFID.is_unique and b.PUMFID.is_unique
    assert set(d.PUMFID) == set(b.PUMFID)
    b = b.set_index('PUMFID').loc[d.PUMFID]
    assert np.array_equal(b.index.to_numpy(), d.PUMFID.to_numpy())
    bsw = [f'BSW{i}' for i in range(1, 1001)]
    assert set(bsw) == {c for c in b if c.startswith('BSW')}
    W = np.column_stack([d.CSWCWT.to_numpy(float), b[bsw].to_numpy(float)])
    assert np.isfinite(W).all() and (W >= 0).all() and (W[:, 0] > 0).all()
    domains = {'COWMAIN3': ['1', '2', '3'], 'GENDER': [1., 2.], 'G_AI_05A': [1., 2.],
               'WTQ_45': [1., 2., 3., 4., 5.], 'WTQ_60': [1., 2., 3., 4.],
               'AGECAT': ['1', '2', '3', '4', '5'], 'EDUC_G': ['1', '2', '3'],
               'NOC7': [f'{i:02}' for i in range(8)], 'NAICS8': [f'{i:02}' for i in range(1, 9)]}
    schema = {}
    for col, levels in domains.items():
        assert d[col].notna().all(), col+' has missing values'
        observed = sorted(d[col].unique().tolist())
        assert set(observed) == set(levels), (col, observed, levels)
        schema[col] = {'levels': observed, 'missing_n': 0}
    ai = (d.G_AI_05A == 1).to_numpy(float)
    benchmark = summarize(ratio(W, ai, np.ones(len(d), bool)), len(d), ai.sum())
    keep = d.COWMAIN3.isin(['1', '2']).to_numpy()
    d = d[keep].copy().reset_index(drop=True)
    W = W[keep]
    assert len(d) == 20538
    group = ((d.GENDER.to_numpy(int)-1)*2+(d.G_AI_05A == 1).to_numpy(int))
    assert np.bincount(group).tolist() == [7993, 2224, 8080, 2241]
    outcomes = {'frequent': d.WTQ_45.isin([1, 2]).to_numpy(float), 'difficult': d.WTQ_60.isin([3, 4]).to_numpy(float)}
    out = {'study': 'E08', 'analysis_date': '2026-10-07', 'layer': 'Internal full-precision aggregate verification, not public downloadable data',
       'source_checks': checks, 'schema_checks': schema, 'sample_flow': {'whole_file_n': 23314, 'excluded_self_employed_n': 2776,
       'employee_n': 20538, 'analysis_missing_exclusions_n': 0, 'groups_n': dict(zip(LABELS, np.bincount(group).tolist()))},
       'weight_checks': {'one_to_one_join': True, 'identical_key_sets': True, 'alignment_verified': True,
                         'all_weights_finite_nonnegative': True, 'all_point_weights_positive': True},
       'inference': {'replicates': 1000, 'variance': 'mean((T_b-T_full)^2)', 'normal_multiplier': 1.96,
                     'percentile_sensitivity': 'Exactly eight raw proportions: four frequent and four difficult; quantile method=linear',
                     'public_generalized_bootstrap_not_confidential_master': True},
       'benchmark': benchmark, 'raw': {}, 'distributions': {}, 'common_composition': {}}
    full_values = {}
    for name, y in outcomes.items():
        out['raw'][name], full_values[name] = profile(W, y, group, percentile=True)
        field, labels = ('WTQ_45', FREQUENCIES) if name == 'frequent' else ('WTQ_60', TIMEOFF)
        distribution = []
        stack = []
        for c, label in enumerate(labels, 1):
            z = (d[field] == c).to_numpy(float)
            obj, vals = profile(W, z, group)
            stack.append(vals)
            for g, row in enumerate(obj['rates']):
                distribution.append({'result_id': f'{name}.distribution.{g}.{c}', 'category': label, **row})
        err = float(np.max(np.abs(np.sum(stack, axis=0)-1)))
        assert err < 1e-12
        out['distributions'][name] = distribution
        out['raw'][name]['distribution_sum_max_error'] = err
    print('Raw profiles complete; refitting additive projections under all 1,000 replicates.', flush=True)
    out['additive'] = additive(d, W, outcomes, group)
    for target, fields in [('occupation_sector', ['NOC7', 'COWMAIN3']),
          ('occupation_sector_education', ['NOC7', 'COWMAIN3', 'EDUC_G']),
          ('age_saturated_failed_diagnostic', ['NOC7', 'COWMAIN3', 'EDUC_G', 'AGECAT'])]:
        print('Computing common composition:', target, flush=True)
        out['common_composition'][target] = common_composition(d, W, outcomes, group, fields, full_values)
    # Independent prior checks are fixed constants, not calls into the pilot estimator.
    reference = {'benchmark': (0.22138572032190454, 0.003761537539024443),
                 'frequent': (0.0339788519185084, 0.015020347793475186),
                 'difficult': (-0.009429719851659593, 0.018486419537276966)}
    regression = []
    for name, (point, se) in reference.items():
        actual = benchmark if name == 'benchmark' else out['raw'][name]['interaction']
        assert abs(actual['estimate']-point) < 1e-12 and abs(actual['se']-se) < 1e-12
        regression.append({'target': name, 'point_abs_error': abs(actual['estimate']-point), 'se_abs_error': abs(actual['se']-se)})
    assert out['common_composition']['occupation_sector']['support']['retained_n'] == 20538
    assert out['common_composition']['occupation_sector_education']['support']['retained_n'] == 20413
    assert out['common_composition']['age_saturated_failed_diagnostic']['support']['zero_replicate_cell_denominators'] == 2
    out['prior_independent_regression_checks'] = regression
    rows = public_rows(out)
    out['public_release_checks'] = {'rows': len(rows), 'quality_counts': {q: sum(r['quality'] == q for r in rows) for q in 'AEF'},
       'companion_suppressions': [r['result_id'] for r in rows if 'Companion suppression' in r['note']],
       'fine_cell_estimates_released': False, 'bootstrap_weights_released': False, 'respondent_rows_released': False,
       'rounding': 'Percentages and differences: one decimal; weighted counts, if released: nearest hundred',
       'quality_application': 'National categorical thresholds applied to domain and outcome counts; lower grade used as a conservative study rule'}
    dump('results.json', out)
    with (HERE/'public-tables.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    support_rows = []
    for target, obj in out['common_composition'].items():
        s = obj['support']
        for r in [{'group': 'All groups', 'retained_n': s['retained_n'], 'retained_weight_share': s['retained_weight_share']}] + s['groups']:
            support_rows.append({'target': target, 'group': r['group'], 'retained_n': r['retained_n'],
                'retained_weight_percent': rounded(100*r['retained_weight_share']), 'common_strata': s['common_strata'],
                'zero_replicate_cell_denominators': s['zero_replicate_cell_denominators'],
                'status': 'Failed diagnostic; no standardized interval' if s['zero_replicate_cell_denominators'] else 'Pooled estimate with sparse components'})
    with (HERE/'support-summary.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(support_rows[0])); writer.writeheader(); writer.writerows(support_rows)
    percentile_rows = []
    for outcome, obj in out['raw'].items():
        for i, r in enumerate(obj['rates']):
            assert r['release_quality'] == 'A' and not r['boundary_event_count']
            percentile_rows.append({'result_id': f'{outcome}.raw.rate.{i}', 'outcome': outcome, 'group': r['group'],
                'estimate_percent': rounded(r['estimate']*100),
                'normal_low': rounded(r['interval_95'][0]*100), 'normal_high': rounded(r['interval_95'][1]*100),
                'percentile_low': rounded(r['percentile_95'][0]*100), 'percentile_high': rounded(r['percentile_95'][1]*100),
                'quality': r['release_quality'], 'method': 'numpy.quantile method=linear'})
    assert len(percentile_rows) == 8
    with (HERE/'percentile-sensitivity.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(percentile_rows[0])); writer.writeheader(); writer.writerows(percentile_rows)
    dump('figure-specs.json', figures(out, rows))
    dump('environment.json', {'python': platform.python_version(), 'numpy': np.__version__, 'pandas': pd.__version__,
        'platform': platform.platform(), 'dependencies': ['numpy', 'pandas'], 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'thread_settings': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')}})
    print('Completed E08: results.json, public-tables.csv, figure-specs.json, environment.json', flush=True)

if __name__ == '__main__':
    main()
