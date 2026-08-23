"""
記事「炭酸飲料からはなぜシュワシュワ泡が出るの？」用のシミュレーション画像を生成する。
ヘンリーの法則(溶解度は圧力に比例)を可視化し、
開栓による圧力低下で二酸化炭素が過剰になる様子を示す。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

kH = 1.2  # 見かけの溶解度係数(単位省略、相対値)
pressure = np.linspace(0, 5, 200)
solubility = kH * pressure

sealed_pressure = 3.5
opened_pressure = 1.0

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(pressure, solubility, color="#1e3a8a", linewidth=2, label="Max dissolved CO2 (Henry's law)")

sealed_sol = kH * sealed_pressure
opened_sol = kH * opened_pressure

ax.scatter([sealed_pressure], [sealed_sol], color="#166534", zorder=5, s=60)
ax.annotate("Sealed can\n(high pressure)", xy=(sealed_pressure, sealed_sol),
            xytext=(sealed_pressure - 1.3, sealed_sol + 1.0), fontsize=8, color="#166534")

ax.scatter([opened_pressure], [opened_sol], color="#d97706", zorder=5, s=60)
ax.annotate("Opened can\n(atmospheric pressure)", xy=(opened_pressure, opened_sol),
            xytext=(opened_pressure + 0.3, opened_sol - 1.2), fontsize=8, color="#d97706")

# 過剰なCO2(泡になって出ていく量)を矢印で示す
ax.annotate(
    "",
    xy=(opened_pressure, opened_sol),
    xytext=(opened_pressure, sealed_sol),
    arrowprops=dict(arrowstyle="->", color="#dc2626", linewidth=2),
)
ax.text(opened_pressure + 0.1, (opened_sol + sealed_sol) / 2, "Excess CO2\nescapes as bubbles",
        fontsize=8, color="#dc2626")

ax.set_xlabel("Pressure (relative units)")
ax.set_ylabel("Dissolved CO2 (relative units)")
ax.set_title("Henry's law: solubility is proportional to pressure")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/soda_fizz_henry.png")
plt.close(fig)

print("done")
