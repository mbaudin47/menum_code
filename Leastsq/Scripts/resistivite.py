#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Considère 17 observations de la résistivité du cuivre en fonction de la 
température. 
Utilise la méthode des moindres carrés pour déterminer les coefficients 
du polynôme de degré 1 qui s'approche des observations. 

Les étudiants ont trouvé les valeurs suivantes.
Cuivre :
    a=0.307924498
    b=97.7050118
Cuivre :
    a=0.377121471
    b=100.3577414

References
----------
Department of physics
Czech Technical University in Prague
2011
"Determination of temperature 
coefficient of resistance of metals"
http://aldebaran.feld.cvut.cz/vyuka/physics_1/Labs/Lab1sample.pdf

"""

import pylab as pl
import numpy as np
from leastsq import polynomial_fit_normal_equations, polynomial_fit
import matplotlibpreferences

matplotlibpreferences.load_preferences()


# Temperature, resistance
# T (degC), R (Ohm)
# 28,30,...,60
temp = range(28, 62, 2)
copper = [
    106.0,
    106.8,
    107.0,
    108.0,
    108.6,
    109.3,
    110.1,
    110.8,
    111.5,
    111.9,
    112.6,
    113.3,
    113.7,
    114.3,
    114.9,
    115.6,
    116.1,
]
platinum = [
    111.0,
    111.6,
    112.4,
    113.2,
    114.0,
    114.8,
    115.4,
    115.9,
    117.1,
    117.6,
    118.6,
    119.2,
    119.9,
    120.9,
    121.5,
    122.2,
    122.9,
]
# Print data
print(np.array([temp, copper, platinum]).T)

print(u"Cuivre:")
betCopper1 = polynomial_fit_normal_equations(temp, copper, 1)
print(u"(Normal) bet=", betCopper1)
print(u"    Resistivité=", betCopper1[0] / betCopper1[1], "Ohm/Deg")
betCopper2 = polynomial_fit(temp, copper, 1)
print(u"(QR) bet=", betCopper2)
print(u"    Resistivité=", betCopper2[0] / betCopper2[1], "Ohm/Deg")

print(u"Platine:")
betPlatine1 = polynomial_fit_normal_equations(temp, platinum, 1)
print(u"(Normal) bet=", betPlatine1)
print(u"    Resistivité=", betPlatine1[0] / betPlatine1[1], "Ohm/Deg")
betPlatine2 = polynomial_fit(temp, platinum, 1)
print(u"(QR) bet=", betPlatine2)
print(u"    Resistivité=", betPlatine2[0] / betPlatine2[1], "Ohm/Deg")

#
t = np.linspace(28, 60)
pl.figure(figsize=(3.5, 2.0))
pl.plot(temp, copper, "o", label=u"Cu (données)", color="tab:blue")
modeleCuivre = betCopper2[0] * t + betCopper2[1]
pl.plot(t, modeleCuivre, "-", label=u"Cu (modèle)", color="tab:blue")
pl.plot(temp, platinum, "x", label=u"Pt (données)", color="tab:orange")
modelePlatine = betPlatine2[0] * t + betPlatine2[1]
pl.plot(t, modelePlatine, "--", label=u"Pt (modèle)", color="tab:orange")
pl.legend(loc="best")
pl.xlim(left=20.0)
pl.ylim(top=130.0)
pl.xlabel(u"Température (°C)")
pl.ylabel(u"Résistance (Ohm)")
pl.title(u"Résistance en fonction de la température.")
pl.savefig("resistivite.pdf", bbox_inches="tight")

# Resolution
# Design matrix
n = 2
X = np.vander(temp, n)
print("X=")
print(X)
y = copper
print("y=")
print(y)
Q, R = np.linalg.qr(X)
z = Q.T @ y
print("z=")
print(z)
beta = np.linalg.solve(R, z)
print("beta=")
print(beta)
alpha = beta[0] / beta[1]
print(u"Resistivité= %.e3 Ohm/Deg" % (alpha))
