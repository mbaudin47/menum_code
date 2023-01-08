#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Contre-exemples de choix du pas optimal pour la dérivée première. 
Ces exemples montrent que le pas h = sqrt(epsilon) n'est pas toujours 
optimal et qu'il faut tenir compte de la dérivée seconde 
pour évaluer le pas optimal exact.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import sys
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# On utilise une formule décentrée d'ordre 1 pour f'
eps = sys.float_info.epsilon
h = np.sqrt(eps)
print(u"h=", h)


"""
f(x) = sqrt(x)
f'(x) = 0.5 / sqrt(x)
"""
# Cas OK
x = 1.0
print(u"+ x=", x)
xp = x + h
h_exact = xp - x
y = (np.sqrt(xp) - np.sqrt(x)) / h_exact
print(u"y=", y)
exact = 0.5 / np.sqrt(x)
print(u"exact=", exact)
eabs = abs(y - exact)
print(u"eabs=", eabs)
# Cas pas OK
x = 1.0e8
print(u"+ x=", x)
xp = x + h
h_exact = xp - x
print(u"h_exact=", h_exact)
y = (np.sqrt(xp) - np.sqrt(x)) / h_exact
print(u"y=", y)
exact = 0.5 / np.sqrt(x)
print(u"exact=", exact)
eabs = abs(y - exact)
print(u"eabs=", eabs)

# Calcul exact
x = 1.0e8
fx = np.sqrt(x)  # f(x)
f_seconde = 0.25 * x ** (-1.5)  # f''(x)
h = np.sqrt(2.0 * np.abs(fx) / np.abs(f_seconde)) * np.sqrt(eps)
print(u"+ h=", h)
y = (np.sqrt(x + h) - np.sqrt(x)) / h
print(u"y=", y)
exact = 0.5 / np.sqrt(x)
print(u"exact=", exact)
eabs = abs(y - exact)
print(u"eabs=", eabs)
erel = abs(y - exact) / abs(exact)
print(u"erel=", erel)


def decentree(x, h, fonction):
    xp = x + h
    h_exact = xp - x
    y = (fonction(xp) - fonction(x)) / h_exact
    return y


#
# Calcule l'erreur pour différents pas h avec une formule décentrée
x1 = 1.0
x2 = 1.0e2
x3 = 1.0e4
exact1 = 0.5 / np.sqrt(x1)
exact2 = 0.5 / np.sqrt(x2)
exact3 = 0.5 / np.sqrt(x3)
n = 50
e = np.zeros((n, 3))
h = np.logspace(0, -16, n)
for i in range(n):
    # En x1
    y = decentree(x1, h[i], np.sqrt)
    e[i, 0] = abs(exact1 - y)
    # En x2
    y = decentree(x2, h[i], np.sqrt)
    e[i, 1] = abs(exact2 - y)
    # En x3
    y = decentree(x3, h[i], np.sqrt)
    e[i, 2] = abs(exact3 - y)

# Graphique
pl.figure(figsize=(2.0, 1.2))
pl.plot(h, e[:, 0], "-", label="$x=1$")
pl.plot(h, e[:, 1], "--", label="$x=10^2$")
pl.plot(h, e[:, 2], ":", label="$x=10^4$")
pl.xlabel(r"$h$")
pl.ylabel(r"$e_{abs}$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.title(u"Calcule $f'$ par formule décentrée")
pl.xscale("log")
pl.yscale("log")
pl.savefig("contre-exemples.pdf", bbox_inches="tight")

# Recherche du plus petit incrément
x = 1.0e10
delta = 1.0
imax = 100
for i in range(imax):
    print(u"i=", i, "delta=", delta)
    diff = np.sqrt(x + delta) - np.sqrt(x)
    if diff == 0:
        print(u"Différence nulle !")
        break
    delta = delta / 2.0
print(u"delta=", delta)

happrox = np.sqrt(eps)
h = 2 ** 53 * delta * happrox
print(u"h=", h)
