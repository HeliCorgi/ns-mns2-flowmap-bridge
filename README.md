# NS MNS-2 Flow-map Bridge

Navier–Stokes / Hou axisymmetric-with-swirl branch で、非線形 flow map と tangent propagator をつなぎつつ、現在は **実際の `R³` function-space Navier–Stokes operator 層**を Lean で組み立てている研究 repo。

## 最上位目標

この repo の最上位仕様は [`PROJECT_GOAL.md`](PROJECT_GOAL.md)。

ultimate target は **Clay / Fefferman の3次元 Navier–Stokes statement A/B/C/D のいずれかを、公式の仮定と domain に一致する形で厳密に解決すること**。

現在の主攻撃は **breakdown 側（C/D）**。その中でも、数学的に成立するなら **unforced `f = 0`** の構成を優先する。

Hou有限円柱、MNS-2、flow-map identity、mild-solution interface、POD/SVD、Lean の条件付き定理は全部中間層。`R³` / periodic Clay domain への厳密な接続なしに Clay 解決扱いはしない。

## いま何がある？

中心 identity は、同じ differentiable flow map `S_T` に対して

```text
S_T(c(1)) - S_T(c(0)) = ∫ DS_T(c(s))[c'(s)] ds
```

という path integral。v2.2 では synthetic MNS control 上で radial / Gamma-first / Omega-first の3経路が一致し、closed rectangle loop もほぼ0まで落ちている。

**これは discrete flow-map consistency の結果であって、3D continuum Navier–Stokes の一般解証明でも Clay A/B/C/D の証明でもない。**

その上で Lean 側は、抽象 bridge から `R³` の具体的な Fourier / `L²` operator 層へ進んでいる。

## 現在の formal frontier

現時点の流れはだいたい

```text
frequency-fiber algebra
        ↓
L²(R³; ℂ³) Stokes operator
        ↓
closed solenoidal L² carrier
        ↓
physical-space L² Leray projector
        ↓
Fourier-side solenoidal projector      ← いまここ
        ↓
pointwise matrix multiplier P(ξ)       ← 次
        ↓
projected convection / actual mild NS
        ↓
local theory / continuation bridge
```

まで来ている。

すでに formalized 済みなのは、

- Stokes / heat の pointwise Fourier symbol と `L²(R³; ℂ³)` operator
- normalized Fourier divergence と closed solenoidal kernel
- solenoidal carrier 上に制限した Stokes operator
- `L²(R³; ℂ³)` 上の bounded orthogonal Leray projector
- その projector の range / fixed-point / idempotence / contraction

現在の作業 frontier は、physical-space Leray projector を Plancherel Fourier transform で frequency-side projector に移す bridge。

まだ未完なのは、frequency-side の抽象 orthogonal projector を、各周波数での explicit matrix symbol

```text
P(ξ) = I - (ξ ⊗ ξ) / |ξ|²
```

と almost everywhere で同一視する部分。その後に projected convection を実際の `R³` function-space operator として組む。

## 主要な式はどこ？

式は PDF や単独ノートではなく、現在は主に `Formal/*.lean` に theorem / definition として直接入っている。

### 1. Incompressibility / divergence

Fourier 空間では

```text
ξ · û(ξ) = 0
```

を divergence-free 条件として使う。

Lean 実装:

- [`Formal/R3DivergencePointwise.lean`](Formal/R3DivergencePointwise.lean)
- [`Formal/R3NormalizedDivergenceFrequency.lean`](Formal/R3NormalizedDivergenceFrequency.lean)
- [`Formal/R3ClosedSolenoidalCarrier.lean`](Formal/R3ClosedSolenoidalCarrier.lean)

closed `L²` solenoidal carrier は概念的には

```text
L²_σ(R³) = ker(D_norm ∘ 𝓕)
```

として定義されている。

### 2. Leray projector の pointwise symbol

[`Formal/R3LerayFrequencySymbol.lean`](Formal/R3LerayFrequencySymbol.lean) に

```text
P(ξ)v = v - ((ξ · v) / |ξ|²) ξ
```

を証明済み。

