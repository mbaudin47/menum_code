#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Résout l'équation différentielle ordinaire associée au problème de Lorenz.

Références
----------
Morris W. Hirsch, Stephen Smale et Robert. L. Devaney. Differential 
Equations, Dynamical Systems, and an introduction to chaos, Third
Edition. Elsevier, 2013.

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from scipy.integrate import odeint
import numpy as np
import pylab as pl
from odes import ode_plot
from liblorenz import lorenzgui
import matplotlibpreferences


matplotlibpreferences.load_preferences()

#
# 3. Attracteur de Lorenz
print(u"")
print(u"3. Attracteur de Lorenz")
#
# 3.1 Définir la fonction
print(u"3.1 Définir la fonction")


def lorenz_jacobian(y, t, beta, sigma, rho):
    A = np.array([[-beta, 0.0, y[1]], [0.0, -sigma, sigma], [-y[1], rho, -1.0]])
    return A


def lorenz(y, t, beta, sigma, rho):
    """
    The right-hand side of the
    Attracteur de Lorenz.

    Parameters
    sigma : Prandlt number
    rho : Rayleigh number
    """
    A = lorenz_jacobian(y, t, beta, sigma, rho)
    ydot = A @ y
    return ydot


# 3.2 Résoudre l'ODE
print(u"3.2 Résoudre l'ODE")
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
# Condition initiale classique
y0 = np.array([1.0, 1.0, 1.0])
tfinal = 30.0
t = np.linspace(0.0, tfinal, 10000)
y = odeint(lorenz, y0, t, (beta, sigma, rho))

# Condition initiale Moler
if False:
    eta = np.sqrt(beta * (rho - 10))
    yc = np.array([rho - 1.0, eta, eta])
    y0 = yc + np.array([0.0, 0.0, 3.0])

# 3.3 Trajectoire
print(u"3.3 Trajectoire")
pl.figure(figsize=(3.0, 2.0))
pl.plot(y[:, 1], y[:, 2], "-")
pl.axis("equal")
pl.xlabel(u"y[1]")
pl.ylabel(u"y[2]")
# axis([-1.2,1.2,-1.2,1.2])
pl.title(u"Attracteur de Lorenz : Trajectoire")

# 2.4 Regular plot
print(u"2.4 Regular plot")
ode_plot(t, y, "Attracteur de Lorenz", "-")

# Ref. : http://en.wikipedia.org/wiki/Lorenz_system
# 2.5 Other values
print(u"2.5 Other values")
tfinal = 30.0
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
fig = lorenzgui(tfinal, beta, sigma, rho)
pl.title(u"Attracteur de Lorenz. $\\beta=8/3$, $\\sigma=10$, $\\rho=28$.")
fig.set_size_inches(2.5, 1.5, forward=True)
pl.legend(bbox_to_anchor=(1.0, 1.0))
children = fig.get_children()[1]
line = children.get_children()[0]
line.set_linewidth(0.5)
pl.savefig("Lorenz.pdf", bbox_inches="tight")

#
pl.figure(figsize=(3.0, 2.0))
lorenzgui(tfinal=50, rho=14)

#
# Calcule les points stationnaires
print("Point stationnaire 1:")
t = 0.0
yc = [0.0, 0.0, 0.0]
print("yc =", yc)
f_yc = lorenz(yc, t, beta, sigma, rho)
print("f(yc) =", f_yc)
#
print("Point stationnaire 2:")
t = 0.0
yc = [rho - 1.0, np.sqrt(beta * (rho - 1)), np.sqrt(beta * (rho - 1))]
print("yc =", yc)
f_yc = lorenz(yc, t, beta, sigma, rho)
print("f(yc) =", f_yc)
#
print("Point stationnaire 3:")
t = 0.0
yc = [rho - 1.0, -np.sqrt(beta * (rho - 1)), -np.sqrt(beta * (rho - 1))]
print("yc =", yc)
f_yc = lorenz(yc, t, beta, sigma, rho)
print("f(yc) =", f_yc)

# Calcule les valeurs propres de la matrice Jacobienne
# en t = 0.0
t = 0.0
y = np.array([0.0, 0.0, 0.0])
J = lorenz_jacobian(y, t, beta, sigma, rho)
print("J=")
print(J)
w, v = np.linalg.eig(J)
print("w = ", w)
