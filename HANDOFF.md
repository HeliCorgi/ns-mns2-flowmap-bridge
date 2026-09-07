# MNS-2 / Navier--Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST — periodic M-1 parked; primary `R^3` axisymmetric-swirl track at bounded E2R rescue**.

This is the durable continuation point. Merged `main` controls accepted repository state; branch
results and Actions artifacts are evidence only for the exact revisions/runs recorded below. No
current result proves Clay A/B/C/D.

## Accepted `main` boundary

Current accepted `main`:

```text
1a9228633b9cc532ece82401410a95945f27bab3
```

This includes merged PRs #102--#105. Formal state is unchanged by the numerical work below:

- whole-space local actual-NS mild theory for real divergence-free Schwartz data, including
  `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and
  `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic explicit special-family sidecar, including `ClayNS.certified_nonzero_periodic_NS` and
  `ClayNS.clayB_has_nonzero_smooth_specialization`;
- universal `ClayNS.ClayB` remains unproved.

No Lean/formal source changed on the active numerical branch. `FORMAL_SCOPE.md` and `STATUS.md`
remain unchanged.

## Periodic M-1 lane — STOP/PARK

PR #106 is closed **unmerged**. The frozen primary row `(c,sigma)=(16,0.125)` gave on E4c96,
across the 17 common positive-forward global-enstrophy times,

```text
FAR                       14
NO_POSITIVE_LOCAL_GROWTH   3
```

so even a perfect E4c128 result could not satisfy the preregistered `17/17 FAR->FAR` GO rule.
E4c128 passed its R0 provenance/gates in both attempts and then suffered hosted-runner shutdown
inside the expensive near/far computation; that is infrastructure termination, not a scientific
E4c128 FAIL. Exact decision:

```text
M1-FILTERED-NEARFAR-PROMOTION = STOP/PARK
GO_TO_DT2 = NO
```

Do not reopen through post-hoc calibration changes, an alternative `(c,sigma)` row, B3 borrowing,
E4c64 reuse, or a `dt/2` rescue.

## Active branch — primary `R^3` axisymmetric-with-swirl track

Branch:

```text
research/r3-axisym-swirl-candidate-seed
```

No PR is open yet; this avoids spending Lean PR CI while the numerical stack is still being
qualified. The continuum target is the unforced whole-space `R^3` axisymmetric-with-swirl system
from `SPEC.md`. The finite rectangles below are artificial truncations only.

### S0 — explicit compact continuum seed family: PASS

`compact_family.py` defines 12 fixed `C_c^infty` axisymmetric-with-swirl continuum data using
`s=r^2`; `omega1` is derived from `-L5 psi1`, and Cartesian reconstruction/axis regularity are
audited.

Hosted S0 certificate:

```text
run       34066171548
job       101575195688
head      763dbc36812b5a2592f3784bda31c6db65b3ba31
artifact  9998999218
digest    sha256:8f84c3175537118f07112e3d67756fe7c043f964d42fada79daf2d28c6a29582
result    12/12 PASS
```

### E0 — strictly nonperiodic elliptic prototype: PASS as numerical prototype

The truncated-box solver for

\[
-\mathcal L_5\psi_1=\omega_1,
\qquad \mathcal L_5=\partial_r^2+3r^{-1}\partial_r+\partial_z^2
\]

uses the regular axis limit and strictly nonperiodic `z`. The completed hosted suite includes:

```text
R3-E0-GAUSSIAN-SPATIAL-REFINEMENT             PASS
R3-E0-FIRST-DERIVATIVE-RECOVERY               PASS
R3-E0-GREEN-REFERENCE-CROSSCHECK              PASS (floating, not interval)
R3-E0-INDEPENDENT-R/Z-DOMAIN-SENSITIVITY      PASS as diagnostic
R3-E0-LOW-AXIAL-FREQUENCY-STRESS              PASS
R3-E0-COMPACT-R3S04-RECOVERY                  PASS
R3-E0-HOSTED-REVISION-CERT                    PASS
R3-E0-RIGOROUS-FREE-SPACE-TAIL-ENCLOSURE      NOT DONE
```

The completed E0 suite passed as a fail-closed precondition of hosted E1/E2 executions.

### E1 — nonlinear SSPRK3 smoke: PASS, not a resolved trajectory

Preregistration: `experiments/r3_axi_swirl/R3_EVOLUTION_E1_PREREG_2026-09-07.md`.
Hosted scientific run:

```text
workflow  R3 axisymmetric swirl nonlinear E1
run       34075898846
job       101601815270
head      dd8b06af0837b40eb221b7a54bb22b5211d76f1a
artifact  10002018444
digest    sha256:9de007fd3ecbc15c385fb47d33e40462bda548986de087dc9d9e1072a03db0a2
result    E1_pass=True
```

Key streamed diagnostics:

```text
accepted/rejected steps            20 / 0
max pre/stage/post CFL             0.07844
max viscous number                 0.576
max positive one-step dE/E         0
Gamma sup overshoot                0
axis regularity defect             0
max relative divergence Linf       2.40424e-3
max elliptic residual Linf         1.10489e-12
minimum gradient scale             1.42877 grid points
maximum curvature-tail diagnostic  1.93098
outer shell ratio                  2.02e-77
```

Exact boundary:

