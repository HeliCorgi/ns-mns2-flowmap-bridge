# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (thirty-fifth session).

> **Historical archive.** The full session-by-session handoff through the
> twenty-ninth session is preserved at main commit
> `c69315e32eead48c1fd681bf86c8bab1af815e64` (PR #83 merge). This live file is
> intentionally the short-form continuation point. Current theorem/source files and
> dated gate records override stale prose.
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
> `u_j=Delta_j u`, `lambda_j=2^j`, one-window lengths
> `tau_j=a_*/(nu lambda_j^2)`, define
>
> `I_j(t) = lambda_j^(-1) || int_{max(0,t-tau_j)}^t
>              exp(nu(t-s)Delta) Delta_j P div(u tensor u)(s) ds ||_infinity`.
>
> **FDT-INJ remains OPEN.** YES would imply bounded dissipation wavenumber on every
> finite horizon, then `int F<infinity`, then continuation. A static energy-only
> shortcut was killed.
>
> **2026-09-05 (thirty-fourth session): FDT LOW-HIGH OPERATOR GATE ATTACKED.**
> Record: `docs/gates/FDT_LH_DECISION_2026-09-05.md` on PR #87 branch
> `research/fdt-lh-decision`. For `C_j(a,b)=P[Delta_j,a·grad]b` and its one-window
> heat integral, a real divergence-free Schwartz packet counterfamily gives a
> subcritical target high block but arbitrarily large normalized LH contribution
> while both ordinary energy and the one-window enstrophy budget tend to zero.
> Therefore **FDT-LH-OP = NO**. This does not refute FDT-INJ because the bad datum
> changes with `j`.
>
> **2026-09-06 (thirty-fifth session): FDT-LH-DYN AFFINE MODEL ATTACKED.**
> Record: `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md` on PR #87.
>
> Use the trace-free affine strain `a(x)=(-gamma x1, gamma x2, 0)` and transverse
> shear `w(t,x)=e3 f(t,x1)`. Because `(w·grad)a=(w·grad)w=0`, `Delta a=0`, and
> `(a·grad)a` is cancelled by `p=-(gamma^2/2)(x1^2+x2^2)`, the full field `u=a+w`
> is an exact nonlinear unforced NS solution whenever
> `partial_t f-gamma x1 partial_1 f=nu partial_1^2 f`.
>
> For `f(0,x1)=B cos(k0 x1)`, the exact solution is
> `f(t,x1)=B D(t) cos(k(t)x1)`, `k(t)=k0 exp(gamma t)`,
> `D(t)=exp[-nu k0^2(exp(2gamma t)-1)/(2gamma)]`. If
> `m_j(t)=phi_j(k(t)e1)`, then exactly
>
> **`C_j(a,w(t))=-m_j'(t)w(t)`.**
>
> After conjugating by the low flow, the phase is fixed, diffusion is anisotropic,
> and the Eulerian LP cutoff becomes a deformed multiplier `M_j(t)`. In this exact
> model the signed dynamic commutator Duhamel term telescopes to
>
> **`K_j(t)=[m_j(t)-m_j(0)]g(t)`.**
>
> At one viscous window `tau_j=a_*/(nu lambda_j^2)`, take
> `gamma=sigma nu lambda_j^2` and choose an initial frequency below the `j` shell that
> is strained into a point `rho lambda_j` with `m_*=phi(rho e1)>0`. The final heat
> factor is `D(tau_j)=exp[-rho^2(1-exp(-2sigma a_*))/(2sigma)] -> 1` as
> `sigma->infinity`. With `B=epsilon c_0 nu lambda_j/m_*`, `1/2<epsilon<1`, the
> final target block stays subcritical while, for large `sigma`,
>
> **`lambda_j^-1 ||K_j(tau_j)||_infinity
>      = epsilon c_0 nu D(tau_j) > (1/2)c_0 nu`.**
>
> Therefore **FDT-LH-DYN-AFF = NO**. Exact low-flow conjugation does not make the LH
> deformation commutator perturbative; it records order-one shell transport/frequency
> relabeling. The affine background is not in `L^2(R^3)` and is not Schwartz, so this
> is an exact model no-go, not a Clay-admissible or fixed-datum refutation of FDT-INJ.
>
> **Strategic ruling after sessions 34–35:** separate-LH fixed-margin estimates are
> **PARKED**. A viable FDT route should absorb material shell transport into the
> observable instead of charging it as nonlinear injection.

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
10. current GitHub `main`, open PRs, and relevant formal files.

## Handoff update contract

Every substantive session must, before ending: record what was executed and not claimed; rewrite
**Next work** with exact next gate/read order/forbidden shortcuts; synchronize `STATUS.md` and
`FORMAL_SCOPE.md` only if the formal frontier moved; and keep the durable continuation here rather
than only in chat or PR comments.

### Next work (written 2026-09-06, thirty-fifth session)

- **Current state:** parent `FDT-INJ` is **OPEN**. Separate-LH is parked:
  `FDT-LH-OP = NO`, `FDT-LH-DYN-AFF = NO`. The latter is an exact full-NS model
  no-go but not an admissible-data counterexample. S15 `(q,d)` also remains parked.
- **Recommended next gate: `FDT-MAT` (material-frequency injection).** Define a
  low-flow-conjugated/material dyadic projector `Delta_j^mat(t)` following
  `u_{<=j-2}` so principal low transport commutes by construction and the exact
  affine model has zero material-shell transport defect. Derive exact remaining terms
  from conjugated diffusion, Leray projection, deformation metric, HL, and HH before
  estimating anything.
- **First FDT-MAT YES/NO question:** can the residual be defined so that (i) benign
  affine shell relabeling is absorbed exactly, (ii) a fixed critical one-window margin
  would still imply a known continuation criterion, and (iii) no `int F`,
  `int ||grad u||_infinity`, Serrin norm, bounded H3, or equivalent continuation wall
  is inserted by hand?
- **Alternative admissibility bridge:** `FDT-LH-LOC` may localize affine strain/shear
  to Schwartz data and prove a controlled one-window approximation. Pressure,
  nonlocality, and cutoff errors must be quantified; localization is not automatic.
- **Do not resume separate LH margin estimates.** The affine identity shows the
  unavoidable distortion coefficient is schematically
  `int_{t-tau_j}^t ||grad u_{<=j-2}||_infinity ds`; session 34 already showed ordinary
  energy/enstrophy do not make it small.
- **Do not claim FDT-INJ is false.** Neither the non-admissible affine model nor the
  different-datum packet family satisfies the parent fixed-Schwartz-datum NO
  certificate.
- **Lean:** no LP/Bony/paracomposition plumbing until a material-frequency analytic
  gate survives counterexample-first testing.

## Repository / verification state

- `main` at start of session 35: `2fa19df787201a3f306043fd632f569fc245cf4c`
  (merged PR #86).
- Current branch / open PR: `research/fdt-lh-decision`, PR #87.
- Session-34 record first commit: `3306bbead924c1f7c4c8812c5bf5b206b6eb6d01`.
- Session-35 affine record first commit: `17ba363afe0e6fc3061809b920a438600f4db773`.
- No Lean/runtime source changed in sessions 34–35; `FORMAL_SCOPE.md` and `STATUS.md`
  intentionally remain unchanged.
- PR #87 pre-session-35 integration check: workflow `Lean 4 formalization`, run #263
  (`33950506980`), job `101264255550`, conclusion **success**; proof-hole/local-axiom
  scan and cached full build both passed. Final session-35 docs pushes may trigger a
  fresh status run.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement. No current result proves 3D
Navier–Stokes global regularity or blow-up. The newest result is a mechanism-level exact no-go: in
an exact trace-free affine-strain NS solution, low-flow conjugation turns the signed LH commutator
into an order-one LP multiplier boundary displacement rather than a small remainder. Because the
affine background is not finite energy, this refines the FDT route but is not a Clay counterexample
or theorem.