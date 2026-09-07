# R3 axisymmetric-with-swirl evolution E2R result — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / BOUNDED RESOLUTION-DOMAIN RESCUE`.

This record reports the single bounded E2R rescue preregistered after the first `R3S04` E2
lattice failed. The rescue kept the same continuum datum, equations, SSPRK3 integrator,
centered second-order finite differences, zero artificial outer Dirichlet condition, comparison
fields, norms, common physical comparison region, and qualification thresholds. Only the base
artificial box and frozen mesh ladder were changed before execution.

## Hosted provenance

```text
workflow  R3 axisymmetric swirl bounded E2R rescue
run       34080735102
job       101615368942
head      9a99a6fd5384e1d578398edd517d4b4db318834b
runner    Ubuntu 24.04
python    CPython 3.12.14
numpy     2.5.3
scipy     1.18.1
artifact  10003623062
digest    sha256:608f51b57f3e9415ad9c28d2244b6f01ab6779dab5b2b2c2c4c16f9f94c31407
NPZ sha   3978b8f5a7ee1031347b6f8c4df80aed16209ac838ad360951212fc233ebf585
```

The workflow conclusion is `failure` because the preregistered scientific gate exits nonzero when
any E2R qualification condition fails. The result artifact uploaded successfully and contains
`summary.json` and all six final states in `final_states.npz`; exact NPZ reload passed.

## Frozen rescue lattice

Base artificial box `(Rmax,Zmax)=(1.0,0.9)`:

```text
B160   160 x 288   h=0.00625
B200   200 x 360   h=0.005
B240   240 x 432   h=0.004166666667
B240H  240 x 432   dt_cap=0.00015
```

One-coordinate domain enlargement at B200 spacing:

```text
RPLUS2  (1.2,0.9)  240 x 360
ZPLUS2  (1.0,1.1)  200 x 440
```

Every run passed all inherited E1 smoke gates.

## Field/norm convergence substantially improved

The common-grid comparison extrema were

```text
pair             max relative Linf      max relative physical-L2
B160 -> B200      1.9079362108e-01       1.4003650915e-01
B200 -> B240      3.7249548921e-02       3.2141241020e-02
B240 -> B240H     1.6543421599e-06       1.5257927303e-06
B200 -> RPLUS2    1.4002521410e-05       5.4861147191e-05
B200 -> ZPLUS2    1.2672514175e-05       3.0293426093e-05
```

Unlike the first E2 lattice, **every preregistered field and both relative norms satisfy**

```text
D(B200,B240) < D(B160,B200).
```

The highest-grid time refinement is again orders of magnitude below the fine spatial discrepancy,
and both independent domain-enlargement tests are now comfortably below the unchanged `1e-3`
threshold.

These improvements are useful numerical information, but E2R was an all-condition gate.

## Exact E2R failures

Only four frozen resolution-diagnostic conditions fail:

```text
min-gradient-scale sequence:
  1.6013572691 -> 1.5498904688 -> 1.8747038455
  FAIL: not strictly increasing

B240 minimum gradient scale:
  1.8747038455 grid points
  FAIL: < 2.0

curvature-tail sequence:
  1.2615768946 -> 0.9396271112 -> 1.0702177873
  FAIL: not strictly decreasing

B240 curvature-tail:
  1.0702177873
  FAIL: > 1.0
```

No threshold is relaxed merely because the misses are small. In particular `1.8747` is not
rounded up to `2.0`, and `1.0702` is not treated as `<=1.0`.

## Decision

The preregistered bounded stop rule therefore applies exactly:

```text
R3-E2R-SAME-DATUM-CONVERGENCE = FAIL
R3S04-CENTERED-FD-ZERO-BC-STACK = PARK
R3S04-RESOLVED-R3-TRAJECTORY = NOT ESTABLISHED
R3-MULTI-SEED-SCREEN = NOT LICENSED BY R3S04
NO THIRD R3S04 RESOLUTION-RESCUE LATTICE
```

This is a numerical qualification stop for this **datum + discretization + artificial-boundary
stack**, not a statement about the continuum Navier--Stokes solution. The strong field/norm,
time, and domain behavior may inform a future method redesign, but it does not override the frozen
gate.

## Allowed next directions

The E2R preregistration permits continuation only through one of two genuinely new contracts:

1. a different numerical method for `R3S04`, with its own manufactured E0/E1 qualification; or
2. a separately preregistered different continuum datum, not an unbounded resolution escalation
   of `R3S04`.

A natural alternate-datum choice from the already-frozen seed family is `R3S02`
(`s0=0.04`, `ws=0.05`, `wz=0.28`, `zu=0`), selected **before any R3S02 evolution result** because
within the frozen lattice it combines the smallest radial center with the widest axial support,
thereby giving the least steep radial/axial geometry among the unshifted seeds without changing
the formulas or amplitudes. Any such continuation requires a fresh preregistration before hosted
evolution.

## Nonclaims

E2R FAIL does not prove regularity, exclude a singularity, or refute the `R3S04` continuum datum.
It proves only that this finite-resolution numerical stack did not meet its own predeclared
qualification rule. No Clay A/B/C/D conclusion follows.
