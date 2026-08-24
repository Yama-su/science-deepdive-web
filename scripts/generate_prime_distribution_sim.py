"""
記事「なぜ素数は不規則に現れるのか？」用のシミュレーション画像を生成する。
素数計数関数pi(x)と、素数定理の予測x/ln(x)を比較する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

N = 100000

# エラトステネスの篩
sieve = np.ones(N + 1, dtype=bool)
sieve[0:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i * i :: i] = False

primes_cumcount = np.cumsum(sieve)

x_vals = np.arange(2, N + 1, 50)
pi_x = primes_cumcount[x_vals]
pnt_prediction = x_vals / np.log(x_vals)

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=150)
ax.plot(x_vals, pi_x, color="#1e3a8a", linewidth=2, label="pi(x): actual prime count")
ax.plot(x_vals, pnt_prediction, color="#d97706", linewidth=2, linestyle="--",
        label="x / ln(x): Prime Number Theorem prediction")

ax.set_xlabel("x")
ax.set_ylabel("Number of primes up to x")
ax.set_title("Individually irregular, but pi(x) follows x/ln(x) on average")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/prime_counting_function.png")
plt.close(fig)

print("done, pi(100000)=", int(primes_cumcount[N]))
