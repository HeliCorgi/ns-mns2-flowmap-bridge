"""Literature-faithful filtered near/far decomposition (Yu, arXiv:2606.27560 structure) around the
vorticity maximum, at the M-1 snapshots. POST-HOC / DIAGNOSTIC; EVIDENCE-GRADE, periodic box.

Definitions (instantaneous versions of Yu's r-normalised time-integrated quantities; ratios are
r-independent so the normalisation does not affect the axes):
  * x0 = argmax|omega|, Lambda = |omega(x0)|, s_v = sqrt(nu/Lambda); physical scale R = c s_v (ladder C_LADDER);
    near radius rho R with rho = 1/4 (Yu: 0 < ell <= rho r <= r/4); filter length ell = sigma R, sigma in SIGMA_LADDER
    (Yu requires sigma <= rho).
  * FILTER: Gaussian G_ell (multiplier exp(-|k|^2 ell^2/2)) instead of Yu's compactly supported mollifier phi
    (recorded deviation; the kinematic constants depend on the mollifier, the structure does not).
    U = G_ell * u, Omega = curl U (= G_ell * omega); S_ell = sym grad U.
  * NEAR/FAR KERNEL SPLIT of the strain of Omega (Yu's S^near via the cutoff vartheta(z/(rho r))):
    the R^3 Biot-Savart strain kernel is sampled on the periodic displacement grid z in (-L/2, L/2]^3:
        d_i u_j (x) = (1/4pi) eps_{jab} int Omega_a(x - z) H_{ib}(z) dz,  H_{ib}(z) = delta_{ib}|z|^{-3} - 3 z_i z_b |z|^{-5},
    S^far := convolution with H (1 - vartheta(|z|/(rho R))), vartheta = 1 (s <= 1), cos^2(pi(s-1)/2) (1<s<2), 0 (s >= 2)
    (so 'far' = |z| >= 2 rho R with a smooth transition from rho R), computed by FFT of the sampled far kernel
    (periodisation error O((L/2)^{-3}) relative, recorded); S^near := S_ell - S^far.
  * CUTOFF chi_R as in nearfar_decomp.py (C^1 cos^2, = 1 on B_R, supported in B_2R).
  * FILTERED LOCAL ENSTROPHY BUDGET (exact for the filtered NS equations, Yu Prop. 6.1 structure):
        d/dt int chi |Omega|^2/2 = V_near + V_far - P + Rcomm + Lloc,
        V_near = int chi Omega^T S^near Omega,  V_far = int chi Omega^T S^far Omega,
        P = nu int chi |grad Omega|^2,
        Rcomm = - int chi Omega . curl div tau,   tau_ij = G_ell*(u_i u_j) - U_i U_j   (subgrid stress; commutator forcing),
        Lloc  = int (|Omega|^2/2)(U . grad chi) + nu int (|Omega|^2/2) Delta chi      (localisation residual),
    validated by a one-RK4-step forward difference with frozen chi and filter.
  * Reservoir O = int chi |Omega|^2; local energy M_{R,rho} = R^{-1} int_{B((1+2 rho) R)} |u|^2 (Yu's definition);
    sup_{B_2R}|S^far| for the free far-strain comparator.
  * Axes: A_N = V+_near/P, A_F = V+_far/P, A_C = Rcomm/P (signed) and A_C+ = (Rcomm)_+/P, A_L = Lloc/P,
    A_Fe = V+_far/(sup|S^far| O), g = (V_near + V_far - P + Rcomm + Lloc)/P;
    surplus shares at g > 0: s_N = (V_near - P)/(gP), s_F = V_far/(gP), s_C = Rcomm/(gP), s_L = Lloc/(gP) (sum 1).
Output: results_nearfar_yu/<run>.json
"""
import json, os, sys, time
import numpy as np
import events as ev
from nearfar_decomp import cutoff, quad

HERE = os.path.dirname(os.path.abspath(__file__))
C_LADDER = [8.0, 16.0, 32.0]
SIGMA_LADDER = [0.125, 0.25]
RHO = 0.25
_kernel_cache = {}


