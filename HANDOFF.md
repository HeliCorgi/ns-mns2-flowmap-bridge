# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST — R3 W0 PASS; W1 stability preflight PASS; short-time manufactured gate next**.

This is the durable continuation point. Merged `main` controls accepted repository state; draft/stacked PRs and Actions artifacts are evidence only for the exact revisions/runs recorded below. **No current result proves Clay A/B/C/D.**

## Accepted main boundary

Current merged `main` head at this handoff is:

```text
1a9228633b9cc532ece82401410a95945f27bab3
```

which includes PRs #102–#105 from the periodic M-1 numerical stack. Formal state is unchanged by the current R3 numerical work:

- whole-space `R^3` local actual-NS mild stack for real divergence-free Schwartz data, including `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic special-family sidecar from PR #92;
- `ClayNS.ClayB` remains defined but unproved;
- no Lean/formal source has changed in PRs #107/#108.

## Closed periodic M-1 lane

PR #106 executed the second fixed-continuum E4c gate and is **closed unmerged**. E4c96 gave only `14/17` primary-row FAR samples; three calibration-covered samples at `t=0.1,0.2,1.5` had `NO_POSITIVE_LOCAL_GROWTH`. Therefore the preregistered all-FAR/FAR GO condition was logically impossible even without E4c128 completion.

Exact decision:

```text
M1-FILTERED-NEARFAR-PROMOTION = STOP/PARK
GO_TO_DT2 = NO
```

Do not reopen this lane by changing `(c,sigma)`, relaxing calibration, borrowing B3, reusing E4c64, or adding a post-hoc `dt/2` rescue.

## Primary active track — unforced whole-space R3 axisymmetric with swirl

`SPEC.md` controls this track:

```text
domain = R^3
force = 0
axisymmetric with swirl
candidate data = C_c^∞, divergence-free, finite physical R^3 energy
```

The exact W0 datum family is

```text
u1_0(r,z) = A b(r^2/R^2) (z/Z) b(z^2/Z^2)
omega1_0 = 0
psi1_0 = 0
u_0(x,y,z) = (-y u1_0, x u1_0, 0)
```

with radial dependence through `r^2`, hence Cartesian smoothness at the axis. The scale-invariant search parameters are

```text
alpha = A R^2 / nu
kappa = Z / R.
```

No current result says this datum amplifies or becomes singular.

## PR #107 — R3 whole-space W0 static gate — PASS, draft/unmerged

PR #107:

```text
Research: certify R3 axisymmetric whole-space W0 static gate
head branch: research/r3-axisym-wholespace-w0
status: DRAFT / OPEN / UNMERGED
```

Frozen implementation gate:

`docs/gates/R3_AXISYM_WHOLESPACE_W0_IMPLEMENTATION_PREREG_2026-09-07.md`.

Production execution:

```text
revision: 17a16687637c900c0ac1f62619eae04eec3ddf5c
workflow: R3 whole-space W0 static gate
run: 34107564243
conclusion: success
artifact: 10012988252
sha256:38ea952245d2e84b20392d3cefeda9fe9c958e67cf952d9dc93f270203d8f4d6
```

Exact decision:

```text
W0-A PASS  exact datum / Cartesian divergence / energy / support
W0-B PASS  independent 5-D Green reference + finite-box discretization
W0-C PASS  independent Rmax and Zmax zero-boundary expansions + far-field envelope
W0-D PASS  doubled axial-width nonperiodic low-frequency stress
W0-E PASS  odd lifted monopole + physical-vs-lifted measure audit
R3-W0 PASS
```

Selected load-bearing numbers:

```text
Green 48^3 -> 64^3 worst difference: 8.393239228632332e-12
W0-B h=.02 combined receiver error:
  even 1.43898077077948e-4
  odd  2.815451678618197e-4
W0-C final (Rmax,Zmax)=(6,6), h=.02:
  even 3.627737381661155e-3
  odd  3.2107008369493956e-4
W0-D final stress (Rmax,Zmax)=(6,8), h=.02:
  even 4.48602737874246e-3
  odd  2.67524827971251e-4
