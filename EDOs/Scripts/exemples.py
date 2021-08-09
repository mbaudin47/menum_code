#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Utilise différentes méthodes de résolution d'EDOs pour résoudre le problème 
de l'oscillateur harmonique. 
Dessine la trajectoire dans l'espace des phases. 
Dessine la série temporelle.

Use different ODE solves to solve the harmonic oscillator. 
Plot a trajectory in the phase space. 
Plot the time serie.
"""
from scipy.integrate import odeint
import pylab as pl
from odes import ode_plot
import matplotlibpreferences
import numpy as np


matplotlibpreferences.load_preferences()

#
# 1. Oscillateur harmonique
print(u"1. Oscillateur harmonique")
#
# 1.1 Definir la fonction
print(u"1.1 Definir la fonction")


def harmosc(y, t):
    ydot = [y[1], -y[0]]
    return ydot


# 1.2 Resoudre l'ODE
print(u"1.2 Resoudre l'ODE")
t_min = 0.0
t_max = 5.0
y0 = [1.0, 0.0]
t = np.linspace(t_min, t_max, 100)
y = odeint(harmosc, y0, t)

# 1.3 Une trajectoire dans l'espace des phases
print(u"1.3 Une trajectoire dans l'espace des phases")
delta = 0.1
pl.figure(figsize=(3.0, 2.0))
pl.plot(y[:, 0], y[:, 1], "-")
pl.plot(y0[0], y0[1], "*")
pl.plot(y[-1, 0], y[-1, 1], "o")
pl.text(y0[0] + delta, y0[1] + delta, "t=%s" % (t_min))
pl.text(y[-1, 0] + delta, y[-1, 1] + delta, "t=%s" % (t_max))
pl.axis("equal")
pl.axis([-1.2, 1.4, -1.2, 1.4])
pl.xlabel(u"y[0]")
pl.ylabel(u"y[1]")
pl.title(u"Oscillateur harmonique : une trajectoire")
pl.savefig("exemples-phaseplot-comm.pdf", bbox_inches="tight")

# 1.4 Serie temporelle
print(u"1.4 Serie temporelle")
ode_plot(t, y, "Oscillateur harmonique", "-")
fig = pl.gcf()
fig.set_figwidth(3.0)
fig.set_figheight(2.0)
pl.savefig("exemples-timeseries.pdf", bbox_inches="tight")
