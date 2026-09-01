# TSEL_BRIDGE_DISCHARGE — 2026-09-02 (third session) — SEL-1 and SEL-4 PROVED; SEL-3/SEL-5 remain open with a sharpened technical map

**Commission (user, 2026-09-02, third session):** close the T-SEL bridge obligations in
the order SEL-1 → SEL-4 → SEL-3 → SEL-5, known mathematics only, full Lean proofs, no
new research assumptions, no proof search on `R3TSelHead`/`N0`; final goal: only `N0`
left as unproved input of `r3TSel_conditional_globalContinuation`.
`docs/formal/TSEL_BRIDGE_FORMALIZATION_2026-09-02.md` is the authoritative base record.

**Executed this session: SEL-1 and SEL-4 are fully PROVED** (the first two items in the
commissioned order). SEL-3 and SEL-5 remain open statement-Props; the final goal is
therefore **not yet reached** — the honest remaining distance is recorded in §4 below
and in `HANDOFF.md` (Next work). The head `N0` is untouched, per commission.

Base revision: `d4096d3`; this session's proof commits: `0565237` (SEL-1),
`bb1c473` (SEL-4), plus the documentation commit carrying this record.

---

## 1. SEL-1 PROVED — classical Sobolev comparability

`r3TSel_classicalSobolevComparability : R3TSelClassicalSobolevComparability`
(`Formal/R3TSelClassicalComparability.lean`), with explicit constants `c₁ = 1/81`,
`c₂ = 27(2π)⁶`:

`(1/81)·‖J³φ‖² ≤ ∑_{n ≤ 3} ‖D^n φ‖²_{L²} ≤ 27(2π)⁶·‖J³φ‖²` on the Schwartz core,
`D^n` the iterated Fréchet derivative under the operator norm, `‖J³φ‖` the carrier norm
of `r3SchwartzToHsCLM 3 φ`, plus the `MemLp` certificates.

Proof route: direction-tuple derivatives `∂^{v}φ` (mathlib's `iteratedLineDerivOp`,
pointwise equal to `iteratedFDeriv` on basis tuples); iterated
`SchwartzMap.fourier_lineDerivOp_eq` gives the exact frequency weight
`(2π)^{2n}∏ξ_{vᵢ}²`; Schwartz Plancherel (`SchwartzMap.integral_norm_sq_fourier`)
converts each tuple energy; `Fintype.sum_pow` collapses the tuple sum to `‖ξ‖^{2n}`;
the multilinear operator norm is compared two-sidedly with the tuple values (basis
expansion, Cauchy–Schwarz, dimension factor `3ⁿ ≤ 27`); the polynomial weight
`∑(2π)^{2n}r^{2n}` is compared pointwise with `(1+r²)³`; and the carrier norm is the
cubed-weight frequency energy by the repository's explicit Bessel-coordinate frequency
description.

## 2. SEL-4 PROVED — the BKM derivative-tuple commutator

`r3TSel_katoPonceCommutator : ∃ C, 0 ≤ C ∧ R3TSelKatoPonceCommutator C`
(`Formal/R3TSelLeibnizCommutator.lean`), with the explicit (unoptimized) constant
`C = 93(2π)³`: for every direction tuple `v` of length `n ≤ 3` and every Schwartz
velocity `φ`,

`‖∂^v((φ·∇)φ) − (φ·∇)(∂^v φ)‖_{L²} ≤ C·‖∇φ‖_{L∞}·‖J³φ‖_{L²}`.

### 2a. Statement decision (documented, per the no-new-assumptions discipline)

