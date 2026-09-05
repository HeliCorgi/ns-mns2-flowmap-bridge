# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-fourth session)**.

This is the durable short-form continuation point. Current theorem/source files and merged `main` control accepted state. Stacked research PRs are branch-local until merged.

## Accepted main boundary

Accepted `main` head before the current research stack is

`327c2fdc382d4a40cc7779552ae898ec70959ed5`.

PR #92 is merged. The accepted periodic sidecar contains

- `Formal/PeriodicClayCore.lean`;
- `Formal/PeriodicExplicitShear.lean`;
- `Formal/PeriodicClayShear.lean`;
- `Formal/PeriodicClayEnergy.lean`;
- `Formal/PeriodicClayQuantifiers.lean`;
- `Formal/PeriodicClayCertificate.lean`;

with anchors `ClayNS.certified_nonzero_periodic_NS`, `ClayNS.clayB_has_nonzero_smooth_specialization`, and the three quantifier/coverage theorems. The universal proposition `ClayNS.ClayB` remains **unproved**. PR #92 head `198f1c68297b1d55aea0a5ea053ca2956e5bb13e` passed hosted Lean workflow #277 (`33996261541`), including the forbidden-source scan and full cached `Formal.+` build under Lean 4.32.1 / mathlib `520045ab14e26149ee970e2e617ca04b09bde5d6`.

The accepted whole-space formal frontier is unchanged: local actual-NS mild theory on `R^3` for real divergence-free Schwartz data, explicit lifespan, unrestricted uniqueness, restart/continuation dichotomy, decoded velocity/pressure semantics, actual incompressible NS at interior times, and the admissible-data adapter. This remains local/distributional, not a Clay result.

## Breakdown research stack

Merged PR #89 is accepted on `main` and establishes the B2 Gamma-max curvature budget. The parent B2 middle limb remains OPEN.

PR #90 (`research/b2-gamma-flattop-enstrophy`) is open and currently mergeable after session-43 conflict resolution. It contains sessions 39–41, including former stacked PR #91 merged into the PR-90 branch:

- `B2-GAMMA-FLATTOP-ENSTROPHY-KILL = NO`;
- `B2-GAMMA-TRANSITION-VORTICITY = YES`;
- `B2-GAMMA-LATE-ARRIVAL-BARRIER = NO`;
- `B2-GAMMA-TRANSITION-RESIDENCE-KILL = NO`;
- `B2-GAMMA-HITTING-STRAIN = YES`;
- `B2-GAMMA-HITTING-NEW-EXPONENT-CUT = NO`;
- `B2-GAMMA-STRAIN-ELLIPTIC-KILL = NO`;
- `B2-GAMMA-SATURATION-MICROGEOMETRY = PARKED`.

PR #90 conflict-resolution head:

`cf8ea8b0ba502223e83c03383abc4187ba1ccfe2`.

The conflict was only the simultaneous `HANDOFF.md` edit on `main` and the branch; all accepted PR-92 formal files plus all three B2 gate records were retained. No Lean/runtime source changed. Hosted workflow #278 was triggered by the synchronized PR-90 head; read its live status rather than inferring from older runs.

S15 and the FDT cross-track remain parked. The Gamma-saturation microgeometry subprogram remains parked. Do not reopen them without their recorded reopen conditions.

## Session 44 — B2 ancient-Euler compactness decision

Record:

`docs/gates/B2_ANCIENT_EULER_COMPACTNESS_DECISION_2026-09-06.md`.

The post-K11 interior has

`gamma > alpha`, `gamma + alpha > 1`,

with amplitude/scale

`U_n ~ tau_n^(-gamma)`, `ell_n ~ tau_n^alpha`.

Using convective time

`theta_n = ell_n/U_n ~ tau_n^(alpha+gamma)`

and normalized fields

`v_n(y,s)=U_n^(-1)u(x_n+ell_n y,t_n+theta_n s)`,

the exact equation is

`partial_s v_n + (v_n.grad)v_n + grad q_n = eps_n Delta v_n`,

`eps_n = nu/(U_n ell_n) ~ nu tau_n^(gamma-alpha) -> 0`.

Also

`tau_n/theta_n ~ tau_n^(1-alpha-gamma) -> infinity`,

so both forward and backward normalized time horizons tend to infinity. Decisions:

- **`B2-ANCIENT-VANISHING-VISCOSITY = YES`;**
- **`B2-ANCIENT-ETERNAL-WINDOW = YES`.**

Under the natural local normalized `L^infinity` envelope one may extract

`v_n weak-* -> v`, `v_n tensor v_n weak-* -> M`,

and the viscosity vanishes distributionally. The honest compactness endpoint is therefore Euler--Reynolds:

`partial_s v + div(v tensor v) + grad q = -div R`,

`R=M-v tensor v`.

No current B2 budget forces `R=0`, and pointwise max normalization does not force a nonzero weak limit. A smooth axisymmetric pure-swirl high-frequency counterprofile shows why symmetry + `L^infinity` compactness alone cannot identify the quadratic limit. It is a kinematic compactness counterprofile only, not an NS witness.

