"""
記事「地球は丸いのに、なぜ人は落ちないの？」用のシミュレーション画像を生成する。
球の表面上のどの地点でも、重力(下向き)が常に中心を向くことを可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

fig, ax = plt.subplots(figsize=(6.5, 6.5), dpi=150)

theta_circle = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.cos(theta_circle), np.sin(theta_circle), color="#1e3a8a", linewidth=2)
ax.fill(np.cos(theta_circle), np.sin(theta_circle), color="#dbeafe", zorder=0)

angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
for a in angles:
    x, y = np.cos(a), np.sin(a)
    ax.annotate(
        "", xy=(x * 0.55, y * 0.55), xytext=(x, y),
        arrowprops=dict(arrowstyle="->", color="#dc2626", linewidth=2),
    )
    ax.scatter([x], [y], color="#166534", s=40, zorder=5)

ax.scatter([0], [0], color="#1e3a8a", s=60, zorder=5)
ax.text(0, -0.15, "center", ha="center", fontsize=9, color="#1e3a8a")

ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("Gravity ('down') always points toward the center,\nno matter where you stand on the sphere")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/gravity_direction_sphere.png")
plt.close(fig)

print("done")
