#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
L'erreur d'interpolation est 

f(x) = Pn(x) + (x - x1) * (x - x2) * ... * (x - xn) * f(n)(xi) / n!,

pour tout x dans [x1,xn], 
où Pn(x) est le polynôme interpolant de Lagrange et
xi est un réel dans [x1,xn].

Donc l'erreur dépend du polynôme nodal de degré n, défini par :

wn(x) = (x-x1)*(x-x2)*...*(x-xn)

Comment varie cette fonction pour x dans [x1,xn] ?
On considère la norme infinie de cette fonction :
    Wn = max_{x dans [-1,1]} |wn(x)|
    
et on estime Wn pour n = 3 à n = 50. 
Pour cela, on évalue le polynôme nodal sur une grille régulière de m points, 
avec m = 1000 * n et la valeur de Wn est approchée par le maximum 
de la valeur absolue de la fonction wn(x) sur la grille.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import pylab as pl
from math import factorial
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def CalculePolynomeNodal(x, nodes):
    """
    Evalue la fonction
        wn(x) = (x-nodes[0])*(x-nodes[1])*...*(x-nodes[n-1])

    Paramètres
    x : un tableau de doubles, de taille nx, les points où évaluer g
    nodes : un tableau de doubles, de taille n, les noeuds d'interpolation
    y : un tableau de doubles, de taille nx, la valeur de g aux points x
    """
    nx = np.size(x)
    n = np.size(nodes)
    repx = np.tile(x, (n, 1))
    repnodes = np.tile(nodes, (nx, 1))
    repnodes = np.transpose(repnodes)
    y = np.prod(repx - repnodes, axis=0)
    return y


def DessinePolynomeNodal(n, a, b, plotxlabel=True, plotylabel=True):
    """
    Dessine la fonction wn pour n noeuds entre a et b

    Paramètres
    n : un entier, le nombre de noeuds d'interpolation
    a : un double, la borne minimale
    b : un double, la borne maximale
    """
    nodes = np.linspace(a, b, n)  # Points d'interpolation : x1,...,xn
    nx = 1000 * n  # Nombre de points pour évaluer wn
    x = np.linspace(a, b, nx)  # Calcul de la fonction wn
    y = CalculePolynomeNodal(x, nodes)
    pl.plot(nodes, np.zeros((n, 1)), "bo")
    pl.plot(x, y, "r-")
    pl.ylim(-0.4, 0.4)
    if plotxlabel:
        pl.xlabel(u"x")
    if plotylabel:
        pl.ylabel(u"wn(x)")
    pl.title(u"n=%d" % (n))
    return None


# 2. Evalue le maximum de wn, pour x dans [-1,1]
# par force brute.
a = -1.0  # Bornes
b = 1.0
nmin = 3
nmax = 50
ymax = np.zeros(nmax - nmin + 1)
pmax = np.zeros(nmax - nmin + 1)
for n in range(nmin, nmax + 1):
    nodes = np.linspace(a, b, n)  # Points d'interpolation : x1,...,xn
    h = (b - a) / (n - 1)
    nx = 1000 * n  # Nombre de points pour évaluer wn
    x = np.linspace(a, b, nx)  # Calcul de la fonction wn
    y = CalculePolynomeNodal(x, nodes)
    ymax[n - nmin] = max(y)
    pmax[n - nmin] = h ** n * factorial(n - 1) / 4
    # print "%d %e %e\n" % (n,ymax[n-1],pmax[n-1])

fig = pl.figure(figsize=(2.0, 1.2))
pl.plot(range(nmin, nmax + 1), ymax, "-", label=r"$\widetilde{W}_n$")
pl.plot(range(nmin, nmax + 1), pmax, "-", label="Borne sup.")
pl.yscale("log")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"$n$")
pl.savefig("erreur-interpolation.pdf", bbox_inches="tight")
