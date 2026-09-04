"""Stateflow harness for the near/far decomposition (twenty-ninth session).
Uses kernel-dynamics-viewer/stateflow (HeliCorgi/kernel-dynamics-viewer, commit 3fb6421) ONLY as the
episode / transition / persistence / mask harness: FeatureSeries (with mask), Trajectory,
TransitionAnalyzer, and the three-part IndependenceEvidence structure. No NS theorem is generated here.
Set STATEFLOW_PATH to the cloned repository root (defaults to ../../../kernel-dynamics-viewer).
Reads results_nearfar/<run>.json (nearfar_decomp.py) and results/<run>.json (preregistered diagnostics)
and results_xcheck/<run>.json (for cos^2 theta_2 on the intense set, C1, C4 at the same snapshots).
Masks: tail <= 1e-5 (standing rule), R >= 3 dx, ell >= 1.5 dx, all axes finite.
"""
import json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SF = os.environ.get('STATEFLOW_PATH', os.path.join(HERE, '..', '..', '..', 'kernel-dynamics-viewer'))
sys.path.insert(0, SF)
from stateflow.core import FeatureSeries, Trajectory, TransitionAnalyzer  # noqa: E402
from stateflow.independence import IndependenceEvidence  # noqa: E402
import postprocess as pp  # noqa: E402

AXES = ['A_N', 'A_F', 'A_C', 'A_L', 'A_Fe', 'g', 's_N', 's_F', 's_C', 's_L']
MODE = os.environ.get('NF_MODE', 'subfilter')  # 'subfilter' -> results_nearfar (nearfar_decomp.py); 'yu' -> results_nearfar_yu (nearfar_yu.py)
RESDIR = {'subfilter': 'results_nearfar', 'yu': 'results_nearfar_yu'}[MODE]
CLASSES = {'s_F': 'FAR', 's_C': 'COMM', 's_L': 'LOC'}


def build(name, c, sigma):
    nf = json.load(open(os.path.join(HERE, RESDIR, f'{name}.json')))
    pre = json.load(open(os.path.join(HERE, 'results', f'{name}.json')))
    xc = json.load(open(os.path.join(HERE, 'results_xcheck', f'{name}.json')))
    ev = pp.growth_events(np.array(pre['t_cheap']), np.array(pre['enstrophy']))
    t = np.array(nf['t']); T = len(t)
    cols = {k: np.full(T, np.nan) for k in AXES + ['Lam', 'R_over_dx', 'ell_over_dx', 'P', 'O', 'M', 'JB_over_nuLap',
                                                   'betchov_resid', 'budget_resid', 'cos2_2_set', 'C1', 'C4', 'Eprime', 'inev']}
    tail = np.array(nf['tail'])
    dx = 2 * np.pi / nf['N']
    Ec = np.array(pre['enstrophy']); tc = np.array(pre['t_cheap']); dE = np.gradient(Ec, tc)
    for k, s in enumerate(nf['snap']):
        cols['Lam'][k] = s['Lam']; cols['inev'][k] = float(any(a <= t[k] <= b for a, b, _, _ in ev))
        cols['Eprime'][k] = float(np.interp(t[k], tc, dE))
        row = next((r for r in s['ladder'] if abs(r['c'] - c) < 1e-9), None)
        if row is None:
            continue
        f = next((ff for ff in row['filters'] if abs(ff['sigma'] - sigma) < 1e-9), None)
        if f is None:
            continue
        for kk in ('R_over_dx', 'M'):
            cols[kk][k] = row[kk]
        if MODE == 'subfilter':
            for kk in ('P', 'O', 'JB_over_nuLap', 'betchov_resid', 'budget_resid'):
                cols[kk][k] = row[kk]
        else:
            for kk in ('P', 'O', 'budget_resid'):
                cols[kk][k] = f[kk]
        cols['ell_over_dx'][k] = f['ell_over_dx']
        for kk in AXES:
            cols[kk][k] = f[kk]
        # matched preregistered / cross-check diagnostics at the same time
        kx = int(np.argmin(np.abs(np.array(xc['t']) - t[k])))
        if abs(xc['t'][kx] - t[k]) < 1e-9:
            fx = xc['full'][kx]; rx = pp.ratios(fx)
            cols['cos2_2_set'][k] = rx['cos2_2_set']; cols['C1'][k] = rx['C1']; cols['C4'][k] = rx['C4']
    names = list(cols.keys())
    F = np.stack([cols[n] for n in names], axis=1)
    mask = (tail <= 1e-5) & (cols['R_over_dx'] >= 3.0) & (cols['ell_over_dx'] >= 1.5) & np.all(np.isfinite(F[:, [names.index(a) for a in ['A_N', 'A_F', 'A_C', 'A_L', 'g']]]), axis=1)
    fs = FeatureSeries(time=t, features=F, feature_names=names, mask=mask,
                       metadata=dict(provenance=f'{name}: mode={MODE} c={c} sigma={sigma}; cutoff cos^2 C^1 at R=c sqrt(nu/Lam) around argmax|omega|; Gaussian filter ell=sigma R; masks tail<=1e-5, R>=3dx, ell>=1.5dx',
                                     source='experiments/m1_events', units='dimensionless axes', N=nf['N'], nu=nf['nu']))
    return fs, ev


