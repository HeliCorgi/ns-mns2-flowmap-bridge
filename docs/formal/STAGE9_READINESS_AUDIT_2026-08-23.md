# Stage-9 readiness audit — 2026-08-23

Bounded audit executed after the Stage-9 readiness pass (Tasks A and B). Scope: decide
whether the formal side carries enough machinery to **begin Stage 9** (attacking the
unresolved Navier–Stokes mathematics), and stop formal plumbing if it does.

This document is an audit of what is **machine-checked**, not a plan. Every anchor below is
a named theorem; filenames are not evidence. Provenance: the Gate-A prerequisites and the
whole Gate-C machinery are committed on `main` at the baseline commit below; the three
modules added by this pass (§0) were verified by the local Elan-pinned gate and land on
`main` in the same commit as this document. No hosted CI run exists for either (quota
exhausted), so no third party has independently reproduced the gate.

Baseline commit: `1b9cb0a`. Verification runner: local Elan-pinned Lean `v4.32.1`
(`lean-toolchain`); full `Formal.+` gate via `scripts/lean-ci-local.sh`: **exit 0, 8769
jobs**, zero errors, zero warnings from the three new modules, pinned
`sorry`/`admit`/`axiom`/`opaque` scan clean, and all **277** audited declarations depend
only on `propext`, `Classical.choice`, `Quot.sound`. GitHub-hosted Actions were not invoked
(quota exhausted; hosted runs banned).

---

## 0. What the readiness pass added

| Task | Anchor | File |
|---|---|---|
| A — realness transport | `r3L2Conj_r3H3ToL2Operator`, `isR3RealVelocity_r3H3ToL2Operator`, `r3EndpointSafeProjectedMild_isR3RealVelocity_decoded` | `Formal/R3DecodedVelocityRealness.lean` |
| B — admissible initial-data adapter | `IsR3AdmissibleSchwartzDatum`, `isR3AdmissibleSchwartzDatum_iff`, `r3H3ToL2Operator_r3SchwartzToHsCLM`, `IsR3AdmissibleSchwartzDatum.encode_mem_solenoidal`, `r3AdmissibleSchwartzDatum_navierStokes`, `exists_isR3AdmissibleSchwartzDatum_ne_zero` | `Formal/R3SchwartzInitialData.lean` |
| B — divergence-condition equivalence | `r3SchwartzDivergence_fourier_apply`, `r3Schwartz_rawDivergence_fourier_iff_classical` | `Formal/R3SchwartzDivergence.lean` |

Nothing else was built. No reality framework was rebuilt (Task A is three lines of
consequence over the existing generic `r3L2Conj_of_fourier_realEven`); no general
`H³ ⇒ C^∞` implication was attempted, claimed, or smuggled in — that implication is
**false** and the adapter runs in the opposite direction (Schwartz datum ⇒ carrier
coordinate).

---

## 1. Gate A — actual Navier–Stokes semantics

**Verdict: PASS at the readiness bar, with the semantic strength recorded exactly.**

Anchor: `r3EndpointSafeProjectedMild_navierStokes` (`Formal/R3NavierStokesEquation.lean`).
For `0 < ν`, an endpoint-safe projected mild solution `u` with solenoidal initial
coordinate, and `t ∈ Ioo 0 T`, the decoded physical velocity `U s = r3H3ToL2Operator (u s)`
satisfies

- **strong `L²` time derivative**

  ```text
  ∂ₜU = ν ΔU − P((U·∇)U)
  ```

  (`HasDerivAt`, edge 2b-ii.a);

- **unprojected momentum equation**, componentwise in `𝓢'(R³, ℂ)`, with the explicit
  Helmholtz pressure `p = r3HelmholtzPressure ((U·∇)U)` (edge 2a, consumed through
  `postcomp_r3LerayL2Operator_eq`)

  ```text
  ∂ₜU − ν ΔU + (U·∇)U + ∇p = 0
  ```

- **incompressibility**, distributionally (edge 1a)

  ```text
  ∇ · U = 0.
  ```

`Δ` and `(U·∇)U` are **identified by theorem**, not by naming:
`r3L2ToTempered_r3H3LaplacianL2Operator` (the decoded multiplier `Δ̂·J⁻³` *is* the
distributional `∑ᵢ ∂ᵢ∂ᵢ`) and edge 2b-i
(`r3H2ToL2Operator_r3ConvectionH3ToH2` / `r3MildConvectionSource_eq`, the completed
coordinate convection decodes to the literal pointwise `∑ᵢ Uᵢ ∂ᵢU`, whose `fderiv` is
genuine).

**Realness — the gap this pass closed.** Before this pass the capstone's `U` was a field
on the complex carrier with realness *neither used nor asserted*. Now:

```text
r3L2Conj (r3H3ToL2Operator g) = r3H3ToL2Operator (r3L2Conj g)      (decoder symbol J⁻³ real + even)
IsR3RealVelocity g → IsR3RealVelocity (r3H3ToL2Operator g)
IsR3RealVelocity u₀ → ∀ t ∈ Icc 0 T, IsR3RealVelocity (r3H3ToL2Operator (u t))
```

