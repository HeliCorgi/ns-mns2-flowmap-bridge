# MNS-2 / Navier--Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST — periodic M-1 stopped; primary `R^3` axisymmetric-swirl track through E1**.

This is the durable continuation point. Merged `main` controls accepted repository state; branch
results and Actions artifacts are evidence only for the exact revisions/runs recorded below. No
current result proves Clay A/B/C/D.

## Accepted `main` boundary

Current accepted `main`:

```text
1a9228633b9cc532ece82401410a95945f27bab3
```

This is the merge of PR #105, the calibrated E3c periodic M-1 result. The formal theorem boundary
is unchanged:

- whole-space local actual-NS mild theory for real divergence-free Schwartz data, including
  `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and
  `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic explicit shear sidecar, including `ClayNS.certified_nonzero_periodic_NS` and
  `ClayNS.clayB_has_nonzero_smooth_specialization`;
- universal `ClayNS.ClayB` remains unproved.

No Lean/formal source changed in the numerical work below. `FORMAL_SCOPE.md` and `STATUS.md` do not
need synchronization for this branch.

## Periodic M-1 lane — STOP/PARK

PR #106 is closed **unmerged**:

`[STOPPED] Numerics: test E4c with frozen near-far calibration`.

The preregistered primary row was `(c,sigma)=(16,0.125)`. E4c96 completed its R1 diagnostic and,
on the 17 common positive-forward global-enstrophy times, gave

```text
FAR                       14
NO_POSITIVE_LOCAL_GROWTH   3
```

with the three non-FAR samples at `t=0.1,0.2,1.5`. Therefore even a perfect E4c128 result could
not satisfy the preregistered `17/17 FAR->FAR` GO condition.

E4c128 passed exact R0 artifact provenance/gates in both attempts, then its expensive near/far
step was terminated twice by hosted-runner shutdown (`exit 143`). This is an infrastructure
termination, not a scientific E4c128 FAIL. A third retry is not justified because E4c96 already
logically forces the decision:

```text
M1-FILTERED-NEARFAR-PROMOTION = STOP/PARK
GO_TO_DT2 = NO
```

Do not reopen this periodic mechanism-selection lane through post-hoc calibration changes,
alternative rows, B3 borrowing/interpolation, E4c64 reuse, or `dt/2` rescue.

## Active branch — primary `R^3` axisymmetric-with-swirl track

Branch:

```text
research/r3-axisym-swirl-candidate-seed
```

The load-bearing hosted scientific execution for the current frontier is revision

```text
dd8b06af0837b40eb221b7a54bb22b5211d76f1a
```

Later commits on the same branch only record result documentation unless explicitly noted.
No PR has been opened yet, avoiding an unnecessary Lean PR build while this numerical lane is
still being qualified.

### S0 — explicit compact continuum seed family

`compact_family.py` defines 12 fixed `C_c^infty` axisymmetric-with-swirl continuum data using
`s=r^2`, with `omega1` derived exactly from `-L5 psi1` and Cartesian reconstruction built in.

Hosted S0 certificate:

```text
run       34066171548
job       101575195688
head      763dbc36812b5a2592f3784bda31c6db65b3ba31
artifact  9998999218
digest    sha256:8f84c3175537118f07112e3d67756fe7c043f964d42fada79daf2d28c6a29582
result    12/12 PASS
```

This certifies the static formula/reconstruction audit only; it is not evolution evidence.

### E0 — strictly nonperiodic elliptic prototype

`free_space_elliptic_prototype.py` solves the truncated-box approximation to

\[
-\mathcal L_5\psi_1=\omega_1,
\qquad \mathcal L_5=\partial_r^2+3r^{-1}\partial_r+\partial_z^2,
\]

with the regular axis limit and strictly nonperiodic `z`.

The completed E0 suite was rerun successfully on the E1 scientific head `dd8b06af...` and now
includes:

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

The low-axial-frequency manufactured stress uses
`psi=exp(-r^2/0.20^2-z^2/0.80^2)` and showed clear second-order reduction at
`24/48/96`, so the old periodic-Fourier-gap concern is explicitly tested at E0.

### E1 — nonlinear integrator smoke

Preregistration: `experiments/r3_axi_swirl/R3_EVOLUTION_E1_PREREG_2026-09-07.md`.

Frozen run: `R3S04`, `nu=.002`, `T=.02`, `(Rmax,Zmax)=(.8,.7)`, `nr=96`, `nz=168`,
SSPRK3, centered second-order node FD, factorized `-L5`, zero artificial outer Dirichlet,
strictly nonperiodic `z`.

Hosted result:

```text
workflow  R3 axisymmetric swirl nonlinear E1
run       34075898846
job       101601815270
head      dd8b06af0837b40eb221b7a54bb22b5211d76f1a
artifact  10002018444
digest    sha256:9de007fd3ecbc15c385fb47d33e40462bda548986de087dc9d9e1072a03db0a2
result    SUCCESS / E1_pass=True
```

Key streamed maxima/minima:

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

Exact current decision:

```text
R3-E1-NONLINEAR-INTEGRATOR-SMOKE = PASS
R3-E1-RESOLVED-R3-TRAJECTORY = NOT ESTABLISHED
R3-E1-GROWTH-CANDIDATE = NO CLAIM
R3-FREE-SPACE-TRUNCATION-CERTIFICATE = NOT DONE
```

The weak resolution diagnostics matter: `1.43` grid points for the minimum gradient scale and
curvature-tail `1.93` are acceptable only under the deliberately weak E1 smoke gate. They are not
resolved-candidate evidence. On this short interval energy and circulation decrease, and the run
is not itself a growth event.

## Exact next gate — E2 same-continuum-datum convergence lattice

Before any multi-seed candidate search or singularity/exponent fit, E2 must test the same `R3S04`
continuum datum through:

1. three spatial resolutions on the same physical box;
2. highest accepted spatial grid rerun with actual time step halved;
3. radial-only and axial-only domain enlargement at fixed physical grid spacing;
4. common-physical-coordinate comparisons of `u1`, `omega1`, reconstructed velocity, and first
   derivatives;
5. all E1 streaming gates at every run;
6. reload/provenance and finite-state checks.

No resolution threshold or exponent fit may be selected after seeing E2 results. The next code
change should therefore be an E2 preregistration plus a comparison driver before the hosted
lattice is run.

## Negative-knowledge / commission boundaries

Do not reopen the steady continuous self-similar front (Tsai / Chae--Wolf kill), continuum-to-
lattice shadowing, or other registry-killed routes without proving escape from the recorded
binding obstruction. Do not identify the 5D scalar `L5` representation with a 5D fluid problem.
Do not call truncated-box E0/E1 evidence a whole-space convergence theorem.

No current numerical result proves finite-time singularity, nonextendability, global regularity,
or Clay A/B/C/D.
