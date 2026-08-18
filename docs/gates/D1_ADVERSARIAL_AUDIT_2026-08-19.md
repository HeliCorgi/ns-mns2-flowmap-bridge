# Adversarial audit of [D1] (the ρ < 1/2 ring kill) — verdict: UNSOUND as stated, replaced

Date: 2026-08-19 (JST). Target:
[`TYPE2_SURVIVAL_MAP_2026-08-18.md`](TYPE2_SURVIVAL_MAP_2026-08-18.md) §4 [D1].

## 1. The claimed argument

A ring at radius `R ~ τ^ρ` with amplitude `τ^{−γ}` visits a fixed point `x₀`, `|x₀| = d`, at
time-distance `τ_visit = d^{1/ρ}`; for `ρ < 1/2` the visit lies inside the parabolic
cylinder `Q_d(x₀, T*)`; CKN ε-regularity at the regular point `(x₀, T*)` bounds `|u| ≤ C/d`
there; the ring amplitude `d^{−γ/ρ}` then forces `γ ≤ ρ < 1/2`, contradicting Type II.

## 2. The gap (audit finding)

The step "`(x₀, T*)` regular ⇒ `|u| ≤ C/d` on `Q_{d/2}(x₀, T*)` with universal `C`" is
**not a theorem**. What regularity of `(x₀, T*)` gives is boundedness of `u` on *some*
parabolic neighborhood `Q_{r₀(x₀)}(x₀, T*)` with *point-dependent* `r₀(x₀)` and constant.
The scale-invariant bound `|u| ≤ C/d` at scale `d` follows from CKN ε-regularity **only if
the scaled local quantities at scale `d` are below the ε-threshold** — a quantitative
smallness assumption on the solution near `x₀` at scale `d` that is not available for free;
the passing ring is precisely a mechanism that can make those local quantities large at the
visited scale. Largeness at one scale does not make `(x₀, T*)` singular either (the CKN
criterion is a smallness-at-some-scale test, so failure at one scale proves nothing), so no
contradiction with the measure-zero singular set can be extracted this way. The argument is
circular where it matters. **[D1] is withdrawn as a hard cut.**

## 3. Sound replacement [D1′] (weaker, hypothesis-labeled)

**Hypothesis (T):** the singular structure is materially transported: its radial position
changes no faster than advection by the flow plus viscous spreading,
`R(τ₀) ≲ ∫₀^{τ₀} ‖u(s)‖_∞ ds + √(ν τ₀)`.

This is not a theorem for an arbitrary "structure", but it is the physically forced regime
for a vorticity-supported feature (vorticity moves by advection and diffusion; stretching
amplifies but does not translate support). Under (T), with `‖u‖_∞ ~ s^{−γ}` and `γ < 1`:

`τ₀^ρ ≲ τ₀^{1−γ} + τ₀^{1/2}` for all small `τ₀` ⟹ **`ρ ≥ min(1 − γ, 1/2)`** [D1′].

- For `γ ∈ (1/2, 1)`: the cut is `ρ ≥ 1 − γ`, strictly weaker than the withdrawn `ρ ≥ 1/2`.
- Without hypothesis (T), **no lower bound on `ρ` is currently established** here.

## 4. Impact analysis

- **On-axis blob window (`ρ = α`): unaffected.** The blob core never translates (it sits at
  the origin while its scale collapses), so neither the withdrawn [D1] nor [D1′] applies to
  it. The published primary window
  `{1/2 < γ < 1, max(2γ/3, 2γ−1) ≤ α < γ}` stands as stated.
- **Ring corridor: re-cut.** Replace `ρ ≥ 1/2` by the conditional
  `ρ ≥ min(1−γ, 1/2)` [D1′/(T)]. The corridor widens accordingly at `γ` close to 1; all
  other ring constraints (dissipation `ρ > 2γ−1`, geometry `α ≥ ρ`, [D2], and the new
  CSTY-II cut in the kill table) are unchanged.
- **Registry correction:** the statement "sub-parabolic ring collapse is dead" in the
  2026-08-18 registry entry and survival-map document is downgraded to the conditional
  [D1′] form; correction notes are appended in place rather than silently edited.

## 5. Credit

The audit demand came from the external reviewer's (GPT) observation that [D1] carried a
larger logical step than the other cuts — center choice, time window, and the smallness of
local integral quantities were exactly where the gap lay.
