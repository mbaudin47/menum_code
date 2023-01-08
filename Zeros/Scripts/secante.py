#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Utilise la méthode de la sécante pour calculer une approximation de sqrt(2) 
par résolution de l'équation non linéaire x^2 - 2 = 0. 
Calcule le nombre de chiffres exacts durant les itérations intermédiaires 
de l'algorithme.

Use the secant method to compute sqrt(2) by resolution of the 
equation x^2 - 2 = 0. 
Compute the number of accurate digits during the intermediate 
iterations of the algorithm. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from math import sqrt
from fzero import secant, secantgui
from pylab import plot, xlabel, ylabel, title, figure
from floats import computeDigits


def myFunction(x):
    y = x ** 2 - 2
    return y


a = 1.0
b = 2.0
xs, history = secant(myFunction, a, b)
print(u"xs=", xs)
for x_intermediate in history:
    print("x=", x_intermediate)

#
# 1. Secant
print(u"")
print(u"1. Secant")
N = 100
a = 1.0
b = 2.0
xs, history = secantgui(myFunction, a, b)
title(u"$f(x)=x^2-2$")

print(u"xs=", xs)
xexact = sqrt(2.0)
d = computeDigits(xexact, xs, 10)
print(u"Correct decimal digits=", d)
print(u"Iterations=", len(history))
#
# 2. Faire un graphique
print(u"")
print(u"2. Faire un graphique")
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
title(u"Convergence de la sécante.")
