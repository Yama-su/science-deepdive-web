"""
記事「マイナス×マイナスがプラスになるのはなぜ？」用のシミュレーション画像を生成する。
3×(-2), 2×(-2), 1×(-2), 0×(-2), -1×(-2), -2×(-2) という規則的な数列を可視化し、
パターンの延長として(-1)×(-2)=2にならざるを得ないことを示す。
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

multipliers = [3, 2, 1, 0, -1, -2, -3]
values = [m * (-2) for m in multipliers]

colors = ["#1e3a8a" if m >= 0 else "#dc2626" for m in multipliers]

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
bars = ax.bar([str(m) for m in multipliers], values, color=colors)

ax.axhline(0, color="#334155", linewidth=1)
ax.set_xlabel("Multiplier (x)")
ax.set_ylabel("x times (-2)")
ax.set_title("Extending the pattern: each step adds +2")

for bar, v in zip(bars, values):
    offset = 0.6 if v >= 0 else -1.0
    ax.text(bar.get_x() + bar.get_width() / 2, v + offset, str(v), ha="center", fontsize=9)

ax.annotate(
    "Pattern forces\n(-1) x (-2) = +2",
    xy=(4, 2), xytext=(4.6, 4.5),
    arrowprops=dict(arrowstyle="->", color="#dc2626"),
    fontsize=9, color="#dc2626",
)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/negative_times_negative.png")
plt.close(fig)

print("done")