odd lifted monopole / L1: 2.0029798599148406e-18
```

Result record:

`docs/gates/R3_AXISYM_WHOLESPACE_W0_RESULT_2026-09-07.md`.

Interpretation: the **static** whole-space gateway passed on the frozen manufactured tests. This is not a continuum evolution theorem. In particular, compact-source far-field envelopes are not automatically valid for later viscously spread evolved sources.

## PR #108 — R3 W1 stability preflight — PASS, draft/unmerged

PR #108 is stacked on PR #107:

```text
Research: certify R3 W1 stability preflight
base: research/r3-axisym-wholespace-w0
head: research/r3-axisym-wholespace-w1-preflight
status: DRAFT / OPEN / UNMERGED
```

Frozen preregistration:

`docs/gates/R3_AXISYM_WHOLESPACE_W1_STABILITY_PREREG_2026-09-07.md`.

Production execution:

```text
revision: c138fb957af98f68007b532e01cc502599f6bdea
workflow: R3 W1 stability preflight
run: 34108056875
conclusion: success
artifact: 10013168914
sha256:f3dea6a4cf51945026ad73ef45c89bb138aa6e153a2743db3e695123bd594acf
```

Frozen detector result:

```text
S1 pure centered advection:
  Heun   1.003194896318756   instability detected
  SSPRK3 1.0                 PASS
  RK4    1.0                 PASS
S2 stable advection-diffusion + conservative L5 radial stress:
  SSPRK3 1.0                 PASS
  RK4    1.0                 PASS
S3 intentionally oversized step:
  SSPRK3 5.615746020181708   reject as required
  RK4    4.810988282315105   reject as required
R3-W1-STABILITY-PREFLIGHT = PASS
```

Result record:

`docs/gates/R3_AXISYM_WHOLESPACE_W1_STABILITY_RESULT_2026-09-07.md`.

Interpretation: this discharges only the frozen-coefficient **P0-A detector preflight**. It does not prove nonlinear solver stability and does not discharge P0-B/C.

## Current smallest gate — W1 short-time manufactured nonlinear evolution

The next gate is deliberately short-time and diagnostic-only. It must consume the exact W0 identities

```text
partial_t omega1|_0 = partial_z(u1_0^2)
partial_t u1|_0 = nu L5 u1_0
```

before any long-time amplification is inspected.

Before any growth is interpreted, the dynamic implementation must satisfy the standing Fable5 P0-B/C obligations for every attempted/accepted step:

- proposed/accepted/clipped `dt`;
- pre-state and every RK-stage `max|u^r|`, `max|u^z|`;
- pre/stage CFL and viscous stability number;
- pre/stage frozen-symbol amplification factor;
- fail-closed rejected-step count/reason;
- finite-value checks;
- Poisson algebraic residual;
- physical energy and energy-balance defect;
- odd-z and axis-parity defects;
- reconstructed physical divergence;
- streaming acceptance maxima/minima over **all** accepted steps, not only saved snapshots;
- matched RK4 versus SSPRK3 comparison on the same physical datum/output targets.

No long-time amplification scan opens before this short-time manufactured gate passes.

## Standing analytic state / negative knowledge

The B2 middle limb remains open. Previously parked/narrowed analytic lanes remain parked unless their recorded reopen conditions are met. The 2026 axisymmetric-with-swirl global-regularity preprint remains `unverified-with-confirmed-load-bearing-gaps` in the repository audit; do not treat it as a theorem that closes this track.

The external Fable5 audit is binding negative knowledge. In particular:

- periodic-z radial-wall sensitivity is not an R3 transition theorem;
- Heun + centered advection cannot be promoted without stability analysis;
- acceptance-critical diagnostics must be streamed over all steps;
- grid-scale resolution must be measured explicitly before any fitted blow-up narrative.

## Commission boundaries / forbidden shortcuts

Do **not**:

- merge PR #107 or #108 without explicit user instruction and result audit;
- call W0 a continuum whole-space evolution theorem;
- call W1 stability preflight a nonlinear stability theorem or singularity result;
- start a long-time growth scan before the short-time manufactured W1 gate passes;
- use a periodic Fourier gap to justify nonperiodic whole-space truncation;
- reuse Hou finite-cylinder no-slip closure in the free-space track;
- treat lifted `r^3 dr dz` as the physical three-dimensional volume measure;
- relax preregistered tolerances after production output;
- claim Clay A/B/C/D, numerical blow-up, or numerical global regularity.

## Resume protocol

At substantive resume inspect, in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. current `main`;
7. PR #107 and W0 artifact `10012988252`;
8. PR #108 and W1 stability artifact `10013168914`;
9. Fable5 P0-A/B/C/E audit text.

Current smallest objective:

```text
freeze and implement the W1 short-time manufactured nonlinear gate;
only if it passes may candidate-time dynamics be opened.
```

No current result proves a 3D Navier–Stokes singularity or global regularity.
