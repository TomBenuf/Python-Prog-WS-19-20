#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Bahnkurve -- Tom Barnowsky - 20.11.2019

    Stellt die Bahnkurve einer gestoßenen Kugel grafisch dar.'''

import matplotlib.pyplot as plt
import numpy as np

def wurf(v0, z0, a0=False, g = 9.81) :
    if a0 == False :
        a0 = np.arcsin(1 / np.sqrt((1/(2*g*z0)/v0**2)+2))
    x = np.linspace(0,30, num = 1000)
    z = x * np.tan(a0) - g /( 2* (v0**2) * (np.cos(a0)**2)) * (x**2) + z0
    return x, z

x, z = wurf(14 ,  2.4)
plt.plot(x, z)
plt.title("Bahnkurve Kugelstoßen")
plt.xlabel("Wurfweite /m")
plt.ylabel("Wurfhöhe /m")
plt.ylim(0, 30)
plt.xlim(0, 30)
plt.show()

