# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (thirty-ninth session).

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
>
> Parent `FDT-INJ` remains OPEN. Static energy closure failed; `FDT-LH-OP = NO`;
> `FDT-LH-DYN-AFF = NO`; `FDT-MAT-COMM = YES`; `FDT-MAT-BRIDGE-UNIF = NO`.
> The remaining material/Eulerian bridge is the critical low-flow deformation itself, so
> `FDT-DEF-BUDGET-AS-INDEPENDENT-REDUCTION = FAIL` and the FDT cross-track is **PARKED**.
>
> **2026-09-06 (thirty-eighth session): BREAKDOWN SIDE REOPENED — B2 GAMMA-MAX CURVATURE.**
> Record: `docs/gates/B2_GAMMA_MAX_CURVATURE_DECISION_2026-09-06.md` on branch
> `research/b2-gamma-curvature-gate`.
>
> For the actual axisymmetric circulation equation
>
> `(partial_t + u^r partial_r + u^z partial_z) Gamma
>   = nu (partial_r^2 - r^{-1} partial_r + partial_z^2) Gamma`,
>
> a fixed signed non-evanescent maximum satisfies, a.e.,
>
> **`-M_sigma'(t)=nu kappa_sigma(t)`**,
>
> where `kappa_sigma` is the least nonnegative transverse curvature among active maximizers.
> Hence
>
> **`nu int^{T*} kappa_sigma(t) dt < infinity`**
>
> and, with `ell_Gamma=(M_sigma/kappa_sigma)^{1/2}`,
>
> **`int^{T*} ell_Gamma^{-2} dt < infinity`.**
>
> Therefore a non-evanescent Gamma maximum cannot maintain a tau-uniform one-scale turnover
> `ell_Gamma <= C tau^beta` for `beta>=1/2`. Decisions:
>
> - `B2-GAMMA-CURVATURE-BUDGET = YES`;
> - `B2-GAMMA-ONESCALE(beta>=1/2) = NO`.
>
> The Stage-9 arithmetic witness `(gamma,alpha,beta_v)=(3/5,9/20,1/2)` remains a frozen-row
> consistency certificate but is not an actual-NS witness with a uniformly comparable smooth
> Gamma-turnover width.
>
> **2026-09-06 (thirty-ninth session): B2 GAMMA FLAT-TOP / TRANSITION ENSTROPHY AUDIT.**
> Record: `docs/gates/B2_GAMMA_FLATTOP_ENSTROPHY_DECISION_2026-09-06.md` on the same branch.
>
> The mandatory axis-to-saturation transition has exact swirl-generated poloidal vorticity
>
> `omega^r = -Gamma_z/r`, `omega^z = Gamma_r/r`,
>
> so its physical enstrophy contribution is
>
> `E_Gamma = 2pi int (|Gamma_r|^2+|Gamma_z|^2)/r dr dz`.
>
> If `|Gamma(R,z)|>=m` then the radial line inequality gives
>
> **`int_0^R |Gamma_r|^2/r dr >= 2m^2/R^2`.**
>
> If this saturation persists over axial length `L_z`, then
>
> **`E_Gamma >= 4pi m^2 L_z/R^2`.**
>
> This does **not** kill the middle limb. For `L_z~R~tau^{beta_v}` the cost is only
> `~tau^{-beta_v}`, time-integrable because `beta_v<gamma<1`. Even under the stronger
> `L_z~tau^alpha` core-sheet hypothesis, the cost `~tau^{alpha-2 beta_v}` is integrable because
>
> **`2 beta_v-alpha < 2 gamma-alpha < 1`**
>
> from the frozen strict K5/dissipation inequality `alpha>2gamma-1`.
>
> Thus **`B2-GAMMA-FLATTOP-ENSTROPHY-KILL = NO`**: the standard finite physical dissipation budget
> produces no new exponent cut beyond K5.
>
> The transition does force pointwise vorticity. By the mean-value theorem, some point inside the
> radial transition obeys
>
> **`|omega^z| >= m/R^2`, hence `||omega||_infinity >= c tau^{-2 beta_v}`.**
>
> Thus **`B2-GAMMA-TRANSITION-VORTICITY = YES`**. For `beta_v>=1/2` this is already non-integrable
> in time, which is compatible with a breakdown trajectory rather than contradictory.
>
> Pointwise curvature depletion also does not imply a thick high-Gamma neighborhood. A smooth
> logarithmic-capacity flat-top profile centered at radius `R`, with plateau radius `a`, outer scale
> `L<R/4`, and logarithmic transition, has weighted Dirichlet/enstrophy cost
>
> **`<= C M^2/[R log(L/a)]`**
>
> while fixed-fraction saturation stays at radius comparable to `R`. Taking the pure-swirl field
> `u^theta=Gamma/r` gives a real divergence-free `C_c^infinity(R^3)` instantaneous datum. This is
> not a B2 singular trajectory; it falsifies any universal instantaneous claim that `r_sat` plus
> second-order flatness alone forces a thick or expensive transition.
>
> The full vorticity-production identity does not repair the kill with known budgets: palinstrophy
> and the stretching source have no independent finite/sign-definite budget up to a hypothetical
> singular time. A production-based kill would therefore require genuinely new PDE control.

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
12. current GitHub `main`, open PRs, and relevant formal files.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, thirty-ninth session)

