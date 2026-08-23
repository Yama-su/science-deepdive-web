"""
記事「雷はなぜ光ってから音が遅れて聞こえるの？」用のシミュレーション画像を生成する。
光速と音速の違いによる、雷までの距離と遅延時間の関係を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

SPEED_OF_SOUND = 343.0  # m/s (at ~20C)

distance_km = np.linspace(0, 10, 200)
delay_seconds = (distance_km * 1000) / SPEED_OF_SOUND

fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
ax.plot(distance_km, delay_seconds, color="#1e3a8a", linewidth=2)

# 3km地点の例を強調
example_km = 3.0
example_delay = (example_km * 1000) / SPEED_OF_SOUND
ax.scatter([example_km], [example_delay], color="#d97706", zorder=5)
ax.annotate(
    f"{example_km}km -> {example_delay:.1f}s delay",
    xy=(example_km, example_delay),
    xytext=(example_km + 1.5, example_delay - 3),
    arrowprops=dict(arrowstyle="->", color="#d97706"),
)

ax.set_xlabel("Distance to lightning (km)")
ax.set_ylabel("Delay between flash and thunder (seconds)")
ax.set_title("Light arrives instantly, sound takes ~1s per 343m")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/thunder_delay.png")
plt.close(fig)

print("done")
