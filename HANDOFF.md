# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (forty-first session).

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
> `omega^r=-Gamma_z/r`, `omega^z=Gamma_r/r`, and
> `E_Gamma=2pi int (|Gamma_r|^2+|Gamma_z|^2)/r dr dz`.
> If `|Gamma(R,z)|>=m`, then
> **`int_0^R |Gamma_r|^2/r dr >= 2m^2/R^2`**; over axial length `L_z`,
> **`E_Gamma >= 4pi m^2 L_z/R^2`**. This does not kill the middle limb because the
> resulting costs are already integrable inside the frozen K5 wedge. Thus
> **`B2-GAMMA-FLATTOP-ENSTROPHY-KILL = NO`**.
> The transition nevertheless forces
> **`||omega||_infinity >= c tau^{-2 beta_v}`**, so
> **`B2-GAMMA-TRANSITION-VORTICITY = YES`**. A logarithmic-capacity flat-top snapshot
> prevents inferring a thick high-Gamma set from maximum curvature alone.
>
> **2026-09-06 (fortieth session): B2 GAMMA TRANSITION-RESIDENCE STOP/GO.**
> Record: `docs/gates/B2_GAMMA_TRANSITION_RESIDENCE_DECISION_2026-09-06.md`.
> The local diffusive clock `nu int R^{-2}` diverges for `R~tau^{beta_v}` with
> `beta_v>=1/2`, but the B2 hypotheses do not force one high-Gamma packet to remain resident.
> Delivery over the remaining time and delivery faster than one local diffusion time both fit below
> the Type-II amplitude envelope. An exact infinite-energy affine NS conveyor confirms the mechanism
> no-go. Decisions:
> - `B2-GAMMA-LATE-ARRIVAL-BARRIER = NO` from presently controlled quantities;
> - `B2-GAMMA-TRANSITION-RESIDENCE-KILL = NO`;
> - `B2-GAMMA-FLATTOP / RESIDENCE SUBLANE = PARKED`.
>
> **2026-09-06 (forty-first session): STOCHASTIC/BESSEL HITTING ATTACK.**
> Record: `docs/gates/B2_GAMMA_STOCHASTIC_HITTING_DECISION_2026-09-06.md` on branch
> `research/b2-gamma-stochastic-hitting`, stacked on open PR #90.
>
> Put `y=r^2` and `S=-u^r/r`.  The exact circulation equation becomes
>
> **`G_t - 2 S y G_y + u^z G_z = 4 nu y G_yy + nu G_zz`.**
>
> Thus the radial diffusion is the zero-dimensional squared-Bessel generator.  For frozen inward
> strain `A>=0`, the probability/harmonic measure of reaching `L^2` before the absorbing axis is
>
> **`p_A(y;L)=(1-exp(-A y/(2 nu)))/(1-exp(-A L^2/(2 nu)))`**,
>
> with `p_0=y/L^2`.
>
> More importantly, this promotes to an actual-PDE comparison barrier.  For fixed small `L`, define
> the running inward-strain ceiling `A(t)` as the maximum of a datum-dependent baseline and
> `sup_{s<=t, r<=L,z} S(s,r,z)`.  For either sign of Gamma,
>
> **`sigma Gamma(r,z,t) <= 2 M0 p_{A(t)}(r^2;L)`.**
>
> Hence fixed-fraction saturation at radius `R<<L` forces
>
> **`A(t) R^2 >= c(1-e^{-1}) nu`**
>
> up to the printed fixed-fraction constant.  Therefore a middle-limb law
> `R~tau^{beta_v}` forces arbitrarily late inward strain with
>
> **`S^+ >= c nu tau^{-2 beta_v}`**
>
> along a sequence.  Decision: **`B2-GAMMA-HITTING-STRAIN = YES`.**
>
> This still gives no new exponent exclusion.  If the strain is realized near `r~R`, the required
> radial speed is only `nu/R~tau^{-beta_v}`, strictly below the Type-II envelope because
> `beta_v<gamma`.  Moreover the hoped-for elliptic bridge fails structurally:
> `psi_1=A z` has `S=A` but `L5 psi_1=0`, hence `omega_1=0` locally.  Compact localization moves
> the elliptic source to a cutoff shell, and at the critical choice `A~nu/R^2` its energy and
> one-viscous-window dissipation costs are both `~nu^2 R -> 0`.  NS scaling preserves `S R^2`
> while energy scales to zero.
>
> Exact decisions:
> - **`B2-GAMMA-HITTING-STRAIN = YES`;**
> - **`B2-GAMMA-HITTING-NEW-EXPONENT-CUT = NO`;**
> - **`B2-GAMMA-STRAIN-ELLIPTIC-KILL = NO`;**
> - **`B2-GAMMA-SATURATION-MICROGEOMETRY = PARKED`.**
>
> The parent B2 middle limb remains OPEN.  The park ruling prevents another loop through
> co-location / max-displacement / packet-thickness variants unless a genuinely propagated
> cross-location or cross-scale theorem appears.

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
13. `docs/gates/B2_GAMMA_STOCHASTIC_HITTING_DECISION_2026-09-06.md`;
14. current GitHub `main`, open PRs, and the latest breakdown-side kill/readiness records.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, forty-first session)

- **Current state:** B2 remains the active parent breakdown-side lane, but the Gamma-saturation
  microgeometry program is **PARKED**.  It produced real dynamical necessities (maximum-curvature
  budget, transition vorticity, and now a BESQ/hitting inward-strain barrier), but every attempted
  kill is compatible with Type-II amplitude and finite energy/dissipation once the bad set is allowed
  to relocate or become scale-critical.
- **Do not proceed to `B2-GAMMA-MAX-DISPLACEMENT` as another location bookkeeping pass.** Reopen this
  family only for a propagated theorem forcing co-location, a one-fixed-solution scale-to-scale
  material-history theorem, a global constraint excluding harmonic strain, or an external critical
  drift theorem genuinely weaker than known continuation criteria.
- **Next research selection must be orthogonal to Gamma saturation location.** Return to the
  post-K11 / ancient-limit / steady-Euler side of the Type-II funnel, or select another actual-NS
  quantity with a signed/global propagated budget.  Prefer an obstruction invariant under relocating
  the bad set, so a remote-region escape cannot simply reopen the same branch.
- **Do not reopen S15 or FDT** absent their recorded reopen conditions.
- **Do not claim the parent B2 middle limb is false or realized.** It remains OPEN; only this proof
  mechanism is parked.
- **Lean:** no new formal layer. The formal frontier did not move; `FORMAL_SCOPE.md` and `STATUS.md`
  remain unchanged.

## Repository / verification state

- Main includes merged PR #89 (session-38 curvature gate).
- PR #90 (`research/b2-gamma-flattop-enstrophy`) remains open and contains sessions 39–40; its
  current head `66aa21f4e0647cd5abc78b3f62ea27dc99f28d73` passed workflow run #276.
- Current stacked branch: `research/b2-gamma-stochastic-hitting`, based on PR #90 head.
- Session-41 gate first commit: `90e0133c06d32c84abd22cbf372ec61b0567d4c0`.
- No Lean/runtime source changed in sessions 39–41; analytic docs-only frontier work.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The newest result is an actual-PDE Bessel/hitting barrier:
fixed-fraction circulation saturation approaching the axis forces scale-critical inward meridional
strain of order `nu/R^2` along arbitrarily late scales.  That requirement is nevertheless compatible
with the frozen Type-II envelope and can be supported by locally harmonic strain at vanishing
energy cost under NS scaling.  The Gamma-saturation microgeometry route is therefore parked rather
than extended through another escape-location variable.
