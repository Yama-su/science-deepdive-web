"""
記事「電気はなぜコンセントから来るの？」用のシミュレーション画像を生成する。
回転するコイルの磁束変化から生じる交流電圧の正弦波を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

B = 1.0       # 磁束密度(例示的な値)
A_area = 1.0  # コイルの面積(例示的な値)
f = 60        # Hz(発電機の回転数、日本の東側の周波数)
omega = 2 * np.pi * f

t = np.linspace(0, 3 / f, 500)  # 3周期分
flux = B * A_area * np.cos(omega * t)
emf = B * A_area * omega * np.sin(omega * t)

fig, axes = plt.subplots(2, 1, figsize=(8, 6.5), dpi=150, sharex=True)

axes[0].plot(t * 1000, flux, color="#1e3a8a", linewidth=2)
axes[0].set_ylabel("Magnetic flux Phi(t)")
axes[0].set_title("Rotating coil: flux oscillates as B*A*cos(wt)")
axes[0].grid(alpha=0.3)

axes[1].plot(t * 1000, emf, color="#d97706", linewidth=2)
axes[1].set_xlabel("Time (ms)")
axes[1].set_ylabel("Induced EMF (voltage)")
axes[1].set_title("Faraday's law: EMF = -dPhi/dt gives the sinusoidal AC waveform")
axes[1].grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/ac_induction_waveform.png")
plt.close(fig)

print("done")
