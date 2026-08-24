"""
記事「サイコロで同じ目が続けて出ることはあるの？」用のシミュレーション画像を生成する。
大量のサイコロ試行から「最長連続記録」の分布をヒストグラムにし、
理論的に予測される期待値と比較する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(7)
n_simulations = 5000
n_rolls = 100

longest_streaks = []
for _ in range(n_simulations):
    rolls = rng.integers(1, 7, n_rolls)
    max_streak = 1
    cur_streak = 1
    for i in range(1, n_rolls):
        if rolls[i] == rolls[i - 1]:
            cur_streak += 1
            max_streak = max(max_streak, cur_streak)
        else:
            cur_streak = 1
    longest_streaks.append(max_streak)

longest_streaks = np.array(longest_streaks)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
bins = np.arange(1, longest_streaks.max() + 2) - 0.5
ax.hist(longest_streaks, bins=bins, color="#1e3a8a", edgecolor="white", rwidth=0.85)

mean_streak = longest_streaks.mean()
ax.axvline(mean_streak, color="#dc2626", linestyle="--", linewidth=2,
           label=f"Average longest streak = {mean_streak:.1f}")

ax.set_xlabel("Longest streak of the same number (out of 100 rolls)")
ax.set_ylabel("Number of simulations")
ax.set_title(f"{n_simulations} simulated sequences of {n_rolls} dice rolls")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/dice_streak_distribution.png")
plt.close(fig)

print("done, mean streak =", mean_streak)
