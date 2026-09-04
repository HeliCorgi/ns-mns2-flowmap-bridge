"""Postprocessing of the Betchov cross-check (results_xcheck/*.json) against the preregistered
results (results/*.json): determinism check, growth-event medians of beta_B(theta), the four
questions (E0 profile; datum dependence; beta vs C4; E2 vs E2b grid stability), and the
correlation structure of (C1, beta_B, C4) within events.
"""
import json, os, sys
import numpy as np
import postprocess as pp

HERE = os.path.dirname(os.path.abspath(__file__))
LABELS = ['top0.5', 'top1', 'top2', 'top5', 'top10', 'top20', 'intense', 'omega25']


def load(name):
    x = json.load(open(os.path.join(HERE, 'results_xcheck', f'{name}.json')))
    pre = json.load(open(os.path.join(HERE, 'results', f'{name}.json')))
    ev = pp.growth_events(np.array(pre['t_cheap']), np.array(pre['enstrophy']))
    rows = []
    for k, t in enumerate(x['t']):
        f = x['full'][k]; b = x['beta'][k]
        r = pp.ratios(f); r['t'] = t
        r['inev'] = any(a <= t <= bb for a, bb, _, _ in ev)
        r['Lam'] = f['max']['Lam']; r['E'] = f['E']
        for lab in LABELS:
            r['beta_' + lab] = b['sets'][lab]['beta']; r['Qshare_' + lab] = b['sets'][lab]['Qshare']; r['vol_' + lab] = b['sets'][lab]['vol']
        r['beta_global'] = b['beta_global']; r['divJ_resid'] = b['divJ_resid_rel']; r['alg'] = b['alg_identity_rel']; r['tail'] = x['tail'][k]
        # determinism vs preregistered run at the same time
        kk = int(np.argmin(np.abs(np.array(pre['t_full']) - t)))
        if abs(pre['t_full'][kk] - t) < 1e-9:
            r['det_check'] = abs(pre['full'][kk]['P'] - f['P']) / max(abs(f['P']), 1e-300)
        rows.append(r)
    return x, rows, ev


def med(vals):
    v = np.array(vals, dtype=float); v = v[np.isfinite(v)]
    return (float(np.median(v)), float(v.min()), float(v.max())) if len(v) else (float('nan'),) * 3


if __name__ == "__main__":
    names = sys.argv[1:]
    table = {}
    for n in names:
        x, rows, ev = load(n)
        ins = [r for r in rows if r['inev']]
        print(f"== {n}: N={x['N']} nu={x['nu']} maxtail={max(x['tail']):.1e} | beta_global max|1-b|={max(abs(1-r['beta_global']) for r in rows):.1e} "
              f"divJ_resid max={max(r['divJ_resid'] for r in rows):.1e} alg max={max(r['alg'] for r in rows):.1e} | determinism max={max(r.get('det_check', 0) for r in rows):.1e} | outputs in events {len(ins)}")
        prof = {lab: med([r['beta_' + lab] for r in ins]) for lab in LABELS}
        print("   beta_B event medians [min,max]: " + "  ".join(f"{lab}={m:.3f}[{lo:.2f},{hi:.2f}]" for lab, (m, lo, hi) in prof.items()))
        print("   Qshare medians: " + "  ".join(f"{lab}={med([r['Qshare_'+lab] for r in ins])[0]:.3f}" for lab in LABELS))
        print("   vol medians: " + "  ".join(f"{lab}={med([r['vol_'+lab] for r in ins])[0]:.4f}" for lab in LABELS))
        # within-event correlations among C1, beta(top1), beta(intense), C4, cos2_2, twist, minrun
        keys = ['C1', 'beta_top1', 'beta_intense', 'C4', 'cos2_2_set', 'twist_share', 'minrun', 'Lam']
        M = np.array([[r[k] for k in keys] for r in ins], dtype=float)
        ok = np.all(np.isfinite(M), axis=1); M = M[ok]
        if len(M) > 3:
            C = np.corrcoef(M.T)
            print("   within-event corr matrix (" + ",".join(keys) + "):")
            for i, k in enumerate(keys):
                print("     %-13s " % k + " ".join(f"{C[i, j]:+.2f}" for j in range(len(keys))))
        table[n] = dict(prof=prof, C1=med([r['C1'] for r in ins])[0], C4=med([r['C4'] for r in ins])[0],
                        beta_top1=med([r['beta_top1'] for r in ins])[0], beta_int=med([r['beta_intense'] for r in ins])[0])
        # time profile of beta(top1) and beta(intense) inside events (for the E0 transition question)
        print("   t: " + " ".join(f"{r['t']:.1f}" for r in ins))
        print("   b1:" + " ".join(f"{r['beta_top1']:.2f}" for r in ins))
        print("   bI:" + " ".join(f"{r['beta_intense']:.2f}" for r in ins))
        print("   C4:" + " ".join(f"{r['C4']:.2f}" for r in ins))
    print("\n== cross-run event medians: run | C1 | beta(top1) | beta(intense) | C4")
    for n, v in table.items():
        print(f"   {n:4s} {v['C1']:.3f} {v['beta_top1']:.3f} {v['beta_int']:.3f} {v['C4']:+.3f}")
    with open(os.path.join(HERE, 'results_xcheck', 'summary_xcheck.json'), 'w') as fh:
        json.dump(table, fh, indent=1)
