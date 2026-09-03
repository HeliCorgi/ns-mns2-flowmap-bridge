# PREREG — M-1 re-opened (twenty-seventh session, 2026-09-04): term-by-term budgets of enstrophy-growth events and the search for a sub-wall cancellation observable

**Status:** preregistration, committed BEFORE any run (house discipline). **EVIDENCE-GRADE / DIAGNOSTIC ONLY** — periodic box, certificate-inadmissible by the standing rule; no statement about certified `ℝ³` solutions, no blow-up claim, no regularity claim in either direction.

**Commissioning provenance.** User instruction (twenty-seventh session), paraphrased: *re-open M-1, not to prove blow-up numerically, but to study the conditional statistics / geometry of each exact NS term that composes an enstrophy-growth event, and to look for a new cancellation observable weaker than the known walls.* Interpretation recorded: the original M-1 content (Hou 2022 no-slip wall-vorticity closure, finite cylinder) is not needed for this objective and stays on file unstarted; the periodic pseudo-spectral solver validated in the T-GRAM probe (identity `G′ = −2νD − 2𝒫` at residual `∼4×10⁻⁴`) is reused, re-implemented with parametrised resolution and cross-validated against the stored R1 series.

## 1. Runs

| id | datum | `ν` | `N` | `T` | `dt` | role |
|---|---|---|---|---|---|---|
| E0 | Taylor–Green (= T-GRAM R1) | 0.02 | 64 | 3.5 | 0.0125 | cross-validation of the re-implementation (energy series must match `results/R1.json` to `10⁻⁸` relative) |
| E1 | Taylor–Green | 0.01 | 64 | 8.0 | 0.01 | the classical enstrophy-growth event (Brachet et al.) |
| E2 | antiparallel Gaussian vortex tubes (core `a = 0.4`, half-separation `0.8`, sinusoidal perturbation `ε = 0.2`), `u_rms = 1` | 0.01 | 64 (96 if E2 fails the tail rule) | 6.0 | 0.01 | coherent-tube stretching / flattening event (Kerr-type) |
| E3 | shear + band noise (= T-GRAM R4 datum) | 0.02 | 64 | 3.5 | 0.0125 | strongest growth event on file (`E: 2112 → 4714`) |
| E4 | random band `1 ≤ |k| ≤ 2`, `u_rms = 1` | 0.02 | 64 | 6.0 | 0.0125 | large-scale random datum with a cascade build-up phase |

Fail-closed resolution rule (as in the T-GRAM probe): a run enters the verdict only if its spectral tail fraction (`|k| ≥ 0.9k_cut`) stays `≤ 10⁻⁵`; otherwise it is diagnostic-only. Growth events = maximal time intervals on which the enstrophy `E = ‖ω‖²₂` increases (from a local minimum to the following local maximum), sampled at the full-diagnostic outputs.

## 2. Exact identities used (each verified numerically at every full output; tolerances fixed here)

- enstrophy budget `½dE/dt = ∫ωᵀSω − ν‖∇ω‖²`, with `∫ωᵀSω = Σ_i∫λ_iω_i² = −4∫det S` (`ω_i = ω·e_i`, strain eigenframe) — tolerance `10⁻⁶` relative between the three evaluations;
- `∫|ω|² = 2∫|S|²` — `10⁻¹⁰`;
- `|∇ω|² = |∇|ω||² + |ω|²|∇ξ|²` pointwise (defines the twist dissipation);
- pressure `Δp = ½|ω|² − |S|²` (spectral `p̂ = −k_ak_bF[u_au_b]/|k|²`) — `Σ_ip_{ii}` vs `½|ω|² − |S|²`: `10⁻⁶` relative `L²`;
- `∫S:∇²p = 0` — `10⁻⁶` relative to `∫|S||∇²p|`;
- the eigenvalue equation `D_tλ₂ = −λ₂² + ¼(|ω|² − ω₂²) − p_{22} + ν(ΔS)_{22}` (twenty-sixth record §2) — its right-hand side terms are recorded; the left side is not independently measured (no finite-difference check preregistered).