- **Current state:** breakdown-side B2 remains active. Frozen arithmetic does not pin `beta_v`.
  Actual Gamma dynamics kills a nondegenerate one-scale maximum turnover at `beta_v>=1/2`, but the
  flat-top escape is **not** killed by physical `L^2` enstrophy/dissipation. Instead the required
  axis-to-saturation transition carries large off-maximum vorticity `~r_sat^{-2}`.
- **Next gate: `B2-GAMMA-TRANSITION-RESIDENCE`.** Use the actual scalar Gamma advection-diffusion
  equation to ask whether high-Gamma material can be delivered to `R(t)~tau^{beta_v}` and remain
  non-evanescent despite diffusion across the mandatory transition. Distinguish **late arrival** from
  residence for `~tau` time; a static enstrophy estimate cannot make this distinction.
- The residence gate must use actual drift/flow geometry. It is invalid to assume a bound equivalent
  to a continuation criterion merely to control the meridional flow.
- **Parallel fallback:** `B2-GAMMA-MAX-DISPLACEMENT`. If high-Gamma material can always arrive late,
  allow first fixed-fraction saturation at `r_sat` while the true non-evanescent maximum lies farther
  out; audit whether this creates a genuinely new region or collides with K6/K9 location premises.
- **Do not infer superlevel thickness from maximum curvature.** The logarithmic-capacity snapshot
  demonstrates that second-order flatness plus one saturation point does not supply such thickness.
- **Do not call `beta_v<=1/2` a theorem.** Flat-top, late-arrival, max-displacement, and multiscale
  escapes remain open.
- **Do not reopen S15 or FDT** absent their recorded reopen conditions.
- **Lean:** no new formal layer yet. The formal frontier did not move; `FORMAL_SCOPE.md` and
  `STATUS.md` remain unchanged.

## Repository / verification state

- Branch / PR: `research/b2-gamma-curvature-gate`, PR #89.
- Session-38 curvature record first commit: `bafdfe48ed0fd66cc585e708c89271907d6ee073`.
- Session-39 flat-top/enstrophy record first commit: `fe86ce32235ac24c86bc48cdc445d3961eaaa6ee`.
- No Lean/runtime source changed in sessions 38–39; both are analytic docs-only frontier work.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The current breakdown-side refinement says: a
non-evanescent Gamma maximum cannot maintain a one-scale nondegenerate turnover at exponent
`>=1/2`; flattening that maximum shifts the cost into an off-maximum swirl-gradient/vorticity layer,
but the standard finite physical enstrophy budget is too weak to exclude that layer throughout the
frozen B2 middle limb.