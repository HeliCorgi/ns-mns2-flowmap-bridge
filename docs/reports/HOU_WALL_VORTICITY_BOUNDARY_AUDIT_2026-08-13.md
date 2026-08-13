# Hou wall-vorticity boundary audit

Date: 2026-08-13 JST

## Verdict

**Current MNS-2 pilot wall treatment is NOT a Hou-production no-slip vorticity closure.**

Do not promote longer-time, near-singular, or late-state results from the present pilot as a reproduction of Thomas Hou's 2022 Navier--Stokes computation until the wall closure below is implemented and independently audited.

This is a numerical-scope blocker, not a claim that the current short synthetic flow-map/JVP tests are invalid for their stated finite-discrete purpose.

## Primary equation-level requirement

Hou, *Potentially Singular Behavior of the 3D Navier--Stokes Equations*, Foundations of Computational Mathematics (2022), imposes periodicity in `z`, even pole conditions at `r=0`, and no-flow/no-slip at the solid wall `r=1`.

In the transformed variables

`u1 = u^theta/r`, `omega1 = omega^theta/r`, `psi1 = psi^theta/r`,

the paper states the pole conditions

`u1_r(t,0,z) = omega1_r(t,0,z) = psi1_r(t,0,z) = 0`.

At the solid wall it gives

`psi1(t,1,z) = 0`,

and no slip additionally implies

`psi1_r(t,1,z) = 0`.

The resulting transformed no-slip boundary is

`u1(t,1,z) = 0`,

`omega1(t,1,z) = - psi1_rr(t,1,z)`.

Hou explicitly says that the `omega1` condition is enforced as a **vorticity boundary condition** by discretizing

`omega1(t,1,z) = -psi1_rr(t,1,z)`

while imposing `psi1_r(t,1,z)=0`.

Reference: Hou 2022, Section 2, equations (2.3)--(2.5), DOI `10.1007/s10208-022-09578-4`.

## Current pilot behavior

`src/core/mns2_full_holomorphic_pilot_v1.1.py` already labels itself as a differentiability/discrete-structure pilot and states that its wall-vorticity closure is not Hou's production treatment.

The current elliptic matrix uses a homogeneous wall value for the streamfunction solve, and the same discrete `L5` operator is reused in the `omega1` diffusion path. There is no state-dependent boundary update implementing

`omega1_wall = -psi1_rr_wall`

together with the discrete no-slip constraint `psi1_r_wall=0`.

Therefore a long-time computation using this pilot solves a different discrete boundary problem from the production scheme described by Hou.

## What must be supplied before Hou-production promotion

A replacement wall closure must provide all of the following.

1. **Discrete no-flow constraint**
   - enforce `psi1=0` at `r=1` in the chosen cell/face layout.

2. **Discrete no-slip derivative constraint**
   - impose `psi1_r=0` at `r=1` with an explicitly documented stencil/ghost relation.

3. **Vorticity creation boundary condition**
   - derive the boundary value of `omega1` from the same discrete streamfunction closure via `omega1=-psi1_rr`.
   - the vorticity value must enter the `omega1` transport/diffusion operator consistently.

4. **Swirl wall condition**
   - enforce `u1=0` (equivalently `Gamma=0` at `r=1`) in a way consistent with the conservative transport/diffusion discretization.

5. **Pole conditions**
   - preserve evenness / zero radial derivative for `u1`, `omega1`, and `psi1` at `r=0`.

6. **Holomorphic tangent compatibility**
   - the frozen tangent/JVP map must differentiate the exact same wall update.
   - no state-dependent `max`, `abs`, `sign`, clipping, or branch selection may be silently inserted into the perturbed holomorphic map.

7. **Adjoint compatibility**
   - if physical-metric adjoints are used, the reverse map must include all new wall-row / ghost-row contributions.

8. **Verification gates**
   - finite-difference JVP checks must include perturbations concentrated near the wall;
   - Euclidean transpose/adjoint dot-product tests must include wall-sensitive vectors;
   - recovered wall velocities must verify `u^r=0`, `u^theta=0`, `u^z=0` to the advertised discretization accuracy;
   - refinement tests must separately track wall residuals, not only interior norms.

## Stencil status: fail closed

The 2022 paper states the boundary relations and says they are discretized, but the exact production stencil is delegated to the detailed numerical methodology cited there. This repository should **not invent a stencil and call it Hou's production stencil** without primary-source confirmation or an independent derivation/validation clearly labeled as a new scheme.

Until that source/stencil audit is complete, the allowed labels are:

- `MNS-2 finite-discrete pilot`;
- `synthetic flow-map/JVP regression`;
- `alternative wall closure` if a new closure is introduced and explicitly described.

The disallowed labels are:

- `Hou production reproduction`;
- `Hou late-state validation`;
- `resolved Hou singular regime`.

## Clay relevance

The Clay target requires an exact chain to the intended three-dimensional incompressible Navier--Stokes problem. A boundary-condition mismatch is therefore structural: numerical behavior from a different wall problem cannot be promoted merely because the interior equations or transformed variables agree.

Even a faithful reproduction of Hou's finite-cylinder computation would still be distinct from a Clay `R^3` or `T^3` result. The wall audit is necessary for Hou comparison, but it is not a domain-transfer theorem.
