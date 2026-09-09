# R3 alpha-kappa family screen — implementation freeze

Date: 2026-09-09 JST

This file records the production implementation state **before any family-screen numerical output**.

Preregistered design is in `R3_AXISYM_WHOLESPACE_FAMILY_SCREEN_PREREG_2026-09-09.md`.

Production entry point:

```text
experiments/r3_wholespace_w1/family_screen_gate.py
```

Core implementation:

```text
experiments/r3_wholespace_w1/family_screen.py
```

The core implementation reuses the already merged W1 finite-difference/Poisson/RK4 machinery and introduces only a parameterized initial-state subclass:

```text
A = alpha * nu
Z = kappa
u1_0 = A b(r^2) (z/Z) b(z^2/Z^2)
```

The two box solvers are constructed once and their factorized elliptic operators are reused across the 12 sequential parameter rows; no state is reused between rows.

A small production wrapper is frozen because the first core draft incremented an internal descriptive `valid_count` for `INVALID_DOMAIN` rows. That bookkeeping was detected **before workflow execution and before scientific output**. `family_screen_gate.py` recomputes the overall decision directly from the final row classifications so that only `NO_GROWTH_TRIGGER` and `PROMOTE_HIGH_RES` count as valid, exactly matching the preregistration. It changes no PDE, datum, grid, time step, runtime diagnostic, domain threshold, or growth threshold.

Production workflow must compile both files and execute only `family_screen_gate.py`. Any later change to the frozen parameter set or tolerances requires a new versioned gate rather than editing the result after inspection.