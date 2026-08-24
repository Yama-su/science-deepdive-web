"""
記事「お酢と重曹を混ぜるとなぜ泡が出るの？」用のシミュレーション画像を生成する。
重曹の量に対して発生する二酸化炭素の体積が、
酢が律速となるまでは比例して増えることを可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

M_NaHCO3 = 84.0  # g/mol
R = 0.0821       # L*atm/(mol*K)
T = 298          # K
P = 1.0          # atm

vinegar_moles_available = 0.15  # mol(例:大さじ数杯分の酢に含まれる酢酸のモル数、例示的な値)

baking_soda_g = np.linspace(0, 20, 200)
baking_soda_mol = baking_soda_g / M_NaHCO3

# 酢(酢酸)が律速になる量を超えたら、それ以上CO2は増えない
co2_mol = np.minimum(baking_soda_mol, vinegar_moles_available)
co2_volume_L = co2_mol * R * T / P

limiting_g = vinegar_moles_available * M_NaHCO3

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(baking_soda_g, co2_volume_L, color="#1e3a8a", linewidth=2.5)
ax.axvline(limiting_g, color="#dc2626", linestyle="--", linewidth=1.5,
           label=f"Vinegar becomes limiting (~{limiting_g:.1f}g baking soda)")

ax.set_xlabel("Baking soda used (g)")
ax.set_ylabel("CO2 gas produced (L)")
ax.set_title("CO2 volume grows linearly, then plateaus once vinegar runs out")
ax.legend(loc="lower right", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/vinegar_baking_soda_co2.png")
plt.close(fig)

print("done, limiting_g=", limiting_g)
