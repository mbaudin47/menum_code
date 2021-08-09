#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Démonstration de la notation de Landau
quand x tend vers l'infini.
"""

import numpy as np
import pylab as pl
import matplotlibpreferences
from fzero import zeroin


matplotlibpreferences.load_preferences()

"""
Landau when x -> +INF
p(x) = 5 x^3 - 6 x^2 + 3
q(x) = 14 x^3
x0=1
"""


def poly_p(x):
    y = 5 * x ** 3 - 6 * x ** 2 + 3
    return y


def poly_q(x):
    y = 14 * x ** 3
    return y


#
x0 = 1.0
x = np.linspace(x0 - 0.5, x0 + 0.5)
p = poly_p(x)
q = poly_q(x)
#
pl.figure(figsize=(2.5, 1.0))
pl.plot(x, p, "-", label="$5 x^3 - 6 x^2 + 3$")
pl.plot(x, q, "--", label="$14 x^3$")
pl.plot([x0, x0], [0.0, poly_q(x0)], "k:")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(r"Notation de Landau quand $x\rightarrow +\infty$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("Landau-x0un.pdf", bbox_inches="tight")

"""
Landau when x -> +INF
p(x) = 5 x^3 - 6 x^2 + 3
q(x) = 5 x^3
x0 = sqrt(2.0) / 2.0
"""


def poly_qmin(x):
    y = 5 * x ** 3
    return y


#
x0 = np.sqrt(2.0) / 2.0
print(u"x0=%.3f" % (x0))
x = np.linspace(x0 - 0.5, x0 + 0.5)
p = poly_p(x)
q = poly_qmin(x)
#
pl.figure(figsize=(2.5, 1.0))
pl.plot(x, p, "-", label="$5 x^3 - 6 x^2 + 3$")
pl.plot(x, q, "--", label="$5 x^3$")
pl.plot([x0, x0], [0.0, poly_qmin(x0)], "k:")
pl.text(x0 + 0.03, poly_qmin(x0) - 1.5, "$x_0$=%.4f" % (x0))
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(r"Notation de Landau quand $x\rightarrow +\infty$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("Landau-x0-exact.pdf", bbox_inches="tight")

"""
Use zeroin in order to compute the solution of the equation p(x0) = q(x0)
"""


def myf(x):
    y = poly_p(x) - poly_q(x)
    return y


x0, history = zeroin(myf, 0.0, 2.0)
print(u"x0=%.4f" % (x0))
#
x = np.linspace(x0 - 2.0, x0 + 2.0)
p = poly_p(x)
q = poly_q(x)
#
pl.figure(figsize=(2.5, 1.0))
pl.plot(x, p, "-", label="$5 x^3 - 6 x^2 + 3$")
pl.plot(x, q, "--", label="$14 x^3$")
pl.plot([x0, x0], [-50.0, poly_q(x0)], "k:")
pl.text(x0 - 1.0, poly_q(x0) + 30.0, "$x_0$=%.4f" % (x0))
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(r"Notation de Landau quand $x\rightarrow +\infty$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("Landau-xmin.pdf", bbox_inches="tight")

"""
Landau when x -> 0
p(x) = 5 x^3 - 6 x^2 + 3
q(x) = 1
delta = 1
M = 14
"""

#
delta = 1.0
M = 14.0
x = np.linspace(-1.3 * delta, 1.3 * delta, 101)
p = np.abs(poly_p(x))
q = M * np.ones_like(x)
#
pl.figure(figsize=(2.5, 1.0))
pl.plot(x, p, "-", label="$|5 x^3 - 6 x^2 + 3|$")
pl.plot(x, q, "--", label="%d" % (M))
pl.plot([-delta, -delta], [0.0, M], "k:")
pl.plot([delta, delta], [0.0, M], "k:")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(r"Notation de Landau quand $x\rightarrow 0$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("Landau-zero.pdf", bbox_inches="tight")
