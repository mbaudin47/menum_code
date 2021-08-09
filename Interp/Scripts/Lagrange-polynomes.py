#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
On considère l'intervalle [-1,1]. 
On utilise n points equidistants.
On en deduit les n polynomes de Lagrange, tels que 

Li(xj)= 1 si i=j, 
        0 sinon.

Evalue la constante de Lebesgue, qui apparaît dans l'analyse du 
conditionnement du polynôme interpolant.

Références
Annales Mathematicae et Informaticae, 33 (2006) pp. 109–123
Lebesgue constants in polynomial interpolation, Simon J. Smith

Turetskii, A. H., The bounding of polynomials prescribed at equally distributed
points, Proc. Pedag. Inst. Vitebsk Vol. 3 (1940), 117–127 (in Russian).
"""

import numpy as np
import pylab as pl
import math
import matplotlibpreferences


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


matplotlibpreferences.load_preferences()

fig = pl.figure(figsize=(2.0, 1.0))
n = 4
nx = 1000
nodes = np.linspace(-1, 1, n)
pl.plot(nodes, np.zeros((n, 1)), "o")
x = np.linspace(-1.1, 1.1, nx)
#
y = lagrange(x, 0, nodes)
pl.plot(x, y, "-", label=r"$L_1$")
y = lagrange(x, 1, nodes)
pl.plot(x, y, "--", label=r"$L_2$")
y = lagrange(x, 2, nodes)
pl.plot(x, y, "-.", label=r"$L_3$")
y = lagrange(x, 3, nodes)
pl.plot(x, y, ":", label=r"$L_4$")
pl.legend(bbox_to_anchor=(1.05, 1))
pl.xlabel(u"x")
pl.title(u"Polynômes de Lagrange (n=%d)." % (n))
pl.savefig("Lagrange-polynome.pdf", bbox_inches="tight")

# 2. Evalue la constante de Lebesgue, pour x dans [-1,1]
# par force brute
def lebesgueConstant(nodes, nx):
    """
    Evalue la constante de Lebesgue, pour nx valeurs régulièrement
    réparties dans l'intervalle [a,b], avec a=nodes[0] et b=nodes[n-1].
    Utilise un algorithme de force brute.

    Parametres
    nodes : un tableau de doubles de taille n, les noeuds d'interpolation
    nx : un entier, le nombre de points où evaluer la fonction
    """
    n = np.size(nodes)
    x = np.linspace(nodes[0], nodes[-1], nx)
    y = np.zeros((n, nx))
    for i in range(n):
        y[i, 0:nx] = lagrange(x, i, nodes)
    L = max(sum(abs(y), axis=0))
    return L


# Le calcul est long : enregistre les valeurs
nmax = 80
if False:
    L = np.zeros((nmax - 2, 1))
    for n in range(2, nmax):
        nodes = np.linspace(-1, 1, n)
        nx = 1000 * n
        L[n - 2] = lebesgueConstant(nodes, nx)
        print(u"n=%d, d=%d, L=%e" % (n, n - 1, L[n - 2]))
        # print "%d & %.3f\\\\" % (n,L)

# Valeur théorique exacte de la constante de Lebesgue.
# Source
# Annales Mathematicae et Informaticae, 33 (2006) pp. 109–123
# Lebesgue constants in polynomial interpolation, Simon J. Smith
#
# Turetskii, A. H., The bounding of polynomials prescribed at equally distributed
# points, Proc. Pedag. Inst. Vitebsk Vol. 3 (1940), 117–127 (in Russian).
n = 1.0 * np.arange(2, nmax)
lbound = 2 ** n / (math.e * n * np.log(n))
fig = pl.figure(figsize=(2.2, 1.2))
pl.plot(n, lbound, "-")
pl.xlabel(u"n")
pl.ylabel(r"$\Lambda_n$")
pl.yscale("log")
pl.title(u"Constante de Lebesgue.")
pl.savefig("Lagrange-polynome-Lebesgue-constantasymp.pdf", bbox_inches="tight")


def lebesgueFunction(nodes, x):
    """
    Evalue la fonction de Lebesgue aux points x.

    Parametres
    nodes : un tableau de doubles de taille n, les noeuds d'interpolation
    x : un tableau de doubles de taille nx, les points où evaluer la fonction
    """
    n = np.size(nodes)
    y = np.zeros((n, nx))
    for i in range(n):
        y[i, 0:nx] = lagrange(x, i, nodes)
    y = np.sum(abs(y), axis=0)
    return y


n = 5
a = -1
b = 1
nodes = np.linspace(a, b, n)
nx = 100 * n
x = np.linspace(a, b, nx)
y = lebesgueFunction(nodes, x)
fig = pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(r"$\lambda_%d(x)$" % (n))
pl.title(u"Fonction de Lebesgue (n=%d)." % (n))
pl.savefig("Lagrange-polynome-Lebesgue-fonction.pdf", bbox_inches="tight")
