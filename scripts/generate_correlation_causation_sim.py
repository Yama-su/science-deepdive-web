"""
記事「相関関係はなぜ因果関係を意味しないのか？」用のシミュレーション画像を生成する。
共通の交絡変数(気温)だけを通じて、直接の因果関係が一切ない
2つの変数(アイスクリーム販売数と水難事故数)の間に、
見かけ上の強い相関が生まれる様子を可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

rng = np.random.default_rng(11)
n = 200

# 交絡変数: 気温(唯一の共通原因)
temperature = rng.uniform(0, 35, n)

# アイスクリーム販売数と水難事故数は、どちらも気温だけに依存し、
# 互いへの直接的な因果関係は一切コードされていない
ice_cream_sales = 20 * temperature + rng.normal(0, 100, n)
drowning_incidents = 0.8 * temperature + rng.normal(0, 4, n)

correlation = np.corrcoef(ice_cream_sales, drowning_incidents)[0, 1]

fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=150)
sc = ax.scatter(ice_cream_sales, drowning_incidents, c=temperature, cmap="coolwarm", s=25, alpha=0.8)
cbar = fig.colorbar(sc, ax=ax)
cbar.set_label("Temperature (the hidden confounder)")

ax.set_xlabel("Ice cream sales")
ax.set_ylabel("Drowning incidents")
ax.set_title(f"r = {correlation:.2f}, yet ice cream sales do NOT cause drownings\n(both are driven only by temperature)")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/correlation_confounder_demo.png")
plt.close(fig)

print("done, correlation =", correlation)
