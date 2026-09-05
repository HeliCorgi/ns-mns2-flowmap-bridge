# Dominant-balance inversion — what dynamics does NS itself demand inside S_survive?

Date: 2026-08-19 (JST). Inputs: the frozen survival set of
[`TYPE2_KILL_TABLE_2026-08-19.md`](TYPE2_KILL_TABLE_2026-08-19.md). One pass, per plan; the
purpose is not to build a candidate but to determine which leading-order balances of the
Navier–Stokes equation are even possible inside the surviving wedge.

Status labels as in the kill table ([H]/[B]/[D]/[C]). Everything below is at the same
ansatz-bookkeeping level [B] as the map itself unless marked otherwise.

## 1. Term exponents at the core

Blob core: amplitude `U ~ τ^{−γ}`, scale `ℓ ~ τ^{α}`, `τ = T* − t`. Since the amplitude
itself grows like `τ^{−γ}` at core points, `|∂ₜu| ≳ U/τ` where the amplitude is achieved.

| NS term | magnitude | exponent |
|---|---|---|
| `∂ₜu` | `U/τ` | `−(γ + 1)` |
| `(u·∇)u` | `U²/ℓ` | `−(2γ + α)` |
| `∇p` | `~ U²/ℓ` (Calderón–Zygmund from `Δp = −div div(u⊗u)`; outer-field contribution subleading under the ansatz) | `−(2γ + α)` |
| `νΔu` | `νU/ℓ²` | `−(γ + 2α)` |

## 2. Pairwise dominance inside the wedge

- **Convection vs. diffusion:** `(u·∇)u / νΔu ~ ν^{-1}τ^{−(γ−α)}`; the wedge has `α < γ`
  (K6), so **convection dominates diffusion everywhere in the wedge**; the core Reynolds
  number `Re_core ~ Uℓ/ν ~ τ^{α−γ}/ν → ∞`. Consequence for the question raised in review:
  a balance `(u·∇)u ~ νΔu` requires `γ = α`, which is impossible for a core that carries
  the critical-norm divergence; it can only occur in multi-region designs where another
  scale carries `L³`.
- **Convection vs. time derivative:** convection reaches `∂ₜu` iff `γ + α ≥ 1`.
- **Diffusion vs. time derivative:** diffusion reaches `∂ₜu` iff `α ≥ 1/2`; inside the
  wedge `γ > 1/2`, so `α ≥ 1/2` already forces `γ + α > 1`.

**[K11] New cut, `γ + α ≥ 1` (double derivation).**
(i) *Term balance:* if `γ + α < 1` in the wedge then convection, pressure gradient, and
diffusion are all `≪ ∂ₜu`, and no term can respond to the growing amplitude — the equation
cannot hold. (ii) *Energy flux:* core energy `U²V ~ τ^{−2γ+3α}` grows at rate
`τ^{−2γ+3α−1}`, while the convective supply through the core boundary is
`U³ℓ² ~ τ^{−3γ+2α}`; supply ≥ growth forces `−3γ+2α ≤ −2γ+3α−1`, i.e. `γ + α ≥ 1`. Two
independent derivations agree.

Refined wedge:
`S_blob = {1/2 < γ < 1, max(1−γ, 2γ/3, 2γ−1) ≤ α < γ}`,
lower envelope `1−γ` on `(1/2, 3/5]`, `2γ/3` on `[3/5, 3/4]`, `2γ−1` on `[3/4, 1)`;
nonempty for every `γ ∈ (1/2, 1)`.

## 3. Classification of admissible balances

1. **Edge `γ + α = 1` (`γ ∈ (1/2, 3/5]`): generalized self-similar Euler balance.**
   `∂ₜu ~ (u·∇)u ~ ∇p ≫ νΔu` (viscous ratio `τ^{2γ−1} → 0`). Rescaling
   `u = τ^{−γ}U(x/τ^{α}, s)`, `s = log(1/τ)` gives the self-similar Euler profile system
   with anomalous exponent pair `(γ, 1−γ)` plus a vanishing viscous correction.
   **Independent convergence:** this edge is *exactly* Seregin's Euler-scaling Type II
   class (K10: `γ = α_S/(α_S+1) ∈ (1/2, 3/5)`, `α = 1 − γ`), where conditional exclusions
   (vanishing self-similar/DSS limit profiles, no swirl surviving the limit) already apply.
   The most reachable part of the wedge is contested territory.
2. **Interior `γ + α > 1`: quasi-static Euler cores.**
   `(u·∇)u ~ ∇p ≫ ∂ₜu ≫ νΔu`: to leading order the core must satisfy the *steady*
   axisymmetric Euler equations — i.e. a Bragg–Hawthorne (Squire–Long) profile — slowly
   modulated on the collapse timescale, with the time derivative entering at relative order
   `τ^{γ+α−1}` and viscosity at `ν τ^{γ−α}`. Under the K9 razor the profile carries `O(1)`
   swirl circulation `Γ` while its swirl amplitude is subdominant (`σ = α < γ`).
