# BH quantitative no-swirl rigidity + K12 — adversarial audit

Date: 2026-08-19 (JST). Task: external reviewer's vertical-integration + BH-reopen brief
(one bounded adversarial pass; stop rules observed: no numerics, no new ansatz, no Lean
changes, no modification of the frozen map, no Clay claims). Baseline:
[`BH_PROFILE_TASTE_REPORT.md`](BH_PROFILE_TASTE_REPORT.md) (YELLOW), frozen window per
[`TYPE2_KILL_TABLE_2026-08-19.md`](TYPE2_KILL_TABLE_2026-08-19.md).

**Process.** Four independent analyses (rigidity formulation/compactness, GS singular-limit
escapes, K12, literature) + two adversarial verifications (rigidity, K12) + one
completeness critic, run as parallel agents; this document is the synthesis, with every
mandatory correction from the verifications applied. Honesty note: the GS-escape analysis
and the literature analysis received **no** adversarial verification; the GS-escape
analysis's supporting derivation sections were partially lost to output truncation, so its
headline claims (the viscous-realizability blocks V1–V3) are carried at `[C]`-at-best.
Epistemic tags: [H] hard, [V] verified from a primary source read today, [V?] search-level,
[C] conditional, [B] bookkeeping.

## 1. Verdict up front — YELLOW (unchanged grade, substantially replaced content)

The branch is still YELLOW: no admissible degenerating family is constructed, and no
contradiction under the frozen constraints is proved. But the *content* of YELLOW changes:

