# M1 boundary/localization estimate audit — 2026-09-04

## Verdict

- **Localized Betchov `J_B` as a physical enstrophy-transport mechanism: ROUTE-KILLED.**
  Fable's cross-check correctly identifies `q+4 det S = 4 det(∇u) = div J_B`; the `J_B` language is a divergence representation of the regional third invariant, not an independent transport mechanism.
- **A direct cutoff boundary estimate does exist**, but it is not scale-uniform enough to close regularity.
- **Replacement candidate:** filtered near/far vortex-stretching decomposition. Positive near-field stretching can be absorbed by diffusion up to a lower-order filtered-enstrophy reservoir; the unresolved burden moves to far-field strain, commutator forcing, and localization residuals.

## 1. Direct localized Betchov estimate [D]

For smooth incompressible `u`, let `A=∇u`, `q=ω^T S ω`, and
\[
q+4\det S = \nabla\cdot J_B,
\qquad
|J_B|\le C |u|\,|\nabla u|^2.
\]

Let `χ` be a smooth cutoff with `χ=1` on `B_r`, supported in `B_{2r}`, and
\[
|\nabla χ|\le C/r.
\]
Then
\[
\int χ q
=
-4\int χ\det S
-\int J_B\cdot\nabla χ.
\]

The boundary/localization remainder obeys
\[
\left|\int J_B\cdot\nabla χ\right|
\le
\frac{C}{r}\|u\|_2\|\nabla u\|_4^2.
\]
Using
\[
\|\nabla u\|_4
\le
C\|\nabla u\|_2^{1/4}\|\nabla^2u\|_2^{3/4},
\]
and Young,
\[
\boxed{
\left|\int J_B\cdot\nabla χ\right|
\le
\varepsilon\nu\|\nabla^2u\|_2^2
+
C\varepsilon^{-3}\nu^{-3}r^{-4}
\|u\|_2^4\|\nabla u\|_2^2.
}
\]

Since `||u(t)||_2 <= ||u_0||_2`,
\[
\boxed{
|B_\chi(t)|
\le
\varepsilon\nu P(t)
+
C_{\varepsilon}\nu^{-3}r^{-4}
\|u_0\|_2^4 E(t).
}
\]

This is a real estimate: at every fixed `r>0`, the boundary term is diffusion-absorbable plus a term linear in enstrophy. But the coefficient blows up like `r^{-4}`, so it gives no scale-uniform closure as a potential singular core shrinks.

## 2. Why this does not solve the wall

At a dynamically shrinking radius `r(t)`, the coefficient
\[
r(t)^{-4}\|u_0\|_2^4
\]
is worse as `r→0`. Thus the direct `J_B` boundary route does not create a free critical quantity. It repackages the cubic invariant into a localization remainder and returns a shrinking-scale obstruction.

This matches the Fable result that `β_B` is primarily an alignment/third-invariant coordinate, not an independent regularizing mechanism.

## 3. Physically meaningful replacement: near/far strain [D + literature lead]

For the strain represented by Biot–Savart, split at radius `R`:
\[
S=S_R^{near}+S_R^{far}.
\]
Integrating the far kernel by parts from vorticity to velocity and applying Cauchy–Schwarz gives the free-energy estimate
\[
\boxed{
\|S_R^{far}(t)\|_\infty
\le
C R^{-5/2}\|u(t)\|_2
\le
C R^{-5/2}\|u_0\|_2.
}
\]
Hence
\[
\boxed{
\int \chi (S_R^{far}\omega\cdot\omega)_+
\le
C R^{-5/2}\|u_0\|_2
\int\chi |\omega|^2.
}
\]

The remaining dangerous part is the singular near field.

A June-2026 arXiv preprint by Runlong Yu proves, for spatially filtered vorticity, a finite-scale near-field coercive estimate of the form
\[
\mathcal V^{near,+}_{r,\ell}
\le
(1-\varepsilon)\mathcal P^\rho_{r,\ell}
+
C_\varepsilon M_{r,\rho}(u)
\left(\frac r\ell\right)^5
\mathcal O_{r,\ell},
\]
where `P` is filtered diffusion, `O` filtered enstrophy, and `M` a scale-invariant local energy quantity. For `ell = sigma r`,
\[
\boxed{
\mathcal V^{near,+}_{r,\sigma r}
\le
(1-\varepsilon)\mathcal P^\rho_{r,\sigma r}
+
C_{\varepsilon,\sigma}
M_{r,\rho}(u)\mathcal O_{r,\sigma r}.
}
\]

This is much closer to the desired cancellation estimate than the Betchov `J_B` flux language: positive singular near-field stretching is actually absorbed by diffusion, modulo a lower-order reservoir.

## 4. Combined finite-scale shape

Schematic combined localized filtered balance:
\[
\boxed{
\mathcal V^+
\lesssim
(1-\varepsilon)\mathcal P
+
\Big[
C_{\varepsilon,\sigma}M_{r,\rho}(u)
+
C\,\frac{\|u_0\|_2}{\sqrt r}
\Big]\mathcal O
+
\mathcal C_{\rm comm}
+
\mathcal L_{\rm loc}.
}
\]

The exact bookkeeping depends on the chosen filter/cutoff. The key point is the obstruction list:

1. scale-uniform control/packing of the far-field contribution;
2. commutator forcing from filtering;
3. localization residuals;
4. scale-uniform local energy / packing input.

So the near-field singular stretching itself is not the remaining wall in this formulation.

## 5. M-1 experiment that is now decision-relevant

Do **not** run more `β_B`-only tests.

At the same M-1 snapshots, measure for a ladder
\[
R=c\sqrt{\nu/\Lambda},\qquad
\ell=\sigma R
\]
the trajectories

- `near_positive_stretch / diffusion`;
- `far_positive_stretch / enstrophy`;
- local scale-invariant energy `M_R`;
- filter commutator work;
- localization residual;
- alignment `cos^2 theta_2` as explanatory geometry.

Use stateflow only as the episode/transition harness. The decision question is:

> Does every resolved enstrophy-growth event enter a regime where the near-field term is diffusion-absorbed and the positive surplus is carried by one reproducible residual class (far field / commutator / localization)?

If yes, that residual becomes the one proof target.
If no, this finite-scale decomposition does not select a universal mechanism and should be parked.

## Current label

**BETCHOV-BOUNDARY: ROUTE-KILLED as a new physical mechanism.**

**FILTERED-NEAR/FAR: REPLACEMENT-CANDIDATE / literature-backed finite-scale estimate, not promoted to a Clay proof head.**
