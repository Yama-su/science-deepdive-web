"""
記事「虹はどうやってできるの？」用のシミュレーション画像を生成する。
水滴中での屈折・反射による偏角(deviation angle)を入射角の関数として計算し、
赤色光と紫色光で最小偏角がわずかにずれることで虹の色分かれが起こる様子を示す。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

n_red = 1.331
n_violet = 1.344

theta_i = np.linspace(0.1, 89.9, 2000) * np.pi / 180  # 入射角(ラジアン)


def deviation_deg(theta_i, n):
    theta_r = np.arcsin(np.sin(theta_i) / n)
    D = np.pi + 2 * theta_i - 4 * theta_r  # ラジアン
    return np.degrees(D)


D_red = deviation_deg(theta_i, n_red)
D_violet = deviation_deg(theta_i, n_violet)

theta_i_deg = np.degrees(theta_i)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(theta_i_deg, D_red, color="#dc2626", linewidth=2, label=f"Red light (n={n_red})")
ax.plot(theta_i_deg, D_violet, color="#7c3aed", linewidth=2, label=f"Violet light (n={n_violet})")

# 最小偏角の位置をマーク
idx_red_min = np.argmin(D_red)
idx_violet_min = np.argmin(D_violet)
ax.scatter([theta_i_deg[idx_red_min]], [D_red[idx_red_min]], color="#dc2626", zorder=5)
ax.scatter([theta_i_deg[idx_violet_min]], [D_violet[idx_violet_min]], color="#7c3aed", zorder=5)

ax.annotate(
    f"Min deviation\n{D_red[idx_red_min]:.1f} deg",
    xy=(theta_i_deg[idx_red_min], D_red[idx_red_min]),
    xytext=(theta_i_deg[idx_red_min] - 30, D_red[idx_red_min] + 8),
    arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626",
)
ax.annotate(
    f"Min deviation\n{D_violet[idx_violet_min]:.1f} deg",
    xy=(theta_i_deg[idx_violet_min], D_violet[idx_violet_min]),
    xytext=(theta_i_deg[idx_violet_min] - 30, D_violet[idx_violet_min] - 14),
    arrowprops=dict(arrowstyle="->", color="#7c3aed"), fontsize=8, color="#7c3aed",
)

ax.set_xlabel("Angle of incidence (degrees)")
ax.set_ylabel("Total deviation angle D (degrees)")
ax.set_title("Deviation angle vs incidence angle for red and violet light")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/rainbow_deviation.png")
plt.close(fig)

print("done")
print("red min:", theta_i_deg[idx_red_min], D_red[idx_red_min], 180 - D_red[idx_red_min])
print("violet min:", theta_i_deg[idx_violet_min], D_violet[idx_violet_min], 180 - D_violet[idx_violet_min])
