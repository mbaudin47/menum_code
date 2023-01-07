#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Compare plusieurs méthodes sur le problème test :
    * Euler
    * Heun
    * RK4
    
Le problème test est :
    
y'(t) = a * y(t),  t >= 0
y(0) = 1

avec a = 1.
"""

from numpy import linspace, exp
from odes import euler, explicit_method
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

# 3. Solve dy/dt=y
#
print(u"3. Solve dy/dt=ay")
print(u"3.1 Define the function")


def linearf(y, t, a):
    ydot = a * y
    # ydot=array(ydot)
    return ydot


a = 1.0
tspan = [0.0, 4.0]
y0 = 1.0
h = 1.0
#
pl.figure(figsize=(2.5, 1.5))
#
tout, yout = euler(linearf, tspan, y0, h, a)
pl.plot(tout, yout, "o:", label="Euler")
#
tout, yout = explicit_method("rk2", linearf, tspan, y0, h, a)
pl.plot(tout, yout, "*-.", label="RK2")
#
tout, yout = explicit_method("rk4", linearf, tspan, y0, h, a)
pl.plot(tout, yout, "+--", label="RK4")
#
texact = linspace(tspan[0], tspan[1], 100)
yexact = exp(a * texact)
pl.plot(texact, yexact, "-", label="Exact")
pl.legend(loc=2)
pl.xticks(range(5))
pl.title(u"ODE linéaire")
pl.xlabel(u"t")
pl.ylabel(u"y")
pl.savefig("probleme-test.pdf", bbox_inches="tight")
