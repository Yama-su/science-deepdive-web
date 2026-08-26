"""
記事「牛乳を温めるとなぜ膜ができるの？」用のシミュレーション画像を生成する。
表面の水分が蒸発するにつれて、タンパク質濃度が
質量保存則に基づき上昇していく様子を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

f = np.linspace(0, 0.95, 300)  # 蒸発した水分の割合
C_ratio = 1 / (1 - f)  # C/C0

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(f * 100, C_ratio, color="#1e3a8a", linewidth=2.5)

denature_threshold = 3.0  # 例示的な変性が起こる濃度倍率
f_threshold = 1 - 1 / denature_threshold
ax.axhline(denature_threshold, color="#dc2626", linestyle="--", linewidth=1.5,
           label="Concentration triggering denaturation (example)")
ax.axvline(f_threshold * 100, color="#dc2626", linestyle=":", linewidth=1.2)

ax.set_xlabel("Fraction of surface water evaporated (%)")
ax.set_ylabel("Protein concentration (relative to bulk, C/C0)")
ax.set_title("Surface protein concentration rises sharply as water evaporates")
ax.set_ylim(0.5, 6)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/milk_skin_concentration.png")
plt.close(fig)

print("done")