The session-2 formalization had stated SEL-4 in the **fractional Bessel form**
(`J³` commutator). That form is the sharp Kato–Ponce inequality (CPAM 41 (1988)),
whose known proofs need Littlewood–Paley/paraproduct technology absent from mathlib;
a session-3 feasibility analysis (recorded here) confirmed the frequency-side
symbol-difference routes cannot reach the `‖∇φ‖_{L∞}` coefficient (they produce
Wiener-algebra/`‖J³φ‖` coefficients instead).  The audit record's **own SS-6 SEL-4
statement is the `D^α` (derivative-tuple) form** — BKM CMP 94 (1984), ineq. (13) —
which is exactly what the `D^α` energy derivation of SEL-5 consumes.  The Lean Prop
`R3TSelKatoPonceCommutator` was therefore restated to the tuple form (commit
`bb1c473`), the reformulation distance being precisely the **now-proved** SEL-1
comparability.  The `J³`-form is consumed by nothing in the T-SEL chain and is
deliberately not restated; nothing about it is claimed in either direction.  The
divergence-free hypothesis of the paper statement is dropped (not needed for the
commutator; it is spent on the transport cancellation inside SEL-5).

### 2b. Proof infrastructure (all new, all Schwartz-core, `Formal/R3TSelSchwartzCalculus.lean`)

* `r3SchwartzSMul` with the exact product rule for `∂_{m}`; the convection as the sum
  of coordinate–derivative products;
* commutation of line derivatives from `C²` symmetry of the second Fréchet derivative
  (`ContDiffAt.isSymmSndFDerivAt` — **no analyticity**), iterated through tuples;
  commutation of `∂` with the coordinate projection;
* sup bounds: CLM operator norms by standard-basis values; `x ↦ ‖fderiv φ x‖` bounded;
  first derivatives pointwise below `r3SchwartzGradSup φ`;
* the single-tuple `L²` bound `‖∂^{v}φ‖_{L²} ≤ (2π)³‖J³φ‖` for `|v| ≤ 3`, extracted
  from the SEL-1 comparability machinery;
* **integration by parts on `ℝ³` via the Fourier transform at frequency zero**
  (`integral_fderiv_apply_eq_zero`): for integrable differentiable `H` with integrable
  derivative, `∫ ∂_m H = 0` — no boundary-term or density analysis;
* Cauchy–Schwarz for integrals (`integral_mul_le_sqrt_mul_sqrt`, bundled `L²` route);
* the **by-parts Gagliardo–Nirenberg quartic interpolation** `r3TSel_gn_quartic`:
  `∫|∂_q∂_p u|⁴ ≤ 9 S² ∫|∂_q∂_q∂_p u|²` whenever `S` bounds `∂_p u` pointwise — the
  `L⁴` step of BKM, proved by writing `|w|⁴ = (w̄²w)·w` and moving the outer derivative
  by parts, then Cauchy–Schwarz.

### 2c. Assembly (`Formal/R3TSelLeibnizCommutator.lean`)

Exact Leibniz commutator expansions at orders 1–3 (subset-free, one/three/seven
explicit terms); every scalar factor carries at least one derivative.  Three product
modes: sup on a first-order factor times a `≤ 3`-tuple `L²` bound (modes 1–2), and for
the balanced second×second products of order three, Cauchy–Schwarz into two quartics,
each `≤ 81·(‖∇φ‖_{L∞}(2π)³‖J³φ‖)²` by the GN lemma (with the sup landing on a
first-order factor) — mode 3.  Per-tuple totals: `1, 3, 31` times
`‖∇φ‖_{L∞}(2π)³‖J³φ‖` at orders 1, 2, 3; summing the three convection components gives
`C = 93(2π)³`.

### 2d. Ladder realness correction (session-3, part of `bb1c473`)

`R3TSelH3Ladder` now requires `IsR3RealVelocity u0`.  The transport cancellation
`re⟨V,(U·∇)V⟩ = −½∫(div U)|V|²` consumes a **real** transport field; for complex data
the imaginary part of the transport term is uncontrolled at `H³` energy level, so the
unrestricted ladder statement was not provable-as-stated (and is not known to be true).
SEL-8 supplies realness for every admissible datum, and the head/N3 quantify only over
admissible data, so the chain is unaffected: the realness hypothesis is threaded
through `r3TSel_carrierBound_of_ladder`, `r3TSel_uniform_carrierBound_of_head`,
`r3TSel_horizons_unbounded` (each gains `IsR3RealVelocity u0`), discharged in the
`N3` packagings by `IsR3AdmissibleSchwartzDatum.isR3RealVelocity_encode`.

