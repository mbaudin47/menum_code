#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Démontre le théorème de Rolle appliqué à la fonction :

    f(x) = sin(x) * (1 - x ^ 2)
    
entre 0 et 1.
"""

import numpy as np
import pylab as pl
from fzero import zeroin
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def func(x):
    y = np.sin(x) * (1 - x ** 2)
    return y


x = np.linspace(-0.2, 1.2, 100)
y = func(x)
z = np.zeros_like(x)


def mygradient(x):
    y = np.cos(x) * (1 - x ** 2) - 2 * x * np.sin(x)
    return y


xi, history = zeroin(mygradient, 0.0, 1.0)

pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-", label="$(1-x^2)\sin(x)$")
pl.plot(x, z, "-")
pl.plot([-0.0, 1.0], [0.0, 0.0], "o")
pl.plot([xi], [func(xi)], "o")
pl.text(xi - 0.1, func(xi) + 0.2, r"$\xi=%.4f$" % (xi))
pl.ylim(top=1.0)
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"Théorème de Rolle")
pl.legend(bbox_to_anchor=(2.0, 1.0))
pl.savefig("Rolle.pdf", bbox_inches="tight")
