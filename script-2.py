import sys

sys.path.append("include/")
import numpy as np
import matplotlib.pyplot as plt
import clipboard_and_style_sheet as cr
import td_phase_correct as td
from tqdm import tqdm
import os
import scipy.constants as sc

cr.style_sheet()

# ______________ load and phase correct _______________________________________
# # path = r"D:\230105_1G113 DATA/"
# path = r"/Volumes/Extreme SSD/Research_Projects/1G113_Kristina_Chang" \
#        r"/230105_1G113 DATA/"
# N = 20  # number of files
# names = [str(i + 1) + '_pc.npy' for i in range(N)]
# names = [path + i for i in names]
#
# ppifg = int(2e7)
# center = ppifg // 2
# data = np.zeros((len(names), ppifg))
# for n, i in enumerate(tqdm(names)):
#     data[n] = np.load(i)
#
# opt = td.Optimize(data[:, center - 118:center + 160])
# opt.phase_correct(data)
# avg = np.mean(data, 0)
# np.save("data/avg.npy", avg)

# ______________ frequency axis _______________________________________________
ppifg = int(2e7)
center = ppifg // 2
freq_f = np.fft.rfftfreq(ppifg, d=1 / 100e6) * ppifg * 1e-12
freq_a = np.fft.rfftfreq(ppifg // 100, d=1 / 100e6) * ppifg * 1e-12

avg = np.load("data/avg.npy")
ft_f = np.fft.rfft(avg)
ft_a = np.fft.rfft(avg[center - ppifg // 100 // 2: center + ppifg // 100 // 2])
wl_f = sc.c * 1e9 / (freq_f * 1e12)
wl_a = sc.c * 1e9 / (freq_a * 1e12)

# ______________ plotting _____________________________________________________
plt.plot(freq_f, abs(ft_f) / abs(ft_a)[100:].max(), label="100 MHz resolution")
plt.plot(freq_a, abs(ft_a) / abs(ft_a)[100:].max(), label="10 GHz resolution")
plt.ylim(-.02, 1.1)
plt.xlim(756, 800)
plt.legend(loc='best')

plt.figure()
plt.plot(wl_f, abs(ft_f) / abs(ft_a)[100:].max(), label="100 MHz resolution")
plt.plot(wl_a, abs(ft_a) / abs(ft_a)[100:].max(), label="10 GHz resolution")
plt.ylim(-.02, 1.1)
plt.xlim(sc.c * 1e9 / 800e12, sc.c * 1e9 / 756e12)
plt.legend(loc='best')
