#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Analyse du modèle logistique.

Références
Martin Braun. Differential equations and their applications, Fourth Edition. 
Texts in applied mathematics. Springer, 1993.

Morris W. Hirsch, Stephen Smale et Robert. L. Devaney. Differential 
Equations, Dynamical Systems, and an introduction do chaos, Third
Edition. Elsevier, 2013.

"""
import pylab as pl
import numpy as np
from scipy.integrate import odeint


def logistique(y, t):
    dydt = a * y[0] * (1.0 - y[0] / N)
    ydot = [dydt]
    return ydot


# Paramètres
a = 1.0
N = 1.0
t_min = 0.0
t_max = 2.0
n_points = 100
t = np.linspace(t_min, t_max, n_points)

#
pl.figure(figsize=(3.0, 1.5))
y0 = [0.5]
y = odeint(logistique, y0, t)
pl.plot(t, y[:, 0], "-")
pl.plot(t, np.ones(n_points), "k-")
pl.plot(t, np.zeros(n_points), "k-")
pl.xlabel(u"t")
pl.ylabel(u"y")
pl.title(u"Modèle logistique.")

# Plusieurs conditions initiales
pl.figure(figsize=(3.0, 1.5))
for y_initial in np.linspace(-0.05, 1.5, 5):
    y0 = [y_initial]
    y = odeint(logistique, y0, t)
    pl.plot(t, y[:, 0], "-")
pl.plot(t, np.ones(n_points), "k-")
pl.plot(t, np.zeros(n_points), "k-")
pl.xlabel(u"t")
pl.ylabel(u"y")
pl.title(u"Modèle logistique.")
pl.savefig("logistique-dynamique.pdf", bbox_inches="tight")

# Vector field
n_points = 10
t_range = np.linspace(t_min, t_max, 10)
y_range = np.linspace(-0.5, 1.5, 10)
T, Y = np.meshgrid(t_range, y_range)
dtdt = np.ones(T.shape)
dydt = a * Y * (1.0 - Y / N)
# Normalize arrows
s = np.sqrt(dtdt ** 2 + dydt ** 2)
dtdt = dtdt / s
dydt = dydt / s

#
pl.figure(figsize=(2.5, 1.5))
pl.title(u"Modèle logistique.")
pl.xlabel(u"t")
pl.ylabel(u"y")
pl.quiver(T, Y, dtdt, dydt, angles="xy")
t = np.linspace(t_min, t_max, n_points)
for y_initial in np.linspace(-0.05, 1.5, 5):
    y0 = [y_initial]
    y = odeint(logistique, y0, t)
    pl.plot(t, y[:, 0], "-")
pl.plot(t, np.ones(n_points), "k-")
pl.plot(t, np.zeros(n_points), "k-")
pl.savefig("logistique-champ.pdf", bbox_inches="tight")