Decision:

- **`B2-ANCIENT-EULER-REYNOLDS-LIMIT = YES`** conditional on local normalized `L^infinity` tightness;
- **`B2-ANCIENT-EULER-COMPACTNESS = NO` from current B2 controls.**

The naive second step also fails: smooth compactly supported nontrivial steady Euler flows in `R^3` exist, and Constantin--La--Vicol realize the construction through the stationary **axisymmetric Grad--Shafranov ansatz with swirl**. Their multiscale construction also allows independently rescaled steady templates. Hence:

- **`B2-STEADY-EULER-STATIC-LIOUVILLE-KILL = NO`;**
- **`B2-STEADY-EULER-STATIC-EXPONENT-CUT = NO`.**

This does not reopen the external-registry route already killed for a continuous self-similar steady-front NS profile. The present interior leading equation is steady Euler; the relevant compact Euler templates are known to exist.

### New positive calculation: first-order modulation adjoint

For a nonzero compact smooth steady Euler profile `V`, let

`L_V w = P[(V.grad)w + (w.grad)V]`.

For divergence-free `w`,

`<V,L_V w> = 0`.

For the dilation generator

`D_{gamma,alpha}V = gamma V + alpha (y.grad)V`,

one has

`<V,D_{gamma,alpha}V> = (gamma - 3 alpha/2)||V||_2^2`,

and

`<V,-Delta V> = ||grad V||_2^2 > 0`.

In a dynamically normalized fixed-shape frame the two subleading coefficients are

`delta_t ~ tau^(alpha+gamma-1)`,

`delta_nu ~ nu tau^(gamma-alpha)`,

so

`delta_nu/delta_t = nu tau^(1-2alpha)`.

A bounded first-order correction to a **shape-stationary** steady profile must therefore satisfy the exact adjoint solvability balance

`delta_t (gamma - 3 alpha/2)||V||_2^2 + delta_nu ||grad V||_2^2 = lower order`.

Conditional consequences:

- `alpha<1/2`: leading solvability forces `alpha=2gamma/3`;
- `alpha>1/2`: the viscous forcing fails the adjoint test for every nonzero compact fixed profile;
- `alpha=1/2`: one needs the tuned relation `(3/4-gamma)||V||_2^2 = nu||grad V||_2^2`.

Decision:

**`B2-STEADY-EULER-MODULATION-ADJOINT = YES` as a conditional algebraic obstruction.**

It is not an unconditional exponent cut because the current B2 hypotheses do not provide defect-free strong compactness, nonzero compact profile convergence, asymptotic shape stationarity, or a justified bounded first-order expansion.

## Next work

The only live continuation of the ancient/steady-Euler idea is

**`B2-MODULATION-COMPACTNESS`**:

> For one fixed hypothetical B2 solution in the K11 interior, do actual NS plus the existing energy/dissipation/Type-II hypotheses force enough strong compactness and asymptotic shape stationarity to make the first-order steady-Euler modulation equation valid with a bounded correction?

A YES activates the adjoint obstruction and would collapse a large portion of the interior exponent wedge toward exceptional balance sets. A NO must exhibit a dynamically admissible one-fixed-solution escape mechanism (persistent Reynolds defect, motion through a steady-Euler moduli family, or true sub-core oscillation). A snapshot oscillation family alone is not enough.

**Stop rule:** if proving this compactness requires a continuation-strength hypothesis (uniform positive Sobolev/Besov control, BKM/Serrin, bounded H3, or equivalent), park the ancient/steady-Euler route instead of renaming regularity as compactness.

## Resume protocol

Read in order:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/GPT_WORKFLOW.md`;
7. `docs/LEAN_CI_OPERATIONS.md`;
8. `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`;
9. `docs/gates/DOMINANT_BALANCE_INVERSION_2026-08-19.md`;
10. the merged B2 curvature gate and the three PR-90 Gamma records;
11. `docs/gates/B2_ANCIENT_EULER_COMPACTNESS_DECISION_2026-09-06.md`;
12. the external read-only no-go registry;
13. current `main`, PR #90, the current stacked branch/PR, and latest CI.

## Claim boundary / forbidden shortcuts

Do not:

- claim Clay A/B/C/D;
- treat PR-90 or later stacked research conclusions as merged main state;
- call Euler--Reynolds an Euler solution;
- infer nonzero weak limit from a pointwise normalized maximum;
- drop the Reynolds defect without strong convergence;
- use Gavrilov/Constantin--La--Vicol steady Euler flows as NS blow-up witnesses;
- promote the conditional modulation-adjoint calculation to an unconditional B2 cut;
- reopen the killed continuous self-similar steady-front route under renamed variables;
- continue the parked Gamma-saturation route with another local escape variable;
- reopen S15/FDT without their recorded conditions;
- use numerical evidence as a continuum blow-up proof;
- add Lean plumbing merely for completeness.

The parent B2 middle limb remains OPEN. No current result proves 3D Navier--Stokes blow-up or global regularity.