- the baseline §1 dichotomy sentence ("if the forced rate is a power of 1/ε → RED-ward;
  if logarithmic → GREEN-ward") is **RETIRED as ill-posed**: the two candidate rate
  objects produced this pass (a forced blow-up rate and a permitted gluing-defect decay)
  point in *opposite* directions, the constitutive steepness `Q₁ = sup|P̂′(s)|/s` is
  `+∞` identically on the class (so "its rate" is vacuous), and the defect functional has
  no fixed norm. Neither direction of the old dichotomy is well-posed.
- the **smallest missing theorem has changed** — see §6, the swirl-fraction gap (★).
- scope: everything below concerns **`S_blob`, interior quasi-static branch** (`γ+α>1`).
  `S_ring` and the ≥3-region corridor are untouched by this pass; moreover the planar
  analogue of no-swirl rigidity is **false** [H] (any compactly supported radial vortex
  `ω = f(|x|)` is a nontrivial compactly supported steady 2-D Euler flow), so the ring
  corridor has *no rigidity kill at all* in its leading-order description.

Why not YELLOW-RED: too much of the anticipated kill machinery broke under verification
(the Harnack rate route is vacuous, the thin-ring exclusion is conditional and partly
circular, K12's conclusion does not follow as stated). Why not YELLOW-GREEN: the only
GREEN-ward argument produced (a "log² is survivable" reading) was refuted as a non
sequitur, and GREEN-ward grades must not be earned by absence of contradiction.

## 2. Normalization (baseline §3, with three additions)

Recorded convention (unchanged): `u = (1/r)ψ_z e_r − (1/r)ψ_r e_z + (1/r)F(ψ)e_θ`,
`−Δ*ψ = ∂_ψ(F²/2 + r²P(ψ))`, `Δ* = ∂_rr − (1/r)∂_r + ∂_zz`; core rescaling
`x = ℓŷ`, `ψ = U_pol ℓ² ψ̂`, `F = ε U_pol ℓ F̂(ψ̂)`, `P = U_pol² P̂(ψ̂)` gives
**`−Δ̂*ψ̂ = ε²(F̂F̂′)(ψ̂) + r̂²P̂′(ψ̂)`** with `F̂ = Γ = O(1)` and `F̂(0) = 0` forced
(`Γ = 0` on the axis and on the free boundary) [B, re-verified this pass].

Additions this pass:

1. **Energy swirl fraction** [B]: `s := ∫|u_θ|²/∫|u_pol|²` equals `ε² = τ^{2(γ−α)}` on
   the blob branch (`σ = α`), and `τ^{2(γ−ρ)}` on the ring branch (`σ = ρ`). This
   scale-invariant ratio is the object of the corrected missing theorem (§6).
2. **The circulation diffuses by `Δ*` itself** [H]: `∂_tΓ + u_pol·∇Γ = νΔ*Γ` with
   `Δ*Γ = ΔΓ − (2/r)∂_rΓ = r∇·(r^{−1}∇Γ)` — the same operator as the left side of the
   BH equation, in divergence form with weight `r^{−1}`. `Γ` is *near-passive* (feedback
   on the poloidal field only through the `O(ε²)` term), so the correct homogenization
   anchor is scalar closed-streamline homogenization (Batchelor/Rhines–Young type), which
   is a materially easier setting than Prandtl–Batchelor for vorticity — but note §7's
   ζ-averaging lead, where the genuine nonlinear PB structure reappears.
3. **`F̂′ → 0` yields `Γ → const`, not "no swirl"** [H]. A constant-`Γ` flow is not
   swirl-free; only its *poloidal equation* coincides with the no-swirl one
   (`FF′ = ∂_ψ(F²/2) = 0`). Any argument that ends "…hence the no-swirl rigidity theorem
   applies" needs either `Γ → 0` (see K12″, §7.6) or a rigidity statement at the
   Bragg–Hawthorne level. The baseline's K12 chain silently skips this step.

## 3. The compactness-to-rigidity argument, audited

Setting: normalized profiles `û_ε`, swirl fraction ≤ ε, uniform support in a fixed ball
(LOC), uniform `C^{1,β}` (REG), poloidal sup-norm normalized to 1 (NORM).

**What genuinely works** [H]:

- Arzelà–Ascoli extraction in `C¹`; the steady Euler equation passes to the limit in weak
  form under *uniform convergence alone* — the pressure is **enslaved** (`∇p = 0` off the
  support ⇒ `p` constant on each complement component, `0` on the unbounded one; `C¹`
  convergence of `û` forces `C⁰` convergence of `p̂`), so pressure compactness is not a
  separate burden;
- compact support passes (decay hypotheses do **not** substitute);
- the sup-norm normalization **survives the limit** (uniform convergence on the set
  containing the maximizers). The baseline's worry about normalization loss is unfounded
  for sup-norm-type normalizations — but would be correct for scaling-critical ones
  (`L³`, `‖∇u‖_{L²}`), which can vanish in the limit by concentration. The physics hands
  us an `L^∞`-type exponent (γ), so the right normalization is available.

**Where all the risk sits** (this pass's grading correction of baseline Gate C: hypothesis
(iv) is not a "footnote-level residue" — it is the theorem):

- **rigidity-class membership of the limit**: steps 1–4 deliver a `C^{1,β}` compactly
  supported axisymmetric no-swirl steady limit — but whether that contradicts anything
  depends on the hypothesis class of the rigidity theorem actually available (§5, §D.1
  finding below);
- **single-valuedness of the constitutive functions** (new, previously unlisted): reducing
  to GS needs the level-set foliation of `ψ̂_ε` to be uniformly nondegenerate; nested or
  counter-rotating cells make `P̂_ε` multivalued and dissolve the global GS reduction;
- **axis degeneracy for the on-axis blob** (new, promoted from footnote to blocking): the
  frozen branch's support *contains* the axis (`inf_supp r̂ = 0`, `sup_supp r̂ = O(1)`);
  the drift `−(1/r̂)∂_r̂` of `Δ̂*` is then only borderline-integrable exactly where the
  free boundary meets the axis, and every elliptic estimate used anywhere in this file
  (Harnack, `C²` limit passage, Schauder) needs a stated workaround there.

## 4. The canonical escape list (merged; supersedes both analysts' lists)

If no subsequence yields the contradiction, at least one of the following fails. Status
marks which escapes are actually available after this pass's cross-checks.

| # | escape | status after audit |
|---|---|---|
| E1 | uniform `C^{1,β}` fails for every β (no uniform modulus for `∇û`) | LIVE; and a **literature precedent exists at fixed swirl fraction** [V]: Constantin–La–Vicol Thm 3 constructs localized families in `L² ∩ C^{1/3}` and *not* `C^β` for any `β > 1/3`, with `‖∇u‖‖u‖²` arbitrarily large |
| E2 | sup-attaining point escapes every fixed core ball | LIVE (exits toward multi-scale designs; interacts with K5/K6 bookkeeping — unchecked, see §8 M4) |
| E3 | support thins to lower-dimensional set (torus minor radius → 0) | thin-ring direction: **only conditionally excluded** — the momentum-flux argument (§5) gives an `O(1)` obstruction but needs (LOC)+(REG)+an energy-concentration hypothesis and is partly circular; do **not** cite as an exclusion. [C] |
| E4 | core drifts to `R ≫ ℓ` (ring corridor) | exits `S_blob`; **in the ring corridor the rigidity kill vanishes entirely** (planar rigidity false [H]) — the corridor is open and cheaper, not blocked |
| E5 | constitutive steepening of `F̂` (route (F): `F̂′ ~ ε^{−2}`) | **closed to a separatrix sliver** across the wedge by two independent [C] mechanisms (viscous realizability; homogenization §7) — the one surviving realisation is the period-divergence (`T̂`) channel near separatrices |
| E6 | constitutive steepening / non-Lipschitz `P̂′` (route (P)) | LIVE — and the **generic** mechanism: the slab free-boundary model [H] shows *any* compactly supported profile needs the Osgood/Vázquez condition `∫₀ ds/√(2|Ĝ(s)|) < ∞` to fail Lipschitz-at-0, with or without swirl; a `C^∞` dead-core template exists with bounded `‖∇²û‖` and non-Lipschitz `P̂′`. Literature precedent at fixed swirl [V]: CLV Thm 2 is generically only Hölder, `F(ψ) ~ √ψ`, `F′ ~ ψ^{−1/2}` at a point |
| E7 | foliation degeneracy / multivalued constitutive functions | LIVE (new; unlisted in baseline) |
| E8 | limit leaves the classical class (weak/sheet/defect limit) | LIVE |
| E9 | trivial poloidal limit | **NOT AVAILABLE** [H] under a sup-norm normalization (§3); would become live only under a scaling-critical normalization |
| E10 | swirl-term self-degeneration (`‖F̂F̂′‖ → 0` faster than ε²) | consistent with the frozen window only via §2.3's `Γ → const` caveat; strengthens rather than escapes the contradiction |

**Consequence** (from the GS-escape analysis, carried at [C] because its derivation
sections were truncated and unverified): the viscous-realizability requirements V1–V3
(features thinner than `√(ν·(local time))` cannot be sustained by the fixed-ν NS core)
block every escape in the **swirl** sector; the surviving degeneration lives in the
**poloidal/regularity** sector (E6, E7, E8). *The required singular family is not
swirl-driven; the poloidal field must degenerate.* Two important two-sided facts:

- the swirl term has the **wrong sign for localization** in the slab model [H]
  (`Ĝ = ε²F̂²/2 + r̂²P̂` — the swirl contribution is ≥ 0 and impedes compact support),
  yet swirl is **structurally essential** to every known localized construction [V]
  (Gavrilov; CLV, who cite Jiu–Xin for the necessity). Reconciliation: the free-boundary
  tangency does not need swirl; the *global* localizability structure does. The
  swirl/no-swirl separation is **global, not local** — candidate mechanism [V?]: the
  no-swirl problem must fit a *single* `P̂′` across level sets sitting at different `r̂`
  (the `r̂²` weight is a cross-foliation compatibility constraint); swirl supplies a
  second constitutive function `F̂`, restoring one degree of freedom per level set;
- CLV's localizability identity `|∇ψ|² + F² = 2r²A(ψ)` [V] in the limit `F → 0` becomes
  an eikonal-type overdetermination on `ψ` — CLV themselves note the constraint "severely
  curtails" the choice of `F, P`. Whether it is necessary or only sufficient for
  localizability is [V?]; even if only sufficient, it says the known constructions do not
  push to `ε → 0`. Second-most-promising unexplored lead (§8).

## 5. Is any quantitative rate proved / known / derivable? Four answers

1. **Proved here: no rate.** One exact new identity was proved and survived adversarial
   verification (two independent derivations) [H]:

   > for every compactly supported steady axisymmetric Euler flow (velocity `C¹` is
   > ample), `∫u_r² + ∫u_θ² = 2∫u_z²` exactly; equivalently
   > `∫u_iu_j = (1/3)(∫|u|²)δ_ij` (Cartesian equipartition), all first moments of the
   > momentum-flux tensor vanish, and the isotropic virial is vacuous (`0 = 0` — the
   > correct negative control, since Gavrilov's flows exist).

   With `‖u_θ‖_∞ ≤ ε‖u_pol‖_∞` this yields the `ε²`-defect budget
   `|∫u_r² − 2∫u_z²| ≤ Cε²E_pol` (plus an energy-concentration hypothesis). This is an
   ingredient of exactly the right order, but an `O(1)` constraint, not a rate.
2. **Known in the literature: no — and this is an actively-searched negative result, not
   a search failure** [V]. Five independent query families for quantitative
   Liouville/stability-of-rigidity/small-swirl (2019–2026) returned nothing; the nearest
   misses (Coiculescu–Yang conditional Liouville for stationary NS; Chae–Weng sufficient
   conditions) are qualitative and NS-specific. Jiu–Xin's statement itself is confirmed
   [V] *as quoted verbatim in Constantin–La–Vicol (read in full)*: smooth compactly
   supported no-swirl axisymmetric steady Euler ⇒ `u ≡ 0` (full velocity). The primary
   CMP 287 text remains inaccessible (paywall); the secondary paraphrase suggests the
   hypothesis class may be "finite energy + constant far-field" (more general than
   compact support — if so, good news for the kill side) [V?]. The exact hypothesis class
   is still the single most consequential unchecked literature item.
3. **Derivable by Harnack / unique continuation: no — the route is vacuous.** The
   anticipated argument (weak Harnack on `−Δ̂*ψ̂ − Vψ̂ ≥ −ε²K` with `Λ = ‖V‖_∞`,
   `V = r̂²P̂′(ψ̂)/ψ̂`, yielding `Λ ≳ log²(1/ε)`) **fails structurally**: the slab model's
   own necessary condition forces `|P̂(s)|/s² → ∞`, i.e. `Λ = Q₁ = +∞ for every member of
   the class at every ε` — the Harnack hypothesis (`V ∈ L^q`, `q` above the
   Moser/Krylov–Safonov threshold) is violated by the very family the argument targets,
   exactly at the free boundary where the argument needs its ball. The salvageable finite
   constitutive quantities are the **Osgood integral** `∫₀ ds/√(2|Ĝ_ε(s)|)` and the
   **climb distance** (thickness over which `ψ̂` rises from 0 to a fixed fraction of its
   max); no rate has been derived for either. The UCP variant is normalization-dependent
   and no better. **No rate can exist at all in velocity-side norms** ([H] for the slab
   template — a `C^∞` compactly supported dead-core profile with bounded `‖∇²û‖_∞`
   exists; [C] at family level): the degeneration must be measured in constitutive or
   support-geometry quantities, never in `C^k` norms of the velocity.
4. **Derivable by the momentum-flux route: possibly — this is the live route.** A
   quantitative lower bound on the *poloidal anisotropy defect*
   `|∫u_r² − 2∫u_z²| ≥ Ψ^{-1}·E_pol` over localized poloidal profiles would convert the
   `ε²` budget into a rate, polynomial whenever `Ψ` is. Neither proof nor counterexample
   is known. This is subsumed into (★) below.

## 6. The corrected smallest missing theorem — the swirl-fraction gap (★)

The baseline's "how fast must `C^k` norms, support anisotropy, or constitutive steepness
blow up as ε → 0" is now known to be **ill-posed in the `C^k` sector** (5.3) and
**vacuous in the constitutive-steepness sector** (`Q₁ ≡ +∞`). Replace it with a bounded,
scale- and amplitude-invariant functional gap in the energy topology:

> **(★) Swirl-fraction gap (quantitative Jiu–Xin).** For nontrivial compactly supported
> axisymmetric steady Euler flows `u` on `R³` (classical `C¹`, or distributional with
> `u ∈ L²`), set `s(u) := ∫|u_θ|² dx / ∫|u_pol|² dx`. Rigidity says `s(u) = 0` is
> impossible. **Is `inf s(u) > 0` over the class?**

Why this is the right object:

1. it is exactly what the frozen window forces: `s = ε²` (blob), `s = τ^{2(γ−ρ)}` (ring)
   — **one statement covers both branches**, unlike every argument above;
2. it applies member-by-member — no subsequence, no `C^{1,β}`, no constitutive
   hypothesis, no foliation condition, no rigidity-class membership; it collapses the
   Gate-C hypothesis list to *localization alone* (caveat [B]: for decaying rather than
   compactly supported profiles the threshold decay `|u|² + |p| = o(|x|^{−3})` is
   marginal and must be stated);
3. it is immune to E1, E5–E10 by scale invariance; only "not localized" and "not steady
   Euler at leading order" (the `γ+α = 1` edge — K10's territory) evade it;
4. by the [H] identity, `s(u) = (2∫u_z² − ∫u_r²)/∫|u_pol|²` — (★) is equivalently the
   **poloidal-anisotropy gap**: can a localized poloidal circulation approach exact
   Cartesian equipartition `∫u_r² = 2∫u_z²` arbitrarily closely?
5. it is falsifiable in both directions, and it has a **cheap first probe**: compute
   `s(u)` for Gavrilov's explicit solution and CLV's Thm 2/3 families — the first upper
   bound on `inf s`, a bounded literature-plus-algebra task.

Decision consequence, replacing the retired dichotomy: **`inf s > 0` ⇒ RED for blob and
ring alike; an explicit family with `s → 0` ⇒ YELLOW-GREEN with the construction
constraints of §4.** Second-place missing theorem (do not conflate): a rigorous
closed-streamline homogenization theorem for a 3-D axisymmetric slowly-modulated
collapsing core — confirmed absent from the literature [V] (all rigorous
Prandtl–Batchelor results are 2-D steady or 2-D quasi-periodic, vanishing-viscosity
constructions) — needed only on `{α ≥ 1/2}`, hence not load-bearing.

## 7. K12 adversarial audit

**Final status: KEEP CONDITIONAL.** Not PROMOTE (the stated conclusion does not follow);
not WITHDRAW (the premise is sound and, for `α > 1/2`, stronger than the baseline
claims). The frozen map is unchanged.

1. **The averaged object, derived** [H]: integrating the `Γ`-equation over the region
   inside a closed streamline (weight `r dr dz`) cancels advection exactly and yields, in
   the enclosed-volume label `J` and the accumulated diffusive time
   `N(τ) = ∫_τ ν τ′^{−2α} dτ′`, the reduced equation `∂_N F = ∂_J(Â²χ ∂_J F)` with
   `Â` = streamsurface area and `χ = ⟨|∇ψ|⟩⟨|∇ψ|^{−1}⟩ ≥ 1`. Corrections applied per
   verification: `χ` multiplies the conductance and therefore **accelerates**
   homogenization (every reverse claim deleted); the gap is controlled by
   `λ₁ ≳ (inf Â²)/J_max²`, i.e. by small streamsurface *area*, and an isoperimetric
   argument [C] shows a small-area surface cannot separate two large volumes.
2. **The trichotomy is in accumulated time, not the instantaneous ratio** [B]:
   `α < 1/2` ⇒ `N` bounded (no homogenization forced); `α = 1/2` ⇒ `N = ν log(1/τ)`
   diverges logarithmically, damping `Γ_J` by `τ^{λ₁ν}` — the mechanism **acts**, with a
   margin that is a power of τ with a **non-universal, ν- and geometry-dependent
   exponent**; `α > 1/2` ⇒ `N` diverges as a power, damping super-polynomially. Note
   `α < 1/2 ⟺ ℓ ≫ √(ντ)` is elementary and independent of any PB theorem.
3. **Robustness** [C]: every Gate-C degeneration tested (support thinning, cellular
   refinement, boundary tangency — where vanishing orbit speed and diverging period
   compensate exactly in the volume label) leaves the reduced diffusion as fast or
   faster. The intuition "singular geometry protects the swirl structure" is backwards.
4. **But the conclusion does not follow — two breaks** [C]:
   (i) `F̂′ = Γ_J · T̂`: homogenization controls `Γ_J`, not `F̂′`; the orbit period `T̂`
   diverges near separatrices, and the surviving realisation of route (F) is an
   `O(1)` circulation jump across a `T̂`-thin separatrix sliver — for `α > 1/2` this
   needs a doubly-exponentially thin sliver (not viable [B]+[C]); at `α = 1/2` only a
   power-law period divergence (admissible; this is the **one** honest reason the
   `α = 1/2` line stays grey, together with the ν-non-uniformity of the margin —
   whether the sliver can feed back at leading order into `−Δ̂*ψ̂` is unchecked and
   plausibly self-defeating);
   (ii) even granting `F̂F̂′ → 0`, the profile returns to the **singular no-swirl branch
   that Gate D already declares "not excluded"** — the rigidity theorem's hypothesis
   class is exactly what the surviving family has abandoned, so no contradiction is
   re-triggered. K12 is not an independent cut; it converts the `α ≥ 1/2` interior
   branch into an unconditional dependence on (★).
5. **Scope** [B]/[H]: blob branch only. In the ring corridor the leading problem is
   planar, where rigidity is false — K12's chain has no last step there. Exact geography:
   `S_blob ∩ {α ≥ 1/2} = {1/2 < γ ≤ 3/4, 1/2 ≤ α < γ} ∪ {3/4 < γ < 1, 2γ−1 ≤ α < γ}`
   (nonempty for every γ); the level set `α = 1/2` meets the wedge for `γ ∈ (1/2, 3/4]`,
   interior except at the corner `(3/4, 1/2)`. K12 and K10 attack disjoint regions. If
   K12′ were ever promoted *with* (★) supplied, the jointly uncontested residue would be
   the open set `{1/2 < γ < 3/4, max(1−γ, 2γ/3) < α < 1/2}` (a contested *edge* does not
   remove the fibre above it — corrected from the analyst's triangle).
6. **Two new report-level candidate routes surfaced by the verification (not proposed for
   the map):**
   - **K12″ (axis-Dirichlet route)** [C]: on an on-axis blob the axis (`Γ ≡ 0` by
     regularity) and the free boundary lie on the *same* `ψ = 0` level set (Hill-type
     topology); the reduced problem's outer boundary condition is then Dirichlet with
     value 0, homogenization drives `Γ → 0` — hence `σ > α`, a **direct violation of the
     K9 razor with no rigidity theorem invoked at all**. Conditional on the PB premise,
     on the topology, and on `α ≥ 1/2`; the shortest kill route now on the table.
   - **ζ-averaging** [B]+[C]: the identical streamline average applies to
     `ζ = ω_θ/r` (`∂_tζ + u·∇ζ = ν(Δ + (2/r)∂_r)ζ`, same weight, same operator, same
     gap), forcing `P̂′ → const` on `{α ≥ 1/2}` — which would close the non-Lipschitz-
     `P̂′` escape (E6) there and *narrow route (P)*. Honest caveats: the `ζ` problem has
     `O(1)` feedback (genuine nonlinear PB, no rigorous 3-D theorem exists [V]), and the
     compact-support flux identity does **not** close on the blob because of the
     axis-segment flux `∫u_z dz ≠ 0`. Top open lead of this pass; "route (P) is
     untouched" is therefore *not established* — route (P) is narrowed, not killed.
7. **K12′ — the annotation recommended for the next freeze cycle** (report-level text,
   NOT a ledger edit): *on `S_blob ∩ {α > 1/2}`, secular closed-streamline diffusion
   homogenizes the volume-labelled circulation at super-polynomial rate; route (F) is
   closed there up to the separatrix-sliver caveat, and the branch survives only through
   a singular no-swirl BH profile (route (P), narrowed by the ζ-lead). K12′ converts the
   `α > 1/2` interior branch into a dependence on (★). It excludes nothing on its own.
   Status [B]+[C].* Hypotheses that must be frozen with any future promotion: blob-only;
   interior wedge; nested-foliation/Reeb structure with Kirchhoff matching at separatrix
   vertices; no positive-measure stagnation set; isoperimetric streamsurface bound;
   adiabatic invariance off a separatrix layer + Taylor-dispersion completion
   (`α > (3−2γ)/4`); `Γ` maximum principle; outer boundary condition stated explicitly
   (no-flux vs axis-Dirichlet — decides between K12′ and K12″); `λ₁` bounded below
   uniformly along the modulation; and explicitly: route (P) not excluded without (★).

## 8. New debts and leads (recorded, not absorbed)

1. **K9 two-scale debt** (verification debt against the frozen kill table): the `σ = α`
   razor's derivation assumes a one-scale core; a near-axis sub-core at `r ~ τ^γ`
   respects the `Γ` maximum principle, violates every CFZ bound, and has `σ = γ`. K9 as
   written does not exclude two-scale cores; the viscous block offered against them is
   [C] while K9 is carried as [V✓]+[C]. Log this against
   `TYPE2_KILL_TABLE_2026-08-19.md` at the next freeze review.
2. **First probe of (★)**: compute `s(u)` for Gavrilov's and CLV's explicit families
   (literature + algebra; no numerics needed).
3. **CLV localizability constraint in the `F → 0` limit** (§4) — second unexplored lead.
4. **Escape-vs-map compatibility**: whether E2/E3-type escapes are consistent with the
   K5/K6 energy and `L³` bookkeeping was never checked.
5. **ζ-averaging** (§7.6) — top open lead.

## 9. Failures recorded (unrepaired, per stop rule)

T1/T2/T3 (Harnack-route rate statements) withdrawn as vacuous; T4 (thin-ring exclusion)
demoted to [C], partly circular; the `log²` K12 "sharpening" withdrawn (vacuous input +
boundary-layer/interior category error); the GREEN-ward reading withdrawn (non sequitur);
the defect functional `D` has no fixed norm; `λ₁` never computed for any concrete
profile; the 1-D reduction is invalid near separatrices — exactly where the surviving
route-(F) realisation lives; the anisotropy-defect lower bound (→ (★)) has neither proof
nor counterexample; Jiu–Xin's primary hypothesis class unverified first-hand; the
GS-escape analysis's V1–V3 blocks rest on physical heuristics with no theorem behind
them, and its derivation sections were lost to truncation without adversarial review.

## 10. Decision per the task's §14

BH verdict is **YELLOW** ⇒ isolate exactly one smallest missing theorem and stop broad
exploration. The theorem is **(★)** (§6), with the cheap first probe (§8.2) as the
designated next bounded step. The frozen survival map is unchanged; K12 remains
conditional (report-level K12′/K12″ annotations only); no numerics, no new ansatz, no
Lean changes were made in this pass.
