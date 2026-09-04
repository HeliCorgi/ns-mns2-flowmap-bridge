"""Finite-scale near/far decomposition of the vortex stretching in the local enstrophy budget
around the vorticity maximum (twenty-ninth session). POST-HOC / DIAGNOSTIC (the preregistered
verdict and resolution rule of the M-1 study are unchanged). EVIDENCE-GRADE, periodic box.

Fully recorded definitions (the commission requires the kernel/filter/cutoff to be explicit):

  * x0 = argmax |omega| at the snapshot; Lambda = |omega(x0)|; viscous scale s_v = sqrt(nu/Lambda).
  * CUTOFF chi_R(x) = chi0(|x - x0|_per / R), chi0(s) = 1 (s <= 1), cos^2(pi (s-1)/2) (1 < s < 2), 0 (s >= 2)
    -- C^1, supported in B(x0, 2R), = 1 on B(x0, R); R = c s_v on the ladder c in C_LADDER.
    grad chi and Delta chi are computed spectrally from chi (so that the identities below hold on the grid).
  * FILTER: Gaussian G_ell with Fourier multiplier exp(-|k|^2 ell^2 / 2), ell = sigma R, sigma in SIGMA_LADDER.
    omega_bar = G_ell * omega (large scales, 'far'), omega' = omega - omega_bar (subfilter, 'near').
    S_bar = S[omega_bar] = G_ell * S (linear), S' = S - S_bar.
  * EXACT three-way split of q = omega^T S omega:
        q_far  = omega_bar^T S_bar omega_bar          (resolved x resolved)
        q_near = omega'^T S' omega'                  (subfilter x subfilter)
        q_comm = q - q_far - q_near                  (all cross terms: the 'filter commutator work')
  * LOCAL ENSTROPHY BUDGET (exact for the continuous equations):
        d/dt int chi |omega|^2/2 = int chi q - nu int chi |grad omega|^2 + C_loc,
        C_loc = int (|omega|^2/2) (u . grad chi) + nu int (|omega|^2/2) Delta chi     (localization residual)
    validated by a one-RK4-step forward difference with the SAME frozen chi.
  * Quantities: V+_near = int chi (q_near)_+, V+_far = int chi (q_far)_+, V+_comm = int chi (q_comm)_+,
    signed V_near, V_far, V_comm; P = nu int chi |grad omega|^2 (local palinstrophy / diffusion companion);
    O = int chi |omega|^2 (local enstrophy reservoir); M_{R,rho} = R^{-1} int_{B(x0, rho R)} |u|^2 (rho = 2),
    scale-invariant local energy; supSbar = sup_{B(x0,2R)} |S_bar| (free-bound comparator);
    localized Betchov check: int chi q + 4 int chi det S + int J_B . grad chi = 0 (relative residual),
    with |int J_B . grad chi| reported against nu ||grad^2 u||_2^2 (whole domain) and E = ||omega||_2^2.
  * Dimensionless axes (all denominators strictly positive for a nonzero field):
        A_N = V+_near / P,  A_F = V+_far / P,  A_C = V+_comm / P,  A_L = C_loc / P,
        A_Fe = V+_far / (supSbar * O)  in [0, 1],  g = (int chi q - P + C_loc) / P  (local growth rate / P),
    and the surplus shares at growth outputs (g > 0):
        s_N = (V_near - P)/(g P), s_F = V_far/(g P), s_C = V_comm/(g P), s_L = C_loc/(g P)   (sum = 1).
Output: results_nearfar/<run>.json.
"""
import json, os, sys, time
import numpy as np
import events as ev

HERE = os.path.dirname(os.path.abspath(__file__))
C_LADDER = [8.0, 16.0, 32.0]
SIGMA_LADDER = [0.25, 0.5]
RHO = 2.0


def cutoff(g, idx, R):
    d2 = ev.periodic_dist2(g, idx)
    s = np.sqrt(d2) / R
    chi = np.where(s <= 1.0, 1.0, np.where(s >= 2.0, 0.0, np.cos(0.5 * np.pi * (s - 1.0)) ** 2))
    chih = g.rfft(chi)
    gchi = [g.irfft(1j * g.K[i] * chih) for i in range(3)]
    lchi = g.irfft(-g.K2 * chih)
    return chi, gchi, lchi


