#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Utilise la méthode de la dichotomie pour déterminer une approximation de 
sqrt(2) par résolution de l'équation non linéaire x^2 - 2 = 0. 
On dessine le nombre de chiffres corrects en fonction du nombre 
d'itérations. x

Use the bisection algorithm to compute sqrt(2) by resolution of the 
equation x^2 - 2 = 0. 
Locate the zero of the function. 
Plot the number of correct digits during intermediate iterations of the 
algorithm. 
"""
from math import ceil, log, sqrt
from fzero import bisectiongui, bisection
from pylab import plot, xlabel, ylabel, title, figure
from floats import computeDigits
from numpy import linspace

#
# 1. Combien d'iterations de bisection pour e=0.5e-3
print(u"1. Combien d'iterations de bisection")
print(u"   pour e=0.5e-3")
e = 0.5e-3
print(u"e=", e)
i = ceil(-log(e) / log(2))
print(u"i=", i)


def myFunction(x):
    y = x ** 2 - 2
    return y


#
# 2. Dessiner la fonction pour localiser un zero
print(u"")
print(u"2. Dessiner la fonction pour localiser un zero")
N = 100
x = linspace(0.0, 2.0, N)
y = myFunction(x)
figure()
plot(x, y, "r-")
xlabel(u"x")
ylabel(u"f(x)")
title(u"$f(x)=x^2-2$")

#
# 3. Bisection
print(u"")
print(u"3. Bisection")
a = 1.0
b = 2.0
xs, history = bisection(myFunction, a, b)
print(u"xs=", xs)
for x_intermediate in history:
    print("x=", x_intermediate)

xs, history = bisectiongui(myFunction, a, b)
title(u"$f(x)=x^2-2$")

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
digits = list()
for xs in history:
    d = computeDigits(xexact, xs, 10)
    digits.append(d)

i = list(range(n))
figure()
plot(i, digits, "-")
xlabel(u"Iterations")
ylabel(u"Nombre de chiffres corrects")
title(u"Convergence de la dichotomie.")
