#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
On considère une boîte de soupe de rayon r et de volume imposé. 
On recherche le rayon qui minimise la surface latérale de la boîte, dans 
le but de minimiser le coût de production, c'est à dire le coût de l'aluminium.
On utilise la méthode du nombre d'or. 

Optimize the radius of a soup can with golden section algorithm.
"""

import pylab as pl
from numpy import linspace
from math import pi
from optim import goldensectiongui
from floats import computeDigits
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# 1.
def cansurface(r):
    V = 5.0e-4  # m**3
    S = 2 * pi * r ** 2 + 2 * V / r
    return S


# 2.
r_min = 0.01
r_max = 0.15
r = linspace(r_min, r_max, 100)
S = cansurface(r)
pl.figure()
pl.plot(r, S, "-")
pl.xlabel(u"Rayon (m)")
pl.ylabel(u"Surface (m2)")
pl.title(u"Probleme de la boite de soupe")

# 3.
reltolx = 1.0e-8
ropt, Sopt = goldensectiongui(cansurface, r_min, r_max, reltolx)
print(u"ropt=", ropt)
print(u"Sopt=", Sopt)

# 4.
V = 5.0e-4  # m**3
rstar = (V / (2 * pi)) ** (1.0 / 3.0)
print(u"Rayon optimal : r=", rstar, "(m)")
hstar = V / (pi * rstar ** 2)
print(u"Hauteur optimale : h=", hstar, "(m)")
digits = computeDigits(rstar, ropt, 10)
print(u"Chiffres corrects:", digits)

# 5.
Sstar = cansurface(rstar)
print(u"Surface optimale : S=", Sstar, "(m**2)")

########################################
#
# Optionnel
#
# 2. Plot
sr = linspace(r_min, r_max, 100)
S = cansurface(r)
pl.figure(figsize=(2.0, 1.0))
pl.plot(r, S, "-")
pl.plot(rstar, Sstar, "o")
pl.text(rstar - 0.02, Sstar + 0.02, "($R^\star$,$S^\star$)")
pl.xlabel(u"Rayon (m)")
pl.ylabel(u"Surface ($m^2$)")
pl.title(u"Problème de la boite de soupe.")
pl.savefig("soupe.pdf", bbox_inches="tight")
