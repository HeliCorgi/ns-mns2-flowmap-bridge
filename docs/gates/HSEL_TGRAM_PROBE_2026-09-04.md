# HSEL_TGRAM_PROBE — 2026-09-04 — the T-GRAM specialization stress-test / probe: preregistered, fail-closed, EVIDENCE-GRADE; VERDICT: CANONICAL-ADVERSE — T-GRAM is PARKED and the operative head reverts to T-DIR-SPK(∃e) (numerical probe record)

**Repo:** `c:/Users/corgi/Downloads/ns-mns2-flowmap-bridge` · **Status:** numerical-probe record, EVIDENCE-GRADE ONLY (periodic-box DNS — the torus is certificate-inadmissible by standing rule; the certified class is ℝ³-Schwartz; outcomes bear on the *stability of the canonical-direction specialization*, i.e. the commissioned ratio question, not on certified-class statements). No Lean file touched; no proof search; nothing frozen moved. Lean baseline unchanged (8775-job gate).

**Commissioning provenance.** User instruction, 2026-09-04 (eighteenth session): compute `A(T′) = ∫₀^{T′}G dt`, its minimal eigenspace `E_min(T′)`, observe `B(T′) = inf_{e∈E_min∩S²}∫(−eᵀ𝒫e)₊dt` vs the unrestricted `B_all(T′)`, and test whether `R = B/B_all` grows dangerously. Verdict ∈ {CANONICAL-STABLE / CANONICAL-ADVERSE / UNDETERMINED}; ADVERSE ⟹ park T-GRAM and revert to T-DIR-SPK; STABLE ⟹ T-GRAM proof search commissioned. **Preregistration committed before any run** (`experiments/tgram_probe/PREREG.md`, commit `906601f`): solver spec, five fixed families R1–R5, validation criteria V1–V3, estimators, thresholds, consequences.

**Execution.** Solver `experiments/tgram_probe/tgram_probe.py` (64³ pseudo-spectral, rotational form, Leray projection, 2/3 dealias, RK4, `dt = 0.0125`, `T = 3.5`); post-processing `postprocess.py` (preregistered estimators); outputs `experiments/tgram_probe/results/*.json`. Smoke validation before the runs: Taylor–Green initial energy exact vs analytic (62.01255…), divergence at machine zero, viscous decay matching prediction, and the **Y-1 matrix-identity residual ≈ 3.7×10⁻⁴** — a joint validation of the code and the derived identity `G′ = −2νD − 2𝒫`. Commands: `python tgram_probe.py R1 R2 R3 R4 R5` then `python postprocess.py`.

---

## §1 — Validation and run table (fail-closed)

| Run | V1 (energy bal., med.) | V2 (Y-1 residual, med.) | V3 (max tail) | Resolved? | max R̃ (T′ ≥ T/4) | R̃(T) | Run verdict |
|---|---|---|---|---|---|---|---|
| R1 Taylor–Green | 0.0000 | 0.0000 | 2.9×10⁻⁸ | **PASS** | 1.000 | 1.000 | STABLE |
| R2 anisotropic band | 0.0000 | 0.0001 | 3.6×10⁻⁵ | FAIL (V3) | 1.026 | 1.025 | (diagnostic only) |
| R3 isotropic band | 0.0000 | 0.0001 | 3.6×10⁻⁵ | FAIL (V3) | 1.018 | 1.018 | (diagnostic only) |
| R4 shear superposition | 0.0001 | 0.0002 | 4.8×10⁻⁵ | FAIL (V3) | 1.056 | 1.056 | (diagnostic only) |
| R5 small-data control | 0.0000 | 0.0001 | 1.1×10⁻¹⁷ | **PASS** | **309.1** | **17.3** | **ADVERSE** |

R2–R4 exceeded the preregistered tail threshold (10⁻⁵) by 3.6–4.8× — under-resolved per V3, **excluded from the verdict** (fail-closed; no tuned reruns admitted). V1/V2 residuals ≤ 2×10⁻⁴ across ALL runs — the solver and the Y-1 identity are strongly validated everywhere.

