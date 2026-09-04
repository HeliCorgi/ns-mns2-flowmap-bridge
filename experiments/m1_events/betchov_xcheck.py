"""POST-HOC ADVERSARIAL CROSS-CHECK (not part of the PREREG verdict; the preregistration,
resolution rule and the DIAGNOSTIC-ONLY verdict of the M-1 study are unchanged).

Local Betchov identity (exact for divergence-free fields):
    q := omega^T S omega,   q + 4 det S = div J_B,
    J_B = (4/3) B,  B_i = u_j A_jk A_ki - (1/2) u_i tr(A^2),  A_ij = d_i u_j,
and in the enstrophy equation the modified flux is -J_B. For a region Omega
    beta_B(Omega) := (-4 int_Omega det S) / (int_Omega q)          [GPT-side convention]
so beta_B < 1  <=>  int_Omega q > -4 int_Omega det S  <=>  the modified flux -J_B converges into Omega
("flux-fed"); beta_B(whole torus) = 1 (implementation validation).
Sets: top-theta % of positive q (quantile among q > 0 points), theta in {0.5,1,2,5,10,20};
the intense mask {lambda_2 > 0} & {|omega| > 0.25 Lambda}; the whole domain.
At every full output the preregistered diagnostics (events.full_diag) are recomputed on the same
snapshot (determinism check against results/*.json) so that (C1, beta_B(theta), C4, ...) are matched.
Output: results_xcheck/<run>.json. EVIDENCE-GRADE / DIAGNOSTIC ONLY.
"""
import json, os, sys, time
import numpy as np
import events as ev

HERE = os.path.dirname(os.path.abspath(__file__))
THETAS = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]


def beta_diag(g, uh):
    K = g.K
    u = [g.irfft(uh[i]) for i in range(3)]
    du = [[g.irfft(1j * K[i] * uh[c]) for c in range(3)] for i in range(3)]  # du[i][c] = d_i u_c = A_ic
    w = np.array([du[1][2] - du[2][1], du[2][0] - du[0][2], du[0][1] - du[1][0]])
    S = np.empty((g.N, g.N, g.N, 3, 3))
    for i in range(3):
        for j in range(3):
            S[..., i, j] = 0.5 * (du[i][j] + du[j][i])
    lam = np.linalg.eigvalsh(S)
    wt = w.transpose(1, 2, 3, 0)
    q = np.einsum('abci,abcij,abcj->abc', wt, S, wt)
    det = lam[..., 0] * lam[..., 1] * lam[..., 2]
    absw = np.sqrt(np.sum(w ** 2, axis=0)); Lam = float(absw.max())
    # flux J_B and its divergence (validation of the local identity)
    trA2 = sum(du[i][j] * du[j][i] for i in range(3) for j in range(3))
    adv = [sum(u[j] * du[j][k] for j in range(3)) for k in range(3)]          # (u . grad) u
    B = [sum(adv[k] * du[k][i] for k in range(3)) - 0.5 * u[i] * trA2 for i in range(3)]
    J = [(4.0 / 3.0) * B[i] for i in range(3)]
    divJ = sum(g.irfft(1j * K[i] * g.rfft(J[i])) for i in range(3))
    resid = float(np.sqrt(np.sum((q + 4 * det - divJ) ** 2) / max(np.sum(q ** 2), 1e-300)))
    alg = q + 4 * det
    trA3 = sum(du[i][j] * du[j][k] * du[k][i] for i in range(3) for j in range(3) for k in range(3))
    alg_err = float(np.sqrt(np.sum((alg - (4.0 / 3.0) * trA3) ** 2) / max(np.sum(q ** 2), 1e-300)))
    dx3 = g.dx3
    Q = dx3 * float(np.sum(q)); D = -4.0 * dx3 * float(np.sum(det))
    out = dict(Lam=Lam, Q=Q, D=D, beta_global=D / Q if abs(Q) > 1e-300 else float('nan'),
               divJ_resid_rel=resid, alg_identity_rel=alg_err, fpos=float(np.mean(q > 0)), sets={})
    qpos = q[q > 0]

    def region(m, label):
        Qm = dx3 * float(np.sum(q[m])); Dm = -4.0 * dx3 * float(np.sum(det[m]))
        out['sets'][label] = dict(vol=float(np.mean(m)), Q=Qm, D=Dm, beta=Dm / Qm if abs(Qm) > 1e-300 else float('nan'),
                                  Qshare=Qm / Q if abs(Q) > 1e-300 else float('nan'),
                                  flux=Qm - Dm, lam2pos=float(np.mean(lam[..., 1][m] > 0)) if m.any() else float('nan'),
                                  Eshare=float(np.sum(absw[m] ** 2) / max(np.sum(absw ** 2), 1e-300)))
    for th in THETAS:
        thr = float(np.quantile(qpos, 1.0 - th / 100.0)) if qpos.size else np.inf
        region(q > thr, f'top{th:g}')
    region((lam[..., 1] > 0) & (absw > 0.25 * Lam), 'intense')
    region(absw > 0.25 * Lam, 'omega25')
    return out


def run(name):
    cfg = ev.RUNS[name]
    g = ev.Grid(cfg['N']); nu, T, dt = cfg['nu'], cfg['T'], cfg['dt']
    uh = g.project(cfg['ic'](g)) * g.DEALIAS
    nsteps = int(round(T / dt)); every = max(1, int(round(0.1 / dt)))
    out = dict(name=name, nu=nu, N=cfg['N'], T=T, dt=dt, t=[], beta=[], full=[], tail=[])
    t0 = time.time()
    for step in range(nsteps + 1):
        t = step * dt
        if step % every == 0:
            b = beta_diag(g, uh); f = ev.full_diag(g, uh, nu)
            out['t'].append(t); out['beta'].append(b); out['full'].append(f); out['tail'].append(g.tail(uh))
            print(f"{name} t={t:.2f} beta_glob={b['beta_global']:.6f} divJ_resid={b['divJ_resid_rel']:.1e} "
                  f"b(top1)={b['sets']['top1']['beta']:.3f} b(int)={b['sets']['intense']['beta']:.3f} C1={f['P']/max(f['G'],1e-300):.3f}", flush=True)
        if step == nsteps:
            break
        uh = g.step(uh, nu, dt)
    out['walltime_s'] = time.time() - t0
    os.makedirs(os.path.join(HERE, 'results_xcheck'), exist_ok=True)
    with open(os.path.join(HERE, 'results_xcheck', f'{name}.json'), 'w') as fh:
        json.dump(out, fh)
    print(f"{name}: xcheck done in {out['walltime_s']:.1f}s", flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
