#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
On considère la fonction de Runge :
    
    f(x) = 1 / (1 + 25 * x ^ 2)

pour tout x dans [-1, 1]. 

On interpole la fonction de Runge avec 6 points puis 10 points par deux 
polynômes de degrés 5 et 9, ce qui produit des oscillations. 
On observe les dérivées f'(x), f''(x) et f'''(x) et on observe que l'amplitude 
de ces dérivées augmente rapidement quand l'ordre de dérivation augmente.

See the Runge phenomenon with interpolating polynomials of degrees 5 and 9. 
See the Runge function and its derivatives f', f'', f'''.
"""
from numpy import linspace
import pylab as pl
from interp import polynomial_interpolation
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# Le phenomene de Runge
#
def runge(x):
    y = 1.0 / (1.0 + 25 * x ** 2)
    return y


print(u"")
print(u"Phenomene de Runge")
x = linspace(-1, 1, 100)
y = runge(x)
#
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, ":", label="f(x)")
#
# Degree 5 (6 points)
x = linspace(-1, 1, 6)
y = runge(x)
u = linspace(-1, 1, 100)
v = polynomial_interpolation(x, y, u)
pl.plot(u, v, "--", label="6 pts")
pl.plot(x, y, ".")
#
# Degree 9 (10 points)
x = linspace(-1, 1, 10)
y = runge(x)
u = linspace(-1, 1, 100)
v = polynomial_interpolation(x, y, u)
pl.plot(u, v, "-", label="10 pts")
pl.plot(x, y, ".")
#
pl.title(u"Le phénomène de Runge")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.savefig("runge-interpolation.pdf", bbox_inches="tight")

# Derivees de f
def rungePrime(x):
    y = -50 * x / (1.0 + 25 * x ** 2) ** 2
    return y


def rungePPrime(x):
    y = 50 * (75 * x ** 2 - 1) / (1.0 + 25 * x ** 2) ** 3
    return y


def rungePPPrime(x):
    y = -15000 * x * (25 * x ** 2 - 1) / (1.0 + 25 * x ** 2) ** 4
    return y


x = linspace(-1, 1, 100)
y = runge(x)
yp = rungePrime(x)
ypp = rungePPrime(x)
yppp = rungePPPrime(x)
#
fig = pl.figure(figsize=(4.0, 2.5))
pl.suptitle(u"Dérivées de la fonction de Runge", y=0.95)
pl.subplot(2, 2, 1)
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"y=f(x)")
pl.subplot(2, 2, 2)
pl.plot(x, yp, "-")
pl.xlabel(u"x")
pl.ylabel(u"y=f'(x)")
pl.subplot(2, 2, 3)
pl.plot(x, ypp, "-")
pl.xlabel(u"x")
pl.ylabel(u"y=f''(x)")
pl.subplot(2, 2, 4)
pl.plot(x, yppp, "-")
pl.xlabel(u"x")
pl.ylabel(u"y=f'''(x)")
fig.tight_layout()
pl.savefig("runge-derivees.pdf", bbox_inches="tight")
