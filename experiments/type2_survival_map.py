"""Type II survival map for axisymmetric Navier-Stokes blowup exponents.

Renders docs/gates/type2_survival_map.png from the constraints derived in
docs/gates/TYPE2_SURVIVAL_MAP_2026-08-18.md (on-axis blob, core-carried L^3):

    gamma > 1/2                  (Leray + CSTY/KNSS: Type II required)
    alpha >= 2*gamma/3           (energy budget)
    alpha >  2*gamma - 1         (dissipation budget)
    alpha <  gamma               (core must carry the ESS L^3 divergence)

Survival window: 1/2 < gamma < 1, max(2g/3, 2g-1) < alpha < gamma.
"""
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#1a1d21"
INK_MUTED = "#5b6470"
DEAD_FILL = "#e8eaed"
DEAD_HATCH = "#c3c8cf"
OPEN_FILL = "#7fb3d5"
OPEN_EDGE = "#2e6f9e"
SURFACE = "#ffffff"

g = np.linspace(0.40, 1.15, 600)

fig, ax = plt.subplots(figsize=(8.6, 6.4), dpi=160)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

# Dead background (everything starts dead; the open window is drawn on top).
ax.fill_between([0.40, 1.15], 0.20, 1.15, color=DEAD_FILL, zorder=0)

# Survival window: 1/2 < g < 1, max(2g/3, 2g-1) < a < g.
gw = np.linspace(0.5, 1.0, 400)
lower = np.maximum(2 * gw / 3, 2 * gw - 1)
upper = gw
ax.fill_between(gw, lower, upper, where=upper > lower, color=OPEN_FILL,
                alpha=0.85, zorder=2, linewidth=0)

# Constraint boundary curves (2px, labeled directly).
ax.plot(g, g, color=INK_MUTED, lw=2, zorder=3)
ax.plot(g, 2 * g / 3, color=INK_MUTED, lw=2, zorder=3)
gd = np.linspace(0.5, 1.15, 300)
ax.plot(gd, 2 * gd - 1, color=INK_MUTED, lw=2, ls=(0, (5, 3)), zorder=3)
ax.axvline(0.5, color=INK_MUTED, lw=2, zorder=3)

# Hatch the dead side of the Type I wall for emphasis.
ax.fill_between([0.40, 0.5], 0.20, 1.15, facecolor="none",
                hatch="///", edgecolor=DEAD_HATCH, linewidth=0, zorder=1)

# Direct labels for the kill regions (ink text, never series-colored).
ax.text(0.445, 0.68, "KILLED\nType I\n(CSTY / KNSS\n+ Leray)", ha="center",
        va="center", fontsize=9.5, color=INK, zorder=4)
ax.text(0.63, 0.92, "KILLED: core $L^3$ stays bounded\n(ESŠ needs $\\alpha<\\gamma$)",
        ha="center", va="center", fontsize=9.5, color=INK, zorder=4)
ax.text(0.80, 0.38, "KILLED: energy budget\n(needs $\\alpha \\geq 2\\gamma/3$)",
        ha="center", va="center", fontsize=9.5, color=INK, zorder=4)
ax.text(1.055, 0.83, "KILLED:\ndissipation\nbudget\n(needs $\\alpha>2\\gamma-1$)",
        ha="center", va="center", fontsize=9.5, color=INK, zorder=4)
ax.text(0.746, 0.645, "OPEN\nwindow", ha="center", va="center", fontsize=12,
        color="#123a57", fontweight="bold", zorder=4)

# Boundary-curve labels.
ax.text(1.005, 1.035, r"$\alpha=\gamma$", fontsize=10, color=INK_MUTED,
        rotation=38, zorder=4)
ax.text(1.02, 0.655, r"$\alpha=2\gamma/3$", fontsize=10, color=INK_MUTED,
        rotation=25, zorder=4)
ax.text(0.905, 0.755, r"$\alpha=2\gamma-1$", fontsize=10, color=INK_MUTED,
        rotation=52, zorder=4)

# Reference points.
ax.plot([0.5], [0.5], marker="o", ms=9, mfc="#b3423a", mec=SURFACE, mew=1.5,
        zorder=5)
ax.annotate("Hou 2107.06509 (one-scale):\n$\\gamma=1/2$, Type I — killed",
            xy=(0.5, 0.5), xytext=(0.565, 0.30), fontsize=9, color=INK,
            arrowprops=dict(arrowstyle="-", color=INK_MUTED, lw=1), zorder=5)
ax.plot([0.5], [1.0], marker="s", ms=8, mfc="#8a8f98", mec=SURFACE, mew=1.5,
        zorder=5)
ax.annotate("Hou–Huang two-scale geometry ($\\ell\\sim\\tau$):\n"
            "Euler / degenerate-$\\nu$ only — no standard-$\\nu$ candidate",
            xy=(0.5, 1.0), xytext=(0.545, 1.065), fontsize=9, color=INK,
            arrowprops=dict(arrowstyle="-", color=INK_MUTED, lw=1), zorder=5)

# Window-closing corner.
ax.plot([1.0], [1.0], marker="o", ms=6, mfc=INK_MUTED, mec=SURFACE, mew=1.2,
        zorder=5)
ax.text(0.968, 1.062, "window closes\nat $\\gamma=1$", fontsize=9,
        color=INK_MUTED, ha="center", zorder=5)

ax.set_xlim(0.40, 1.15)
ax.set_ylim(0.20, 1.15)
ax.set_xlabel(r"velocity amplitude exponent  $\gamma$   "
              r"($\|u\|_\infty \sim \tau^{-\gamma}$)", fontsize=11, color=INK)
ax.set_ylabel(r"core scale exponent  $\alpha$   ($\ell \sim \tau^{\alpha}$)",
              fontsize=11, color=INK)
ax.set_title("Axisymmetric NS blowup — Type II survival map\n"
             "(on-axis core carrying the critical-norm divergence)",
             fontsize=12.5, color=INK, pad=12)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(INK_MUTED)
ax.tick_params(colors=INK_MUTED)
ax.grid(color="#eef0f3", lw=0.8, zorder=0)
fig.text(0.01, 0.012,
         "Derivation: TYPE2_SURVIVAL_MAP_2026-08-18.md + TYPE2_KILL_TABLE_2026-08-19.md "
         "(D1 withdrawn, see D1_ADVERSARIAL_AUDIT)  |  ring corridor & ≥3-region "
         "scenarios doc-side only  |  rev. 2026-08-19",
         fontsize=8, color=INK_MUTED)

out = Path(__file__).resolve().parents[1] / "docs" / "gates" / "type2_survival_map.png"
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(out, facecolor=SURFACE)
print(f"wrote {out}")
