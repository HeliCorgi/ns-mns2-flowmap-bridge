# R3 W1 elliptic discretization / boundary-error decomposition — result

Date: 2026-09-07 JST

## Production execution

```text
revision: bfcbb52dc46c501bf59ab040e3d012454f47fbb0
workflow: R3 W1 elliptic discretization-boundary decomposition
run: 34118150738
conclusion: success
artifact: r3-w1-elliptic-decomposition
artifact id: 10017101755
sha256:6f6c2270f523f210a6375110fe9ac7d63b0aba85c96d5fd79dba81a02a056d27
```

Exact machine decision:

```text
R3-W1-ELLIPTIC-DECOMPOSITION = PASS
```

Parent decisions remain unchanged:

```text
PR #112  dynamic-domain v1  = STOP_REPAIR_GREEN_QUADRATURE
PR #113  Green repair       = PASS
PR #114  dynamic-domain v2  = STOP_REPAIR_DYNAMIC_DOMAIN
```

## E0 — source and Green reproduction

All source/runtime rows and the independently passed Q6 Green isolation rows passed again.

## E1 — spatial order on B22

Receiver differences across the frozen three-level elliptic refinement were

```text
d42 = rel(h=.04,h=.02) = 4.191328398605410e-3
d21 = rel(h=.02,h=.01) = 1.047328148841019e-3
fine/coarse ratio       = 2.498797634634161e-1
```

against the preregistered `<=.35` ratio. This is essentially the expected second-order `.25` reduction.

## E2 — Richardson stabilization

For

```text
X42 = (4 R_.02 - R_.04)/3
X21 = (4 R_.01 - R_.02)/3
```

on B22,

```text
rel(X42,X21) = 8.881891892944590e-7
rel(X42,X21) / d21 = 8.480524373161707e-4
```

well below the frozen `.35*d21` requirement.

## E3 — original box-direction question after discretization reduction

The fixed-`h=.04` PR #114 errors to Q6 were

```text
B22 4.598734911371308e-3
B23 4.848264397380328e-3
B24 4.854020029975020e-3
B32 4.923712918590292e-3
B42 4.937515097721673e-3
B44 5.547358297635768e-3
```

and therefore moved in the wrong direction under box expansion.

At `h=.02` they dropped to roughly `1e-3` but were still not a clean monotone box sequence:

```text
B22 1.237469018830008e-3
B23 1.003147377865653e-3
B24 1.000684832411958e-3
B32 1.044829894534782e-3
B42 1.043339336614003e-3
B44 1.358775982035425e-3
```

After the preregistered second-order Richardson extrapolation, the errors were

```text
B22 1.671546886567295e-3
B23 1.144411622396564e-3
B24 1.133375112119839e-3
B32 1.083593623465416e-3
B42 1.060477287070227e-3
B44 5.563242519255671e-5
```

so all five original direction rows passed:

```text
B32 < B22
B42 < B32
B23 < B22
B24 < B23
B44 <= min(B42,B24).
```

## Diagnostic decomposition

The inter-resolution `.04/.02` difference was nearly box-independent:

```text
B22 4.191328398605410e-3
B23 4.192630135905506e-3
B24 4.192664335024259e-3
B32 4.191947376883716e-3
B42 4.191982620326396e-3
B44 4.193700579067095e-3
```

while same-resolution adjacent box changes were much smaller and already stable across refinement. For example radial small-to-mid stayed near `5.9e-4`, radial mid-to-large near `2.32e-5`, axial small-to-mid near `5.3e-4`, and axial mid-to-large near `1.11e-5` at `.04`, `.02`, and after Richardson extrapolation.

This supports the preregistered narrow diagnosis: the PR #114 fixed-grid continuum comparison was dominated by leading finite-difference error, and smaller-box boundary corrections partially cancelled that error. Once the leading discretization term was separately validated and removed, the original box-direction trend reappeared.

## Interpretation / next gate

This PASS does **not** retroactively turn PR #114 into a PASS. It also does not show that the `h=.04` dynamic solver is quantitatively resolved enough for long-time use.

The next smallest gate should therefore be a **resolution-aware early-time dynamic audit**: rerun the nonlinear dynamics at matched `.04/.02` resolution on a minimal frozen box set, preserve all streaming diagnostics, and verify that the dynamic state / recovered-velocity observables exhibit the expected refinement behavior while the independently established box sensitivity remains smaller than the discretization correction.

Only after such a dynamic resolution gate passes should a candidate-time pilot be opened.

## Nonclaims

This result is not a continuum theorem, not a rigorous whole-space truncation enclosure, not a long-time evolution result, not evidence of finite-time blow-up or global regularity, and not a Clay A/B/C/D result.
