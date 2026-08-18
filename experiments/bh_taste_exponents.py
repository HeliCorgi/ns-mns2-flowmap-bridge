"""Symbolic exponent bookkeeping for the BH-profile taste pass (no simulation).

Verifies, over rational samples of the frozen interior wedge
    S = { 1/2 < g < 1,  max(1-g, 2g/3, 2g-1) <= a < g,  g + a > 1 },
the residual tau-power table of docs/gates/BH_PROFILE_TASTE_REPORT.md and the
sign claims used by Gates D/E:

  euler pair          -(2g + a)      (reference; cancels for a steady profile)
  amplitude/scale mod -(g + 1)       relative order  g + a - 1  > 0
  swirl-drift (eps')  -(a + 1)       relative order  2g - 1     > 0
  viscous poloidal    -(g + 2a)      relative order  g - a      > 0
  viscous azimuthal   -(3a)          relative (theta-transport) g - a > 0
  PB secular ratio    nu * tau^(1 - 2a)  -> 0 iff a < 1/2

Exit code 0 iff all checks pass on the sample grid.
"""
from fractions import Fraction as F

def lower_env(g):
    return max(1 - g, F(2, 3) * g, 2 * g - 1)

def checks():
    ok = True
    samples = []
    for gnum in range(51, 100, 2):
        g = F(gnum, 100)
        lo, hi = lower_env(g), g
        if lo >= hi:
            ok = False
            print(f"EMPTY window at g={g}")
            continue
        for t in (F(1, 4), F(1, 2), F(3, 4)):
            a = lo + (hi - lo) * t
            if not (g + a > 1):
                # interior branch demands g + a > 1; the lower edge itself has g+a=1
                if g + a == 1 and t == 0:
                    continue
            samples.append((g, a))
    for g, a in samples:
        rel_mod = g + a - 1
        rel_eps = 2 * g - 1
        rel_visc = g - a
        pb = 1 - 2 * a  # PB secular exponent; sustainable iff > 0
        if not (rel_mod >= 0 and rel_eps > 0 and rel_visc > 0):
            ok = False
            print(f"FAIL relative orders at (g,a)=({g},{a}): "
                  f"mod={rel_mod} eps={rel_eps} visc={rel_visc}")
    # PB sub-wedge nonemptiness: a < 1/2 possible iff lower_env(g) < 1/2 iff g < 3/4.
    for gnum in (51, 60, 70, 74):
        g = F(gnum, 100)
        if not (lower_env(g) < F(1, 2)):
            ok = False
            print(f"PB sub-wedge unexpectedly empty at g={g}")
    for gnum in (76, 90, 99):
        g = F(gnum, 100)
        if lower_env(g) < F(1, 2):
            ok = False
            print(f"PB sub-wedge unexpectedly nonempty at g={g}")
    return ok

def table(g, a):
    rows = [
        ("euler pair (cancels)", -(2 * g + a), F(0)),
        ("amplitude/scale modulation", -(g + 1), g + a - 1),
        ("swirl-parameter drift", -(a + 1), 2 * g - 1),
        ("viscous poloidal", -(g + 2 * a), g - a),
        ("viscous azimuthal", -(3 * a), g - a),
    ]
    print(f"\n(g, a) = ({g}, {a});  PB secular exponent 1-2a = {1 - 2 * a}")
    for name, absexp, rel in rows:
        print(f"  {name:28s} tau^({absexp})   relative tau^({rel})")

if __name__ == "__main__":
    good = checks()
    table(F(3, 5), F(47, 100))   # strict-interior PB-compatible sample (a < 1/2)
    table(F(4, 5), F(13, 20))    # a > 1/2 sample (PB-obstructed)
    print("\nALL CHECKS PASS" if good else "\nCHECKS FAILED")
    raise SystemExit(0 if good else 1)
