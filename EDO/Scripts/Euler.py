#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Utilise la méthode d'Euler pour calculer la solution du problème de 
l'oscillateur harmonique. 
Utilise la méthode d'Euler pour calculer la solution du problème-test, c'est 
à dire de l'EDO associée à la fonction exponentielle.


Uses Euler' method to simulate the harmonic oscillator. 
Uses Euler' method to solve the test problem, i.e. the problem with 
exponential solution. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from numpy import linspace, pi, cos, sin, array
from numpy.linalg import norm
from odes import euler
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

#
# 1. Oscillateur Harmonique a la main
#
print(u"1. Oscillateur Harmonique a la main")


def harmosc(y, t):
    ydot = array([y[1], -y[0]])
    return ydot


# 1.1 Methode d'Euler
print(u"1.1 Methode d'Euler")
t0 = 0.0
tfinal = 2 * pi
h = 0.1
y0 = array([1.0, 0.0])
t = t0
y = y0
i = 0
while t <= tfinal:
    y = y + h * harmosc(y, t)
    t = t + h
    i = i + 1

# 1.2 Solution
print(u"1.2 Solution")
print(u"h=", h)
print(u"y=", y)
yexact = [cos(tfinal), -sin(tfinal)]
print(u"yexact=", yexact)
print(u"Nombre d'iterations:", i)
print(u"Erreur absolue=", norm(yexact - y, 1))
#
# 2. Oscillateur Harmonique avec une fonction
#
print(u"2. Oscillateur Harmonique avec une fonction")
# 2.1 Approximate solution
print(u"2.1 Approximate solution")
tspan = [0.0, 2 * pi]
h = 0.1
y0 = [1.0, 0.0]
tout, yout = euler(harmosc, tspan, y0, h)

# 2.2 Exact solution
print(u"2.2 Exact solution")
n = 100
t = linspace(0, 2 * pi, n)
yexact = array([cos(t), -sin(t)])
yexact = yexact.T

# 2.3 Phase plot
print(u"2.3 Phase plot")
pl.figure(figsize=(2.0, 1.0))
pl.plot(yout[:, 0], yout[:, 1], "-+", label="Euler")
pl.plot(yexact[:, 0], yexact[:, 1], "--", label="Exact")
pl.axis("equal")
pl.axis([-1.2, 1.4, -1.4, 1.6])
pl.xlabel(u"\\tt{y[0]}")
pl.ylabel(u"\\tt{y[1]}")
pl.legend(bbox_to_anchor=(1.0, 1.0, 0.0, 0.0))
pl.title(u"Diagramme de phase")
pl.savefig("Euler.pdf", bbox_inches="tight")

###############################################
#
# Exercices supplementaires
#
from math import ceil
from numpy import zeros, exp

#
# 3. Solve dy/dt=y
#
print(u"3. Solve dy/dt=ay")
# 3.1 Define the function
print(u"3.1 Define the function")


def linearf(y, t, a):
    ydot = a * y
    return ydot


a = 1.0
t0 = 0.0
tfinal = 4.3
# 3.2 Algorithme d'Euler
print(u"3.2 Algorithme d'Euler")
h = 1.0
y = 1.0
t = t0
n = 1 + ceil((tfinal - t0) / h)
tout = zeros(n)
yout = zeros(n)
tout[0] = t
yout[0] = y
i = 0
while t < tfinal:
    h = min(h, tfinal - t)
    y = y + h * linearf(y, t, a)
    t = t + h
    i = i + 1
    tout[i] = t
    yout[i] = y

# 3.2 Plot
print(u"3.3 Plot")
texact = linspace(t0, tfinal, 100)
yexact = exp(a * texact)
#
pl.figure(figsize=(3.0, 2.0))
pl.plot(tout, yout, "-+")
pl.plot(texact, yexact, "--")
pl.legend(("Euler", "Exact"), loc=2)
pl.xticks(list(range(5)))
pl.title(u"ODE linéaire")
pl.xlabel(u"$t$")
pl.ylabel(u"$y$")
