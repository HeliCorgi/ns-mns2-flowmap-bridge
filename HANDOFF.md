# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-09 JST — merged R3 short-time stack and candidate-time pilot; alpha-kappa family screen completed**.

This is the durable continuation point. `main` controls accepted state; exact workflow revisions/artifacts below are the scientific evidence. **No current result proves finite-time blow-up, global regularity, or Clay A/B/C/D.**

## Accepted main boundary

Merged `main` before the current family-screen PR is

```text
3aad852ee20dd0e1e72a4634bcf800c0831a390a
```

This includes merged PRs #107, #108, #110, #111, #113, #115, #116, and #117. Formal/Lean source was not changed by these numerical gates. `ClayNS.ClayB` remains unproved.

Primary physical contract remains `SPEC.md`:

```text
domain = R^3
force = 0
axisymmetric with swirl
nu = .01
candidate data = C_c^infty, divergence-free, finite physical R^3 energy
```

Datum family:

```text
u1_0(r,z)=A b(r^2/R^2)(z/Z)b(z^2/Z^2)
omega1_0=psi1_0=0
alpha=A R^2/nu
kappa=Z/R
```

Physical measure is always `2 pi r dr dz`; the lifted 5-D measure is never a physical-energy measure.

## Permanent stopped/archival rows

```text
PR #106 periodic M-1                STOP/PARK
PR #109 W1 manufactured-v1          STOP_REPAIR_W1_MANUFACTURED
PR #112 dynamic-domain-v1           STOP_REPAIR_GREEN_QUADRATURE
PR #114 dynamic-domain-v2           STOP_REPAIR_DYNAMIC_DOMAIN
```

Do not retroactively relabel these PASS, relax their preregistered thresholds, reopen periodic/Fourier-gap arguments as R3 evidence, or reuse finite-cylinder wall closure as a whole-space theorem.

## Merged R3 infrastructure milestones

```text
PR #107 R3-W0 static whole-space                 PASS
PR #108 R3-W1 stability preflight                PASS
PR #110 recovered-divergence diagnostic repair   PASS
PR #111 manufactured short-time v2               PASS
PR #113 arbitrary-source Green quadrature repair PASS
PR #115 elliptic discretization/boundary split   PASS
PR #116 resolution-aware early dynamics          PASS
```

Load-bearing artifacts remain recorded in their result documents. These are numerical implementation/domain audits, not continuum theorems.

## Merged PR #117 — candidate-time pilot

Production:

```text
revision: 3d180af78735ef5a674c36b6699351da63a3cfac
workflow run: 34316821748
artifact: 10090698088
sha256:0cdd946049c97d61badc815cdf13d1147a3b142d6cd8fba8e4f806bd6c558d67
R3-CANDIDATE-TIME-PILOT = PASS_NO_GROWTH_TRIGGER_THROUGH_T025
```

Frozen datum was `(alpha,kappa)=(16,1)` through `T=.25`. Numerical-validity rows passed, including three-level state/velocity refinement, independent time-step shadow, and later-time B22/B44 domain veto.

Finest B22 growth diagnostics:

```text
max physical enstrophy / initial = 1.0
final physical enstrophy / initial = 0.7794650982175626
final physical-vorticity sup / initial = 0.947673253825679
final max|u1| / initial = 0.947673253825679
```

Interpretation: dissipative through this horizon; no preregistered growth trigger. This does not prove regularity or exclude later growth.

## Current PR #118 — alpha-kappa family screen

Branch:

```text
research/r3-axisym-wholespace-family-screen
```

Preregistered grid:

```text
alpha = {16,32,64,128}
kappa = {.75,1.00,1.50}
T=.25, h=.08, dt=.002, RK4
B22 and B44 for every row
```

Production scientific revision:

```text
ba8ccc63016ac97a4bfc43157707bbfafd3d1147
workflow: R3 alpha-kappa family screen
run: 34330169892
conclusion: success
artifact: r3-alpha-kappa-family-screen
artifact id: 10095803752
sha256:76692b74bbecca915d75efdf1d256237a211bfda7ed6b05ba952a85d8c1d055b
```

Exact machine decision:

```text
R3-FAMILY-SCREEN = PASS_NO_PROMOTIONS
promotion_set = []
```

All 12 rows passed runtime and B22/B44 domain vetoes. Every row had

```text
max physical enstrophy / initial = 1.0
```

so no enstrophy amplification occurred above the initial value. B44 final physical-vorticity ratios ranged approximately `.9171` to `.96475`, all below one.

Worst domain metrics were

```text
max state B22/B44 relative difference    7.597116483473903e-6
max velocity B22/B44 relative difference 3.2365476928470954e-3
max Emax ratio box delta                  0
max final-vorticity ratio box delta       9.389977746243616e-6
```

all well inside frozen screen vetoes.

The largest descriptive generated toroidal-vorticity scale was

```text
final max|omega1|/A = 0.15074196234560067
at (alpha,kappa)=(128,.75)
```

but the same row's physical-vorticity supremum ended below its initial value. No row qualifies for high-resolution confirmation under the preregistered rule. Do **not** run high-resolution confirmation for a non-promoted row without opening a new, separately justified gate.

Result record:

`docs/reports/R3_AXISYM_WHOLESPACE_FAMILY_SCREEN_RESULT_2026-09-09.md`.

## Current interpretation

The present compact pure-swirl bump family, over the frozen parameter rectangle sampled here and through `T=.25`, has shown dissipation rather than a physical enstrophy/vorticity growth event. Increasing `alpha` up to 128 did generate more normalized `omega1`, but did not produce the preregistered physical-growth trigger.

This narrows the usefulness of this particular family for the breakdown-side search. It does not justify extrapolating beyond the sampled parameter grid/horizon, and it says nothing decisive about different compact datum shapes.

## Next smallest research gate

Because `promotion_set=[]`, the preregistered high-resolution confirmation lane is closed for this screen. The next step should be a **new shape-family or mechanism-level preregistration**, not post-hoc high-resolution work on one of these rows.

A sensible next design should change one structural feature at a time while preserving exact `C_c^infty`, divergence-free R3 admissibility and all W1 runtime/domain obligations. Candidate directions include changing the signed axial profile or radial localization so that initial swirl-generated `partial_z(u1^2)` produces stronger spatial alignment with meridional stretching. Any such family must be analytically specified before numerical output and must not be selected by inspecting a broad unregistered parameter sweep.

## Resume protocol

At substantive resume inspect:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. current `main`;
7. PR #117 result record/artifact;
8. PR #118 preregistration/result/artifact if merged;
9. external Fable5 exclusion registry / P0 audit.

Standing rules: fail closed, preserve archival STOPs, keep numerical evidence distinct from continuum proof, and make no Clay claim without closing the actual continuation/nonextendability obligations.