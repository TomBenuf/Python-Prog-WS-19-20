#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Ableitung  - Tom Barnowsky - 15.01.2020

    enthält diff() Funktion die eingegeben Zusammenhang
    numerisch differenziert.'''

import numpy as np

def diff(t, h) :

    ''' Leitet die Werte im h Array nach dem t Array ab.
        '''

    m = np.zeros_like(t)            # 1D Array so groß wie Messwerte
    m[0] = (h[1]-h[0])/(t[1]-t[0])  # erster Punk mit Differenzenquotient
    m[1:-1] = (h[2:]-h[:-2])/(t[2:]-t[:-2]) # Mittelteil mit zentraler Differentation
    m[-1] = (h[-1]-h[-2])/(t[-1]-t[-2]) # letzter Punkt mit Differenzenquotient
    return m # Anstiegs Array zurück
