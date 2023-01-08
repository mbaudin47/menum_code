#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Analyse les polynômes interpolants de Lagrange.

On considère l'intervalle [-1,1]. 
On utilise n points equidistants.
On en deduit les n polynomes de Lagrange, tels que 

Li(xj)= 1 si i=j, 
        0 sinon.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import pylab as pl
from quadrature import composite_trapezoidal
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def lagrange(x, i, nodes):
    """
    Retourne la valeur du i-ème polynôme de Lagrange
    au point x, pour les noeuds donnés dans nodes.

    Paramètres
    x : un double, le point
    i : un entier, l'indice du polynôme avec i dans {0,1,...,n-1}
    nodes : un tableau de taille n, les noeuds d'interpolation
      Le tableau doit être trié par ordre croissant :
        nodes[0] < nodes[1] < ... < nodes[n-1]
    y : un double, la valeur du polynôme de Lagrange en x
    """
    n = np.size(nodes)
    nx = np.size(x)
    nodei = nodes[i]  # Extrait l'élément i
    nodes = np.delete(nodes, i)  # Retire l'élément i
    repx = np.tile(x, (n - 1, 1))
    repnodes = np.tile(nodes, (nx, 1))
    repnodes = np.transpose(repnodes)
    p = np.prod(repx - repnodes, axis=0)
    q = np.prod(nodei - repnodes, axis=0)
    y = p / q
    return y


def integrand(t, i, nodes):
    a = nodes[0]
    b = nodes[-1]
    h = b - a
    x = a + h * t
    y = lagrange(x, i, nodes)
    return y


n = 2
nodes = np.linspace(-1, 1, n)
pl.figure()
pl.plot(nodes, np.zeros((n, 1)), "bo")
pl.xlabel(u"x")
pl.title(u"Noeuds - n =%d" % (n))
#
np.set_printoptions(precision=4)
a = 0.0
b = 1.0
tol = 1.0e-10
nombre_noeuds = 1000


def quadrature_sans_faille(f, a, b, tol, nombre_noeuds, *args):
    # Q, fcount = adaptsim(integrand, a, b, tol, *args)
    # Parfois, la quadrature est attrapée par les zéros de Lagrange !
    Q, fcount = composite_trapezoidal(integrand, a, b, nombre_noeuds, *args)
    return Q


# Calcule la somme des poids par
# intégrale de Lk entre -1 et 1
nmax = 10
weights_table = np.zeros((nmax, nmax))
for n in range(1, nmax):
    nodes = np.linspace(-1, 1, n)
    weights = np.zeros((1, n))
    for polyindex in range(n):
        Q = quadrature_sans_faille(
            integrand, a, b, tol, nombre_noeuds, polyindex, nodes
        )
        weights_table[n - 1, polyindex] = Q
    print(u"n=%d, %s" % (n, weights_table[n - 1, 0:n]))

# Calcule la somme des poids par
# intégrale de Lk entre -1 et 1
nmax = 20
wmin = np.zeros((nmax - 1, 1))
wmax = np.zeros((nmax - 1, 1))
s = np.zeros((nmax - 1, 1))

weights_table = np.zeros((nmax, nmax))
for n in range(1, nmax):
    print(u"n=", n)
    nodes = np.linspace(-1, 1, n)
    weights = np.zeros((1, n))
    for polyindex in range(n):
        Q = quadrature_sans_faille(
            integrand, a, b, tol, nombre_noeuds, polyindex, nodes
        )
        weights[0, polyindex] = Q
    # print weights
    weightmin = weights.min(axis=1)
    wmin[n - 1] = weightmin[0]
    weightmax = weights.max(axis=1)
    wmax[n - 1] = weightmax[0]
    aw = abs(weights)
    weightssum = aw.sum(axis=1)
    s[n - 1] = weightssum[0]
    print(u"%d & %.4f & %.4f & %.4f \\\\" % (n, wmin[n - 1], wmax[n - 1], s[n - 1]))

narray = range(1, nmax)
pl.figure(figsize=(2.0, 1.0))
pl.plot(narray, s, "o")
pl.ylim(0.0, 200.0)
pl.ylabel(u"$\sum_{k=1}^n |u_k|$")
pl.xlabel(u"$n$")
# pl.title(u"Somme des valeurs absolues des poids réduits.")
pl.savefig("Newton-Cotes-calculpoids.pdf", bbox_inches="tight")
