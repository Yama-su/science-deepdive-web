"""
記事「なぜ紙は燃えるのに金属は燃えないの？」用のシミュレーション画像を生成する。
アレニウスの式を使い、活性化エネルギーの違いによる反応速度の差を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

R = 8.314  # J/(mol*K)
A = 1e13   # 頻度因子(例示的な値、両者共通と仮定)

Ea_paper = 100000   # J/mol (紙の燃焼の活性化エネルギー、例示的な値)
Ea_iron = 200000     # J/mol (鉄の燃焼の活性化エネルギー、例示的な値)

T = np.linspace(300, 1200, 300)  # K

k_paper = A * np.exp(-Ea_paper / (R * T))
k_iron = A * np.exp(-Ea_iron / (R * T))

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(T, k_paper, color="#1e3a8a", linewidth=2, label=f"Paper (Ea={Ea_paper/1000:.0f} kJ/mol)")
ax.plot(T, k_iron, color="#dc2626", linewidth=2, label=f"Iron (Ea={Ea_iron/1000:.0f} kJ/mol)")
ax.set_yscale("log")

match_flame_T = 800
ax.axvline(match_flame_T, color="#94a3b8", linestyle="--", linewidth=1.5, label="Match flame (~800K)")

ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Reaction rate constant k (log scale)")
ax.set_title("A modest difference in activation energy means a huge rate difference")
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3, which="both")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/arrhenius_paper_vs_iron.png")
plt.close(fig)

ratio_at_match = k_paper[np.searchsorted(T, match_flame_T)] / k_iron[np.searchsorted(T, match_flame_T)]
print("done, ratio at match flame temp =", ratio_at_match)
