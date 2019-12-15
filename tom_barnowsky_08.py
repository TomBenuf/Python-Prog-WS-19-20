#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Lineare Anpassung - Tom Barnowsky - 11.12.19

    Passt einen Satz Messwerte (aus Datei Pa234.dat) des Zerfalls von Pa234 linear an
    und berechnet Halbwertszeit und weitere größen.
    
    enthält lin_reg() Funktion zur linearen Anpassung von Datensätzen.'''

import numpy as np

def lin_reg(x, y, dy) :

    ''' Lineare Anpassung

        passt Datensatz Linear an
        
        Eingaben:
        x = x-Wert Array
        y = y-Wert Array
        dy = y Unsicherheiten Array (ohne 0 Einträge)

        Rückgaben:
        [m, dm, n, dn, cov, corr]
        m = Anstieg als 'float'
        dm = Unsicherheit Ansteig als 'float'
        n = Achsenabschnitt als 'float'
        dn = Unsicherhiet Achsenabschnitt als 'float'
        cov = 2x2 Kovarianzmatrix als 'numpy.matrix'
        corr = Korrelationskoeffizient als 'float'
    '''

    # Funktion nimmt nur Arrays als Eingaben
    if not isinstance(x, np.ndarray) :      # x Werte kein Array
        raise TypeError                     # -> Fehlermeldung, Ende
    if not isinstance(y, np.ndarray) :      # y Werte kein Array
        raise TypeError                     # -> Fehlermeldung, Ende
    if not isinstance(dy, np.ndarray) :     # y Unsicherheiten kein Array
        raise TypeError                     # -> Fehlermeldung, Ende

    # Funktion braucht eindimensionale Eingaben
    if x.ndim != 1 :                        # Dimension x Array nicht 1
        raise ValueError                    # -> Fehlermeldung, Ende
    if y.ndim != 1 :                        # Dimension y Array nicht 1
        raise ValueError                    # -> Fehlermeldung, Ende
    if dy.ndim != 1 :                       # Dimension y Unsicherheiten nicht 1
        raise ValueError                    # -> Fehlermedlung, Ende

    # Berechnung
    a = sum(x**2 / dy**2)
    b = sum(x / dy**2)
    c = sum(1 / dy**2)
    d = sum((x*y) / dy**2)
    e = sum(y / dy**2)
    D = a*c - b**2

    # Rückgaben
    cov = 1/D * np.matrix([[a, -b],[-b, c]])    # Kovarianzmatrix
    corr = -b / np.sqrt(a*c)                    # Korrelationskoeffizient
    m = (d*c - b*e) / D                         # Anstieg
    dm = np.sqrt(c / D)                         # Unsicherheit Anstieg
    n = (a*e - b*d) / D                         # Achsenabschnitt
    dn = np.sqrt(a / D)                         # Unsicherheit Achsenabschnitt
    ls = sum((y - n - m*x)**2 / dy**2)          # Kleinstes Quadrat

    return  m, dm, n, dn, ls,  corr, cov              # Rückgabe


if __name__ == '__main__' :

    from matplotlib import pyplot as plt            # Import Matplotlib jetzt erst da für Funktion nicht notwendig

    dat = np.loadtxt('Pa234.dat', skiprows = 1)     # Lade Datei
    t = dat[:,0]                                    # Spalte 1 = Messzeitpunkte
    N = dat[:,1]                                    # Spalte 2 = Messwerte
    N_err = np.sqrt(N)                              # Unsicherheiten aller Messwerte
    N_log = np.log(N)                               # logarithmierung aller Messwerte

    m, dm, n, dn, ls, corr, cov = lin_reg(t, N_log, 1/N_err)        # Linearisierung logarithmierte Messwerte
    mgraph = m*6                                                    # Anstieg Graph (Messungen alle 6 Sekunden)
    lin = np.linspace(n, n+mgraph*len(t), num = len(t))             # Werte mit Anfangswert n mit Anstieg m

    # -------- Terminal Ausgabe --------
    print("---- Auswertung Zerfall Pa234 ----\n\n\
Standardabweichung der Impuslanzahlen:  {0:14.10f}\n\n\
Für logaritmierte Werte:\n\
Achsenabschnitt:                        {1:14.10f}\n\
dessen Standardabweichung:              {2:14.10f}\n\
Anstieg:                                {3:14.10f}\n\
dessen Standardabweichung:              {4:14.10f}\n\
mininamles x²:                          {5:14.10f}\n\
Anzahl Freiheitsgrade:                  {6:14d}\n\
Korellationskoeffizient:                {7:14.10f}\n\
Halbwertszeit:                          {8:13.9f}s\n"\
.format(np.std(N), n, dn, m, dm, ls, len(t)-1, corr, -1/m*np.log(2)))
                                                    # Halbwertszeit = -ln(1/2)/Anstieg
                                                    # Freiheitsgrade Anzahl Stichproben -1 


    # -------- Matplotlib Ausgabe --------

    # ---- Figure ----
    fig, sub = plt.subplots(2)                                      # Fenster mit zwei Subplots
    fig.suptitle("Zerfall Pa234         ", fontsize = 22)           # Überschrift mit Platz für Legende
    fig.set_size_inches(7, 6)                                       # Fenstergröße
    fig.canvas.set_window_title("Zerfall Pa234")                    # Fenstertitel
    fig.text(0.05,0.48,"N = Impulsanzahl, t = Zeit")                # Erklärung Variablen

    # ---- Plot 1 - Logartithmierung ----
    sub[0].errorbar(t, N_log, yerr = 1/N_err, linestyle = 'None', marker = '.')
                          # Plot logarithmierte Messergebnisse mit Unsicherheiten
    sub[0].plot(t, lin)   # Plot Linearisierung der logarithmierten Ergebnisse
    sub[0].set_xlabel("t /s")                       # Label x-Achse
    sub[0].set_ylabel("ln(N)")                      # Label y-Achse

    # ---- Plot 2 - Messwerte ----
    sub[1].errorbar(t, N, yerr = N_err, marker = '.', linestyle = 'None')   # Plot Messergebnisse mit Unsicherheiten
    sub[1].plot(t, np.e**lin)               # Plot Linearisierung der Ergebnisse (e hoch lin)
    sub[1].set_xlabel("t /s")               # Label x-Achse
    sub[1].set_ylabel("N")                  # Label y-Achse

    fig.legend(["Linearisierung", "Messwerte mit Unsicherheiten"])   # Legende
    fig.subplots_adjust(hspace = 0.4)                               # Abstand der Plots zueinander
    print("Fertig.")                                                # Statusausgabe in Terminal
    plt.show()                                                      # ZEIGE FENSTER
