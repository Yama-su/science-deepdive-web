"""
記事「一番大きい数はあるの？」用のシミュレーション画像を生成する。
「候補の数」に常に+1できることを示す図。
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

candidates = list(range(1, 8))
values = [10 ** n for n in candidates]

fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
ax.bar([f"N{i}" for i in candidates], values, color="#6366f1")
ax.set_yscale("log")
ax.set_ylabel("Candidate 'largest number' (log scale)")
ax.set_title("Every candidate for 'the largest number' has a successor: N -> N+1")

for i, v in enumerate(values):
    label = "N+1 exists" if i < len(values) - 1 else "...and so on, forever"
    ax.text(i, v * 1.3, label, ha="center", fontsize=8, color="#334155")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/largest_number_infinity.png")
plt.close(fig)

print("done")