## §2 — The adverse signal (R5) and its mechanism

R5 (the small-data control, fully resolved) shows a **persistently large ratio**: `B ≈ 3.3×10⁻²` vs `B_all ≈ 1.9×10⁻³` at `T` (R̃ ≈ 17), spiking to R̃ ≈ 309 early (`B_all = 0` at the first sample; δ-regularized). Both budgets are absolutely tiny — **T-GRAM itself would numerically HOLD in R5 with a tiny `Q₀`** — but the commissioned and preregistered question was the RATIO, and it fires the ADVERSE threshold (`max R̃ ≥ 10`).

**Mechanism reading [D, diagnostic]:** in the Stokes-dominated regime, both the canonical direction `ē` (the `λ_min`-eigenvector of `∫G dt`, locked to the datum's anisotropy — R5 inherits R2's x₃-weighting) and the production tensor's frame (locked to the datum's decaying cubic correlations) are **data-frozen with no dynamical mixing**; nothing ties the `L¹`-optimal direction to the production-optimal one. By contrast, all four *nonlinear* runs — including the three V3-excluded ones, reported as diagnostics only — show `R̃ ≈ 1.00–1.06`: the canonical direction is near-optimal exactly when the dynamics is active (and R1's 1.000 is partly definitional — triple degeneracy makes `E_min` the whole sphere). **The specialization's optimality margin is thus unbounded precisely where the dynamics is weakest** — a structural fragility of the canonical choice, not a smallness artifact of the test: the preregistered criterion measured what the commission asked.

## §3 — VERDICT and consequences (per the preregistered rules and the commission)

**GLOBAL VERDICT: CANONICAL-ADVERSE** (≥ 1 resolved run ADVERSE; resolved set = {R1 STABLE, R5 ADVERSE}).

- **T-GRAM is PARKED** (on file with its proved reduction and the Y-1/Y-2 yields, which are unaffected — they are theorems of the record regardless of the specialization's fate).
- **The operative head REVERTS to T-DIR-SPK(∃e)** — the ∃-direction production budget `∃e ∈ S²: ∫₀^{T′}(−eᵀ𝒫(t)e)₊dt ≤ Q₀(ν,T,M)` — whose position is unchanged and unweakened: the proved quadratic-damping reduction (or directly the Y-1 sup-arrow along the chosen `e`), DQ-1, and the V-15-verified quantitative M-only bridge all consume only ∃e. T-GRAM's proof value survives as: *any* future proof producing a budget along *any* fixed direction suffices; the canonical `ē` just cannot be relied on as the direction.
- **T-GRAM proof search is NOT commissioned** (the STABLE branch did not obtain). No other commissioning follows automatically.
- Diagnostic notes for any future re-test (proposals only): (i) an absolute-scale-gated ratio criterion (ignore R̃ when `B_all` and `B` are both below a datum-scaled floor) would separate the harmless small-data misalignment from a genuinely dangerous one — the current preregistration deliberately did not include such a gate and the verdict stands under it; (ii) higher resolution (96³+) or larger ν would resolve R2–R4-class runs, whose diagnostic R̃ ≈ 1 suggests the nonlinear-regime picture is favorable to ∃e-heads.

## §4 — Claim boundary

EVIDENCE-GRADE numerical probe on `T³`; no statement about certified ℝ³ solutions, regularity, or any open head's truth is made in either direction. **Nothing here asserts, approaches, or implies a resolution of the Navier–Stokes Millennium problem.** The verdict adjudicates only the commissioned specialization-stability question under the preregistered thresholds, fail-closed; the excluded runs are reported, not hidden; evidence files are preserved under `experiments/tgram_probe/results/` (never overwritten). The Y-1/Y-2 mathematical yields and the T-DIR-SPK(∃e) head are unaffected; commissioning anything downstream (probe re-test, T-DIR-SPK proof work) is a user act. C0 discipline throughout.
