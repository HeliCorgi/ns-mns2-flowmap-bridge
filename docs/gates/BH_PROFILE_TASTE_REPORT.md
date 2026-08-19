# BH-profile taste report — localized quasi-static Euler cores vs the frozen Type II window

Date: 2026-08-19 (JST). Task specification: external reviewer's taste-task brief of
2026-08-19 (one bounded pass; stop rules observed: no Lean changes, no simulation, no
Stage B, no window modification, minimum literature).
Bookkeeping script: `experiments/bh_taste_exponents.py` (all checks pass).

## 1. Verdict — YELLOW

Localized steady axisymmetric Euler cores with swirl exist (Gavrilov; Constantin–La–Vicol),
but the frozen window demands a **swirl-poor, circulation-carrying family** `ε → 0`, and
that family cannot be regular: the swirl enters the Grad–Shafranov equation only at `O(ε²)`,
so a regular limit would be a nontrivial compactly supported no-swirl steady axisymmetric
Euler flow, which is dead by Jiu–Xin rigidity. Every admissible family must therefore
degenerate as `ε → 0`. On the Navier–Stokes side, the slow-modulation residual hierarchy is
structurally plausible — but only on the `α < 1/2` part of the interior wedge: for
`α ≥ 1/2` a closed-streamline (Prandtl–Batchelor-type) secular argument homogenizes the
core circulation, decouples the swirl, and re-triggers the same no-swirl rigidity. The
branch is neither green (the degenerating family is unconstructed) nor red (no
contradiction under the frozen constraints for `α < 1/2`). **Single smallest missing item:
a quantitative no-swirl rigidity theorem — how fast must `C^k` norms, support anisotropy,
or constitutive steepness of a compactly supported swirl-poor steady axisymmetric Euler
family blow up as `ε → 0`.** If that forced rate is a power of `1/ε`, the modulation
hierarchy likely breaks (RED-ward); if logarithmic, the branch becomes a genuine candidate
seed (GREEN-ward).

## 2. Scaling dictionary

`τ = T* − t`; frozen interior blob branch of `S_survive`:

| object | scale |
|---|---|
| core scale | `ℓ ~ τ^α` |
| poloidal amplitude | `‖u_pol‖ ~ τ^{−γ}` |
| swirl amplitude | `‖u_θ‖ ~ τ^{−σ}`, frozen `σ = α` |
| circulation | `Γ = r u_θ ~ ℓ·τ^{−α} = O(1)`, nontrivial |
| swirl/poloidal ratio | `ε(τ) = τ^{γ−α} → 0` |
| window | `1/2 < γ < 1`, `max(1−γ, 2γ/3, 2γ−1) ≤ α < γ`; interior: `γ+α > 1` |

Consistency: `Γ ~ ε · ‖u_pol‖ · ℓ = τ^{γ−α}·τ^{−γ}·τ^{α} = τ⁰` ✓.

## 3. Grad–Shafranov convention and nondimensional equation

Convention (recorded; Bragg–Hawthorne ≡ Grad–Shafranov up to notation):
`u = (1/r)∂_zψ e_r − (1/r)∂_rψ e_z + (1/r)F(ψ) e_θ`, so `Γ = F(ψ)`, and
`−Δ*ψ = ∂_ψ(F(ψ)²/2 + r²P(ψ))`, `Δ* = ∂_r² − (1/r)∂_r + ∂_z²`.

Rescale `x = ℓ ŷ`, `ψ = (U_pol ℓ²) ψ̂`, `F = ε U_pol ℓ F̂(ψ̂)`, `P = U_pol² P̂(ψ̂)` (this makes
poloidal `O(1)`, swirl `O(ε)`, and physical `Γ = O(1)` automatic). Then

**`−Δ̂*ψ̂ = ε² (F̂F̂′)(ψ̂) + r̂² P̂′(ψ̂)`.**

The swirl is an `O(ε²)` **regular perturbation** of the no-swirl problem. This single
formula drives Gates C/D.

## 4. Gate B — fixed-profile scaling: double no-go

