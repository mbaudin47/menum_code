#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Utilise la quadrature adaptative sur un exemple.
"""
import numpy as np
from quadrature import adaptsim


def myfunc(x):
    y = np.sin(2.5 * x) ** 2
    return y


Q, fcount = adaptsim(myfunc, 0.0, 1.0)
print(u"Q =", Q)
print(u"fcount =", fcount)
exacte = (5.0 - np.sin(5.0)) / 10.0
erreur_absolue = abs(Q - exacte)
print(u"erreur_absolue =", erreur_absolue)
