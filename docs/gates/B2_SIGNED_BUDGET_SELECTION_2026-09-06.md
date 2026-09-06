# B2 signed/global budget selection — 2026-09-06

**Classification:** `BOUNDED SELECTION AUDIT / NO-CHANNEL`. This record does **not** prove blow-up, global regularity, or any Clay alternative.

## 0. Selection rule

After parking the Gamma-saturation microgeometry route and the fixed-profile ancient/steady-Euler route, the next bounded pass asked whether the original `R^3` axisymmetric Navier--Stokes solution already carries an exact **global or signed** identity that is strong enough to cut the surviving B2 wedge without taking a singular limit.

A candidate is eligible only if all four conditions hold:

1. exact actual-NS identity/inequality on the current `SPEC.md` domain/data class;
2. sign, monotonicity, or finite total budget that survives relocation of the bad set;
3. a nontrivial scaling interaction with the B2 wedge beyond existing K5 energy/dissipation and the parked Gamma-saturation microgeometry;
4. not a continuation criterion or regularity norm in disguise.

The result of the pass is:

**`B2-SIGNED-BUDGET-SELECTION = NO-CHANNEL` among the standard exact identities audited below.**

This is an inventory decision, not a theorem that no new signed functional can ever exist.

## 1. Total kinetic energy — exact but already K5

For smooth unforced NS,

`(1/2) d/dt ||u||_2^2 + nu ||grad u||_2^2 = 0`.

This is the foundational K5 budget already built into the frozen wedge. It is relocation-proof and signed, but fails the novelty requirement.

**Decision:** reject as duplicate (`K5`).

## 2. Swirl-component energy — exact exchange, wrong sign structure

Let

`E_theta(t) = int_{R^3} |u^theta|^2 dx`

and

`D_theta(t) = int [ |grad u^theta|^2 + |u^theta|^2/r^2 ] dx`.

The axisymmetric swirl equation gives

`(1/2) E_theta'(t) + nu D_theta(t)`
`  = - int (u^r/r) |u^theta|^2 dx`
`  = int S |u^theta|^2 dx`,

where `S=-u^r/r` is inward meridional strain.

The same transfer appears with the opposite sign in the poloidal kinetic-energy balance, so the total energy identity is recovered after summation.

The identity controls only the **signed** time integral of the transfer through endpoint energy and dissipation. It does not control the positive variation

`int ( int S |u^theta|^2 dx )_+ dt`.

Moreover, the session-41 hitting barrier forces large `S^+` only at a sufficiently inward location/scale; it does not force that strain to overlap a large `|u^theta|^2` volume. The transfer can therefore remain small under the same localization/co-location escapes already identified in the parked Gamma program.

**Decision:** `NO NEW CUT`.

## 3. Global circulation entropies — genuine monotonicity, too cheap near the axis

For

`Gamma = r u^theta`,

the exact equation is

`partial_t Gamma + u^r partial_r Gamma + u^z partial_z Gamma`
`  = nu (Gamma_rr - r^(-1) Gamma_r + Gamma_zz)`.

The meridional flow is divergence-free with respect to the physical axisymmetric measure `r dr dz`:

`partial_r(r u^r) + partial_z(r u^z) = 0`.

For every `p>1`, smooth decay and `Gamma(0,z,t)=0` give the exact entropy identity

`(1/p) d/dt int |Gamma|^p r dr dz`
`  + nu (p-1) int |Gamma|^(p-2) |grad_{r,z} Gamma|^2 r dr dz = 0`.

Thus every finite-`p` weighted `L^p(r dr dz)` norm of `Gamma` is nonincreasing. The `p=infinity` endpoint is the familiar maximum principle.

This is a real relocation-proof signed budget, but it does not cut the middle limb. A fixed-order circulation level `|Gamma|~M` supported near radial scale `R` over axial length `L_z` contributes only

`~ M^p R^2 L_z`

to the entropy mass. The corresponding one-scale entropy-dissipation cost is at most order

`~ M^p L_z`

before any flat-top/capacity improvement, and becomes cheaper when `L_z` shrinks. In the B2 collapse geometries already surviving K5, these quantities can tend to zero as the structure approaches the axis.

The `p=infinity` endpoint is exactly the previously audited Gamma maximum/saturation channel and does not supply a new global cost.

**Decision:** `EXACT MONOTONE, BUT NO NEW B2 EXPONENT CUT`.

## 4. Axial angular momentum — conserved but may vanish and decouples from the core

The signed axial angular momentum is

`J_z = int_{R^3} r u^theta dx`

or, in axisymmetric variables up to the `2pi` factor,

`J_z = int Gamma r dr dz`.

For smooth rapidly decaying unforced solutions it is conserved. This is also the signed `p=1` moment of the circulation equation after the axis boundary terms vanish.

However:

