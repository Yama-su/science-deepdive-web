"""
記事「分数の割り算はなぜひっくり返してかけるの？」用のシミュレーション画像を生成する。
ランダムな分数の組について、直接の割り算と「ひっくり返してかけ算」の結果が
すべて完全に一致することを散布図で数値的に検証する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(0)
n_samples = 200

a = rng.integers(1, 50, n_samples)
b = rng.integers(1, 50, n_samples)
c = rng.integers(1, 50, n_samples)
d = rng.integers(1, 50, n_samples)

direct_division = (a / b) / (c / d)
flip_and_multiply = (a / b) * (d / c)

fig, ax = plt.subplots(figsize=(6.5, 6.5), dpi=150)
ax.scatter(direct_division, flip_and_multiply, color="#1e3a8a", s=18, alpha=0.7)

lims = [0, max(direct_division.max(), flip_and_multiply.max()) * 1.05]
ax.plot(lims, lims, color="#dc2626", linestyle="--", linewidth=1.5, label="y = x (perfect match)")

ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_xlabel("(a/b) / (c/d)  [direct division]")
ax.set_ylabel("(a/b) x (d/c)  [flip and multiply]")
ax.set_title(f"{n_samples} random fraction pairs: both methods always agree")
ax.legend(loc="upper left", fontsize=8)
ax.set_aspect("equal")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/fraction_division_check.png")
plt.close(fig)

max_diff = np.max(np.abs(direct_division - flip_and_multiply))
print("done, max_diff =", max_diff)
