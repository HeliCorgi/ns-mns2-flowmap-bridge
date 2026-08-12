# NS MNS-2 Flow-map Bridge

Navier–Stokes / Hou axisymmetric-with-swirl branch で、非線形 flow map と tangent propagator をつなぐ研究repoだよ〜。

## いま何がある？

中心identityは、同じ differentiable flow map `S_T` に対して

```text
S_T(c(1)) - S_T(c(0)) = ∫ DS_T(c(s))[c'(s)] ds
```

っていう path integral。v2.2 では synthetic MNS control 上で radial / Gamma-first / Omega-first の3経路が一致し、closed rectangle loop もほぼ0まで落ちてる。

**これは discrete flow-map consistency の結果であって、3D continuum Navier–Stokes の一般解証明ではないよ。**

## ディレクトリ

- `src/core/` — LF-WENO7 / full pilot / physical-metric adjoint
- `src/bridge/` — flow-map bridge
- `src/geometry/` — clustered SVD / 4-way projector geometry / temporal scan
- `src/lattice/` — grid-dt-window convergence planner/gate
- `tests/data/` — synthetic reproducibility seed/meta/schedule
- `docs/reports/` — 進捗レポ
- `failcases/` — proof / numerical inference failcase集

## Claim discipline

現状サポートされるラベルは

`EXACT DISCRETE SOLUTION-MAP REPRESENTATION: SUPPORTED`

まで。continuum general solution / blowup proof へのpromotionはまだしてないよ〜。
