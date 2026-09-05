# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (thirty-sixth session).

> **Historical archive.** The full session-by-session handoff through the twenty-ninth
> session is preserved at main commit `c69315e32eead48c1fd681bf86c8bab1af815e64`
> (PR #83 merge). This live file is intentionally the short-form continuation point.
> Current theorem/source files and dated gate records override stale prose.
>
> **Sessions 30–32: ASTRA S15 traveling-max cone explored, then parked.**
> Read `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`,
> `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md`, and
> `docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md`. The exact moving-max identity is
> `A'=(2q-d)A^2`; the candidate cone `q>=1/4`, `0<=d<=1/8` gives conditional
> `A'>=(3/8)A^2`. Q-UNIV was killed by remote pressure freedom and D-UNIV by local
> fourth-jet freedom. The `(q,d)` S15 realization is **PARKED BY DEFAULT**.
>
> **2026-09-05 (thirty-third session): FREQUENCY / DISSIPATION-SCALE ROUTE OPENED.**
> Record: `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`, merged
> by PR #86 as `2fa19df787201a3f306043fd632f569fc245cf4c`. With LP blocks
> `u_j=Delta_j u`, `lambda_j=2^j`, and one-window lengths
> `tau_j=a_*/(nu lambda_j^2)`, define the signed one-window Eulerian Duhamel injection
>
> `I_j(t) = lambda_j^(-1) || int exp(nu(t-s)Delta) Delta_j P div(u tensor u)(s) ds ||_infinity`.
>
> **FDT-INJ remains OPEN.** A universal YES would bound the dissipation wavenumber on
> every finite horizon and imply the known Cheskidov–Shvydkoy continuation criterion.
> A static energy-only shortcut was killed.
>
> **2026-09-05 (thirty-fourth session): FDT LOW-HIGH OPERATOR GATE ATTACKED.**
> Record: `docs/gates/FDT_LH_DECISION_2026-09-05.md`. For
> `C_j(a,b)=P[Delta_j,a·grad]b`, a real divergence-free Schwartz packet counterfamily
> gives a subcritical target high block but arbitrarily large normalized LH contribution
> while ordinary energy and the one-window enstrophy budget tend to zero. Therefore
> **FDT-LH-OP = NO**. This does not refute FDT-INJ because the bad datum changes with
> `j`.
>
> **2026-09-06 (thirty-fifth session): FDT-LH-DYN AFFINE MODEL ATTACKED.**
> Record: `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`. The exact
> trace-free affine strain plus transverse shear is a full nonlinear unforced NS
> solution with `C_j(a,w(t))=-m_j'(t)w(t)`. After low-flow conjugation the signed
> commutator Duhamel term telescopes exactly to
>
> `K_j(t)=[m_j(t)-m_j(0)]g(t)`.
>
> On one viscous window, strain can move a mode into shell `j` late enough that its
> heat damping is arbitrarily small, while the final block remains subcritical and
> `lambda_j^-1 ||K_j||_infinity > (1/2)c_0 nu`. Therefore
> **FDT-LH-DYN-AFF = NO**. The large LH term is benign shell transport/frequency
> relabeling, not high-mode self-amplification. The affine background is not `L^2` or
> Schwartz, so this is an exact model no-go, not a parent FDT-INJ refutation.
>
> **2026-09-06 (thirty-sixth session): FDT MATERIAL-FREQUENCY STRUCTURE DECIDED.**
> Record: `docs/gates/FDT_MAT_STRUCT_DECISION_2026-09-06.md` on branch
> `research/fdt-mat-struct-decision`.
>
> For the low flow `X_j` of `v_j=u_{<=j-2}`, define the componentwise pullback
> `U_j(t,s)f=f o X_j(t,s)` and the canonical material projector
>
> `Delta_j^mat(t;s)=U_j(t,s)^(-1) Delta_j U_j(t,s)`.
>
> It satisfies exactly
>
> **`[partial_t + v_j·grad, Delta_j^mat]=0`.**
>
> Therefore **FDT-MAT-COMM = YES**: principal low transport and affine shell
> relabeling can be absorbed by construction.
>
> However, for an affine trace-free low flow `v=Sx`, the exact material multiplier is
>
> **`m_j^mat(t,xi)=phi_j(exp(t S^T) xi)`.**
>
> Hence a material annulus becomes an ellipsoid under the inverse-transpose
> deformation. For `S=diag(-gamma,gamma,0)` its Eulerian axis frequencies are
> distorted by factors `exp(+gamma t)` and `exp(-gamma t)`. On one viscous window
> `tau_j=a_*/(nu lambda_j^2)`, choosing `gamma=sigma nu lambda_j^2` gives distortion
>
> **`exp(sigma a_*)`, arbitrarily large for arbitrary sigma.**
>
> Therefore no trajectory-independent constant uniformly compares exact-commuting
> material shell index to fixed Eulerian dyadic frequency. A material-tail estimate
> cannot be fed back into the fixed-Eulerian Cheskidov–Shvydkoy continuation theorem
> without quantitative control of `DX_j` and `DX_j^{-1}`, schematically
> `exp(int ||grad v_j||_infinity)`. The previous LH counterfamily already shows that
> ordinary energy/enstrophy does not make this strain budget small.
>
> Thus **FDT-MAT-BRIDGE-UNIF = NO**, and the ambitious conjunction
> **FDT-MAT-STRUCT = NO as stated**. The positive exact commutation identity is kept.
>
> A second structural cost is recorded: componentwise pullback commutes with NS
> convection but does not generally preserve divergence; the divergence-preserving
> Piola pullback instead produces an explicit `(grad v)w` deformation term. Leray
> projection therefore does not remove low deformation for free.

This is the durable continuation point for future GPT sessions. Do not rely on chat history.

## Resume protocol

Follow `docs/GPT_WORKFLOW.md`. Read, in order:
1. `PROJECT_GOAL.md`;
2. `SPEC.md`;
3. `AGENTS.md`;
4. `FORMAL_SCOPE.md`;
5. this file;
6. `docs/LEAN_CI_OPERATIONS.md`;
7. `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`;
8. `docs/gates/FDT_LH_DECISION_2026-09-05.md`;
9. `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md`;
10. `docs/gates/FDT_MAT_STRUCT_DECISION_2026-09-06.md`;
11. current GitHub `main`, open PRs, and relevant formal files.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, thirty-sixth session)

