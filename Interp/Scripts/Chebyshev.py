#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Analyse les polynômes de Chebyshev.
Dessine les polynômes de degré 0 à 4. 
Dessine les racines et les extremas du polynôme de Chebyshev de degré 8.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import interp
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

number_of_data_points = 8
number_of_points = 100

# Plot polynomial and roots
xk = interp.compute_Chebyshev_roots(number_of_data_points)
print("xk=", xk)

x = np.linspace(-1.0, 1.0, number_of_points)
y = interp.compute_Chebyshev_polynomial(number_of_data_points, x)

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(xk, np.zeros(number_of_data_points), "o", label="Roots")
pl.plot(x, y, "-", label="Chebyshev")
pl.title("Polynôme de Chebyshev")
pl.savefig("Chebyshev-roots.pdf", bbox_inches="tight")

# Plot extremas
xk_prime = interp.compute_Chebyshev_extremas(number_of_data_points)

print("xk'=", xk_prime)
yk_prime = interp.compute_Chebyshev_polynomial(number_of_data_points, xk_prime)

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(xk_prime, yk_prime, "o", label="Extremas")
pl.plot(x, y, "-", label="Chebyshev")
pl.title("Polynôme de Chebyshev")
pl.savefig("Chebyshev-extremas.pdf", bbox_inches="tight")

# Print
for k in range(number_of_data_points):
    print("| %d | %.4f | %.4f |" % (k, xk[k], xk_prime[k]))

# Plot the roots on the circle
number_of_points = 100  # Number of points on the circle
number_of_roots = 8  # Number of Chebyshev roots
delta_x = -0.05  # Horizontal offset for root labels
delta_y = -0.15  # Vertical offset for root labels
theta = np.linspace(0.0, np.pi, number_of_points)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
cheby_theta = np.arccos(interp.compute_Chebyshev_roots(number_of_roots))
cheby_x = np.cos(cheby_theta)
cheby_y = np.sin(cheby_theta)
pl.figure(figsize=(3.0, 2.0))
pl.plot(cheby_x, np.zeros(number_of_roots), "o")
pl.plot(circle_x, circle_y, "-")
pl.plot(cheby_x, cheby_y, "o")
for index in range(number_of_roots):
    theta = cheby_theta[index]
    pl.text(np.cos(theta) + delta_x, delta_y, "$x_%d$" % (index))
    pl.plot([0.0, np.cos(theta)], [0.0, np.sin(theta)], "-", color="tab:purple")
    pl.plot([np.cos(theta), np.cos(theta)], [0.0, np.sin(theta)], "--", color="tab:red")
pl.axis([-1.2, 1.2, -0.5, 1.5])
pl.axis("equal")
pl.savefig("Chebyshev-circle.pdf", bbox_inches="tight")

# Plot the 5 first Chebyshev polynomials
pl.figure(figsize=(2.5, 1.5))
lines_style_list = ["-", ":", "--", "-.", "-"]
x = np.linspace(-1.0, 1.0, 100)
for n in range(5):
    y = interp.compute_Chebyshev_polynomial(n, x)
    pl.plot(x, y, lines_style_list[n], label="$T_{%d}$" % (n))
pl.xlabel("$x$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.title("Polynômes de Chebyshev")
pl.savefig("Chebyshev-premiers.pdf", bbox_inches="tight")
