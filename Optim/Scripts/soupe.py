#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
On considère une boîte de soupe de rayon r et de volume imposé. 
On recherche le rayon qui minimise la surface latérale de la boîte, dans 
le but de minimiser le coût de production, c'est à dire le coût de l'aluminium.
On utilise la méthode du nombre d'or. 

Optimize the radius of a soup can with golden section algorithm.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
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
    v = 5.0e-4  # m**3
    s = 2 * pi * r ** 2 + 2 * v / r
    return s


# 2.
r_min = 0.01
r_max = 0.15
r = linspace(r_min, r_max, 100)
s = cansurface(r)
pl.figure()
pl.plot(r, s, "-")
pl.xlabel(u"Rayon (m)")
pl.ylabel(u"Surface (m2)")
pl.title(u"Probleme de la boîte de soupe")

# 3.
reltolx = 1.0e-8
ropt, Sopt = goldensectiongui(cansurface, r_min, r_max, reltolx)
print(u"ropt=", ropt)
print(u"Sopt=", Sopt)

# 4.
v = 5.0e-4  # m**3
r_opt = (v / (2 * pi)) ** (1.0 / 3.0)
print(u"Rayon optimal : r=", r_opt, "(m)")
hstar = v / (pi * r_opt ** 2)
print(u"Hauteur optimale : h=", hstar, "(m)")
digits = computeDigits(r_opt, ropt, 10)
print(u"Chiffres corrects:", digits)

# 5.
s_opt = cansurface(r_opt)
print(u"Surface optimale : s=", s_opt, "(m**2)")

########################################
#
# Optionnel
#
# 2. Plot
r = linspace(r_min, r_max, 100)
s = cansurface(r)
pl.figure(figsize=(2.0, 1.0))
pl.plot(r, s, "-")
pl.plot(r_opt, s_opt, "o")
pl.text(r_opt - 0.02, s_opt + 0.02, "($r^\star$,$s^\star$)")
pl.xlabel(u"Rayon (m)")
pl.ylabel(u"Surface ($m^2$)")
pl.title(u"Problème de la boîte de soupe")
pl.savefig("soupe.pdf", bbox_inches="tight")