`U_{A,L}(x) = A·U(x/L)` multiplies poloidal and swirl by the same `A`:

- matching `‖u_pol‖`: `A = τ^{−γ}` gives `σ = γ ≠ α` — K9 violated; moreover
  `Γ ~ A·L = τ^{α−γ} → ∞` — violates the hard swirl maximum principle;
- re-tuning to preserve `Γ = O(1)`: `A ~ 1/L` gives `γ = α` — outside the window (ESŠ).

A fixed profile cannot realize the frozen scaling under either tuning. At least one
additional degenerating internal parameter (the swirl/poloidal ratio) is mandatory.

## 5. Gate C — swirl-poor compactness / no-swirl limit obstruction

**Proposition (conditional).** Let `V_ε` be normalized profiles (poloidal `O(1)`, swirl
`O(ε)`), each a steady axisymmetric Euler flow, with (i) supports contained in a fixed ball
in core variables; (ii) uniform `C^{1,β}` bounds; (iii) normalized poloidal sup bounded
below; then a subsequence converges in `C¹` to a nontrivial compactly supported
axisymmetric **swirl-free** steady Euler flow, provided (iv) the limit lies in the class of
the rigidity theorem. By Jiu–Xin (CMP 287, 2009: a compactly supported axisymmetric
no-swirl steady Euler solution vanishes), this is a contradiction.

**Exact roles:** (i)+(ii) give compactness (Arzelà–Ascoli) and let the quadratic term pass
to the limit (uniform convergence suffices for the weak form; `C¹` keeps the limit
classical); (iii) blocks the trivial limit; (iv) is the rigidity class membership
(smooth/`C¹`, compact support, axisymmetric, no swirl — verified at search level from the
Jiu–Xin statement; first-hand class check is a footnote-level residue).

**What a surviving family must sacrifice (at least one):** uniform `C^{1,β}` bounds
(gradient blow-up as `ε → 0`); uniform support control in core variables (support thinning
to a lower-dimensional set or escaping — e.g. torus thinning, or drifting to `R ≫ ℓ`, which
exits the blob branch into the ring corridor); the nontrivial poloidal limit; smooth
constitutive dependence (steepening `F̂′`, non-Lipschitz `P̂′`); or classical regularity of
the limit (dropping below the rigidity class).

## 6. Gate D — small-swirl Grad–Shafranov family: no regular family

From §3, at `ε = 0` the equation is the pure no-swirl problem
`−Δ̂*ψ̂ = r̂²P̂′(ψ̂)`. A **regular** family (uniformly controlled as `ε → 0`) would converge
to a nontrivial localized solution of it — dead by Jiu–Xin. If instead both right-hand
terms degenerate, `Δ̂*ψ̂ → 0` with compact support forces `ψ̂ → 0` (elliptic uniqueness) and
the poloidal amplitude dies. Hence:

- **regular family: impossible** (conditional only on the verified rigidity);
- **singular family: not excluded** — the constraints are mutually consistent at the
  power-counting level provided the degeneration list of Gate C is entered deliberately;
- **no family: not established** — no contradiction under the frozen constraints alone.

Classification: **singular family required; existence unconstructed.** A singular family is
not yet a Navier–Stokes seed (task definition).

## 7. Gate E — fixed-ν NS residual τ-power table

Modulated ansatz: `u = τ^{−γ}[V_pol(y; ε(t)) + ε V_θ e_θ]`, `y = x/τ^α`, `ε = τ^{γ−α}`,
steady-Euler pair cancelling at order `τ^{−(2γ+α)}`. Magnitudes (script-verified):

| residual component | τ-power | relative to Euler pair |
|---|---|---|
| cancelled Euler pair (reference) | `−(2γ+α)` | `τ⁰` |
| amplitude + scale-drift modulation | `−(γ+1)` | `τ^{γ+α−1}` |
| swirl-parameter drift (`ε̇`) | `−(α+1)` | `τ^{2γ−1}` |
| viscous, poloidal | `−(γ+2α)` | `τ^{γ−α}` |
| viscous, azimuthal (vs `θ`-transport) | `−3α` | `τ^{γ−α}` |
| pressure corrector | enslaved (Leray) | — |

