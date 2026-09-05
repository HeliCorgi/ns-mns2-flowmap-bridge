# B2 ancient-Euler compactness / steady-Euler compatibility decision — 2026-09-06

**Classification:** `CONDITIONAL THEOREM / NO-GO RESEARCH GATE` on the breakdown side. This record does **not** prove blow-up, global regularity, or any Clay A/B/C/D alternative.

## 0. Why this gate exists

The post-K11 dominant-balance record splits the surviving one-core Type-II bookkeeping into

- the edge `gamma + alpha = 1`, where the normalized leading equation is a generalized self-similar Euler equation; and
- the interior `gamma + alpha > 1`, where convection and pressure dominate both the physical time derivative and viscosity, so the leading core is expected to be quasi-static Euler.

Sessions 38–41 then showed that the Gamma-saturation microgeometry route should be parked: curvature, transition enstrophy, residence, and Bessel-hitting all produced real necessary conditions but no exclusion once the bad set could relocate or use scale-critical transport.

This gate therefore asks a location-independent question:

> Does an interior B2 sequence actually converge, after the natural convective rescaling, to a nonzero ancient/eternal Euler solution to which a Liouville or steady-profile obstruction can be applied?

The answer has three layers. The rescaled **time window and inviscid limit are real**, but the currently controlled quantities yield only an **Euler--Reynolds limit**, not an Euler limit. Moreover, even granting strong convergence to a steady Euler profile does not by itself give a contradiction because smooth compactly supported axisymmetric steady Euler flows with swirl exist.

## 1. Natural convective rescaling

Let a hypothetical smooth unforced NS solution have finite maximal time `T_*`, and take interior B2 times

` t_n -> T_* `, ` tau_n = T_* - t_n -> 0 `.

Write the core amplitude and scale as

` U_n ~ tau_n^(-gamma) `, ` ell_n ~ tau_n^alpha `,

with

` gamma > alpha ` and ` gamma + alpha > 1 `.

For an axis-preserving center `x_n=(0,0,z_n)` define the convective time

` theta_n = ell_n / U_n ~ tau_n^(alpha+gamma) `

and the normalized fields

` v_n(y,s) = U_n^(-1) u(x_n + ell_n y, t_n + theta_n s) `,

` q_n(y,s) = U_n^(-2) p(x_n + ell_n y, t_n + theta_n s) `.

Then the exact NS equation becomes

` partial_s v_n + (v_n . grad) v_n + grad q_n = eps_n Delta v_n `,

` div v_n = 0 `,

with

` eps_n = nu / (U_n ell_n) ~ nu tau_n^(gamma-alpha) -> 0 `.

Thus:

**`B2-ANCIENT-VANISHING-VISCOSITY = YES`.**

The normalized viscosity genuinely vanishes in the interior B2 regime.

## 2. The normalized time interval becomes eternal

The physical interval `[0,T_*)` becomes

` s in (-t_n/theta_n, tau_n/theta_n) `.

Since

` tau_n/theta_n ~ tau_n^(1-alpha-gamma) -> infinity `

when `alpha+gamma>1`, and `t_n/theta_n -> infinity` as well, every fixed compact interval in rescaled time eventually lies inside the normalized solution interval.

Therefore:

**`B2-ANCIENT-ETERNAL-WINDOW = YES`.**

The K11 interior is stronger than merely ancient: the natural convective frames have both backward and forward rescaled time horizons tending to infinity.

This is a genuine dynamical consequence of the interior exponent inequality and is independent of Gamma-max location.

## 3. What compactness follows from the Type-II amplitude envelope

Suppose the amplitude law used by the B2 bookkeeping is available as a local-in-time upper envelope, so on every fixed normalized cylinder `K = B_R x [-S,S]` one has

` sup_K |v_n| <= C(R,S) `.

This is the natural consequence of a two-sided/pinned Type-II amplitude law because

` theta_n/tau_n = tau_n^(alpha+gamma-1) -> 0 `,

so a fixed rescaled time window changes the remaining physical time by only `o(tau_n)`.

By Banach--Alaoglu and a diagonal extraction, after a subsequence

` v_n weak-* -> v ` in `L^infinity_loc`,

` v_n tensor v_n weak-* -> M ` in `L^infinity_loc`.

For every compactly supported divergence-free test field `phi`, the viscous term vanishes distributionally because

