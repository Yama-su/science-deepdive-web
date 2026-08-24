"""
記事「磁石はなぜくっつくの？」用のシミュレーション画像を生成する。
磁気双極子間の力(1/r^4)が、重力(1/r^2)よりずっと急激に
距離とともに弱まることを対数グラフで可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

r = np.geomspace(0.01, 1.0, 200)  # メートル

F_magnet = 1 / r**4
F_gravity = 1 / r**2

# 同じ基準(r=0.01m)で正規化して比較しやすくする
F_magnet /= F_magnet[0]
F_gravity /= F_gravity[0]

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(r, F_magnet, color="#1e3a8a", linewidth=2, label="Magnetic dipole force ~ 1/r^4")
ax.plot(r, F_gravity, color="#d97706", linewidth=2, label="Gravity / Coulomb force ~ 1/r^2")
ax.set_xscale("log")
ax.set_yscale("log")

ax.set_xlabel("Distance (m, log scale)")
ax.set_ylabel("Relative force (log scale, normalized at r=0.01m)")
ax.set_title("Magnetic force falls off much faster than gravity")
ax.legend(loc="upper right", fontsize=8)
ax.grid(alpha=0.3, which="both")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/magnet_force_falloff.png")
plt.close(fig)

print("done")
