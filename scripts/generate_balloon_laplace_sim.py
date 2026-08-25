"""
記事「風船はなぜ膨らませ始めが一番大変なの？」用のシミュレーション画像を生成する。
ラプラスの法則 ΔP = 2*gamma/r に基づき、風船の半径が小さいほど
必要な圧力が大きくなることを可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

gamma = 0.05  # 膜の張力(例示的な値)

r = np.linspace(0.005, 0.15, 300)  # メートル
delta_P = 2 * gamma / r

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(r * 100, delta_P, color="#1e3a8a", linewidth=2.5)

r_small = 0.01
r_large = 0.1
ax.scatter([r_small * 100, r_large * 100], [2 * gamma / r_small, 2 * gamma / r_large],
           color="#dc2626", zorder=5)
ax.annotate(f"Small balloon\n(r=1cm): needs\nhigh pressure",
            xy=(r_small * 100, 2 * gamma / r_small), xytext=(6, 8),
            arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626")
ax.annotate(f"Large balloon\n(r=10cm): needs\nmuch less pressure",
            xy=(r_large * 100, 2 * gamma / r_large), xytext=(11, 3),
            arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626")

ax.set_xlabel("Balloon radius (cm)")
ax.set_ylabel("Required pressure difference (relative units)")
ax.set_title("Laplace's law: smaller radius needs disproportionately more pressure")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/balloon_laplace_pressure.png")
plt.close(fig)

print("done")
