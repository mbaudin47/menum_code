#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Calcule la dérivée seconde d'une fonction réelle par des méthodes 
de différences finies d'ordre de précision égales à 1, 2, 4.
Observe la sensibilité en fonction de la longueur du pas de différentiation.

Compute second derivative of a scalar function with methods of accuracy order 
1, 2 and 4. 
See the sensitivity to the step width.
"""
import numdiff
from floats import computeDigits
from pylab import plot, xlabel, ylabel, title, figure, xscale, legend
import numpy as np


def mysquare(x):
    y = x ** 2
    return y


#
# 1. Compute second derivative
print(u"")
print(u"1. Compute second derivative")
x = 1.0
h = 1.0e-4
expected = 2.0
print(u"x=", x)
H, fcount = numdiff.second_derivative(mysquare, x, h, p=1)
d = computeDigits(expected, H, 10)
print(u"Forward (order 1) : H=", H, ", digits=", d, ", fcount=", fcount)
H, fcount = numdiff.second_derivative(mysquare, x, h, p=1)
d = computeDigits(expected, H, 10)
print(u"Centered (order 2): H=", H, ", digits=", d, ", fcount=", fcount)
H, fcount = numdiff.second_derivative(mysquare, x, p=4)
d = computeDigits(expected, H, 10)
print(u"Centered (order 4): H=", H, ", digits=", d, ", fcount=", fcount)
#
# 2. Use various step sizes
# Plot digits
print(u"")
print(u"2. Use various step sizes")
print(u"Plot digits")


def mysin(x):
    y = np.sin(x)
    return y


x = 1.0
expected = -np.sin(x)
n = 100
d1 = np.zeros(n)
d2 = np.zeros(n)
d4 = np.zeros(n)
h = np.logspace(2, -11, n)
for i in range(n):
    H, fcount = numdiff.second_derivative(mysin, x, h[i], p=1)
    d1[i] = computeDigits(expected, H, 10)
    H, fcount = numdiff.second_derivative(mysin, x, h[i], p=2)
    d2[i] = computeDigits(expected, H, 10)
    H, fcount = numdiff.second_derivative(mysin, x, h[i], p=4)
    d4[i] = computeDigits(expected, H, 10)

figure()
(p1,) = plot(h, d1, "-")
(p2,) = plot(h, d2, "--")
(p4,) = plot(h, d4, ":")
xscale("log")
ylabel(u"Number of digits")
xlabel(u"Step size")
legend([p1, p2, p4], ["p=1", "p=2", "p=4"])
title(u"Computes f'' by finite differences")
