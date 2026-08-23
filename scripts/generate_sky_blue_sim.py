"""
記事「なぜ空は青いの？」用のシミュレーション画像を生成する。
レイリー散乱の強度は波長の-4乗に比例することを可視化する。
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = "public/assets/simulations"

wavelength_nm = np.linspace(380, 750, 400)  # visible light range
scattering_intensity = 1 / (wavelength_nm ** 4)
scattering_intensity /= scattering_intensity.max()


def wavelength_to_rgb(wl):
    if wl < 440:
        r, g, b = -(wl - 440) / (440 - 380), 0.0, 1.0
    elif wl < 490:
        r, g, b = 0.0, (wl - 440) / (490 - 440), 1.0
    elif wl < 510:
        r, g, b = 0.0, 1.0, -(wl - 510) / (510 - 490)
    elif wl < 580:
        r, g, b = (wl - 510) / (580 - 510), 1.0, 0.0
    elif wl < 645:
        r, g, b = 1.0, -(wl - 645) / (645 - 580), 0.0
    else:
        r, g, b = 1.0, 0.0, 0.0
    return (max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b)))


colors = [wavelength_to_rgb(wl) for wl in wavelength_nm]

fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
ax.scatter(wavelength_nm, scattering_intensity, c=colors, s=8)
ax.plot(wavelength_nm, scattering_intensity, color="#94a3b8", linewidth=0.8, zorder=0)

ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Relative Rayleigh scattering intensity (normalized)")
ax.set_title("Rayleigh scattering intensity ~ 1 / wavelength^4")
ax.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(f"{OUT_DIR}/sky_blue_rayleigh.png")
plt.close(fig)

print("done")