def dominant_labels(fs):
    """Per-step label: which residual class carries the largest POSITIVE share of the local growth surplus
    (only at growth steps, g > 0, inside a global growth event and unmasked); None otherwise."""
    g = fs.column('g'); inev = fs.column('inev')
    labels = []
    for k in range(len(fs.time)):
        if not fs.mask[k] or not (g[k] > 0) or inev[k] < 0.5:
            labels.append(None); continue
        shares = {CLASSES[s]: fs.column(s)[k] for s in CLASSES}
        lab = max(shares, key=shares.get)
        labels.append(lab if shares[lab] > 0 else 'NONE')
    return labels


def analyze(name, c, sigma):
    fs, ev = build(name, c, sigma)
    ta = TransitionAnalyzer()
    A_N = Trajectory(times=fs.time, values=fs.column('A_N'), mask=fs.mask, name='A_N')
    absorbed = ta.from_threshold(fs.time, np.where(fs.mask, fs.column('A_N'), np.nan), 1.0)  # A_N > 1 = near NOT absorbed
    labels = dominant_labels(fs)
    lab_traj = ta.from_labels(fs.time, labels)
    m = fs.mask & (fs.column('inev') > 0.5)
    mg = m & (fs.column('g') > 0)
    def med(col, mm):
        v = fs.column(col)[mm]; v = v[np.isfinite(v)]
        return (float(np.median(v)), float(v.min()), float(v.max())) if len(v) else (np.nan,) * 3
    summary = dict(run=name, c=c, sigma=sigma, n_masked_in=int(m.sum()), n_growth=int(mg.sum()), n_total=len(fs.time),
                   R_over_dx=med('R_over_dx', m), ell_over_dx=med('ell_over_dx', m),
                   betchov_resid_max=float(np.nanmax(np.abs(fs.column('betchov_resid')[m]))) if m.any() else np.nan,
                   budget_resid_max=float(np.nanmax(np.abs(fs.column('budget_resid')[m]))) if m.any() else np.nan,
                   axes_in_event={a: med(a, m) for a in ['A_N', 'A_F', 'A_C', 'A_L', 'A_Fe', 'g', 'M', 'JB_over_nuLap']},
                   shares_at_growth={s: med(s, mg) for s in ['s_N', 's_F', 's_C', 's_L']},
                   dominant_counts={lab: int(sum(1 for l in labels if l == lab)) for lab in ('FAR', 'COMM', 'LOC', 'NONE')},
                   label_transitions=[(tr.time, tr.kind) for tr in lab_traj.transitions],
                   label_persistence=TransitionAnalyzer.persistence(lab_traj), label_recurrence=TransitionAnalyzer.recurrence(lab_traj),
                   A_N_crossings=[(tr.time, tr.kind) for tr in absorbed.transitions],
                   frac_absorbed_in_event=float(np.mean(fs.column('A_N')[m] < 1.0)) if m.any() else np.nan)
    return fs, labels, summary


if __name__ == "__main__":
    runs = sys.argv[1:]
    allsum = []
    for name in runs:
        nf = json.load(open(os.path.join(HERE, RESDIR, f'{name}.json')))
        cs = sorted({r['c'] for s in nf['snap'] for r in s['ladder']})
        for c in cs:
            for sigma in ((0.25, 0.5) if MODE == 'subfilter' else (0.125, 0.25)):
                fs, labels, summ = analyze(name, c, sigma)
                allsum.append(summ)
                print(f"== {name} c={c:g} sigma={sigma}: masked-in-event {summ['n_masked_in']}/{summ['n_total']} (growth {summ['n_growth']}); R/dx med {summ['R_over_dx'][0]:.1f}; "
                      f"betchov {summ['betchov_resid_max']:.1e} budget {summ['budget_resid_max']:.1e}")
                if summ['n_masked_in']:
                    ax = summ['axes_in_event']
                    print("   axes med[min,max]: " + "  ".join(f"{a}={v[0]:.3f}[{v[1]:.2f},{v[2]:.2f}]" for a, v in ax.items()))
                    sh = summ['shares_at_growth']
                    print("   surplus shares at growth med[min,max]: " + "  ".join(f"{a}={v[0]:+.2f}[{v[1]:+.2f},{v[2]:+.2f}]" for a, v in sh.items()))
                    print(f"   dominant class counts {summ['dominant_counts']}; transitions {summ['label_transitions']}; persistence {summ['label_persistence']:.2f}; recurrence {summ['label_recurrence']}; frac A_N<1 {summ['frac_absorbed_in_event']:.2f}; A_N crossings {summ['A_N_crossings']}")
    with open(os.path.join(HERE, RESDIR, 'stateflow_summary.json'), 'w') as fh:
        json.dump(allsum, fh, indent=1, default=float)
