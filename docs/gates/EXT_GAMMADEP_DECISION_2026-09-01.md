# (EXT-ΓDEP-1) — external Γ-DEP decision record, IMPORTED (2026-09-01)

**Provenance.** Produced by a ChatGPT-side pass; supplied **verbatim by the user on
2026-09-01** in the commissioning conversation of freeze review round 3. Registered
IMPORT-PENDING in `FREEZE_REVIEW_3_2026-09-01.md` §5 earlier the same day; imported
here with the in-repo audit of §B below. Transcription artifacts of the chat medium
(mangled LaTeX brackets, dropped `ν` factors, literal `c_<c_0`) are **preserved in
§A** and repaired only in the audit's restatements.

**Headline (as reported): `Γ-DEP decision = UNDERDETERMINED`.** Not PROVED (no
τ-uniform axis depletion follows from the frozen Scope-B inputs + maximum principle
+ circulation–vorticity identities + finite energy + time-integrated enstrophy +
known Hölder/Harnack machinery); not COUNTERMODEL (the counterprofile is
field-level, single-time — promoting it to an actual finite-time singular NS
trajectory is the open core itself). The record names **(Γ-OSC)**, a τ-uniform
boundary-oscillation contraction for `Γ` at core scale — its "minimal new input"
framing is superseded by §B2.1: *the most direct identified sufficient condition*,
sufficiency only.

---

## §A. The external record, verbatim as supplied

