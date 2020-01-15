#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Ableitung  - leitet ab

    enthält diff() Funktion die eingegeben Zusammenhang
    numerisch differenziert.'''

import numpy as np

def diff(t, h) :
    m = np.zeros_like(t)
    m[0] = (h[1]-h[0])/(t[1]-t[0])
    m[1:-1] = (h[2:]-h[:-2])/(t[2:]-t[:-2])
    m[-1] = (h[-1]-h[-2])/(t[-1]-t[-2])
    return m
