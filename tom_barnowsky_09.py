#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Poisson-Statistik

    ?????????????? '''

import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt

dat = np.loadtxt("PV.dat")
#print(np.sqrt(len(dat)))
mean = np.mean(dat)

# AUS SCIPY DOCS
x = np.arange(poisson.ppf(0.01, mean), poisson.ppf(0.99, mean))
plt.plot(x, poisson.pmf(x , mean))

# Histogram ÜBER DATEN
hist, bins = np.histogram(dat, bins = int(np.sqrt(len(dat))))
center = (bins[:-1] + bins[1:])/2
plt.errorbar(center, hist/len(dat), yerr = np.sqrt(hist)/len(dat))

# Eintragen Mittelwert
plt.plot([mean, mean], [0,np.amax(hist)/1000+0.01])

# Zeigen
plt.show()
