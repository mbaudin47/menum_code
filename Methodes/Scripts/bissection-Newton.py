#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Compare la convergence des méthodes de la dichotomie et de Newton sur des 
exemples bien choisis.
"""
from math import ceil, log
from fzero import newton, bisection
import pylab as pl
from floats import computeDigits
from numpy import linspace
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# Bisection vs Newton
#

#
# 1. Combien d'iterations de bisection pour e=0.5e-3
print(u"1. Combien d'iterations de bisection")
print(u"   pour e=0.5e-3")
e = 0.5e-3
print(u"e=", e)
i = ceil(-log(e) / log(2))
print(u"i=", i)


def myFunction(x):
    y = x ** 3 + x - 1
    return y


def myFunctionPrime(x):
    y = 3 * x ** 2 + 1
    return y


#
# 2. Dessiner la fonction pour localiser un zero
print(u"")
print(u"2. Dessiner la fonction pour localiser un zero")
N = 10
x = linspace(0.0, 1.0, N)
y = myFunction(x)
pl.figure()
pl.plot(x, y, "r-")
pl.xlabel(u"x")
pl.ylabel(u"X**2+X-1")
pl.title(u"The function")
# pl.savefig(")

#
# 3. Bisection
#
print(u"")
print(u"3. Bisection")
# 3.1 Test
print(u"")
print(u"3.1 Test")
a = 0.0
b = 1.0
xs, history = bisection(myFunction, a, b)
print(u"xs=", xs)
# Exact from Wolfram Alpha:
xexact = 0.68232780382801932737
d = computeDigits(xexact, xs, 10)
print(u"Correct decimal digits=", d)
print(u"Iterations=", len(history))
#
# 3.2 Faire un graphique
print(u"")
print(u"3.2 Bisection - Faire un graphique")
n = len(history)
abserr = list()
for xs in history:
    re = abs(xs - xexact)
    abserr.append(re)
i = list(range(n))
pl.figure()
pl.plot(i, abserr, "r-")
pl.xlabel(u"Iterations")
pl.ylabel(u"Absolute error")
pl.title(u"Convergence of Bisection")
pl.yscale("log")

#
# 4. Newton-Raphson
print(u"")
print(u"4. Newton-Raphson")
#
# 4.1 Test
print(u"")
print(u"4.1 Test")
x0 = 1.0
xs, history = newton(myFunction, x0, myFunctionPrime)
print(u"xs=", xs)
# Exact from Wolfram Alpha:
xexact = 0.68232780382801932737
d = computeDigits(xexact, xs, 10)
print(u"Correct decimal digits=", d)
print(u"Iterations=", len(history))
#
# 4.2 Faire un graphique
print(u"")
print(u"4.2 Newton-Raphson - Faire un graphique")
n = len(history)
abserr = list()
for xs in history:
    re = abs(xs - xexact)
    abserr.append(re)
i = list(range(n))
#
pl.figure()
pl.plot(i, abserr, "r-")
pl.xlabel(u"Iterations")
pl.ylabel(u"Absolute error")
pl.title(u"Convergence of Newton-Raphson")
pl.yscale("log")
