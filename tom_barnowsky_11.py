#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Kugeltank 2 - Tom Barnowsky - 15.01.2020

    Kugeltank wird numerisch abgeleitet und dargestellt. '''

import numpy as np
from matplotlib import pyplot as plt
import ableitung as abl

t, h = np.loadtxt('Kugeltank.dat', unpack = True, skiprows = 1)
t /= 60
h *= 100

m = abl.diff(t, h)

grad = np.gradient(h, t[1])

# -------- Matplotlib Ausgabe --------

# ---- Figure ----
sub = [None, None]
fig, sub[0] = plt.subplots(1)
fig.suptitle("Differenzierung Kugeltank")
fig.set_size_inches(8, 6)
fig.canvas.set_window_title("Differenzierung Kugeltank")

# ---- Plot 1 - Messwerte ----
sub[0].plot(t, h, color = 'b', label = "Messwerte")
sub[0].set_ylabel("Füllstand Tank /cm")
sub[0].set_xlabel("Zeit /min")

# ---- Plot 2 - Ansteig ----
sub[1] = sub[0].twinx()
sub[1].plot(t, m, color = 'r', label = "Anstieg")
sub[1].plot(t, grad)
sub[1].set_ylabel("Anstieg /(cm/min)")

fig.legend()
fig.tight_layout(rect = (0, 0, 1, 0.9))
plt.show()
