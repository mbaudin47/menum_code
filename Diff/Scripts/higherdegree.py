#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Calcule des dérivées numériques de degré élevé. 
Calcule les dérivées jusqu'à l'ordre 4 d'un polynôme de degré 4. 
Calcule la dérivée d'ordre 10 des fonctions exp et sin.

Compute numerical derivatives of higher degree.
Compute derivatives up to the 4th order of a degree 4 polynomial.
Compute order 10 derivatives of exp and sin functions.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from floats import computeDigits
from pylab import plot, title, figure
import matplotlibpreferences
import numpy as np
import numdiff

matplotlibpreferences.load_preferences()


def mypoly(x):
    print(u"+ mypoly - x=", x)
    y = x ** 4 + x ** 3 + x ** 2 + x + 1
    return y


#
# 1. Consider a polynomial
print(u"1. Consider the polynomial x**4+x**3+x**2+x+1")
# 1.1 Evaluate f(x)
print(u"")
print(u"1.1 Evaluate f(x)")
x = 1.0
expected = mypoly(x)
y = numdiff.derivative_forward(mypoly, x, 0)
print(u"x=", x)
print(u"Exact f(x)=", expected)
print(u"Computed f(x)=", y)

# 1.2 Evaluate f'(x)
print(u"")
print(u"1.2 Evaluate f'(x)")
x = 1.0
expected = 4 * x ** 3 + 3 * x ** 2 + 2 * x + 1
y = numdiff.derivative_forward(mypoly, x, 1)
print(u"x=", x)
print(u"Exact f'(x)=", expected)
print(u"Computed f'(x)=", y)

# 1.3 Evaluate f''(x)
print(u"")
print(u"1.3 Evaluate f''(x)")
x = 1.0
expected = 12 * x ** 2 + 6 * x + 2
y = numdiff.derivative_forward(mypoly, x, 2)
print(u"x=", x)
print(u"Exact f''(x)=", expected)
print(u"Computed f''(x)=", y)

# 1.4 Evaluate f'''(x)
print(u"")
print(u"1.4 Evaluate f'''(x)")
x = 1.0
expected = 24 * x + 6
y = numdiff.derivative_forward(mypoly, x, 3)
print(u"x=", x)
print(u"Exact f'''(x)=", expected)
print(u"Computed f'''(x)=", y)

# 1.5 Evaluate f''''(x)
print(u"")
print(u"1.5 Evaluate f''''(x)")
x = 1.0
expected = 24
y = numdiff.derivative_forward(mypoly, x, 4)
print(u"x=", x)
print(u"Exact f''''(x)=", expected)
print(u"Computed f''''(x)=", y)


def myexp(x):
    y = np.exp(x)
    return y


# 2. Evaluate f(d)(x) for increasing d,
# with f(x)=exp(x)
print(u"")
print(u"2. Evaluate f(d)(x) for increasing d, ")
print(u"with f(x)=exp(x)")
x = 1.0
print(u"x=", x)
print(u"Exact f(d)(x)=", expected)
expected = np.exp(x)
for d in range(8):
    y = numdiff.derivative_forward(myexp, x, d)
    digits = computeDigits(expected, y, 10)
    print(u"d=", d, ", f(x)=", y, ", digits=", digits)

# 3. Plot the points required for d=4
def myexpplot(x):
    plot(x, 0.0, "b|")
    print(u"x=", x)
    y = np.exp(x)
    return y


print(u"")
print(u"3. Plot the points required for d=4")
x = 1.0
print(u"x=", x)
print(u"Exact f(d)(x)=", expected)
expected = np.exp(x)
figure()
y = numdiff.derivative_forward(myexpplot, x, 4)
title(u"Degree 4 derivative of exp(x)")

# Méthode itérative pour dériver y=sin(x) trois fois
x = 1.0
degre = 3
expected = -np.cos(x)
print(u"f(3)(x)=", expected)
h = 1.0e-3
y = numdiff.derivative_forward(np.sin, x, degre)
digits = computeDigits(expected, y, 10)
print(u"y=", y, ", digits=", digits)

# Méthode itérative pour dériver y=sin(x) trois fois
x = 1.0
degre = 3
expected = -np.cos(x)
print(u"f(3)(x)=", expected)
h = 1.0e-3
y = numdiff.derivative_centered(np.sin, x, degre)
digits = computeDigits(expected, y, 10)
print(u"y=", y, ", digits=", digits)

# 2. Evaluate f(d)(x) for increasing d,
# with f(x)=exp(x)
print(u"")
print(u"2. Evaluate f(d)(x) for increasing d, ")
print(u"with f(x)=exp(x)")
x = 1.0
print(u"x=", x)
print(u"Exact f(d)(x)=", expected)
expected = np.exp(x)
for d in range(8):
    y = numdiff.derivative_centered(myexp, x, d)
    digits = computeDigits(expected, y, 10)
    print(u"d=", d, ", f(x)=", y, ", digits=", digits)
