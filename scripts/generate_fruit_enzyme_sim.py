"""
記事「果物は熟れるとなぜ甘くなるの？」用のシミュレーション画像を生成する。
ミカエリス・メンテン式による酵素反応速度のグラフを描く。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

Vmax = 10.0  # 最大反応速度(例示的な値)
Km = 5.0     # ミカエリス定数(例示的な値)

S = np.linspace(0, 50, 300)  # 基質(でんぷん)濃度
v = Vmax * S / (Km + S)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(S, v, color="#1e3a8a", linewidth=2.5)
ax.axhline(Vmax, color="#94a3b8", linestyle=":", linewidth=1.5, label=f"Vmax = {Vmax}")
ax.axhline(Vmax / 2, color="#d97706", linestyle="--", linewidth=1.2)
ax.axvline(Km, color="#d97706", linestyle="--", linewidth=1.2, label=f"Km = {Km}")
ax.scatter([Km], [Vmax / 2], color="#dc2626", zorder=5)

ax.set_xlabel("Substrate (starch) concentration [S]")
ax.set_ylabel("Reaction rate v")
ax.set_title("Michaelis-Menten kinetics: enzyme-driven starch-to-sugar conversion")
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/fruit_enzyme_kinetics.png")
plt.close(fig)

print("done")
