"""
記事「花火の色はどうしてあんなに色々な色が出せるの？」用のシミュレーション画像を生成する。
金属元素ごとの炎色反応の発光波長を可視化する。
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

# 代表的な金属元素の炎色反応(主な発光波長, nm)とおおよその色
elements = [
    ("Li (Lithium)", 670, "#ff3b3b"),
    ("Sr (Strontium)", 606, "#ff5e1a"),
    ("Ca (Calcium)", 622, "#ff8c1a"),
    ("Na (Sodium)", 589, "#ffd400"),
    ("Ba (Barium)", 524, "#3ddc84"),
    ("Cu (Copper)", 505, "#1ac6c6"),
    ("K (Potassium)", 404, "#8a2be2"),
]

names = [e[0] for e in elements]
wavelengths = [e[1] for e in elements]
colors = [e[2] for e in elements]

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
bars = ax.barh(names, wavelengths, color=colors)

ax.set_xlabel("Characteristic emission wavelength (nm)")
ax.set_title("Flame test colors: each metal emits its own characteristic wavelength")
ax.invert_yaxis()
ax.grid(alpha=0.3, axis="x")

for bar, wl in zip(bars, wavelengths):
    ax.text(wl + 5, bar.get_y() + bar.get_height() / 2, f"{wl}nm", va="center", fontsize=8)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/firework_flame_colors.png")
plt.close(fig)

print("done")
