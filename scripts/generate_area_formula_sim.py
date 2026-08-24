"""
記事「図形の面積の公式はなぜそう決まっているのか？」用のシミュレーション画像を生成する。
ランダムな三角形について、底辺x高さ/2の公式と座標を使った公式(シューレース公式)の
結果が常に一致することを数値的に検証する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(5)
n_triangles = 200

base_height_areas = []
shoelace_areas = []

for _ in range(n_triangles):
    pts = rng.uniform(-10, 10, size=(3, 2))
    A, B, C = pts

    # 底辺=AB、高さ=Cから直線ABまでの距離、として計算
    base_vec = B - A
    base_len = np.linalg.norm(base_vec)
    # 点Cから直線ABまでの距離(外積の絶対値/底辺の長さ)
    cross = base_vec[0] * (C[1] - A[1]) - base_vec[1] * (C[0] - A[0])
    height = abs(cross) / base_len
    base_height_area = 0.5 * base_len * height

    # シューレース公式(座標だけから計算する独立した方法)
    shoelace_area = 0.5 * abs(
        A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])
    )

    base_height_areas.append(base_height_area)
    shoelace_areas.append(shoelace_area)

base_height_areas = np.array(base_height_areas)
shoelace_areas = np.array(shoelace_areas)

fig, ax = plt.subplots(figsize=(6.5, 6.5), dpi=150)
ax.scatter(shoelace_areas, base_height_areas, color="#1e3a8a", s=18, alpha=0.7)

lims = [0, max(shoelace_areas.max(), base_height_areas.max()) * 1.05]
ax.plot(lims, lims, color="#dc2626", linestyle="--", linewidth=1.5, label="y = x (perfect match)")

ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_xlabel("Area via shoelace formula (coordinates)")
ax.set_ylabel("Area via base x height / 2")
ax.set_title(f"{n_triangles} random triangles: both formulas always agree")
ax.legend(loc="upper left", fontsize=8)
ax.set_aspect("equal")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/triangle_area_formula_check.png")
plt.close(fig)

max_diff = np.max(np.abs(base_height_areas - shoelace_areas))
print("done, max_diff =", max_diff)