def strain_of(g, wh):
    uh = g.project(g.biot_savart(wh))
    du = [[g.irfft(1j * g.K[i] * uh[c]) for c in range(3)] for i in range(3)]
    S = np.empty((g.N, g.N, g.N, 3, 3))
    for i in range(3):
        for j in range(3):
            S[..., i, j] = 0.5 * (du[i][j] + du[j][i])
    return S


def quad(w, S):
    wt = w.transpose(1, 2, 3, 0)
    return np.einsum('abci,abcij,abcj->abc', wt, S, wt)


def snapshot(g, uh, nu, dt):
    K, K2, dx3 = g.K, g.K2, g.dx3
    u = [g.irfft(uh[i]) for i in range(3)]
    du = [[g.irfft(1j * K[i] * uh[c]) for c in range(3)] for i in range(3)]
    w = np.array([du[1][2] - du[2][1], du[2][0] - du[0][2], du[0][1] - du[1][0]])
    wh = [g.rfft(w[c]) for c in range(3)]
    S = np.empty((g.N, g.N, g.N, 3, 3))
    for i in range(3):
        for j in range(3):
            S[..., i, j] = 0.5 * (du[i][j] + du[j][i])
    lam = np.linalg.eigvalsh(S)
    det = lam[..., 0] * lam[..., 1] * lam[..., 2]
    q = quad(w, S)
    w2 = np.sum(w ** 2, axis=0); absw = np.sqrt(w2)
    idx = np.unravel_index(int(np.argmax(absw)), absw.shape); Lam = float(absw[idx])
    dw2 = sum(g.irfft(1j * K[i] * wh[c]) ** 2 for i in range(3) for c in range(3))
    lap_u2 = dx3 * float(np.sum(sum(g.irfft(-K2 * uh[c]) ** 2 for c in range(3))))  # ||Lap u||^2 = ||grad^2 u||^2
    E = dx3 * float(np.sum(w2))
    # J_B for the localized Betchov check
    trA2 = sum(du[i][j] * du[j][i] for i in range(3) for j in range(3))
    adv = [sum(u[j] * du[j][k] for j in range(3)) for k in range(3)]
    J = [(4.0 / 3.0) * (sum(adv[k] * du[k][i] for k in range(3)) - 0.5 * u[i] * trA2) for i in range(3)]
    u2 = sum(ui ** 2 for ui in u)
    # one RK4 step for the local-budget validation (frozen chi)
    uh1 = g.step(uh, nu, dt)
    du1 = [[g.irfft(1j * K[i] * uh1[c]) for c in range(3)] for i in range(3)]
    w1 = np.array([du1[1][2] - du1[2][1], du1[2][0] - du1[0][2], du1[0][1] - du1[1][0]])
    w2_1 = np.sum(w1 ** 2, axis=0)
    sv = np.sqrt(nu / Lam)
    out = dict(Lam=Lam, E=E, sv=sv, sv_over_dx=sv / g.dx, ladder=[])
    for c in C_LADDER:
        R = c * sv
        if 2 * R >= g.L / 2:
            continue
        chi, gchi, lchi = cutoff(g, idx, R)
        P = nu * dx3 * float(np.sum(chi * dw2))
        O = dx3 * float(np.sum(chi * w2))
        Q = dx3 * float(np.sum(chi * q))
        Dt = -4.0 * dx3 * float(np.sum(chi * det))
        JB = dx3 * float(np.sum(sum(J[i] * gchi[i] for i in range(3))))
        betchov_resid = (Q - Dt + JB) / max(abs(Q) + abs(Dt) + abs(JB), 1e-300)
        Cloc_t = dx3 * float(np.sum(0.5 * w2 * sum(u[i] * gchi[i] for i in range(3))))
        Cloc_d = nu * dx3 * float(np.sum(0.5 * w2 * lchi))
        Cloc = Cloc_t + Cloc_d
        dloc_fd = (dx3 * float(np.sum(chi * w2_1)) - dx3 * float(np.sum(chi * w2))) / (2.0 * dt)  # d/dt int chi |w|^2/2 (forward)
        dloc_pred = Q - P + Cloc
        d2m = ev.periodic_dist2(g, idx)
        M = dx3 * float(np.sum(u2[d2m <= (RHO * R) ** 2])) / R
        row = dict(c=c, R=R, R_over_dx=R / g.dx, P=P, O=O, Q=Q, D=Dt, JB=JB, betchov_resid=betchov_resid,
                   Cloc=Cloc, Cloc_transport=Cloc_t, Cloc_diffusion=Cloc_d, dloc_fd=dloc_fd, dloc_pred=dloc_pred,
                   budget_resid=(dloc_fd - dloc_pred) / max(abs(dloc_fd) + abs(dloc_pred), 1e-300),
                   M=M, JB_over_nuLap=abs(JB) / max(nu * lap_u2, 1e-300), filters=[])
        for sig in SIGMA_LADDER:
            ell = sig * R
            Gh = np.exp(-0.5 * K2 * ell ** 2)
            whb = [wh[cc] * Gh for cc in range(3)]
            wb = np.array([g.irfft(whb[cc]) for cc in range(3)])
            Sb = strain_of(g, whb)
            wp = w - wb; Sp = S - Sb
            qf = quad(wb, Sb); qn = quad(wp, Sp); qc = q - qf - qn
            Vn = dx3 * float(np.sum(chi * qn)); Vf = dx3 * float(np.sum(chi * qf)); Vc = dx3 * float(np.sum(chi * qc))
            Vnp = dx3 * float(np.sum(chi * np.maximum(qn, 0))); Vfp = dx3 * float(np.sum(chi * np.maximum(qf, 0)))
            Vcp = dx3 * float(np.sum(chi * np.maximum(qc, 0)))
            mask2R = d2m <= (2 * R) ** 2
            supSb = float(np.sqrt(np.max(np.sum(Sb[mask2R] ** 2, axis=(-2, -1)))))
            gP = Q - P + Cloc
            row['filters'].append(dict(sigma=sig, ell=ell, ell_over_dx=ell / g.dx,
                                       V_near=Vn, V_far=Vf, V_comm=Vc, Vp_near=Vnp, Vp_far=Vfp, Vp_comm=Vcp,
                                       supSbar=supSb,
                                       A_N=Vnp / P, A_F=Vfp / P, A_C=Vcp / P, A_L=Cloc / P, A_Fe=Vfp / max(supSb * O, 1e-300),
                                       g=gP / P,
                                       s_N=(Vn - P) / gP if gP != 0 else float('nan'), s_F=Vf / gP if gP != 0 else float('nan'),
                                       s_C=Vc / gP if gP != 0 else float('nan'), s_L=Cloc / gP if gP != 0 else float('nan')))
        out['ladder'].append(row)
    return out


