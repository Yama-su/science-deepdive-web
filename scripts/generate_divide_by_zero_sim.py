"""
記事「ゼロ除算の深淵」用のシミュレーション画像を生成する。
- divide_by_zero_static.png: y = 1/x のグラフ（x=0近傍で発散する様子）
- divide_by_zero_limit.gif: epsilon -> 0 で 1/epsilon が発散するアニメーション
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

OUT_DIR = "public/assets/simulations"

# --- 静止画: y = 1/x ---
fig, ax = plt.subplots(figsize=(7, 5), dpi=150)

x_pos = np.linspace(0.05, 4, 400)
x_neg = np.linspace(-4, -0.05, 400)

ax.plot(x_pos, 1 / x_pos, color="#1e3a8a", linewidth=2)
ax.plot(x_neg, 1 / x_neg, color="#1e3a8a", linewidth=2)
ax.axvline(0, color="#d97706", linestyle="--", linewidth=1.5, label="x = 0 (undefined)")
ax.axhline(0, color="#94a3b8", linewidth=0.8)

ax.set_xlim(-4, 4)
ax.set_ylim(-10, 10)
ax.set_xlabel("x")
ax.set_ylabel("y = 1/x")
ax.set_title("As x approaches 0, 1/x diverges")
ax.legend(loc="upper right")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/divide_by_zero_static.png")
plt.close(fig)

# --- アニメーション: epsilon -> 0 のときの 1/epsilon ---
fig2, ax2 = plt.subplots(figsize=(6, 4.5), dpi=120)
epsilons = np.geomspace(1.0, 0.01, 40)

def update(frame):
    ax2.clear()
    eps = epsilons[frame]
    val = 1 / eps
    ax2.bar(["1 / epsilon"], [val], color="#6366f1")
    ax2.set_ylim(0, 110)
    ax2.set_title(f"epsilon = {eps:.3f}  ->  1/epsilon = {val:.1f}")
    ax2.set_ylabel("value")

ani = matplotlib.animation.FuncAnimation(fig2, update, frames=len(epsilons))
ani.save(f"{OUT_DIR}/divide_by_zero_limit.gif", writer=PillowWriter(fps=8))
plt.close(fig2)

print("done")
