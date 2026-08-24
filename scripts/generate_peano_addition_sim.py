"""
記事「1+1はなぜ2になるの？」用のシミュレーション画像を生成する。
ペアノの公理に基づく再帰的な足し算の定義が、通常の足し算と
常に一致することを数値的に検証する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"


def succ(n):
    return n + 1


def pred(n):
    return n - 1


def peano_add(a, b):
    """a + b を、a+0=a, a+S(b)=S(a+b) という再帰的定義だけで計算する。"""
    if b == 0:
        return a
    return succ(peano_add(a, pred(b)))


rng = np.random.default_rng(3)
n_samples = 150
a_vals = rng.integers(0, 200, n_samples)
b_vals = rng.integers(0, 200, n_samples)

peano_results = np.array([peano_add(int(a), int(b)) for a, b in zip(a_vals, b_vals)])
native_results = a_vals + b_vals

fig, ax = plt.subplots(figsize=(6.5, 6.5), dpi=150)
ax.scatter(native_results, peano_results, color="#1e3a8a", s=18, alpha=0.7)

lims = [0, max(native_results.max(), peano_results.max()) * 1.05]
ax.plot(lims, lims, color="#dc2626", linestyle="--", linewidth=1.5, label="y = x (perfect match)")

ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_xlabel("a + b (native addition)")
ax.set_ylabel("peano_add(a, b) (recursive Peano definition)")
ax.set_title(f"{n_samples} random pairs: Peano's recursive definition always matches")
ax.legend(loc="upper left", fontsize=8)
ax.set_aspect("equal")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/peano_addition_check.png")
plt.close(fig)

max_diff = np.max(np.abs(peano_results - native_results))
print("done, max_diff =", max_diff)
