#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin


import numpy as np
import interp
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

#
# Discrete data
#
#
# 1. Trapezoidal rule
print(u"")
print(u"1. Trapezoidal rule")
x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5])
print(u"x=", x)
# y = np.sin(x)
y = np.array([0.0, 0.4794, 0.8415, 0.9975, 0.9093, 0.5985])
print(u"y=", y)

# -cos(2.5) + cos(0)
exact = 1.801143615546933715
T = sum(np.diff(x) * (y[0:-1] + y[1:]) / 2.0)
error_T = abs(T - exact)
print(u"T=%.3f (error = %.3e)" % (T, error_T))

#
# 2. Spline correction
print(u"")
print(u"2. Spline correction")
h = np.diff(x)
delta = np.diff(y) / h
d = interp.spline_slopes_not_a_knot(h, delta)
D = sum(h ** 2 * (d[1:] - d[0:-1]) / 12.0)
print(u"D=", D)
S = T - D
error_S = abs(S - exact)
print(u"S=%.3f (error = %.3e)" % (S, error_S))

fig = pl.figure(figsize=(2.0, 1.0))
u = np.linspace(-0.5, 3.0)
v = interp.spline_interpolation(x, y, u)
pl.title(u"Intégration de données discrètes.")
pl.plot(x, y, "o")
pl.plot(x, y, "-", label="Trapèze : T = %.3f" % (T))
pl.plot(u, v, "--", label="Spline : S = %.3f" % (S))
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.savefig("discrete.pdf", bbox_inches="tight")