def far_kernel_hat(g, rnear):
    key = (g.N, round(rnear, 10))
    if key in _kernel_cache:
        return _kernel_cache[key]
    N, L = g.N, g.L
    x = np.arange(N) * g.dx
    z = np.where(x > L / 2, x - L, x)  # periodic displacement in (-L/2, L/2]
    Z = np.meshgrid(z, z, z, indexing='ij')
    r2 = Z[0] ** 2 + Z[1] ** 2 + Z[2] ** 2
    r = np.sqrt(r2); r_safe = np.where(r == 0, 1.0, r)
    s = r / rnear
    vth = np.where(s <= 1.0, 1.0, np.where(s >= 2.0, 0.0, np.cos(0.5 * np.pi * (s - 1.0)) ** 2))
    far = (1.0 - vth) * (r > 0)
    H = {}
    for i in range(3):
        for b in range(i, 3):
            h = ((1.0 if i == b else 0.0) / r_safe ** 3 - 3 * Z[i] * Z[b] / r_safe ** 5) * far / (4 * np.pi)
            H[(i, b)] = H[(b, i)] = g.rfft(h) * g.dx3 * g.N ** 3  # convolution normalisation: (f*h)^ = N^3 dx^3 f^ h^ / N^3 ... see below
    _kernel_cache[key] = H
    return H


def far_strain(g, Oh, rnear):
    """S^far from the filtered vorticity Fourier coefficients Oh (list of 3 rfft arrays, coefficient convention)."""
    H = far_kernel_hat(g, rnear)
    eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
    du = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = np.zeros_like(Oh[0])
            for a in range(3):
                for b in range(3):
                    e = eps.get((j, a, b), 0)
                    if e:
                        acc = acc + e * H[(i, b)] * Oh[a]
            du[i][j] = g.irfft(acc)
    S = np.empty((g.N, g.N, g.N, 3, 3))
    for i in range(3):
        for j in range(3):
            S[..., i, j] = 0.5 * (du[i][j] + du[j][i])
    return S


def filtered_fields(g, uh, ell):
    Gh = np.exp(-0.5 * g.K2 * ell ** 2)
    Uh = np.array([uh[c] * Gh for c in range(3)])
    Oh = g.curl_h(Uh)
    U = [g.irfft(Uh[c]) for c in range(3)]
    Om = np.array([g.irfft(Oh[c]) for c in range(3)])
    dU = [[g.irfft(1j * g.K[i] * Uh[c]) for c in range(3)] for i in range(3)]
    S = np.empty((g.N, g.N, g.N, 3, 3))
    for i in range(3):
        for j in range(3):
            S[..., i, j] = 0.5 * (dU[i][j] + dU[j][i])
    gradO2 = sum(g.irfft(1j * g.K[i] * Oh[c]) ** 2 for i in range(3) for c in range(3))
    return Uh, Oh, U, Om, S, gradO2, Gh


def commutator_forcing(g, uh, Uh, Gh):
    u = [g.irfft(uh[c]) for c in range(3)]
    U = [g.irfft(Uh[c]) for c in range(3)]
    tau_h = [[g.rfft(u[i] * u[j]) * Gh - g.rfft(U[i] * U[j]) for j in range(3)] for i in range(3)]
    divtau_h = [sum(1j * g.K[j] * tau_h[i][j] for j in range(3)) for i in range(3)]
    curl_h = g.curl_h(divtau_h)
    return np.array([g.irfft(curl_h[c]) for c in range(3)])  # curl div tau


