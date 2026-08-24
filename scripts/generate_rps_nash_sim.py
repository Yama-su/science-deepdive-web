"""
記事「じゃんけんで絶対に負けない方法はあるの？」用のシミュレーション画像を生成する。
偏った手を出すプレイヤーは読まれて搾取されるが、
均等な1/3ずつのランダム戦略は、どんな相手に対しても勝率がちょうど1/3に保たれ、
搾取されないことをシミュレーションで示す。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(42)
n_games = 20000

# 手: 0=グー, 1=パー, 2=チョキ (それぞれ次を負かす: 0>2, 1>0, 2>1)
def judge(a, b):
    if a == b:
        return 0
    if (a - b) % 3 == 1:
        return 1  # aの勝ち
    return -1  # bの勝ち

# ケース1: 偏ったプレイヤー(グーを60%出す)に対し、常にパーを出す相手
biased_player = rng.choice([0, 1, 2], size=n_games, p=[0.6, 0.2, 0.2])
exploiter_moves = np.full(n_games, 1)  # 常にパー
results_biased = [judge(exploiter_moves[i], biased_player[i]) for i in range(n_games)]
win_rate_exploited = np.mean(np.array(results_biased) == 1)

# ケース2: 均等ランダムなプレイヤーに対し、同じ「常にパー」戦略
uniform_player = rng.choice([0, 1, 2], size=n_games, p=[1/3, 1/3, 1/3])
results_uniform = [judge(exploiter_moves[i], uniform_player[i]) for i in range(n_games)]
win_rate_uniform = np.mean(np.array(results_uniform) == 1)

fig, ax = plt.subplots(figsize=(6.5, 5), dpi=150)
labels = ["Biased player\n(60% rock)\nvs fixed counter", "Uniform 1/3-1/3-1/3\nplayer\nvs fixed counter"]
rates = [win_rate_exploited, win_rate_uniform]
colors = ["#dc2626", "#1e3a8a"]

bars = ax.bar(labels, rates, color=colors)
ax.axhline(1/3, color="#166534", linestyle="--", linewidth=1.5, label="Fair win rate (1/3)")

for bar, r in zip(bars, rates):
    ax.text(bar.get_x() + bar.get_width() / 2, r + 0.02, f"{r:.1%}", ha="center", fontsize=10)

ax.set_ylabel("Opponent's win rate")
ax.set_ylim(0, 0.8)
ax.set_title("A biased strategy gets exploited; uniform 1/3 stays unexploitable")
ax.legend(fontsize=8)
ax.grid(alpha=0.3, axis="y")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/rps_nash_equilibrium.png")
plt.close(fig)

print("done", win_rate_exploited, win_rate_uniform)