つまり matrix notation では

```text
P(ξ) = I - (ξ ⊗ ξ) / |ξ|².
```

`ξ = 0` では identity になるよう Lean 側の定義と整合している。

### 3. Stokes / heat semigroup

[`Formal/R3StokesFrequencySymbol.lean`](Formal/R3StokesFrequencySymbol.lean) では mathlib の Fourier convention に合わせて

```text
λ_ν(ξ) = (2π)² ν |ξ|²
```

```text
e^{-t λ_ν(ξ)} = exp(-(2π)² ν |ξ|² t)
```

を使い、

```text
Ŝ_ν(t)u(ξ) = e^{-(2π)² ν |ξ|² t} û(ξ)
```

という scalar Fourier multiplier を定義している。

実際の bounded `L²` operator への lift は

- [`Formal/R3StokesL2Operator.lean`](Formal/R3StokesL2Operator.lean)
- [`Formal/R3StokesSolenoidalOperator.lean`](Formal/R3StokesSolenoidalOperator.lean)

にある。

### 4. Function-space Leray projector

[`Formal/R3LerayL2Operator.lean`](Formal/R3LerayL2Operator.lean) では

```text
P_L² : L²(R³; ℂ³) → L²(R³; ℂ³)
```

を closed solenoidal submodule への orthogonal projection として定義している。

証明済みの性質は

```text
range(P_L²) = L²_σ
P_L²(P_L² u) = P_L² u
P_L² u = u       if u ∈ L²_σ
‖P_L² u‖₂ ≤ ‖u‖₂
```

など。

### 5. Fourier bridge

現在の branch / PR で作業中なのが

[`Formal/R3LerayFourierBridge.lean`](Formal/R3LerayFourierBridge.lean)。

狙っている theorem は

```text
𝓕(P_L² u) = P_freq(𝓕u)
```

で、physical-space orthogonal projector と frequency-side orthogonal projector を Plancherel Fourier transform で conjugate する。

その次に必要なのが

```text
P_freq f(ξ) = P(ξ) f(ξ)    a.e. ξ,
```

つまり abstract Hilbert projection と上の explicit Leray matrix symbol の一致。

## Navier–Stokes 本体との距離

最終的に接続したい equation は unforced incompressible 3D Navier–Stokes

```text
∂ₜu - νΔu + (u · ∇)u + ∇p = 0
∇ · u = 0
```

で、Leray projection 後は形式的に

```text
∂ₜu - νΔu + P((u · ∇)u) = 0
```

mild form は

```text
u(t) = e^{νtΔ}u₀
       - ∫₀ᵗ e^{ν(t-s)Δ} P((u(s) · ∇)u(s)) ds.
```

repo には abstract quadratic mild / tangent / continuation bridge はすでにあるが、**上の `R³` Navier–Stokes nonlinear term をその abstract layer に完全接続した段階ではまだない**。

現在の `R³` formalization の目的は、まさにその missing bridge を埋めること。

## ディレクトリ

- `PROJECT_GOAL.md` — 最上位の Clay goal / acceptance specification
- `AGENTS.md` — claim / exploration guardrails
- `FORMAL_SCOPE.md` — Lean 側の現在の定理境界
- `HANDOFF.md` — 次セッションへの継続点
- `Formal/` — Lean 4 formalization。本当に証明されている式・operator・bridge はここ
- `src/core/` — LF-WENO7 / full pilot / physical-metric adjoint
- `src/bridge/` — flow-map bridge
- `src/geometry/` — clustered SVD / 4-way projector geometry / temporal scan
- `src/lattice/` — grid-dt-window convergence planner/gate
- `tests/data/` — synthetic reproducibility seed/meta/schedule
- `docs/reports/` — 進捗レポ
- `failcases/` — proof / numerical inference failcase 集

## Claim discipline

現状サポートされるラベルは

`EXACT DISCRETE SOLUTION-MAP REPRESENTATION: SUPPORTED`

など各成果物の明示 scope まで。continuum general solution / blowup proof / Clay resolution への promotion は、`PROJECT_GOAL.md` の最終 gate を満たすまでしない。