def run(name):
    cfg = ev.RUNS[name]
    g = ev.Grid(cfg['N']); nu, T, dt = cfg['nu'], cfg['T'], cfg['dt']
    uh = g.project(cfg['ic'](g)) * g.DEALIAS
    nsteps = int(round(T / dt)); every = max(1, int(round(0.1 / dt)))
    out = dict(name=name, nu=nu, N=cfg['N'], T=T, dt=dt, t=[], snap=[], tail=[])
    t0 = time.time()
    for step in range(nsteps + 1):
        t = step * dt
        if step % every == 0:
            s = snapshot(g, uh, nu, dt)
            out['t'].append(t); out['snap'].append(s); out['tail'].append(g.tail(uh))
            r0 = s['ladder'][0] if s['ladder'] else None
            if r0:
                f0 = r0['filters'][0]
                print(f"{name} t={t:.2f} Lam={s['Lam']:.2f} sv/dx={s['sv_over_dx']:.2f} | c={r0['c']:g} R/dx={r0['R_over_dx']:.1f} "
                      f"betchov={r0['betchov_resid']:.1e} budget={r0['budget_resid']:.1e} A_N={f0['A_N']:.2f} A_F={f0['A_F']:.2f} "
                      f"A_C={f0['A_C']:.2f} A_L={f0['A_L']:+.2f} g={f0['g']:+.2f}", flush=True)
        if step == nsteps:
            break
        uh = g.step(uh, nu, dt)
    out['walltime_s'] = time.time() - t0
    os.makedirs(os.path.join(HERE, 'results_nearfar'), exist_ok=True)
    with open(os.path.join(HERE, 'results_nearfar', f'{name}.json'), 'w') as fh:
        json.dump(out, fh)
    print(f"{name}: nearfar done in {out['walltime_s']:.1f}s", flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
