"""HR-2 middle-eigenvalue strain-energy fraction diagnostic (twenty-sixth session).

DIAGNOSTIC / EVIDENCE-GRADE ONLY. Periodic box 64^3 (certificate-inadmissible by the
standing rule); no verdict consequence beyond informing the sub-wall margin of HR-2.
Reuses the T-GRAM probe solver unchanged (experiments/tgram_probe/tgram_probe.py:
rotational form, Leray projection, 2/3 dealias, RK4, numpy only). R2-R4 were tail-excluded
in the T-GRAM probe (spectral tail 3.6-4.8e-5 > 1e-5); here they are diagnostic only.

Per output time:
  S2    = ||S||_2^2            (enstrophy E = ||omega||_2^2 = 2 S2 for divergence-free periodic fields)
  X     = ||lambda_2^+||_2^2   (the HR-2 channel; the (4,2) head is int X^2 dt <= Q0)
  r     = X / S2               (sub-wall margin; r <= 1/6 pointwise-derived bound)
  prod  = -4 int det S         (= int omega^T S omega, the enstrophy production)
  bound = 2 int lambda_2^+ |S|^2   (Miller's pointwise bound; prod <= bound)
  fpos  = volume fraction with lambda_2 > 0;  wpos = |S|^2-weighted fraction with lambda_2 > 0
  supl2p, supS = sup lambda_2^+, sup |S|
Validation at two times: prod vs -tr(P) from the T-GRAM observables (tr P = -int omega^T S omega)
and 2 S2 vs tr G (= ||grad u||_2^2).
"""
import sys, os, json, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'tgram_probe'))
import tgram_probe as tp  # noqa: E402


def strain_obs(uh):
    du = [[np.real(tp.irfft(1j * tp.K[i] * uh[c])) for c in range(3)] for i in range(3)]
    S = np.empty((tp.N, tp.N, tp.N, 3, 3))
    for i in range(3):
        for j in range(3):
            S[..., i, j] = 0.5 * (du[i][j] + du[j][i])
    lam = np.linalg.eigvalsh(S)  # ascending: l1 <= l2 <= l3
    l1, l2, l3 = lam[..., 0], lam[..., 1], lam[..., 2]
    S2 = (lam ** 2).sum(-1)
    dx3 = (tp.L / tp.N) ** 3
    l2p = np.maximum(l2, 0.0)
    X = dx3 * float(np.sum(l2p ** 2))
    normS2 = dx3 * float(np.sum(S2))
    det = l1 * l2 * l3
    prod = -4.0 * dx3 * float(np.sum(det))
    bound = 2.0 * dx3 * float(np.sum(l2p * S2))
    fpos = float(np.mean(l2 > 0))
    wpos = float(np.sum(S2 * (l2 > 0)) / max(np.sum(S2), 1e-300))
    return dict(X=X, S2=normS2, E=2.0 * normS2, r=X / max(normS2, 1e-300), prod=prod, bound=bound,
                fpos=fpos, wpos=wpos, supl2p=float(l2p.max()), supS=float(np.sqrt(S2.max())))


def run(name, obs_every=4):
    t0 = time.time()
    uh, nu = tp.make_ic(name)
    uh = tp.project(uh)
    for i in range(3):
        uh[i] *= tp.DEALIAS
    nsteps = int(round(tp.T_END / tp.DT))
    out = {"name": name, "nu": nu, "N": tp.N, "dt": tp.DT, "T": tp.T_END, "obs_every": obs_every,
           "t": [], "obs": [], "validation": []}
    for step in range(nsteps + 1):
        t = step * tp.DT
        if step % obs_every == 0:
            o = strain_obs(uh)
            out["t"].append(t)
            out["obs"].append(o)
            if step in (0, (nsteps // 2 // obs_every) * obs_every):
                e, G, D, P, tail = tp.observables(uh, nu)
                out["validation"].append({"t": t, "prod_det": o["prod"], "minus_trP": -float(np.trace(P)),
                                          "twoS2": o["E"], "trG": float(np.trace(G)), "tail": tail})
        if step == nsteps:
            break
        k1_ = tp.rhs(uh, nu)
        k2_ = tp.rhs(uh + 0.5 * tp.DT * k1_, nu)
        k3_ = tp.rhs(uh + 0.5 * tp.DT * k2_, nu)
        k4_ = tp.rhs(uh + tp.DT * k3_, nu)
        uh = uh + (tp.DT / 6.0) * (k1_ + 2 * k2_ + 2 * k3_ + k4_)
        uh = tp.project(uh)
        for i in range(3):
            uh[i] *= tp.DEALIAS
    out["walltime_s"] = time.time() - t0
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', f'{name}.json'), 'w') as f:
        json.dump(out, f)
    rs = [o['r'] for o in out['obs']]
    Es = [o['E'] for o in out['obs']]
    print(f"{name}: done in {out['walltime_s']:.1f}s; r min/max {min(rs):.4f}/{max(rs):.4f}; "
          f"E(0)={Es[0]:.3f} Emax={max(Es):.3f} at t={out['t'][int(np.argmax(Es))]:.2f}; "
          f"validation={out['validation']}", flush=True)


if __name__ == "__main__":
    for name in sys.argv[1:]:
        run(name)