## 3. Observables (recorded at every full output, globally and conditioned on the sets `Ω_λ = {|ω| > λ‖ω‖_∞}`, `λ ∈ {0.5, 0.25}`, on `{λ₂ > 0}`, and at the maximum point `x_max`)

Term budgets: `E`, `P = ∫ωᵀSω`, `P_i = ∫λ_iω_i²`, `P_abs = Σ_i∫|λ_i|ω_i²`, `G = ∫|S||ω|²`, `ν∫|∇ω|²`, `ν∫|∇|ω||²`, `ν∫|ω|²|∇ξ|²`, `|ω|²`-weighted `⟨cos²θ_i⟩`, volume and enstrophy fractions of the sets; `λ₂`-equation terms `∫(−λ₂²)`, `∫¼|ω_{⊥2}|²`, `∫(−p_{22})`, `ν∫(ΔS)_{22}` on `{λ₂>0}∩Ω_λ`; at `x_max`: `Λ = |ω|`, `α = ξ·Sξ`, `|S|`, `ν|∇ξ|²`, `νΔ|ω|/|ω|`, and the near/far strain split `S = S_near + S_far` with `S_near` induced (Biot–Savart) by the vorticity inside the ball of radius `r_c = c(ν/Λ)^{1/2}`, `c ∈ {0.5,1,2}`: `α_near, α_far, |S_near|, |S_far|`; fat-core statistic: in-set fraction of the segment `x_max ± ρ d`, `ρ = c(ν/Λ)^{1/2}`, `c ∈ {0.5,1,2,4}`, for the seven directions `{e_x,e_y,e_z,e₁,e₂,e₃,ξ}` at threshold `λ = 0.4` (`≈ 1/(2M)`, `M = 1.25`), and the minimal in-set run length over those directions in units of `(ν/Λ)^{1/2}`.

**Candidate cancellation ratios (fixed now; a ratio is "systematic" if it is `≤ 0.5` at every full output inside every growth event of every resolved run):**
- **C1** `= P/G` (net stretching over gross strain–enstrophy product; geometric depletion);
- **C2** `= P/P_abs` (net over gross in the strain eigenframe; sign cancellation between compression and extension);
- **C3** `= [α − ν|∇ξ|² + νΔ|ω|/|ω|](x_max) / α(x_max)` (effective peak growth rate over stretching; twist + magnitude diffusion cancellation at the maximum) — reported also with the finite-difference `d/dt\log‖ω‖_∞` for consistency;
- **C4** `= ∫_{\{λ₂>0\}∩Ω_{0.25}}(−λ₂² + ¼|ω_{⊥2}|² − p_{22}) / ∫_{\{λ₂>0\}∩Ω_{0.25}}¼|ω_{⊥2}|²` (fraction of the vortical source of the middle eigenvalue surviving self-damping and the pressure Hessian; the pressure-Hessian shielding of `λ₂`);
- **C5** `= α_far/α` at `x_max` with `c = 1` (nonlocality of the stretching at the maximum) together with `C5′ = α/|S|` at `x_max`.

## 4. Verdict rule (fixed now)

- **OBSERVABLE-CANDIDATE**: at least one of C1–C5 is systematic (definition above) **and** the corresponding integrated quantity admits a free (energy-level) companion budget **and** a bridge shape to a continuation theorem can be written (the analytical assessment is part of the record, not of the numerics);
- **DIAGNOSTIC-ONLY**: cancellations measured, but no candidate satisfies all three clauses;
- **NEGATIVE**: no ratio is systematic in any resolved run.
Numerics cannot upgrade any statement beyond evidence grade; any candidate is a *proposal* for a later on-paper session, subject to the SYM-test and the per-solution-truth check before any promotion.

## 5. Not done / not claimed

No blow-up search; no extrapolation in `ν`; no Hou wall closure; no statement about `ℝ³`; no claim that a measured cancellation is a theorem. Results directory `results/` is preserved; excluded runs are kept and labelled.
