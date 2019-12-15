#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Auswertung Mathematisches Pendel - Tom Barnowsky - 29.11.19

    Wertet Messdaten der Periodendauer eines Pendels statistisch aus.'''

import matplotlib.pyplot as plt
import numpy as np

# - Einlesen der Daten -
print("Bitte Pfad zur asuzuwertenden Datei eingeben oder leer bestätigen,\n\
um 'Pendel-Messung.dat' aus dem aktuellen Verzeichnis zu verwenden.") 
filename = input(">") # Nutzereingabe

if filename ==  '' :    # Eingabe leer
    filename = 'Pendel-Messung.dat' # nehme 'Pendel-Messung.dat'

print("Lese daten..\n") # Statusausgabe in Terminal

try:

    dat = np.loadtxt(filename)  # Lese Daten aus Datei
    float(dat[0])               # dat (Numpy Array) unterstütz nur durchgehend einen Datentyp
                                # lässt sich das erste Element ohne Fehler in float
                                # umwandeln ist das gesamte Array Int oder Float womit das
                                # Prgramm umgehen kann

except: # wenn irgendwas einen Fehler brint -> Problem mit Datei -> Abbruch

    print("Datei nicht vorhanden oder nicht nur mit Zahlen gefüllt.\n\
Beende.")   # Statusausgabe in Terminal
    quit()  # Beende

N = len(dat)                            # Bestimme Anzahl Messungen
n = np.arange(0, N, 1)                  # Erstelle Nummerierung Werte (X-Achse)

# - Bestimmung statistischer Größen -
mean = dat.mean()           # Mittelwert
var = dat.var(ddof = 1)     # Varianz
std = dat.std(ddof = 1)     # Standardabweichung
stdm = std/np.sqrt(N)       # Standardabweichung des Mittelwerts

# - Ausgabe Werte und Status in Terminal -
print("\
Mittelwert                          {0:.10f}s\n\
Varianz                             {1:.10f}s\n\
Standardabweichung                  {2:.10f}s\n\
Standardabweichung des Mittelwerts  {3:.10f}s\n\n\
Bereite grafische Ausgabe vor..".format(mean, var, std, stdm))

# - Vorbereitung Histogram - 
hist, bins= np.histogram(dat, bins = int(np.sqrt(N)))   # Sortiere Messwerte in Intervalle
center = (bins[:-1] + bins[1:])/2                       # Bestimme Intervallmitten


# -------- Matplotlib Ausgabe ---------

# ---- Figure ----
fig, sub = plt.subplots(3)                              # Erstelle Fenster mit 3 Subplots
fig.suptitle("Datenauswertung Pendel                 ", fontsize = 22)
    # Erstelle Überschrift, Mit vielen Leerzeichen damit die Legende Platz hat
fig.set_size_inches(7, 8)                               # Setze Fenstergröße
fig.canvas.set_window_title("Datenauswertung Pendel")   # Setze Fenstertitel

# ---- Plot 1 - 10% der Messwerte ----
sub[0].errorbar(n[::10],dat[::10], yerr = std , capsize = 2, color = "orange",\
        marker = 'x', markeredgecolor = "b", linestyle = "none")
        # Jeder 10. Messwert als Punkt mit Standardabweichung als Unsicherheit
sub[0].set_title("10% der Messwerte")                   # Titel für Graph
sub[0].set_xlabel("Messung")                            # Bezeichnung x-Achse
sub[0].set_ylabel("Messwert /s")                        # Bezeichnung y-Achse

# ---- Plot 2  - absolute Häufigkeit ----
sub[1].errorbar(center, hist, yerr = np.sqrt(hist) , capsize = 2, color="orange",\
        marker = 'x', markeredgecolor = "g", linestyle = "none")
        # Anzahl der Werte in Intervall mit Abweichung = Wurzel der Anzahl
sub[1].set_title("absolute Häufigkeitsverteilung")      # Titel für Graph
sub[1].set_xlabel("Messwert /s")                        # Bezeichnung x-Achse
sub[1].set_ylabel("Häufigkeit")                         # Bezeichnung y-Achse

# ---- Plot 3 - relative Häufigkeit ----
sub[2].errorbar(center, hist/N, yerr = np.sqrt(hist)/N , capsize = 2, color = "orange",\
        marker = 'x', markeredgecolor = 'r', linestyle = "none")
        # Wie Plot 2 nur relativ, also durch die Gesamtzahl Messungen geteilt
sub[2].set_title("relative Häufigkeitsverteilung")      # Titel für Graph
sub[2].set_xlabel("Messwert /s")                        # Bezeichnung x-Achse
sub[2].set_ylabel("Häufigkeit")                         # Bezeichnung y-Achse

# ---- Standardabweichung, Mittelwert ----
# Zeichnet Linien zwichen zwei Punkten (0 und dem größten Wert der Achse)
# an den x bzw y Stellen wo Mittelwert usw liegt.
# nur bei den Linien im ersten Plot wurde 'label' gesetzt da die Farben
# zu den anderen Plots identisch sind und die Legende übersichtlich bleiben soll
sub[0].plot([0, N], [mean]*2 , color = 'm', label = "Mittelwert")               # Mittelwert
sub[0].plot([0, N], [mean+std]*2 , color = 'c', label = "+ Standardabweichung") # Mittelwert + Standardabweichung
sub[0].plot([0, N], [mean-std]*2 , color = 'y', label = "- Standardabweichung") # Mittelwert - Standardabweichung
sub[1].plot([mean]*2, [0, np.amax(hist)+10], color = 'm')
sub[1].plot([mean+std]*2, [0, np.amax(hist)+10], color = 'c')
sub[1].plot([mean-std]*2, [0, np.amax(hist)+10], color = 'y')
sub[2].plot([mean]*2, [0, np.amax(hist/N)+0.025], color = 'm')
sub[2].plot([mean+std]*2, [0, np.amax(hist/N)+0.025], color = 'c')
sub[2].plot([mean-std]*2, [0, np.amax(hist/N)+0.025], color = 'y')

fig.legend()                                            # Aktiviere Legende für Mittelwert usw.
fig.subplots_adjust(hspace = 0.5)                       # Abstand der Graphen zueiander
print("Fertig.")                                        # Statusausgabe in Terminal
plt.show()                                              # ZEIGE FENSTER
