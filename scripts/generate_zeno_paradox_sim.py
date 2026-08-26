"""
記事「ゼノンのパラドックス」用のシミュレーション画像を生成する。
アキレスが亀に追いつくまでの時間を無限級数の部分和として計算し、
有限の値に収束していく様子を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

d0 = 100.0   # 亀の最初のリード(m)
vA = 10.0    # アキレスの速さ(m/s)
vT = 2.0     # 亀の速さ(m/s)
r = vT / vA

t1 = d0 / vA
n_steps = 20
steps = np.arange(1, n_steps + 1)
times = t1 * r ** (steps - 1)
cumulative_time = np.cumsum(times)

true_catch_time = d0 / (vA - vT)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(steps, cumulative_time, "o-", color="#1e3a8a", linewidth=1.5, markersize=4)
ax.axhline(true_catch_time, color="#dc2626", linestyle="--", linewidth=1.5,
           label=f"True catch-up time = {true_catch_time:.2f}s")

ax.set_xlabel("Number of Zeno's steps considered")
ax.set_ylabel("Cumulative time (s)")
ax.set_title("Infinitely many steps, but the total time converges to a finite value")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/zeno_paradox_convergence.png")
plt.close(fig)

print("done, true_catch_time =", true_catch_time, "final partial sum =", cumulative_time[-1])
