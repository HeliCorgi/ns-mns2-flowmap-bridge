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
> Read, in order: `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`, and
> `docs/gates/FDT_MAT_STRUCT_DECISION_2026-09-06.md`.
>
> Parent `FDT-INJ` remains **OPEN**. The static energy shortcut was killed.
> `FDT-LH-OP = NO`; `FDT-LH-DYN-AFF = NO`; `FDT-MAT-COMM = YES`; and
> `FDT-MAT-BRIDGE-UNIF = NO`, hence `FDT-MAT-STRUCT = NO as stated`.
> Fixed Eulerian LH overcounts benign shell transport; exact material shells absorb that transport
> but become geometrically distorted, so comparison back to fixed Eulerian shells requires low-flow
> deformation control.

> **2026-09-06 (thirty-seventh session): FDT ROUTE PARK DECISION.**
> Record: `docs/gates/FDT_ROUTE_PARK_DECISION_2026-09-06.md` on `main`.
>
> The remaining proposed gate `FDT-DEF-BUDGET` was evaluated as a reduction rather than falsely
> declared solved. For the low flow `X_j`, material/Eulerian shell comparison requires control of
> `DX_j` and `DX_j^{-1}` (equivalently Cauchy–Green distortion). The deterministic bound is
> schematically
>
> `K_j(t,s) <= exp(int_s^t ||grad u_{<=j-2}||_infinity)`.
>
> The one-viscous-window deformation quantity is scale-critical under NS scaling, while energy and
> total dissipation are supercritical. Mere finiteness on compact subintervals of a smooth lifespan
> is useless; continuation needs a bound uniform up to a possible first singular time and across the
> relevant high scales. That is itself a new critical deformation regularity theorem.
>
> Exact status:
> - `FDT-DEF-BUDGET` on Clay-admissible `R^3` data: **OPEN**, not disproved;
> - `FDT-DEF-BUDGET-AS-INDEPENDENT-REDUCTION`: **FAIL** for the present chain;
> - current FDT regularity cross-track: **PARKED**.
>
> Reopen only for a genuinely new independent deformation theorem, a new material continuation
> theorem that does not hide the same strain control, an admissible full-term cancellation identity,
> or an external result that changes the frontier. Do not add FDT-specific LP/Bony/Piola/
> paracomposition Lean plumbing while parked.

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
8. `docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md`;
9. `docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`;
10. the latest breakdown-side kill table / readiness audit referenced there;
11. current GitHub `main`, open PRs, and relevant formal files.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, thirty-seventh session)

- **Current state:** the FDT regularity cross-track is **PARKED**. Parent `FDT-INJ` remains
  mathematically OPEN; do not call it false. The park decision is strategic: the only remaining
  bridge is the critical low-flow deformation itself, and the present chain provides no independent
  budget for it.
- **Return to the repository's declared main breakdown-side priority.** Re-read `SPEC.md`,
  `STAGE9_DECISION_SELECTION_2026-08-23.md`, `BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`, and the
  latest Type-II / B2 kill table.
- **Next research-selection rule:** choose one actual-NS dynamical decision beyond the already-settled
  scope-free exponent arithmetic. The prior `beta_v` middle-limb arithmetic consistency certificate
  is not enough; the next object must use pressure, viscosity, transport, vorticity/strain, or another
  actual PDE constraint.
- **Do not reopen S15 `(q,d)`** unless one propagated structure simultaneously excludes both the
  remote-pressure Q counterfamily and the local fourth-jet D counterfamily.
- **Do not reopen FDT** unless one of the explicit reopen conditions in
  `FDT_ROUTE_PARK_DECISION_2026-09-06.md` is met.
- **Lean:** no new FDT-specific formalization. `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.

## Repository / verification state

- `main` includes merged PR #88 material-structure work plus session-37 direct docs commits.
- Session-37 park record commit: `c175707448b4336c950cd89c0efc94032565704f`.
- No Lean/runtime source changed in session 37; `FORMAL_SCOPE.md` and `STATUS.md` remain intentionally
  unchanged.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**. Session-37 changes are docs-only.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The newest result is a strategic negative conclusion: the
current FDT chain has reduced its missing input to scale-critical low-flow deformation, but has not
independently controlled that quantity. The route is parked to avoid relabeling the original
regularity problem as a deformation-budget lemma.
