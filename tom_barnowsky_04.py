#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Übung 04 -- Tom Barnowsky 13.11.2019

    Berechnet Wurzeln nach dem Heron Verfahren.'''

def heron(a, n):

    ''' Heron Wurzelberechnungs Funktion

        Berechnet Wurzeln nach dem Heron verfahren.
        a = zu berechnende Wurzel
        n = Durchläufe
        Akzeptiert nur postive Integer als Attribute.
            nicht Integer -> TypeError
            nicht positiv -> ValueError

        heron.counter Zählt Funktionsaufrufe falls diese Variable
                      vorher angelegt wurde.'''
    
    if not isinstance(a, int) or not isinstance(n, int):    #Fehlermeldung keine Integer
        raise TypeError("'heron(a, n)' only supports instances 'int'")

    elif n <= 0 or a <= 0 : #Fehlermedlung negative Eingabewerte
        raise ValueError("'heron(a ,n)' only supports positive inputs ")

    if n==1 :
        r = 0.5*(a+1)   #Heron Formel für n = 1 damit heron() nicht für negative n aufgerufen wird

    else :
        r = 0.5*(heron(a, n-1) + a / heron(a, n-1)) #Heron Formel

    try: 
        heron.counter += 1  # Zähler eins weiter
    except AttributeError : # Falls kein Zähler vorher definiert
        pass    # nix tun

    return r    #Gibt Ergebnis zurück



if __name__ == "__main__":  #Nur wenn Programm selbst gestartet nicht als Modul geladen
    
    from math import sqrt   # Import notwendige Module
    from time import time   # erst jetzt da für Heron nicht notwenig
                            # würde mit geladen werden wenn man dies als Modul importiert

    try:    #Nutzereingaben
        a = int(input("Zu berechnende Wurzel eingeben: ")) # int() bringt ValueError wenn Eingabe
        n = int(input("Anzahl Durchläufe eingeben: "))     # nicht umgewandelt werden kann. -> Abbruch

        if a <= 0 or n <= 0 : # Abbruch wenn Nutzer keine postiven Werte eingibt
            raise ValueError

        print("\nBerechnung Wurzel {0} für {1} Durchläufe \n\n\
'Nr.'   'Heron Berechnung'   'Unterschied zu sqrt()' \
'Rechenzeit' 'Interne Aufrufe'".format(a, n))    # Tabellenkopf

        for i in range(1,n+1):  # Schleife die Tabellenzeilen erzeugt
            heron.counter = 0   # Zähler Rücksetzen

            t = time()  # Computerzeit vor Ausführung
            r = heron(a,i)  # Ausführung Heron
            t = time()-t    # Differenz Computerzeit zu Zeit vor Ausführung

            print(" {0:2d}{1:23.16f}{2:24.16f}\
{3:12.5f}s      {4}".format(i,r,abs(sqrt(a)-r),t,heron.counter)) #Tabellenzeile
            # Nr, Berechneter Wert, Betrag Unterschied zu sqrt(2), Rechenzeit, Anzahl Durchläufe 

    except ValueError or TypeError :
        print("Bitte positive Integer eingeben!") # Meldung wenn Eingaben nicht passen

        # Anmerkung: Nutzereingaben die zu exceptions der Funktion führen würden,
        # werden vorher gefiltert damit der Tabellenkopf usw. nicht erst angezeigt wird
        # bevor diese Fehlermedlung kommt. Die exceptions der Funktion werden diese
        # trotzdem auslösen falls 'komische' Eingaben zu Fehlern während der Ausführung führen.
    
    input("\nPress Enter")   # Hält Fenster offen bis Enter gedrückt
