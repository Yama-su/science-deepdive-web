"""
記事「飛行機はなぜ飛べるの？」用のシミュレーション画像を生成する。
運動量保存則に基づく揚力モデル L = rho * A * v^2 * sin(theta) を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rho = 1.225  # kg/m^3, 空気密度
A = 30.0     # m^2, 翼が影響を与える空気の断面積(例示的な値)
theta_fixed = np.radians(5)  # 迎え角5度
v_fixed = 70  # m/s

fig, axes = plt.subplots(1, 2, figsize=(11, 5), dpi=150)

# 左図: 速度とリフトの関係(2乗に比例)
v = np.linspace(20, 100, 200)
L_v = rho * A * v**2 * np.sin(theta_fixed)
axes[0].plot(v, L_v / 1000, color="#1e3a8a", linewidth=2)
axes[0].set_xlabel("Airspeed (m/s)")
axes[0].set_ylabel("Lift force (kN)")
axes[0].set_title("Lift grows with the SQUARE of speed")
axes[0].grid(alpha=0.3)

# 右図: 迎え角とリフトの関係(小角では比例)
theta_deg = np.linspace(0, 15, 200)
L_theta = rho * A * v_fixed**2 * np.sin(np.radians(theta_deg))
axes[1].plot(theta_deg, L_theta / 1000, color="#d97706", linewidth=2)
axes[1].set_xlabel("Angle of attack (degrees)")
axes[1].set_ylabel("Lift force (kN)")
axes[1].set_title("Lift grows with angle of attack (until stall)")
axes[1].grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/lift_force_relationships.png")
plt.close(fig)

print("done")
