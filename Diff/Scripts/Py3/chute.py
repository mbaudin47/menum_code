#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Calcule des dérivées par différences finies sur le problème 
de la chute d'un objet dans un fluide.
"""
import numpy as np
import pylab as pl
from optim import goldensection
import numdiff
import sys
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def altitude(t):
    g = 9.81
    z0 = 50.0
    v0 = 76.0
    m = 250.0
    c = 7.0
    z = z0 + (m / c) * (v0 + (m * g / c)) * (1 - np.exp(-(c / m) * t)) - (m * g / c) * t
    return z


def moins_altitude(t):
    z = altitude(t)
    return -z


reltolx = 1.0e-8
topt, fopt = goldensection(moins_altitude, 0.0, 12.0, reltolx)
fopt = -fopt

print(u"topt=", topt)
print(u"fopt=", fopt)

# Calcul de la trajectoire
t = np.linspace(0, 12, 100)
z = altitude(t)

# 2. Graphique
pl.figure(figsize=(2.0, 1.0))
pl.plot(t, z, "-")
pl.plot(topt, fopt, "o")
pl.xlabel(u"Temps (s)")
pl.ylabel(u"Altitude (m)")
pl.title(u"Jet d'une masse dans un fluide visqueux.")
pl.savefig("chute.pdf", bbox_inches="tight")

# Calcul de la dérivée première
zp1, fcount = numdiff.first_derivative(altitude, topt, p=1)
print(u"z'(t) (ordre=1)=%.3e" % (zp1))
zp2, fcount = numdiff.first_derivative(altitude, topt, p=2)
print(u"z'(t) (ordre=2)=%.3e" % (zp2))
zp4, fcount = numdiff.first_derivative(altitude, topt, p=4)
print(u"z'(t) (ordre=4)=%.3e" % (zp4))

# Calcul de la dérivée seconde
zpp1, fcount = numdiff.second_derivative(altitude, topt, p=1)
print(u"z''(t) (ordre=1)=%.3e" % (zpp1))
zpp2, fcount = numdiff.second_derivative(altitude, topt, p=2)
print(u"z''(t) (ordre=2)=%.3e" % (zpp2))
zpp4, fcount = numdiff.second_derivative(altitude, topt, p=4)
print(u"z''(t) (ordre=4)=%.3e" % (zpp4))

# Calcul de l'erreur sur zp avec une formule d'ordre 1
# Erreur = h * f'' / 2 # Burden, Faires, p164
p = 1
eps = sys.float_info.epsilon
h = eps ** (1.0 / (p + 1))
erreur_zp = np.abs(zpp1) * h / 2.0
print(u"Erreur sur z'(t) (ordre=1)=%.3e" % (erreur_zp))

# Calcul de la dérivée quatrième
zpppp = numdiff.finite_differences(altitude, topt, order=4, p=5)
print(u"z^(4)(t) (ordre=6)=%.3e" % (zpppp))

# Calcul de l'erreur sur zpp avec une formule d'ordre 1
# erreur = h^2 * f^(4) / 12 # Burden, Faires, p171
p = 1
eps = sys.float_info.epsilon
h = eps ** (1.0 / (p + 2))
erreur_zpp = np.abs(zpppp) * h ** 2 / 12.0
print(u"Erreur sur z''(t) (ordre=1)=%.3e" % (erreur_zpp))
