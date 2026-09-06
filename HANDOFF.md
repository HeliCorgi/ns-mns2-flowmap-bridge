# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: **2026-09-06 JST (forty-fifth session)**.

This is the durable short-form continuation point. Current theorem/source files and merged `main` control accepted state. Stacked research branches are not accepted `main` state until integrated there.

## Accepted main boundary

Current accepted `main` head at this session start:

`6d70e3c9a8040d7d6e6570f0f62379fdb9b313c9`

(PR #90 merge).

Accepted formal state includes the PR-92 periodic sidecar and the pre-existing whole-space `R^3` local actual-NS stack. The periodic anchors include `ClayNS.certified_nonzero_periodic_NS` and `ClayNS.clayB_has_nonzero_smooth_specialization`; the universal proposition `ClayNS.ClayB` remains **unproved**. The whole-space anchors remain `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and `MNS2.r3EndpointSafeProjectedMild_navierStokes`; that result is local/distributional, not global regularity.

PR #92 head `198f1c68297b1d55aea0a5ea053ca2956e5bb13e` passed hosted Lean workflow #277 (`33996261541`). PR #90 reconciled head `cf8ea8b0ba502223e83c03383abc4187ba1ccfe2` passed hosted workflow #278 (`33998128794`). No Lean/runtime source changed in sessions 39–45.

## Breakdown research accepted on main

PR #89 plus PR #90 are now merged on `main`.

The accepted B2 Gamma results include:

- `B2-GAMMA-CURVATURE-BUDGET = YES`;
- one-scale `B2-GAMMA-ONESCALE(beta>=1/2) = NO` under its stated nondegeneracy;
- `B2-GAMMA-FLATTOP-ENSTROPHY-KILL = NO`;
- `B2-GAMMA-TRANSITION-VORTICITY = YES`;
- `B2-GAMMA-LATE-ARRIVAL-BARRIER = NO`;
- `B2-GAMMA-TRANSITION-RESIDENCE-KILL = NO`;
- `B2-GAMMA-HITTING-STRAIN = YES`;
- `B2-GAMMA-HITTING-NEW-EXPONENT-CUT = NO`;
- `B2-GAMMA-STRAIN-ELLIPTIC-KILL = NO`;
- `B2-GAMMA-SATURATION-MICROGEOMETRY = PARKED`.

The parent B2 middle limb remains OPEN. S15 and FDT remain parked under their recorded reopen rules.

## Session 44 branch-local result — ancient / steady Euler

PR #93 was merged into its stacked base branch `research/b2-gamma-flattop-enstrophy` **after** PR #90 had already been merged to `main`; therefore the session-44 file is branch history, not automatically accepted main history.

Record:

`docs/gates/B2_ANCIENT_EULER_COMPACTNESS_DECISION_2026-09-06.md`.

For the K11 interior `gamma>alpha`, `gamma+alpha>1`, the convective scaling has

`eps_n = nu/(U_n ell_n) -> 0`

and both normalized time horizons diverge. Under local normalized `L^infinity` tightness, weak compactness reaches Euler--Reynolds, not automatically Euler. Static steady-Euler Liouville/exponent kills fail broadly because nontrivial compact axisymmetric steady Euler flows with swirl exist.

The session also found the conditional fixed-shape adjoint identity:

`<V,L_V w>=0`,

`<V,D_{gamma,alpha}V>=(gamma-3alpha/2)||V||_2^2`,

`<V,-Delta V>=||grad V||_2^2`.

It gives a first-order obstruction **only if** defect-free strong compactness, a nonzero steady profile, shape stationarity, and a bounded first-order expansion are independently justified.

## Session 45 — B2 modulation compactness decision

Current branch:

`research/b2-modulation-compactness-decision`

based on `research/b2-ancient-euler-compactness`.

New record:

`docs/gates/B2_MODULATION_COMPACTNESS_DECISION_2026-09-06.md`.

### Exact dynamic normalization

With

`U=tau^(-gamma)`, `ell=tau^alpha`, `ds/dt=U/ell`,

`u(x,t)=U(t)v((x-x_c(t))/ell(t),s)`,

the exact normalized equation is

`partial_s v + (v.grad)v + grad q - (x_c'/U).grad v`
`  + delta [gamma v + alpha(y.grad)v] = eps Delta v`,

where

`delta=tau^(alpha+gamma-1)->0`,

`eps=nu tau^(gamma-alpha)->0`.

The coefficient of `partial_s v` is **exactly one**. Thus `gamma+alpha>1` makes the fitted amplitude/scale drift slow on the convective clock; it does **not** force the normalized shape to be stationary. The general leading equation is unsteady Euler (or Euler--Reynolds after only weak compactness), not steady Euler.

Decisions:

- **`B2-MODULATION-SLOW-PARAMETERS = YES`;**
- **`B2-MODULATION-SHAPE-STATIONARITY = NO` from current B2 hypotheses.**

This corrects an overstatement in `DOMINANT_BALANCE_INVERSION_2026-08-19.md`: the K11 cut `gamma+alpha>=1` remains valid, but the old unconditional phrase "interior => quasi-static steady-Euler core" is withdrawn. An explicit dated erratum was appended; no silent repair was made.

### Strong compactness audit

For a normalized cylinder,

`int |grad_y v_n|^2 ~ (1/(U_n ell_n^2)) int |grad_x u|^2`,

with

`1/(U_n ell_n^2) ~ tau_n^(gamma-2alpha)`.

Since the frozen blob wedge has `alpha>=2gamma/3`, this prefactor diverges. Finite physical dissipation gives no rate that produces a uniform positive normalized regularity/translation modulus. The normalized viscous length is `sqrt(eps_n)`, leaving a growing inertial band

`1 << k_n << eps_n^(-1/2)`

where `eps_n k_n^2->0` and sub-core oscillations can survive a convective window.

An exact periodic NS shear family is recorded only as a mechanism test: bounded vanishing-viscosity solutions can weakly converge while retaining a nonzero quadratic defect. It is **not** an `R^3` axisymmetric B2 witness. The earlier axisymmetric snapshot counterprofile separately shows symmetry alone does not supply compactness.

Decisions:

- **`B2-MODULATION-STRONG-COMPACTNESS = NO` from current B2 budgets;**
- **`B2-MODULATION-COMPACTNESS = NO` as the proposed unconditional reduction.**

The energy pairing of the dynamic equation merely rewrites the physical energy equality and reproduces the K5 `alpha>=2gamma/3` threshold; it gives no hidden stationarity or defect-killing budget.

### Strategic ruling

The chain

`B2 interior -> strong steady-Euler fixed profile -> first-order adjoint obstruction`

is **PARKED**.

The session-44 adjoint identity remains a valid conditional specialization test. Reopen this lane only for a genuinely independent one-fixed-solution cross-scale compactness theorem, a propagated shape-locking theorem, or an obstruction formulated directly at the unsteady Euler--Reynolds level.

Do **not** introduce a positive Sobolev/Besov/BKM/Serrin/H3 assumption and rename it "compactness".

## Next work

Run one bounded selection pass:

**`B2-SIGNED-BUDGET-SELECTION`**.

Goal: inspect exact global/signed identities of the original `R^3` axisymmetric NS solution **before any singular rescaling** and select at most one new theorem-shaped gate. Candidate channels may include component-energy exchange, global circulation/weighted-circulation entropies, angular momentum, helicity-type balances, or another exact signed quantity.

Selection requirements:

1. exact actual-NS identity/inequality on the current `SPEC.md` domain/data class;
2. sign/monotonicity or finite total budget that survives relocation of the bad set;
3. nontrivial scaling interaction with the B2 wedge beyond existing K5 energy/dissipation and the parked Gamma-saturation microgeometry;
4. not a continuation criterion in disguise.

If no candidate passes all four tests, record `NO-CHANNEL` and do not open another local-geometry escape branch.

## Resume protocol

Read in order:

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
11. `docs/gates/B2_ANCIENT_EULER_COMPACTNESS_DECISION_2026-09-06.md` on the stacked history;
12. `docs/gates/B2_MODULATION_COMPACTNESS_DECISION_2026-09-06.md`;
13. the external read-only no-go registry;
14. current `main`, current research branch/PR, and latest CI.

## Claim boundary / forbidden shortcuts

Do not:

- claim Clay A/B/C/D;
- claim the parent B2 middle limb is excluded or realized;
- treat Euler--Reynolds as Euler;
- infer shape stationarity from `gamma+alpha>1`;
- infer strong compactness from finite physical dissipation after the singular normalization;
- promote the conditional steady-profile adjoint calculation to an unconditional cut;
- reopen the parked Gamma-saturation, S15, FDT, or fixed-profile ancient-Euler lanes without their recorded reopen conditions;
- use the periodic shear mechanism as an `R^3` B2 witness;
- use numerical evidence as a continuum blow-up proof;
- add Lean plumbing merely for completeness.

No current result proves 3D Navier--Stokes blow-up or global regularity.
