# Two-scale literature gate — Hou–Huang traveling-wave scenarios vs the Stage-A battery

Date: 2026-08-18 (JST). Pre-registration:
[`BARKER_GATE_PREREGISTRATION_2026-08-18.md`](BARKER_GATE_PREREGISTRATION_2026-08-18.md).
Companion verdict for the one-scale candidate:
[`STAGE_A_LITERATURE_VERDICT_2026-08-18.md`](STAGE_A_LITERATURE_VERDICT_2026-08-18.md).

## 1. Identification of the two-scale scenarios

The "two-scale structure observed in [24], [25]" contrasted in Hou's FoCM NS paper
(arXiv:2107.06509) is the **Hou–Huang two-scale traveling wave**:

- **[24]** T. Y. Hou, D. Huang, *Potential singularity formation of incompressible
  axisymmetric Euler equations with degenerate viscosity coefficients*, arXiv:2102.06663,
  Multiscale Model. Simul. 21 (2023).
- **[25]** T. Y. Hou, D. Huang, *A potential two-scale traveling wave singularity for 3D
  incompressible Euler equations*, Physica D (2022).

Reported geometry (from [24]'s abstract): the traveling-wave center sits on a ring of radius
`R(t) ~ (T−t)^{1/2}` around the symmetry axis while the ring thickness collapses at rate
`ℓ(t) ~ (T−t)` — a genuinely super-parabolic inner scale (`α = 1 > 1/2`), i.e. exactly the
geometry class that could support Type II amplitudes.

## 2. Gate outcomes

- **G7 (equation fidelity) — FIRES for both references.** [24] concerns Euler with
  *degenerate viscosity coefficients*; [25] concerns *Euler*. Neither is the standard
  fixed-viscosity Navier–Stokes equation of the official Clay statement. As direct Clay-C
  candidates both are out of scope by `PROJECT_GOAL.md` / `SPEC.md` §12.
- **Standard-ν transfer test — negative, by the candidate authors' own data.** Hou's FoCM NS
  paper reports verbatim that "the relative growth of the maximum vorticity of the 3D
  Navier–Stokes solution using a constant viscosity ν = 10⁻⁵ reported in [24] is less than
  2." The two-scale scenario, run under standard constant-viscosity NS, produces essentially
  **no singular growth** (compare ×10⁷ for the tuned one-scale run, itself killed by G2).
- **Structural stability note.** The same source reports that the Euler version of the
  two-scale scenario "develops a three-scale structure and the thickness of the sharp front
  does not seem to settle down to a stable scale" — the ansatz destabilizes even without
  viscosity.

## 3. Verdict

**No two-scale standard-ν Navier–Stokes candidate exists in the literature.** The two-scale
scenarios are (i) posed for Clay-inadmissible equations, (ii) reported by their own authors
to die under standard viscosity (growth factor < 2), and (iii) structurally unstable even in
the inviscid setting. The two-scale *escape hatch* is therefore currently empty of concrete
candidates; what survives of it is only the **geometry class** (super-parabolic inner scale
around a collapsing ring), which is passed as input to the Type II survival map
([`TYPE2_SURVIVAL_MAP_2026-08-18.md`](TYPE2_SURVIVAL_MAP_2026-08-18.md)) to decide whether
*any* amplitude assignment on such geometry can thread the known exclusion theorems.

Reopen condition for the two-scale route: a standard fixed-ν NS computation exhibiting
sustained growth on a two-scale geometry with converged diagnostics, passing G1–G7 —
none is currently reported anywhere.
