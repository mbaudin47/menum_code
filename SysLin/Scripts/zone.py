#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Dessine des zones approchées dans lesquelles se trouvent la plupart des 
solutions d'un système d'équations perturbées. 

Partie 1 : On perturbe le second membre et on dessine les 
points y tels que ||A * y - b||< 1 où b = A * x.

Partie 2 : On perturbe le second membre. 
Dessine les points y tels que A * y = b + delta
où delta est aléatoire uniforme : delta ~ U(-0.5,0.5). 

Partie 3 : On perturbe la matrice A. 
Dessine les points y tels que
(A + E) * y = b
où E est aléatoire uniforme E ~ U(-0.5,0.5). 

Test approximate solutions to a linear equation.
"""

from numpy import array, linspace, inf
from numpy.linalg import solve, norm, cond
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


######################################################
# Partie 1
#
# Points y tels que ||A*y-b||< 1
# où b = A*x.

x1min = -4.0
x1max = 8.0
x2min = -4.0
x2max = 9.0

samplesize = 100

pl.figure()

for i in range(2):
    pl.subplot(1, 2, i + 1)
    A = get_matrix(i)
    #
    pl.title(u"K=%.2f" % (cond(A, inf)))
    pl.axis("equal")
    #
    x = array([2.0, 3.0])
    b = A @ x
    print(u"A=")
    print(A)
    print(u"b=")
    print(b)
    x = solve(A, b)
    print(u"solve(A,b)=")
    print(x)
    #
    # Plot the two lines an their intersection
    x1 = linspace(x1min, x1max)
    pl.plot(x[0], x[1], "g*")
    # Equation #1
    x2 = (b[0] - A[0, 0] * x1) / A[0, 1]
    x2 = array(x2).flatten()
    pl.plot(x1, x2, "r-")
    # Equation #2
    x2 = (b[1] - A[1, 0] * x1) / A[1, 1]
    x2 = array(x2).flatten()
    pl.plot(x1, x2, "b-")
    #
    # Plot approximate solutions
    for j in range(samplesize * 10):
        x1 = uniform(x1min, x1max)
        x2 = uniform(x2min, x2max)
        y = array([[x1], [x2]])
        c = A @ y
        if norm(b - c) < 1.0:
            pl.plot(y[0], y[1], "r.")
    #
    pl.xlabel(u"$x_1$")
    pl.ylabel(u"$x_2$")
    pl.xlim((x1min, x1max))
    pl.ylim((x2min, x2max))

######################################################
# Partie 2
#
# Dessine les points y tels que
# A*y=b+delta
# où delta est aléatoire uniforme :
# delta ~ U(-0.5,0.5)

pl.figure(figsize=(4.0, 1.5))

for i in range(2):
    pl.subplot(1, 2, i + 1)
    A = get_matrix(i)
    #
    pl.title(u"Perturb. de b, K=%.2f" % (cond(A, inf)))
    pl.axis("equal")
    #
    x = array([2.0, 3.0])
    b = A @ x
    print(u"A=")
    print(A)
    print(u"b=")
    print(b)
    x = solve(A, b)
    print(u"solve(A,b)=")
    print(x)
    #
    # Plot the two lines an their intersection
    x1 = linspace(x1min, x1max)
    pl.plot(x[0], x[1], "*")
    # Equation #1
    x2 = (b[0] - A[0, 0] * x1) / A[0, 1]
    x2 = array(x2).flatten()
    pl.plot(x1, x2, "-")
    # Equation #2
    x2 = (b[1] - A[1, 0] * x1) / A[1, 1]
    x2 = array(x2).flatten()
    pl.plot(x1, x2, "-")
    #
    # Plot exact solutions of perturbed problems
    for j in range(samplesize):
        delta = uniform(-0.5, 0.5, 2)
        bdelta = b + delta
        y = solve(A, bdelta)
        pl.plot(y[0], y[1], ".", color="tab:green")
    #
    pl.xlabel(u"$x_1$")
    pl.ylabel(u"$x_2$")
    pl.xlim((x1min, x1max))
    pl.ylim((x2min, x2max))

pl.subplots_adjust(wspace=0.3)
pl.savefig("zone-b.pdf", bbox_inches="tight")

######################################################
# Partie 3
#

# Dessine les points y tels que
# (A+E)*y=b
# où E est aléatoire uniforme :
# E ~ U(-0.5,0.5)

pl.figure(figsize=(4.0, 1.5))

for i in range(2):
    pl.subplot(1, 2, i + 1)
    A = get_matrix(i)
    #
    pl.title(u"Perturb. de A, K=%.2f" % (cond(A, inf)))
    pl.axis("equal")
    #
    # Compute the solution
    x = array([2.0, 3.0])
    b = A @ x
    print(u"A=")
    print(A)
    print(u"b=")
    print(b)
    x = solve(A, b)
    print(u"solve(A,b)=")
    print(x)
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
    pl.plot(x1, x2, "--")
    #
    # Plot exact solutions of perturbed problems
    for j in range(samplesize):
        E = uniform(-0.1, 0.1, 4).reshape(2, 2)
        y = solve(A + E, b)
        pl.plot(y[0], y[1], ".", color="tab:green")

    pl.xlabel(u"$x_1$")
    pl.ylabel(u"$x_2$")
    pl.xlim((x1min, x1max))
    pl.ylim((x2min, x2max))
pl.subplots_adjust(wspace=0.3)
pl.savefig("zone-A.pdf", bbox_inches="tight")
