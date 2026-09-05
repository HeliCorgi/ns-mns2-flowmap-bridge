# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (thirty-seventh session).

> **Historical archive.** The full session-by-session handoff through the twenty-ninth
> session is preserved at main commit `c69315e32eead48c1fd681bf86c8bab1af815e64`
> (PR #83 merge). This live file is intentionally the short-form continuation point.
> Current theorem/source files and dated gate records override stale prose.

> **Sessions 30–32: ASTRA S15 traveling-max cone explored, then parked.**
> Read `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`,
> `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md`, and
> `docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md`. The conditional cone gave
> `A'>=(3/8)A^2`, but Q-UNIV was killed by remote pressure freedom and D-UNIV by
> local fourth-jet freedom. The `(q,d)` S15 realization remains **PARKED BY DEFAULT**.

> **Sessions 33–36: FDT regularity cross-track explored.**
> Read, in order:
> `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`, and
> `docs/gates/FDT_MAT_STRUCT_DECISION_2026-09-06.md`.
>
> Parent `FDT-INJ` asks for a datum-dependent high-frequency cutoff above which the
> signed one-viscous-window Eulerian nonlinear Duhamel injection has a fixed critical
> margin. A YES would imply bounded dissipation wavenumber and then a known
> Cheskidov–Shvydkoy continuation criterion. Parent `FDT-INJ` remains **OPEN**.
>
> The static energy shortcut was killed. `FDT-LH-OP = NO`: a real divergence-free
> Schwartz packet family has a subcritical target block and arbitrarily small ordinary
> energy / one-window enstrophy but arbitrarily large normalized frozen LH commutator.
> This does not refute parent FDT-INJ because the datum changes with the active scale.
>
> `FDT-LH-DYN-AFF = NO`: in an exact trace-free affine-strain + transverse-shear NS
> model, the signed low-flow-conjugated LH commutator telescopes to an order-one LP
> multiplier boundary displacement. Large LH is benign shell transport/frequency
> relabeling, not high-mode self-amplification. The affine background is not finite
> energy, so this is a model no-go rather than an admissible R3 counterexample.
>
> `FDT-MAT-COMM = YES`: the canonical material projector
> `Delta_j^mat=U_j^(-1) Delta_j U_j` commutes exactly with the principal low transport.
> But exact commutation deforms dyadic annuli. In affine strain the material/Eulerian
> shell distortion over one viscous window is `exp(sigma a_*)`, arbitrarily large.
> Hence `FDT-MAT-BRIDGE-UNIF = NO` and `FDT-MAT-STRUCT = NO as stated`. A componentwise
> pullback also loses divergence preservation, while Piola transport restores
> divergence at the cost of an explicit `(grad v)w` deformation term.

> **2026-09-06 (thirty-seventh session): FDT ROUTE PARK DECISION.**
> Record: `docs/gates/FDT_ROUTE_PARK_DECISION_2026-09-06.md` on branch
> `research/fdt-mat-struct-decision`, PR #88.
>
> The remaining proposed gate `FDT-DEF-BUDGET` was evaluated as a reduction rather
> than falsely declared solved. For the low flow `X_j`, shell comparison requires
> control of `DX_j` and `DX_j^(-1)` (equivalently Cauchy–Green distortion). The
> deterministic bound is schematically
>
> `K_j(t,s) <= exp(int_s^t ||grad u_{<=j-2}||_infinity)`.
>
> The one-viscous-window strain/deformation quantity is scale-critical under NS
> scaling, while energy and total dissipation are supercritical. Thus it is not a
> small consequence of the already-controlled budgets. Mere finiteness on compact
> subintervals of a smooth lifespan is useless; to close continuation one needs a
> uniform bound up to a potential first singular time and across relevant high scales.
> That is itself a new critical deformation regularity theorem.
>
> Therefore the exact status is:
>
> - `FDT-DEF-BUDGET` on Clay-admissible R3 data: **OPEN**, not disproved;
> - `FDT-DEF-BUDGET-AS-INDEPENDENT-REDUCTION`: **FAIL** for the present chain;
> - current FDT regularity cross-track: **PARKED**.
>
> Reopen only if a genuinely new deformation theorem, a material continuation theorem
> not hiding the same strain control, an admissible full-term cancellation identity,
> or a relevant external result changes the frontier. Do not add LP/Bony/Piola/
> paracomposition Lean plumbing while the route is parked.

This is the durable continuation point for future GPT sessions. Do not rely on chat history.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:
1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. `docs/gates/FDT_ROUTE_PARK_DECISION_2026-09-06.md` if reviewing the parked FDT lane;
8. for the next active research lane, `docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md`;
9. `docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`;
10. the latest breakdown-side kill table / readiness audit referenced by Stage 9;
11. current GitHub `main`, open PRs, and relevant formal files.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, thirty-seventh session)

- **Current state:** the FDT regularity cross-track is **PARKED**. Parent `FDT-INJ`
  remains mathematically OPEN; do not call it false. The park decision is strategic:
  the only remaining bridge is the critical low-flow deformation itself, and the
  present chain provides no independent budget for it.
- **Return to the repository's declared main breakdown-side priority.** Re-read
  `SPEC.md`, `STAGE9_DECISION_SELECTION_2026-08-23.md`,
  `BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`, and the latest Type-II / B2 kill table.
- **Next research-selection rule:** choose one actual-NS dynamical decision beyond the
  already-settled scope-free exponent arithmetic. The prior `beta_v` middle-limb
  arithmetic consistency certificate is not enough; the next object must use pressure,
  viscosity, transport, vorticity/strain, or another actual PDE constraint.
- **Do not reopen S15 `(q,d)`** unless one propagated structure simultaneously excludes
  both the remote-pressure Q counterfamily and the local fourth-jet D counterfamily.
- **Do not reopen FDT** unless one of the explicit reopen conditions in
  `FDT_ROUTE_PARK_DECISION_2026-09-06.md` is met.
- **Lean:** no new FDT-specific formalization. `FORMAL_SCOPE.md` and `STATUS.md` remain
  unchanged because the formal frontier did not move.

## Repository / verification state

- `main` at start of session 37: `9f8e3f94ab7baaeb6659e937ab8e019797cbf531`
  (merged PR #87).
- Current branch / PR: `research/fdt-mat-struct-decision`, PR #88.
- Session-36 material-structure record first commit:
  `0d16a5c1cc5a6c3d7aee99caefb4bef9e9812bba`.
- Session-37 FDT park record first commit:
  `88b55f91f148185fb93be894571ee41d2f518738`.
- No Lean/runtime source changed in sessions 36–37; `FORMAL_SCOPE.md` and `STATUS.md`
  intentionally remain unchanged.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**. PR #88 workflow
  runs are docs-only integration/status checks.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The newest result is a strategic negative conclusion:
the current FDT chain has reduced its missing input to scale-critical low-flow deformation, but has
not independently controlled that quantity. The route is parked to avoid relabeling the original
regularity problem as a deformation-budget lemma.
