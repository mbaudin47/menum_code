#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine la convergence de la méthode de la dichotomie en utilisant le 
logarithme en base 10 de l'erreur absolue, en fonction du nombre 
d'itérations. 

Plot the convergence of the bisection algorithm in terms of the 
base-10 logarithm of the absolute error, depending on the number of 
iterations. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from math import sqrt, log10
from fzero import bisection
import pylab as pl
from floats import computeDigits
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def myFunction(x):
    y = x ** 2 - 2
    return y


# 3. Bisection
#
print(u"")
print(u"3. Bisection")
a = 1.0
b = 2.0
xs, history = bisection(myFunction, a, b)
print(u"xs=", xs)
xexact = sqrt(2.0)
d = computeDigits(xexact, xs, 10)
print(u"Correct decimal digits=", d)
print(u"Iterations=", len(history))
#
# 4. Faire un graphique des digits
print(u"")
print(u"4. Faire un graphique")
n = len(history)
erreur = list()
for xs in history:
    d = log10(abs(xexact - xs))
    erreur.append(d)

i = list(range(n))
pl.figure(figsize=(2.0, 1.0))
pl.plot(i, erreur, "-")
pl.xlabel(u"Itérations")
pl.ylabel(u"Log10(erreur)")
pl.title(u"Convergence de la dichotomie")
pl.savefig("bissection-erreur.pdf", bbox_inches="tight")