```text
判定は UNDERDETERMINED です。現時点では frozen Scope-B のまま (Γ-DEP) は証明できず、かつ actual Navier–Stokes trajectory の反例も構成できません。ただし、指数簿記より一段強い「実際の滑らかな divergence-free 場」レベルの反例 profile は構成できるため、energy/enstrophy・circulation/vorticity identities・瞬間的な incompressible kinematics だけから (Γ-DEP) を出すルートは閉じています。

1. (Γ-DEP) の field-level statement は少し修正して固定すべき

既存記録では

[
\sup_{r\le \delta\tau^\alpha}|\Gamma|<c'\Gamma_0
]

という形です。

ただし frozen class は

[
\liminf_{t\uparrow T_*}\frac{\|\Gamma(t)\|_\infty}{\Gamma_0}\ge c_0>0
]

しか仮定していません。したがって単に c' ∈ (0,1) とすると、c' > c_0 を選んで saturation level 自体が存在しない、という vacuous なケースが混ざります。

actual theorem として一意に固定するなら、私は次を operative statement にします。

[
(\Gamma\text{-DEP})_{\rm fld}:\quad
\exists\,c_*\in(0,c_0),\ \delta>0,\ \tau_0>0\
\forall\,0<\tau<\tau_0,\qquad
\sup_{\substack{z\in\mathbb R\\0\le r\le\delta\tau^\alpha}}
|\Gamma(r,z,T_*-\tau)|
<c_*\Gamma_0 .
]

ここで (\Gamma=r u^\theta)。

これなら (c_*<c_0) により level (c_*\Gamma_0) は終端近くで非自明に存在し、

[
r_{\rm sat}(t;c_*)\ge\delta\tau^\alpha
]

なので power-law (r_{\rm sat}\asymp\tau^{\beta_v}) があるなら

[
\beta_v\le\alpha.
]

つまり middle limb を本当に排除します。

2. exact identities は (Γ-DEP) を与えない

軸対称 NS では circulation は

[ \partial_t\Gamma +u^r\partial_r\Gamma+u^z\partial_z\Gamma
=
\nu\left(
\partial_r^2-\frac1r\partial_r+\partial_z^2
\right)\Gamma,
\qquad
\Gamma|_{r=0}=0.
]

標準 Laplacian で書けば、文献で (\Theta=r u_\theta) と書かれている量について

[
(\partial_t+(u+2e_r/r)\cdot\nabla-\Delta)\Theta=0
]

です。Ożański–Palasek もこの方程式から axis 近傍の Hölder estimate を導いています。(DOI)

また exact に

[
\omega^z=\frac{\partial_r\Gamma}{r},
\qquad
\omega^r=-\frac{\partial_z\Gamma}{r}.
]

したがって

[ E_\theta
=
2\pi\int\frac{\Gamma^2}{r}\,dr\,dz,
]

および swirl に由来する enstrophy は

[
2\pi\int
\frac{|\Gamma_r|^2+|\Gamma_z|^2}{r}\,dr\,dz.
]

これだけ見ると一見かなり強そうですが、middle saturation のコストは frozen budget で十分払えます。

3. actual divergence-free counterprofile が作れる

任意の

[
(\gamma,\alpha)\in S_{\rm blob},
\qquad
\alpha<\beta<\gamma
]

を固定します。既存 frozen wedge は (\gamma<1)、(\alpha<\gamma)、energy/dissipation の条件を持っています。

[
a(\tau)=\tau^\beta,\qquad \ell(\tau)=\tau^\alpha.
]

滑らかな compactly-supported 関数 (\chi,\eta) を、(\chi(s)=s^2) near (s=0)、(\chi(1)=1)、(\eta(0)=1) となるよう選び、

[ \Gamma_\tau(r,z)
=
m\Gamma_0\,
\chi\!\left(\frac r a\right)
\eta\!\left(\frac{z-z_*}{a}\right),
\qquad c_0<m<1
]

とします。

すると

[
u^\theta_\tau=\frac{\Gamma_\tau}{r}
]

は axis で (O(r)) なので Cartesian に滑らかです。そして (r\sim a) に

[
|\Gamma_\tau|\sim m\Gamma_0
]

が存在するため、

[
\frac a{\tau^\alpha}
=\tau^{\beta-\alpha}\to0.
]

したがって 任意の固定 (\delta>0) に対し終端近くでは saturation が (r<\delta\tau^\alpha) に入り、(Γ-DEP)_fld を破ります。

この sub-core の scaling は

[
\|u^\theta\|_\infty\asymp a^{-1}
=\tau^{-\beta}
=o(\tau^{-\gamma}),
]

[
E_\theta\asymp \Gamma_0^2 a
=\Gamma_0^2\tau^\beta,
]

[
\|\omega^{r,z}\|_2^2
\asymp\Gamma_0^2 a^{-1}
=\Gamma_0^2\tau^{-\beta},
]

[
\|u^\theta\|_3^3\asymp O(1).
]

しかも (\beta<1) なので

[
\int_0^{\tau_0}\tau^{-\beta}\,d\tau<\infty.
]

つまり O(1) circulation を sub-core に置くコストは Leray dissipation budget と両立します。

さらに別途、scale (\ell=\tau^\alpha)、amplitude (U=\tau^{-\gamma}) の axisymmetric poloidal blob を streamfunction から作れます。例えば

[ \psi_{1,\tau}
=
\tau^{-\gamma}
\Phi\!\left(\frac r\ell,
\frac{z-z_*}{\ell}\right),
]

[
u^r=-r\partial_z\psi_1,\qquad
u^z=2\psi_1+r\partial_r\psi_1.
]

これは identically divergence-free です。その scaling は

[
E_{\rm pol}\asymp
U^2\ell^3
=\tau^{3\alpha-2\gamma},
]

[
D_{\rm pol}\asymp
U^2\ell
=\tau^{\alpha-2\gamma},
]

[
\|u_{\rm pol}\|_3^3
\asymp U^3\ell^3
=\tau^{3(\alpha-\gamma)}\to\infty.
]

frozen (S_{\rm blob}) の

[
\alpha\ge\frac{2\gamma}{3},
\qquad
\alpha>2\gamma-1,
\qquad
\alpha<\gamma
]

が、ちょうど

finite energy,
time-integrable dissipation,
(L^3) divergence

を同時に許します。

したがって

[ u_\tau
=
u_{\rm pol,\tau}
+
u^\theta_\tau e_\theta
]

は、smooth / compactly supported / axisymmetric / divergence-free / axis-regular な actual 3D field で、frozen の主要 budget を満たしつつ (Γ-DEP) を破れます。

これは前回の (W^\star) より一段強いです。単なる exponent tuple ではありません。

ただし重要なのは、({u_\tau}_{\tau\downarrow0}) が 1本の NS trajectory であることは証明していないことです。各 snapshot は admissible な滑らかな divergence-free datum ですが、それらを1本の有限時間 blow-up trajectory として接続できれば、それ自体が未解決問題の核心です。

したがって verdict は COUNTERMODEL には上げられません。

4. Γ PDE の dynamic scaling も直ちには矛盾しない

saturation radius (a=\tau^\beta) を inward に動かす速度スケールは

[
|\dot a|\sim \frac a\tau
=\tau^{\beta-1}.
]

viscosity と競合する速度スケールは

[
\frac{\nu}{a}
\sim\nu\tau^{-\beta}.
]

middle limb では

[
\beta>\alpha\ge1-\gamma,
\qquad
\beta<\gamma.
]

したがって

[
\tau^{\beta-1}\lesssim\tau^{-\gamma},
\qquad
\nu\tau^{-\beta}\lesssim\tau^{-\gamma}.
]

つまり frozen の amplitude budget (\|u\|_\infty\asymp\tau^{-\gamma}) は、radial compression と diffusion の両方を balance できるだけの速度を許している。

ここにも exponent-level contradiction はありません。

5. 既知の parabolic regularity がちょうど足りない

Γ 方程式には確かに near-axis Hölder mechanism があります。Ożański–Palasek の Proposition 5.1 は

[
\operatorname{osc}_{B(r)}\Gamma
\lesssim
\left(\frac rR\right)^{\eta}
\operatorname{osc}_{Q_R}\Gamma,
\qquad
\eta=\exp(-\mathcal N(R)^{O(1)})
]

という形で、(\mathcal N(R)) は drift の scale-critical norm に依存します。(DOI)

問題は frozen Scope-B がその (\mathcal N) を τ-uniform に制御しないことです。

core で

[
R=\tau^\alpha,\qquad
|u|\sim\tau^{-\gamma}
]

なら、critical drift size は概念的に

[
R\|u\|
\sim\tau^{\alpha-\gamma}\to\infty.
]

したがって Hölder exponent は 0 に退化し得ます。

同論文が紹介する "almost Hölder" estimate も、slightly-supercritical な 追加の local energy bound を仮定して初めて得られるものです。(DOI) Frozen B2 の (U R\sim\tau^{\alpha-\gamma}) は polynomial に発散するため、その仮定は frozen rows からは出ません。

repo 内部の K12 監査も同じ方向を示しています。closed-streamline diffusion は (\alpha>1/2) なら強くなり得ますが、(\alpha<1/2) では accumulated diffusive time が bounded で homogenization は forced ではない。さらに K12″ は nested foliation、axis/free-boundary topology、uniform spectral gap など追加仮定つきの [C] のままです。

したがって K12 を (Γ-DEP) の proof として流用することもできません。

6. 不足する最小の新入力は1つ

指数条件ではありません。

必要なのは core-scale で τ-uniform な Γ の boundary oscillation contraction です。例えば新しい1定理を

[
\text{(Γ-OSC)}
]

として、

ある固定

[
0<\theta<1,\qquad 0<q<1
]

があり、終端近くの全ての axis-centered parabolic cylinder、特に

[
R=\tau^\alpha
]

について

[
\operatorname{osc}_{Q_{\theta R}}\Gamma
\le
q\,\operatorname{osc}_{Q_R}\Gamma
]

が τ に依存しない同じ (q,\theta) で成り立つ、とするものです。

Γ は axis 上で 0、かつ (\|\Gamma\|_\infty\le\Gamma_0) なので、固定回数 (N) だけ iterate して

[
2q^N<c_0
]

と取れば、

[
\sup_{r\le\theta^N\tau^\alpha}|\Gamma|
<c_*\Gamma_0,\qquad c_*<c_0,
]

すなわち (Γ-DEP)_fld が直ちに出ます。

これが今回の minimal new input です。

要するに必要なのは、

Type-II の大きな meridional drift があっても、axis の Dirichlet condition (\Gamma=0) の影響が core scale (\tau^\alpha) の固定割合まで τ-uniform に浸透する

という genuinely parabolic な定理です。

これは Γ の「空間配置」を制御します。K3/K5/K6/K9/K11 の exponent arithmetic を1本追加しても代用できません。

Decision record

(Γ-DEP) decision = UNDERDETERMINED.

PROVED ではない理由は、既存 maximum principle、circulation-vorticity identities、finite energy、time-integrated enstrophy、および既知 Hölder/Harnack machinery のいずれも frozen Scope-B 下で τ-uniform な axis depletion を与えないためです。COUNTERMODEL ではない理由は、field-level counterprofile は構成できるものの、それを1本の actual finite-time singular NS trajectory に昇格することは未解決だからです。

今回かなりはっきりしたのは、次に必要なのは新しい指数不等式ではなく (Γ-OSC) 型の drift–diffusion / boundary-Harnack 機構だという点です。

なお、2026年6月には axisymmetric-with-swirl の無条件大域正則性を主張する arXiv preprint も出ていますが、これは非常に強い未検証の主張で、独立した確立済み入力としては扱わず今回の判定には使用していません。(arxiv.org)
```

