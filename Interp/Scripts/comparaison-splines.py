#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Compare la spline naturelle et la spline not-a-knot. 
On considère la fonction f(x) = sin(x) pour x dans [0, 2pi]. 
On considère 4 noeuds d'interpolation. 
On interpole les données par une spline naturelle et par une spline 
not-a-knot.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import pylab as pl
from interp import spline_interpolation
import matplotlibpreferences


matplotlibpreferences.load_preferences()

# Part 1 : on a small interval

# Compute points to interpolate
n_interpolation = 4
delta_x = 2.0
x = np.linspace(0.0, 2.0 * np.pi, n_interpolation)
y = np.sin(x)

# Compute f
npoints = 100
xmin = x[0] - 0.25
xmax = x[-1] + 0.25
x_data = np.linspace(xmin, xmax, npoints)
y_data = np.sin(x_data)

#
nu = 100
u = np.linspace(xmin, xmax, nu)
fig = pl.figure()
pl.plot(x_data, y_data, "--")
pl.plot(x, y, "o")
v = spline_interpolation(x, y, u, siderule="natural")
pl.plot(u, v, "-")
v = spline_interpolation(x, y, u, siderule="not-a-knot")
pl.plot(u, v, "-.")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.legend(["Fonction", "Données", "Naturelle", "Not-a-knot"], bbox_to_anchor=(1.0, 1.1))
pl.title(u"Interpolation par spline")
fig.set_figwidth(2.0)
fig.set_figheight(1.0)
pl.ylim(top=1.5)
pl.savefig("comparaison-splines.pdf", bbox_inches="tight")