## 3. Verification evidence

```text
runner: local Elan-pinned toolchain, lake + bash scripts/lean-ci-local.sh
toolchain: leanprover/lean4:v4.32.1; pinned lake-manifest unchanged
targeted: Formal.R3TSelClassicalComparability PASS (8750 jobs)
targeted: Formal.R3TSelSchwartzCalculus       PASS (8751 jobs)
targeted: Formal.R3TSelLeibnizCommutator      PASS (8752 jobs)
targeted: Formal.AxiomAudit                   PASS (8766/8768 jobs)
full pinned gate (source scan + lake build)   PASS — see HANDOFF entry for job count
axiom audit: every new printed theorem depends only on
  [propext, Classical.choice, Quot.sound]
forbidden-source scan: clean (no sorry/admit/axiom/opaque under Formal/)
```

## 4. What remains OPEN (honest map for the next session)

`R3TSelInteriorSobolevSmoothing` (SEL-3) and `R3TSelH3Ladder` (SEL-5) are still
statement-Props; `r3TSel_conditional_globalContinuation` still carries the ladder
hypothesis besides `N0`.  The session-3 feasibility analysis fixes the intended route
and its genuinely remaining obstacles:

1. **Mollified energy method** (Majda–Bertozzi-style), physical mollifier `ρ_ε * ·`:
   the mollified trajectory `U_ε` inherits a strong `L²` time derivative from the
   capstone through the bounded convolution operator, making
   `t ↦ ‖D^α U_ε‖²` differentiable without any smoothing theorem — this replaces the
   SEL-3 bootstrap as the load-bearing device (SEL-3 membership then falls out of the
   uniform-in-`ε` energy bounds rather than feeding them).
2. **Friedrichs commutator lemma** `‖[ρ_ε*, f·∇]g‖_{L²} ≤ C‖∇f‖_{L∞}‖g‖_{L²}`
   uniformly in `ε` — elementary kernel proof (mean value + Minkowski integral
   inequality); new Lean infrastructure (Minkowski for Bochner convolutions).
3. **SEL-4 for mollified fields**: the proved commutator is Schwartz-core; the energy
   method applies it to `ρ_ε * U` — smooth, all derivatives `L²`, first derivatives
   bounded, but *not* Schwartz.  The mode-1/2/3 machinery generalizes to that class;
   the Schwartz-specific ingredients (decay-based sup bounds, `memLp`, tuple bounds
   via Schwartz Plancherel) need class-level replacements (frequency-side multiplier
   bounds).  This is a refactor of `R3TSelSchwartzCalculus`/`R3TSelLeibnizCommutator`
   around a "mollified-regular field" class, not new mathematics.
4. **Transport cancellation for solutions**: `re⟨V, (U·∇)V⟩ = 0` with `V` mollified
   real and `U` the real `H³` decoded field — via Plancherel pairing and the certified
   a.e. vanishing of the frequency divergence (no physical by-parts needed); realness
   from the (new) ladder hypothesis.
5. **Passage to the limit** `ε → 0` and Grönwall (SEL-6, proved) close the integrated
   ladder; the `t₀ ↓ 0` endpoint is already absorbed in the integral form.

Warned-against dead ends (checked and rejected this session): frequency-side
symbol-difference commutator bounds (Wiener-algebra coefficient, not `‖∇U‖_{L∞}`);
sharp-cutoff truncation commutators (no uniform gs-coefficient bound); difference
quotients on the mild equation (quadratic coefficient; the pairing hits the `H⁴` wall).

## 5. Claim boundary

Unchanged from the base record: `N0` is OPEN, unclaimed, untouched (no proof search
performed); nothing here approaches the Millennium problem in either direction; the
frozen research map, round-4 park, watches, and M-1 hold are untouched.  The two
remaining open Props are never asserted; every `r3TSel_*` conditional theorem carries
its hypotheses explicitly.  SEL-4's `J³` fractional form is not claimed in either
direction.  C0 discipline maintained throughout.
