# MNS-2 / Navier–Stokes flow-map bridge handoff

Last updated: 2026-09-06 JST (thirty-fifth session).

> **Historical archive.** The full session-by-session handoff through the
> twenty-ninth session is preserved at main commit
> `c69315e32eead48c1fd681bf86c8bab1af815e64` (PR #83 merge).  This live file is
> intentionally the short-form continuation point.  Current theorem/source files and
> dated gate records override stale prose.
>
> **Sessions 30–32: ASTRA S15 traveling-max cone explored, then parked.**
> Read, in order:
> `docs/gates/ASTRA_S15_TRAVELING_MAX_2026-09-05.md`,
> `docs/gates/ASTRA_S15_Q_DECISION_2026-09-05.md`, and
> `docs/gates/ASTRA_S15_D_DECISION_2026-09-05.md`.
> The exact moving-max identity is `A'=(2q-d)A^2`; the candidate cone
> `q>=1/4`, `0<=d<=1/8` gives conditional `A'>=(3/8)A^2`.  Q-UNIV was killed by
> remote pressure freedom and D-UNIV by local fourth-jet freedom.  The `(q,d)` S15
> realization is **PARKED BY DEFAULT**.  PR #83 merged as
> `c69315e32eead48c1fd681bf86c8bab1af815e64`, PR #84 as
> `0fa9cadf998fcb5935812cfb56b4a86ea49c81cd`, and PR #85 as
> `084aa0d1fca1d89726af1f544f3689a95a3f71ba`.
>
> **2026-09-05 (thirty-third session): FREQUENCY / DISSIPATION-SCALE ROUTE OPENED.**
> Record: `docs/gates/FREQUENCY_DISSIPATION_TRANSFER_DECISION_2026-09-05.md`,
> merged by PR #86 as `2fa19df787201a3f306043fd632f569fc245cf4c`.
> This is a regularity-side cross-track gate; it does not silently replace the current
> `SPEC.md` breakdown-side priority.
>
> With a smooth inhomogeneous LP decomposition `u_j=Delta_j u`, `lambda_j=2^j`,
> define `tau_j=a_*/(nu lambda_j^2)` and the exact signed vector Duhamel injection
>
> `I_j(t) = lambda_j^(-1) || int_{max(0,t-tau_j)}^t
>              exp(nu(t-s)Delta) Delta_j P div(u tensor u)(s) ds ||_infinity`.
>
> **FDT-INJ asks:** for every `nu>0`, every real divergence-free Schwartz datum,
> and every finite horizon `L`, is there a datum-dependent finite `J` such that
>
> `sup_{0<t<min(L,T_*)} sup_{j>=J} I_j(t) <= (1/2)c_0 nu`?
>
> **FDT-INJ remains OPEN.**  The gate records the full first-contact implication
> `FDT-INJ => bounded dissipation wavenumber on finite horizons => int F < infinity =>
> continuation`.  A static energy-only shortcut was killed.
>
> **2026-09-05 (thirty-fourth session): FDT LOW–HIGH OPERATOR GATE ATTACKED.**
> Record: `docs/gates/FDT_LH_DECISION_2026-09-05.md` on PR #87 branch
> `research/fdt-lh-decision`.
>
> For low `a` and high `b`, define
>
> `C_j(a,b) = P [Delta_j, a·grad] b`
>
> and
>
> `W_j(a,b) = lambda_j^(-1) int_0^{tau_j}
>                 exp(nu(tau_j-s)Delta) C_j(a,b) ds`.
>
> A Fourier-symbol packet construction gives real divergence-free Schwartz `a,b`
> with nonzero commutator.  For
>
> `a_{j,M}(x)=M nu lambda_j a(lambda_j x)`,
> `b_j(x)=epsilon c_0 nu lambda_j b(lambda_j x)`,
>
> the target high packet is subcritical while
>
> `||W_j(a_{j,M},b_j)||_infinity = M epsilon Gamma_LH c_0 nu`.
>
> Simultaneously the ordinary energy and one-window enstrophy budget are
> `O(lambda_j^-1) -> 0`.  Hence **FDT-LH-OP = NO**: spectral separation,
> incompressibility, Leray, heat damping, and ordinary energy/dissipation do not force
> a fixed LH margin.  This does not refute FDT-INJ because the bad datum changes with
> `j`.
>
> **2026-09-06 (thirty-fifth session): FDT-LH-DYN AFFINE MODEL ATTACKED.**
> Record: `docs/gates/FDT_LH_DYN_AFFINE_DECISION_2026-09-06.md` on the same PR #87
> branch.  The session also updated `FDT_LH_DECISION_2026-09-05.md` to cross-link and
> incorporate the new ruling.
>
> Use the trace-free affine strain
>
> `a(x)=(-gamma x1, gamma x2, 0)`
>
> and transverse shear
>
> `w(t,x)=e3 f(t,x1)`.
>
> Because `(w·grad)a=(w·grad)w=0`, `Delta a=0`, and
> `(a·grad)a` is cancelled by
> `p=-(gamma^2/2)(x1^2+x2^2)`, the full field **`u=a+w` is an exact nonlinear
> unforced NS solution** whenever
>
> `partial_t f - gamma x1 partial_1 f = nu partial_1^2 f`.
>
> For initial `f(0,x1)=B cos(k0 x1)`, the exact solution is
>
> `f(t,x1)=B D(t) cos(k(t)x1)`,
> `k(t)=k0 exp(gamma t)`,
> `D(t)=exp[-nu k0^2 (exp(2 gamma t)-1)/(2 gamma)]`.
>
> Let `m_j(t)=phi_j(k(t)e1)`.  The LP low-high commutator satisfies exactly
>
> **`C_j(a,w(t)) = -m_j'(t) w(t)`**.
>
> Conjugate by the low flow.  The phase becomes fixed, diffusion becomes anisotropic,
> and the Eulerian LP projector becomes a deformed multiplier `M_j(t)`.  Since the
> conjugated heat operator and `M_j(t)` are simultaneous Fourier multipliers on this
> exact model, the signed dynamic commutator Duhamel integral telescopes:
>
> **`K_j(t) = [m_j(t)-m_j(0)] g(t)`**.
>
> Thus there is no hidden temporal/phase cancellation.  The term is exactly the LP
> multiplier displacement caused by strain.
>
> At one parent viscous window `tau_j=a_*/(nu lambda_j^2)`, choose
> `gamma=sigma nu lambda_j^2` and an initial frequency below the `j` shell which strain
> moves to a point `rho lambda_j` with `m_*=phi(rho e1)>0`.  The final heat factor is
>
> `D(tau_j)=exp[-rho^2(1-exp(-2 sigma a_*))/(2 sigma)] -> 1`
>
> as `sigma -> infinity`.  Normalize
>
> `B = epsilon c_0 nu lambda_j / m_*`, with `1/2<epsilon<1`.
>
> For sufficiently large `sigma`, the final target block is still subcritical but
>
> **`lambda_j^-1 ||K_j(tau_j)||_infinity
>      = epsilon c_0 nu D(tau_j) > (1/2)c_0 nu`.**
>
> Therefore **`FDT-LH-DYN-AFF = NO`**.  Low-flow conjugation plus exact signed time
> integration does not make the LH deformation commutator perturbative.  In this model
> a large LH term is benign **shell transport / frequency relabeling**, not high-mode
> self-amplification.
>
> **Scope boundary:** the affine background is not in `L^2(R^3)` and is not Schwartz.
> Hence this is an exact model no-go, not a valid Clay-admissible or fixed-datum
> refutation of FDT-INJ.  The admissible `R^3` question remains OPEN.
>
> **Strategic ruling after sessions 34–35:** the strategy “bound the LH term separately
> by a fixed critical margin” is **PARKED**.  `FDT-LH-OP` fails by a Schwartz packet
> scaling counterfamily, and the natural signed/Lagrangian repair fails in the exact
> affine model because the residual telescopes to shell displacement.  A viable FDT
> route should absorb material shell transport into the observable instead of charging
> it as nonlinear injection.

This is the durable continuation point for future GPT sessions.  Do not rely on chat history.

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
10. for why S15 is parked, the three Astra S15 gate records;
11. current GitHub `main`, open PRs, and relevant Stokes/Leray/convection formal files.

## Handoff update contract

Every substantive session must, before ending:

1. record what was executed and what was deliberately not claimed;
2. rewrite **Next work** below with the exact next gate, read order, and forbidden shortcuts;
3. update `STATUS.md` / `FORMAL_SCOPE.md` only if the formal frontier actually moved;
4. keep the durable continuation here, not only in chat, PR comments, or commit messages.

### Next work (written 2026-09-06, thirty-fifth session)

Read first: the session-33/34/35 blocks above and the three FDT gate records listed in
Resume protocol items 7–9.

- **Current target/state:** parent `FDT-INJ` is still **OPEN**.  The separate-LH proof
  strategy is now **PARKED**: `FDT-LH-OP = NO`; `FDT-LH-DYN-AFF = NO`.  The latter is
  an exact full-NS model no-go but not an admissible-data counterexample because the
  affine background has infinite energy.  The old S15 `(q,d)` cone remains parked.
- **Recommended next analytic gate: `FDT-MAT` (material-frequency injection).**
  Define a low-flow-conjugated/material dyadic projector `Delta_j^mat(t)` which follows
  `u_{<=j-2}` so that principal low transport commutes by construction and the exact
  affine model has **zero material-shell transport defect**.  Then derive, without
  estimates first, the exact remaining terms from conjugated diffusion, Leray
  projection, deformation of the metric, and the HL/HH paraproducts.
- **FDT-MAT first YES/NO question:** can the resulting one-window residual be stated
  so that (i) affine shell relabeling is absorbed exactly, (ii) a fixed critical
  margin would still imply a known continuation criterion, and (iii) the coefficients
  do not already assume `int F`, `int ||grad u||_infinity`, Serrin, or bounded H3?
  Attack this definition counterexample-first before estimating HH.
- **Alternative admissibility bridge:** if one wants to turn the affine no-go into an
  admissible-data obstruction, define a separate `FDT-LH-LOC` gate: localize the affine
  strain and transverse packet to Schwartz data, prove a controlled one-window
  approximation to the exact affine solution, and state precisely what this kills.
  Do not claim such localization is automatic; pressure/nonlocality and boundary
  errors must be quantified.
- **Do not resume separate LH margin estimates.**  The exact affine identity says the
  missing coefficient is deformation strain, schematically
  `S_j(t)=int_{t-tau_j}^t ||grad u_{<=j-2}||_infinity ds`.  The previous operator gate
  already showed ordinary energy/enstrophy do not make this small.  Reintroducing
  `S_j` as an assumption without an independent budget is a disguised continuation
  wall.
- **Do not claim FDT-INJ is false.**  The affine model is non-admissible and the
  session-34 packet family changes the datum with `j`; neither satisfies the fixed
  Schwartz-datum NO certificate required by the parent gate.
- **Lean ruling:** no LP/Bony/paracomposition Lean layer yet.  Formalize only after a
  material-frequency analytic gate survives counterexample-first testing.

## Repository / verification state

- `main` at start of session 35: `2fa19df787201a3f306043fd632f569fc245cf4c`
  (merged PR #86).
- Current branch / open PR: `research/fdt-lh-decision`, PR #87.
- Session-34 FDT-LH record first commit:
  `3306bbead924c1f7c4c8812c5bf5b206b6eb6d01`.
- Session-35 affine decision first commit:
  `17ba363afe0e6fc3061809b920a438600f4db773`.
- Session-35 integration/update commits after that include
  `a5df47d0676c82fe50aff780a581d6dea473a1a8` (cross-link/update of the session-34
  record) and this final handoff commit.
- No Lean/runtime source changed in sessions 34–35; `FORMAL_SCOPE.md` and `STATUS.md`
  intentionally remain unchanged.
- PR #87 pre-session-35 hosted integration check: workflow `Lean 4 formalization`,
  run **#263** (`33950506980`), job `101264255550`, conclusion **success**; proof-hole /
  local-axiom scan and cached full build both passed.  Session-35 docs pushes may
  trigger a fresh integration run; treat it as status only.
- Prior exact formal baseline remains Lean 4.32.1 / **8777 jobs PASS**.
- GitHub-hosted Actions remain a final/status resource, not an interactive compiler.

## Project claim boundary

Ultimate target: an exact official Clay/Fefferman A/B/C/D statement.  No current result proves
3D Navier–Stokes global regularity or blow-up.  The newest result is a mechanism-level exact no-go:
in an exact trace-free affine-strain NS solution, low-flow conjugation turns the signed LH
commutator into an order-one LP multiplier boundary displacement rather than a small remainder.
Because the affine background is not finite energy, this refines the FDT route but is not a Clay
counterexample or theorem.