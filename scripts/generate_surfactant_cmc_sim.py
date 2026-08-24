"""
記事「洗剤はなぜ油を落とせるの？」用のシミュレーション画像を生成する。
界面活性剤の濃度と水の表面張力の関係、臨界ミセル濃度(CMC)を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

concentration = np.geomspace(0.001, 10, 300)  # mM(対数スケール)
CMC = 1.0  # mM(例示的な値)
tension_water = 72.0  # mN/m, 純水の表面張力
tension_plateau = 30.0  # mN/m, CMC以上での表面張力

log_c = np.log10(concentration)
log_cmc = np.log10(CMC)

tension = np.where(
    concentration < CMC,
    tension_water - (tension_water - tension_plateau) * (log_c - log_c.min()) / (log_cmc - log_c.min()),
    tension_plateau,
)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(concentration, tension, color="#1e3a8a", linewidth=2.5)
ax.axvline(CMC, color="#dc2626", linestyle="--", linewidth=1.5, label=f"CMC (~{CMC} mM)")
ax.set_xscale("log")

ax.annotate("Micelles start forming\nsurface tension plateaus",
            xy=(CMC, tension_plateau), xytext=(CMC * 2, tension_plateau + 10),
            arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626")

ax.set_xlabel("Surfactant concentration (mM, log scale)")
ax.set_ylabel("Surface tension (mN/m)")
ax.set_title("Surface tension drops sharply, then plateaus at the CMC")
ax.legend(loc="upper right", fontsize=8)
ax.grid(alpha=0.3, which="both")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/surfactant_cmc_curve.png")
plt.close(fig)

print("done")
