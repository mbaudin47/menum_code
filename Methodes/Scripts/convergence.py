#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre la convergence linéaire et quadratique d'une suite.
"""
import numpy
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 1. Linear Convergence
print(u"1. Linear Convergence")
n = 5
x = numpy.zeros(n)
x[0] = 1.0
for i in range(1, n):
    x[i] = x[i - 1] / 2.0

#
# 2. Quadratic Convergence
print(u"")
print(u"2. Quadratic Convergence")
y = numpy.zeros(n)
y[0] = 0.1
for i in range(1, n):
    y[i] = y[i - 1] ** 2

#
# 3. Plot
pl.figure(figsize=(2.5, 2.0))
(p1,) = pl.plot(numpy.arange(n), x, "o--")
(p2,) = pl.plot(numpy.arange(n), y, "x-")
pl.yscale("log")
pl.xlabel(u"Nombre d'itérations")
pl.ylabel(u"Erreur absolue")
pl.legend([p1, p2], ["Linéaire, $\mu=1/2$", "Quadratique"], loc=3)
pl.title(u"Convergence linéaire et quadratique")
pl.savefig("convergence.pdf", bbox_inches="tight")
