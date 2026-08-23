"""
記事「重いものと軽いものはどっちが速く落ちる？」用のシミュレーション画像を生成する。
真空中では質量によらず落下速度が同じであること、空気中では空気抵抗により
軽い(密度の低い)物体の方が遅くなることを可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

g = 9.8
t = np.linspace(0, 2, 200)

fig, axes = plt.subplots(1, 2, figsize=(11, 5), dpi=150)

# 左図: 真空中(空気抵抗なし) - 質量によらず同じ
v_vacuum = g * t
axes[0].plot(t, v_vacuum, color="#1e3a8a", linewidth=3, label="1kg object")
axes[0].plot(t, v_vacuum, color="#d97706", linewidth=1.5, linestyle="--", label="1000kg object")
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Falling speed (m/s)")
axes[0].set_title("In vacuum: mass does not matter")
axes[0].legend(fontsize=8)
axes[0].grid(alpha=0.3)

# 右図: 空気中(抵抗あり) - terminal velocityモデル
def velocity_with_drag(t, terminal_v):
    tau = terminal_v / g
    return terminal_v * (1 - np.exp(-t / tau))

v_hammer = velocity_with_drag(t, terminal_v=45)  # 密度が高く空気抵抗の影響が小さい
v_feather = velocity_with_drag(t, terminal_v=2)  # 軽くて空気抵抗の影響が大きい

axes[1].plot(t, v_hammer, color="#1e3a8a", linewidth=2, label="Hammer (dense)")
axes[1].plot(t, v_feather, color="#d97706", linewidth=2, label="Feather (light, large drag)")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Falling speed (m/s)")
axes[1].set_title("In air: drag makes light objects fall slower")
axes[1].legend(fontsize=8)
axes[1].grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/free_fall_comparison.png")
plt.close(fig)

print("done")
