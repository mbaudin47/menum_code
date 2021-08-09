#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Plot convergence of four rules of numerical integration depending on the 
interval length.
"""
import numpy as np
import pylab as pl
from quadrature import (
    midpoint_rule,
    trapezoidal_rule,
    simpson_rule,
    compositesimpson_rule,
    boole_rule,
)
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def myfunc(x):
    y = np.sin(2.5 * x) ** 2
    return y


h = 1.0
tol = 1.0e-20
a = 0.0
npoints = 200
h = np.logspace(0, -10, npoints)
errorMidpoint = np.zeros((npoints))
errorTrapezoidal = np.zeros((npoints))
errorSimpson = np.zeros((npoints))
errorCompositeSimpson = np.zeros((npoints))
errorBoole = np.zeros((npoints))
for i in range(npoints):
    b = a + h[i]
    exacte = (5.0 * h[i] - np.sin(5.0 * h[i])) / 10.0
    #
    I, fcount = midpoint_rule(myfunc, a, b)
    errorMidpoint[i] = abs(exacte - I)
    #
    I, fcount = trapezoidal_rule(myfunc, a, b)
    errorTrapezoidal[i] = abs(exacte - I)
    #
    I, fcount = simpson_rule(myfunc, a, b)
    errorSimpson[i] = abs(exacte - I)
    #
    I, fcount = compositesimpson_rule(myfunc, a, b)
    errorCompositeSimpson[i] = abs(exacte - I)
    #
    I, fcount = boole_rule(myfunc, a, b)
    errorBoole[i] = abs(exacte - I)

# Set NaN to avoid zeros (for log scale)
# errorMidpoint[errorMidpoint==0.0] = np.nan
# errorSimpson[errorSimpson==0.0] = np.nan
# errorCompositeSimpson[errorCompositeSimpson==0.0] = np.nan
# errorTrapezoidal[errorTrapezoidal==0.0] = np.nan
# errorBoole[errorBoole==0.0] = np.nan

pl.figure(figsize=(2.5, 1.5))
if False:
    pl.plot(h, h ** 3, "k-", label="h**3")
    pl.plot(h, h ** 5, "k-", label="h**5")
    pl.plot(h, h ** 7, "k-", label="h**7")
    pl.ylim([1.0e-26, 1.0e-2])
pl.plot(h, errorMidpoint, "-", label="Milieu")
pl.plot(h, errorTrapezoidal, "--", label="Trapèze")
pl.plot(h, errorSimpson, "-.", label="Simpson")
pl.plot(h, errorCompositeSimpson, ":", label="Simpson $S_2$")
pl.plot(h, errorBoole, "-", label="Boole")
pl.legend(bbox_to_anchor=(1.0, 1.0, 0.0, 0.0))
pl.xscale("log")
pl.yscale("log")
pl.xlabel(u"h")
pl.ylabel(u"Erreur absolue")
pl.savefig("integration-convergence.pdf", bbox_inches="tight")
