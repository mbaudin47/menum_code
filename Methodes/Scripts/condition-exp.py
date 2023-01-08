#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Conditionnement de la fonction exponentielle.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import pylab as pl
from numpy import exp, linspace
from floats import expCond
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 2. Plot
N = 1000
x = linspace(0.5, 1.5, N)
y = exp(x)
c = expCond(x)
#
pl.figure(figsize=(2.5, 2.5))
#
pl.subplot(2, 1, 1)
pl.suptitle(u"Conditionnement de la fonction exp")
pl.plot(x, y, "-")
pl.ylabel(u"$\exp(x)$")
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.yscale("log")
pl.xlabel(u"$x$")
pl.ylabel(u"Cond. de exp")
pl.subplots_adjust(hspace=0.3)
pl.savefig("condition-exp.pdf", bbox_inches="tight")
