# Stage-A literature-level verdict — Hou fixed-ν NS candidate vs necessary-condition gates

Date: 2026-08-18 (JST). Pre-registration:
[`BARKER_GATE_PREREGISTRATION_2026-08-18.md`](BARKER_GATE_PREREGISTRATION_2026-08-18.md)
(thresholds frozen before extraction).

## 1. Source data (level L)

T. Y. Hou, *The potentially singular behavior of the 3D incompressible Navier–Stokes
equations*, arXiv:2107.06509 / FoCM 2022. Extracted diagnostics (full text, §3):

| Quantity | Reported behavior |
|---|---|
| `‖u‖_{L∞}` | `~ (T−t)^{−1/2}` (clean fit, no log factor reported) |
| `‖ω‖_{L∞}` | `~ |log(T−t)| / (T−t)` |
| `‖ω‖²_{L²}` | `~ (T−t)^{−1/2}` |
| `‖p‖_{L∞}` | `~ (T−t)^{−1}` |
| scales `R(t), Z(t)` | both `~ (T−t)^{1/2}`, ratio `O(1)` (**one-scale** structure) |
| viscosity | two-stage: `ν = 5·10⁻⁴` on `[0, t₀]`, then **increased** to `5·10⁻³`, tuned for "nearly optimal growth rate" |
| amplification | max vorticity growth ×10⁷ (transient measure) |
| Type I/II discussion | none; CSTY/KNSS not cited |

## 2. Gate outcomes

- **G1 (enstrophy band `β ∈ [1/4, 1/2)`)** — `‖∇u‖_{L²} = ‖ω‖_{L²} ~ τ^{−1/4}`, i.e.
  `β = 1/4`: **passes**, sitting exactly on the Leray lower boundary. Internal consistency
  check: `‖ω‖_∞ ~ ‖u‖_∞ / ℓ ~ τ^{−1}` and `‖ω‖²_{L²} ~ ‖ω‖_∞² ℓ³ ~ τ^{−1/2}` with
  `ℓ ~ τ^{1/2}` — the reported numbers are a self-consistent **Type I** one-scale picture.
- **G2 (Type II requirement, CSTY/KNSS)** — **FIRES, decisively.** The candidate's own
  velocity fit is `‖u‖_∞ ~ τ^{−1/2}` with one-scale parabolic geometry: exactly the
  scale-invariant bound under which axisymmetric finite-energy Navier–Stokes solutions are
  **regular** (Chen–Strain–Tsai–Yau IMRN 2008 / Comm. PDE 2009; Koch–Nadirashvili–Seregin–
  Šverák, Acta Math. 2009). As scaled, this cannot be an NS singularity.
- **G3 (`L³` divergence)** — `‖u‖_{L³}` at a Type I one-scale profile is `O(1)` in `τ`
  (scale-invariant norm of a fixed profile): consistent with *bounded* `L³`, i.e. also in
  tension with ESŠ divergence. Advisory support for the G2 verdict.
- **G7 (equation fidelity)** — the two-stage viscosity schedule is reinterpretable as a
  fixed-`ν = 5·10⁻³` Navier–Stokes evolution from the prepared smooth datum `u(t₀)`; so no
  out-of-scope fire, but the tuning is recorded: the ×10⁷ amplification is an engineered
  transient, not evidence of sustained blowup.

## 3. Escape-hatch analysis (what could unkill)

1. **Logarithmic Type II.** The vorticity fit carries a `|log τ|` factor. If the *velocity*
   also carried an unbounded correction (`√τ‖u‖_∞ → ∞` however slowly), the CSTY/KNSS
   hypotheses would fail and the exclusion would not apply. But the candidate's own velocity
   fit is clean `τ^{−1/2}`; the burden of an unkill is to demonstrate, with converged
   diagnostics, that `√τ‖u‖_∞` diverges. Nothing in the reported data does this.
2. **Non-axisymmetric candidates.** CSTY/KNSS is an axisymmetric theorem; dropping the
   symmetry removes the obstruction but abandons the current candidate class and its
   numerical advantages.
3. **Modified equations.** Degenerate/variable-viscosity variants (cf. the later
   generalized-NS blowup literature) escape the theorem but are Clay-inadmissible; out of
   scope by `PROJECT_GOAL.md`.

## 4. Verdict (per frozen decision rule §3 of the pre-registration)

**ROUTE KILLED at candidate level:** "formalize the existing fixed-ν Hou NS candidate
as-is toward Clay C" is excluded at the literature level. Binding obstruction:
CSTY 2008/2009 + KNSS 2009 (axisymmetric no-Type-I) against the candidate's own reported
`τ^{−1/2}` velocity scaling and one-scale parabolic geometry.

**What survives, unchanged in value:**

- the entire formal program (real local theory → continuation criterion → abstract
  stability-implies-breakdown skeleton) is candidate-independent infrastructure; a Type II or
  non-axisymmetric successor candidate plugs into the same interfaces;
- the gate battery itself (this document's G1–G7 with controls) becomes the standing
  admission test for any successor candidate, per `SPEC.md` §8–10;
- the (N)-level harness (in-repo candidate generation + gates + null/positive controls)
  remains worth building — its first target is now *measuring `√τ‖u‖_∞` growth*, i.e.
  testing the only live escape hatch, rather than reproducing a killed scaling.

**Reopen condition** (PROJECT_GOAL registry discipline): a candidate diagnostic, converged
across resolutions, showing `√τ‖u(t)‖_{L∞}` unbounded as `t → T*` (genuine Type II), or an
explicitly non-axisymmetric candidate class.

## 5. Strategic consequence for the 10-scale

The direct 2.8 → 5 jump *through the current Hou NS candidate* is closed by theorem, not by
missing engineering. The honest 5/10 target is re-specified: conditional Chen–Hou-style
skeleton (Stage B) + a **Type II-compatible** candidate passing this battery. This is
precisely the early answer Stage A was run to obtain.
