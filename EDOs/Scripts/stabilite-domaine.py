#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre le domaine de stabilité de plusieurs méthodes numériques 
pour les EDOs :
    * Euler explicite
    * Heun
"""

from numpy import linspace, meshgrid
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

#
pl.figure(figsize=(2.0, 1.1))
n = 100
x = linspace(-5, 5, n)
y = linspace(-5, 5, n)
xx, yy = meshgrid(x, y)
z = xx + 1j * yy
# Euler explicite
R = abs(1 + z)
pl.contour(xx, yy, R, levels=[1.0], colors=["tab:blue"])
pl.text(-1.7, -0.1, "Euler")
# Heun
R = abs(1 + z + 0.5 * z ** 2)
pl.contour(xx, yy, R, levels=[1.0], colors=["tab:orange"])
pl.text(0.3, 1.0, "Heun")
pl.axis("equal")
pl.xlim([-2.5, 1.5])
pl.ylim([-2.0, 2.0])
pl.xlabel(u"Re(z)")
pl.ylabel(u"Im(z)")
pl.title(u"Domaine de stabilité")
pl.savefig("stabilite-domaine.pdf", bbox_inches="tight")
