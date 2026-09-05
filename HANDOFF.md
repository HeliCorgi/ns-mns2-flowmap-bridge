# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (fortieth session).

> **Historical archive.** The full session-by-session handoff through the twenty-ninth
> session is preserved at main commit `c69315e32eead48c1fd681bf86c8bab1af815e64`
> (PR #83 merge). This live file is intentionally the short-form continuation point.
> Current theorem/source files and dated gate records override stale prose.
>
> **Sessions 30–32: ASTRA S15 traveling-max cone explored, then parked.**
> Read `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`,
> `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md`, and
> `docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md`. The conditional cone gave
> `A'>=(3/8)A^2`, but Q-UNIV was killed by remote pressure freedom and D-UNIV by
> local fourth-jet freedom. The `(q,d)` S15 realization remains **PARKED BY DEFAULT**.
>
> **Sessions 33–37: FDT regularity cross-track explored, then parked.**
> Read `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DECISION_2026-09-05.md`,
> `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`,
> `docs/gates/FDT_MAT_STRUCT_DECISION_2026-09-06.md`, and
> `docs/gates/FDT_ROUTE_PARK_DECISION_2026-09-06.md`.
> Parent `FDT-INJ` remains OPEN. `FDT-LH-OP = NO`, `FDT-LH-DYN-AFF = NO`,
> `FDT-MAT-COMM = YES`, `FDT-MAT-BRIDGE-UNIF = NO`; the remaining bridge is the
> critical low-flow deformation itself, so the FDT cross-track is **PARKED**.
>
> **2026-09-06 (thirty-eighth session): B2 GAMMA-MAX CURVATURE.**
> Record: `docs/gates/B2_GAMMA_MAX_CURVATURE_DECISION_2026-09-06.md` (merged by PR #89).
> For the actual circulation equation
>
> `(partial_t + u^r partial_r + u^z partial_z) Gamma
>   = nu (partial_r^2 - r^{-1} partial_r + partial_z^2) Gamma`,
>
> a fixed signed non-evanescent maximum satisfies a.e.
>
> **`-M_sigma'(t)=nu kappa_sigma(t)`**, hence
> **`nu int^{T*} kappa_sigma(t) dt < infinity`**.
>
> With `ell_Gamma=(M_sigma/kappa_sigma)^{1/2}`,
> **`int^{T*} ell_Gamma^{-2} dt < infinity`**. Therefore a non-evanescent Gamma maximum
> cannot maintain a tau-uniform one-scale turnover `ell_Gamma <= C tau^beta` for
> `beta>=1/2`. Decisions: `B2-GAMMA-CURVATURE-BUDGET = YES` and
> `B2-GAMMA-ONESCALE(beta>=1/2) = NO`.
>
> **2026-09-06 (thirty-ninth session): B2 GAMMA FLAT-TOP / TRANSITION ENSTROPHY.**
> Record: `docs/gates/B2_GAMMA_FLATTOP_ENSTROPHY_DECISION_2026-09-06.md`.
> The mandatory axis-to-saturation transition carries
>
> `omega^r=-Gamma_z/r`, `omega^z=Gamma_r/r`,
>
> and physical enstrophy
>
> `E_Gamma=2pi int (|Gamma_r|^2+|Gamma_z|^2)/r dr dz`.
>
> If `|Gamma(R,z)|>=m`, then
> **`int_0^R |Gamma_r|^2/r dr >= 2m^2/R^2`**; over axial length `L_z`,
> **`E_Gamma >= 4pi m^2 L_z/R^2`**. This does not kill the middle limb: for
> `L_z~R~tau^{beta_v}` the cost is `~tau^{-beta_v}` and is integrable since
> `beta_v<gamma<1`; even `L_z~tau^alpha` is integrable because
> `2 beta_v-alpha < 2 gamma-alpha < 1` from K5. Thus
> **`B2-GAMMA-FLATTOP-ENSTROPHY-KILL = NO`**.
>
> The transition nevertheless forces
> **`||omega||_infinity >= c tau^{-2 beta_v}`**, so
> **`B2-GAMMA-TRANSITION-VORTICITY = YES`**. A logarithmic-capacity flat-top snapshot
> shows that second-order flatness plus one saturation point does not imply a thick or
> expensive high-Gamma neighborhood.
>
> **2026-09-06 (fortieth session): B2 GAMMA TRANSITION-RESIDENCE STOP/GO.**
> Record: `docs/gates/B2_GAMMA_TRANSITION_RESIDENCE_DECISION_2026-09-06.md`.
>
> For a transition width `R(t)`, define the diffusive clock
>
> `D(t0,t1)=nu int_{t0}^{t1} R(s)^(-2) ds`.
>
> If `R~tau^{beta_v}` with `beta_v>=1/2`, then `D(t0,T*)=infinity`; so a fixed
> high-Gamma packet that genuinely remains confined on one `R`-scale, is not replenished,
> and has a uniform capacity/Poincare gap would suffer unlimited diffusive time. This gives
> **`B2-GAMMA-RESIDENCE-DIFFUSIVE-CLOCK = YES`**.
>
> But the frozen middle limb does not force such residence. To move `O(R)` during the
> remaining time requires only `|u^r|~R/tau~tau^{beta_v-1}`, and K11 plus
> `beta_v>alpha>=1-gamma` gives `tau^{beta_v-1}=o(tau^{-gamma})`. To outrun one local
> diffusion time requires only `|u^r|~nu/R~nu tau^{-beta_v}`, also below the Type-II
> amplitude because `beta_v<gamma`. Localized conveyor energy/dissipation costs have the
> correct sign to remain finite and even vanish with `R`.
>
> An exact nonlinear affine NS model
>
> `u^r=-a(t)r`, `u^z=2a(t)z`, `u^theta=Omega(t)r`, `Omega'=2a Omega`
>
> has `Gamma=Omega r^2`, for which `(partial_r^2-r^{-1}partial_r)Gamma=0`; along radial
> characteristics `dGamma/dt=0`. With `a=beta/tau`, material radii satisfy
> `r~tau^beta`, while the radial and swirl speeds remain compatible with the middle-limb
> Type-II envelope whenever `beta>alpha>=1-gamma` and `beta<gamma`. The affine model is
> not finite energy and is not a B2 witness; it is a mechanism-level exact-NS no-go to any
> drift-independent residence theorem.
>
> Exact decisions:
> - **`B2-GAMMA-LATE-ARRIVAL-BARRIER = NO`** from the presently controlled quantities;
> - **`B2-GAMMA-TRANSITION-RESIDENCE-KILL = NO`** as an unconditional current reduction;
> - **`B2-GAMMA-FLATTOP / RESIDENCE SUBLANE = PARKED`**.
>
> The parent Scope-B B2 middle limb remains OPEN through late-arrival/conveyor,
> max-displacement, or genuinely multiscale replenishment. Do not confuse parking this
> proof mechanism with proving the middle limb exists.

This is the durable continuation point for future GPT sessions. Do not rely on chat history.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:
1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. `docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md`;
8. `docs/gates/BH_BETAV_ENDPOINT_PINNING_2026-08-23.md`;
9. `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md`;
10. `docs/gates/B2_GAMMA_MAX_CURVATURE_DECISION_2026-09-06.md`;
11. `docs/gates/B2_GAMMA_FLATTOP_ENSTROPHY_DECISION_2026-09-06.md`;
12. `docs/gates/B2_GAMMA_TRANSITION_RESIDENCE_DECISION_2026-09-06.md`;
13. current GitHub `main`, open PRs, and relevant formal files.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, fortieth session)

- **Current state:** B2 remains the active breakdown-side lane, but the current
  flat-top/transition-residence sublane is **PARKED** by the user's stop/go rule. The diffusive clock
  diverges at `beta_v>=1/2`, yet the actual hypotheses do not force the same high-Gamma material to
  remain resident for that clock; late arrival is compatible with the frozen amplitude and finite
  energy/dissipation budgets.
- **Next distinct gate: `B2-GAMMA-MAX-DISPLACEMENT`.** Treat this as a new branch, not another
  residence repair. Allow first fixed-fraction saturation at `r_sat~tau^{beta_v}` while the true
  non-evanescent `|Gamma|` maximum sits parametrically farther out. Decide whether this necessarily
  creates an additional dynamically relevant region beyond the two-region `C+S` witness, or whether
  it remains compatible with K6/K9 location premises and the separate `L^3` carrier.
- The max-displacement gate must be **actual-PDE/geometry aware**. Repeating frozen exponent
  arithmetic is insufficient. Useful inputs may include the Gamma maximum principle, meridional
  incompressibility/flow-map geometry, and the exact locations at which K6/K9 hypotheses fire.
- **Do not continue `B2-GAMMA-TRANSITION-RESIDENCE`** by adding new exponents, static norms, or local
  capacity quantities. Reopen only for a genuinely new material-history/drift theorem, propagated
  superlevel-capacity result, or interaction forcing residence.
- **Do not call `beta_v<=1/2` a theorem.** Late-arrival, max-displacement, and multiscale escapes remain.
- **Do not use the affine model as a Clay-admissible witness.** It is infinite-energy and serves only
  as an exact-NS mechanism no-go for drift-independent residence decay.
- **Do not reopen S15 or FDT** absent their recorded reopen conditions.
- **Lean:** no new formal layer. `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.

## Repository / verification state

- Main includes merged PR #89 (session-38 curvature gate).
- Current branch / open PR: `research/b2-gamma-flattop-enstrophy`, PR #90.
- Session-39 flat-top/enstrophy first commit: `cf69c182806ee06cac692d65068e4faece036761`.
- Session-40 residence decision first commit: `2e0d71582d9d0772f1ac1ace82f9b78e8750cb95`.
- No Lean/runtime source changed in sessions 39–40; analytic docs-only frontier work.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The newest conclusion is a strategic/dynamical split:
`beta_v>=1/2` gives an infinite local diffusive clock for persistent one-scale residence, but the
actual B2 hypotheses do not force such residence, and known budgets allow late radial delivery.
Therefore the flat-top/residence proof mechanism is parked; the parent B2 middle limb remains open.
