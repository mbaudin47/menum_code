#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Dessine le principe de la quadrature.

Références
----------
Cleve Moler. Numerical Computing with Matlab. Society for
Industrial Mathematics, 2004.

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def myfunc(x):
    y = np.sin(2.5 * x) ** 2
    return y


#
a = 0.0
b = 1.0
exacte = 0.59589242746631385

#
delta = 0.25
x = np.linspace(a - delta, b + delta, 100)
y = myfunc(x)
u = np.linspace(a, b, 100)
v = myfunc(u)
#
width = 2.0
height = 1.0
fig = pl.figure(figsize=(width, height))
pl.plot(x, y, "-")
pl.fill_between(u, 0.0, v, color="tab:orange")
"""
ax = fig.get_axes()
major_ticks = np.linspace(a, b, 3)
ax[0].set_xticks(major_ticks)
ax[0].set_yticks(major_ticks)
delta_minor = 0.1
ax[0].set_xticks(np.arange(a - 0.3, b + 0.4, delta_minor), minor=True)
ax[0].set_yticks(np.arange(a, b, delta_minor), minor=True)
pl.grid(which="both")
"""
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
pl.savefig("principe-quadrature.pdf", bbox_inches="tight")

# Compte les carrés entièrement sous la courbe
# Il y a 4 coins :
#
#  1       4
#   +-----+
#   |     |
#   |     |
#   +-----+
#  2       3
n = 11
n = n
h = (b - a) / (n - 1)  # Longueur du carré

fig = pl.figure(figsize=(width, height))
pl.plot(x, y, "-")
# pl.fill_between(u, 0.0, v, color="tab:orange")
ax = fig.get_axes()
major_ticks = np.linspace(a, b, 3)
ax[0].set_xticks(major_ticks)
ax[0].set_yticks(major_ticks)
ax[0].set_xticks(np.arange(a - 0.3, b + 0.4, h), minor=True)
ax[0].set_yticks(np.arange(a, b, h), minor=True)
pl.grid(which="both")
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
n_carres_dessous = 0
n_carres_au_dessus = 0
for i in range(n - 1):
    for j in range(n - 1):
        corner1 = [a + i * h, (j + 1) * h]
        corner2 = [a + i * h, j * h]
        corner3 = [a + (i + 1) * h, j * h]
        corner4 = [a + (i + 1) * h, (j + 1) * h]
        y1 = myfunc(corner1[0])
        y2 = myfunc(corner2[0])
        y3 = myfunc(corner3[0])
        y4 = myfunc(corner4[0])
        if corner1[1] <= y1 and corner4[1] <= y4:
            n_carres_dessous += 1
            pl.plot([a + i * h + h / 2], [j * h + h / 2], ".", color="tab:orange")
        if corner2[1] >= y2 and corner3[1] >= y3:
            n_carres_au_dessus += 1
            pl.plot([a + i * h + h / 2], [j * h + h / 2], "r.", color="tab:green")
print("Nombre de carrés dessous = ", n_carres_dessous)
integrale_min = n_carres_dessous * h ** 2
print("Nombre de carrés au dessus = ", n_carres_au_dessus)
print("Nombre de carrés contenant = ", n ** 2 - n_carres_au_dessus)
integrale_max = (n ** 2 - n_carres_au_dessus) * h ** 2
print("Minorant de l'intégrale =", integrale_min)
print("Majorant de l'intégrale =", integrale_max)
erreur_absolue = abs(integrale_min - exacte)
print("Erreur absolue =", erreur_absolue)
pl.savefig("principe-quadrature-comptage.pdf", bbox_inches="tight")
