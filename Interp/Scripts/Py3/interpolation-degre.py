#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre comment approcher une table de valeurs par un polynôme de 
degré constant par morceau, linéaire par morceau ou un polynôme 
global.
Calcule l'erreur absolue entre la fonction et son interpolant lorsqu'on 
utilise une interpolation linéaire par morceaux.
Calcule l'erreur absolue entre la fonction et son interpolant lorsqu'on 
utilise une interpolation polynomiale globale associée aux noeuds 
de Chebyshev.
"""
import numpy as np
import pylab as pl
import interp
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def SetAxesForMyGraph(fig):
    """
    Configure the axes of the spline.

    Parameters
    ----------
    fig : matplotlib.figure
        The figure to set.

    Returns
    -------
    None.
    """
    ax = fig.get_axes()
    for i in range(len(ax)):
        ax[i].xaxis.set_major_locator(pl.MaxNLocator(4))
        ax[i].set_xlim(left=-0.5, right=6.5)
        ax[i].set_ylim(bottom=-1.2, top=1.2)
    return


step = 1.0
x = np.arange(0.0, 7.0, step)
number_of_data_points = len(x)
y = np.sin(x)
for i in range(number_of_data_points):
    print(u"x=%.1f, y=%.4f" % (x[i], y[i]))

figure_width = 2.0
figure_height = 1.0

# Figure 1
fig = pl.figure(figsize=(figure_width, figure_height))
pl.plot(x, y, "o")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"Données.")
SetAxesForMyGraph(fig)
pl.savefig("interpolation-degre-donnees.pdf", bbox_inches="tight")

# Figure 2 : interpolation constante
fig = pl.figure(figsize=(figure_width, figure_height))
pl.plot(x, y, "o")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"Interpolation constante par morceaux.")
delta = step / 2.0
for i in range(number_of_data_points):
    pl.plot([x[i] - delta, x[i] + delta], [y[i], y[i]], "-", color="tab:orange")
SetAxesForMyGraph(fig)
pl.savefig("interpolation-degre-constante.pdf", bbox_inches="tight")

# Figure 2 : interpolation linéaire
nu = 100
u = np.linspace(-0.25, 6.25, nu)
v = interp.piecewise_linear(x, y, u)

fig = pl.figure(figsize=(figure_width, figure_height))
pl.plot(x, y, "o")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"Interpolation linéaire par morceaux.")
delta = step / 2.0
pl.plot(u, v, "-", color="tab:orange")
SetAxesForMyGraph(fig)
pl.savefig("interpolation-degre-lineaire.pdf", bbox_inches="tight")

# Figure 3 : interpolation polynomiale
nu = 100
u = np.linspace(-0.25, 6.25, nu)
v = interp.polynomial_interpolation(x, y, u)

fig = pl.figure(figsize=(figure_width, figure_height))
pl.plot(x, y, "o")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"Interpolation polynomiale (globale).")
delta = step / 2.0
pl.plot(u, v, "-", color="tab:orange")
SetAxesForMyGraph(fig)
pl.savefig("interpolation-degre-polynomiale.pdf", bbox_inches="tight")

# Affiche les coefficients du polynôme interpolant
A = np.vander(x)
c = np.linalg.solve(A, y)
for i in range(6):
    print(u"c(%d)=%.3e" % (i, c[i]))

# Erreur de l'interpolation linéaire
nu = 201
u = np.linspace(0.0, 6.0, nu)
v = interp.piecewise_linear(x, y, u)
error_piecewise = np.abs(v - np.sin(u))
v = interp.polynomial_interpolation(x, y, u)
error_global = np.abs(v - np.sin(u))

fig = pl.figure(figsize=(figure_width, figure_height))
pl.plot(u, error_piecewise, "-", label="Lin.p.m.")
pl.plot(u, error_global, "--", label="Polynôme")
pl.xlabel(u"x")
pl.ylabel(u"Erreur abs.")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("interpolation-degre-erreur.pdf", bbox_inches="tight")

# Chebyshev roots
a = 0.0
b = 6.0
# 1. Equidistant points
x = np.linspace(a, b, number_of_data_points)
nu = 201
u = np.linspace(0.0, 6.0, nu)
v = interp.polynomial_interpolation(x, y, u)
error_piecewise = np.abs(v - np.sin(u))
# 2. Chebyshev points
x = interp.compute_Chebyshev_roots(number_of_data_points, a, b)
y = np.sin(x)
v = interp.polynomial_interpolation(x, y, u)
error_global = np.abs(v - np.sin(u))

fig = pl.figure(figsize=(figure_width, figure_height))
pl.plot(u, error_piecewise, "-", label="Equidistant")
pl.plot(u, error_global, "--", label="Chebyshev")
pl.xlabel(u"x")
pl.ylabel(u"Erreur abs.")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("interpolation-degre-Chebyshev-erreur.pdf", bbox_inches="tight")
