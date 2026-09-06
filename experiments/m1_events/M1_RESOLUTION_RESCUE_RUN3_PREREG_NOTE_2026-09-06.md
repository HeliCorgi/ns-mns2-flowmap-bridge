# M-1 resolution rescue — E3c128 execution note (2026-09-06)

**Classification:** `NUMERICAL EXPERIMENT EXECUTION NOTE / EVIDENCE-GRADE ONLY`.

This note records the next preregistered fixed-datum screen after `E3c64` failed and `E3c96` passed the whole-run spectral-tail gate.

The datum, viscosity, time interval, solver, and scientific threshold are unchanged. The only preregistered refinement is:

```text
run = E3c128
N = 128
nu = 0.02
T = 3.5
dt = 1/160
tail_tolerance = 1e-5 over the entire run
```

Decision rule:

- PASS only if `max_tail <= 1e-5` and the state remains finite;
- scientific tail FAIL is not an infrastructure/CI failure;
- no near/far diagnostic is run on an unresolved E3c grid;
- if `E3c128` passes, `E3c96` and `E3c128` become the first tail-qualified same-datum pair and may proceed to the preregistered refinement comparison / near-far stage;
- if it fails, do not move the threshold or invent an intermediate resolution outside the preregistered ladder.

No `R^3`, blow-up, regularity, or Clay claim is attached to this screen.
