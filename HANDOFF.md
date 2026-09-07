# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST — R3 W0 PASS; W1 stability PASS; manufactured-v1 STOP; divergence repair PASS; manufactured-v2 PASS**.

This is the durable continuation point. Merged `main` controls accepted repository state; draft/stacked PRs and Actions artifacts are evidence only for the exact revisions/runs recorded below. **No current result proves Clay A/B/C/D.**

## Accepted main boundary

Current merged `main` remains:

```text
1a9228633b9cc532ece82401410a95945f27bab3
```

It includes the accepted periodic M-1 stack through PR #105. The current R3 whole-space numerical stack is unmerged. Formal/Lean state is unchanged:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, including `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92;
- `ClayNS.ClayB` remains defined but unproved;
- no current R3 numerical PR changes formal source.

## Closed periodic M-1 lane

PR #106 is closed unmerged. Its E4c gate made the preregistered all-FAR/FAR GO condition impossible (`14/17` FAR on E4c96 with three calibration-covered `NO_POSITIVE_LOCAL_GROWTH` samples).

```text
M1-FILTERED-NEARFAR-PROMOTION = STOP/PARK
GO_TO_DT2 = NO
```

Do not reopen this lane by changing `(c,sigma)`, relaxing calibration, borrowing B3, reusing E4c64, or adding a post-hoc `dt/2` rescue.

## Primary active track

`SPEC.md` controls:

```text
domain = R^3
force = 0
axisymmetric with swirl
candidate data = C_c^∞, divergence-free, finite physical R^3 energy
```

Frozen W0 datum family:

```text
u1_0(r,z) = A b(r^2/R^2) (z/Z) b(z^2/Z^2)
omega1_0 = 0
psi1_0 = 0
u_0(x,y,z) = (-y u1_0, x u1_0, 0)
```

Scale-invariant search parameters:

```text
alpha = A R^2 / nu
kappa = Z / R.
```

No current result says this datum has late-time amplification or becomes singular.

## PR #107 — W0 static whole-space gate — PASS, draft/unmerged

```text
branch: research/r3-axisym-wholespace-w0
run: 34107564243
revision: 17a16687637c900c0ac1f62619eae04eec3ddf5c
artifact: 10012988252
sha256:38ea952245d2e84b20392d3cefeda9fe9c958e67cf952d9dc93f270203d8f4d6
R3-W0 = PASS
```

It passed exact datum, independent 5-D free-space Green reference, independent radial/axial box expansion, long-axial-scale stress, and physical-vs-lifted measure checks. This is a static domain-correctness audit, not a continuum evolution theorem. Compact-source far-field bounds from W0 are not automatically valid after viscous evolution spreads the source.

## PR #108 — W1 frozen-coefficient stability preflight — PASS, draft/unmerged

```text
branch: research/r3-axisym-wholespace-w1-preflight
run: 34108056875
revision: c138fb957af98f68007b532e01cc502599f6bdea
artifact: 10013168914
sha256:f3dea6a4cf51945026ad73ef45c89bb138aa6e153a2743db3e695123bd594acf
R3-W1-STABILITY-PREFLIGHT = PASS
```

Frozen detector results:

```text
pure centered advection:
  Heun   1.003194896318756 -> instability detected
  SSPRK3 1.0               -> PASS
  RK4    1.0               -> PASS
oversized row:
  SSPRK3 5.615746020181708 -> rejected
  RK4    4.810988282315105 -> rejected
```

This closes only the P0-A detector preflight, not nonlinear stability.

## PR #109 — W1 manufactured-v1 — STOP, closed/unmerged

Frozen v1 parameters:

```text
nu=.01, A=.16, R=Z=1, alpha=16, kappa=1
Rmax=Zmax=2
h=.04,.02
T=2e-4, dt=2.5e-5
RK4 primary / SSPRK3 comparison
```

Production:

