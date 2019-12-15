#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Übung 03 -- Tom Barnowsky 06.11.2019

    3 Funktionen zur Berechnung von größtem gemeinsamen Teiler
    und kleinstem gemeinsamen Vielfachen zweier Ganzzahlen.
    '''

def ggT(a,b):
    ''' Klassischer euklidischer Algorithmus

        Berechnet größten gemeinsamen Teiler durch wiederholte Subtraktion.
        Zwei Integer a und b als Argumente.'''

    if not isinstance(a, int) or not isinstance(b, int) : # Eingabewerte keine Integer?
        raise TypeError("'ggT(a,b)' only supports instances 'int'") #-> TypeError Fehlermeldung

    while True :    # wiederhole immer

        if a > b :  # a größer b?
            a -= b  #-> subtrahiere a von b, Ergebnis wieder a

        elif a < b :    # a kleiner b?
            a1 = a  #-> tausche Variablen
            a = b
            b = a1

        else :  # a = b?
            break   #-> Abbruch Schleife

    return a # rückgabe a

def ggTmod(a,b) :
    ''' Moderner euklidischer Algorithmus

        Berechnet größten gemeinsamen Teiler durch wiederholte Division mit Rest
        Zwei Integer a und b als Argumente.'''
    
    if not isinstance(a, int) or not isinstance(b, int) :   # Eingebewerte keine Integer?
        raise TypeError("'ggTmod(a,b)' only supports instances 'int'")  #-> TypeError Fehlermedlung

    while True : # wiederhole immer

        if a % b == 0 : # a mod b = 0?
            break   #-> Abbruch Schleife

        else :  # sonst
            a1 = a % b  #-> b = a mod b, a = altes b
            a = b
            b = a1

    return b # rückgabe b

def kgV(a,b) :
    ''' Kleinstes gemeinsames Vielfaches

        Kleinstes gemeinsames Vielfaches - berechnet kleinstes
        gemeinsames Vielfaches indem das Produkt der Parameter
        durch deren größten gemeinsamen Teiler geteilt wird.
        Zwei Integer a und b als Argumente.'''

    if not isinstance(a, int) or not isinstance(b, int) :   # Eingabewerte keine Integer?
        raise TypeError("'kgV(a,b)' only supports instances 'int'") #-> TypeError Fehlermeldung

    a0 = a  # zwischenspeichern Eingabevariablen
    b0 = b

    # moderner euklidischer Algorithmus auf a und b

    while True : # wiederhole immer
        
        if a % b == 0 : # a mod b = 0?
            break   #-> Abbruch Schleife
        
        else :  # sonst
            a1 = a % b  #-> b = a mod b, a = altes b
            a = b
            b = a1

    return int((a0 * b0) / b) # Produkt der Eingabevariablen geteilt durch deren größten gemeinsamen Teiler
        # Ausgabe als Integer

a = 15170983
b = 6002039

print("Eingabewerte {0} und {1}\n\n\
Größter gemeinsamer Teiler nach klassischem Algorithmus:  {2}\n\
Größter gemeinsamer Teiler nach modernem Algorithmus:     {3}\n\
Kleinstes gemeinsames Vielfaches:                         {4}".format(\
a,b,ggT(a,b),ggTmod(a,b),kgV(a,b)))
