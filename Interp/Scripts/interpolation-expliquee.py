#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Explique le fonctionnement de l'interpolation linéaire par morceaux.
On compare deux implémentation du calcul:
    - un calcul non vectorisé, fondé sur deux boucles imbriquées, combinées 
      à des conditions,
    - un calcul vectorisé fondé sur un une seule boucle for.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import interp

# Data
x = np.arange(0.0, 6.0)
print("x=", x)
y = np.array([5.0, 4.0, 2.0, -2.0, 1.0, 3.0])
print("y=", y)
n = np.size(x)

# Linear Interpolation
m = 10
u = np.linspace(-0.25, 5.25, m)
print("u=", u)

# Partie 1 : calcul non vectorisé
v = np.zeros((m))
for i in range(m):
    print("i=", i, "u[i]=", u[i])
    # Si u[i] < x[0], alors k = 0.
    # Si u[i] > x[n - 1], alors k = n - 2.
    # Sinon trouve l'indice k tel que x[k] <= u[i] < x[k+1]

    # Recherche l'indice k
    if u[i] < x[0]:
        k = 0
    elif u[i] > x[n - 1]:
        k = n - 2
    else:
        for j in range(n - 1):
            print("        j=", j, "x[j]=", x[j], "x[j+1]=", x[j + 1])
            if u[i] < x[j + 1]:
                k = j
                print("    k=", k, "Stop.")
                break
    print("    k=", k)
    # Calcule la pente
    delta = (y[k + 1] - y[k]) / (x[k + 1] - x[k])
    print("    delta=", delta)
    # Evalue l'interpolant
    s = u[i] - x[k]
    v[i] = y[k] + s * delta
print("v=", v)

pl.figure()
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.title(u"Piecewise linear interpolation")


def piecewise_linear_naive(x, y, u):
    n = np.size(x)
    m = np.size(u)
    v = np.zeros((m))
    for i in range(m):
        # Si u[i] < x[0], alors k = 0.
        # Si u[i] > x[n - 1], alors k = n - 2.
        # Sinon trouve l'indice k tel que x[k] <= u[i] < x[k+1]

        # Recherche l'indice k
        if u[i] < x[0]:
            # Extrapolation à gauche
            k = 0
        elif u[i] > x[n - 1]:
            # Extrapolation à droite
            k = n - 2
        else:
            # Interpolation
            for j in range(n - 1):
                if u[i] < x[j + 1]:
                    k = j
                    break
        # Calcule la pente
        delta = (y[k + 1] - y[k]) / (x[k + 1] - x[k])
        # Evalue l'interpolant
        s = u[i] - x[k]
        v[i] = y[k] + s * delta
    return v


u = np.linspace(-0.25, 5.25, 100)
v = piecewise_linear_naive(x, y, u)
pl.figure()
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.title(u"Piecewise linear interpolation")

# Partie 2 : calcul vectorisé

m = 10
u = np.linspace(-0.25, 5.25, m)
print("u=", u)

delta = np.diff(y) / np.diff(x)
print("delta=", delta)
# Trouve les indices des sous-intervalles k tels que
# x[k] <= u < x[k + 1]
n = np.size(x)
k = np.zeros(np.size(u), dtype=int)
print("k=", k)
for j in range(1, n - 1):
    print("j=", j)
    print("x[j] <= u", x[j] <= u)
    k[x[j] <= u] = j
    print("k=", k)
# Evaluate interpolant
s = u - x[k]
print("s=", s)
v = y[k] + s * delta[k]
print("v=", v)

pl.figure()
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.title(u"Piecewise linear interpolation")

u = np.linspace(-0.25, 5.25, 100)
v = interp.piecewise_linear(x, y, u)
pl.figure()
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.title(u"Piecewise linear interpolation")
