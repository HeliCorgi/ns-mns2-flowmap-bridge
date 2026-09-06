"""Run the expensive Yu-structured filtered near/far diagnostic only on rescued M-1 grids.

A run should enter the mechanism verdict only after its matching resolution_rescue JSON reports
``tail_pass=true`` for the whole interval. This script refuses otherwise.
"""
from __future__ import annotations

import json
import os
import sys
import time

import events as ev
import nearfar_yu as nf
import resolution_rescue as rr

HERE = os.path.dirname(os.path.abspath(__file__))


def run(name: str) -> dict:
    screen_path = os.path.join(HERE, "results_resolution_rescue", f"{name}.json")
    if not os.path.exists(screen_path):
        raise RuntimeError(f"missing resolution screen: {screen_path}")
    with open(screen_path) as fh:
        screen = json.load(fh)
    if not (screen.get("tail_pass") and screen.get("finite_pass")):
        raise RuntimeError(f"{name}: fail-closed; resolution screen did not pass")

    cfg = rr.CONFIGS[name]
    g = ev.Grid(cfg["N"])
    nu, T, dt = cfg["nu"], cfg["T"], cfg["dt"]
    uh = g.project(cfg["ic"](g)) * g.DEALIAS
    nsteps = int(round(T / dt))
    every = max(1, int(round(0.1 / dt)))
    out = dict(name=name, nu=nu, N=cfg["N"], T=T, dt=dt, rho=nf.RHO,
               resolution_screen=os.path.basename(screen_path), t=[], snap=[], tail=[])
    t0 = time.time()
    for step in range(nsteps + 1):
        t = step * dt
        if step % every == 0 or step == nsteps:
            out["t"].append(t)
            out["snap"].append(nf.snapshot(g, uh, nu, dt))
            out["tail"].append(g.tail(uh))
        if step == nsteps:
            break
        uh = g.step(uh, nu, dt)
    out["walltime_s"] = time.time() - t0
    outdir = os.path.join(HERE, "results_nearfar_yu_rescue")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, f"{name}.json"), "w") as fh:
        json.dump(out, fh)
    print(f"{name}: near/far rescue done in {out['walltime_s']:.1f}s", flush=True)
    return out


if __name__ == "__main__":
    for name in sys.argv[1:]:
        run(name)