```text
run: 34111861776
revision: c4a69fba0adf253c1c32c5aa4275cc4d1ab4bfdd
artifact: 10014663277
sha256:030daaae303071b742c223f895ea9480aed3d0becc1a4c317c75052be478424e
R3-W1-MANUFACTURED-v1 = STOP_REPAIR_W1_MANUFACTURED
```

All frozen rows passed except the v1 absolute independently reconstructed divergence requirement `<=1e-10`:

```text
h=.04 ~1.030541016664716e-3
h=.02 ~2.5434609153687554e-4
```

Post-run algebra identified the exact centered-stencil product-rule defect

```text
q = D_z psi
u_r = -r q
u_z = 2 psi + r D_r psi
D_r u_r + u_r/r + D_z u_z
  = q_i - (q_{i+1}+q_{i-1})/2
  = -(h^2/2) D_rr q_i.
```

The v1 failure is permanent archival evidence and is never retroactively changed.

Result record:

`docs/gates/R3_AXISYM_WHOLESPACE_W1_MANUFACTURED_RESULT_2026-09-07.md`.

## PR #110 — recovered-divergence diagnostic repair — PASS, draft/unmerged

Branch:

```text
research/r3-axisym-wholespace-w1-divergence-repair
```

Production:

```text
run: 34112298964
revision: 21f994d779a401895fc2f3a8c37da90e82effcc7
artifact: 10014824733
sha256:cc44cb205dedc664d356d651d2aa57edd087f8ea6f78dd355b82ca65aa6474a0
R3-W1-DIVERGENCE-DIAGNOSTIC-REPAIR = PASS
```

The repair was preregistered on two compact manufactured streamfunctions and grids `h=.08,.04,.02`. It independently verified:

```text
D1 exact defect identity: worst relative error 6.197347369817331e-12
D2 independent divergence refinement:
  h=.08 ~4.1525112239459e-3
  h=.04 ~8.940481354390e-4
  h=.02 ~2.139589936968e-4
D3 predicted leading h^2 truncation structure: convergent on both profiles
D4 compatible commutator: worst 1.0667838413545287e-15
```

Interpretation: continuum incompressibility, independent centered-difference truncation, and algebraically compatible discrete cancellation are separate diagnostics.

Result record:

`docs/gates/R3_AXISYM_WHOLESPACE_W1_DIVERGENCE_REPAIR_RESULT_2026-09-07.md`.

## PR #111 — W1 manufactured-v2 — PASS, draft/unmerged

Branch:

```text
research/r3-axisym-wholespace-w1-manufactured-v2
```

V2 was preregistered after the repair, preserving all v1 PDE/data/box/grid/time/integrator settings and every non-divergence M1–M5 threshold. Only the incompressibility diagnostic was versioned:

```text
D1 exact centered defect identity <= 1e-9 at every accepted step
D2 independent divergence h=.02 / h=.04 <= .35 at all 8 matched times
D3 compatible commutator <= 1e-12 at every accepted step
```

The first workflow attempt `34112802643` failed before scientific output because the v2 wrapper removed a descriptive legacy key before the unchanged v1 summary helper read it (`KeyError`). No frozen scientific parameter/formula/tolerance changed. Commit `bd8ee744803b0765608854a6c8e952bd86882b42` restored that key only.

Production rerun:

```text
run: 34112974469
revision: bd8ee744803b0765608854a6c8e952bd86882b42
artifact: 10015094692
sha256:253345aa64bf10a36ab15bae57513bba4305be05f2003c79604571213c02c5b6
R3-W1-MANUFACTURED-V2 = PASS
```

Selected load-bearing numbers:

