"""
記事「ろうそくの火はなぜ消えるの？」用のシミュレーション画像を生成する。
密閉容器内の酸素濃度が燃焼によって低下し、限界酸素濃度を下回ると
火が消えることを可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

O2_initial = 21.0  # %
LOC = 16.0          # 限界酸素濃度(%, 目安値)
consumption_rate = 0.6  # %/秒(容器サイズ等による例示的な値)

t = np.linspace(0, 10, 200)
O2 = O2_initial - consumption_rate * t
O2 = np.clip(O2, LOC - 2, None)  # 消火後は近似的に一定とみなす

extinguish_t = (O2_initial - LOC) / consumption_rate

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(t, O2, color="#1e3a8a", linewidth=2.5)
ax.axhline(LOC, color="#dc2626", linestyle="--", linewidth=1.5, label=f"Limiting O2 concentration (~{LOC}%)")
ax.axvline(extinguish_t, color="#d97706", linestyle=":", linewidth=1.5)
ax.scatter([extinguish_t], [LOC], color="#dc2626", zorder=5)
ax.annotate(f"Flame goes out\nat t~{extinguish_t:.1f}s",
            xy=(extinguish_t, LOC), xytext=(extinguish_t + 0.8, LOC + 1.5),
            arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626")

ax.set_xlabel("Time (seconds)")
ax.set_ylabel("O2 concentration in sealed jar (%)")
ax.set_title("O2 depletes as the candle burns inside a sealed jar")
ax.legend(loc="upper right", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/candle_oxygen_depletion.png")
plt.close(fig)

print("done, extinguish_t=", extinguish_t)
