"""
記事「影はなぜできるの？」用のシミュレーション画像を生成する。
広がりを持つ光源による半影の幅が、スクリーンまでの距離に比例して
広がっていく様子を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

w = 0.5   # 光源の幅(例示的な値)
d1 = 2.0  # 光源から物体までの距離

d2 = np.linspace(0, 10, 200)  # 物体からスクリーンまでの距離
penumbra_width = w * d2 / d1

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(d2, penumbra_width, color="#1e3a8a", linewidth=2.5)

ax.set_xlabel("Distance from object to screen (d2)")
ax.set_ylabel("Penumbra width")
ax.set_title("Penumbra width grows linearly with distance behind the object")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/shadow_penumbra_growth.png")
plt.close(fig)

print("done")
