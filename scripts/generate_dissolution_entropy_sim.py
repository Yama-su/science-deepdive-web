"""
記事「塩や砂糖は水に溶けるとどこへ消えるの？」用のシミュレーション画像を生成する。
混合のエントロピー変化を、モル分率に対してプロットする。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

R = 8.314  # J/(mol*K)

x1 = np.linspace(0.001, 0.999, 300)
x2 = 1 - x1

delta_S_mix = -R * (x1 * np.log(x1) + x2 * np.log(x2))  # 1molあたり

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(x1, delta_S_mix, color="#1e3a8a", linewidth=2.5)
ax.axvline(0.5, color="#94a3b8", linestyle=":", linewidth=1.5)

max_idx = np.argmax(delta_S_mix)
ax.scatter([x1[max_idx]], [delta_S_mix[max_idx]], color="#dc2626", zorder=5)
ax.annotate(f"Maximum at 50:50 mix\n{delta_S_mix[max_idx]:.2f} J/(mol*K)",
            xy=(x1[max_idx], delta_S_mix[max_idx]), xytext=(0.15, delta_S_mix[max_idx] - 1.2),
            arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626")

ax.set_xlabel("Mole fraction of solute (x1)")
ax.set_ylabel("Entropy of mixing per mole (J/(mol*K))")
ax.set_title("Mixing always increases entropy: this drives dissolution")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/dissolution_entropy_mixing.png")
plt.close(fig)

print("done")
