"""
記事「モンティ・ホール問題」用のシミュレーション画像を生成する。
「選び直す」戦略と「変えない」戦略の勝率を、大量のシミュレーションで比較する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(123)
n_trials = 50000

car_positions = rng.integers(0, 3, n_trials)
initial_picks = rng.integers(0, 3, n_trials)

stay_wins = np.sum(initial_picks == car_positions)

switch_wins = 0
for i in range(n_trials):
    doors = {0, 1, 2}
    car = car_positions[i]
    pick = initial_picks[i]
    # 司会者はcarでもpickでもない扉を開ける
    remaining = doors - {pick, car} if pick != car else doors - {pick}
    host_opens = rng.choice(list(remaining))
    switch_to = list(doors - {pick, host_opens})[0]
    if switch_to == car:
        switch_wins += 1

stay_rate = stay_wins / n_trials
switch_rate = switch_wins / n_trials

fig, ax = plt.subplots(figsize=(6.5, 5), dpi=150)
labels = ["Stay with\noriginal door", "Switch to the\nother door"]
rates = [stay_rate, switch_rate]
colors = ["#dc2626", "#1e3a8a"]

bars = ax.bar(labels, [r * 100 for r in rates], color=colors)
ax.axhline(33.3, color="#94a3b8", linestyle=":", linewidth=1.2, label="1/3")
ax.axhline(66.7, color="#94a3b8", linestyle=":", linewidth=1.2, label="2/3")

for bar, r in zip(bars, rates):
    ax.text(bar.get_x() + bar.get_width() / 2, r * 100 + 1.5, f"{r:.1%}", ha="center", fontsize=11)

ax.set_ylabel("Win rate (%)")
ax.set_ylim(0, 80)
ax.set_title(f"{n_trials} simulated games: switching wins about twice as often")
ax.grid(alpha=0.3, axis="y")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/monty_hall_simulation.png")
plt.close(fig)

print("done", stay_rate, switch_rate)