` |<eps_n Delta v_n, phi>| = |<eps_n v_n, Delta phi>| <= eps_n ||v_n||_infinity ||Delta phi||_1 -> 0 `.

The limit therefore satisfies

` partial_s v + div M + grad q = 0 `,

` div v = 0 `

in distributions. Writing

` R = M - v tensor v `

gives the Euler--Reynolds form

` partial_s v + div(v tensor v) + grad q = - div R `.

Hence, under the local normalized `L^infinity` envelope:

**`B2-ANCIENT-EULER-REYNOLDS-LIMIT = YES`.**

But there is no current theorem forcing `R=0`.

## 4. Why the Euler defect is a real missing theorem

The current B2 budgets do not provide strong `L^2_loc` compactness, a uniform positive-regularity Besov/Sobolev bound, or another estimate that makes

` v_n tensor v_n -> v tensor v `

strong enough to remove the Reynolds defect.

Axisymmetry alone does not fix this. A kinematic compactness counterprofile is

` w_k(r,z) = r chi(r,z) sin(k z) e_theta `,

with smooth axisymmetric compactly supported `chi`. In Cartesian form this is

` w_k = chi(r,z) sin(kz) (-y,x,0) `,

so it is smooth, axisymmetric, divergence-free, and uniformly bounded. Yet

` w_k weak-* -> 0 `

while the quadratic tensors retain a nonzero averaged limit proportional to

` (1/2) r^2 chi^2 e_theta tensor e_theta `.

This is **not** an NS solution sequence and is not a blow-up witness. Its role is narrower: it shows that the presently available symmetry plus amplitude compactness cannot, by itself, identify the quadratic weak limit.

Point normalization also does not guarantee a nonzero weak limit: a normalized maximum can concentrate in a set of vanishing normalized measure unless one has an independent local-mass or equicontinuity theorem.

Decision:

**`B2-ANCIENT-EULER-COMPACTNESS = NO` from the currently controlled B2 quantities.**

More precisely, the current compactness endpoint is Euler--Reynolds / Young-measure level. To upgrade it to Euler one needs a new propagated compactness theorem that kills `R`; to guarantee a nonzero limit one additionally needs normalized local mass or regularity that prevents pointwise concentration from disappearing weakly.

## 5. A broad steady-Euler Liouville kill is impossible

Even if one grants the missing strong compactness and obtains a nonzero **steady** Euler limit, there is no general finite-local-energy/compact-support Liouville contradiction available in the required axisymmetric-with-swirl class.

Primary-source facts:

1. A. V. Gavrilov, *A steady Euler flow with compact support*, GAFA 29 (2019), constructs a nontrivial smooth compactly supported steady incompressible Euler velocity in `R^3`.
2. P. Constantin, J. La, V. Vicol, *Remarks on a paper by Gavrilov: Grad--Shafranov equations, steady solutions of the three dimensional incompressible Euler equations with compactly supported velocities, and applications*, GAFA 29 (2019), gives the construction through the **stationary axisymmetric Grad--Shafranov ansatz with swirl**

   `u = r^(-1) psi_z e_r - r^(-1) psi_r e_z + r^(-1) F(psi) e_theta`,

   and explicitly notes that a smooth compactly supported stationary axisymmetric Euler velocity must vanish when the swirl `F` vanishes. Thus the nontrivial compactly supported axisymmetric examples live precisely in the swirl-capable class relevant here.
3. The same Constantin--La--Vicol paper constructs multiscale stationary Euler fields from rescaled compact templates with independently chosen positive amplitude and length parameters on disjoint supports. At the steady Euler level, amplitude versus spatial scale is therefore not pinned by a Liouville law.

Consequences:

- **`B2-STEADY-EULER-STATIC-LIOUVILLE-KILL = NO`.**
- **`B2-STEADY-EULER-STATIC-EXPONENT-CUT = NO`.**

A leading-order steady Euler core is not contradictory merely because it is smooth, localized, finite energy, axisymmetric, or has swirl.

This is distinct from the old read-only-registry kill of the **continuous self-similar steady-front NS profile**. That old route is not reopened here. The present interior scaling has a vanishing normalized viscosity and a leading stationary Euler equation; the relevant compact Euler templates are known to exist. Any new obstruction must therefore consume the **subleading Navier--Stokes modulation**, not just the leading steady Euler equation.

## 6. New positive calculation: an adjoint solvability obstruction for shape-stationary modulation

