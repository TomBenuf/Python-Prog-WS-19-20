#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Übung 11 - Kugeltank 2 - Tom Barnowsky - 15.01.2020

    Messwerte Kugeltank werden numerisch abgeleitet und dargestellt. '''

import numpy as np
from matplotlib import pyplot as plt
import ableitung as abl # importiere eigene Ableitungs Funktion aus ableitung.py

t, h = np.loadtxt('Kugeltank.dat', unpack = True, skiprows = 1) # lade Daten
t /= 60     # Zeit in Minuten umrechnen
h *= 100    # Höhe in Meter umrechnen

m = abl.diff(t, h)  # Leite Daten numerisch ab

grad = np.gradient(h, t[1]) # Leite Daten numerisch ab mit Numpy Funktion

# -------- Matplotlib Ausgabe --------

# ---- Figure ----
sub = [None, None]
fig, sub[0] = plt.subplots(1)                               # Ein Subplot
fig.suptitle("Differenzierung Kugeltank")                   # Überschrift
fig.set_size_inches(8, 6)                                   # Fenstergröße
fig.canvas.set_window_title("Differenzierung Kugeltank")    # Fenstertitel

# ---- Plot 1 - Messwerte ----
sub[0].plot(t, h, color = 'b', label = "Messwerte")         # plotte Messwerte
sub[0].set_ylabel("Füllstand Tank /cm")                     # Y Bezeichnung
sub[0].set_xlabel("Zeit /min")                              # X Bezeichnung

# ---- Plot 2 - Ansteig ----
sub[1] = sub[0].twinx()                                     # zweite y Achse im Plot
# kein Unterschied zu erkennen
sub[1].plot(t, m, color = 'r', label = "Anstieg")           # plotte Ableitung
sub[1].plot(t, grad, color = 'r')                           # plotte Numpy Gradient
sub[1].set_ylabel("Anstieg /(cm/min)")                      # Y Bezeichnung

fig.legend()                                                # zeige Legende
fig.tight_layout(rect = (0, 0, 1, 0.9))                     # Fomatierung im Fenster
plt.show()                                                  # ZEIGE FENSTER
