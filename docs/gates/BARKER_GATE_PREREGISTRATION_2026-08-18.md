# Stage-A pre-registration — necessary-condition gate battery for axisymmetric NS blowup candidates

Date frozen: 2026-08-18 (JST). Author: Fable5 session, Stage A of the
Hou-candidate × necessary-conditions × rigorous-numerics program (see HANDOFF.md).

Status of this document: **pre-registration**. The gate definitions, thresholds, and kill
rules below are frozen before extracting quantitative scaling numbers from candidate sources
and before running any in-repo candidate evolution. The analyst has prior qualitative
exposure to the literature; the pre-registration therefore fixes *quantitative* thresholds
and *decision rules*, which is what prevents post-hoc rationalization.

## 0. Object under test

A "candidate" is any claimed approximately-singular axisymmetric-with-swirl solution of the
**standard fixed-viscosity incompressible 3D Navier–Stokes equations** (`f = 0`), presented
either as

- (L) literature-reported diagnostics (scaling fits, growth factors, sup norms), or
- (N) in-repo numerical data satisfying the auditability invariants of `SPEC.md` §8.

Candidates for modified equations (degenerate/variable viscosity, generalized models,
boundary-driven Euler) are **out of scope as Clay C candidates** by `PROJECT_GOAL.md` and are
recorded only as context.

## 1. Gates

All gates are *necessary conditions* derived from proved theorems for suitable/energy
solutions of standard NS. A candidate that robustly violates a gate is not a Navier–Stokes
singularity candidate (it may still be a singular candidate for a *different* equation).

Notation: putative blowup time `T*`, `τ = T* − t`, viscosity `ν`, energy `E₀ = ½‖u₀‖²_{L²}`.

### G1 — Enstrophy exponent band (Leray lower bound × energy inequality)

If `‖∇u(t)‖_{L²} ~ C τ^{−β}` as `τ → 0`, then

- `β ≥ 1/4` (Leray-type lower bound: `‖∇u(t)‖_{L²} ≥ c ν^{3/4} τ^{−1/4}`), and
- `β < 1/2` (energy inequality: `ν ∫₀^{T*} ‖∇u‖²_{L²} dt ≤ E₀ < ∞`).

**Kill rule:** fitted `β` (with fit window covering ≥ 2 decades of `τ` or the maximal
available range, reported with least-squares CI) outside `[0.25 − σ, 0.5 + σ)` where `σ` is
the fit's 2-standard-error, fires the gate. A fitted `β ≥ 0.5` with CI excluding `0.5` is a
hard kill (infinite dissipated energy).

### G2 — Type II requirement (CSTY / KNSS axisymmetric Type-I exclusion)

For **axisymmetric** finite-energy solutions, Type I bounds imply regularity
(Chen–Strain–Tsai–Yau 2008/2009; Koch–Nadirashvili–Seregin–Šverák 2009). Hence a genuine
axisymmetric NS singularity must be **Type II**:

`limsup_{t→T*} √τ · ‖u(t)‖_{L∞} = ∞.`

**Kill rule:** if the candidate's own scaling ansatz or fitted behavior gives
`‖u‖_{L∞} ~ C τ^{−1/2}` (self-similar or "nearly self-similar" with velocity exponent
`1/2 ± σ`, CI containing `1/2` and bounded amplitude factor), the gate fires: the candidate,
*as scaled*, is excluded by theorem. Survival requires demonstrated superlinear growth of
`√τ‖u‖_{L∞}` (or an explicit Type II mechanism).

### G3 — Critical norm divergence (Escauriaza–Seregin–Šverák)

`‖u(t)‖_{L³(ℝ³)} → ∞` as `t → T*` is necessary. **Kill rule:** candidate data whose `L³`
norm saturates or decays over the final resolved decade of `τ` while claiming approach to
blowup fires the gate (resolution caveat mandatory; this gate is advisory at level (N) unless
convergence-tested across resolutions).

### G4 — Swirl maximum principle (Γ = r·u_θ)

`‖Γ(t)‖_{L∞}` is non-increasing for axisymmetric NS. **Kill rule:** any candidate evolution
in which the audited `‖Γ‖_{L∞}` increases beyond discretization tolerance fires the gate
(this is an equation-fidelity check as much as a physics check).

