# MNS-2 v2.13 convergence-lattice failcases

## FC-082 — Stable cross-grid scalars promoted to operator/subspace convergence

**Failure:** similar endpoint-error or residual scalars on several grids are described as convergence of the tangent operator, POD subspace, or continuum flow map.

**Why it fails:** scalar agreement does not identify or compare the underlying operators/subspaces across changing discrete spaces.

**Required gate:** label the v2.13 grid axis as scalar diagnostic only. Operator/subspace promotion needs a common embedding/restriction framework and an explicit convergence metric for the represented object.

## FC-083 — Timestep refinement conflated with physical-time robustness

**Failure:** changing `dt` and number of steps simultaneously without keeping physical time fixed is called timestep convergence.

**Required gate:** the dt axis must satisfy `dt * steps = T_ref` exactly. Physical-time robustness is a separate axis at fixed `dt`.

## FC-084 — Silent step rounding used to hit a target time

**Failure:** a requested target time is approximated by rounding `T/dt` to an integer number of steps, then reported as if evaluated at the exact common physical time.

**Required gate:** reject non-representable `(dt, steps, T)` triples rather than silently rounding.

## FC-085 — Identity-dominated endpoint norm hides a poor nonlinear-correction model

**Failure:** a tiny predictive error relative to the full endpoint is used as the sole reduced-model metric even when the nonlinear correction is much smaller than the identity/Stokes-like reference tangent.

**Required gate:** always report and gate the integrated predictive residual relative to the integrated norm of the true nonlinear correction, separately from error relative to the full endpoint norm.
