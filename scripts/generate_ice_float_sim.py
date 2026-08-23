"""
記事「なぜ氷は水に浮くの？」用のシミュレーション画像を生成する。
水の密度が4°C付近で最大になる異常性(密度異常)を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

# Kell(1975)の実験式に基づく水の密度(近似)。0-100°Cの範囲で4°C付近に極大を持つ。
t = np.linspace(0, 100, 500)
density = (
    999.83952
    + 16.945176 * t
    - 7.9870401e-3 * t ** 2
    - 46.170461e-6 * t ** 3
    + 105.56302e-9 * t ** 4
    - 280.54253e-12 * t ** 5
) / (1 + 16.879850e-3 * t)

ice_density = 916.7  # kg/m^3, 0°Cの氷の密度(液体の水より軽い)

fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
ax.plot(t, density, color="#1e3a8a", linewidth=2, label="Liquid water density")
ax.axhline(ice_density, color="#d97706", linestyle="--", linewidth=1.5, label="Ice density (0°C)")

max_idx = np.argmax(density)
ax.scatter([t[max_idx]], [density[max_idx]], color="#dc2626", zorder=5)
ax.annotate(
    f"Max density at {t[max_idx]:.1f}°C",
    xy=(t[max_idx], density[max_idx]),
    xytext=(t[max_idx] + 15, density[max_idx] - 5),
    arrowprops=dict(arrowstyle="->", color="#dc2626"),
)

ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Density (kg/m^3)")
ax.set_title("Water is denser than ice, and densest around 4°C")
ax.legend(loc="lower left")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/ice_float_density.png")
plt.close(fig)

print("done")