Although static steady Euler is too flexible, the next-order NS modulation has a nontrivial scalar obstruction.

Let `V` be a nonzero smooth compactly supported divergence-free steady Euler field:

` (V . grad)V + grad P = 0 `.

For a smooth divergence-free perturbation `w`, define the projected linearized steady-Euler operator

` L_V w = P_Leray[(V . grad)w + (w . grad)V] `.

Then

` <V, L_V w>_(L2) = 0 `.

Indeed,

` <V,(V.grad)w> = - <(V.grad)V,w> = <grad P,w> = 0 `,

and

` <V,(w.grad)V> = int w.grad(|V|^2/2) = 0 `.

Define the dilation forcing

` D_{gamma,alpha} V = gamma V + alpha (y . grad)V `.

Integration by parts in three dimensions gives

` <V,D_{gamma,alpha}V> = (gamma - 3 alpha/2) ||V||_2^2 `,

while

` <V,-Delta V> = ||grad V||_2^2 > 0 `.

Now use a dynamically normalized shape-preserving frame

` u(x,t) = U(t) v((x-x_c(t))/ell(t), s(t)) `,

` ds/dt = U/ell `,

with `U~tau^(-gamma)`, `ell~tau^alpha`. The normalized equation contains the small coefficients

` delta_t = ell/(U tau) ~ tau^(alpha+gamma-1) `,

` delta_nu = nu/(U ell) ~ nu tau^(gamma-alpha) `,

and, apart from a translation generator whose `L2` pairing with `V` vanishes, the first subleading forcing is

` delta_t D_{gamma,alpha}V - delta_nu Delta V `.

Therefore any asymptotic expansion in which a **fixed shape** `V` is corrected by a bounded first-order solution of the linearized steady-Euler equation must satisfy the adjoint solvability balance

` delta_t (gamma - 3 alpha/2) ||V||_2^2 + delta_nu ||grad V||_2^2 = lower-order terms `.

The ratio is

` delta_nu/delta_t = nu tau^(1-2 alpha) `.

This yields the following conditional first-order consequences:

### (a) `alpha < 1/2`

Viscosity is smaller than the modulation forcing. A bounded first-order shape correction requires

` gamma - 3 alpha/2 = 0 `,

that is

` alpha = 2 gamma/3 `.

Inside the frozen energy wedge, all strict points `alpha > 2 gamma/3` with `alpha<1/2` fail this fixed-profile first-order solvability test.

### (b) `alpha > 1/2`

Viscosity is the larger subleading forcing. After normalization by `delta_nu`, the adjoint pairing sees `||grad V||_2^2>0`, so a nonzero compact fixed profile cannot have a bounded first-order correction of this form.

### (c) `alpha = 1/2`

The two effects are comparable. Solvability requires the tuned relation

` (3/4 - gamma) ||V||_2^2 = nu ||grad V||_2^2 `.

This is not an immediate contradiction for `1/2 < gamma < 3/4`; steady Euler scaling can change the profile ratio `||grad V||_2^2/||V||_2^2`. At `gamma=3/4`, the relation would force `grad V=0` and hence excludes a nonzero compact profile.

Thus:

**`B2-STEADY-EULER-MODULATION-ADJOINT = YES` as a conditional algebraic obstruction.**

It is **not** yet an unconditional B2 cut because current B2 hypotheses do not provide:

- strong Euler compactness (`R=0`);
- a nonzero compact limiting profile;
- asymptotic stationarity of the normalized profile shape;
- a first-order expansion with bounded correction in a topology that justifies the linearized solvability equation.

Those are exactly the new load-bearing hypotheses and must not be silently assumed.

## 7. Decision table

| Decision object | Verdict | Meaning |
|---|---|---|
| `B2-ANCIENT-VANISHING-VISCOSITY` | **YES** | normalized viscosity `nu/(U ell)` tends to zero |
| `B2-ANCIENT-ETERNAL-WINDOW` | **YES** | interior `gamma+alpha>1` gives diverging forward/backward convective horizons |
| `B2-ANCIENT-EULER-REYNOLDS-LIMIT` | **YES, conditional on local normalized L∞ tightness** | weak compactness reaches Euler--Reynolds |
| `B2-ANCIENT-EULER-COMPACTNESS` | **NO from current B2 controls** | Reynolds defect / strong compactness is missing |
| `B2-STEADY-EULER-STATIC-LIOUVILLE-KILL` | **NO** | nontrivial smooth compactly supported axisymmetric steady Euler flows with swirl exist |
| `B2-STEADY-EULER-STATIC-EXPONENT-CUT` | **NO** | steady Euler scaling/templates do not pin amplitude versus scale |
| `B2-STEADY-EULER-MODULATION-ADJOINT` | **YES, conditional** | fixed-shape first-order NS modulation has an exact `L2` solvability obstruction |

