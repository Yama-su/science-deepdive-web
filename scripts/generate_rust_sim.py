"""
記事「鉄はなぜさびるの？」用のシミュレーション画像を生成する。
湿度条件によって錆の進行速度がどう変わるかを、飽和曲線モデルで可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

t = np.linspace(0, 30, 300)  # days


def rust_progress(t, k):
    return 100 * (1 - np.exp(-k * t))


dry = rust_progress(t, k=0.01)
humid = rust_progress(t, k=0.15)
saltwater = rust_progress(t, k=0.35)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(t, dry, color="#94a3b8", linewidth=2, label="Dry air (low humidity)")
ax.plot(t, humid, color="#1e3a8a", linewidth=2, label="Humid air")
ax.plot(t, saltwater, color="#dc2626", linewidth=2, label="Salty humid air (coastal)")

ax.set_xlabel("Time (days)")
ax.set_ylabel("Rusted surface area (%)")
ax.set_title("Rust progression depends heavily on moisture and ions")
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/rust_progression.png")
plt.close(fig)

print("done")