- admissible data may have `J_z=0`;
- even when `J_z != 0`, a collapsing fixed-amplitude `Gamma` core contributes only `~ M R^2 L_z`, which can vanish and leave the conserved angular momentum in a remote region.

Therefore conservation does not constrain the B2 core without an additional co-location hypothesis, which is precisely the parked escape-location problem.

**Decision:** `NO UNIVERSAL CUT`.

## 5. Helicity — exact evolution, no sign

For smooth decaying NS, helicity

`H(t)=int u dot omega dx`

obeys

`H'(t) = -2 nu int omega dot curl omega dx`.

The right-hand side has no sign. Energy does not control its total variation without introducing enstrophy/palinstrophy information at or above continuation strength.

Axisymmetry does not restore a sign for the full helicity production.

**Decision:** reject (`NO SIGNED FINITE BUDGET`).

## 6. Enstrophy / palinstrophy — vortex stretching wall

The exact enstrophy identity is

`(1/2) d/dt ||omega||_2^2 + nu ||grad omega||_2^2`
`  = int (omega.grad u) dot omega dx`
`  = int omega dot S omega dx`.

The production term is sign-indefinite and is the classical 3D vortex-stretching difficulty. Bounding its positive part by a globally finite quantity is already continuation-level content.

Passing to palinstrophy only moves the same problem to a higher derivative level and is strictly worse for the current purpose.

**Decision:** reject (`REGULARITY WALL`).

## 7. Normalized axisymmetric variables `q=u^theta/r` and `eta=omega^theta/r`

The exact equations are

`D_t q = 2 S q + nu L5 q`,

`D_t eta = partial_z(q^2) + nu L5 eta`.

Neither supplies an unconditional positive global entropy with the needed sign:

- `q` has the same inward-strain source that drove the parked T-SRC/spin-up analyses;
- `eta` has the divergence source `partial_z(q^2)`, which has no one-sided global sign.

Known ways to close these channels require precisely the critical swirl/strain budgets previously audited or a regularity criterion.

**Decision:** reject (`SOURCE SIGN FAILURE / PREVIOUSLY AUDITED WALL`).

## 8. Linear momentum / impulse-type moments

Linear momentum and related first moments are conserved under the usual decay assumptions, but they are signed, may vanish for admissible data, and a collapsing localized core contributes vanishingly to them. They therefore allow the conserved quantity to remain in the far field without constraining the blow-up core.

**Decision:** reject (`REMOTE-CARRIER ESCAPE`).

## 9. Selection table

| Channel | Exact sign/budget? | Relocation-proof? | New B2 scaling cut? | Verdict |
|---|---:|---:|---:|---|
| total energy | yes | yes | no — already K5 | duplicate |
| swirl/poloidal energy exchange | signed only | no at positive-part level | no | reject |
| `Gamma` finite-`p` entropies | yes, monotone | yes | no; axis collapse is cheap | reject as non-cutting |
| angular momentum | conserved signed | yes globally | no; may vanish / remote carrier | reject |
| helicity | no sign | yes globally | no | reject |
| enstrophy/palinstrophy | no free sign | yes globally | only at regularity wall | reject |
| `q`, `eta` | source terms | partly | previously audited critical wall | reject |
| momentum/impulse | conserved signed | yes globally | no; remote carrier | reject |

No standard channel passes all four selection requirements.

Therefore:

**`B2-SIGNED-BUDGET-SELECTION = NO-CHANNEL`.**

## 10. Strategic consequence

The current analytic narrowing program has now exhausted three different classes without producing an unconditional middle-limb kill:

1. local Gamma microgeometry / residence / hitting;
2. ancient/steady-Euler fixed-profile compactness and modulation;
3. standard exact global/signed invariants of the original NS solution.

This is a meaningful stop signal. Continuing by introducing another local scale, another standard norm, or another elementary conserved moment is likely to reproduce an already recorded escape.

The parent B2 middle limb remains OPEN; only the in-house analytic mechanism inventory is exhausted at this level.

## 11. What could legitimately reopen analytic work

A new analytic lane should not be opened unless it contains at least one genuinely new ingredient of one of these types:

- a nonstandard exact signed functional with a proven NS evolution law and a scaling interaction not reducible to energy/Gamma entropy;
- a one-fixed-solution cross-scale theorem coupling distant regions or times;
- a new external theorem below continuation strength that intersects the frozen B2 wedge;
- a computer-assisted argument with rigorous continuum/error control tied to an explicit admissible candidate.

Absent such an ingredient, the rational project move is to stop adding theorem-shaped escape variables and return either to the numerical candidate program / M-1 infrastructure or to bounded literature watch.

## 12. Claim boundary

Do not interpret `NO-CHANNEL` as a proof that no useful invariant exists in Navier--Stokes. It means only that the standard exact identities audited here fail the project selection test.

Do not claim B2 is realized, excluded, or that Clay C/D is proved.
