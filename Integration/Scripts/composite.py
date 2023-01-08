#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Illustre une méthode d'intégration composite: milieu, trapèze et Simpson 
composite. 
Pour cela, on considère la fonction :
    f(x) = 1 + x ^ 6 + sin(2 * pi * x)

pour x dans [-1, 1].

Références
----------
Cleve Moler. Numerical Computing with Matlab. Society for
Industrial Mathematics, 2004.

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import quadrature
from floats import computeDigits
from interp import polynomial_interpolation


figure_width = 2.0
figure_height = 1.0

def test_f(x):
    alpha = 2.0
    y = 1.0 + x ** 6 + np.sin(alpha * np.pi * x)
    return y


a = -1.0
b = 1.0
exact = 16.0 / 7.0

number_of_points = 200
x = np.linspace(a - 0.1, b + 0.1, number_of_points)
y = [test_f(x[k]) for k in range(number_of_points)]

# Compute function at nodes
number_of_nodes = 7
print("Number of nodes = ", number_of_nodes)
x_nodes = np.linspace(a, b, number_of_nodes)
y_nodes = [test_f(x_nodes[k]) for k in range(number_of_nodes)]

#
# 1. Uses composite midpoint
integral_Mc, fcount_Mc = quadrature.composite_midpoint(test_f, a, b, number_of_nodes)

def plot_composite_midpoint(x, y, x_nodes, integral_Mc, plot_title=True):
    number_of_nodes = len(x_nodes)
    pl.plot(x, y, "--")
    for k in range(number_of_nodes - 1):
        x_midpoint = (x_nodes[k] + x_nodes[k + 1]) / 2.0
        y_midpoint = test_f(x_midpoint)
        pl.plot([x_midpoint], [y_midpoint], "o", color="tab:orange")
        pl.plot([x_nodes[k], x_nodes[k]], [0.0, y_midpoint], ":", color="tab:orange")
        pl.plot(
            [x_nodes[k + 1], x_nodes[k + 1]], [0.0, y_midpoint], ":", color="tab:orange"
        )
        pl.plot(
            [x_nodes[k], x_nodes[k + 1]], [y_midpoint, y_midpoint], "-", color="tab:orange"
        )
    pl.xlabel("$x$")
    pl.ylabel("$y$")
    if plot_title:
        pl.title("Milieu comp. : %.3f" % (integral_Mc))

# Plot composite midpoint
fig = pl.figure(figsize=(figure_width, figure_height))
plot_composite_midpoint(x, y, x_nodes, integral_Mc)
pl.savefig("composite-midpoint.pdf", bbox_inches="tight")

# 2. Uses composite trapezoidal
integral_Tc, fcount_Tc = quadrature.composite_trapezoidal(test_f, a, b, number_of_nodes)

def plot_composite_trapezoidal(x, y, x_nodes, y_nodes, integral_Tc, plot_title=True):
    number_of_nodes = len(x_nodes)
    pl.plot(x, y, "--")
    pl.plot(x_nodes, y_nodes, "o-")
    for k in range(number_of_nodes):
        pl.plot([x_nodes[k], x_nodes[k]], [0.0, y_nodes[k]], ":", color="tab:orange")
    pl.xlabel("$x$")
    pl.ylabel("$y$")
    if plot_title:
        pl.title("Trapèze comp. : %.3f" % (integral_Tc))

# Plot composite trapezoidal
fig = pl.figure(figsize=(figure_width, figure_height))
plot_composite_trapezoidal(x, y, x_nodes, y_nodes, integral_Tc)
pl.savefig("composite-trapezoidal.pdf", bbox_inches="tight")

# 3. Uses composite Simpson
integral_Sc, fcount_Sc = quadrature.composite_simpson(test_f, a, b, number_of_nodes)


def plotsimpson(f, a, b, *args):
    # Plot Simpson's rule.
    c = (a + b) / 2.0
    fa = f(a, *args)
    fb = f(b, *args)
    fc = f(c, *args)
    # Dessine l'approximation
    x = np.linspace(a, b)
    y = polynomial_interpolation([a, c, b], [fa, fc, fb], x)
    pl.plot(x, y, "-", color="tab:orange")
    # pl.plot([a, c, b], [fa, fc, fb], "o")
    return None

def plot_composite_simpson(x, y, x_nodes, y_nodes, integral_Sc, plot_title=True):
    number_of_nodes = len(x_nodes)
    pl.plot(x, y, "--")
    pl.plot(x_nodes, y_nodes, "o", color="tab:orange")
    for k in range(number_of_nodes - 1):
        pl.plot([x_nodes[k], x_nodes[k]], [0.0, y_nodes[k]], ":", color="tab:orange")
        plotsimpson(test_f, x_nodes[k], x_nodes[k + 1])
    pl.xlabel("$x$")
    pl.ylabel("$y$")
    if plot_title:
        pl.title("Simpson comp. : %.3f" % (integral_Sc))

# Plot composite Simpson
fig = pl.figure(figsize=(figure_width, figure_height))
plot_composite_simpson(x, y, x_nodes, y_nodes, integral_Sc)
pl.savefig("composite-Simpson.pdf", bbox_inches="tight")

# 4. Plot digits
digits_Mc = computeDigits(exact, integral_Mc, 10.0)
digits_Tc = computeDigits(exact, integral_Tc, 10.0)
digits_Sc = computeDigits(exact, integral_Sc, 10.0)

print("Integral exact= %.3f" % (exact))
print(
    "Composite Midpoint = %.3f, Digits=%.2f, f_count=%d"
    % (integral_Mc, digits_Mc, fcount_Mc)
)
print(
    "Composite Trapezo. = %.3f, Digits=%.2f, f_count=%d"
    % (integral_Tc, digits_Tc, fcount_Tc)
)
print(
    "Composite Simpson  = %.3f, Digits=%.2f, f_count=%d"
    % (integral_Sc, digits_Sc, fcount_Sc)
)

# 5. Implement composite trapezoidal
n = number_of_nodes
h = (b - a) / (n - 1)
y_sum = test_f(a)
for i in range(1, n - 1):
    xi = a + i * h
    y_sum += 2.0 * test_f(xi)
y_sum += test_f(b)
integral = y_sum * h / 2.0
print("Composite Trapezoidal  = %.3f" % (integral))

# Plot three composite methods
y_min = -0.32
y_max = 2.5
fig = pl.figure(figsize=(5.5, figure_height))
pl.subplot(1, 3, 1)
plot_composite_midpoint(x, y, x_nodes, integral_Mc, False)
pl.ylim(y_min, y_max)
pl.subplot(1, 3, 2)
plot_composite_trapezoidal(x, y, x_nodes, y_nodes, integral_Tc, False)
pl.ylim(y_min, y_max)
pl.subplot(1, 3, 3)
plot_composite_simpson(x, y, x_nodes, y_nodes, integral_Sc, False)
pl.ylim(y_min, y_max)
pl.suptitle("Méthodes composites : M.C.=%.3f, T.C.=%.3f, S.C.=%.3f" % (
    integral_Mc, integral_Tc, integral_Sc))
pl.subplots_adjust(top=0.8, wspace=0.3)
pl.savefig("composite-trois_methodes.pdf", bbox_inches="tight")
