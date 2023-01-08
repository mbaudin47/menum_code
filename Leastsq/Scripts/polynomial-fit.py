#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
On considère 4 observations de la fonction f(x) = round(exp(x)) pour 
x entre -1 et 2 où round arrondi à la valeur entière la plus proche. 
On utilise la méthode des équations normales pour déterminer un polynôme 
de degré 2 s'ajustant aux observations au sens des moindres carrés.
On utilise la méthode des équations normales et on utilise la matrice de 
Vandermonde pour calculer la matrice de conception.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import pylab as pl
import numpy as np
from leastsq import polynomial_fit_normal_equations, polynomial_value
from numpy.linalg import solve, cond
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# 1. Données
# t
t = np.array([-1, 0, 1, 2])
print(u"t=")
print(t)
# y
y = np.round(np.exp(t))
print(u"y=")
print(y)

# 2. Plot
pl.figure()
pl.plot(t, y, "bo", label=u"Données")
pl.xlabel(u"t")
pl.ylabel(u"y")

# 3. Equations normales à la main
X = np.vander(t, 3)
print(u"X=")
print(X)
A = np.dot(np.transpose(X), X)
print(u"A=")
print(A)
print(u"log10(cond(A))=", np.log10(cond(A)))
b = np.dot(np.transpose(X), y)
print(u"b=")
print(b)
bet = solve(A, b)
print(u"(solve) bet=", bet)

# 4. Vérification
bet = polynomial_fit_normal_equations(t, y, 2)
print(u"(polynomial_fit_normal_equations) bet=", bet)

u = np.linspace(-1.5, 2.5)
p = polynomial_value(bet, u)

pl.figure(figsize=(1.0, 1.0))
pl.plot(u, p, "-", label=u"Modèle")
pl.plot(t, y, "o", label=u"Données")
pl.ylim([-0.5, 7.5])
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"$t$")
pl.ylabel(u"$y$")
pl.savefig("polynomial-fit.pdf", bbox_inches="tight")
