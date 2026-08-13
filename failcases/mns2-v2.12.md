# MNS-2 v2.12 predictive reduced-bridge failcases

These guardrails extend the local v2.11 reduced-bridge audit.

## FC-079 — Coarse amplitude training hides the low-amplitude coefficient crossover

**Failure:** a coefficient model trained only at coarse amplitudes such as `0.25,0.5,0.75,1.0` is called converged because its quadrature integral is stable.

**Observed negative control:** on the short synthetic v2.11 map the nonlinear correction is zero at `lambda=0` but reaches nearly its plateau magnitude by roughly `lambda=5e-3 ... 1e-2`. A coarse-amplitude PCHIP fit misses this transition and gave a predictive endpoint error of about `2.27e-7`, even though the certification quadrature itself was stable.

**Required gate:** training resolution and quadrature resolution are separate. Resolve coefficient-model variation in amplitude before interpreting quadrature convergence as model convergence. The default v2.12 training mesh therefore includes `0.005,0.01,0.025,0.05,0.1` before the coarse amplitudes.

## FC-080 — POD rank is frozen before enriching the training distribution

**Failure:** a rank selected from a coarse training set is retained after adding low-amplitude snapshots, while the enlarged snapshot spectrum is ignored.

**Observed negative control:** the coarse correction snapshots looked essentially rank two, but the richer low-amplitude training set exposed additional resolved POD directions. On the current synthetic test, rank 2 remains usable but gives about `1.66e-8` endpoint error, while rank 4 gives about `9.10e-9`.

**Required gate:** whenever the amplitude/time/grid training distribution changes, recompute the singular spectrum and rerun a rank ladder. Do not transfer a previous rank label without a new residual/error audit.

## FC-081 — Certification truth leaks into the predictor

**Failure:** a held-out quadrature node is used to fit the coefficient interpolant, choose its basis, retune hyperparameters, or otherwise form `q_pred(lambda)` before its claimed prediction is recorded.

**Why it fails:** this collapses prediction back into certification projection and reintroduces FC-078 under a different name.

**Required gate:** the predictor must be fully determined from registered training amplitudes before the true JVP at a certification node is evaluated. Certification nodes must be disjoint from training nodes, and the code must form/store the prediction first, then evaluate truth only for residual auditing.