- **Current state:** parent `FDT-INJ` is still **OPEN**. Separate-LH fixed-margin
  closure is parked (`FDT-LH-OP = NO`, `FDT-LH-DYN-AFF = NO`). Naive material-shell
  repair is also decided: `FDT-MAT-COMM = YES` but
  `FDT-MAT-BRIDGE-UNIF = NO`, hence `FDT-MAT-STRUCT = NO as stated`.
- **Recommended next gate: `FDT-DEF-BUDGET`.** Ask whether the actual finite-energy NS
  low-frequency flow admits an independently finite/subcritical deformation budget on
  viscous windows which is strong enough to compare material and Eulerian shells but
  is genuinely weaker than known continuation criteria. Attack counterexample-first.
- A candidate budget must control both `DX_j` and `DX_j^{-1}` or an equivalent
  Cauchy–Green distortion. It is invalid if the proof simply assumes or re-labels
  `int F`, `int ||grad u||_infinity`, a Serrin norm, bounded `H^3`, or another known
  continuation wall.
- **Decision rule:** if `FDT-DEF-BUDGET = NO`, park the current material-frequency
  regularity route rather than adding more LP/paracomposition machinery. If a
  genuinely weaker budget survives, only then derive the material diffusion/Leray/
  HL/HH residual and test a new continuation theorem.
- **Alternative research path:** `FDT-MAT-CONT` may seek a genuinely new continuation
  theorem directly in a deformation-aware material metric, but it must recover
  classical regularity without hiding the same deformation control in the norm.
- **Admissibility bridge remains optional:** localize the affine strain/shear to
  Schwartz data only if needed to distinguish a model no-go from an actual
  finite-energy obstruction. Pressure and cutoff errors must be quantified.
- **Do not claim FDT-INJ is false.** None of the affine model no-gos satisfies the
  fixed-Schwartz-datum parent NO certificate.
- **Lean:** no material LP/Piola/paracomposition plumbing until a load-bearing analytic
  bridge survives. The formal frontier did not move in session 36.

## Repository / verification state

- `main` at start of session 36: `9f8e3f94ab7baaeb6659e937ab8e019797cbf531`
  (merged PR #87).
- Current branch: `research/fdt-mat-struct-decision`.
- Session-36 material-structure record first commit:
  `0d16a5c1cc5a6c3d7aee99caefb4bef9e9812bba`.
- No Lean/runtime source changed in session 36; `FORMAL_SCOPE.md` and `STATUS.md`
  remain intentionally unchanged.
- PR #87 run #263 (`33950506980`), job `101264255550`, completed successfully; later
  docs-only runs on the old PR are status-only. A new PR for session 36 should trigger
  the same integration workflow.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The newest result is a structural split: low transport
can be removed exactly in a material dyadic frame, but exact commutation forces deformation of the
frequency shells, and no uniform bridge back to the fixed Eulerian continuation criterion exists
without a deformation budget. This refines/limits the FDT regularity route; it is not a Clay result.