### G5 — Blowup locus on the axis

For axisymmetric-with-swirl NS, singularities can only occur on the symmetry axis
(`r = 0`); away from the axis the solution is locally regular (standard structure results,
e.g. as reviewed in the axisymmetric literature). **Kill rule:** candidate whose maximal
gradients concentrate at `r_c > 0` bounded away from the axis at fixed `z`-window with
refinement, fires the gate.

### G6 — Parabolic concentration scale (Barker–Prange type)

Quantitative localization results require critical-norm concentration at parabolic scale near
a potential singularity: there exist `γ > 0` with
`‖u(t)‖_{L³(B_{R(t)}(x*))} ≥ γ`, `R(t) = O(√τ)`.
**Kill rule (advisory level):** candidate whose fitted concentration length `ℓ(t)` (scale of
the near-axis structure) shrinks much *faster* than every parabolic window while its local
`L³` mass on `B_{√τ}` tends to 0 fires the gate. (Two-scale candidates must be tested on the
inner scale; the gate is recorded as advisory pending exact constant extraction from the
literature.)

### G7 — Structural no-go hygiene (repo registry)

FC-086 (Tao averaged-NS): any *positive* claim must use structure beyond generic estimates.
For candidates: the diagnostic pipeline must distinguish standard NS from a degenerate-ν or
generalized model — if a candidate's supporting computation actually integrates a modified
equation (variable ν, added damping, model truncation), it is reclassified out of scope
(G7 fire = out-of-scope, not "NS candidate killed").

## 2. Null and positive controls (mandatory before any (N)-level verdict)

- **Null control:** a small-data / no-swirl axisymmetric run (known globally regular
  regime). Required outcome: G1–G6 report "no blowup signature"; any gate firing on the null
  control invalidates that gate's implementation.
- **Positive control:** a synthetic exactly self-similar Type I mock field
  (`u(x,t) = τ^{-1/2} U(x/√τ)` with smooth compactly supported `U`). Required outcome:
  G2 fires (by construction), G1 reports `β = 1/2⁻` boundary behavior. If G2 fails to fire
  on the mock, its implementation is invalid.

## 3. Decision rules for the route (frozen)

- If the **standard-ν Hou-type candidate** fails G2 at literature level (velocity scaling
  consistent with Type I / nearly self-similar `τ^{−1/2}`), then the route
  "formalize the existing candidate as-is" is **KILLED**, and the surviving reformulation is
  "Type II candidate search under the same formal infrastructure". This outcome must be
  recorded in the exclusion registry with the binding obstruction = CSTY/KNSS.
- If literature-level numbers are inconclusive (no clean velocity exponent reported), the
  decision moves to (N)-level: reproduce a candidate evolution in-repo under `SPEC.md` §8 and
  apply G1–G6 with controls.
- Gates G1+G2 firing together at (N) level with controls passing = route KILLED at candidate
  level; the formal program (local theory, continuation, abstract Chen–Hou skeleton) is
  unaffected and continues as infrastructure for any successor candidate.

## 4. Primary theorem sources

- J. Leray, Acta Math. 63 (1934) — lower bounds / energy inequality.
- C.-C. Chen, R. M. Strain, T.-P. Tsai, H.-T. Yau, IMRN 2008 & Comm. PDE 2009 — lower bound
  on axisymmetric blowup rate (no Type I), arXiv:math/0701796, arXiv:0709.4230.
- G. Koch, N. Nadirashvili, G. Seregin, V. Šverák, Acta Math. 203 (2009) — Liouville
  theorems and axisymmetric Type I exclusion.
- L. Escauriaza, G. Seregin, V. Šverák, Uspekhi/Russian Math. Surveys 58 (2003) — `L³`
  endpoint regularity.
- T. Barker, C. Prange — quantitative/localized concentration near potential singularities
  (concentration of critical norms at parabolic scales).
- T. Y. Hou, "The potentially singular behavior of the 3D incompressible Navier–Stokes
  equations", arXiv:2107.06509 / FoCM (2022) — candidate source (L).
- Registry: `ns-singularity-certificate-lab` FC-086/FC-087 and `SPEC.md` §8–10.
