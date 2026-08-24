"""
記事「なぜ0は偶数なのか？」用のシミュレーション画像を生成する。
-10から10までの整数を偶数/奇数で色分けし、
0が例外なく偶数のパターンにきれいに収まることを可視化する。
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

numbers = list(range(-10, 11))
is_even = [n % 2 == 0 for n in numbers]

fig, ax = plt.subplots(figsize=(9, 3), dpi=150)

for n, even in zip(numbers, is_even):
    color = "#1e3a8a" if even else "#d97706"
    marker = "o" if even else "s"
    ax.scatter([n], [0], color=color, s=200, marker=marker, zorder=3,
               edgecolor="#dc2626" if n == 0 else "none", linewidth=2.5 if n == 0 else 0)
    ax.text(n, 0.35, str(n), ha="center", fontsize=10)

ax.plot(numbers, [0] * len(numbers), color="#94a3b8", zorder=1, linewidth=1)

ax.scatter([], [], color="#1e3a8a", marker="o", s=100, label="Even")
ax.scatter([], [], color="#d97706", marker="s", s=100, label="Odd")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.3), ncol=2, fontsize=9)

ax.set_ylim(-0.5, 0.6)
ax.axis("off")
ax.set_title("0 fits perfectly into the alternating even/odd pattern\n(circled in red)", pad=40)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/zero_even_pattern.png")
plt.close(fig)

print("done")