*(End of verbatim record. The `(DOI)` / `(arxiv.org)` markers are citation
placeholders as supplied — the identifiers did not survive the chat medium; see
debts D-1/D-3 below.)*

---

## §B. In-repo audit (2026-09-01) — against the round-3 §5 import checklist

**Overall: PASS at snapshot level.** Every derivable claim was independently
recomputed; the construction is sound as a single-time field. Itemized:

1. **Divergence-free** — verified exactly: for `u^r = −r∂_zψ₁`,
   `u^z = 2ψ₁ + r∂_rψ₁`, `∇·u = (1/r)∂_r(ru^r) + ∂_zu^z = (−2∂_zψ₁ − r∂_r∂_zψ₁)
   + (2∂_zψ₁ + r∂_r∂_zψ₁) = 0` identically; the swirl component contributes no
   divergence in axisymmetry. (The `ψ₁` convention matches the Hou-form used
   elsewhere in this program.)
2. **Axis regularity** — `χ(s) = s²` near `s = 0` gives `Γ = O(r²)`, so
   `u^θ = Γ/r = O(r)`: Cartesian-smooth. The poloidal part needs `Φ` even in its
   first argument for axis smoothness — a free choice, implicitly available;
   noted, not a defect.
3. **Scalings** — all recomputed and confirmed: `‖u^θ‖_∞ ≍ Γ₀τ^{−β} = o(τ^{−γ})`;
   `E_θ ≍ Γ₀²τ^{β}` (the `s²` vanishing kills the axis logarithm — log-free,
   matching OOV-3 hygiene); swirl enstrophy `≍ Γ₀²τ^{−β}`, `dτ`-integrable for
   `β < 1` (K5b); `‖u^θ‖₃³ = O(1)` (the exactly-critical invisibility the β_v
   decision's §4 predicted); `E_pol ≍ τ^{3α−2γ}` finite on the window (K5a);
   `D_pol ≍ τ^{α−2γ}` integrable iff `α > 2γ−1` (A7); `‖u_pol‖₃³ ≍ τ^{3(α−γ)} → ∞`
   (K6). The window inequalities are consumed **exactly**, none to spare.
4. **Class constraints** — Γ-max (`‖Γ‖_∞ = mΓ₀ < Γ₀`), non-evanescence
   (`m > c₀`), envelope (at `r ≍ τ^β`: `r‖u‖_∞ ≍ τ^{β−γ} → ∞ ≫ Γ₀`, flat branch
   binds, corner attainment fails), K2 Type-II, blob shape `v = 3λ`, `ρ = λ`: all
   PASS. The field realizes **a strictly more conservative, swirl-free-outer
   variant of C13's tuples at field level** — the swirl is confined to the
   sub-core (no outer `1/r` branch), so region C's `σ` component is vacuous
   rather than realized; fewer rows fire than for `W★`.
5. **(Γ-DEP)_fld sharpening — ADOPTED as the operative field-level statement.**
   The 2026-08-23 print's `c′ ∈ (0,1)` admits a vacuity: for `c′ > c₀` the
   saturation level need not exist (then `r_sat(c′) = ∞` and `β_v` at that level
   is undefined). Requiring `c_* ∈ (0, c₀)` makes the level non-trivially attained
   near `T*` and the pin derivation (`r_sat ≥ δτ^α ⟹ β_v ≤ α`) unconditional. This
   is a **statement-level refinement**, not a change of the 08-23 ruling; recorded
   here, cross-referenced from HANDOFF.
6. **(Γ-OSC) ⟹ (Γ-DEP)_fld** — verified: `Γ = 0` on the axis and `‖Γ‖_∞ ≤ Γ₀`
   give `osc_{Q_R}Γ ≤ 2Γ₀` and `sup_{r ≤ θ^NR}|Γ| ≤ osc_{Q_{θ^N R}}Γ ≤ 2q^NΓ₀`;
   choosing `N` with `2q^N < c₀` and `c_* ∈ (2q^N, c₀)` yields (Γ-DEP)_fld with
   `δ = θ^N`. Clean; the implication consumes only axis Dirichlet + Γ-max.
7. **Dynamic-scaling consistency (§4 of the record)** — recomputed: inward speed
   `τ^{β−1} ≲ τ^{−γ}` ⟺ `β ≥ 1−γ` (holds: `β > α ≥ 1−γ`); diffusion speed
   `ντ^{−β} ≲ τ^{−γ}` ⟺ `β ≤ γ` (holds). No exponent-level contradiction ✓.
8. **§5's degeneration mechanism** — the scale-critical drift size
   `R‖u‖ ≍ τ^{α−γ} → ∞` is exactly the corpus's recurring `τ^{α−γ}` misfire
   factor (K9/A1); the convergence of the two records on this one factor is
   noted as corroborating, not proof.

**Named debts (carried, not discharged):**

- **D-1 [V?]** Ożański–Palasek: Proposition 5.1's exact form
  (`η = exp(−N(R)^{O(1)})`) and the "almost Hölder" variant's slightly-
  supercritical hypothesis — citation identifiers lost in transit; full-text
  verification owed before any chain consumes §5's negative claim.
- **D-2 [to verify at commissioning]** Bare-drift falsity risk: for general
  divergence-free supercritical drifts, parabolic continuity/Harnack is known to
  fail in 3D in some regimes (the Seregin–Silvestre–Šverák–Zlatoš divergence-free
  drift line — exact scope to be verified first-hand). If confirmed, a bare-drift
  (Γ-OSC) is likely FALSE, and the statement fixer **must** decide which
  NS/axisymmetric-specific structure (the drift being the actual NS velocity;
  the `2ν e_r/r` term; the axis boundary; K11's viscous-scale placement) the
  decision consumes. This is a feature: it makes Γ-OSC genuinely two-sided.
- **D-3 [WATCH, unverified, consumed by nothing]** The reported June-2026 arXiv
  preprint claiming **unconditional global regularity for axisymmetric NS with
  swirl** — unidentified (no arXiv number survived transit). If it existed and
  were verified, it would terminate the entire axisymmetric breakdown track
  (CAP-level event). To be identified and read first-hand at the next literature
  pass; used nowhere until then, exactly as the external record itself ruled.
  *(Status 2026-09-02: **IDENTIFIED and triaged first-hand** — arXiv:2606.07869v1,
  Shahmurov, supplied by the user as a PDF and read in full; adversarially
  adjudicated **load-bearing gaps CONFIRMED** at the variational core (G1a/G1b)
  and the exhaustion layer (G2); correctness NOT ESTABLISHED; **still consumed by
  nothing; no CAP fire**. Master record:
  `D3_TRIAGE_2606_07869_2026-09-02.md`, incl. watch/re-check triggers.)*

**Effect on the round-3 record:** condition (1) of `FREEZE_REVIEW_3_2026-09-01.md`
§6 (import first) is **discharged**; condition (2) (statement fixing in frozen
vocabulary — now seeded by §A's (Γ-DEP)_fld and (Γ-OSC) drafts plus debts D-1/D-2)
**stands**; condition (3) (the pre-registered termination rule) **stands as refined
by §B2.5**. See the round-3 record's §8 addendum.

**Claim boundary (unchanged):** the counterprofile is a single-time field, not a
trajectory; nothing here constructs or implies blow-up; UNDERDETERMINED is a
statement about derivability at frozen scope, not about Navier–Stokes; no Clay
claim of any kind.

---

## §A2. Second external record (same source, same day) — verbatim as supplied

```text
これは前回より一段おもしろいです。今回の結果で、かなり重要な切り分けができています。

一番大きいのは、

「指数簿記だけではダメ」

だけでなく、

「各時刻の smooth/div-free/finite-energy な場だけ見てもダメ」

まで進んだことです。

つまり (Γ-DEP) を強制するなら、snapshot の幾何・energy・enstrophy・circulation identities では足りず、NS の時間発展そのものを使わないといけない。これは研究上かなり有用な no-go です。

今回の3値判定も UNDERDETERMINED が妥当です。構成した u_τ は actual smooth 3D field なので、単なる exponent tuple より強い。一方で {u_τ}_{τ↓0} を単一の Navier–Stokes trajectory にするところはまさに未解決部分なので、COUNTERMODEL に上げなかったのも正しいです。

ただし、一箇所だけ表現を弱めた方がいいです。

> 「不足する最小の新入力は (Γ-OSC)」

これは現時点では

> 「確認できた最も直接的な十分条件」

くらいが正確です。

(Γ-OSC) が論理的に必要最小であることまでは、この調査からは出ていません。NS dynamics には、uniform Hölder contraction 以外にも、meridional transport の幾何、vorticity coupling、time-coherence、非局所的制約などから (Γ-DEP) を出す可能性があります。

なので、Γ-OSC ⟹ Γ-DEP はかなり明瞭。

でも Γ-DEP ⟹ Γ-OSC や「Γ-OSC以外では無理」は未証明です。

### 次に何をやるか

ここでいきなり

> (Γ-OSC) を証明せよ

にすると、かなり巨大な問題になる可能性があります。

次の decision theorem はもう一段小さくした方がいいです。

焦点は、

Γ_t + b·∇Γ = ν(∂_r² − (1/r)∂_r + ∂_z²)Γ

について、τ-uniform oscillation contraction を得るために必要な drift control が、frozen B2 から本当に出るかです。

例えば次タスクはこうです。

> Γ-OSC feasibility decision を行え。frozen Scope-B は変更しない。まず既知の
> drift–diffusion / boundary regularity theorem から、core scale R = τ^α において
> τ-uniform な oscillation contraction
>   osc_{Q_{θR}}Γ ≤ q·osc_{Q_R}Γ,  q, θ < 1
> を得るための最弱の定量的 drift 条件を明示せよ。その条件が frozen B2 から導かれるか、
> または frozen B2 と両立しながらその drift 条件を破る smooth divergence-free
> field/profile を構成できるかを両方向から検証する。結論は
> IMPLIED / VIOLATED / UNDERDETERMINED の3値とする。新しい exponent restriction を
> 追加して代用しないこと。

これを先にやる理由があります。

今の記述では critical size が概ね R‖u‖ ~ τ^{α−γ} → ∞ なので、既知の De Giorgi/Hölder
machinery をそのまま使うと exponent が潰れる、というところまで来ています。

だったら次の問いは、

「NS 特有の構造によって、この『巨大 drift』を一般 drift より良く扱えるか？」

です。

ここが YES なら (Γ-OSC) に本当に新しい勝ち筋があります。

ここが NO に近いなら、Γ depletion lane 自体の期待値がかなり下がります。

もう一つ良い点があります。今回の smooth snapshot counterprofile は今後のテストケースとして
保存すべきです。新しい「Γ depletion theorem」が出るたびに、その仮説をこの profile に当てて、

* どの仮説が snapshot を排除しているのか
* それは genuine NS dynamic input なのか
* 実は hidden Scope-A assumption を入れていないか

をチェックできます。

要するに今回の成果は、

指数だけでは決まらない
        ↓
instantaneous NS-compatible geometryでも決まらない
        ↓
時間発展を本当に使う必要がある
        ↓
drift–diffusion boundary regularity が候補
        ↓
★ 次はここが genuine NS structure で強化できるか判定

まで来た、ということです。

これはかなりちゃんと Stage 9 の研究になっています。
```

## §B2. Audit addendum for §A2 — adopted rulings

1. **Γ-OSC status weakened — ADOPTED.** §A's "minimal new input" claim for (Γ-OSC)
   is **superseded**: the established relation is one-directional,
   **`(Γ-OSC) ⟹ (Γ-DEP)_fld`** (§B item 6); neither the converse nor any
   exclusivity is proved. Operative wording from now on: *"(Γ-OSC) is the most
   direct identified sufficient condition for (Γ-DEP)_fld."* This is the exact
   analogue, one level down, of the round-3 **C0** policy for (Γ-DEP) itself
   (sufficient-only; no "unique closer" language) — the same hygiene now applies
   at both levels of the chain
   `(Γ-OSC) ⟹ (Γ-DEP)_fld ⟹ β_v ≤ α ⟹ middle limb closed`.
2. **The escalated no-go — ADOPTED as the record's headline result.** The chain
   "exponent bookkeeping insufficient (β_v decision) → single-time
   NS-compatible smooth geometry insufficient (§A counterprofile) → any (Γ-DEP)
   proof must consume the time evolution" is verified in-repo (§B items 1–6
   confirm the middle step; the first step is the frozen 08-23 ruling).
3. **Next-decision reduction — ADOPTED as the recommended commissioning shape.**
   The **Γ-OSC feasibility decision** as drafted in §A2 (extract the weakest
   quantitative drift condition for the τ-uniform contraction at `R = τ^α` from
   known drift–diffusion/boundary-regularity theorems; then check **both**
   directions — IMPLIED by frozen B2 / VIOLATED by an explicit frozen-compatible
   smooth divergence-free profile / UNDERDETERMINED; no new exponent restrictions
   as substitutes) is strictly smaller than "prove (Γ-OSC)" and directly targets
   the live uncertainty (§B debt D-2: whether NS-specific structure beats the
   generic large-drift obstruction `R‖u‖ ≍ τ^{α−γ} → ∞`). It subsumes D-1/D-2 as
   its literature step.
4. **Counterprofile promoted to a standing test case — ADOPTED.** Rule recorded:
   every future Γ-depletion-type theorem candidate must be run against §A's
   `u_τ` to identify (i) which hypothesis excludes the snapshot, (ii) whether
   that hypothesis is a genuine NS-dynamic input, (iii) whether it smuggles a
   Scope-A assumption. (This is the same discipline as the map's misfire checks.)
5. **Termination framing refined** (supersedes the two-strikes clause's wording in
   `FREEZE_REVIEW_3_2026-09-01.md` §6, recorded in its §8 addendum): the branch
   continues past the feasibility decision **only on IMPLIED** (or a partial
   IMPLIED naming the consumed NS structure). **VIOLATED** closes the
   generic-machinery route and drops the Γ-depletion lane's expected value to
   near-nil — end/pivot justified; a second consecutive **UNDERDETERMINED**
   exhausts the in-house inventory — the BH branch ends. Pivot options unchanged
   (the `SPEC.md` numerical candidate program; literature-level Seregin watch).
