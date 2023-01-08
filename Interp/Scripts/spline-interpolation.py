#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Interpolation de la fonction sinus par une spline cubique par morceaux. 
On considère la fonction f(x) = sin(x) pour tout x.
On souhaite observer l'influence du comportement de la fonction, 
en particulier l'effet de la courbure locale de la fonction sur la précision 
de l'interpolation.

Cas 1  : on utilise 7 points régulièrement répartis dans l'intervalle [0, 6].
Cela correspond à un écart égal à Delta = 1 entre chaque point.
On affiche l'équation formelle de la spline en fonction de la variable 
locale s.

Cas 2  : on utilise 7 points régulièrement répartis dans l'intervalle [0, 12].
Cela correspond à un écart égal à Delta = 2 entre chaque point.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import pylab as pl
import interp
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# Part 1 : on a small interval

# Compute points to interpolate
n_interpolation = 7
delta_x = 1.0
x = np.array([k * delta_x for k in range(n_interpolation)])
y = np.sin(x)

# Compute f
npoints = 100
xmin = x[0] - 0.25
xmax = x[-1] + 0.25
x_data = np.linspace(xmin, xmax, npoints)
y_data = np.sin(x_data)

# Draw f and the points
pl.figure(figsize=(5, 4))
pl.plot(x_data, y_data, "--")
pl.plot(x, y, "ko")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.legend(["Fonction", "Données"])
pl.title(u"Des données à interpoler.")

nu = 100
u = np.linspace(xmin, xmax, nu)
v = interp.spline_interpolation(x, y, u)
pl.figure(figsize=(1.2, 1.0))
pl.plot(x_data, y_data, "--")
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
# pl.xlim(right=10.0)
# pl.ylim(top=1.5)
pl.ylim(top=1.5, bottom=-1.5)
#pl.legend(["Fonction", "Données", "Spline"], bbox_to_anchor=(1.0, 1.0))
pl.title(u"Spline naturelle")
pl.savefig("spline-interpolation-deltax-%.0f.pdf" % (delta_x), bbox_inches="tight")

# Calcule les coefficients de la spline
#  First derivatives
h = np.diff(x)
delta = np.diff(y) / h
d = interp.spline_slopes_natural(h, delta)
#  Piecewise polynomial coefficients
n = np.size(x)
c = (3 * delta - 2 * d[0 : n - 1] - d[1:n]) / h
b = (d[0 : n - 1] - 2 * delta + d[1:n]) / h ** 2
for k in range(n_interpolation - 1):
    print(
        "P%d = %.4f + s * (%.4f + s * (%.4f + s * %.4f))" % (k, y[k], d[k], c[k], b[k])
    )

# Part 2 : On a larger interval

# Compute points to interpolate
n_interpolation = 7
delta_x = 2.0  # Increase delta_x to enlage the interval
x = np.array([k * delta_x for k in range(n_interpolation)])
y = np.sin(x)

# Compute f
npoints = 100
xmin = x[0] - 0.25
xmax = x[-1] + 0.25
x_data = np.linspace(xmin, xmax, npoints)
y_data = np.sin(x_data)

nu = 100
u = np.linspace(xmin, xmax, nu)
v = interp.spline_interpolation(x, y, u)
pl.figure(figsize=(1.2, 1.0))
pl.plot(x_data, y_data, "--")
pl.plot(x, y, "o")
pl.plot(u, v, "-")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.xlim(right=15.0)
pl.ylim(top=1.5, bottom=-1.5)
pl.legend(["Fonction", "Données", "Spline"], bbox_to_anchor=(1.0, 1.0))
pl.title(u"Spline naturelle")
pl.savefig("spline-interpolation-deltax-%.0f.pdf" % (delta_x), bbox_inches="tight")
