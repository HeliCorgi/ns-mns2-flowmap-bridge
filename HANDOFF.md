# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (thirty-eighth session).

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

> **Sessions 33–37: FDT regularity cross-track explored, then parked.**
> Read `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`,
> `docs/gates/FDT_MAT_STRUCT_DECISION_2026-09-06.md`, and
> `docs/gates/FDT_ROUTE_PARK_DECISION_2026-09-06.md`.
>
> Parent `FDT-INJ` remains OPEN. Static energy closure failed; `FDT-LH-OP = NO`;
> `FDT-LH-DYN-AFF = NO`; `FDT-MAT-COMM = YES`; `FDT-MAT-BRIDGE-UNIF = NO`.
> The remaining material/Eulerian bridge is the critical low-flow deformation itself, so
> `FDT-DEF-BUDGET-AS-INDEPENDENT-REDUCTION = FAIL` and the FDT cross-track is **PARKED**.

> **2026-09-06 (thirty-eighth session): BREAKDOWN SIDE REOPENED — B2 GAMMA-MAX CURVATURE.**
> Record: `docs/gates/B2_GAMMA_MAX_CURVATURE_DECISION_2026-09-06.md` on branch
> `research/b2-gamma-curvature-gate`.
>
> Re-read `SPEC.md`, `STAGE9_DECISION_SELECTION_2026-08-23.md`,
> `BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`, and `TYPE2_KILL_TABLE_2026-08-19.md`.
> The Stage-9 arithmetic result `YES (CONSISTENT)` is retained: frozen rows alone do not pin
> `beta_v`. The new pass uses the actual circulation PDE
>
> `(partial_t + u^r partial_r + u^z partial_z) Gamma
>   = nu (partial_r^2 - r^{-1} partial_r + partial_z^2) Gamma`.
>
> For the signed maxima `M_sigma(t)=sup sigma Gamma`, choose the fixed sign whose monotone
> limit stays positive under B2 non-evanescence. At active nonzero maximizers the advection,
> `Gamma_r`, `Gamma_z`, and the `-r^{-1}Gamma_r` term vanish. Defining
>
> `kappa_sigma(t)=min_Argmax [-(partial_r^2+partial_z^2)(sigma Gamma)]`,
>
> the maximum-envelope identity gives, a.e.,
>
> **`-M_sigma'(t)=nu kappa_sigma(t)`**,
>
> hence the exact finite curvature budget
>
> **`nu int^{T*} kappa_sigma(t) dt < infinity`.**
>
> With curvature length `ell_Gamma=(M_sigma/kappa_sigma)^{1/2}`, B2 non-evanescence implies
>
> **`int^{T*} ell_Gamma(t)^{-2} dt < infinity`.**
>
> Therefore a non-evanescent Gamma maximum with a tau-uniform one-scale turnover
> `ell_Gamma <= C tau^beta` is impossible for `beta>=1/2` (log divergence at equality).
> Exact decisions:
>
> - **`B2-GAMMA-CURVATURE-BUDGET = YES`;**
> - **`B2-GAMMA-ONESCALE(beta>=1/2) = NO`.**
>
> This dynamically audits the Stage-9 witness
> `(gamma,alpha,beta_v)=(3/5,9/20,1/2)`: its synthetic `Gamma` profile remains a valid
> frozen-row consistency certificate, but any smoothing with a uniformly comparable turnover width
> would have curvature `~Gamma0/tau` and would force logarithmically infinite maximum loss.
> Therefore it is **not an actual-NS witness in that one-scale form**.
>
> The full middle limb is NOT killed. For `beta_v>=1/2` it must escape by at least one of:
> curvature depletion / flat-top formation; displacement of the true non-evanescent Gamma maximum
> away from the first saturation radius; or a genuinely multiscale turnover. In particular, because
> `alpha>=1/2` throughout the frozen blob wedge for `gamma>=3/4`, every high-gamma middle-limb
> realization is forced into one of those escape structures.

This is the durable continuation point for future GPT sessions. Do not rely on chat history.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:
1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. `docs/gates/FDT_ROUTE_PARK_DECISION_2026-09-06.md` only if reviewing the parked FDT lane;
8. `docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md`;
9. `docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`;
10. `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`;
11. `docs/gates/B2_GAMMA_MAX_CURVATURE_DECISION_2026-09-06.md`;
12. current GitHub `main`, open PRs, and relevant formal files.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, thirty-eighth session)

- **Current state:** breakdown-side B2 is again the active research lane. Frozen arithmetic still
  says the middle limb is consistent, but actual Gamma dynamics has now killed its simplest
  nondegenerate one-scale realization at `beta_v>=1/2`.
- **Next gate: `B2-GAMMA-FLATTOP`.** Attack the surviving curvature-depletion branch
  counterexample-first. Do not introduce a new power exponent unless forced. Use the exact curvature
  length `ell_Gamma` and ask whether a neighborhood-scale flat-top can coexist with finite physical
  enstrophy/dissipation and the separate `L^3` carrier.
- **Parallel branch to audit if flat-top survives:** `B2-GAMMA-MAX-DISPLACEMENT`. Allow fixed-fraction
  saturation at `r_sat` while the true non-evanescent `|Gamma|` maximum sits parametrically farther
  out. Decide whether this forces an additional region beyond the two-region `C + S` witness or
  collides with K6/K9 location bookkeeping.
- **Do not call `beta_v<=1/2` a theorem.** The curvature gate only proves that a Gamma maximum cannot
  have a uniformly nondegenerate turnover on scale `tau^beta` for `beta>=1/2`. Flat-top and
  max-displacement escapes remain open.
- **Do not use the Stage-9 `W★` synthetic profile as an actual PDE trajectory.** Its role after this
  session is arithmetic consistency only unless a curvature-depleted/multiscale smoothing is built.
- **Do not reopen S15 or FDT** absent their recorded reopen conditions.
- **Lean:** no new formal layer yet. The new result depends on the pointwise Gamma PDE and
  maximum-envelope/Dini machinery not present in the current formal stack. `FORMAL_SCOPE.md` and
  `STATUS.md` remain unchanged.

## Repository / verification state

- Branch: `research/b2-gamma-curvature-gate` from current `main`.
- New gate record first commit: `bafdfe48ed0fd66cc585e708c89271907d6ee073`.
- No Lean/runtime source changed in session 38; this is an analytic docs-only frontier move.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The newest result is a pressure-free actual-NS dynamical
restriction on the B2 circulation maximum: non-evanescent Gamma cannot maintain a one-scale
nondegenerate peak at or below the diffusive length exponent `1/2`. The full middle limb remains
open through flat-top, max-displacement, or multiscale escape geometries.
