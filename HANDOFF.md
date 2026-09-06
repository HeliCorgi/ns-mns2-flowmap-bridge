# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-sixth session)**.

This is the durable continuation point. Current theorem/source files and merged `main` control accepted state. Stacked research branches are branch-local until integrated into `main`.

## Accepted main boundary

Current accepted `main` head at this session start:

`6d70e3c9a8040d7d6e6570f0f62379fdb9b313c9`

(PR #90 merge).

Accepted formal state is unchanged: the whole-space `R^3` local actual-NS stack remains local/distributional, and the PR-92 periodic sidecar proves only a global nonzero special-family shear certificate. `ClayNS.ClayB` remains unproved. No Clay A/B/C/D statement is proved.

Latest relevant hosted verification:

- PR #92 head `198f1c68297b1d55aea0a5ea053ca2956e5bb13e`: workflow #277 PASS;
- PR #90 reconciled head `cf8ea8b0ba502223e83c03383abc4187ba1ccfe2`: workflow #278 PASS.

No Lean/runtime source changed in sessions 39–46.

## Breakdown research accepted on main

PR #89 and PR #90 are merged. The B2 Gamma-saturation microgeometry program is **PARKED** after the accepted sequence:

- Gamma-max curvature budget YES;
- one-scale `beta>=1/2` peak NO under nondegeneracy;
- flat-top enstrophy kill NO;
- transition vorticity YES;
- residence/late-arrival kill NO;
- Bessel-hitting inward-strain necessity YES;
- no new exponent cut from that strain;
- no elliptic kill from local harmonic strain.

The parent B2 middle limb remains OPEN. S15 and FDT remain parked under their own reopen conditions.

## Session 44 branch-local — ancient / steady Euler

Record:

`docs/gates/B2_ANCIENT_EULER_COMPACTNESS_DECISION_2026-09-06.md`.

For the K11 interior `gamma>alpha`, `gamma+alpha>1`, convective rescaling has vanishing normalized viscosity and diverging forward/backward normalized time horizons. Weak compactness reaches Euler--Reynolds, not automatically Euler. Broad static steady-Euler Liouville/exponent kills fail because nontrivial compact axisymmetric steady Euler flows with swirl exist.

A conditional fixed-shape adjoint obstruction was found, but it needs defect-free strong compactness, nonzero steady profile convergence, shape stationarity, and a bounded first-order expansion.

PR #93 was merged only into its stacked research base after PR #90 had already landed on `main`; treat this session-44 result as branch history unless separately integrated into `main`.

## Session 45 — modulation compactness

Record:

`docs/gates/B2_MODULATION_COMPACTNESS_DECISION_2026-09-06.md`.

Branch/PR:

- `research/b2-modulation-compactness-decision`;
- PR #94, stacked on `research/b2-ancient-euler-compactness`.

Exact dynamic normalization:

`partial_s v + (v.grad)v + grad q - (x_c'/U).grad v`
`  + delta [gamma v + alpha(y.grad)v] = eps Delta v`,

with

`delta=tau^(alpha+gamma-1)->0`,

`eps=nu tau^(gamma-alpha)->0`.

The coefficient of `partial_s v` is exactly one. Thus `gamma+alpha>1` means the fitted scale/amplitude drift is slow on the convective clock; it does **not** force shape stationarity. The general leading dynamics is unsteady Euler/Euler--Reynolds.

Decisions:

- `B2-MODULATION-SLOW-PARAMETERS = YES`;
- `B2-MODULATION-SHAPE-STATIONARITY = NO` from current B2 hypotheses;
- `B2-MODULATION-STRONG-COMPACTNESS = NO` from current B2 budgets;
- `B2-MODULATION-COMPACTNESS = NO` as the proposed unconditional reduction.

The normalized dissipation prefactor is

`1/(U ell^2) ~ tau^(gamma-2alpha)`,

which diverges throughout the frozen blob wedge because `alpha>=2gamma/3`. The high-Re limit also leaves a sub-core inertial window `1 << k << eps^(-1/2)`, so viscosity does not supply a uniform translation modulus.

A dated erratum was appended to `DOMINANT_BALANCE_INVERSION_2026-08-19.md`: K11 `gamma+alpha>=1` remains valid, but the old unconditional phrase "interior => quasi-static steady-Euler core" is withdrawn. A steady fixed shape is now only a specialization.

Strategic ruling: the chain

`B2 interior -> strong steady-Euler fixed profile -> first-order adjoint obstruction`

is **PARKED**. Reopen only for an independent one-fixed-solution cross-scale compactness theorem, a propagated shape-locking theorem, or an obstruction formulated directly for unsteady Euler--Reynolds.

## Session 46 — signed/global budget selection

Current branch:

`research/b2-signed-budget-selection`

stacked on PR #94.

Record:

`docs/gates/B2_SIGNED_BUDGET_SELECTION_2026-09-06.md`.

Selection rule: inspect exact identities of the original `R^3` axisymmetric NS solution before singular rescaling and keep a channel only if it has (i) an exact sign/finite budget, (ii) relocation resistance, (iii) a new B2 scaling cut beyond K5/Gamma microgeometry, and (iv) no continuation-strength hidden assumption.

Audited channels:

- total kinetic energy: exact, but duplicate K5;
- swirl/poloidal component-energy exchange: exact but only signed; positive variation not controlled and co-location can fail;
- finite-`p` circulation entropies: exact monotone identities
  `(1/p)d/dt int |Gamma|^p r dr dz + nu(p-1) int |Gamma|^(p-2)|grad Gamma|^2 r dr dz = 0`,
  but fixed-amplitude circulation near the axis is too cheap in the weighted measure to cut the B2 wedge;
- axial angular momentum: conserved, but may vanish and a collapsing core contributes vanishingly, allowing a remote carrier;
- helicity: exact evolution but no sign;
- enstrophy/palinstrophy: vortex-stretching sign wall / continuation-level;
- `q=u^theta/r` and `eta=omega^theta/r`: source-sign failure, already adjacent to audited critical criteria;
- linear momentum / impulse-type moments: conserved signed but may vanish and allow remote carriers.

Decision:

**`B2-SIGNED-BUDGET-SELECTION = NO-CHANNEL`** among the standard exact identities audited.

This is an inventory result, not a theorem that no useful NS functional can exist.

## Strategic state after session 46

Three analytic mechanism classes have now been exhausted without an unconditional middle-limb kill:

1. local Gamma microgeometry / residence / hitting;
2. ancient/steady-Euler fixed-profile compactness and modulation;
3. standard exact global/signed invariants.

This is a genuine stop signal. Do not continue by adding another local scale, elementary conserved moment, or standard norm.

## Next work

There is no automatic next analytic theorem in the current in-house inventory.

A new analytic lane should open only if it brings one genuinely new ingredient:

- a nonstandard exact signed functional with a proved NS evolution law and new B2 scaling interaction;
- a one-fixed-solution cross-scale theorem coupling distant regions/times;
- a new external theorem below continuation strength that intersects the frozen B2 wedge;
- or a computer-assisted continuum argument tied to an explicit admissible candidate.

Absent one of those, the two rational project moves are:

1. return to the numerical candidate/M-1 infrastructure under `SPEC.md` and its fail-closed validation rules; or
2. run a **bounded literature watch** specifically for new post-2026 axisymmetric-with-swirl / Type-II / critical-drift results that satisfy the reopen criteria above.

Do not open another theorem-shaped analytic branch merely to rename one of the exhausted walls.

## Resume protocol

At substantive resume read:

1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this `HANDOFF.md`;
6. `docs/GPT_WORKFLOW.md`;
7. `docs/LEAN_CI_OPERATIONS.md`;
8. `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`;
9. `docs/gates/DOMINANT_BALANCE_INVERSION_2026-08-19.md` including the 2026-09-06 erratum;
10. merged B2 Gamma records;
11. `docs/gates/B2_ANCIENT_EULER_COMPACTNESS_DECISION_2026-09-06.md`;
12. `docs/gates/B2_MODULATION_COMPACTNESS_DECISION_2026-09-06.md`;
13. `docs/gates/B2_SIGNED_BUDGET_SELECTION_2026-09-06.md`;
14. the external read-only no-go registry;
15. current `main`, open/stacked PRs, and latest CI.

## Claim boundary / forbidden shortcuts

Do not:

- claim Clay A/B/C/D;
- claim the B2 middle limb is excluded or realized;
- treat Euler--Reynolds as Euler;
- infer shape stationarity from `gamma+alpha>1`;
- infer strong compactness from finite dissipation after singular normalization;
- promote the conditional steady-profile adjoint calculation to an unconditional cut;
- treat `NO-CHANNEL` as proof that no useful invariant exists;
- reopen Gamma-saturation, S15, FDT, or fixed-profile ancient-Euler without their recorded triggers;
- use a periodic/infinite-energy mechanism model as an `R^3` Clay witness;
- use numerical evidence as a continuum blow-up proof;
- add Lean plumbing merely for completeness.

No current result proves 3D Navier--Stokes blow-up or global regularity.