3. **Impossible in the wedge:** pure heat balance (`∂ₜu ~ νΔu` needs `γ < 1/2`),
   time-derivative-dominant dynamics (K11), convection–diffusion balance at an
   `L³`-carrying core (`γ = α` excluded).

Consistency re-checks (per plan):
- **Energy/dissipation/L³:** unchanged (K5/K6 did not involve time); K11 is *implied* by
  the energy-flux budget, so no new tension.
- **Γ-equation:** `∂ₜΓ + u·∇Γ = ν(ΔΓ − 2∂_rΓ/r)`; at the core, advection dominates
  (`γ + α > 1` ⇒ `u·∇Γ ≫ ∂ₜΓ`) and the viscous term is smaller by `ν τ^{γ−α}` — Γ is
  transported to leading order, consistent with the maximum principle and with `Γ ~ O(1)`
  at the core (K9 razor).
- **Scale count:** the edge and interior balances are self-consistent as **one-scale**
  (blob) structures; ring variants inherit the prior constraints (K3: `γ > ρ` or mesoscale
  violation; K8 conditional); swirl-dominated designs remain ≥ 3-region (K6/D2).

## 4. Fixed-ν self-consistency verdict

Every surviving balance is **asymptotically inviscid**: viscosity enters only as a
vanishing correction (relative size `ν τ^{γ−α}`), with `Re_core → ∞`. Standard fixed-ν NS
must therefore sustain an Euler-type focusing mechanism *against* viscous damping at
growing local Reynolds number — either genuinely unsteady generalized self-similar Euler
dynamics (edge, conditionally contested by K10) or a quasi-statically modulated
Bragg–Hawthorne core (interior). This is precisely the regime where Hou's constant-ν
transfer tests failed empirically (growth < 2), which is now explained structurally: at the
tested parameters the flow sat outside the wedge, where viscosity is *not* subdominant.

**Answer to the guiding question:** membership in `S_survive` forces the NS dynamics to be
Euler-dominated at the core; the only remaining choices are "unsteady self-similar Euler on
the contested edge" or "steady-Euler profile with slow modulation in the interior". A
convection–diffusion-balanced (`γ = α`, Type-I-like local Reynolds) singular core is
arithmetically incompatible with carrying the critical norm. The next research-grade
question, deferred by plan until after Lean Stage 0: do Bragg–Hawthorne profiles compatible
with `σ = α`, `O(1)` circulation, and the wedge exponents exist at all?

## Erratum (2026-09-01, synthesis audit — appended, not silently repaired)

**§3 item 1: the heading interval `(1/2, 3/5]` and the clause "this edge is *exactly*
Seregin's Euler-scaling Type II class" are inconsistent with the item's own K10 cite
two lines later (`γ ∈ (1/2, 3/5)`).** The K10 image is the open interval
(`m₀ ∈ (2/5, 1)` ⟹ `m ∈ (1/2, 1)` ⟹ `γ = α_S/(α_S+1) ∈ (1/2, 3/5)`); the edge point
`(γ, α) = (3/5, 2/5)` lies on the `γ + α = 1` edge but outside the class. "Exactly"
holds only on `γ ∈ (1/2, 3/5)`; K10's conditional exclusion pressure does not reach
the endpoint `γ = 3/5`. (Kill-table queue item F39; survival-map erratum recorded
likewise.)

## Erratum (2026-09-06, modulation-compactness audit — appended, not silently repaired)

**§1/§3 item 2/§4 overstate the size of the full time derivative in the K11 interior.**
The amplitude-growth argument supplies a lower-scale requirement `|partial_t u| >=~ U/tau`
at an amplitude-achieving point; it does **not** prove the universal asymptotic equality
`|partial_t u| ~ U/tau` for the entire core field. A normalized shape may evolve on the
faster convective clock while its fitted amplitude and length drift on the slower collapse
clock.

With the exact dynamic normalization

`u(x,t)=U(t) v((x-x_c(t))/ell(t),s)`, `ds/dt=U/ell`,

one obtains

`partial_s v + (v.grad)v + grad q - (x_c'/U).grad v`
`  + delta [gamma v + alpha (y.grad)v] = eps Delta v`,

where

`delta=tau^(alpha+gamma-1)->0`, `eps=nu tau^(gamma-alpha)->0`

in the interior. The coefficient of `partial_s v` is exactly one. Hence the general leading
core equation is **unsteady Euler**, not steady Euler. `gamma+alpha>1` makes the scale/amplitude
modulation slow compared with the convective dynamics; it does not force shape stationarity.

The K11 cut `gamma+alpha>=1` itself is **unchanged**: its amplitude-response logic and the
independent energy-flux derivation remain valid. What is withdrawn is only the unconditional
classification "interior => quasi-static / steady-Euler fixed shape". A steady
Bragg--Hawthorne profile is now treated as an additional shape-locking specialization, exactly
as recorded in `B2_MODULATION_COMPACTNESS_DECISION_2026-09-06.md`.
