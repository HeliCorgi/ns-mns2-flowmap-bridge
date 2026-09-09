# R3 axisymmetric whole-space candidate-time pilot — result

Date: 2026-09-09 JST

## Production execution

```text
revision: 3d180af78735ef5a674c36b6699351da63a3cfac
workflow: R3 candidate-time pilot
run: 34316821748
conclusion: success
artifact: r3-candidate-time-pilot
artifact id: 10090698088
sha256:0cdd946049c97d61badc815cdf13d1147a3b142d6cd8fba8e4f806bd6c558d67
```

Exact machine decision:

```text
R3-CANDIDATE-TIME-PILOT = PASS_NO_GROWTH_TRIGGER_THROUGH_T025
```

This is a numerical observation only.

## C0 — streaming runtime checks

All five frozen RK4 runs completed their exact preregistered horizons with zero rejected steps:

```text
B22 h=.08 dt=.002      125 steps
B22 h=.04 dt=.0005     500 steps
B22 h=.02 dt=.000125  2000 steps
B22 h=.04 dt=.00025   1000 steps  [time-step shadow]
B44 h=.04 dt=.0005     500 steps  [later-domain veto]
```

All stage/step finite, frozen-symbol amplification, CFL, viscous-number, Poisson, odd-z parity, physical-energy, and energy-balance checks passed. The largest frozen-symbol amplification remained exactly `1.0`; the finest run's maximum Poisson residual was below `4.7e-14`.

## C1/C2 — spatial refinement

Final common-core nonlinear state:

```text
S84 = rel(B22 h=.08, h=.04) = 2.038959975950788e-3
S42 = rel(B22 h=.04, h=.02) = 5.329656270915219e-4
S42/S84                         = 0.26139092153733645
```

against the frozen `<=.45` requirement.

Recovered meridional velocity at the four frozen receivers:

```text
V84 = 1.9232957085882494e-2
V42 = 4.768672830150299e-3
V42/V84 = 0.2479427790982091
```

also passing the frozen `<=.45` requirement and remaining close to second-order `.25` refinement.

## C3 — independent time-step shadow

At fixed B22 `h=.04`, halving `dt` from `.0005` to `.00025` changed the final state and receiver velocity only at roundoff-scale relative to the spatial correction:

```text
state time difference    = 2.629599703814216e-15
state time / S42         = 4.933901118847681e-12
velocity time difference = 1.130242403768513e-15
velocity time / V42      = 2.3701403808256015e-13
```

Both frozen `<=.10` subordinate-to-spatial rules passed.

## C4 — later-time domain veto

At matched `h=.04, dt=.0005, T=.25`, B22-vs-B44 differences were

```text
state box difference       = 1.0849807283623343e-7
state box / S42            = 2.0357424066599688e-4
velocity box difference    = 2.226261629209636e-3
velocity box / V42         = 0.4668514088729104
```

Both pass the frozen `.50` limit. The velocity row is not far below the limit, so later horizons must continue to re-audit domain sensitivity rather than inherit this result indefinitely.

## Growth diagnostics on the finest run

For B22 `h=.02, dt=.000125`, physical enstrophy decreased monotonically across the frozen checkpoints:

```text
t=.05  enstrophy / initial = 0.9433850960836765
t=.10  enstrophy / initial = 0.8951727469168805
t=.25  enstrophy / initial = 0.7794650982175626
max over [0,.25] / initial = 1.0
```

At `T=.25`:

```text
physical vorticity sup / initial = 0.947673253825679
max|u1| / initial                = 0.947673253825679
max|omega1|                      = 0.00298254508274464
max|omega1| / A                  = 0.018640906767154002
```

Therefore all three preregistered follow-up triggers were false:

```text
G1 max enstrophy ratio >= 1.01       false
G2 final vorticity-sup ratio >= 1.05 false
G3 final max|u1| ratio >= 1.02       false
```

## Interpretation

The `alpha=16, kappa=1` datum passes the pilot's numerical validity checks through `T=.25`, but the monitored physical vorticity/enstrophy/swirl amplitudes show no growth trigger. Over this horizon the dominant observed behavior is dissipative, while nonzero `omega1` is generated as expected by the swirl forcing.

This result does **not** prove global regularity and does not rule out later growth. It says only that this particular frozen datum gives no preregistered reason, through `T=.25`, to promote the run as a growth candidate.

## Next research choice

The next gate should not fit a singular time or call this a failed Clay branch. Two scientifically distinct options remain:

1. extend the same datum to a separately preregistered later horizon while keeping the domain veto active; or
2. before spending much more runtime on a visibly dissipative trajectory, preregister a small `(alpha,kappa)` candidate-family screen with fail-closed numerical checks and reserve expensive matched-resolution confirmation for any parameter row that shows a genuine physical-growth trigger.

Because this pilot has no growth trigger and `A*T=.04` is still well below one nonlinear-time unit, either option is admissible; no post-hoc parameter retuning is authorized by this result alone.

## Nonclaims

No singularity, nonextendability, continuum whole-space convergence, global regularity, or Clay A/B/C/D result is established here.
