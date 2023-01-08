#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
On considère une table de 5 points et on compare l'interpolation et 
l'ajustement polynomial par un polynôme de degré 1.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
from interp import polynomial_interpolation
from leastsq import polynomial_fit_normal_equations, polynomial_value
import matplotlibpreferences


matplotlibpreferences.load_preferences()

x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.1, 0.6, 2.1, 3.3, 3.9])

# Interpolation
u = np.linspace(-0.25, 4.25)
v_interpolation = polynomial_interpolation(x, y, u)

# Ajustement
beta = polynomial_fit_normal_equations(x, y, 1)
v_moindrescarres = polynomial_value(beta, u)

# Number of points where to interpolate
fig = pl.figure(figsize=(2.0, 1.2))
pl.plot(x, y, "o")
pl.plot(u, v_interpolation, "-", label="Interpolation")
pl.plot(u, v_moindrescarres, "--", label="Ajustement")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("interpolation-ajustement.pdf", bbox_inches="tight")
