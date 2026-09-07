# MNS-2 / Navier--Stokes flow-map bridge handoff

Last updated: **2026-09-07 JST — periodic M-1 parked; centered-FD `R^3` seed qualification path parked after E2R and R3S02**.

This is the durable continuation point. Merged `main` controls accepted repository state; branch
results and Actions artifacts are evidence only for the exact revisions/runs recorded below. No
current result proves Clay A/B/C/D.

## Accepted `main` boundary

Current accepted `main`:

```text
1a9228633b9cc532ece82401410a95945f27bab3
```

This includes merged PRs #102--#105. Formal state is unchanged by the numerical work below:

- whole-space local actual-NS mild theory for real divergence-free Schwartz data, including
  `MNS2.r3AdmissibleSchwartzDatum_navierStokes` and
  `MNS2.r3EndpointSafeProjectedMild_navierStokes`;
- periodic explicit special-family sidecar, including `ClayNS.certified_nonzero_periodic_NS` and
  `ClayNS.clayB_has_nonzero_smooth_specialization`;
- universal `ClayNS.ClayB` remains unproved.

No Lean/formal source changed. `FORMAL_SCOPE.md` and `STATUS.md` remain unchanged.

## Periodic M-1 lane — STOP/PARK

PR #106 is closed **unmerged**. On the frozen primary row `(c,sigma)=(16,0.125)`, E4c96 gave
`14 FAR + 3 NO_POSITIVE_LOCAL_GROWTH` across the 17 common positive-forward times, so the
preregistered `17/17 FAR->FAR` GO rule became impossible regardless of E4c128. E4c128's repeated
runner shutdowns occurred only after R0 provenance/gates passed and are infrastructure
terminations, not scientific R0 failures.

```text
M1-FILTERED-NEARFAR-PROMOTION = STOP/PARK
GO_TO_DT2 = NO
```

Do not reopen by changing calibration, selecting another row, borrowing B3, reusing E4c64, or
adding a post-hoc `dt/2` rescue.

## `R^3` axisymmetric-with-swirl numerical track

Source branch containing the completed centered-FD study:

```text
research/r3-axisym-swirl-candidate-seed
```

No PR is open. The physical target is the unforced whole-space `R^3` system in `SPEC.md`; every
finite rectangle below is only an artificial truncation.

### S0 compact continuum family — PASS

Twelve fixed `C_c^infty` axisymmetric-with-swirl data are defined analytically in `s=r^2`, with
`omega1=-L5 psi1` and Cartesian/axis reconstruction audits.

```text
run       34066171548
job       101575195688
head      763dbc36812b5a2592f3784bda31c6db65b3ba31
artifact  9998999218
digest    sha256:8f84c3175537118f07112e3d67756fe7c043f964d42fada79daf2d28c6a29582
result    12/12 PASS
```

### E0 centered second-order nonperiodic elliptic prototype — PASS as prototype

Manufactured Gaussian/compact tests, first derivatives, independent 5D Green cross-check,
one-coordinate domain enlargement, and low-axial-frequency stress pass. This is not a rigorous
free-space tail enclosure.

### E1 centered-FD nonlinear SSPRK3 smoke — PASS only as smoke

```text
run       34075898846
job       101601815270
head      dd8b06af0837b40eb221b7a54bb22b5211d76f1a
artifact  10002018444
digest    sha256:9de007fd3ecbc15c385fb47d33e40462bda548986de087dc9d9e1072a03db0a2
result    E1_pass=True
```

The short R3S04 smoke had min gradient scale `1.42877` grid points and curvature-tail `1.93098`,
so it never established a resolved trajectory or growth candidate.

### E2 R3S04 same-datum lattice — FAIL

Prereg/result:

- `R3_EVOLUTION_E2_PREREG_2026-09-07.md`
- `R3_EVOLUTION_E2_RESULT_2026-09-07.md`

```text
run       34076351801
job       101603124339
head      37368f37fb32477850388fe9abc3c0a8df5141e6
artifact  10002183475
digest    sha256:6d88d10749cc744dcf2c2afecce019b000461cf2cf9f98994dffd9de8ea511a2
NPZ sha   c14c45618f9a07c4a65d247ffa0a071d8fca3bc719120609c6fd80ab879bdf3a
```

Time refinement was tiny, but 12 field/norm spatial inequalities failed, the fine-grid minimum
gradient scale was `1.549889 < 2`, and one radial-domain `uz` physical-L2 comparison missed
`1e-3`. Exact:

```text
R3-E2-SAME-DATUM-CONVERGENCE = FAIL
R3S04-RESOLVED-R3-TRAJECTORY = NOT ESTABLISHED
```

### E2R single bounded R3S04 rescue — FAIL / R3S04 stack PARK

Prereg/result:

