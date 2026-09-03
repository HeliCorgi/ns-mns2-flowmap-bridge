"""Postprocessing for the M-1 re-opened event study (PREREG.md section 3-4).
Growth events: maximal intervals of increasing enstrophy in the cheap series (t_cheap, enstrophy),
smoothed by requiring a net rise >= 1% of E over the interval. Ratios C1-C5 are evaluated at every
full-diagnostic output whose time lies inside a growth event. Resolution rule: max tail <= 1e-5.
"""
import json, sys, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def growth_events(t, E, min_rel_rise=0.01):
    t = np.asarray(t); E = np.asarray(E)
    d = np.diff(E)
    events = []
    i = 0
    while i < len(d):
        if d[i] > 0:
            j = i
            while j < len(d) and d[j] > 0:
                j += 1
            if E[j] - E[i] >= min_rel_rise * E[i]:
                events.append((t[i], t[j], E[i], E[j]))
            i = j
        else:
            i += 1
    return events


def ratios(full):
    mx = full['max']
    C1 = full['P'] / max(full['G'], 1e-300)
    C2 = full['P'] / max(full['P_abs'], 1e-300)
    a = mx['alpha']
    C3 = (a - mx['nu_twist'] + mx['nu_lap']) / a if abs(a) > 1e-12 else float('nan')
    s = full['sets']['0.25']['lam2_terms']
    C4 = (s['self'] + s['vort'] + s['press']) / s['vort'] if s['vort'] > 0 else float('nan')
    nr = mx['near']['1.0']
    C5 = nr['alpha_far'] / a if abs(a) > 1e-12 else float('nan')
    C5p = a / mx['absS'] if mx['absS'] > 0 else float('nan')
    return dict(C1=C1, C2=C2, C3=C3, C4=C4, C5=C5, C5p=C5p,
                depletion_set=full['sets']['0.25']['P'] / max(full['sets']['0.25']['G'], 1e-300),
                lam2pos_frac=full['sets']['0.25']['lam2pos_frac'],
                minrun=mx['minrun_over_scale'], fat1=min(mx['fatcore']['1.0'].values()), fat2=min(mx['fatcore']['2.0'].values()),
                cos2_2=full['cos2'][1], cos2_2_set=full['sets']['0.25']['cos2'][1],
                twist_share=full['diss_twist'] / max(full['diss'], 1e-300), Efrac25=full['sets']['0.25']['Efrac'],
                volfrac25=full['sets']['0.25']['volfrac'])


def summarize(name):
    d = json.load(open(os.path.join(HERE, 'results', f'{name}.json')))
    tc, Ec = np.array(d['t_cheap']), np.array(d['enstrophy'])
    ev = growth_events(tc, Ec)
    maxtail = max(d['tail'])
    resolved = maxtail <= 1e-5
    vals = {k: max(f['validation'][k] for f in d['full']) for k in d['full'][0]['validation']}
    tf = np.array(d['t_full'])
    rows = []
    for k, f in enumerate(d['full']):
        inev = any(a <= tf[k] <= b for a, b, _, _ in ev)
        r = ratios(f)
        r['t'] = float(tf[k]); r['E'] = f['E']; r['inev'] = inev; r['Lam'] = f['max']['Lam']; r['alpha'] = f['max']['alpha']
        rows.append(r)
    # finite-difference d/dt log Lam for the C3 consistency check
    lams = np.array([f['max']['Lam'] for f in d['full']])
    dlog = np.gradient(np.log(lams), tf)
    for k, r in enumerate(rows):
        r['dlogLam_fd'] = float(dlog[k]); r['rate_pred'] = r['alpha'] - d['full'][k]['max']['nu_twist'] + d['full'][k]['max']['nu_lap']
    inrows = [r for r in rows if r['inev']]
    def rng(key):
        v = np.array([r[key] for r in inrows], dtype=float); v = v[np.isfinite(v)]
        return (float(v.min()), float(v.max()), float(np.median(v))) if len(v) else (float('nan'),) * 3
    summary = dict(name=name, nu=d['nu'], N=d['N'], resolved=resolved, maxtail=maxtail, validation_max=vals,
                   events=[(float(a), float(b), float(e0), float(e1)) for a, b, e0, e1 in ev],
                   E_range=(float(Ec.min()), float(Ec.max())), n_full_in_events=len(inrows),
                   ranges={k: rng(k) for k in ('C1', 'C2', 'C3', 'C4', 'C5', 'C5p', 'depletion_set', 'lam2pos_frac', 'minrun', 'fat1', 'fat2', 'cos2_2', 'cos2_2_set', 'twist_share', 'Efrac25', 'volfrac25')},
                   rows=rows)
    return summary


if __name__ == "__main__":
    names = sys.argv[1:]
    allsum = {}
    for n in names:
        s = summarize(n)
        allsum[n] = s
        print(f"== {n}: nu={s['nu']} N={s['N']} resolved={s['resolved']} maxtail={s['maxtail']:.2e} E {s['E_range'][0]:.1f}-{s['E_range'][1]:.1f}")
        print("   validation max:", {k: f'{v:.1e}' for k, v in s['validation_max'].items()})
        print("   events (t0,t1,E0,E1):", [tuple(round(x, 2) for x in e) for e in s['events']], "| full outputs in events:", s['n_full_in_events'])
        for k, (lo, hi, med) in s['ranges'].items():
            print(f"   {k:14s} min {lo:8.3f} max {hi:8.3f} median {med:8.3f}")
        # C3 consistency: compare predicted rate with finite difference inside events
        ins = [r for r in s['rows'] if r['inev']]
        if ins:
            err = [abs(r['rate_pred'] - r['dlogLam_fd']) / max(abs(r['dlogLam_fd']), 1e-9) for r in ins]
            print(f"   C3 consistency |rate_pred - dlogLam_fd|/|fd|: median {np.median(err):.2f} max {np.max(err):.2f}")
    with open(os.path.join(HERE, 'results', 'summary.json'), 'w') as f:
        json.dump({k: {kk: vv for kk, vv in v.items() if kk != 'rows'} for k, v in allsum.items()}, f, indent=1)
