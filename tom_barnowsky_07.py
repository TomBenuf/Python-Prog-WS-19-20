#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Tankentleerung - Tom Barnowsky - 05.12.2019

    Zeitberechnung der Entleerung eines Tanks mit
    konstantem Volumenstrom. Anschließende grafische Ausgabe.'''

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial as poly

try:

    R = float(input("Bitte Radius des Tanks in Metern eingeben: "))             # Nutzereingabe Radius 
    I = float(input("Bitte Volumenstrom in Liter pro Sekunde eingeben: "))/1000 # Nutzereingabe Durchfluss/s

except :                                                                        # Eingabe keine Zahl?

    print("Bitte mit Punkt als Komma getrennte Zahlen eingeben!\nBeende.")      # Fehlermeldung
    quit()                                                                      # Abbruch

T_end = int(round((((4/3)*(R**3)*np.pi)/I), 0)) # berechne Endzeit und runde auf ganze Zahl
print("\nDer Tank ist nach {}s vollständig entleert.".format(T_end))    # Ausgabe T_end
t = np.arange(1, T_end, 1)                      # erstelle t Wert array von 1 bis zur Endzeit
    # nicht von 0? -> siehe tom_barnowsky_07_anmerk.txt

def h(t):                           # definiere Funktion 'h' die Nullstellen für ein t berechnet

    koef = (I*t - (4/3)*np.pi*(R**3), 0, np.pi*R, -np.pi/3)     # Koeffizienten für Polynom
    return poly(koef).roots()       # gib Nullstellen des Polynoms von 'koef' zurück

h = np.vectorize(h, otypes = [np.ndarray])
    # mache 'h' für array Argumente ausführbar
    # die Ausgaben von h werden bei der Ausführung für jedes t als Arrays in einem großen Array abgelegt

roots = np.concatenate(h(t))
    # führe h aus und liste alle Ergebnisse hintereinander in ein 1-Dim Array

# Nutzeringabe 'Nullstellen auflisten?'
zeigen = input("\nSämtliche Nullstellen des Polynoms zur Berechnung der Füllhöhe anzeigen? [ja/NEIN] : ")

if zeigen in ['ja', 'Ja', 'jA', 'JA', 'yes'] :  # ZEIGEN
    
    counter = 0                                 # Zählvariable erstllenn und gleich 0

    for root in roots :                         # für jede brechnete Nullstelle
        
        print(format(root, '.10f'), end = ' ')  # gib diese auf 10 Stellen an aber mach keine Neue Zeile auf
        counter += 1                            # Zähler um 1 erhöhen

        if counter == 3 :                       # Zähler = 3?
            
            print('\r')                         # Neue Zeile
            counter = 0                         # Zähler zurücksetzen

elif zeigen in ['Nein' , 'nein', 'NEIN', 'No', '', ' '] : pass # NICHT ZEIGEN -> mach nix

else :                                          # komische Eingabe

    print("Eingabe nicht erkannt.\nBeende.")    # Fehlermeldung
    quit()                                      # Abbruch

print("\nBereite grafische Ausgabe vor.")       # Statusausgabe
roots = roots[roots >= 0]                       # lösche alle negativen Nullstellen
roots = roots[roots <= 2*R]                     # lösche alle Nullstellen größer als 2R

# -------- Matplotlib Ausgabe --------

# ---- Figure ----
fig, plot = plt.subplots()                      # Erstelle Fenster mit Subplot
fig.suptitle("Entleerung Tank", fontsize = 22)  # Setzte Überschrift
fig.canvas.set_window_title("Entleerung Tank")  # Setze Fenstertitel

# ---- Plot ----
plot.plot(t, roots)                             # h(t) als Linie
plot.set_xlabel("Zeit /s")                      # Bezeichnung x-Achse
plot.set_ylabel("Füllstand /m")                 # Bezeichnung y-Achse

print("Fertig.")                                # Statusausgabe
plt.show()                                      # ZEIGE FENSTER
