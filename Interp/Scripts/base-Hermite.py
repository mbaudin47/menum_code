#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine les fonctions de base d'Hermite.
Ces polynômes sont définis sur l'intervalle [0,1] et sont tels que
phi1(0) = 1, phi1'(0) = 0, phi1(1) = 0, phi1'(1) = 0 
phi2(0) = 0, phi2'(0) = 1, phi2(1) = 0, phi2'(1) = 0 
phi3(0) = 0, phi3'(0) = 0, phi3(1) = 1, phi3'(1) = 0 
phi4(0) = 0, phi4'(0) = 0, phi4(1) = 0, phi4'(1) = 1 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

t = np.linspace(0.0, 1.0)
phi1 = 2 * t ** 3 - 3 * t ** 2 + 1
phi2 = t ** 3 - 2 * t ** 2 + t
phi3 = -2 * t ** 3 + 3 * t ** 2
phi4 = t ** 3 - t ** 2

fig = pl.figure()
pl.plot(t, phi1, "-", label=r"$\varphi_1$")
pl.plot(t, phi2, "--", label=r"$\varphi_2$")
pl.plot(t, phi3, "-.", label=r"$\varphi_3$")
pl.plot(t, phi4, ":", label=r"$\varphi_4$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"$t$")
pl.ylabel(u"$y$")
pl.title(u"Base polynomiale cubique d'Hermite")
fig.set_figwidth(2.0)
fig.set_figheight(1.0)
pl.savefig("base-Hermite.pdf", bbox_inches="tight")

# Résout les 4 systèmes d'équations linéaires

A = np.array(
    [
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0, 0.0],
        [1.0, 1.0, 1.0, 1.0],
        [3.0, 2.0, 1.0, 0.0],
    ]
)
print(u"A=")
print(A)
print(u"det(A)=", np.linalg.det(A))

print(u"inv(A)")
print(np.linalg.inv(A))

# Affiche les coefficients des polynômes d'Hermite
for i in range(4):
    print(u"i=", i)
    b = np.zeros((4,))
    b[i] = 1.0
    print(u"b=", b)
    c = np.linalg.solve(A, b)
    print(u"c=", c)