def snapshot(g, uh, nu, dt):
    dx3 = g.dx3
    du = [[g.irfft(1j * g.K[i] * uh[c]) for c in range(3)] for i in range(3)]
    w = np.array([du[1][2] - du[2][1], du[2][0] - du[0][2], du[0][1] - du[1][0]])
    absw = np.sqrt(np.sum(w ** 2, axis=0))
    idx = np.unravel_index(int(np.argmax(absw)), absw.shape); Lam = float(absw[idx])
    u2 = sum(g.irfft(uh[c]) ** 2 for c in range(3))
    E = dx3 * float(np.sum(absw ** 2))
    sv = np.sqrt(nu / Lam)
    uh1 = g.step(uh, nu, dt)
    d2m = ev.periodic_dist2(g, idx)
    out = dict(Lam=Lam, E=E, sv=sv, sv_over_dx=sv / g.dx, ladder=[])
    for c in C_LADDER:
        R = c * sv
        if 2 * R >= g.L / 2:
            continue
        chi, gchi, lchi = cutoff(g, idx, R)
        rnear = RHO * R
        M = dx3 * float(np.sum(u2[d2m <= ((1 + 2 * RHO) * R) ** 2])) / R
        row = dict(c=c, R=R, R_over_dx=R / g.dx, rnear_over_dx=rnear / g.dx, M=M, filters=[])
        for sig in SIGMA_LADDER:
            ell = sig * R
            Uh, Oh, U, Om, S, gradO2, Gh = filtered_fields(g, uh, ell)
            Sfar = far_strain(g, Oh, rnear)
            Snear = S - Sfar
            qn = quad(Om, Snear); qf = quad(Om, Sfar)
            O2 = np.sum(Om ** 2, axis=0)
            P = nu * dx3 * float(np.sum(chi * gradO2)); O = dx3 * float(np.sum(chi * O2))
            Vn = dx3 * float(np.sum(chi * qn)); Vf = dx3 * float(np.sum(chi * qf))
            Vnp = dx3 * float(np.sum(chi * np.maximum(qn, 0))); Vfp = dx3 * float(np.sum(chi * np.maximum(qf, 0)))
            cdt = commutator_forcing(g, uh, Uh, Gh)
            Rc = -dx3 * float(np.sum(chi * np.sum(Om * cdt, axis=0)))
            Ll = dx3 * float(np.sum(0.5 * O2 * sum(U[i] * gchi[i] for i in range(3)))) + nu * dx3 * float(np.sum(0.5 * O2 * lchi))
            # validation: filtered budget vs one-step FD with frozen chi and filter
            Oh1 = g.curl_h(np.array([uh1[cc] * Gh for cc in range(3)]))
            O2_1 = np.sum(np.array([g.irfft(Oh1[cc]) for cc in range(3)]) ** 2, axis=0)
            dfd = (dx3 * float(np.sum(chi * O2_1)) - dx3 * float(np.sum(chi * O2))) / (2.0 * dt)
            dpred = Vn + Vf - P + Rc + Ll
            mask2R = d2m <= (2 * R) ** 2
            supSf = float(np.sqrt(np.max(np.sum(Sfar[mask2R] ** 2, axis=(-2, -1)))))
            gP = dpred
            row['filters'].append(dict(sigma=sig, ell=ell, ell_over_dx=ell / g.dx, P=P, O=O, V_near=Vn, V_far=Vf, Vp_near=Vnp, Vp_far=Vfp,
                                       Rcomm=Rc, Lloc=Ll, dfd=dfd, dpred=dpred,
                                       budget_resid=(dfd - dpred) / max(abs(dfd) + abs(dpred), 1e-300), supSfar=supSf,
                                       A_N=Vnp / P, A_F=Vfp / P, A_C=Rc / P, A_Cp=max(Rc, 0) / P, A_L=Ll / P,
                                       A_Fe=Vfp / max(supSf * O, 1e-300), g=gP / P,
                                       s_N=(Vn - P) / gP if gP != 0 else float('nan'), s_F=Vf / gP if gP != 0 else float('nan'),
                                       s_C=Rc / gP if gP != 0 else float('nan'), s_L=Ll / gP if gP != 0 else float('nan')))
        out['ladder'].append(row)
    return out


def run(name):
    cfg = ev.RUNS[name]
    g = ev.Grid(cfg['N']); nu, T, dt = cfg['nu'], cfg['T'], cfg['dt']
    uh = g.project(cfg['ic'](g)) * g.DEALIAS
    nsteps = int(round(T / dt)); every = max(1, int(round(0.1 / dt)))
    out = dict(name=name, nu=nu, N=cfg['N'], T=T, dt=dt, rho=RHO, t=[], snap=[], tail=[])
    t0 = time.time()
    for step in range(nsteps + 1):
        t = step * dt
        if step % every == 0:
            s = snapshot(g, uh, nu, dt)
            out['t'].append(t); out['snap'].append(s); out['tail'].append(g.tail(uh))
            if s['ladder']:
                r0 = s['ladder'][-1]; f0 = r0['filters'][-1]
                print(f"{name} t={t:.2f} Lam={s['Lam']:.2f} c={r0['c']:g} R/dx={r0['R_over_dx']:.1f} budget={f0['budget_resid']:.1e} "
                      f"A_N={f0['A_N']:.2f} A_F={f0['A_F']:.2f} A_C={f0['A_C']:+.2f} A_L={f0['A_L']:+.2f} g={f0['g']:+.2f}", flush=True)
        if step == nsteps:
            break
        uh = g.step(uh, nu, dt)
    out['walltime_s'] = time.time() - t0
    os.makedirs(os.path.join(HERE, 'results_nearfar_yu'), exist_ok=True)
    with open(os.path.join(HERE, 'results_nearfar_yu', f'{name}.json'), 'w') as fh:
        json.dump(out, fh)
    print(f"{name}: nearfar_yu done in {out['walltime_s']:.1f}s", flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
