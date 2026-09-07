# R3 W1 arbitrary-source Green quadrature repair — result

Date: 2026-09-07 JST

## Production execution

```text
revision: bf93f6d1b3ac0864e8b8b6f3824aa7d93f92b181
workflow: R3 W1 Green quadrature repair
run: 34117229696
conclusion: success
artifact: r3-w1-green-quadrature-repair
artifact id: 10016747185
sha256:cd6db795a1e4aef3bd1f0d3f075b0c2f2f9ce6d01a1629f88ee2d96874c9efd3
```

Exact machine decision:

```text
R3-W1-GREEN-QUADRATURE-REPAIR = PASS
```

The stopped parent decision remains unchanged:

```text
PR #112: R3-W1-DYNAMIC-DOMAIN-AUDIT = STOP_REPAIR_GREEN_QUADRATURE
```

## G0 — source/runtime reproduction

All frozen source reproduction rows passed. The B44 RK4 evolution completed exactly eight accepted steps with zero rejected steps. Selected maxima:

```text
max frozen-symbol amplification = 1.0
max CFL                         = 1.0542087606169871e-10
max viscous number              = 1.8750000000000004e-3
max stage Poisson residual      = 1.1839666691113501e-14
max step Poisson residual       = 1.1055557802966425e-14
max odd-z defect                = 7.0132460922925915e-15
max energy ratio                = 0.9999848059901274
max energy-balance defect       = 1.3125894526608511e-2
```

The source audit reproduced the stopped dynamic-domain source:

```text
lifted L1                       = 7.129562804864683e-8
outside-B22 lifted-L1 fraction = 3.8008063868879254e-115
normalized lifted odd monopole = 5.255087359910218e-18
```

## G1 — three-level convergence

Frozen production levels:

```text
Q2 = source-cell GL2, theta GL64
Q4 = source-cell GL4, theta GL96
Q6 = source-cell GL6, theta GL144
```

Observed combined receiver differences:

```text
d24 = rel(Q2,Q4) = 5.828114175576683e-4
d46 = rel(Q4,Q6) = 5.842908630632889e-5
```

Thus `d46 < d24` and `d46 <= 1e-3` both passed. The final increment is about one tenth of the preceding increment.

## G2/G3 — angular and source isolation

```text
angular isolation:
rel(Q6 theta96, Q6 theta144) = 2.0958599872015252e-7

source-cell isolation:
rel(Q4 theta144, Q6 theta144) = 5.842630871480762e-5
```

Both are below the preregistered `7.5e-4` tolerances.

## G4 — active-component stability

Ten of the twelve receiver components were active under the frozen `|Q6_k| >= 1e-3 max|Q6|` mask. The maximum active componentwise relative change from Q4T to Q6 was

```text
3.4235827050088126e-4
```

against the frozen `1e-2` tolerance.

## Final repaired reference candidate

The preregistered final reference is exactly Q6. Its receiver rows `(psi, psi_r, psi_z)` are

```text
(0.12,  0.00):  4.9717796085832245e-23  -2.3339996333171292e-23   1.865209261292360e-7
(0.24,  0.20):  2.6229614780031334e-8   -3.2451403526544906e-8    6.135680149156202e-8
(0.28, -0.24): -2.6380137961913967e-8    3.9401078301785390e-8    1.8268708052777616e-8
(0.20,  0.32):  2.6931973699661990e-8   -2.7338813289256980e-8   -7.670337827221581e-8
```

## Interpretation / next gate

The repaired arbitrary-source Green path is self-resolved under the separately frozen G0–G4 gate. This authorizes only a **versioned rerun** of the stopped early dynamic-domain audit using Q6 as the frozen independent free-space reference.

The stopped PR #112 A4 rows are not retroactively reinterpreted. The versioned rerun must preserve the original boxes, dynamic evolution, common-core sensitivity rules, source checks, receivers, Poisson solve, and A4 monotonic direction rules; only the Green reference version may change to the independently passed repaired Q6 evaluator.

## Nonclaims

This PASS is not a continuum convergence theorem, a whole-space truncation theorem, a long-time evolution result, evidence of finite-time blow-up or global regularity, or a Clay A/B/C/D result.
