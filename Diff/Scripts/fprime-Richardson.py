#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Etude de l'extrapolation de Richardson appliquée à la 
formule de différences finies centrées pour f'.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
from floats import computeDigits
import sys
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def formule_centree(f, x, h):
    g = (f(x + h) - f(x - h)) / (2.0 * h)
    return g


x = 1.0
print(u"x=", x)
epsilon = sys.float_info.epsilon
h = epsilon ** (1.0 / 5.0)
print(u"h=", h)
exact = np.cos(x)
print(u"exact=", exact)
g1 = formule_centree(np.sin, x, h)
g2 = formule_centree(np.sin, x, 2.0 * h)
g = (4.0 * g1 - g2) / 3.0
print(u"g=", g)
d = computeDigits(exact, g, 10)
print(u"d=", d)


################################
# Itération de la méthode de Richardson
m = 6
h0 = 1.0
g = np.zeros((m, m))
# Intialisation
for i in range(m):
    h = h0 * (2 ** -i)
    print(u"h=", h)
    g[i, 0] = formule_centree(np.sin, x, h)
# Itérations
for i in range(1, m):
    for j in range(i):
        pj = 2 * (j + 1)
        print(u"j=", j, "pj=", pj)
        delta = (g[i, j] - g[i - 1, j]) / (2 ** pj - 1.0)
        g[i, j + 1] = g[i, j] + delta
print(g)

# Affichage formatté
for i in range(0, m):
    row = ""
    for j in range(i + 1):
        row += " %.4f" % (g[i, j])
    print(row)

# Calcul du nombre de chiffres corrects
d = np.zeros((m, m))
# Itérations
for i in range(0, m):
    for j in range(i + 1):
        d[i, j] = computeDigits(exact, g[i, j], 10)
print(d)

# Affichage formatté
for i in range(0, m):
    row = ""
    for j in range(i + 1):
        row += " %.2f" % (d[i, j])
    print(row)

####################################
# Nombre de chiffres gagnés par chaque division du pas h par 2.
chiffres = [p * np.log10(2.0) for p in [1, 2, 4, 6, 8, 10, 12]]
for c in chiffres:
    print(u"%.4f" % (c))
