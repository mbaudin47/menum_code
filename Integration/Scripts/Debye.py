#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Calcule la température de Debye d'un solide. 
On considère la fonction de Debye d'ordre 3.
Pour cela, on utilise une méthode de quadrature adaptative. 

V est le volume du solide
N est le nombre d'atomes
rho est la densité du nombre d'atome par unité de volume
V = 0.001 # (m3) est le volume d'un litre d'aluminium
rho = 6.022e28 est le nombre d'atomes
kB est la constante de Boltzmann
TD est la température de Debye

Références
----------
http://en.wikipedia.org/wiki/Debye_model

M. Newman. "Computational Physics"
CHAPTER 5, INTEGRALS AND DERIVATIVES
Exercise 5.9: Heat capacity of a solid, p.33
http://www-personal.umich.edu/~mejn/cp/chapters/int.pdf

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
from quadrature import adaptsim
import matplotlibpreferences

matplotlibpreferences.load_preferences()


TD = 428.0  # Debye temperature (K) of aluminium
kB = 1.381e-23  # (J/K)
T = 298.0  # (K) = 25 deg Celsius


def debyeintegrand(x):
    if x == 0.0:
        f = 0.0
    else:
        f = x ** 4 * np.exp(x) / np.expm1(x) ** 2
    return f


# Make a plot
n = 100
x = np.linspace(0.0, T / TD, n)
y = np.zeros(n)
for i in range(n):
    y[i] = debyeintegrand(x[i])
pl.figure()
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"T=" + str(T) + " (K)")

u = T / TD
print(u"u = %.4f" % (u))
Q, fcount = adaptsim(debyeintegrand, 0.0, 1.0 / u)
print(u"Q = %.4f" % (Q))
N = 1
D = 3 * u ** 3 * Q
cv = 3 * N * kB * D
print(u"cv = %.3e (J/K)" % (cv))
cA = 6.0221412927e23  # Avogadro constant (1/mol)
print(u"Molar Heat capacity at 298 (K):", cv * cA, " (J/mol/K)")

# Debye function for heat capacity
# cv/(3*N*KB)
def debyefunc(u):
    # u=T/TD
    if u == 0.0:
        D = 0.0
    else:
        Q, fcount = adaptsim(debyeintegrand, 0.0, 1 / u)
        D = 3 * u ** 3 * Q
    return D


# Make a plot
n = 100
u = np.linspace(0.0, 1.5, n)
D = np.zeros(n)
for i in range(n):
    D[i] = debyefunc(u[i])
pl.figure(figsize=(2.0, 1.0))
pl.plot(u, D, "-")
pl.xlabel(u"T/TD")
pl.ylabel(u"CV/(3Nk)")
pl.title(u"Fonction de Debye")
pl.savefig("Debye.pdf", bbox_inches="tight")
