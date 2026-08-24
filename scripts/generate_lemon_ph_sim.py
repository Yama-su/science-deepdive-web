"""
記事「レモンはなぜ酸っぱいの？」用のシミュレーション画像を生成する。
クエン酸の濃度に対するpHの変化(弱酸の平衡近似)を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

Ka = 7.4e-4  # クエン酸の第一解離定数(近似値)
concentration = np.geomspace(0.001, 1.0, 300)  # mol/L

H_plus = np.sqrt(Ka * concentration)
pH = -np.log10(H_plus)

lemon_conc = 0.3  # レモン果汁のおおよそのクエン酸濃度(例示的な値)
lemon_pH = -np.log10(np.sqrt(Ka * lemon_conc))

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(concentration, pH, color="#1e3a8a", linewidth=2.5)
ax.scatter([lemon_conc], [lemon_pH], color="#dc2626", zorder=5, s=60)
ax.annotate(f"Lemon juice (~{lemon_conc}mol/L)\npH ~ {lemon_pH:.2f}",
            xy=(lemon_conc, lemon_pH), xytext=(lemon_conc * 1.5, lemon_pH + 0.6),
            arrowprops=dict(arrowstyle="->", color="#dc2626"), fontsize=8, color="#dc2626")

ax.set_xscale("log")
ax.set_xlabel("Citric acid concentration (mol/L, log scale)")
ax.set_ylabel("pH")
ax.set_title("pH decreases with the SQUARE ROOT of acid concentration")
ax.grid(alpha=0.3, which="both")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/lemon_citric_acid_ph.png")
plt.close(fig)

print("done, lemon_pH=", lemon_pH)
