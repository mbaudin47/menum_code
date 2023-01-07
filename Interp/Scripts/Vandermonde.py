#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Considère une table de 4 observations et utilise la fonction vander du module 
numpy pour évaluer la matrice de Vandermonde.
Cette matrice est utile pour l'interpolation d'une fonction par un polynôme.
Utilise deux boucles imbriquées pour évaluer la matrice. 
Réalise une interpolation de Lagrange sur les données.

Use numpy's vander function.
Evaluate the Vandermonde matrix with two for loops.
Perform Lagrange interpolation.
"""
import numpy as np
import pylab as pl
from interp import polynomial_interpolation
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 1. Compute and use Vandermonde matrix
print(u"")
print(u"1. Compute and use Vandermonde matrix")
x = np.array([-1.0, 0.0, 1.0, 2.0])
print(u"x=", x)
V = np.vander(x)
print(u"V=")
V
y = np.array([-2.0, 1.0, 0.0, 1.0])
print(u"y=", y)
c = np.linalg.solve(V, y)
print(u"c=", c)
exact = np.array([1.0, 0.0, -2, -5])
print(u"exact=", exact)
# Compute matrix "by hand"
n = x.shape[0]
V = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        V[i, j] = x[i] ** (n - j - 1)

print(u"V=")
print(V)
#
# 2. Interpolation de Lagrange
print(u"")
print(u"2. Interpolation de Lagrange")
# Number of points where to interpolate
nu = 100
x = np.array([-1.0, 0.0, 1.0, 2.0])
y = np.array([-2.0, 1.0, 0.0, 1.0])
u = np.linspace(-1.25, 2.25, nu)
v = polynomial_interpolation(x, y, u)
#
pl.figure(figsize=(2.0, 1.0))
pl.title(u"Le polynôme $x^3 - 2 x^2 + 1$")
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.savefig("Vandermonde.pdf", bbox_inches="tight")

########################################
#
# Optionnel
#
#
# 3. Un autre exemple
print(u"")
print(u"3. Un autre exemple")
x = np.arange(0, 7)
y = np.array([0.0, 0.8415, 0.9093, 0.1411, -0.7568, -0.9589, -0.2794])
print(u"data=")
print(x)
print(y)
nu = 100
print(u"nu=", nu)
u = np.linspace(-0.25, 6.25, nu)
v = polynomial_interpolation(x, y, u)
pl.figure()
pl.plot(x, y, "o")
pl.plot(u, v, "-")

#
# 4. Encore un autre exemple
print(u"")
print(u"4. Encore un autre exemple")
pl.figure(figsize=(2.0, 1.5))
x = np.arange(0.0, 6.0)
y = np.array([5.0, 4.0, 2.0, -2.0, 1.0, 3.0])
pl.plot(x, y, "o")
print(u"data=")
print(x)
print(y)
nu = 100
print(u"nu=", nu)
u = np.linspace(-0.25, 5.25, nu)
v = polynomial_interpolation(x, y, u)
pl.plot(u, v, "--")
pl.title(u"Interpolation polynomiale")

#
# 5. Exemple : affiche le polynome
print(u"")
print(u"5. Exemple : affiche le polynome")
x = np.arange(0, 7)
y = np.array([0.0, 0.8415, 0.9093, 0.1411, -0.7568, -0.9589, -0.2794])
print(u"data=")
print(x)
print(y)
A = np.vander(x)
print(u"A=", A)
c = np.linalg.solve(A, y)
for i in range(6):
    print(u"c(%d)=%.4f" % (i, c[i]))
