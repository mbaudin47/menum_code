#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Utilise la méthode de Newton pour calculer une approximation de sqrt(2) par 
résolution de l'équation non linéaire x^2 - 2 = 0.
Calcule le nombre de chiffres corrects durant les itérations intermédiaires. 
Présente des contre-exemple de non convergence de la méthode de Newton. 

Use Newton's method to compute sqrt(2) by resolution of the 
equation x^2 - 2 = 0. 
Compute the number of significant digits during intermediate iterations 
of the algorithm.
Present counter-examples for Newton's method:
    * non convergence, 
    * divergence 1, 
    * divergence 2.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from math import sqrt
from fzero import newton, newtongui
import pylab as pl
from floats import computeDigits
from numpy import linspace, vectorize, exp, zeros
import matplotlibpreferences


matplotlibpreferences.load_preferences()

# 3. Definir myFunction
def myFunction(x):
    y = x ** 2 - 2
    return y


# 4. Definir myFunctionPrime
def myFunctionPrime(x):
    y = 2 * x
    return y


xs, history = newton(myFunction, 1.0, myFunctionPrime)
print(u"xs=", xs)
for x_intermediate in history:
    print("x=", x_intermediate)

# 5. Utiliser newtongui
N = 100
x = linspace(1.0, 2.0, N)
y = myFunction(x)
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"f(x)")
pl.title(u"$f(x)=x^2-2$")
xs, history = newtongui(myFunction, 1.0, myFunctionPrime)

# 6. Utiliser computeDigits
print(u"xs=", xs)
xexact = sqrt(2.0)
d = computeDigits(xexact, xs, 10)
print(u"Correct decimal digits=", d)
print(u"Iterations=", len(history))

# 7. Convergence de la methode
n = len(history)
digits = zeros(n)
for i in range(n):
    xs = history[i]
    digits[i] = computeDigits(xexact, xs, 10)

i = list(range(n))
pl.figure()
pl.plot(i, digits, "o")
pl.xlabel(u"Iterations")
pl.ylabel(u"Nombre de chiffres corrects")
pl.title(u"Convergence de la methode de Newton")

#####################################
#
# Optionnel
#
# 3. Contre-exemple - A
# Aller-retour autour de a
#
print(u"")
print(u"3. Contre-exemple A")
print(u"   Aller-retour autour de a")


def counterF(x, a):
    if x >= a:
        y = sqrt(x - a)
    else:
        y = -sqrt(a - x)
    return y


def counterFPrime(x, a):
    y = 1.0 / (2 * sqrt(abs(x - a)))
    return y


a = 2.0
N = 100
x = linspace(0.0, 4.0, N)
f = vectorize(counterF)
y = f(x, a)
pl.figure()
pl.plot(x, y, "r-")
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
pl.title(u"Newton Counter Example - A")
if False:
    # Generates an exception
    xs, history = newtongui(counterF, 1.0, counterFPrime, None, a)
    print(u"Iterations=", len(history))

# Figure dans le manuel
pl.figure(figsize=(1.0, 1.0))
pl.plot(x, y, "-", label="f", color="tab:red")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
x1 = 1.0
y0 = counterF(x1 + a, a)
y1 = counterF(a - x1, a)
pl.plot([a + x1, a + x1], [0.0, y0], "--", label="Newton", color="tab:blue")
pl.plot([a + x1, a - x1], [y0, 0.0], "--", color="tab:blue")
pl.plot([a - x1, a - x1], [0.0, y1], "--", color="tab:blue")
pl.plot([a - x1, a + x1], [y1, 0.0], "--", color="tab:blue")
pl.plot(a, 0.0, "o", color="tab:green")
pl.plot(a + x1, 0.0, "o", color="tab:orange")
pl.plot(a + x1, y0, "o", color="tab:orange")
pl.plot(a - x1, 0.0, "o", color="tab:orange")
pl.plot(a - x1, y1, "o", color="tab:orange")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("Newton.pdf", bbox_inches="tight")

#
# 4. Contre-exemple - B
# Divergence
#
print(u"")
print(u"4. Contre-exemple B")
print(u"   Divergence")


def counterExpF(x):
    y = x * exp(-(x ** 2))
    return y


def counterExpFPrime(x):
    y = exp(-(x ** 2)) * (1.0 - 2.0 * x ** 2)
    return y


N = 100
x = linspace(-2.0, 2.0, N)
y = counterExpF(x)
pl.figure()
pl.plot(x, y, "-", color="tab:orange")
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
pl.title(u"Newton Counter Example - B")
try:
    xs, history = newtongui(counterExpF, 1.0, counterExpFPrime)
    print(u"Iterations=", len(history))
except ValueError:
    print("Newton does not converge !")

#
# 5. Contre-exemple - C
# Convergence lente
#
print(u"")
print(u"5. Contre-exemple C")
print(u"Convergence lente")


def counterPow3F(x):
    y = (x - 1.0) ** 3
    return y


def counterPow3FPrime(x):
    y = 3 * (x - 1) ** 2
    return y


N = 100
x = linspace(0.0, 2.0, N)
y = counterPow3F(x)
pl.figure()
pl.plot(x, y, "-")
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
pl.title(u"Newton Counter Example - C")
x1 = 1.01
xs, history = newtongui(counterPow3F, x1, counterPow3FPrime)
print("history", history)
print("Number of iterations:", len(history))

#
# 6. Contre-exemple - D
# Division par zéro
#
print(u"")
print(u"6. Contre-exemple D")
print(u"Division par zéro")


def counterExempleD(x):
    y = x**3 + 3 * x ** 2 - 6
    return y


def counterExempleDPrime(x):
    y = 3 * x ** 2 + 6 * x
    return y


N = 100
x = linspace(-3.0, 1.5, N)
y = counterExempleD(x)
pl.figure(figsize=(1.0, 1.0))
pl.plot(x, y, "-")
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
x_exact = 1.195823345445647153
pl.plot([x_exact], [0.0], "+", label="Zéro")
x1 = -2.0
pl.plot([x1], [0.0], "o", label="$x_1$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("Newton-contre-exemple.pdf", bbox_inches="tight")
try:
    xs, history = newtongui(counterExempleD, x1, counterExempleDPrime)
except ZeroDivisionError:
    print("Division par zéro!")
