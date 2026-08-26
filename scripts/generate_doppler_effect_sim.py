"""
記事「救急車のサイレンはなぜ近づくと高く聞こえるの？」用の
シミュレーション画像を生成する。
音源の速さに対する観測される周波数の変化(ドップラー効果)を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

v_sound = 343.0  # m/s
f_source = 800.0  # Hz(サイレンの元の周波数、例示的な値)

vs = np.linspace(0, 320, 300)  # 音源の速さ(接近時)

f_approaching = f_source * v_sound / (v_sound - vs)
f_receding = f_source * v_sound / (v_sound + vs)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(vs * 3.6, f_approaching, color="#dc2626", linewidth=2, label="Approaching (pitch rises)")
ax.plot(vs * 3.6, f_receding, color="#1e3a8a", linewidth=2, label="Receding (pitch falls)")
ax.axhline(f_source, color="#94a3b8", linestyle=":", linewidth=1.5, label=f"Source frequency ({f_source:.0f}Hz)")

ax.set_xlabel("Source speed (km/h)")
ax.set_ylabel("Observed frequency (Hz)")
ax.set_title("Doppler effect: pitch shifts as the source moves toward or away")
ax.set_ylim(400, 1600)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/doppler_effect_frequency.png")
plt.close(fig)

print("done")
