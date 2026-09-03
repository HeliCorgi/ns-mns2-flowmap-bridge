"""T-GRAM specialization stress-test probe (preregistered: PREREG.md).

Pseudo-spectral incompressible NS on [0,2pi)^3, rotational form, RK4, 2/3 dealias.
Observables: energy, Gram G_ij, dissipation tensor D_ij, production tensor P_ij, tail.
EVIDENCE-GRADE ONLY (torus; certificate-inadmissible by standing rule).
"""
import json, sys, time
import numpy as np

N = 64
L = 2 * np.pi
DT = 0.0125
T_END = 3.5
OBS_EVERY = 2  # steps

k1 = np.fft.fftfreq(N, d=1.0 / N)  # integer wavenumbers
KX = k1[:, None, None]
KY = k1[None, :, None]
KZ_full = k1[None, None, :]
kz_r = k1[: N // 2 + 1]
KZ = kz_r[None, None, :]
KXr = np.broadcast_to(KX, (N, N, N // 2 + 1))
KYr = np.broadcast_to(KY, (N, N, N // 2 + 1))
KZr = np.broadcast_to(KZ, (N, N, N // 2 + 1))
K = [KXr, KYr, KZr]
K2 = KXr**2 + KYr**2 + KZr**2
K2_safe = np.where(K2 == 0, 1.0, K2)
KCUT = N // 3
DEALIAS = (np.abs(KXr) <= KCUT) & (np.abs(KYr) <= KCUT) & (np.abs(KZr) <= KCUT)
VOL = L**3
# Parseval factor for rfftn: sum over full spectrum = sum over rfft grid with kz>0 doubled
RW = np.where((KZr > 0) & (KZr < N // 2), 2.0, 1.0)  # kz = N/2 plane appears once

def rfft(u):
    return np.fft.rfftn(u) / N**3  # coefficient convention: u = sum uh e^{ikx}

def irfft(uh):
    return np.fft.irfftn(uh * N**3, s=(N, N, N))

def project(uh):
    div = K[0] * uh[0] + K[1] * uh[1] + K[2] * uh[2]
    for i in range(3):
        uh[i] = uh[i] - K[i] * div / K2_safe
    return uh

def rhs(uh, nu):
    u = [irfft(uh[i]) for i in range(3)]
    wh = [
        1j * (K[1] * uh[2] - K[2] * uh[1]),
        1j * (K[2] * uh[0] - K[0] * uh[2]),
        1j * (K[0] * uh[1] - K[1] * uh[0]),
    ]
    w = [irfft(wh[i]) for i in range(3)]
    c = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
    ch = np.array([rfft(ci) * DEALIAS for ci in c])
    ch = project(ch)
    return np.array([ch[i] - nu * K2 * uh[i] for i in range(3)])

def observables(uh, nu):
    spec = RW * sum(np.abs(uh[i]) ** 2 for i in range(3))
    energy = VOL * float(np.sum(spec))
    tail_mask = np.sqrt(K2) >= 0.9 * KCUT
    tail = float(np.sum(spec[tail_mask]) / max(np.sum(spec), 1e-300))
    G = np.zeros((3, 3))
    D = np.zeros((3, 3))
    for i in range(3):
        for j in range(i, 3):
            gij = VOL * float(np.sum(RW * (K[i] * K[j]) * sum(np.abs(uh[c]) ** 2 for c in range(3))))
            dij = VOL * float(np.sum(RW * (K[i] * K[j]) * K2 * sum(np.abs(uh[c]) ** 2 for c in range(3))))
            G[i, j] = G[j, i] = gij
            D[i, j] = D[j, i] = dij
    # gradients in physical space: du[i][c] = d_i u_c
    du = [[irfft(1j * K[i] * uh[c]) for c in range(3)] for i in range(3)]
    S = [[0.5 * (du[i][j] + du[j][i]) for j in range(3)] for i in range(3)]
    P = np.zeros((3, 3))
    dx3 = (L / N) ** 3
    for i in range(3):
        for j in range(i, 3):
            acc = np.zeros((N, N, N))
            for kk in range(3):
                for ll in range(3):
                    acc += du[i][kk] * S[kk][ll] * du[j][ll]
            pij = dx3 * float(np.sum(acc))
            P[i, j] = P[j, i] = pij
    return energy, G, D, P, tail

def sym6(M):
    return [M[0, 0], M[1, 1], M[2, 2], M[0, 1], M[0, 2], M[1, 2]]

def make_ic(name, seed=None):
    x = np.arange(N) * L / N
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    if name == "R1":
        u = np.array([np.sin(X) * np.cos(Y) * np.cos(Z), -np.cos(X) * np.sin(Y) * np.cos(Z), np.zeros((N, N, N))])
        return np.array([rfft(u[i]) for i in range(3)]), 0.02
    if name in ("R2", "R3", "R5"):
        rng = np.random.default_rng(1 if name in ("R2", "R5") else 2)
        uh = np.zeros((3, N, N, N // 2 + 1), dtype=complex)
        kmag = np.sqrt(K2)
        band = (kmag >= 1) & (kmag <= 4)
        for i in range(3):
            ph = rng.standard_normal((N, N, N // 2 + 1)) + 1j * rng.standard_normal((N, N, N // 2 + 1))
            uh[i] = ph * band
        if name in ("R2", "R5"):
            uh *= (1.0 + 2.0 * (KZr**2) / K2_safe)  # x3-weighted anisotropy
        uh = project(uh)
        u = np.array([irfft(uh[i]) for i in range(3)])
        u = np.real(u)
        urms = np.sqrt(np.mean(np.sum(u**2, axis=0)) / 3.0)
        u *= (1.0 / urms)
        if name == "R5":
            u *= 0.05
        return np.array([rfft(u[i]) for i in range(3)]), 0.035
    if name == "R4":
        rng = np.random.default_rng(3)
        a1 = np.array([0.0, 0.0, 1.0]); k1v = np.array([1.0, 0.0, 0.0])
        a2 = np.array([1.0, 0.0, 0.0]); k2v = np.array([0.0, 2.0, 1.0])
        u = np.zeros((3, N, N, N))
        ph1 = k1v[0] * X + k1v[1] * Y + k1v[2] * Z
        ph2 = k2v[0] * X + k2v[1] * Y + k2v[2] * Z
        for i in range(3):
            u[i] += a1[i] * np.sin(ph1) + 0.8 * a2[i] * np.sin(ph2)
        uhb = np.zeros((3, N, N, N // 2 + 1), dtype=complex)
        kmag = np.sqrt(K2)
        band = (kmag >= 1) & (kmag <= 4)
        for i in range(3):
            ph = rng.standard_normal((N, N, N // 2 + 1)) + 1j * rng.standard_normal((N, N, N // 2 + 1))
            uhb[i] = ph * band
        uhb = project(uhb)
        ub = np.real(np.array([irfft(uhb[i]) for i in range(3)]))
        ub_rms = np.sqrt(np.mean(np.sum(ub**2, axis=0)) / 3.0)
        u += 0.1 * ub / ub_rms
        urms = np.sqrt(np.mean(np.sum(u**2, axis=0)) / 3.0)
        u *= (1.0 / urms)
        return np.array([rfft(u[i]) for i in range(3)]), 0.02
    raise ValueError(name)

def run(name):
    t0 = time.time()
    uh, nu = make_ic(name)
    uh = project(uh)
    for i in range(3):
        uh[i] *= DEALIAS
    nsteps = int(round(T_END / DT))
    out = {"name": name, "nu": nu, "N": N, "dt": DT, "T": T_END, "t": [], "energy": [], "G": [], "D": [], "P": [], "tail": []}
    for step in range(nsteps + 1):
        t = step * DT
        if step % OBS_EVERY == 0:
            e, G, D, P, tail = observables(uh, nu)
            out["t"].append(t); out["energy"].append(e)
            out["G"].append(sym6(G)); out["D"].append(sym6(D)); out["P"].append(sym6(P))
            out["tail"].append(tail)
        if step == nsteps:
            break
        k1_ = rhs(uh, nu)
        k2_ = rhs(uh + 0.5 * DT * k1_, nu)
        k3_ = rhs(uh + 0.5 * DT * k2_, nu)
        k4_ = rhs(uh + DT * k3_, nu)
        uh = uh + (DT / 6.0) * (k1_ + 2 * k2_ + 2 * k3_ + k4_)
        uh = project(uh)
        for i in range(3):
            uh[i] *= DEALIAS
    out["walltime_s"] = time.time() - t0
    with open(f"results/{name}.json", "w") as f:
        json.dump(out, f)
    print(f"{name}: done in {out['walltime_s']:.1f}s, E(0)={out['energy'][0]:.4f}, E(T)={out['energy'][-1]:.4f}, max tail={max(out['tail']):.2e}", flush=True)

if __name__ == "__main__":
    for name in sys.argv[1:]:
        run(name)
