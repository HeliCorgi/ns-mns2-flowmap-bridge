"""Post-processing for the T-GRAM probe (preregistered estimators/thresholds: PREREG.md)."""
import json
import numpy as np

RUNS = ["R1", "R2", "R3", "R4", "R5"]

def sym(v):
    a, b, c, d, e, f = v
    return np.array([[a, d, e], [d, b, f], [e, f, c]])

def fib_half_sphere(n):
    ga = np.pi * (3 - np.sqrt(5))
    pts = []
    for i in range(2 * n):
        z = 1 - (2 * i + 1) / (2 * n)
        r = np.sqrt(max(0.0, 1 - z * z))
        th = ga * i
        p = np.array([r * np.cos(th), r * np.sin(th), z])
        if p[2] < 0:
            p = -p
        pts.append(p)
    return np.unique(np.round(np.array(pts), 12), axis=0)

def budget_series(Pmats, ts, dirs):
    # q[d,t] = dirs^T P(t) dirs ; budget = trapz over t of max(-q,0)
    q = np.einsum("di,tij,dj->dt", dirs, Pmats, dirs)
    neg = np.maximum(-q, 0.0)
    return np.trapz(neg, ts, axis=1)

def refine_min(Pmats, ts, dirs, budgets, rng):
    order = np.argsort(budgets)
    best = budgets[order[0]]
    bestdir = dirs[order[0]]
    for idx in order[:10]:
        base = dirs[idx]
        perturb = rng.standard_normal((60, 3)) * 0.05
        cand = base[None, :] + perturb
        cand /= np.linalg.norm(cand, axis=1)[:, None]
        b = budget_series(Pmats, ts, cand)
        j = int(np.argmin(b))
        if b[j] < best:
            best = b[j]; bestdir = cand[j]
    return best, bestdir

def analyze(name):
    with open(f"results/{name}.json") as f:
        d = json.load(f)
    ts = np.array(d["t"]); E = np.array(d["energy"])
    G = np.array([sym(v) for v in d["G"]])
    D = np.array([sym(v) for v in d["D"]])
    P = np.array([sym(v) for v in d["P"]])
    tail = np.array(d["tail"]); nu = d["nu"]
    res = {"name": name, "nu": nu, "walltime_s": d["walltime_s"]}
    # V1 energy balance
    dEdt = np.gradient(0.5 * E, ts)
    trG = np.trace(G, axis1=1, axis2=2)
    v1 = np.abs(dEdt + nu * trG)[2:-2] / max(np.max(nu * trG), 1e-300)
    res["V1_median"] = float(np.median(v1))
    # V2 matrix identity
    dG = np.gradient(G, ts, axis=0)
    resid = dG + 2 * nu * D + 2 * P
    den = np.linalg.norm(2 * nu * D, axis=(1, 2)) + np.linalg.norm(2 * P, axis=(1, 2)) + 1e-12
    v2 = (np.linalg.norm(resid, axis=(1, 2)) / den)[2:-2]
    res["V2_median"] = float(np.median(v2))
    # V3 tail
    res["V3_maxtail"] = float(np.max(tail))
    res["pass"] = bool(res["V1_median"] <= 0.05 and res["V2_median"] <= 0.10 and res["V3_maxtail"] <= 1e-5)
    # estimators on T' grid (observation times, skip t=0)
    rng = np.random.default_rng(12345)
    dirs = fib_half_sphere(2000)
    delta = 1e-6 * (1 + trG[0])
    rows = []
    idxs = [i for i in range(4, len(ts))]  # need a few points for integrals
    for i in idxs:
        tsub = ts[: i + 1]; Gsub = G[: i + 1]; Psub = P[: i + 1]
        A = np.trapz(Gsub, tsub, axis=0)
        lam, vec = np.linalg.eigh(A)
        # degeneracy rule
        thr = 0.02 * (np.trace(A) / 3.0)
        if lam[1] - lam[0] < thr and lam[2] - lam[1] < thr:
            emin_dirs = dirs  # full sphere
        elif lam[1] - lam[0] < thr:
            angs = np.linspace(0, np.pi, 360, endpoint=False)
            emin_dirs = np.outer(np.cos(angs), vec[:, 0]) + np.outer(np.sin(angs), vec[:, 1])
        else:
            emin_dirs = vec[:, 0][None, :]
        bB = float(np.min(budget_series(Psub, tsub, emin_dirs)))
        ball_grid = budget_series(Psub, tsub, dirs)
        bAll, _ = refine_min(Psub, tsub, dirs, ball_grid, rng)
        rows.append({
            "T": float(ts[i]), "lam_min_A": float(lam[0]), "trA3": float(np.trace(A) / 3),
            "gap_rel": float((lam[1] - lam[0]) / max(np.trace(A) / 3, 1e-300)),
            "B": bB, "B_all": float(bAll), "R": float((bB + delta) / (bAll + delta)),
        })
    res["rows"] = rows
    # verdict per run (T' >= T/4)
    Tq = ts[-1] / 4
    Rs = [r["R"] for r in rows if r["T"] >= Tq]
    res["maxR"] = float(np.max(Rs)); res["R_end"] = float(rows[-1]["R"])
    lasthalf = [r["R"] for r in rows if r["T"] >= ts[-1] / 2]
    mono = all(lasthalf[k + 1] >= lasthalf[k] * 0.95 for k in range(len(lasthalf) - 1))
    if res["maxR"] >= 10 or (res["R_end"] >= 5 and mono):
        res["run_verdict"] = "ADVERSE"
    elif res["maxR"] <= 3:
        res["run_verdict"] = "STABLE"
    else:
        res["run_verdict"] = "UNDETERMINED"
    return res

def main():
    out = []
    for name in RUNS:
        r = analyze(name)
        out.append(r)
        print(f"{name}: pass={r['pass']} V1={r['V1_median']:.4f} V2={r['V2_median']:.4f} tail={r['V3_maxtail']:.2e} "
              f"maxR={r['maxR']:.3f} R_end={r['R_end']:.3f} verdict={r['run_verdict']}")
    resolved = [r for r in out if r["pass"]]
    if any(r["run_verdict"] == "ADVERSE" for r in resolved):
        g = "CANONICAL-ADVERSE"
    elif len(resolved) >= 3 and all(r["run_verdict"] == "STABLE" for r in resolved):
        g = "CANONICAL-STABLE"
    else:
        g = "UNDETERMINED"
    print("GLOBAL VERDICT:", g, f"({len(resolved)}/{len(out)} runs resolved)")
    with open("results/summary.json", "w") as f:
        json.dump({"runs": out, "global_verdict": g}, f, indent=1)

if __name__ == "__main__":
    main()
