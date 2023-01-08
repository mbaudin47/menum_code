#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Analyse la performance de la quadrature adaptative sur la fonction de 
Runge :

    f(x) = 1 / (1 + 25 * x ^ 2)

pour x dans [-1, 1].

Pour cela, on observe l'erreur absolue en fonction du nombre d'appels 
à la fonction f. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import quadrature
from floats import computeDigits
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def runge(x):
    y = 1.0 / (1.0 + 25.0 * x ** 2)
    return y


#
# 1. Integrate the Runge function
print(u"")
print(u"1. Integrate the Runge function")
Q, fcount = quadrature.adaptsim_gui(runge, -1.0, 1.0, 1.0e-3)
_ = pl.title(u"Adaptatif : %.4f." % (Q))
figure = pl.gcf()
figure.set_figwidth(1.5)
figure.set_figheight(1.0)
pl.xlabel("$x$")
pl.ylabel("$y$")
pl.savefig("performance-integration-Runge.pdf", bbox_inches="tight")

# Calcule l'erreur
exact = 2.0 / 5.0 * np.arctan(5.0)
print(u"exact=", exact)
print(u"Q=", Q)
digits = computeDigits(exact, Q, 10)
print(u"Digits=", digits)
print(u"fcount=", fcount)

#
# 2. See convergence

print(u"2. See convergence")
nombre_pas = 50
err_quadadapt = np.zeros(nombre_pas)
fcount_quadadapt = np.zeros(nombre_pas)
print(u"Tol, Fcount, Error, Ratio:")
atol = 1.0
for k in range(nombre_pas):
    atol /= 2.0
    # Adaptive quadrature
    Q, fcount_quadadapt[k] = quadrature.adaptsim(runge, -1.0, 1.0, atol)
    err_quadadapt[k] = abs(Q - exact)
    ratio = err_quadadapt[k] / atol
    print(
        u"%8.0e %7d %13.3e %9.3f" % (atol, fcount_quadadapt[k], err_quadadapt[k], ratio)
    )

# Make a plot
fig = pl.figure(figsize=(1.5, 1.2))
pl.plot(fcount_quadadapt, err_quadadapt, "-")
pl.xlabel(u"Nombre d'appels à $f$")
pl.ylabel(u"Erreur absolue")
pl.xscale("log")
pl.yscale("log")
pl.title(u"Convergence")
pl.savefig("performance-erreur-absolue-integration-Runge.pdf", bbox_inches="tight")

# Composite trapezoidal
nombre_pas = 12
err_comptrap = np.zeros(nombre_pas)
fcount_comptrap = np.zeros(nombre_pas)
n = 1
for k in range(nombre_pas):
    n *= 2
    Q, fcount = quadrature.composite_trapezoidal(runge, -1.0, 1.0, n)
    fcount_comptrap[k] = fcount
    err_comptrap[k] = abs(Q - exact)

# Composite Simpson
nombre_pas = 12
err_compsimpson = np.zeros(nombre_pas)
fcount_compsimpson = np.zeros(nombre_pas)
n = 1
for k in range(nombre_pas):
    n *= 2
    Q, fcount = quadrature.composite_simpson(runge, -1.0, 1.0, n)
    fcount_compsimpson[k] = fcount
    err_compsimpson[k] = abs(Q - exact)

# Plot both errors
fig = pl.figure(figsize=(1.5, 1.0))
pl.plot(fcount_quadadapt, err_quadadapt, "-", label=("Adapt."))
pl.plot(fcount_comptrap, err_comptrap, "--", label="T.C.")
pl.plot(fcount_compsimpson, err_compsimpson, ":", label="S.C.")
pl.legend(bbox_to_anchor=(1.0, 1.0, 0.0, 0.0))
pl.xscale("log")
pl.yscale("log")
pl.xlabel(u"Nombre d'appels à $f$")
pl.ylabel(u"Erreur absolue")
pl.ylim(1.0e-16, 1.0e0)
pl.savefig("performance-err-abs-Runge-adapt-vs-composite.pdf", bbox_inches="tight")
