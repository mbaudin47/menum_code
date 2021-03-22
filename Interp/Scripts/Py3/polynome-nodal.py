#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Dessine le polynôme nodal. 
C'est le polynôme 

w(x) = (x - x1) * (x - x2) * ... * (x - xn)

pour tout x dans [-1, 1], où x1, x2, ..., xn sont les noeuds d'interpolation.
On considère des noeuds sur une grille régulière dans [-1, 1]. 
On observe le polynôme nodal avec n=3, n=4, n=5 et n=6.
"""

import numpy as np
import pylab as pl
import matplotlibpreferences


def ComputeNodalPolynomial(x, x_nodes):
    """
    Calcule le polynôme nodal.

    Parameters
    ----------
    x : float
        Le point où évaluer le polynôme nodal.
    x_nodes : list of floats
        La liste des noeuds.

    Returns
    -------
    y : float
        La valeur du polynôme nodal.
    """
    n_nodes = len(x_nodes)
    y = 1.0
    for i in range(n_nodes):
        y *= x - x_nodes[i]
    return y


def PlotNodalPolynomial(n_nodes, n_points=100):
    """
    Dessine le polynôme nodal.

    Parameters
    ----------
    n_nodes : int
        Le nombre de noeuds.
    n_points : int
        Le nombre de points pour dessiner la fonction.

    Returns
    -------
    fig : matplotlib.figure
        La figure.
    """
    # Define points for plot and nodes
    x = np.linspace(-1.0, 1.0, n_points)
    x_nodes = np.linspace(-1.0, 1.0, n_nodes)
    y = [ComputeNodalPolynomial(x[i], x_nodes) for i in range(n_points)]

    # Figure 1 : 3 noeuds
    pl.plot(x_nodes, np.zeros((n_nodes,)), "o")
    pl.plot(x, y, "-")
    pl.xlabel(u"x")
    pl.ylabel(r"$\omega_%d(x)$" % (n_nodes))
    pl.title(u"n=%d" % (n_nodes))
    pl.ylim(-0.5, 0.5)
    return


matplotlibpreferences.load_preferences()

#
fig = pl.figure(figsize=(3.0, 2.5))
ax = pl.subplot(2, 2, 1)
PlotNodalPolynomial(3)
ax = pl.subplot(2, 2, 2)
PlotNodalPolynomial(4)
ax = pl.subplot(2, 2, 3)
PlotNodalPolynomial(5)
ax = pl.subplot(2, 2, 4)
PlotNodalPolynomial(6)
ax = fig.get_axes()
for i in range(len(ax)):
    ax[i].yaxis.set_major_locator(pl.MaxNLocator(3))
fig.tight_layout()
pl.subplots_adjust(hspace=1.2, wspace=0.9)
pl.savefig("polynome-nodal.pdf", bbox_inches="tight")
