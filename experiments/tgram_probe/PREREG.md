# PREREGISTRATION — T-GRAM specialization stress-test / probe (2026-09-04, eighteenth session)

**Commission.** User instruction (eighteenth session): compute `A(T′) = ∫₀^{T′}G(t)dt`, its minimal eigenspace `E_min(T′)`, observe `B(T′) = inf_{e∈E_min∩S²}∫₀^{T′}(−eᵀ𝒫(t)e)₊dt` against the unrestricted `B_all(T′) = inf_{e∈S²}∫₀^{T′}(−eᵀ𝒫(t)e)₊dt`, and test whether `R(T′) = B/B_all` grows dangerously. Verdict ∈ {CANONICAL-STABLE / CANONICAL-ADVERSE / UNDETERMINED}; ADVERSE ⟹ park T-GRAM, revert to T-DIR-SPK; STABLE ⟹ T-GRAM proof search is commissioned by the same instruction.

**Scope and admissibility (fixed before any run).** EVIDENCE-GRADE ONLY. Runs are pseudo-spectral DNS on the periodic box `T³ = [0,2π)³` — the torus is certificate-inadmissible by standing rule and the certified class is ℝ³-Schwartz; outcomes are evidence about the stability of the canonical-direction specialization (the ratio `R`), not statements about certified solutions. Outcomes are graded only through the preregistered thresholds below. Fail-closed: any run failing validation is EXCLUDED from the verdict and reported as failed; no reruns with tuned parameters are admitted into the verdict set (extra diagnostic reruns may be reported separately, marked non-verdict).

**Solver (fixed).** Incompressible NS, ν explicit, rotational form `∂_t u = u×ω − ∇P_tot + νΔu` with spectral Leray projection, 2/3-rule dealiasing (`k_cut = ⌊N/3⌋`), RK4, fixed `dt`, resolution `N = 64` (real-to-complex FFTs). Observables computed every 2 steps from the spectral state: `energy = ‖u‖₂²`, Gram `G_ij = ∫∂_iu·∂_ju`, dissipation tensor `D_ij = ∫∇∂_iu:∇∂_ju` (Fourier), production tensor `𝒫_ij = ∫(∂_iu)ᵀS(∂_ju)dx` (physical products), spectral-tail metric `tail = E(|k| ≥ 0.9k_cut)/E_total`.

**Runs (fixed; seeds fixed).**
- R1 Taylor–Green: `u = (sin x cos y cos z, −cos x sin y cos z, 0)`, ν = 0.02.
- R2 anisotropic random band: div-free random field, modes `1 ≤ |k| ≤ 4`, seed 1, x₃-weighted anisotropy (spectral weight `1+2k₃²/|k|²`), normalized to `u_rms = 1`, ν = 0.035.
- R3 isotropic random band: same band, seed 2, no weight, `u_rms = 1`, ν = 0.035 (degeneracy stress for `E_min`).
- R4 two-orientation shear superposition + 10% random background, seed 3, `u_rms = 1`, ν = 0.02 (rotating-anisotropy-flavored stress).
- R5 small-data control: R2 field × 0.05, ν = 0.035 (expected trivially stable; validates pipeline).
- All: `T = 3.5`, `dt = 0.0125` (280 steps).

**Validation criteria (fail-closed, fixed).**
- V1 energy balance: median relative residual of `d/dt(½‖u‖²) + ν·trG` over interior observation times ≤ 5% (relative to `max(ν·trG)`).
- V2 matrix-identity check (Y-1): median relative Frobenius residual of `G′ + 2νD + 2𝒫` ≤ 10% (finite-difference `G′` at observation cadence; denominator `‖2νD‖_F + ‖2𝒫‖_F + 10⁻¹²`). This doubly validates code and the derived identity.
- V3 resolution: `max_t tail ≤ 10⁻⁵`.
- A run passes iff V1∧V2∧V3.

**Estimators (fixed).**
- `A(T′)`: cumulative trapezoid of `G`. `E_min`: `numpy.linalg.eigh`; degeneracy rule: if `(λ₂−λ₁)(A) < 0.02·(trA/3)`, `E_min` = span of the two (or three, same rule for λ₃) lowest eigenvectors; `B(T′)` = min of the budget over 360 (2-D) / Fibonacci-241 (3-D) samples of `E_min∩S²`; else the single eigenvector (±).
- Budget per direction: trapezoid of `(−eᵀ𝒫(t)e)₊`.
- `B_all(T′)`: min over a 2000-point half-Fibonacci sphere, refined by 60 local perturbations (radius 0.05, renormalized) around each of the best 10 directions.
- Regularized ratio: `R̃(T′) = (B+δ)/(B_all+δ)`, `δ = 10⁻⁶·(1+trG(0))`; raw `B, B_all` also reported.

**Verdict thresholds (fixed).** Evaluate `R̃(T′)` on observation times `T′ ≥ T/4`. Per resolved run: STABLE iff `max R̃ ≤ 3`; ADVERSE iff `max R̃ ≥ 10`, or `R̃(T) ≥ 5` with `R̃` monotone nondecreasing (within 5% tolerance) over the last half; else UNDETERMINED. Global: **CANONICAL-ADVERSE** iff ≥ 1 resolved run is ADVERSE; **CANONICAL-STABLE** iff ≥ 3 runs resolved and ALL resolved runs STABLE; otherwise **UNDETERMINED**.

**Consequences (per the commission, fixed).** ADVERSE ⟹ T-GRAM parked, operative head reverts to T-DIR-SPK(∃e). STABLE ⟹ T-GRAM proof search stands commissioned. UNDETERMINED ⟹ neither; report and stop.

**Evidence handling.** All configs/seeds above are fixed by this file before execution; outputs go to `experiments/tgram_probe/results/` (never overwritten); the record will list commands and the pass/fail table.
