"""
記事「星はなぜ夜しか見えないの？」用のシミュレーション画像を生成する。
太陽光・昼間の空・薄明・満月・星明かりの照度(lux)を対数スケールで比較する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

sources = [
    ("Direct sunlight", 100000),
    ("Daylight sky\n(scattered sunlight)", 10000),
    ("Twilight", 10),
    ("Full moon", 0.25),
    ("All starlight\ncombined", 0.001),
]

names = [s[0] for s in sources]
values = [s[1] for s in sources]

fig, ax = plt.subplots(figsize=(8, 5.5), dpi=150)
bars = ax.barh(names, values, color="#1e3a8a")
ax.set_xscale("log")

for bar, v in zip(bars, values):
    ax.text(v * 1.5, bar.get_y() + bar.get_height() / 2, f"{v:g} lux", va="center", fontsize=8)

ax.set_xlabel("Illuminance (lux, log scale)")
ax.set_title("Daylight is about 10 million times brighter than all starlight combined")
ax.invert_yaxis()
ax.grid(alpha=0.3, axis="x", which="both")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/star_visibility_brightness.png")
plt.close(fig)

print("done")
