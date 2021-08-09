#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre le domaine de stabilité de plusieurs méthodes numériques 
pour les EDOs :
    * Euler explicite
    * Heun
"""

from numpy import linspace, exp
import pylab as pl
from odes import euler
import matplotlibpreferences


matplotlibpreferences.load_preferences()

#
def testproblem(y, t):
    lamb = -10.0
    ydot = lamb * y
    return ydot


lamb = -10.0
t0 = 0.0
h = 0.1
tfinal = 1.5
y0 = 1.0
tspan = [t0, tfinal]
#
pl.figure(figsize=(2.5, 1.0))
#
h = 0.15
tout, yout = euler(testproblem, tspan, y0, h)
pl.plot(tout, yout, "-.", label="h=" + str(h))
#
h = 0.2
tout, yout = euler(testproblem, tspan, y0, h)
pl.plot(tout, yout, "--", label="h=" + str(h))
#
h = 0.25
tout, yout = euler(testproblem, tspan, y0, h)
pl.plot(tout, yout, ":", label="h=" + str(h))
#
t = linspace(t0, tfinal)
y = exp(lamb * t)
pl.plot(t, y, "-", label="Exact")
#
pl.ylim(top=20.0)
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"t")
pl.ylabel(u"y")
pl.title(u"Méthode d'Euler.")
pl.savefig("stabilite-Euler.pdf", bbox_inches="tight")
