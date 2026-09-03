"""POST-HOC (not preregistered; cannot enter the PREREG verdict): near/far strain split at the maximum
point at radii beyond the (under-resolved) viscous scale, including the L^1-sparseness radius
r1 = (||omega||_1 / Lambda)^{1/3} (K = 1), at every 0.1 time units. Re-runs the named runs with the
same solver; records alpha_near/alpha_far/|S_near|/|S_far| and the free far-strain bound ||omega||_1 / r^3.
EVIDENCE-GRADE / DIAGNOSTIC ONLY.
"""
import json, os, sys, time
import numpy as np
import events as ev

HERE = os.path.dirname(os.path.abspath(__file__))


def split_at(g, w, wh_full, uh, idx, xi, Sm, r):
    d2 = ev.periodic_dist2(g, idx)
    mask = d2 <= r ** 2
    whn = [g.rfft(w[c] * mask) for c in range(3)]
    uhn = g.project(g.biot_savart(whn))
    dun = [[g.irfft(1j * g.K[i] * uhn[c])[idx] for c in range(3)] for i in range(3)]
    Sn = np.array([[0.5 * (dun[i][j] + dun[j][i]) for j in range(3)] for i in range(3)])
    an = float(xi @ Sn @ xi)
    return dict(r=float(r), ncells=int(mask.sum()), alpha_near=an, alpha_far=float(xi @ Sm @ xi) - an,
                absS_near=float(np.sqrt(np.sum(Sn ** 2))), absS_far=float(np.sqrt(np.sum((Sm - Sn) ** 2))))


def run(name):
    cfg = ev.RUNS[name]
    g = ev.Grid(cfg['N']); nu, T, dt = cfg['nu'], cfg['T'], cfg['dt']
    uh = g.project(cfg['ic'](g)) * g.DEALIAS
    nsteps = int(round(T / dt)); every = max(1, int(round(0.1 / dt)))
    out = dict(name=name, nu=nu, N=cfg['N'], t=[], rows=[])
    t0 = time.time()
    for step in range(nsteps + 1):
        t = step * dt
        if step % every == 0:
            du = [[g.irfft(1j * g.K[i] * uh[c]) for c in range(3)] for i in range(3)]
            w = np.array([du[1][2] - du[2][1], du[2][0] - du[0][2], du[0][1] - du[1][0]])
            absw = np.sqrt(np.sum(w ** 2, axis=0))
            idx = np.unravel_index(int(np.argmax(absw)), absw.shape)
            Lam = float(absw[idx]); xi = w[:, idx[0], idx[1], idx[2]] / Lam
            Sm = np.array([[0.5 * (du[i][j][idx] + du[j][i][idx]) for j in range(3)] for i in range(3)])
            L1 = g.dx3 * float(np.sum(absw)); E = g.dx3 * float(np.sum(absw ** 2))
            r1 = (L1 / Lam) ** (1.0 / 3.0); rv = np.sqrt(nu / Lam)
            row = dict(t=t, Lam=Lam, L1=L1, E=E, r1=r1, rv=rv, alpha=float(xi @ Sm @ xi), absS=float(np.sqrt(np.sum(Sm ** 2))), splits={})
            for lab, r in (('v2', 2 * rv), ('v4', 4 * rv), ('v8', 8 * rv), ('r1/2', r1 / 2), ('r1', r1), ('2r1', 2 * r1)):
                if r < g.L / 2:
                    s = split_at(g, w, None, uh, idx, xi, Sm, r)
                    s['free_far_bound'] = L1 / r ** 3
                    row['splits'][lab] = s
            out['t'].append(t); out['rows'].append(row)
        if step == nsteps:
            break
        uh = g.step(uh, nu, dt)
    out['walltime_s'] = time.time() - t0
    with open(os.path.join(HERE, 'results', f'{name}_nearfar.json'), 'w') as f:
        json.dump(out, f)
    print(f"{name}: nearfar done in {out['walltime_s']:.1f}s", flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