the last consuming the **unconditional** coordinate-level realness
`IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity` (no ball hypothesis). The
theorem is actually consumed: `r3AdmissibleSchwartzDatum_navierStokes` exports it.

**Semantic strength (recorded, not hedged):** spatial distributions (componentwise `𝓢'`),
strong `L²`-valued time derivative, interior times `Ioo 0 T` of a **local** certified
horizon, pressure determined up to additive harmonic terms with no regularity or decay
claimed. Per the readiness rule, distributional-in-space + strong-`L²`-time is sufficient
**unless** the selected Stage-9 theorem demands more; the selected theorem (named in §5:
the Scope-B `β_v` endpoint-pinning decision,
`docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md` §2) is a statement about Type-II
exponents and ancient/limit objects, decided by arithmetic over frozen ledger rows, and
consumes **no** Lean declaration at all — in particular no classical time derivative, no
endpoint derivative, and no pressure regularity. See the scope note in §5.

---

## 2. Gate B — admissible initial datum

**Verdict: PASS for one concrete admissible class.**

Class: `IsR3AdmissibleSchwartzDatum φ` for `φ : R3SchwartzVelocity = 𝓢(R³, ℂ³)` —

```text
r3SchwartzConjCLM φ = φ                                   (physically real)
∀ ξ, ξ · 𝓕φ(ξ) = 0                                        (divergence-free, frequency form)
```

Certificates for the **same** datum, all machine-checked:

| Property | Anchor |
|---|---|
| smooth (`C^∞`) | `IsR3AdmissibleSchwartzDatum.smooth` (Schwartz class) |
| rapidly decaying | `IsR3AdmissibleSchwartzDatum.decay` (all derivatives, all polynomial weights) |
| real | `r3SchwartzConjCLM_eq_self_iff` (⟺ every imaginary part vanishes pointwise) |
| divergence-free, classical pointwise | `IsR3AdmissibleSchwartzDatum.classicalDivergence` — **derived**, not assumed |
| finite energy | `r3Schwartz_finiteEnergy` (`∫‖φ‖² = ‖φ.toLp 2‖² < ∞`) |
| encodes into the carrier | `IsR3AdmissibleSchwartzDatum.encode_mem_solenoidal` (`r3SchwartzToHsCLM 3 φ ∈ r3L2SolenoidalSubmodule`) |
| encoded coordinate is real | `IsR3AdmissibleSchwartzDatum.isR3RealVelocity_encode` |
| decode ∘ encode = identity | `r3H3ToL2Operator_r3SchwartzToHsCLM` (`r3H3ToL2Operator (r3SchwartzToHsCLM 3 φ) = φ.toLp 2`) |

**Direction check (honesty item).** The required direction is
`decode(encode(U₀)) = U₀`, and that is exactly the statement proved: the bounded genuine
`J⁻³` multiplier decoder applied to the canonical order-three coordinate of `φ` returns the
literal physical `L²` field of `φ`. This is the order-three transposition of the already
proved order-two identity `r3H2ToL2Operator_r3SchwartzToHsCLM`; the `𝓢'`-level version
`r3HsToTempered_r3SchwartzToHsCLM` and the pointwise-everywhere version for the explicit
inverse-Fourier representative `r3DecodedRepresentative_schwartz` already existed. Nothing
in the chain uses the phantom Sobolev-order alias as an inclusion or smoothing theorem.

**Interface honesty.** The predicate takes the divergence-free condition in its
**frequency form**. Two independent results pin down what that means:

- `IsR3AdmissibleSchwartzDatum.classicalDivergence` derives the classical pointwise form
  through the edge-3a capstone and the exact Schwartz inversion
  `r3DecodedRepresentative_schwartz` (decoding route);
- `r3Schwartz_rawDivergence_fourier_iff_classical` (`Formal/R3SchwartzDivergence.lean`)
  proves the two forms **equivalent in both directions** on the Schwartz core, through the
  exact transfer identity
  `𝓕(∑ᵢ ∂ᵢφᵢ)(ξ) = 2πi · (ξ · 𝓕φ(ξ))` and injectivity of the Schwartz Fourier transform
  (Fourier-multiplier route).

Hence `isR3AdmissibleSchwartzDatum_iff`: the admissible class **is exactly** the class of
real, classically divergence-free Schwartz velocity fields. Nothing convenient was smuggled
into the definition, and the two routes agree.

**Non-vacuity.** `exists_isR3AdmissibleSchwartzDatum_ne_zero` exhibits an explicit
**nonzero** admissible datum: `φ = 𝓕⁻F` with
`F(ξ) = i·b(ξ)·(ξ₁e₀ − ξ₀e₁)` and `b` the existing compactly supported plateau bump.
`ξ · F(ξ) = i b(ξ)(ξ₀ξ₁ − ξ₁ξ₀) = 0` identically; `F` is fixed by reflected conjugation
(`b` real and even, vector factor odd with real entries), which is the frequency-side form
of physical realness; and `F ≠ 0` because at `ξ* = (0, 1/2, 0)` — inside the plateau, where
`b = 1` — the first component is `i/2`. So the entry capstone is **neither an empty
implication nor a statement about the zero datum only**.

