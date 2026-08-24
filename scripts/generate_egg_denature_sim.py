"""
記事「なぜ卵は焼くと固まるの？」用のシミュレーション画像を生成する。
温度に対するタンパク質の変性割合をシグモイド曲線でモデル化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

T = np.linspace(20, 100, 400)
Tm = 65  # 変性が半分進む目安温度(モデル値)
k = 0.25

denatured_fraction = 1 / (1 + np.exp(-k * (T - Tm)))

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(T, denatured_fraction * 100, color="#1e3a8a", linewidth=2.5)
ax.axvline(Tm, color="#d97706", linestyle="--", linewidth=1.5, label=f"Tm (~{Tm}C, model)")
ax.axhline(50, color="#94a3b8", linestyle=":", linewidth=1)

ax.set_xlabel("Temperature (C)")
ax.set_ylabel("Denatured protein fraction (%)")
ax.set_title("Protein denaturation: a sharp transition, not gradual cooking")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/egg_denaturation_curve.png")
plt.close(fig)

print("done")
