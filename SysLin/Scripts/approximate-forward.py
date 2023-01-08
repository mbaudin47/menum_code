# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michael Baudin
"""
Test approximate solutions to a linear equation

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from numpy import linspace, array, inf, zeros, pi, cos, sin
from numpy.linalg import norm, cond, inv
import pylab as pl
from numpy.random import uniform

import matplotlibpreferences

matplotlibpreferences.load_preferences()


def get_matrix(i):
    if i == 0:
        A = array([[1.0, -1.0], [1.0, 1.0]])
    #    elif (i==1):
    #        A=array([[1.,-1.],[1.,0.1]])
    #    elif (i==2):
    #        A=array([[1.,-1.],[1.,-0.5]])
    elif i == 1:
        A = array([[1.0, -1.0], [1.0, -0.7]])
    return A


# Points y tels que ||A*y-b||< 1
# où b = A*x.

x1min = -4.0
x1max = 8.0
x2min = -4.0
x2max = 9.0

samplesize = 10000

pl.figure(figsize=(4.0, 1.5))

for i in range(2):
    pl.subplot(1, 2, i + 1)
    A = get_matrix(i)
    #
    pl.title(u"$\kappa_{\infty}=%.2f$" % (cond(A, inf)))
    pl.axis("equal")
    #
    x = array([2.0, 3.0])
    b = A @ x
    print(u"A=")
    print(A)
    print(u"b=")
    print(b)

    #
    # Plot the two lines an their intersection
    x1 = linspace(x1min, x1max)
    pl.plot(x[0], x[1], "g*")
    # Equation #1
    x2 = (b[0] - A[0, 0] * x1) / A[0, 1]
    x2 = array(x2).flatten()
    pl.plot(x1, x2, "-")
    # Equation #2
    x2 = (b[1] - A[1, 0] * x1) / A[1, 1]
    x2 = array(x2).flatten()
    pl.plot(x1, x2, "-")

    #
    # Plot approximate solutions
    if False:
        for j in range(samplesize):
            x1 = uniform(x1min, x1max)
            x2 = uniform(x2min, x2max)
            y = array([x1, x2])
            c = A @ y
            if norm(b - c) < 1.0:
                pl.plot(y[0], y[1], ".")
    #
    # Dessine l'ellipse
    m = 100
    r = 1.0
    t = linspace(0, 2 * pi, m)
    yall = zeros((m, 2))
    # Plot the unit circle
    for j in range(m):
        delta1 = r * cos(t[j])
        delta2 = r * sin(t[j])
        delta = array([delta1, delta2])
        y = x + inv(A) @ delta
        yall[j, 0] = y[0]
        yall[j, 1] = y[1]

    pl.plot(yall[:, 0], yall[:, 1], "-")
    #
    pl.xlabel(u"$x_1$")
    pl.ylabel(u"$x_2$")
    pl.xlim((x1min, x1max))
    pl.ylim((x2min, x2max))
pl.subplots_adjust(wspace=0.3)
pl.savefig("approximate-forward.pdf", bbox_inches="tight")
