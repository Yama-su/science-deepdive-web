"""
記事「円周率はなぜ終わらない数なの？」用のシミュレーション画像を生成する。
モンテカルロ法による円周率の近似を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(42)
n_points = 3000
x = rng.uniform(-1, 1, n_points)
y = rng.uniform(-1, 1, n_points)
inside = x ** 2 + y ** 2 <= 1

fig, axes = plt.subplots(1, 2, figsize=(11, 5), dpi=150)

# 左図: 点の散布図
axes[0].scatter(x[inside], y[inside], color="#1e3a8a", s=3, label="inside circle")
axes[0].scatter(x[~inside], y[~inside], color="#d97706", s=3, label="outside circle")
axes[0].set_aspect("equal")
axes[0].set_title("Monte Carlo sampling in a square")
axes[0].legend(loc="upper right", fontsize=8)

# 右図: サンプル数を増やしたときのpi推定値の収束
sample_sizes = np.geomspace(10, n_points, 40).astype(int)
estimates = []
for n in sample_sizes:
    est = 4 * np.mean(inside[:n])
    estimates.append(est)

axes[1].plot(sample_sizes, estimates, color="#6366f1", linewidth=2, label="Estimated pi")
axes[1].axhline(np.pi, color="#dc2626", linestyle="--", label="True pi = 3.14159...")
axes[1].set_xscale("log")
axes[1].set_xlabel("Number of random points")
axes[1].set_ylabel("Estimated value of pi")
axes[1].set_title("Estimate converges but never exactly settles")
axes[1].legend(fontsize=8)
axes[1].grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/pi_monte_carlo.png")
plt.close(fig)

print("done")
