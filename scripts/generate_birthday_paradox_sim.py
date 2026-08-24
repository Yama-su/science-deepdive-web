"""
記事「何人集まれば同じ誕生日の人がいる確率が50%を超えるのか？」用の
シミュレーション画像を生成する。
人数nに対する「少なくとも1組が誕生日を共有する確率」を計算し、
50%を超える人数を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

n_values = np.arange(1, 61)
prob_no_match = np.ones(len(n_values))

for i, n in enumerate(n_values):
    p = 1.0
    for k in range(n):
        p *= (365 - k) / 365
    prob_no_match[i] = p

prob_match = 1 - prob_no_match

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(n_values, prob_match * 100, color="#1e3a8a", linewidth=2.5)
ax.axhline(50, color="#dc2626", linestyle="--", linewidth=1.5, label="50% threshold")

cross_idx = np.argmax(prob_match >= 0.5)
cross_n = n_values[cross_idx]
ax.scatter([cross_n], [prob_match[cross_idx] * 100], color="#dc2626", zorder=5)
ax.annotate(f"n={cross_n}: {prob_match[cross_idx]*100:.1f}%",
            xy=(cross_n, prob_match[cross_idx] * 100), xytext=(cross_n + 5, 35),
            arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=9, color="#dc2626")

ax.set_xlabel("Number of people (n)")
ax.set_ylabel("Probability at least two share a birthday (%)")
ax.set_title("The birthday paradox: 50% is reached with surprisingly few people")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/birthday_paradox_curve.png")
plt.close(fig)

print("done, n at 50%:", cross_n, prob_match[cross_idx])
