"""
記事「お風呂の水はなぜ冷めるの？」用のシミュレーション画像を生成する。
ニュートンの冷却法則による指数関数的な温度低下を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

T0 = 40.0   # 湯の初期温度
T_env = 20.0  # 室温
k = 0.05    # 冷却係数(1/分)

t = np.linspace(0, 90, 300)
T = T_env + (T0 - T_env) * np.exp(-k * t)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(t, T, color="#1e3a8a", linewidth=2.5)
ax.axhline(T_env, color="#94a3b8", linestyle=":", linewidth=1.5, label="Room temperature (20C)")

# 最初の10分と、後半の10分での温度低下量を比較
drop_early = T[np.searchsorted(t, 0)] - T[np.searchsorted(t, 10)]
drop_late = T[np.searchsorted(t, 60)] - T[np.searchsorted(t, 70)]

ax.annotate(f"First 10 min: -{drop_early:.1f}C", xy=(5, T[np.searchsorted(t, 5)]),
            xytext=(15, 37), fontsize=8, color="#dc2626",
            arrowprops=dict(arrowstyle="->", color="#dc2626"))
ax.annotate(f"Minutes 60-70: -{drop_late:.1f}C", xy=(65, T[np.searchsorted(t, 65)]),
            xytext=(45, 27), fontsize=8, color="#166534",
            arrowprops=dict(arrowstyle="->", color="#166534"))

ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Water temperature (C)")
ax.set_title("Newton's law of cooling: fast at first, then slows down")
ax.legend(loc="upper right", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/bath_cooling_curve.png")
plt.close(fig)

print("done")