```text
R3-E1-NONLINEAR-INTEGRATOR-SMOKE = PASS
R3-E1-RESOLVED-R3-TRAJECTORY = NOT ESTABLISHED
R3-E1-GROWTH-CANDIDATE = NO CLAIM
```

### E2 — first same-datum convergence lattice: FAIL

Preregistration:
`experiments/r3_axi_swirl/R3_EVOLUTION_E2_PREREG_2026-09-07.md`.
Result record:
`experiments/r3_axi_swirl/R3_EVOLUTION_E2_RESULT_2026-09-07.md`.

Hosted provenance:

```text
workflow  R3 axisymmetric swirl convergence E2
run       34076351801
job       101603124339
head      37368f37fb32477850388fe9abc3c0a8df5141e6
artifact  10002183475
digest    sha256:6d88d10749cc744dcf2c2afecce019b000461cf2cf9f98994dffd9de8ea511a2
NPZ sha   c14c45618f9a07c4a65d247ffa0a071d8fca3bc719120609c6fd80ab879bdf3a
result    R3-E2-SAME-DATUM-CONVERGENCE = FAIL
```

All six runs passed inherited E1 gates and exact NPZ reload. Time refinement was very small:

```text
max field discrepancy S160 -> S160H
relative Linf   3.96091e-6
relative L2     3.30073e-6
```

but spatial qualification was not in a stable asymptotic regime. The worst fine-pair relative
`Linf` remained `1.90782e-1`, 12 preregistered field/norm spatial inequalities failed, the minimum
gradient scale sequence was

```text
1.428770 -> 1.601331 -> 1.549889 grid points
```

and S160 missed the required `>=2.0` points. The curvature-tail diagnostic did improve
`1.930980 -> 1.261577 -> 0.939627`. The radial-only domain test also missed one frozen threshold:
`uz` relative physical-L2 `1.133115e-3 > 1e-3`.

Exact decision:

```text
R3-E2-SAME-DATUM-CONVERGENCE = FAIL
R3-E2-TIME-REFINEMENT = PASS as subdiagnostic
R3-E2-SPATIAL-ASYMPTOTIC-REGIME = NOT ESTABLISHED
R3S04-RESOLVED-R3-TRAJECTORY = NOT ESTABLISHED
R3-MULTI-SEED-SCREEN = NOT LICENSED BY E2
```

No E2 threshold was relaxed and no failing field was deleted.

### Current gate — one bounded E2R resolution/domain rescue

Preregistration:
`experiments/r3_axi_swirl/R3_EVOLUTION_E2R_PREREG_2026-09-07.md`.
Implementation:
`experiments/r3_axi_swirl/check_evolution_e2_rescue.py`.

The rescue keeps `R3S04`, `nu=.002`, `T=.02`, equations, SSPRK3, centered second-order FD,
zero artificial outer Dirichlet, common comparison grid, all 15 comparison fields, norm
definitions, and all qualification thresholds unchanged. It changes only the artificial box and
frozen mesh lattice.

Base box and spatial ladder:

```text
(Rmax,Zmax)=(1.0,0.9)
B160  160 x 288   h=0.00625
B200  200 x 360   h=0.005
B240  240 x 432   h=0.004166666667
B240H same B240 grid, dt_cap=0.00015
```

One-coordinate domain tests at B200 spacing:

```text
RPLUS2  (Rmax,Zmax)=(1.2,0.9), 240 x 360
ZPLUS2  (Rmax,Zmax)=(1.0,1.1), 200 x 440
```

The same E2 rules are reused: every fine spatial discrepancy must improve, the B240 minimum
gradient scale must be at least 2 points, curvature-tail must decrease to at most 1, highest-grid
`dt/2` must be subdominant, and every domain discrepancy must be at most `1e-3`.

Hosted E2R execution is currently active at this handoff revision family:

```text
workflow  R3 axisymmetric swirl bounded E2R rescue
run       34080735102
head      9a99a6fd5384e1d578398edd517d4b4db318834b
status    IN PROGRESS at handoff update
```

Bounded stop rule is frozen: if E2R fails, park `R3S04 + centered-FD + zero-Dirichlet` and do not
add another resolution rescue. A future continuation would require a genuinely new numerical
method contract or a separately preregistered continuum datum. If E2R passes, it only licenses a
separate bounded multi-seed screen; it is not continuum convergence or a blow-up claim.

## Negative knowledge / forbidden shortcuts

Do not reopen the steady continuous self-similar front (Tsai / Chae--Wolf kill), continuum-to-
lattice shadowing, or other registry-killed routes without proving escape from the recorded
binding obstruction. Do not identify the scalar 5D representation of `L5` with a 5D fluid
problem. Do not call finite-box E0/E1/E2R results a whole-space theorem. Do not fit a singularity
exponent or blow-up time before numerical qualification. Do not add Lean plumbing merely because
new numerical files exist.

## Resume protocol

On resume inspect `PROJECT_GOAL.md`, `SPEC.md`, `AGENTS.md`, `FORMAL_SCOPE.md`, this file,
`R3_WHOLE_SPACE_SOLVER_CONTRACT_2026-09-07.md`, the E2/E2R prereg/result records, current `main`,
active branch head, and exact hosted E2R run/artifact. First action is to adjudicate run
`34080735102` exactly against the frozen E2R rule and record PASS/FAIL without threshold changes.

No current numerical result proves finite-time singularity, nonextendability, global regularity,
or Clay A/B/C/D.
