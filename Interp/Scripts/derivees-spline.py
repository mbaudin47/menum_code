#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine la spline cubique et ses dérivées. 
On considère la fonction f(x) = sin(x) pour x dans [0, 12]. 
On considère 7 points régulièrement répartis dans l'intervalle [0, 12], 
ce qui mène à une distance Delta x = 2 entre chaque noeud. 
On dessine la spline interpolante P(x), ainsi que P'(x), P''(x) et P'''(x). 
On observe que P'''(x) est constante par morceaux.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import pylab as pl
import interp
import matplotlibpreferences


def DrawSplineDerivatives(
    x,
    y,
    u,
    siderule="natural",
    figure_width=4.0,
    figure_height=4.0,
    plot_data=True,
    fig=None,
):
    """
    Dessine la spline et ses dérivées.

    Parameters
    ----------
    x : a numpy array with n entries,
        the x observations
    y : a numpy array with n entries,
        the y observations
    u : a numpy array with m entries,
        the evaluation points
    siderule : a string, "natural" for a
        natural spline, or "not-a-knot" for
        a smoother spline
    figure_height : int
        The height of the figure.
    figure_width : int
        The width of the figure.
    plot_data: bool
        If True, plot the data.
    Returns
    -------
    None.
    """
    # Calcule les coefficients de la spline
    #  First derivatives
    h = np.diff(x)
    delta = np.diff(y) / h
    if siderule == "not-a-knot":
        spline_type = "not-a-knot"
        d = interp.spline_slopes_not_a_knot(h, delta)
    else:
        spline_type = "naturelle"
        d = interp.spline_slopes_natural(h, delta)

    #  Piecewise polynomial coefficients
    n = np.size(x)
    c = (3 * delta - 2 * d[0 : n - 1] - d[1:n]) / h
    b = (d[0 : n - 1] - 2 * delta + d[1:n]) / h ** 2

    #  Find subinterval indices k
    # so that x(k) <= u < x(k+1)
    k = np.zeros(np.size(u), dtype=int)
    for j in range(1, n - 1):
        k[x[j] <= u] = j

    #  Evaluate spline and its derivatives
    s = u - x[k]
    v = y[k] + s * (d[k] + s * (c[k] + s * b[k]))
    v1 = d[k] + s * (2.0 * c[k] + 3.0 * s * b[k])
    v2 = 2.0 * c[k] + 6.0 * s * b[k]
    v3 = 6.0 * b[k]

    if fig is None:
        fig = pl.figure()
    #
    pl.subplot(4, 1, 1)
    if plot_data:
        pl.plot(x, y, "o", color="tab:red")
    pl.plot(u, v, "-", color="tab:blue")
    pl.tick_params(axis='x', bottom=False, labelbottom=False)
    pl.xlabel(u"")
    pl.ylabel(u"$P(x)$")
    pl.title(u"Spline %s" % (spline_type))
    #
    pl.subplot(4, 1, 2)
    pl.plot(u, v1, "-", color="tab:blue")
    pl.xlabel(u"")
    pl.tick_params(axis='x', bottom=False, labelbottom=False)
    pl.ylabel(u"$P'(x)$")
    #
    pl.subplot(4, 1, 3)
    pl.plot(u, v2, "-", color="tab:blue")
    pl.xlabel(u"")
    pl.tick_params(axis='x', bottom=False, labelbottom=False)
    pl.ylabel(u"$P''(x)$")
    #
    pl.subplot(4, 1, 4)
    pl.plot(u, v3, "-", color="tab:blue")
    pl.xlabel(u"$x$")
    pl.ylabel(u"$P'''(x)$")
    fig.set_figwidth(figure_width)
    fig.set_figheight(figure_height)
    pl.tight_layout()
    return fig


def SetAxesForMySpline(ax, bottom=-1.8, top=1.8):
    """
    Configure the axes of the spline.

    Parameters
    ----------
    ax : matplotlib.ax
        The axes to set.

    Returns
    -------
    None.
    """
    for i in range(len(ax)):
        ax[i].xaxis.set_major_locator(pl.MaxNLocator(4))
        ax[i].set_ylim(bottom=bottom, top=top)
    return


matplotlibpreferences.load_preferences()

figure_width=2.0
figure_height=2.7
hspace = 0.1

# Compute points to interpolate
n_interpolation = 7
delta_x = 2.0
x = np.array([k * delta_x for k in range(n_interpolation)])
y = np.sin(x)

# Compute the function values
npoints = 100
xmin = x[0] - 0.25
xmax = x[-1] + 0.25
x_data = np.linspace(xmin, xmax, npoints)
y_data = np.sin(x_data)

# 1. Draw the natural spline and its derivatives
fig = DrawSplineDerivatives(
    x,
    y,
    x_data,
    siderule="natural",
    figure_width=figure_width,
    figure_height=figure_height,
)
# Ajoute la fonction à approcher
ax = fig.get_axes()
ax[0].plot(x_data, y_data, "--", color="tab:orange")
ax[0].legend(["Données", "Spline", "$f$"], loc="upper right", bbox_to_anchor=(2.0, 1.2))
SetAxesForMySpline(fig.get_axes())
pl.subplots_adjust(hspace=hspace)
pl.savefig("derivees-spline-natural.pdf", bbox_inches="tight")

# 2. Draw the not-a-knot spline and its derivatives
fig = DrawSplineDerivatives(
    x,
    y,
    x_data,
    siderule="not-a-knot",
    figure_width=figure_width,
    figure_height=figure_height,
)
# Ajoute la fonction à approcher
ax = fig.get_axes()
ax[0].plot(x_data, y_data, "--", color="tab:orange")
ax[0].legend(["Données", "Spline", "$f$"], loc="upper right", bbox_to_anchor=(2.0, 1.2))
SetAxesForMySpline(fig.get_axes())
pl.subplots_adjust(hspace=hspace)
pl.savefig("derivees-spline-notaknot.pdf", bbox_inches="tight")

# 3. Draw the natural spline and its derivatives (no function value)
fig = DrawSplineDerivatives(
    x,
    y,
    x_data,
    siderule="natural",
    plot_data=False,
    figure_width=figure_width,
    figure_height=figure_height,
)
SetAxesForMySpline(fig.get_axes(), bottom=-1.5, top=1.5)
pl.subplots_adjust(hspace=hspace)
pl.savefig("derivees-spline-raw.pdf", bbox_inches="tight")