---

## 3. Gate C — continuation machinery

**Verdict: PASS by instantiation; no new packaging required.**

Every theorem of the local/continuation layer quantifies over an **arbitrary** coordinate
`u₀ : R3HsVelocity 3`, so the admissible datum's coordinate `r3SchwartzToHsCLM 3 φ` enters
each of them verbatim:

| Machinery | Anchor |
|---|---|
| local existence (+ ball uniqueness) | `r3EndpointSafeProjected_exists_localMildSolution` |
| explicit lifespan | `r3EndpointSafeProjected_exists_mildSolutionOn_mildLifespan`, `r3MildLifespan nu r = (δ(r)/(1+(π√ν)⁻¹+δ(r)))²` |
| real local solution | `r3EndpointSafeProjected_exists_realLocalMildSolution`, `IsR3EndpointSafeProjectedMildSolutionOn.isR3RealVelocity` |
| unrestricted uniqueness | `r3EndpointSafeProjectedMildSolution_unique` |
| restart | `IsR3EndpointSafeProjectedMildSolutionOn.restart` |
| concatenation | `IsR3EndpointSafeProjectedMildSolutionOn.concat` |
| extension of bounded solutions | `r3EndpointSafeProjected_exists_extension_of_bounded` |
| blow-up dichotomy | `r3EndpointSafeProjected_blowup_dichotomy` |

The dichotomy instantiated at the admissible datum is shipped as
`r3AdmissibleSchwartzDatum_blowup_dichotomy` so that Gate C is **consumed**, not merely
claimed. The canonical glued maximal trajectory `u*` with pointwise
`limsup ‖u*‖ = ∞` is **not** constructed and is **not** required: no selected Stage-9
theorem consumes it.

---

## 4. Remaining formal gaps — all recorded NON-BLOCKING for Stage 9

| Gap | Status |
|---|---|
| uniform-in-time energy bound / energy inequality (edge 4-uniform) | `DEFERRED / NON-BLOCKING FOR STAGE 9` — pointwise-in-time finite energy is proved; the selected Stage-9 theorem does not consume a uniform bound |
| classical `C^∞` / pointwise-classical solution semantics | open, not required at the readiness bar |
| endpoint derivatives at `t = 0`, `t = T` | open, not required |
| global time | open — **this is the mathematics, not plumbing** |
| pressure regularity | open, not required |
| canonical maximal trajectory `u*` | open (Bucket B), not required |
| general `H³` initial-data characterization (edge 3 proper) | open **and out of scope by design** — `H³ ⇒ C^∞` is false; the adapter direction is the correct one |
| Clay breakdown transfer, official quantifier packaging (edge 5) | deferred until a Stage-9 theorem shape exists |
| classical ⇔ frequency divergence equivalence for Schwartz fields | **CLOSED** in this pass (`Formal/R3SchwartzDivergence.lean`, both directions) — no longer a gap |

None of these may be worked on for completeness. Per the stop rule, they are revisited
only when a concrete Stage-9 theorem needs them.

---

## 5. Verdict

**Stage-9 readiness: `PASS`.**

A real, divergence-free, finite-energy, smooth, rapidly decaying physical datum enters the
certified local Navier–Stokes/continuation theory, and the certified physical velocity
satisfies the actual incompressible Navier–Stokes equations at every **interior** time of a
positive **local** horizon — componentwise in `𝓢'`, with a strong `L²`-valued time
derivative and the explicit Helmholtz pressure (determined up to additive harmonic terms),
incompressibility distributionally — and is real at every certified time. It is **not** a
classical solution and there is no statement at `t = 0`, at `t = T`, or beyond `T`.

**Scope of this PASS.** It means exactly: *no formal gap blocks the commissioned Stage-9
task*. That task (`docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md` §2) is a
vocabulary-level exponent decision over frozen ledger rows, stated for axisymmetric
finite-energy **suitable weak** solutions with first singular time `T* < ∞` — a solution
class with **no formal counterpart in this repository** — so it consumes **no output of the
formal layer at all**. This PASS is therefore *not* a certificate that the formal stack is
adequate for an arbitrary future Stage-9 theorem, and it is *not* a Clay-grade adequacy
claim. If a later research theorem does consume the formal layer, its requirements must be
re-checked against §1–§3 before any deferred item is treated as still deferred.

**FORMAL PLUMBING STOPS HERE.** The next work item is Stage-9 mathematics — the **Scope-B
`β_v` endpoint-pinning decision theorem**, selected and failcase-audited in
`docs/gates/STAGE9_DECISION_SELECTION_2026-08-23.md` (§2 statement, §3 failcase battery)
and summarized in `HANDOFF.md`.

**What did NOT change:**

- Clay problem solved? **NO.**
- Blow-up proved? **NO.**
- Global regularity proved? **NO.**
- Any research-side status changed? **NO** — the 2026-08-21 freeze (round 2) stands
  unchanged; this pass commissioned the next research question, it did not answer one.
