#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Polynôme de Taylor pour la fonction sin au voisinage de 
x=0.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from numpy import linspace, sin
import pylab as pl
from math import pi, factorial
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def P1(x):
    y = x
    return y


def P3(x):
    y = x - x ** 3 / 6
    return y


x = linspace(-pi, pi, 100)
y = sin(x)
y1 = P1(x)
y3 = P3(x)

pl.figure(figsize=(3.0, 1.0))
pl.plot(x, y, "-", label="$\sin$")
pl.plot(x, y1, "--", label="$P_1$")
pl.plot(x, y3, ":", label="$P_3$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.savefig("Taylor.pdf", bbox_inches="tight")

x = 0.5
errmax = abs(x) ** 5 / (factorial(5))
abserr = abs(sin(x) - P3(x))
print(u"Err.Max.=%.3e" % (errmax))
print(u"Abs.Err.=%.3e" % (abserr))
