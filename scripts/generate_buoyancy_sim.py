"""
記事「なぜ水に浮くものと沈むものがあるの？」用のシミュレーション画像を生成する。
様々な材質の密度を水の密度(1000 kg/m^3)と比較し、浮く/沈むを可視化する。
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

materials = [
    ("Cork", 240),
    ("Ice", 917),
    ("Oak wood", 700),
    ("Aluminum", 2700),
    ("Steel", 7850),
    ("Lead", 11340),
]

water_density = 1000

names = [m[0] for m in materials]
densities = [m[1] for m in materials]
colors = ["#1e3a8a" if d < water_density else "#dc2626" for d in densities]

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
bars = ax.barh(names, densities, color=colors)
ax.axvline(water_density, color="#166534", linestyle="--", linewidth=2, label="Water (1000 kg/m^3)")

for bar, d in zip(bars, densities):
    ax.text(d + 150, bar.get_y() + bar.get_height() / 2, f"{d}", va="center", fontsize=8)

ax.set_xlabel("Density (kg/m^3)")
ax.set_title("Floats (blue) if density < water, sinks (red) if density > water")
ax.legend(loc="lower right", fontsize=8)
ax.invert_yaxis()
ax.grid(alpha=0.3, axis="x")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/buoyancy_density_comparison.png")
plt.close(fig)

print("done")
