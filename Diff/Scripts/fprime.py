#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Calcule des dérivées par des méthodes de différences finies. 
Observe la sensibilité de la précision en fonction de la longueur 
du pas de différentiation.
Observe la sensibilité en fonction de l'ordre de précision de la méthode.

Compute numerical derivatives with finite difference methods.
See the sensitivity of the accuracy depending on the step size. 
See the sensitivity of the order of precision of the method. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
from floats import computeDigits
import numdiff
import pylab as pl
import sys
import matplotlibpreferences


matplotlibpreferences.load_preferences()

#
# 1. Compute a derivative with 3 methods
print(u"")
print(u"1. Compute a derivative with 3 methods")
x = 1.0
h = 1.0e-4
print(u"x=", x)
print(u"h=", h)
g = (np.sin(x + h) - np.sin(x)) / h
print(u"g=", g)
exact = np.cos(x)
print(u"exact=", exact)
d = computeDigits(exact, g, 10)
print(u"d=", d)
g = (np.sin(x + h) - np.sin(x - h)) / (2.0 * h)
print(u"g=", g)
d = computeDigits(exact, g, 10)
print(u"d=", d)
#
# 2. Use various step sizes
# 2.1 See absolute error.
print(u"")
print(u"2. Use various step sizes")
print(u"2.1 See absolute error")
print(u"Forward (order 1)")
x = 1.0
print(u"x=", x)
exact = np.cos(x)
n = 16
e = np.zeros(n)
h = np.logspace(0, -15, n)
for i in range(n):
    g = (np.sin(x + h[i]) - np.sin(x)) / h[i]
    e[i] = abs(exact - g)
    print(u"h=", h[i], ", g=", g, ", AE=", e[i])

#
# 2.2 Plot absolute error
print(u"2.2 Plot absolute error")
n = 1000
e = np.zeros(n)
h = np.logspace(0, -15, n)
for i in range(n):
    g = (np.sin(x + h[i]) - np.sin(x)) / h[i]
    e[i] = abs(exact - g)

# Modèle
epsilon = sys.float_info.epsilon
e_modele = np.abs(np.sin(x)) * epsilon / h + np.abs(np.sin(x)) * h / 2.0

# Graphique
pl.figure(figsize=(2.0, 1.2))
pl.plot(h, e, "-", label="Observé")
pl.plot(h, e_modele, "--", label="Modèle")
pl.xlabel(r"$h$")
pl.ylabel(r"$e_{abs}$")
pl.title(u"Calcul de $f'$ par différences finies")
pl.xscale("log")
pl.yscale("log")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("fprime-abserr.pdf", bbox_inches="tight")

########################################
#
# Optionnel
#


#
# 3. Use various step sizes,
#    and various precisions
# See digits
print(u"")
print(u"3. Use various step sizes")
print(u"   and various precisions")
x = 1.0
exact = np.cos(x)
n = 100
d1 = np.zeros(n)
d2 = np.zeros(n)
h = np.logspace(2, -15, n)
for i in range(n):
    g = (np.sin(x + h[i]) - np.sin(x)) / h[i]
    d1[i] = computeDigits(exact, g, 10)
    g = (np.sin(x + h[i]) - np.sin(x - h[i])) / (2.0 * h[i])
    d2[i] = computeDigits(exact, g, 10)

pl.figure(figsize=(4, 3))
pl.plot(np.log10(h), d1, "-", label="$p=1$")
pl.plot(np.log10(h), d2, "--", label="$p=2$")
pl.xlabel(r"$\log_{10}(h)$")
pl.ylabel(u"Nombre de chiffres")
pl.legend()
pl.title(u"Calcul de $f'$ par différences finies")

#
# 2.3 Plot digits
n = 100
d = np.zeros(n)
h = np.logspace(0, -15, n)
for i in range(n):
    g, fcount = numdiff.first_derivative(np.sin, x, h[i], p=1)
    d[i] = computeDigits(exact, g, 10)

print(u"2.3 Plot digits")
pl.figure(figsize=(4, 3))
pl.plot(np.log10(h), d, "-")
pl.xlabel(r"$\log_{10}(h)$")
pl.ylabel(u"Nombre de chiffres")
pl.title(u"Calcul de $f'$ par différences finies")

#
# 1. Compute a derivative with 3 methods
print(u"")
print(u"1. Compute a derivative with 3 methods")
x = 1.0
exact = 2.0 * x
h = 1.0e-4
print(u"x=", x)
print(u"h=", h)
g, fcount = numdiff.first_derivative(np.sin, x, h, p=1)
d = computeDigits(exact, g, 10)
print(u"Forward (order 1) : g=", g, ", digits=", d, ", fcount=", fcount)
g, fcount = numdiff.first_derivative(np.sin, x, h, p=2)
d = computeDigits(exact, g, 10)
print(u"Centered (order 2): g=", g, ", digits=", d, ", fcount=", fcount)
g, fcount = numdiff.first_derivative(np.sin, x, h, p=4)
d = computeDigits(exact, g, 10)
print(u"Centered (order 4): g=", g, ", digits=", d, ", fcount=", fcount)

#
# 3. Use various step sizes,
#    and various precisions
# See digits
print(u"")
print(u"3. Use various step sizes")
print(u"   and various precisions")
x = 1.0
exact = np.cos(x)
n = 100
d1 = np.zeros(n)
d2 = np.zeros(n)
d4 = np.zeros(n)
h = np.logspace(2, -15, n)
for i in range(n):
    g, fcount = numdiff.first_derivative(np.sin, x, h[i], p=1)
    d1[i] = computeDigits(exact, g, 10)
    g, fcount = numdiff.first_derivative(np.sin, x, h[i], p=2)
    d2[i] = computeDigits(exact, g, 10)
    g, fcount = numdiff.first_derivative(np.sin, x, h[i], p=4)
    d4[i] = computeDigits(exact, g, 10)

pl.figure(figsize=(2.0, 1.0))
pl.plot(np.log10(h), d1, "-", label="$p=1$")
pl.plot(np.log10(h), d2, "--", label="$p=2$")
pl.plot(np.log10(h), d4, ":", label="$p=4$")
pl.xlabel(r"$\log_{10}(h)$")
pl.ylabel(u"Nb. de chiffres")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.ylim(top=16.0)
pl.title(u"Calcul de $f'$ par différences finies")
pl.savefig("fprime-trois-formules.pdf", bbox_inches="tight")

# Refaire avec la fonction suivante.
# Que se passe-t-il ?


def calcule_carre(x):
    y = x ** 2
    return y


#
# Utilise le pas optimal
print(u"")
print(u"Pas optimal")
x = 1.0
print(u"x=", x)
eps = sys.float_info.epsilon
h = eps ** (1.0 / 2.0)
print(u"h=", h)
g1 = (np.sin(x + h) - np.sin(x)) / h
print(u"g1=", g1)
exact = np.cos(x)
print(u"exact=", exact)
d1 = computeDigits(exact, g1, 10)
print(u"d1=", d1)
h = eps ** (1.0 / 3.0)
print(u"h=", h)
g2 = (np.sin(x + h) - np.sin(x - h)) / (2.0 * h)
print(u"g2=", g2)
d2 = computeDigits(exact, g2, 10)
print(u"d2=", d2)
