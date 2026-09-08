# R3 axisymmetric whole-space W0 result — 2026-09-07

**Decision:** `R3-W0 = PASS` for the preregistered static whole-space numerical gate.

**Scope:** static numerical infrastructure / manufactured elliptic audit only. This is not a time-evolution result, not a singularity or global-regularity theorem, not a continuum convergence theorem, and not a Clay A/B/C/D result.

## Provenance

Production revision:

```text
17a16687637c900c0ac1f62619eae04eec3ddf5c
```

Workflow:

```text
R3 whole-space W0 static gate
run 34107564243
conclusion: success
```

Artifact:

```text
r3-w0-static-report
artifact id 10012988252
sha256:38ea952245d2e84b20392d3cefeda9fe9c958e67cf952d9dc93f270203d8f4d6
```

The gate and all numerical tolerances were frozen first in
`R3_AXISYM_WHOLESPACE_W0_IMPLEMENTATION_PREREG_2026-09-07.md`.

## W0-A — exact datum generation: PASS

Frozen Cartesian grids `N=33,65,129` gave monotonically decreasing independently differenced divergence defects:

```text
N=33   max|div|=2.379543028498033e-2   rms=3.044452184153661e-3
N=65   max|div|=9.360433056019295e-3   rms=8.825241382125031e-4
N=129  max|div|=2.713709601968773e-3   rms=2.291887217458670e-4
```

The exact signed-r parity defect was `0.0`. Physical Cartesian energy stabilized to

```text
E129 = 1.94163256481464e-2
|E129-E65|/E129 = 1.0178711661959364e-7.
```

The analytic divergence identity and compact-support check passed.

## W0-B — independent Green reference and discretization: PASS

The 48^3 versus 64^3 reduced 5-D Green quadrature self-check was

```text
even max abs difference = 4.389363872370211e-12
odd  max abs difference = 8.393239228632332e-12.
```

With exact Green outer boundary values on `(Rmax,Zmax)=(2,1.2)`, the combined receiver errors decreased as

```text
even: h=.04  1.8766196463036319e-3
      h=.02  1.43898077077948e-4

odd:  h=.04  1.8417941952961526e-3
      h=.02  2.815451678618197e-4.
```

Both passed the preregistered quarter-reduction and `5e-4` fine-grid gates.

## W0-C — independent box expansion: PASS

With homogeneous outer Dirichlet data and fixed `h=.02`, radial and axial box expansions were performed independently.

Radial expansion at `Zmax=6`:

```text
Rmax       even error                 odd error
2          1.0287706638373184e-1      2.211184523368272e-2
3          2.97467640587187e-2        2.8021373828962894e-3
4          1.2376371026985489e-2      7.666740073004484e-4
6          3.627737381661155e-3       3.2107008369493956e-4
```

Axial expansion at `Rmax=6`:

```text
Zmax       even error                 odd error
1.2        1.1496650614841952e-1      9.923925351016195e-2
2          2.6631784824797482e-2      1.0660028523098167e-2
3          8.653239422535682e-3       1.6510566628734108e-3
4          4.854471172471971e-3       5.50928172022422e-4
6          3.627737381661155e-3       3.2107008369493956e-4
```

Every preregistered step decreased strictly and the common final box was below `5e-3` for both sources.

The analytic far-field envelope check also passed. The largest measured-to-envelope ratios were

```text
even 0.12604177682002488
odd  0.015861119129816834.
```

## W0-D — long-axial-scale stress: PASS

After doubling the source axial width from `0.6` to `1.2`, the independent Green self-check remained below `1e-9` and the fixed-`Rmax=6`, `h=.02` axial expansion gave

```text
Zmax       even error                 odd error
2          3.587421376209897e-2       1.9177136972153067e-2
3          1.1243293185893781e-2      2.754123328937016e-3
4          6.214035480908909e-3       7.815969877573238e-4
6          4.606005485368294e-3       2.990195910542926e-4
8          4.48602737874246e-3        2.67524827971251e-4.
```

The errors decreased strictly and passed the preregistered final `6e-3` gate. This is specifically a nonperiodic long-scale stress; it does not use a periodic low-frequency gap.

## W0-E — symmetry and measure audit: PASS

For the odd manufactured source,

```text
|lifted monopole| / lifted L1 = 2.0029798599148406e-18.
```

The report keeps the physical energy and lifted diagnostic under distinct keys:

```text
physical_energy = 1.94163256481464e-2
lifted_u1_sq    = 3.0902042034706206e-3.
```

No lifted measure is substituted for the physical `R^3` energy.

## Decision and next gate

All frozen subgates passed:

```text
W0-A PASS
W0-B PASS
W0-C PASS
W0-D PASS
W0-E PASS
R3-W0 PASS
```

This closes only the static W0 gateway. It permits opening W1 under the original preregistration rule.

The next gate is **W1 dynamic preflight**, not a growth scan. Before interpreting any evolution, W1 must freeze and verify a nonperiodic time integrator and satisfy the standing Fable5 P0-A/B/C requirements: frozen-coefficient advection-diffusion stability, pre/stage/post CFL bookkeeping, all-step streaming acceptance diagnostics, finite-state and elliptic residual checks, and a comparison integrator. The stopped periodic M-1 lane remains parked.
