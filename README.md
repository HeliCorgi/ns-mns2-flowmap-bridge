# NS MNS-2 Flow-map Bridge

Navier–Stokes / Hou axisymmetric-with-swirl branch で、非線形 flow map と tangent propagator をつなぐ研究repoだよ〜。

## 最上位目標

このrepoの最上位仕様は [`PROJECT_GOAL.md`](PROJECT_GOAL.md)。

ultimate target は **Clay / Fefferman の3次元 Navier–Stokes statement A/B/C/D のいずれかを、公式の仮定とdomainに一致する形で厳密に解決すること**。

現在の主攻撃は **breakdown側（C/D）**。その中でも、数学的に成立するなら **unforced `f = 0`** の構成を優先する。

Hou有限円柱、MNS-2、flow-map identity、mild-solution interface、POD/SVD、Leanの条件付き定理は全部中間層。`R^3` / periodic Clay domain への厳密な接続なしにClay解決扱いはしない。

## いま何がある？

中心identityは、同じ differentiable flow map `S_T` に対して

```text
S_T(c(1)) - S_T(c(0)) = ∫ DS_T(c(s))[c'(s)] ds
```

っていう path integral。v2.2 では synthetic MNS control 上で radial / Gamma-first / Omega-first の3経路が一致し、closed rectangle loop もほぼ0まで落ちてる。

**これは discrete flow-map consistency の結果であって、3D continuum Navier–Stokes の一般解証明でもClay A/B/C/Dの証明でもないよ。**

## ディレクトリ

- `PROJECT_GOAL.md` — 最上位のClay goal / acceptance specification
- `AGENTS.md` — claim / exploration guardrails
- `FORMAL_SCOPE.md` — Lean側の現在の定理境界
- `HANDOFF.md` — 次セッションへの継続点
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

など各成果物の明示scopeまで。continuum general solution / blowup proof / Clay resolution へのpromotionは、`PROJECT_GOAL.md` の最終gateを満たすまでしないよ〜。