- `R3_EVOLUTION_E2R_PREREG_2026-09-07.md`
- `R3_EVOLUTION_E2R_RESULT_2026-09-07.md`

```text
run       34080735102
job       101615368942
head      9a99a6fd5384e1d578398edd517d4b4db318834b
artifact  10003623062
digest    sha256:608f51b57f3e9415ad9c28d2244b6f01ab6779dab5b2b2c2c4c16f9f94c31407
NPZ sha   3978b8f5a7ee1031347b6f8c4df80aed16209ac838ad360951212fc233ebf585
```

The larger-box/finer-grid rescue substantially improved the actual field comparisons:

```text
B160->B200  max rel Linf 1.90794e-1   max rel L2 1.40037e-1
B200->B240  max rel Linf 3.72495e-2   max rel L2 3.21412e-2
B240->B240H max rel Linf 1.65434e-6   max rel L2 1.52579e-6
B200->RPLUS2 max rel Linf 1.40025e-5  max rel L2 5.48611e-5
B200->ZPLUS2 max rel Linf 1.26725e-5  max rel L2 3.02934e-5
```

Every preregistered field/norm spatial comparison improved on the fine pair. Nevertheless four
frozen resolution-diagnostic conditions failed:

```text
min gradient scale  1.601357 -> 1.549890 -> 1.874704   not monotone
B240 min scale       1.874704 < 2.0
curvature-tail       1.261577 -> .939627 -> 1.070218    not monotone
B240 curvature-tail  1.070218 > 1.0
```

No rounding or threshold relaxation is allowed. Exact:

```text
R3-E2R-SAME-DATUM-CONVERGENCE = FAIL
R3S04-CENTERED-FD-ZERO-BC-STACK = PARK
NO THIRD R3S04 RESOLUTION-RESCUE LATTICE
```

### Single alternate datum R3S02 — FAIL / current 12-seed centered-FD path PARK

R3S02 was selected before evolution from the frozen continuum geometry (`s0=.04`, `ws=.05`,
`wz=.28`, `zu=0`) as the single permitted alternate datum. The preregistration explicitly
forbids seed-shopping if it fails.

Prereg/result:

- `R3_ALT_S02_QUALIFICATION_PREREG_2026-09-07.md`
- `R3_ALT_S02_QUALIFICATION_RESULT_2026-09-07.md`

Hosted provenance:

```text
workflow  R3 axisymmetric swirl R3S02 qualification
run       34081115069
job       101616428611
head      b2eaa219e69bc6ed0905334a61ccbfe757ca139d
artifact  10003744205
digest    sha256:d70b9951b74478b28a363f7ec1b0f40a671ea92df5731918099dd3a6090d52b4
NPZ sha   a2619b491089d3c27a6056ceaefc6fcb24d82f47f8c10aa7265c2ce2c718868f
```

R3S02's nonlinear short-time diagnostics are markedly cleaner than R3S04: B240 reaches exactly
`2.0` gradient-scale points, curvature-tail decreases to `.941021`, time-refinement differences
are ~`1e-6`, and domain differences are O(`1e-5`). But the fail-closed datum-specific elliptic A0
is nonmonotone from B200 to B240, and two frozen derivative comparisons fail:

```text
omega1_z relative Linf: fine 5.10054e-2 >= coarse 4.05309e-2
utheta_r relative Linf: fine 1.10767e-2 >= coarse 9.48012e-3
```

Exact:

```text
R3S02-ALT-DATUM-QUALIFICATION = FAIL
CURRENT-12-SEED-CENTERED-FD-QUALIFICATION-PATH = PARK
R3-MULTI-SEED-SCREEN = NOT LICENSED
```

Do not try R3S00/R3S06/etc sequentially under the same centered-second-order / zero-Dirichlet
method.

## Exact next allowed numerical direction

The next active numerical work must use a **genuinely new method contract**. It must restart from
manufactured elliptic and derivative qualification before any nonlinear candidate evolution. The
old centered-FD path provides diagnostic comparison only and does not confer qualification on the
new method.

Preferred smallest next gate: a high-order strictly nonperiodic finite-difference elliptic/
derivative prototype (`M0`) with explicit axis treatment, manufactured Gaussian + compact-datum
recovery, low-axial-frequency stress, and one-coordinate boundary sensitivity. Only if M0 passes
may a new nonlinear integrator/evolution qualification be preregistered.

## Forbidden shortcuts / claim boundary

Do not reopen registry-killed self-similar routes, do not identify scalar 5D `L5` with a 5D fluid,
do not fit a singularity exponent or blow-up time before numerical qualification, do not add a
third R3S04 rescue, and do not shop the current 12 seeds for a centered-FD pass. No finite-box
result is a whole-space theorem. No current result proves finite-time singularity,
nonextendability, global regularity, or Clay A/B/C/D.