## 8. Strategic ruling

The naive route

`K11 interior -> steady Euler limit -> Liouville contradiction`

is **killed as stated**.

Two independent reasons:

1. the current compactness only reaches Euler--Reynolds, not Euler;
2. the target steady-Euler class itself contains nontrivial smooth compactly supported axisymmetric-with-swirl solutions.

However, the session found a narrower non-static route that is not the old killed profile argument:

`strong defect-free compactness + asymptotic shape stationarity -> next-order NS modulation -> adjoint solvability condition`.

This is the only continuation of the ancient/steady-Euler idea worth keeping active.

## 9. Next theorem-shaped gate

Define

**`B2-MODULATION-COMPACTNESS`**:

> For one fixed hypothetical B2 solution in the K11 interior, do the actual NS equations plus existing energy/dissipation/Type-II hypotheses force, along some normalized core sequence, enough strong compactness and asymptotic shape stationarity to make the first-order steady-Euler modulation equation valid with a bounded correction?

A YES would activate the adjoint obstruction above and collapse a large part of the interior exponent wedge to the exceptional balance sets `alpha=2gamma/3` and possibly the tuned `alpha=1/2` line.

A NO should identify an actual dynamically admissible defect mechanism (Reynolds stress, moving steady-Euler moduli, or sub-core oscillation) that survives one fixed NS solution and the existing budgets. A merely kinematic oscillatory snapshot family is not enough to refute the one-fixed-solution statement.

### Stop rule

If the only way to prove `B2-MODULATION-COMPACTNESS` is to assume a continuation-strength norm (uniform positive Sobolev/Besov regularity, BKM/Serrin control, bounded H3, or equivalent), then park the ancient/steady-Euler route. Do not rename such a regularity assumption as a compactness lemma.

## 10. Forbidden shortcuts

Do not:

- call an Euler--Reynolds limit an Euler solution;
- infer nontrivial weak limit from a pointwise normalized maximum;
- drop the Reynolds defect without strong convergence;
- use Gavrilov/Constantin--La--Vicol steady Euler solutions as NS blow-up witnesses;
- reopen the old continuous self-similar steady-front route from the external registry;
- promote the conditional adjoint modulation obstruction to an unconditional exponent cut;
- use a kinematic oscillatory family as an actual-NS counterexample;
- claim Clay C/D.

## 11. Sources / provenance

Repository inputs:

- `docs/gates/TYPE2_KILL_TABLE_2026-08-19.md` (K11 and frozen exponent map);
- `docs/gates/DOMINANT_BALANCE_INVERSION_2026-08-19.md` (edge/interior Euler-dominant split);
- `docs/gates/B2_GAMMA_MAX_CURVATURE_DECISION_2026-09-06.md`;
- `docs/gates/B2_GAMMA_FLATTOP_ENSTROPHY_DECISION_2026-09-06.md`;
- `docs/gates/B2_GAMMA_TRANSITION_RESIDENCE_DECISION_2026-09-06.md`;
- `docs/gates/B2_GAMMA_STOCHASTIC_HITTING_DECISION_2026-09-06.md`.

Read-only negative-knowledge preflight:

- `ns-singularity-certificate-lab@fable5-mainline`, `docs/research_notes/verification_sprint_v1/VERDICTS.md`: continuous self-similar steady-front profile already `KILLED`; do not reopen it.

Primary Euler references:

- A. V. Gavrilov, *A steady Euler flow with compact support*, Geom. Funct. Anal. 29 (2019), 190–197; arXiv:1810.08020.
- P. Constantin, J. La, V. Vicol, *Remarks on a paper by Gavrilov: Grad--Shafranov equations, steady solutions of the three dimensional incompressible Euler equations with compactly supported velocities, and applications*, Geom. Funct. Anal. 29 (2019), 1773–1793; arXiv:1903.11699.

No Lean/runtime source is changed in this gate.
