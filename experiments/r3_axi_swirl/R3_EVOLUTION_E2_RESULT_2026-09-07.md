# R3 axisymmetric-with-swirl evolution E2 result — 2026-09-07

**Classification:** `NUMERICAL CANDIDATE INFRASTRUCTURE / SAME-DATUM CONVERGENCE GATE`.

This record reports the first preregistered E2 lattice for the explicit continuum datum `R3S04`.
It is a numerical qualification test for the truncated-box whole-space approximation, not a
continuum convergence theorem and not singularity evidence.

## Frozen contract

Preregistration:
`experiments/r3_axi_swirl/R3_EVOLUTION_E2_PREREG_2026-09-07.md`.

The fixed physical problem was

```text
seed          R3S04
nu            0.002
T             0.02
integrator    SSPRK3
space         centered second-order node finite differences
elliptic      factorized second-order -L5 solve
z topology    strictly nonperiodic
outer BC      zero artificial Dirichlet
```

The spatial ladder was `S96/S128/S160`; the highest grid was rerun as `S160H` with an actual
approximately factor-two time refinement. Artificial-domain tests enlarged `Rmax` and `Zmax`
separately at the S128 physical mesh spacing. All field/norm/threshold choices were frozen before
execution.

## Hosted execution provenance

```text
workflow  R3 axisymmetric swirl convergence E2
run       34076351801
job       101603124339
head      37368f37fb32477850388fe9abc3c0a8df5141e6
runner    Ubuntu 24.04
python    CPython 3.12.14
numpy     2.5.3
scipy     1.18.1
artifact  10002183475
digest    sha256:6d88d10749cc744dcf2c2afecce019b000461cf2cf9f98994dffd9de8ea511a2
```

The workflow job is `failure` because the preregistered E2 scientific gate intentionally exits
nonzero on any failed qualification condition. The artifact upload completed and contains the
full `summary.json` plus `final_states.npz`.

The NPZ exact-reload check passed and the recorded NPZ SHA-256 is

```text
c14c45618f9a07c4a65d247ffa0a071d8fca3bc719120609c6fd80ab879bdf3a
```

## All-run inherited E1 status

Every E2 run independently passed the inherited E1 smoke gates. No run had a non-finite state,
CFL/viscous rejection, positive one-step energy growth, circulation maximum-principle defect,
axis regularity failure, excessive divergence defect, elliptic residual failure, or boundary-shell
failure.

Resolution diagnostics on the base spatial ladder were

```text
run    min gradient scale (grid points)    max curvature-tail
S96            1.4287703923                    1.9309800360
S128           1.6013311945                    1.2615768946
S160           1.5498890266                    0.9396271112
```

Thus the curvature-tail condition improved through the ladder and reached the preregistered
`<=1.0` threshold, but the minimum gradient scale did not increase monotonically and the S160
value stayed below the required `2.0` grid points.

## Comparison extrema

On the fixed common physical comparison grid,

```text
pair             max relative Linf      max relative physical-L2
S96 -> S128       1.3128016993e-01       1.4422189202e-01
S128 -> S160      1.9078201166e-01       1.3983539371e-01
S160 -> S160H     3.9609056272e-06       3.3007313896e-06
S128 -> RPLUS     3.1712776130e-04       1.1331153849e-03
S128 -> ZPLUS     2.9120642809e-04       6.6454113042e-04
```

The time-refinement discrepancy is several orders of magnitude below the remaining spatial
change. The axial-domain enlargement passes the frozen `1e-3` threshold in all reported extrema.
The radial-domain comparison misses it narrowly in one field/norm, `uz` physical-L2.

## Exact preregistered failures

The gate produced 15 failures:

```text
spatial omega1 relative_linf: 1.907820116599e-01 >= 1.072174003994e-01
spatial omega1 relative_l2:   9.479979520024e-02 >= 6.527426809588e-02
spatial ur relative_linf:     1.231949672519e-01 >= 1.169836022958e-01
spatial uz relative_linf:     6.960733191307e-02 >= 6.029916639293e-02
spatial uz relative_l2:       1.210934744545e-01 >= 1.102651205041e-01
spatial omega1_r relative_l2: 9.066282940474e-02 >= 8.094776670425e-02
spatial ur_r relative_linf:   5.772017040017e-02 >= 4.555405967148e-02
spatial ur_r relative_l2:     8.916738124427e-02 >= 7.826588190412e-02
spatial uz_r relative_linf:   1.081746916920e-01 >= 7.996660244178e-02
spatial uz_r relative_l2:     9.378653188607e-02 >= 7.249378205716e-02
spatial uz_z relative_linf:   6.480415758776e-02 >= 4.663117504191e-02
spatial uz_z relative_l2:     9.003268245537e-02 >= 7.848978599998e-02
min-gradient-scale sequence:  [1.4287703923, 1.6013311945, 1.5498890266] not increasing
S160 min-gradient-scale:      1.5498890266 < 2.0
domain S128_RPLUS uz L2:      1.133115384917e-03 > 1e-3
```

No threshold is relaxed and no failing field is removed.

Several fields did improve on the fine spatial pair (`u1`, `utheta`, `u1_r`, `u1_z`,
`omega1_z`, `ur_z`, `utheta_r`, `utheta_z` in at least the relevant preregistered norms), but E2
was an all-fields gate and therefore fails.

## Decision

```text
R3-E2-SAME-DATUM-CONVERGENCE = FAIL
R3-E2-TIME-REFINEMENT = PASS as a subdiagnostic
R3-E2-SPATIAL-ASYMPTOTIC-REGIME = NOT ESTABLISHED
R3-E2-BASE-BOX-RADIAL-TRUNCATION-THRESHOLD = FAIL narrowly in uz relative L2
R3S04-RESOLVED-R3-TRAJECTORY = NOT ESTABLISHED
R3-MULTI-SEED-SCREEN = NOT LICENSED BY THIS E2
```

The numerical pattern is consistent with spatial resolution/truncation, rather than time
integration, being the present bottleneck: S160/S160H differs only at about `4e-6`, while the fine
spatial pair remains O(`1e-1`) in the worst fields and the narrowest gradient scale is only about
`1.55` grid points. This is an interpretation of the diagnostics, not a theorem.

## Bounded rescue condition

A single separately preregistered **E2R resolution/domain rescue** is permitted because E2 failed
before entering an apparent spatial asymptotic regime and the base radial-domain threshold was
also marginally missed. The rescue must:

- keep the same continuum datum `R3S04`, `nu=0.002`, `T=0.02`, equations, SSPRK3 integrator,
  finite-difference formulas, artificial zero boundary condition, common comparison region, field
  list, norm definitions, and qualification thresholds;
- use a larger base artificial box and a strictly finer three-grid spatial ladder;
- repeat the highest-grid `dt/2` confirmation;
- repeat one-coordinate-at-a-time domain enlargement at fixed physical mesh spacing;
- freeze the entire rescue lattice before execution.

If that bounded E2R also fails, do not continue an unbounded sequence of grid escalations for this
`R3S04 + centered-FD + zero-Dirichlet` stack. Park that discretization/candidate pairing and either
improve the numerical method under a new contract or move to another explicitly preregistered
continuum datum family.

## Nonclaims

This FAIL does not prove regularity or rule out singular behavior of the continuum Navier--Stokes
solution. It only says the first finite-difference/truncated-box lattice did not meet its own
predeclared numerical qualification standard. No Clay A/B/C/D conclusion follows.
