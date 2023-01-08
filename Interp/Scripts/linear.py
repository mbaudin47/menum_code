#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Considère une table de 6 points entre 0 et 5. 
Dessine le graphique produit par la fonction "plot" : c'est une interpolation 
linéaire par morceaux.
Interpole les données par un polynôme linéaire par morceaux, puis par un 
polynôme global. 

Perform piecewise linear interpolation. 
Compare with global polynomial interpolation.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
from interp import piecewise_linear, polynomial_interpolation
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 1. Un exemple d'interpolation lineaire
print(u"")
print(u"1. Un exemple d'interpolation lineaire")
x = np.arange(0.0, 6.0)
y = np.array([5.0, 4.0, 2.0, -2.0, 1.0, 3.0])
pl.figure()
pl.plot(x, y, "o")
pl.plot(x, y, "-")
pl.title(u"Piecewise linear interpolation")

#
# 2. Une fonction d'interpolation lineaire
print(u"")
print(u"2. Une fonction d'interpolation lineaire")

nu = 100
u = np.linspace(-0.25, 5.25, nu)
v = piecewise_linear(x, y, u)
pl.figure()
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.title(u"Piecewise linear interpolation")

#
# 3. Comparaison linéaire contre polynomial
print(u"")
print(u"3. Comparaison linéaire contre polynomial")
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "o", label=u"Données")
nu = 100
u = np.linspace(-0.25, 5.25, nu)
v = piecewise_linear(x, y, u)
pl.plot(u, v, "-", label=u"Linéaire")
v = polynomial_interpolation(x, y, u)
pl.plot(u, v, "--", label=u"Polynomial")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
# title(u"Piecewise linear interpolation")
pl.savefig("linear.pdf", bbox_inches="tight")
