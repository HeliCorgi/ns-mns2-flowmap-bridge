"""M-1 re-opened (twenty-seventh session): term-by-term budgets of enstrophy-growth events.

Pseudo-spectral incompressible NS on [0,2pi)^3 (rotational form, Leray projection, 2/3 dealias,
RK4), re-implemented with parametrised N from experiments/tgram_probe/tgram_probe.py with the same
conventions (u = sum uh e^{ikx}); cross-validated against the stored T-GRAM R1 energy series (run E0).
EVIDENCE-GRADE / DIAGNOSTIC ONLY. PREREG.md governs: runs, observables, tolerances, verdict rule.
"""
import json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


class Grid:
    def __init__(self, N, L=2 * np.pi):
        self.N, self.L = N, L
        k1 = np.fft.fftfreq(N, d=1.0 / N)
        kz = k1[: N // 2 + 1]
        KX = np.broadcast_to(k1[:, None, None], (N, N, N // 2 + 1))
        KY = np.broadcast_to(k1[None, :, None], (N, N, N // 2 + 1))
        KZ = np.broadcast_to(kz[None, None, :], (N, N, N // 2 + 1))
        self.K = [KX, KY, KZ]
        self.K2 = KX ** 2 + KY ** 2 + KZ ** 2
        self.K2s = np.where(self.K2 == 0, 1.0, self.K2)
        self.KCUT = N // 3
        self.DEALIAS = (np.abs(KX) <= self.KCUT) & (np.abs(KY) <= self.KCUT) & (np.abs(KZ) <= self.KCUT)
        self.RW = np.where((KZ > 0) & (KZ < N // 2), 2.0, 1.0)
        self.VOL = L ** 3
        self.dx = L / N
        self.dx3 = self.dx ** 3
        x = np.arange(N) * L / N
        self.X = np.meshgrid(x, x, x, indexing="ij")

    def rfft(self, u):
        return np.fft.rfftn(u) / self.N ** 3

    def irfft(self, uh):
        return np.fft.irfftn(uh * self.N ** 3, s=(self.N, self.N, self.N))

    def project(self, uh):
        div = self.K[0] * uh[0] + self.K[1] * uh[1] + self.K[2] * uh[2]
        return np.array([uh[i] - self.K[i] * div / self.K2s for i in range(3)])

    def curl_h(self, vh):
        K = self.K
        return [1j * (K[1] * vh[2] - K[2] * vh[1]), 1j * (K[2] * vh[0] - K[0] * vh[2]), 1j * (K[0] * vh[1] - K[1] * vh[0])]

    def rhs(self, uh, nu):
        u = [self.irfft(uh[i]) for i in range(3)]
        wh = self.curl_h(uh)
        w = [self.irfft(wh[i]) for i in range(3)]
        c = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
        ch = np.array([self.rfft(ci) * self.DEALIAS for ci in c])
        ch = self.project(ch)
        return np.array([ch[i] - nu * self.K2 * uh[i] for i in range(3)])

    def step(self, uh, nu, dt):
        k1 = self.rhs(uh, nu)
        k2 = self.rhs(uh + 0.5 * dt * k1, nu)
        k3 = self.rhs(uh + 0.5 * dt * k2, nu)
        k4 = self.rhs(uh + dt * k3, nu)
        uh = uh + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        uh = self.project(uh)
        return uh * self.DEALIAS

    def energy(self, uh):
        return self.VOL * float(np.sum(self.RW * sum(np.abs(uh[i]) ** 2 for i in range(3))))

    def tail(self, uh):
        spec = self.RW * sum(np.abs(uh[i]) ** 2 for i in range(3))
        m = np.sqrt(self.K2) >= 0.9 * self.KCUT
        return float(np.sum(spec[m]) / max(np.sum(spec), 1e-300))

    def biot_savart(self, wh):
        K = self.K
        cross = [K[1] * wh[2] - K[2] * wh[1], K[2] * wh[0] - K[0] * wh[2], K[0] * wh[1] - K[1] * wh[0]]
        return np.array([1j * cross[i] / self.K2s for i in range(3)])


# ------------------------------------------------------------------ initial data
def ic_taylor_green(g):
    X, Y, Z = g.X
    u = np.array([np.sin(X) * np.cos(Y) * np.cos(Z), -np.cos(X) * np.sin(Y) * np.cos(Z), np.zeros((g.N,) * 3)])
    return np.array([g.rfft(u[i]) for i in range(3)])


def ic_random_band(g, kmin, kmax, seed, anisotropy=False, amp=1.0):
    rng = np.random.default_rng(seed)
    uh = np.zeros((3, g.N, g.N, g.N // 2 + 1), dtype=complex)
    kmag = np.sqrt(g.K2)
    band = (kmag >= kmin) & (kmag <= kmax)
    for i in range(3):
        ph = rng.standard_normal(uh[i].shape) + 1j * rng.standard_normal(uh[i].shape)
        uh[i] = ph * band
    if anisotropy:
        uh *= (1.0 + 2.0 * (g.K[2] ** 2) / g.K2s)
    uh = g.project(uh)
    u = np.real(np.array([g.irfft(uh[i]) for i in range(3)]))
    urms = np.sqrt(np.mean(np.sum(u ** 2, axis=0)) / 3.0)
    u *= amp / urms
    return np.array([g.rfft(u[i]) for i in range(3)])


def ic_r4(g):
    """T-GRAM R4 datum (shear + band noise), reproduced for N = 64 conventions."""
    X, Y, Z = g.X
    rng = np.random.default_rng(3)
    a1 = np.array([0.0, 0.0, 1.0]); k1v = np.array([1.0, 0.0, 0.0])
    a2 = np.array([1.0, 0.0, 0.0]); k2v = np.array([0.0, 2.0, 1.0])
    u = np.zeros((3, g.N, g.N, g.N))
    ph1 = k1v[0] * X + k1v[1] * Y + k1v[2] * Z
    ph2 = k2v[0] * X + k2v[1] * Y + k2v[2] * Z
    for i in range(3):
        u[i] += a1[i] * np.sin(ph1) + 0.8 * a2[i] * np.sin(ph2)
    uhb = np.zeros((3, g.N, g.N, g.N // 2 + 1), dtype=complex)
    kmag = np.sqrt(g.K2)
    band = (kmag >= 1) & (kmag <= 4)
    for i in range(3):
        ph = rng.standard_normal(uhb[i].shape) + 1j * rng.standard_normal(uhb[i].shape)
        uhb[i] = ph * band
    uhb = g.project(uhb)
    ub = np.real(np.array([g.irfft(uhb[i]) for i in range(3)]))
    ub_rms = np.sqrt(np.mean(np.sum(ub ** 2, axis=0)) / 3.0)
    u += 0.1 * ub / ub_rms
    urms = np.sqrt(np.mean(np.sum(u ** 2, axis=0)) / 3.0)
    u *= (1.0 / urms)
    return np.array([g.rfft(u[i]) for i in range(3)])


def ic_antiparallel_tubes(g, a=0.4, y0=0.8, eps=0.2):
    X, Y, Z = g.X
    yc, zc = Y - np.pi, Z - np.pi
    y1 = y0 + eps * np.cos(X)
    wx = np.exp(-((yc - y1) ** 2 + zc ** 2) / a ** 2) - np.exp(-((yc + y1) ** 2 + zc ** 2) / a ** 2)
    wh = np.array([g.rfft(wx), np.zeros_like(g.K2, dtype=complex), np.zeros_like(g.K2, dtype=complex)])
    wh = g.project(wh)  # divergence-free vorticity
    uh = g.biot_savart(wh)
    uh = g.project(uh)
    u = np.real(np.array([g.irfft(uh[i]) for i in range(3)]))
    urms = np.sqrt(np.mean(np.sum(u ** 2, axis=0)) / 3.0)
    u *= (1.0 / urms)
    return np.array([g.rfft(u[i]) for i in range(3)])


RUNS = {
    "E0": dict(ic=lambda g: ic_taylor_green(g), nu=0.02, N=64, T=3.5, dt=0.0125),
    "E1": dict(ic=lambda g: ic_taylor_green(g), nu=0.01, N=64, T=8.0, dt=0.01),
    "E2": dict(ic=lambda g: ic_antiparallel_tubes(g), nu=0.01, N=64, T=6.0, dt=0.01),
    "E2b": dict(ic=lambda g: ic_antiparallel_tubes(g), nu=0.01, N=96, T=6.0, dt=0.0075),
    "E3": dict(ic=lambda g: ic_r4(g), nu=0.02, N=64, T=3.5, dt=0.0125),
    "E4": dict(ic=lambda g: ic_random_band(g, 1, 2, 11), nu=0.02, N=64, T=6.0, dt=0.0125),
}


# ------------------------------------------------------------------ diagnostics
def periodic_dist2(g, idx):
    d2 = np.zeros((g.N,) * 3)
    for ax in range(3):
        c = g.X[ax] - g.X[ax].flat[0] * 0 - (idx[ax] * g.dx)
        c = (c + g.L / 2) % g.L - g.L / 2
        d2 += c ** 2
    return d2


def sample_line_fraction(field_bool, g, x0, d, rho, nsamp=41):
    """fraction of the segment x0 + s d, s in [-rho, rho], inside the set (nearest-grid sampling)."""
    s = np.linspace(-rho, rho, nsamp)
    pts = x0[None, :] + s[:, None] * d[None, :]
    idx = np.mod(np.rint(pts / g.dx).astype(int), g.N)
    return float(np.mean(field_bool[idx[:, 0], idx[:, 1], idx[:, 2]]))


def run_length(field_bool, g, x0, d, maxlen, ds):
    """in-set run length through x0 along +-d (nearest-grid sampling), capped at 2*maxlen."""
    total = 0.0
    for sgn in (1.0, -1.0):
        s = 0.0
        while s < maxlen:
            p = x0 + sgn * s * d
            idx = np.mod(np.rint(p / g.dx).astype(int), g.N)
            if not field_bool[idx[0], idx[1], idx[2]]:
                break
            s += ds
        total += s
    return total


def full_diag(g, uh, nu):
    N = g.N
    K, K2 = g.K, g.K2
    u = [g.irfft(uh[i]) for i in range(3)]
    du = [[g.irfft(1j * K[i] * uh[c]) for c in range(3)] for i in range(3)]  # du[i][c] = d_i u_c
    w = np.array([du[1][2] - du[2][1], du[2][0] - du[0][2], du[0][1] - du[1][0]])
    S = np.empty((N, N, N, 3, 3))
    for i in range(3):
        for j in range(3):
            S[..., i, j] = 0.5 * (du[i][j] + du[j][i])
    w2 = np.sum(w ** 2, axis=0)
    Sfro2 = np.sum(S ** 2, axis=(-2, -1))
    lam, ev = np.linalg.eigh(S)  # ascending eigenvalues, ev[..., :, i] = e_i
    wi = np.einsum('abcj,abcji->abci', w.transpose(1, 2, 3, 0), ev)  # omega . e_i
    dx3 = g.dx3
    E = dx3 * float(np.sum(w2))
    # gradients of omega
    wh = [g.rfft(w[c]) for c in range(3)]
    dw = [[g.irfft(1j * K[i] * wh[c]) for c in range(3)] for i in range(3)]
    gradw2 = sum(dw[i][c] ** 2 for i in range(3) for c in range(3))
    absw = np.sqrt(w2)
    gabs2 = sum((sum(w[c] * dw[i][c] for c in range(3))) ** 2 for i in range(3)) / np.maximum(w2, 1e-300)
    twist = np.maximum(gradw2 - gabs2, 0.0)  # = |omega|^2 |grad xi|^2
    # pressure and Hessian
    uu_h = [[g.rfft(u[a] * u[b]) * g.DEALIAS for b in range(3)] for a in range(3)]
    ph = -sum(K[a] * K[b] * uu_h[a][b] for a in range(3) for b in range(3)) / g.K2s
    H = np.empty((N, N, N, 3, 3))
    for a in range(3):
        for b in range(a, 3):
            H[..., a, b] = H[..., b, a] = g.irfft(-K[a] * K[b] * ph)
    lapS = np.empty((N, N, N, 3, 3))
    for a in range(3):
        for b in range(a, 3):
            lapS[..., a, b] = lapS[..., b, a] = g.irfft(-K2 * g.rfft(S[..., a, b]))
    e2 = ev[..., :, 1]
    p22 = np.einsum('abci,abcij,abcj->abc', e2, H, e2)
    lapS22 = np.einsum('abci,abcij,abcj->abc', e2, lapS, e2)
    trH = H[..., 0, 0] + H[..., 1, 1] + H[..., 2, 2]
    lap_p_exact = 0.5 * w2 - Sfro2
    # validations
    val = {}
    val['trH_vs_lap'] = float(np.sqrt(np.sum((trH - lap_p_exact) ** 2) / max(np.sum(lap_p_exact ** 2), 1e-300)))
    val['S_H'] = float(dx3 * np.sum(S * H) / max(dx3 * np.sum(np.sqrt(Sfro2) * np.sqrt(np.sum(H ** 2, axis=(-2, -1)))), 1e-300))
    P_i = [dx3 * float(np.sum(lam[..., i] * wi[..., i] ** 2)) for i in range(3)]
    P = sum(P_i)
    P_det = -4.0 * dx3 * float(np.sum(lam[..., 0] * lam[..., 1] * lam[..., 2]))
    P_direct = dx3 * float(np.sum(np.einsum('abci,abcij,abcj->abc', w.transpose(1, 2, 3, 0), S, w.transpose(1, 2, 3, 0))))
    val['P_frame_vs_det'] = abs(P - P_det) / max(abs(P_direct), 1e-300)
    val['P_frame_vs_direct'] = abs(P - P_direct) / max(abs(P_direct), 1e-300)
    val['E_vs_2S2'] = abs(E - 2 * dx3 * float(np.sum(Sfro2))) / max(E, 1e-300)
    out = dict(E=E, P=P, P_i=P_i, P_abs=dx3 * float(np.sum(np.abs(lam) * wi ** 2)),
               G=dx3 * float(np.sum(np.sqrt(Sfro2) * w2)), diss=nu * dx3 * float(np.sum(gradw2)),
               diss_abs=nu * dx3 * float(np.sum(gabs2)), diss_twist=nu * dx3 * float(np.sum(twist)),
               cos2=[float(np.sum(wi[..., i] ** 2) / max(np.sum(w2), 1e-300)) for i in range(3)],
               lam2_terms=dict(self=dx3 * float(np.sum(-lam[..., 1] ** 2)),
                               vort=dx3 * float(np.sum(0.25 * (w2 - wi[..., 1] ** 2))),
                               press=dx3 * float(np.sum(-p22)), visc=nu * dx3 * float(np.sum(lapS22))),
               validation=val, sets={})
    Lam = float(absw.max())
    for lamfrac in (0.5, 0.25):
        m = absw > lamfrac * Lam
        mp = m & (lam[..., 1] > 0)
        out['sets'][str(lamfrac)] = dict(
            volfrac=float(np.mean(m)), Efrac=float(np.sum(w2[m]) / max(np.sum(w2), 1e-300)),
            P=dx3 * float(np.sum(np.einsum('abci,abcij,abcj->abc', w.transpose(1, 2, 3, 0), S, w.transpose(1, 2, 3, 0))[m])),
            P_abs=dx3 * float(np.sum((np.abs(lam) * wi ** 2)[m])), G=dx3 * float(np.sum((np.sqrt(Sfro2) * w2)[m])),
            diss=nu * dx3 * float(np.sum(gradw2[m])), diss_twist=nu * dx3 * float(np.sum(twist[m])),
            cos2=[float(np.sum((wi[..., i] ** 2)[m]) / max(np.sum(w2[m]), 1e-300)) for i in range(3)],
            lam2pos_frac=float(np.sum(Sfro2[mp]) / max(np.sum(Sfro2[m]), 1e-300)),
            lam2_terms=dict(self=dx3 * float(np.sum((-lam[..., 1] ** 2)[mp])),
                            vort=dx3 * float(np.sum((0.25 * (w2 - wi[..., 1] ** 2))[mp])),
                            press=dx3 * float(np.sum((-p22)[mp])), visc=nu * dx3 * float(np.sum(lapS22[mp]))))
    # maximum point
    idx = np.unravel_index(int(np.argmax(absw)), absw.shape)
    xi = w[:, idx[0], idx[1], idx[2]] / Lam
    Sm = S[idx]
    alpha = float(xi @ Sm @ xi)
    lap_absw = g.irfft(-K2 * g.rfft(absw))
    mx = dict(Lam=Lam, alpha=alpha, absS=float(np.sqrt(Sfro2[idx])), lam=[float(v) for v in lam[idx]],
              cos2=[float((wi[idx][i] / Lam) ** 2) for i in range(3)], nu_twist=nu * float(twist[idx]) / Lam ** 2,
              nu_lap=nu * float(lap_absw[idx]) / Lam, p22=float(p22[idx]), near={}, fatcore={})
    x0 = np.array([idx[0] * g.dx, idx[1] * g.dx, idx[2] * g.dx])
    d2 = periodic_dist2(g, idx)
    for c in (0.5, 1.0, 2.0):
        r = c * np.sqrt(nu / Lam)
        mask = d2 <= r ** 2
        whn = [g.rfft(w[cc] * mask) for cc in range(3)]
        uhn = g.project(g.biot_savart(whn))
        dun = [[g.irfft(1j * K[i] * uhn[cc])[idx] for cc in range(3)] for i in range(3)]
        Sn = np.array([[0.5 * (dun[i][j] + dun[j][i]) for j in range(3)] for i in range(3)])
        an = float(xi @ Sn @ xi)
        mx['near'][str(c)] = dict(r=r, alpha_near=an, alpha_far=alpha - an, absS_near=float(np.sqrt(np.sum(Sn ** 2))),
                                  absS_far=float(np.sqrt(np.sum((Sm - Sn) ** 2))), ncells=int(mask.sum()))
    setb = absw > 0.4 * Lam
    dirs = {'ex': np.array([1., 0, 0]), 'ey': np.array([0, 1., 0]), 'ez': np.array([0, 0, 1.]),
            'e1': ev[idx][:, 0], 'e2': ev[idx][:, 1], 'e3': ev[idx][:, 2], 'xi': xi}
    scale = np.sqrt(nu / Lam)
    for c in (0.5, 1.0, 2.0, 4.0):
        mx['fatcore'][str(c)] = {k: sample_line_fraction(setb, g, x0, d, c * scale) for k, d in dirs.items()}
    mx['minrun_over_scale'] = float(min(run_length(setb, g, x0, d, 4 * g.L, g.dx / 2) for d in dirs.values()) / scale)
    out['max'] = mx
    return out


def run(name, obs_every_full=None):
    cfg = RUNS[name]
    g = Grid(cfg['N'])
    nu, T, dt = cfg['nu'], cfg['T'], cfg['dt']
    t0 = time.time()
    uh = g.project(cfg['ic'](g)) * g.DEALIAS
    nsteps = int(round(T / dt))
    if obs_every_full is None:
        obs_every_full = max(1, int(round(0.1 / dt)))
    obs_every_cheap = max(1, int(round(0.025 / dt)))
    out = dict(name=name, nu=nu, N=cfg['N'], T=T, dt=dt, t_cheap=[], energy=[], enstrophy=[], tail=[], t_full=[], full=[])
    for step in range(nsteps + 1):
        t = step * dt
        if step % obs_every_cheap == 0:
            wh = g.curl_h(uh)
            ens = g.VOL * float(np.sum(g.RW * sum(np.abs(wh[i]) ** 2 for i in range(3))))
            out['t_cheap'].append(t); out['energy'].append(g.energy(uh)); out['enstrophy'].append(ens); out['tail'].append(g.tail(uh))
        if step % obs_every_full == 0:
            d = full_diag(g, uh, nu)
            out['t_full'].append(t); out['full'].append(d)
            print(f"{name} t={t:.3f} E={d['E']:.3f} P={d['P']:.3f} diss={d['diss']:.3f} Lam={d['max']['Lam']:.3f} "
                  f"alpha={d['max']['alpha']:.3f} tail={out['tail'][-1]:.1e} val={ {k: f'{v:.1e}' for k, v in d['validation'].items()} }", flush=True)
        if step == nsteps:
            break
        uh = g.step(uh, nu, dt)
    out['walltime_s'] = time.time() - t0
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', f'{name}.json'), 'w') as f:
        json.dump(out, f)
    print(f"{name}: done in {out['walltime_s']:.1f}s; max tail {max(out['tail']):.2e}; E range {min(out['enstrophy']):.2f}-{max(out['enstrophy']):.2f}", flush=True)
    return out


if __name__ == "__main__":
    for name in sys.argv[1:]:
        run(name)
