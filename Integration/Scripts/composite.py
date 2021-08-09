#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Illustre une méthode d'intégration composite: milieu, trapèze et Simpson 
composite. 
Pour cela, on considère la fonction :
    f(x) = 1 + x ^ 6 + sin(2 * pi * x)

pour x dans [-1, 1].
"""
import numpy as np
import pylab as pl
import quadrature
from floats import computeDigits


def test_f(x):
    alpha = 2.0
    y = 1.0 + x ** 6 + np.sin(alpha * np.pi * x)
    return y


a = -1.0
b = 1.0
exact = 16.0 / 7.0

number_of_nodes = 200
x = np.linspace(a - 0.1, b + 0.1, number_of_nodes)
y = [test_f(x[k]) for k in range(number_of_nodes)]

# Compute function at nodes
number_of_nodes = 10
x_nodes = np.linspace(a, b, number_of_nodes)
y_nodes = [test_f(x_nodes[k]) for k in range(number_of_nodes)]

# Uses composite midpoint
integral_Mc, fcount_Mc = quadrature.composite_midpoint(test_f, a, b, number_of_nodes)

# Plot composite midpoint
fig = pl.figure(figsize=(4.0, 1.5))
pl.plot(x, y, "--")
for k in range(number_of_nodes - 1):
    x_midpoint = (x_nodes[k] + x_nodes[k + 1]) / 2.0
    y_midpoint = test_f(x_midpoint)
    pl.plot([x_midpoint], [y_midpoint], "bo", color="tab:orange")
    pl.plot([x_nodes[k], x_nodes[k]], [0.0, y_midpoint], ":", color="tab:orange")
    pl.plot(
        [x_nodes[k + 1], x_nodes[k + 1]], [0.0, y_midpoint], ":", color="tab:orange"
    )
    pl.plot(
        [x_nodes[k], x_nodes[k + 1]], [y_midpoint, y_midpoint], "-", color="tab:orange"
    )
pl.xlabel("x")
pl.ylabel("y")
pl.title("Méthode du milieu composite : %.3f" % (integral_Mc))
pl.grid()
pl.savefig("composite-midpoint.pdf", bbox_inches="tight")

# Uses composite trapezoidal
integral_Tc, fcount_Tc = quadrature.composite_trapezoidal(test_f, a, b, number_of_nodes)

# Plot composite trapezoidal
fig = pl.figure(figsize=(4.0, 1.5))
pl.plot(x, y, "--")
pl.plot(x_nodes, y_nodes, "o-")
for k in range(number_of_nodes):
    pl.plot([x_nodes[k], x_nodes[k]], [0.0, y_nodes[k]], ":", color="tab:orange")
pl.xlabel("x")
pl.ylabel("y")
pl.title("Méthode du trapèze composite : %.3f" % (integral_Tc))
pl.grid()
pl.savefig("composite-trapezoidal.pdf", bbox_inches="tight")

# Uses composite Simpson
integral_Sc, fcount_Sc = quadrature.composite_simpson(test_f, a, b, number_of_nodes)


def plotsimpson(f, a, b, *args):
    # Plot Simpson's rule.
    c = (a + b) / 2.0
    fa = f(a, *args)
    fb = f(b, *args)
    fc = f(c, *args)
    # Calcule le polynôme
    A = np.vander([a, c, b])
    coeffs = np.linalg.solve(A, [fa, fc, fb])
    # Dessine l'approximation
    x = np.linspace(a, b)
    y = coeffs[0] * x ** 2 + coeffs[1] * x + coeffs[2]
    pl.plot(x, y, "-", color="tab:orange")
    # pl.plot([a, c, b], [fa, fc, fb], "o")
    return None


# Plot composite Simpson
fig = pl.figure(figsize=(4.0, 1.5))
pl.plot(x, y, "--")
pl.plot(x_nodes, y_nodes, "o", color="tab:orange")
for k in range(number_of_nodes - 1):
    pl.plot([x_nodes[k], x_nodes[k]], [0.0, y_nodes[k]], ":", color="tab:orange")
    plotsimpson(test_f, x_nodes[k], x_nodes[k + 1])
pl.xlabel("x")
pl.ylabel("y")
pl.title("Méthode de Simpson composite : %.3f" % (integral_Sc))
pl.grid()
pl.savefig("composite-Simpson.pdf", bbox_inches="tight")

# Plot digits
digits_Mc = computeDigits(exact, integral_Mc, 10.0)
digits_Tc = computeDigits(exact, integral_Tc, 10.0)
digits_Sc = computeDigits(exact, integral_Sc, 10.0)

print("Integral exact= %.3f" % (exact))
print(
    "Composite Midpoint = %.3f, Digits=%.2f, f_count=%d"
    % (integral_Mc, digits_Mc, fcount_Mc)
)
print(
    "Composite Trapezoidal = %.3f, Digits=%.2f, f_count=%d"
    % (integral_Tc, digits_Tc, fcount_Tc)
)
print(
    "Composite Simpson = %.3f, Digits=%.2f, f_count=%d"
    % (integral_Sc, digits_Sc, fcount_Sc)
)
