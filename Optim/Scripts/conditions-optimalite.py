#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Plusieurs types de minimums :
    - Exemple A : un minimum fort global, un minimum fort local,
    - Exemple B : un minimum faible local.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import pylab as pl
from optim import goldensectiongui

import matplotlibpreferences


matplotlibpreferences.load_preferences()

# Example A
def example_A(x):
    y = np.sin(x) + 0.05 * x ** 2
    return y

n_points = 100
x = np.linspace(-10.0, 10.0, n_points)
y = example_A(x)


pl.figure()
reltolx = 1.0e-8
xopt_1, fopt_1 = goldensectiongui(example_A, -5.0, 1.0, reltolx)
print(u"xopt_1=", xopt_1)
print(u"fopt_1=", fopt_1)

pl.figure()
reltolx = 1.0e-8
xopt_2, fopt_2 = goldensectiongui(example_A, 2.0, 8.0, reltolx)
print(u"xopt_2=", xopt_2)
print(u"fopt_2=", fopt_2)

pl.figure()
reltolx = 1.0e-8
xopt_3, fopt_3 = goldensectiongui(example_A, -10.0, -6.0, reltolx)
print(u"xopt_3=", xopt_3)
print(u"fopt_3=", fopt_3)

#
pl.figure(figsize=(1.5, 0.5))
pl.plot(x, y)
pl.plot(xopt_1, fopt_1, "o", label="Global")
pl.plot(xopt_2, fopt_2, "+", label="Local")
pl.xlabel("$x$")
pl.ylabel("$y$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.ylim(-2.0, 5.5)
pl.savefig("conditions-optimalite-A.pdf", bbox_inches="tight")

# Example B
def example_B(x):
    y = 1.0
    return y

n_points = 100
x = np.linspace(-1.0, 1.0, n_points)
y = np.zeros(n_points)
for i in range(n_points):
    y[i] = example_B(x[i])

#
pl.figure(figsize=(1.5, 1.0))
pl.plot(x, y)
pl.plot([0.0], [1.0], "o", label="Local faible")
pl.xlabel("$x$")
pl.ylabel("$y$")
pl.ylim(0.4, 1.6)
pl.legend(bbox_to_anchor=(2.2, 1.0))
pl.savefig("conditions-optimalite-B.pdf", bbox_inches="tight")
