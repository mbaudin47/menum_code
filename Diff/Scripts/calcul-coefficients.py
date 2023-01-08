#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Calcul des coefficients d'une formule de différences finies 
pour la dérivée d'ordre d avec une précision p.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import sys
import pylab as pl
from numdiff import compute_indices, finite_differences, compute_coefficients

# Calcul pour une formule pour la dérivée première, d'ordre 4, centrée.
direction = "centered"
d = 1
p = 4
imin, imax = compute_indices(d, p, direction)
print(direction, d, p, imin, imax)
indices = list(range(imin, imax + 1))
A = np.vander(indices, increasing=True).T
print(u"A = ")
print(A)
nc = d + p
b = np.zeros((nc))
b[d] = 1.0
print("b=")
print(b)
c = np.linalg.solve(A, b)
print(u"c = ")
print(c)

# Calcul pour différences directions, degrés, précision
for direction in ["forward", "backward"]:
    for d in range(1, 5):
        for p in range(1, 5):
            imin, imax = compute_indices(d, p, direction)
            print(direction, d, p, imin, imax)

# Calculs pour la formule centrée
direction = "centered"
for d in range(1, 5):
    for p in range(1, 5):
        if (d + p) % 2 == 1:
            imin, imax = compute_indices(d, p, direction)
            print(direction, d, p, imin, imax)
            indices = list(range(imin, imax + 1))
            A = np.vander(indices, increasing=True).T
            print(u"A = ")
            print(A)
            c = compute_coefficients(d, p, direction)
            print(u"c = ")
            print(c)


"""
Considère f(x) = sin(x)
On considère la dérivée troisième : d = 3.
On a f'''(x) = - cos(x)
"""

# Evalue f'''(x)
x = 1.0
print(u"x=", x)
exact = -np.cos(x)
print(u"f'''(x)=", exact)
d = 3
p = 4
y = finite_differences(np.sin, x, d, p)
print(u"F.D.=", y)
eabs = abs(exact - y)
print(u"Erreur absolue=", eabs)

# Calcule l'erreur pour différents pas h avec une formule décentrée
n = 1000
e = np.zeros(n)
h = np.logspace(0, -6, n)
for i in range(n):
    y = finite_differences(np.sin, x, d, p, h=h[i])
    e[i] = abs(exact - y)

eps = sys.float_info.epsilon
hopt = eps ** (1.0 / (d + p))
eopt = eps ** (p / (d + p))

# Graphique
pl.figure(figsize=(2.0, 1.5))
pl.plot(h, e, "-")
pl.plot(hopt, eopt, "o")
pl.xlabel(r"$h$")
pl.ylabel(r"$E_{abs}$")
pl.title(u"Calcule f''' par formule centrée.")
pl.xscale("log")
pl.yscale("log")


# Vérification du fait que, si la formule est centrée,
# et si d et pair et p impair,
# alors la formule est en fait d'ordre p + 1.
d = 4
p = 5
direction = "centered"
imin, imax = compute_indices(d, p, direction)
print(direction, d, p, imin, imax)
imin, imax = compute_indices(d, p, direction)
indices = list(range(imin, imax + 1))
A = np.vander(indices, increasing=True).T
print(u"A = ")
print(A)
c = compute_coefficients(d, p, direction)
print(u"c = ")
print(c)
s = 0
for i in range(imin, imax + 1):
    s += i ** (d + p) * c[i - imin]
    print(i ** (d + p), "*", c[i - imin])
print(u"s=", s)

# Cas particulier : d pair, p impair
x = 1.0
print(u"x=", x)
exact = -np.sin(x)
print(u"f''(x)=", exact)
d = 2
p = 5

# Calcule l'erreur pour différents pas h avec une formule décentrée
n = 1000
e = np.zeros(n)
h = np.logspace(0, -6, n)
for i in range(n):
    y = finite_differences(np.sin, x, d, p, h=h[i])
    e[i] = abs(exact - y)

eps = sys.float_info.epsilon
hopt = eps ** (1.0 / (d + p + 1))
eopt = eps ** ((p + 1) / (d + p + 1))

# Graphique
pl.figure(figsize=(2.0, 1.5))
pl.plot(h, e, "-")
pl.plot(hopt, eopt, "o")
pl.xlabel(r"$h$")
pl.ylabel(r"$E_{abs}$")
pl.title(u"Calcule f'' par formule centrée.")
pl.xscale("log")
pl.yscale("log")

# Evolution du conditionnement de A quand d+p augmente
# Si d+p est très grand
dmax = 20
p = 4
d_array = list(range(1, dmax, 2))
conditionnement = np.zeros((len(d_array), 3))
index = 0
for d in d_array:
    #
    direction = "forward"
    imin, imax = compute_indices(d, p, direction)
    indices = list(range(imin, imax + 1))
    A = np.vander(indices, increasing=True).T
    conditionnement[index, 0] = np.linalg.cond(A)
    #
    direction = "backward"
    imin, imax = compute_indices(d, p, direction)
    indices = list(range(imin, imax + 1))
    A = np.vander(indices, increasing=True).T
    conditionnement[index, 1] = np.linalg.cond(A)
    #
    direction = "centered"
    imin, imax = compute_indices(d, p, direction)
    indices = list(range(imin, imax + 1))
    A = np.vander(indices, increasing=True).T
    conditionnement[index, 2] = np.linalg.cond(A)
    index += 1

pl.figure()
pl.plot(d_array, conditionnement[:, 0], "-", label="A droite")
pl.plot(d_array, conditionnement[:, 1], "--", label="A gauche")
pl.plot(d_array, conditionnement[:, 2], "-.", label="Centrée")
pl.yscale("log")
pl.xlabel(u"d")
pl.ylabel(u"$cond_2$")
pl.title(u"Conditionnement de la matrice pour p=%d." % (p))
pl.legend()

#
"""
Démonstration des coefficients sur un cas.
On considère la fonction f(x) = sin(x).
On souhaite estimer f^{4}(x) = sin(x) au point x=1.
"""
d = 4
p = 3
direction = "centered"
c = compute_coefficients(d, p, direction)
print(u"d=", d, "p=", p, "c=", c)
x = 1.0
y = finite_differences(np.sin, x, d, p, direction)
print(u"y=", y)
exact = np.sin(x)
print(u"exact=", exact)
eabs = abs(y - exact)
print(u"Erreur absolue=", eabs)

# Démonstration de formules
direction = "centered"
for d in range(1, 5):
    for p in range(1, 5):
        if (d + p) % 2 == 1:
            imin, imax = compute_indices(d, p, direction)
            print(direction, d, p, imin, imax)
            indices = list(range(imin, imax + 1))
            A = np.vander(indices, increasing=True).T
            c = compute_coefficients(d, p, direction)
            s = "["
            for i in range(d + p):
                s += "%.3e" % (c[i])
                if i < d + p - 1:
                    s += ", "
            s += "]"
            print(u"c = ", s)
