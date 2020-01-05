#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Poisson-Statistik - Tom Barnowsky - 18.12.19

    Wertet Messwerte statistisch aus. '''

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

dat = np.loadtxt("PV.dat", dtype = int)
mean = np.mean(dat)
std = np.std(dat)

hist, bins = np.histogram(dat, bins = dat.ptp())

# -------- Terminal Ausgabe --------
print("Poisson Verteilung\n\n\
Mittelwert:         {0:14.10f}\n\
Standardabweichung: {1:14.10f}".format(mean, std))

# --------  Matplotlib Ausgabe ---------

# ---- Figure ----
fig, sub = plt.subplots(1)
fig.suptitle("Poisson Verteilung                     ")
fig.canvas.set_window_title("Poisson Verteilung")

# ---- Plot ----
sub.errorbar(bins[:-1], hist/len(dat), yerr = np.sqrt(hist)/len(dat),\
        linestyle = "None", marker = 'x', capsize = 2, label = "Messwerte mit Unsicherheiten")
sub.bar(bins, stats.poisson.pmf(bins, mean), color = 'r', label = "Poissonverteilung")
sub.plot(bins, stats.norm.pdf(bins, mean, std), color = 'g', label = "Normalverteilung")
sub.set_xlabel("Anzahl Zerfälle pro s")
sub.set_ylabel("Relative Häufigkeit der Messung")

fig.subplots_adjust(top=0.8)
fig.legend()

plt.show() # ZEIGE FENSTER
