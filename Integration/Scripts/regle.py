#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Draw the four rules of numerical integration.
"""
from numpy import linspace, vander, sin
from numpy.linalg import solve
import pylab as pl
from quadrature import (
    adaptsim,
    midpoint_rule,
    trapezoidal_rule,
    simpson_rule,
    compositesimpson_rule,
    boole_rule,
)
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def myfunc(x):
    y = sin(2.5 * x) ** 2
    return y


def plotfunc(f, a, b, *args):
    x = linspace(a, b, 100)
    y = f(x, *args)
    pl.plot(x, y, "--")
    return


def plotmidpoint(f, a, b, *args):
    # Plot midpoint rule.
    # Dessine l'approximation
    c = (a + b) / 2
    fc = f(c, *args)
    pl.plot([a, b], [fc, fc], "-")
    pl.plot(c, fc, "o")
    I, fcount = midpoint_rule(f, a, b, *args)
    pl.title(u"Point milieu : %.4f" % (I))
    return I


def plottrapezoidal(f, a, b, *args):
    # Plot trapezoidal rule.
    # Dessine l'approximation
    fa = f(a, *args)
    fb = f(b, *args)
    pl.plot([a, b], [fa, fb], "-")
    pl.plot([a, b], [fa, fb], "o")
    I, fcount = trapezoidal_rule(f, a, b, *args)
    pl.title(u"Trapèze : %.4f" % (I))
    return I


def plotsimpson(f, a, b, *args):
    # Plot Simpson's rule.
    c = (a + b) / 2.0
    fa = f(a, *args)
    fb = f(b, *args)
    fc = f(c, *args)
    # Calcule le polynôme
    A = vander([a, c, b])
    coeffs = solve(A, [fa, fc, fb])
    # Dessine l'approximation
    x = linspace(a, b)
    y = coeffs[0] * x ** 2 + coeffs[1] * x + coeffs[2]
    pl.plot(x, y, "-")
    pl.plot([a, c, b], [fa, fc, fb], "o")
    I, fcount = simpson_rule(f, a, b, *args)
    pl.title(u"Simpson : %.4f" % (I))
    return I


def plotcompositesimpson(f, a, b, *args):
    # Plot composite Simpson's rule.
    c = (a + b) / 2.0
    plotsimpson(f, a, c, *args)
    plotsimpson(f, c, b, *args)
    I, fcount = compositesimpson_rule(f, a, b, *args)
    pl.title(u"Simpson $S_2$ : %.4f" % (I))
    return I


def plotBoole(f, a, b, *args):
    # Plot Boole's rule.
    # Calcule le polynôme
    c = (a + b) / 2
    d = (a + c) / 2
    e = (c + b) / 2
    fa = f(a, *args)
    fb = f(b, *args)
    fc = f(c, *args)
    fd = f(d, *args)
    fe = f(e, *args)
    A = vander([a, d, c, e, b])
    coeffs = solve(A, [fa, fd, fc, fe, fb])
    # Dessine l'approximation
    x = linspace(a, b)
    y = (
        coeffs[0] * x ** 4
        + coeffs[1] * x ** 3
        + coeffs[2] * x ** 2
        + coeffs[3] * x ** 1
        + coeffs[4]
    )
    pl.plot(x, y, "-")
    pl.plot([a, d, c, e, b], [fa, fd, fc, fe, fb], "o")
    I, fcount = boole_rule(f, a, b, *args)
    pl.title(u"Boole : %.4f" % (I))
    """
    Verification : integrale du polynôme interpolant
    Pa=coeffs[0]*a**5/5.+coeffs[1]*a**4/4.+coeffs[2]*a**3/3.+coeffs[3]*a**2/2.+coeffs[4]*a
    Pb=coeffs[0]*b**5/5.+coeffs[1]*b**4/4.+coeffs[2]*b**3/3.+coeffs[3]*b**2/2.+coeffs[4]*b
    I=Pb-Pa
    """
    return I


def configureplot(a, b):
    pl.xlim([-0.1, 1.1])
    pl.ylim([-0.1, 1.1])
    pl.xlabel(u"x")
    pl.ylabel(u"f(x)")
    return


#
save = True
#
a = 0.0
b = 1.0
width = 1.5
height = 1.0
#
pl.figure(figsize=(width, height))
plotfunc(myfunc, a, b)
I = plotmidpoint(myfunc, a, b)
configureplot(a, b)
print(u"Règle du milieu:", I)
if save:
    pl.savefig("regle-milieu.pdf", bbox_inches="tight")

#
pl.figure(figsize=(width, height))
plotfunc(myfunc, a, b)
I = plottrapezoidal(myfunc, a, b)
configureplot(a, b)
print(u"Règle du trapèze:", I)
if save:
    pl.savefig("regle-trapeze.pdf", bbox_inches="tight")

#
pl.figure(figsize=(width, height))
plotfunc(myfunc, a, b)
I = plotsimpson(myfunc, a, b)
configureplot(a, b)
print(u"Règle de Simpson:", I)
if save:
    pl.savefig("regle-Simpson.pdf", bbox_inches="tight")

#
pl.figure(figsize=(width, height))
plotfunc(myfunc, a, b)
I = plotcompositesimpson(myfunc, a, b)
configureplot(a, b)
print(u"Règle de Simpson composite S2:", I)
if save:
    pl.savefig("regle-composite-Simpson-S2.pdf", bbox_inches="tight")

#
pl.figure(figsize=(width, height))
plotfunc(myfunc, a, b)
I = plotBoole(myfunc, a, b)
configureplot(a, b)
print(u"Règle de Boole:", I)
if save:
    pl.savefig("regle-Boole.pdf", bbox_inches="tight")

exacte = (5.0 - sin(5.0)) / 10.0
print(u"Exacte:", exacte)
I, fcount = adaptsim(myfunc, a, b)
print(u"Quadtx:", I, " fcount=", fcount, "Erreur absolue=", abs(exacte - I))
I, fcount = midpoint_rule(myfunc, a, b)
print(u"Milieu:", I, " fcount=", fcount, "Erreur absolue=", abs(exacte - I))
I, fcount = trapezoidal_rule(myfunc, a, b)
print(u"Trapeze:", I, " fcount=", fcount, "Erreur absolue=", abs(exacte - I))
I, fcount = simpson_rule(myfunc, a, b)
print(u"Simpson:", I, " fcount=", fcount, "Erreur absolue=", abs(exacte - I))
I, fcount = compositesimpson_rule(myfunc, a, b)
print(u"Simpson Composite:", I, " fcount=", fcount, "Erreur absolue=", abs(exacte - I))
I, fcount = boole_rule(myfunc, a, b)
print(u"Boole:", I, " fcount=", fcount, "Erreur absolue=", abs(exacte - I))
