#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
On considère la méthode de Newton et on fait l'hypothèse que la méthode 
converge de manière quadratique. 
Montre l'évolution de l'erreur absolue sous cette hypothèse, avec un 
terme initial égal à 1. 

Observe le nombre de chiffres corrects dans la méthode de la bissection et 
de la méthode de Newton pour déterminer la racine positive du polynôme :
    P(x) = x ^ 3 + x - 1

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from fzero import newton, bisection
from floats import computeDigits

# Verifions la formule de l'exercice

# Initial
c = 1
e0 = 0.5
# Boucle
e = e0
n = 10
for i in range(n):
    p = c ** (2 ** i - 1) * e0 ** (2 ** i)
    print(u"i=", i, ",e=", e, ",p=", p)
    e = c * e ** 2

################################################################
# Afficher le nombre de chiffres exacts de la bissection


def myFunction(x):
    y = x ** 3 + x - 1
    return y


def myFunctionPrime(x):
    y = 3 * x ** 2 + 1
    return y


#
# 3. Dichotomie vs Newton
#
print(u"3. Bisection vs Newton")
a = 0.0
b = 1.0
xs_bisection, history_bisection = bisection(myFunction, a, b)
print(u"Dichotomie xs=", xs_bisection)
# Newton
x0 = 1.0
xs_newton, history_newton = newton(myFunction, x0, myFunctionPrime)
print(u"Newton xs=", xs_newton)

# Exact from Wolfram Alpha:
xexact = 0.68232780382801932737
print(u"Iterations=", len(history_bisection))
n = len(history_bisection)
latex_mode = False  # Set to True to produce a LaTeX table
for i in range(n):
    x_bisection = history_bisection[i]
    d10_bisection = computeDigits(xexact, x_bisection, 10)
    if not latex_mode:
        print(
            u"%d, Dichotomie x=%.6f, decimales=%.1f" % (i, x_bisection, d10_bisection)
        )
    if i < len(history_newton):
        x_newton = history_newton[i]
        d10_newton = computeDigits(xexact, x_newton, 10)
        if not latex_mode:
            print(u"%d, Newton x=%.16f, decimales=%.1f" % (i, x_newton, d10_newton))
    if latex_mode:
        if i < len(history_newton):
            print(
                "%d & %.6f & %.1f & %.17f & %.0f  \\\\"
                % (i, x_bisection, d10_bisection, x_newton, d10_newton)
            )
        else:
            print(
                "%d & %.6f & %.0f &       &       \\\\"
                % (i, x_bisection, d10_bisection)
            )
