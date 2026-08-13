# MNS-2 v2.11 reduced-bridge failcases

These failcases are local guardrails for the path-correction POD experiment. They extend the broader project audit history without claiming that the entire historical failcase ledger is mirrored in this repository.

## FC-077 — Quadrature residual estimate called a rigorous integrated-residual certificate

**Failure:** a finite Gauss/panel evaluation of

\[
\int_0^1\|g(\lambda)-q(\lambda)\|\,d\lambda
\]

is reported as a proved upper bound on the reduced endpoint error solely because the analytic inequality

\[
\left\|\int(g-q)\right\|\le\int\|g-q\|
\]

is valid.

**Why it fails:** the analytic inequality concerns the exact integral. A floating-point quadrature approximation to its right-hand side has its own discretization/quadrature error and need not be an upper enclosure.

**Required gate:** distinguish the formal exact inequality from its numerical estimator. For a numerical certificate, add a converged quadrature ladder or a validated/interval enclosure for the scalar residual integral. Until then label the value `quadrature residual estimate`, not `rigorous residual bound`.

## FC-078 — Certification projection called a predictive low-cost reduced model

**Failure:** `q_r(lambda)=g0+P_r c(lambda)` is evaluated by first computing the true JVP correction `c(lambda)` at every quadrature node, and the resulting low-dimensional output is then described as a predictor that avoids full tangent solves.

**Why it fails:** the projection compresses the output representation but does not reduce the online cost if the full correction must still be evaluated before projecting it.

**Required gate:** distinguish `representation compression / certification projection` from `predictive reduced model`. A predictive model must produce the POD coefficients from reduced data (for example an independently trained amplitude model) without using the true JVP at the same evaluation node, and must be tested on held-out nodes with an explicit residual budget.
