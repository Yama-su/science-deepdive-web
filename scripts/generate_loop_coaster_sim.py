"""
記事「ジェットコースターはなぜループを宙返りしても落ちないの？」用の
シミュレーション画像を生成する。
ループ半径に対する頂上での最小速度、およびループ内の角度に対する
垂直抗力N(theta)の変化を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

g = 9.8

fig, axes = plt.subplots(1, 2, figsize=(11, 5), dpi=150)

# 左図: ループ半径に対する頂上での最小速度
r = np.linspace(2, 20, 200)
v_min_top = np.sqrt(g * r)
axes[0].plot(r, v_min_top * 3.6, color="#1e3a8a", linewidth=2)  # km/hに変換
axes[0].set_xlabel("Loop radius (m)")
axes[0].set_ylabel("Minimum speed at top (km/h)")
axes[0].set_title("Minimum speed at the top: v = sqrt(g*r)")
axes[0].grid(alpha=0.3)

# 右図: ループ1周の中での垂直抗力N(theta)の変化(v0はちょうど臨界速度sqrt(5gr)とする)
r_fixed = 10
v0 = np.sqrt(5 * g * r_fixed)  # 底での臨界速度
theta = np.linspace(0, 2 * np.pi, 300)
N = (v0**2) / r_fixed - 2 * g + 3 * g * np.cos(theta)  # N/m(質量で割った形)

axes[1].plot(np.degrees(theta), N, color="#d97706", linewidth=2)
axes[1].axhline(0, color="#94a3b8", linestyle=":", linewidth=1.5)
axes[1].scatter([180], [N[np.argmin(np.abs(theta - np.pi))]], color="#dc2626", zorder=5)
axes[1].annotate("Top: N is minimum (=0 at critical speed)",
                  xy=(180, 0), xytext=(60, 20),
                  arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626")
axes[1].set_xlabel("Angle around the loop (degrees, 0=bottom, 180=top)")
axes[1].set_ylabel("Normal force N / mass")
axes[1].set_title("Track force is weakest exactly at the top")
axes[1].grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/loop_coaster_forces.png")
plt.close(fig)

print("done")
