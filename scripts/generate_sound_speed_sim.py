"""
記事「音はどうやって耳に届くの？」用のシミュレーション画像を生成する。
v = sqrt(B/rho) を使い、様々な媒質での音速を比較する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

# (媒質名, 体積弾性率B[Pa], 密度rho[kg/m^3])
# 流体(気体・液体)は体積弾性率だけで音速が正確に決まる。
# 固体はさらに剛性率(せん断への強さ)も音速に寄与するため、
# 単純な体積弾性率だけでは音速を過小評価してしまう(ここでは扱わない)。
media = [
    ("Air", 1.42e5, 1.225),
    ("Water", 2.2e9, 1000),
]

names = [m[0] for m in media]
predicted_v = [np.sqrt(m[1] / m[2]) for m in media]
actual_v = [343, 1480]  # 実測値(近似)

x = np.arange(len(names))
width = 0.35

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.bar(x - width / 2, predicted_v, width, color="#1e3a8a", label="Predicted: sqrt(B/rho)")
ax.bar(x + width / 2, actual_v, width, color="#d97706", label="Actual measured speed")

ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_ylabel("Speed of sound (m/s)")
ax.set_yscale("log")
ax.set_title("v = sqrt(B/rho) correctly predicts sound speed across media")
ax.legend(fontsize=8)
ax.grid(alpha=0.3, axis="y", which="both")

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/sound_speed_media.png")
plt.close(fig)

print("done", predicted_v)
