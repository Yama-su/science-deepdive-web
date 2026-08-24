"""
記事「電池の中にはどうやって電気が詰まっているの？」用のシミュレーション画像を生成する。
ネルンストの式に基づき、放電が進む(反応物の濃度比Qが変化する)につれて
電池の電圧が徐々に低下していく様子を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

E0 = 1.5   # 標準電池電圧(例示的な値、単三電池を想定)
n = 2      # 電子数(例示的な値)
F = 96485  # C/mol
R = 8.314  # J/(mol*K)
T = 298    # K

# 放電の進み具合(0=未使用, 1=完全放電)に応じてQが指数的に増加すると仮定
progress = np.linspace(0.001, 0.999, 300)
Q = progress / (1 - progress)  # 反応が進むほどQ(生成物/反応物)が大きくなる

E = E0 - (R * T) / (n * F) * np.log(Q)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(progress * 100, E, color="#1e3a8a", linewidth=2.5)
ax.axhline(E0, color="#94a3b8", linestyle=":", linewidth=1.5, label=f"Standard voltage E0={E0}V")

ax.set_xlabel("Discharge progress (%)")
ax.set_ylabel("Cell voltage (V)")
ax.set_title("Nernst equation: voltage drops as the battery discharges")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/battery_nernst_voltage.png")
plt.close(fig)

print("done")
