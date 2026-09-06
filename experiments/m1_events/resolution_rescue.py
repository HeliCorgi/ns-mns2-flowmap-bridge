"""Cheap fail-closed resolution screening for the M-1 event family.

This stage deliberately does NOT run the expensive filtered near/far diagnostics. It first asks
whether a fixed continuum datum is spectrally resolved over the whole requested time interval.
Only a run with max tail <= 1e-5 is eligible for the later near/far mechanism comparison.

Usage:
    python experiments/m1_events/resolution_rescue.py E1R96 E3c96

Outputs JSON under experiments/m1_events/results_resolution_rescue/.
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

import events as ev
import resolution_invariant_ic as ric

HERE = os.path.dirname(os.path.abspath(__file__))
TAIL_TOL = 1.0e-5
OUT_EVERY = 0.1


def _cfg(ic, nu: float, N: int, T: float, dt: float) -> dict:
    return dict(ic=ic, nu=nu, N=N, T=T, dt=dt)


CONFIGS = {
    # Taylor--Green: same analytic continuum datum at every N.
    "E1R96": _cfg(lambda g: ev.ic_taylor_green(g), 0.01, 96, 8.0, 1.0 / 150.0),
    "E1R128": _cfg(lambda g: ev.ic_taylor_green(g), 0.01, 128, 8.0, 1.0 / 200.0),
    # Antiparallel tube formula: continue the failed N=64/96 rescue ladder.
    "E2R128": _cfg(lambda g: ev.ic_antiparallel_tubes(g), 0.01, 128, 6.0, 1.0 / 200.0),
    "E2R160": _cfg(lambda g: ev.ic_antiparallel_tubes(g), 0.01, 160, 6.0, 1.0 / 250.0),
    "E2R192": _cfg(lambda g: ev.ic_antiparallel_tubes(g), 0.01, 192, 6.0, 1.0 / 300.0),
    # New continuum-seeded versions of E3/E4. Do not compare old E3/E4 across N as if the
    # random FFT-array initialization represented one fixed datum.
    "E3c64": _cfg(ric.ic_r4_continuum, 0.02, 64, 3.5, 1.0 / 80.0),
    "E3c96": _cfg(ric.ic_r4_continuum, 0.02, 96, 3.5, 1.0 / 120.0),
    "E3c128": _cfg(ric.ic_r4_continuum, 0.02, 128, 3.5, 1.0 / 160.0),
    "E4c64": _cfg(ric.ic_e4_continuum, 0.02, 64, 6.0, 1.0 / 80.0),
    "E4c96": _cfg(ric.ic_e4_continuum, 0.02, 96, 6.0, 1.0 / 120.0),
    "E4c128": _cfg(ric.ic_e4_continuum, 0.02, 128, 6.0, 1.0 / 160.0),
}


def enstrophy_fourier(g: ev.Grid, uh: np.ndarray) -> float:
    wh = g.curl_h(uh)
    density = sum(np.abs(wh[i]) ** 2 for i in range(3))
    return g.VOL * float(np.sum(g.RW * density))


def max_vorticity(g: ev.Grid, uh: np.ndarray) -> float:
    wh = g.curl_h(uh)
    w = np.array([g.irfft(wh[i]) for i in range(3)])
    return float(np.max(np.sqrt(np.sum(w * w, axis=0))))


def run(name: str) -> dict:
    cfg = CONFIGS[name]
    g = ev.Grid(cfg["N"])
    nu, T, dt = cfg["nu"], cfg["T"], cfg["dt"]
    uh = g.project(cfg["ic"](g)) * g.DEALIAS
    nsteps = int(round(T / dt))
    if abs(nsteps * dt - T) > 1.0e-12:
        raise ValueError(f"{name}: T/dt is not integral")
    every = max(1, int(round(OUT_EVERY / dt)))

    e0 = g.energy(uh)
    prev_e = e0
    max_energy_step_growth = 0.0
    max_tail = 0.0
    finite = True
    rows = []
    t0 = time.time()

    for step in range(nsteps + 1):
        t = step * dt
        tail = g.tail(uh)
        energy = g.energy(uh)
        max_tail = max(max_tail, tail)
        max_energy_step_growth = max(max_energy_step_growth, (energy - prev_e) / max(e0, 1.0e-300))
        prev_e = energy
        finite = finite and bool(np.all(np.isfinite(uh))) and np.isfinite(tail) and np.isfinite(energy)

        if step % every == 0 or step == nsteps:
            u = [g.irfft(uh[i]) for i in range(3)]
            umax = float(np.max(np.sqrt(sum(ui * ui for ui in u))))
            rows.append(dict(t=t, tail=tail, energy=energy, enstrophy=enstrophy_fourier(g, uh),
                             max_vorticity=max_vorticity(g, uh), advective_cfl=dt * umax / g.dx))
        if step == nsteps:
            break
        uh = g.step(uh, nu, dt)

    result = dict(name=name, N=g.N, nu=nu, T=T, dt=dt, nsteps=nsteps,
                  tail_tolerance=TAIL_TOL, max_tail=max_tail, tail_pass=bool(max_tail <= TAIL_TOL),
                  finite_pass=bool(finite), initial_energy=e0,
                  max_relative_single_step_energy_growth=max_energy_step_growth,
                  output_cadence=OUT_EVERY, rows=rows, walltime_s=time.time() - t0,
                  claim="periodic T^3 evidence-grade resolution screen only; not an R^3/Clay candidate")
    os.makedirs(os.path.join(HERE, "results_resolution_rescue"), exist_ok=True)
    out = os.path.join(HERE, "results_resolution_rescue", f"{name}.json")
    with open(out, "w") as fh:
        json.dump(result, fh, indent=1)
    print(f"{name}: N={g.N} max_tail={max_tail:.3e} pass={result['tail_pass']} "
          f"energy_step_growth={max_energy_step_growth:.3e} wall={result['walltime_s']:.1f}s", flush=True)
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("pass one or more CONFIGS names")
    for run_name in sys.argv[1:]:
        if run_name not in CONFIGS:
            raise SystemExit(f"unknown run {run_name}; choose from {sorted(CONFIGS)}")
        run(run_name)