Interior wedge: all relative orders positive ⇒ the corrector problem is formally
perturbative; on the edge `γ+α = 1` the modulation joins the leading balance (unsteady
Euler), as the map already records.

**Secular check (the part instantaneous smallness misses).** The quasi-static core has
closed poloidal streamlines; averaging the `Γ`-equation over them cancels advection, so the
viscous flux acts secularly at rate `~ ν/ℓ²` against the remaining time `τ`:
ratio `ν τ^{1−2α}`. For `α < 1/2` the collapse outruns homogenization; for `α ≥ 1/2` the
circulation homogenizes, `F̂′ → 0`, the `ε²F̂F̂′` coupling dies, and the poloidal core must
solve the pure no-swirl problem — dead again by rigidity. **Proposed conditional cut K12
(report-only, NOT applied to the frozen map): the quasi-static interior branch requires
`α < 1/2`,** i.e. `{γ ∈ (1/2, 3/4), max(1−γ, 2γ/3) ≤ α < min(1/2, γ)}`. Status [B]+[C]
(Prandtl–Batchelor reasoning is formal; rigorous PB theorems cover restricted settings).

## 8. First-corrector solvability verdict

`L_BH W ≈ −R_NS` around the localized profile: the kernel directions of `L_BH`
(translation along the axis, scale, swirl-ratio) are exactly matched by the free modulation
functions (amplitude/scale drift, `ε̇`), which is the standard modulation-theory structure;
the closed-streamline solvability conditions are the genuine constraints and are satisfiable
precisely when the K12 condition `α < 1/2` holds (they otherwise force the secular
homogenization above). **Not immediately obstructed on the `α < 1/2` sub-wedge; obstructed
for `α ≥ 1/2`.** No full stability claim is made or implied.

## 9. Comparison with Gavrilov / Constantin–La–Vicol

Gavrilov (arXiv:1810.08020, GAFA 2019) constructs a nontrivial smooth compactly supported
steady 3D Euler flow whose hallmark is the *dependence between the Bernoulli function and
the pressure*; Constantin–La–Vicol (arXiv:1903.11699, GAFA 2019) systematize this as
localizable Grad–Shafranov equations (verified at abstract level). These give the Gate A
sanity: localized BH cores with swirl exist **at fixed swirl fraction**. What the frozen
window needs and what they do not provide is a **degenerating swirl-poor family** with
uniform localization — by Gates C/D such a family must be singular, and the natural locus
of the forced degeneration is exactly the free-boundary constitutive tangency that makes
their constructions localizable.

## 9bis. Erratum (2026-08-19, ring audit P3 — appended, not silently repaired)

§3's equation `−Δ*ψ = ∂_ψ(F²/2 + r²P(ψ))` is the **MHD Grad–Shafranov** form. For
hydrodynamic steady axisymmetric Euler the correct identity is
`Δ*ψ = r²B′(ψ) − FF′(ψ)` with `B = p + |u|²/2` the Bernoulli head — i.e. this file's
`P(ψ)` must be read as `−B(ψ)`, **not** as the pressure. Consequences: (i) the frozen
branch does **not** covertly assume CLV-localizability (`p = p(ψ)` is a genuinely
stronger, added hypothesis — load-bearing for the 2026-08-19 ring audit's scope ruling);
(ii) the `O(ε²)` structure of the swirl term and Gates C/D are unaffected.

## 10. Effect on S_survive

**None to the frozen map** (stop rule respected). Two report-level annotations for the next
freeze cycle: (a) proposed conditional K12 (`α < 1/2` on the quasi-static interior; would
newly bind only for `γ > 3/4`, where it empties the interior branch, and restricts
`γ ∈ (1/2, 3/4)` to `α < 1/2`); (b) the interior branch's viability now hinges on one
quantifiable object — the degeneration rate forced by no-swirl rigidity — recorded as the
smallest missing theorem in §1.