```text
M1 initial RHS relative errors
h=.04: u1 1.2668778207969671e-2, omega1 1.8570827548033405e-2
h=.02: u1 2.883010626216072e-3,  omega1 4.698892278680341e-3

M2 first-step secant relative errors
h=.04: u1 1.2680807472967607e-2, omega1 1.858807315783536e-2
h=.02: u1 2.894482675017511e-3,  omega1 4.716761042930728e-3

repaired independent-divergence diagnostic
h=.04 RK4 max 1.1301103801072167e-3
h=.02 RK4 max 2.8519330514493156e-4
worst fine/coarse ratio over 8 matched times = 0.2523588050911226

worst D1 identity error = 2.799446840033473e-12
worst D3 compatible commutator = 1.1298500016833566e-15

RK4 vs SSPRK3
h=.04 5.362774111905446e-16
h=.02 5.40883926829345e-16

RK4 resolution difference
u1     4.872515088255439e-7
omega1 1.392358632809876e-2
```

All four runs completed exactly eight accepted steps with zero rejected steps; max frozen-symbol amplification was `1.0`; Poisson residuals stayed below `4.3e-14`; odd-z defects below `8.5e-15`; energy stayed nonincreasing over this horizon; max stepwise energy-balance defect was about `.01313` on `h=.04` and `.00349` on `h=.02`.

Result record:

`docs/gates/R3_AXISYM_WHOLESPACE_W1_MANUFACTURED_V2_RESULT_2026-09-07.md`.

Interpretation: this is a **short-time finite-box implementation milestone only**. It does not validate late-time whole-space evolution.

## Current smallest gate — dynamic-domain / elliptic-boundary audit

Before any candidate-time growth scan, isolate finite-box sensitivity for the evolved state. The next gate must be frozen before output and should keep the physical datum, integrator, time step, grid spacing, and common receiver/core region fixed while independently varying radial and axial box extent.

At matched early-time snapshots, the gate should at minimum:

1. compare evolved `u1` and `omega1` on a common physical core under radial-only and axial-only box expansion;
2. compare the finite-box `psi1`, `partial_r psi1`, and `partial_z psi1` against an independent free-space 5-D Green evaluation of the evolved numerical `omega1` at fixed receivers;
3. keep periodic-z/Fourier-gap machinery completely out of this track;
4. distinguish grid/time error from domain/elliptic-boundary error;
5. fail closed if sensitivity does not decrease under the preregistered independent expansions.

This next gate is still numerical evidence. Because viscosity instantly destroys compact support, an analytic or validated enclosure of the evolved whole-space tail remains a later obligation even if the dynamic-domain audit passes.

No long-time amplification fit, candidate singular time, or blow-up narrative opens before this dynamic-domain / elliptic-boundary gate is resolved.

## Standing negative knowledge / forbidden shortcuts

- Do not merge PRs #107, #108, #110, or #111 without explicit user instruction.
- PR #109 remains closed/unmerged and failed; do not relabel it PASS.
- Do not reopen stopped periodic M-1 by post-hoc parameter choices.
- Do not use a periodic Fourier gap to justify an R3 truncation.
- Do not reuse Hou finite-cylinder no-slip wall closure in the free-space track.
- Do not treat lifted `r^3 dr dz` as physical 3D measure.
- Do not relax preregistered tolerances after seeing production output.
- Do not call W0/W1 numerical gates continuum convergence theorems.
- Do not claim numerical blow-up, global regularity, or Clay A/B/C/D.

## Resume protocol

At substantive resume inspect:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. current merged `main`;
7. PR #107 / W0 artifact `10012988252`;
8. PR #108 / stability artifact `10013168914`;
9. closed PR #109 / failed v1 artifact `10014663277`;
10. PR #110 / divergence-repair artifact `10014824733`;
11. PR #111 / manufactured-v2 artifact `10015094692`;
12. Fable5 P0-A/B/C/E audit text.

Current smallest objective:

```text
preregister and implement the early-time dynamic-domain / elliptic-boundary audit;
only if it passes may a longer candidate-time pilot be opened.
```

No current result proves a 3D Navier–Stokes singularity or global regularity.
