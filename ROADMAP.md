# ROADMAP

## v2.3 — modal-coordinate bridge

初期値を `y0 = sum_k a_k e_k` に分解して、coordinate path integral

`S_T(y0)-S_T(0) = sum_k int DS_T(y^(k-1)+s e_k)[e_k] ds`

を実装するよ〜。

見るもの:
- coordinate order permutation drift
- closed-loop / commutator-style consistency
- rank-r reconstruction error
- physical-energy tail error
- grid / dt / quadrature / rank convergence

## v2.4 — SVD-compressed integrand

`DS_T(y)` を clustered SVD / Krylov subspace で圧縮して、solution representation の残差を直接測る。

## continuum promotion gate

離散 exact differential を continuum の一般解表現に昇格するには、少なくとも path 全体で `DS_T^h -> DS_T` の一様制御が必要。ここが最重要 blocker。
