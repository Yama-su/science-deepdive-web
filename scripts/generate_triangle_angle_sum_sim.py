"""
記事「なぜ三角形の内角の和は180度になるの？」用のシミュレーション画像を生成する。
ランダムな200個の三角形について、内角の和が常に180度になることを数値的に検証する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(1)
n_triangles = 200

angle_sums = []
for _ in range(n_triangles):
    pts = rng.uniform(-10, 10, size=(3, 2))
    total = 0
    for i in range(3):
        p_prev = pts[(i - 1) % 3]
        p_cur = pts[i]
        p_next = pts[(i + 1) % 3]
        v1 = p_prev - p_cur
        v2 = p_next - p_cur
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1, 1)
        angle = np.degrees(np.arccos(cos_angle))
        total += angle
    angle_sums.append(total)

angle_sums = np.array(angle_sums)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.hist(angle_sums, bins=30, color="#1e3a8a", edgecolor="white")
ax.axvline(180, color="#dc2626", linestyle="--", linewidth=2, label="180 degrees")

ax.set_xlabel("Sum of interior angles (degrees)")
ax.set_ylabel("Number of triangles")
ax.set_title(f"{n_triangles} random triangles: angle sum is always 180 degrees")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/triangle_angle_sum_check.png")
plt.close(fig)

print("done, min/max:", angle_sums.min(), angle_sums.max())
