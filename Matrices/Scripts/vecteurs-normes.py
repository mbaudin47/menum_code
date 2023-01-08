#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre la boule unité en dimension 2 avec les trois normes 1 (diamant), 
2 (cercle) et infinie (carré). 
Montre deux vecteurs orthogonaux.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()
#


def setAxis():
    pl.axis("equal")
    pl.axis([-1.5, 1.5, -1.5, 1.5])
    return


def UnitEuclidianBall():
    # Boule unite euclidienne
    N = 100
    theta = np.linspace(0, 2 * np.pi, N)
    x = np.cos(theta)
    y = np.sin(theta)
    pl.plot(x, y, "-")
    pl.xlabel(u"$x_1$")
    # pl.ylabel(u"$x_2$")
    pl.title(u"Norme 2")
    setAxis()
    return


def UnitNorm1Ball():
    # Boule unite en norme 1
    N = 1000
    theta = np.linspace(0, 2 * np.pi, N)
    x = np.cos(theta)
    y = np.sin(theta)
    v = np.zeros((N, 2))
    v[:, 0] = x
    v[:, 1] = y
    for i in range(N):
        v[i, :] = v[i, :] / np.linalg.norm(v[i, :], 1)
    #
    x = v[:, 0]
    y = v[:, 1]
    pl.plot(x, y, "-")
    pl.xlabel(u"$x_1$")
    pl.ylabel(u"$x_2$")
    pl.title(u"Norme 1")
    setAxis()
    return


def UnitNormInfiniteBall():
    # Boule unite en norme Infinie
    N = 1000
    theta = np.linspace(0, 2 * np.pi, N)
    x = np.cos(theta)
    y = np.sin(theta)
    v = np.zeros((N, 2))
    v[:, 0] = x
    v[:, 1] = y
    for i in range(N):
        v[i, :] = v[i, :] / np.linalg.norm(v[i, :], np.inf)
    #
    x = v[:, 0]
    y = v[:, 1]
    pl.plot(x, y, "-")
    pl.xlabel(u"$x_1$")
    # pl.ylabel(u"$x_2$")
    pl.title(u"Norme infinie")
    setAxis()
    return


#
# 2. Boule unite euclidienne
print(u"")
print(u"2. Boule unite en norme 2")
pl.figure()
UnitEuclidianBall()

#
# 3. Boule unite en norme 1
print(u"")
print(u"3. Boule unite en norme 1")
pl.figure()
UnitNorm1Ball()


#
# 4. Boule unite en norme Infinie
print(u"")
print(u"4. Boule unite en norme Infinie")
pl.figure()
UnitNormInfiniteBall()


#
# 6. Vecteurs orthogonaux
print(u"")
print(u"Vecteurs orthogonaux")
x = np.array([2.0, 8.0])
y = np.array([4.0, -1.0])
print(u"x=", x)
print(u"y=", y)
print(u"(x,y)=", np.dot(x, y))
pl.figure(figsize=(2.0, 1.5))
pl.plot([0.0, x[0]], [0.0, x[1]], "-")
pl.text(x[0] + 0.5, x[1], "$\mathbf{x}$")
pl.plot([0.0, y[0]], [0.0, y[1]], "-")
pl.text(y[0] + 0.5, y[1], "$\mathbf{y}$")
pl.title(u"Vecteurs orthogonaux")
pl.axis("equal")
pl.xlabel(u"$x_1$")
pl.ylabel(u"$x_2$")
pl.axis([-2.0, 6.0, -2.0, 9.0])
pl.savefig("vecteurs-normes-orthogonaux.pdf", bbox_inches="tight")


# Trois normes dans le même graphique
fig = pl.figure(figsize=(3.5, 1.0))
pl.subplot(1, 3, 1)
UnitNorm1Ball()
pl.subplot(1, 3, 2)
UnitEuclidianBall()
pl.subplot(1, 3, 3)
UnitNormInfiniteBall()
pl.subplots_adjust(wspace=0.5)
pl.savefig("vecteurs-normes.pdf", bbox_inches="tight")
