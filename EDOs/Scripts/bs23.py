#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Analyse le contrôle de l'erreur par l'algorithme de Bogacki-Shampine (2, 3).

Référence
Cleve Moler. Numerical Computing with Matlab. Society for
Industrial Mathematics, 2004.
p.192

David F. Griffiths et Desmond J. Higham. Numerical Methods 
for ODEs. Springer, 2010.
p.20 and p.149.

Walter Gautschi. Numerical Analysis, Second Edition. Birkhäuser, 2012.
p.359
"""

import numpy as np
from odes import bogacki_shampine, explicit_method
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

# The following example is from (Griffiths, Higham, 2010), p.20
def f(y, t):
    ydot = np.array([(1.0 - 2.0 * t) * y[0]])
    return ydot


y0 = [1.0]
tspan = [0.0, 4.0]
t = tspan[1]

# Plot exact solution
t = np.linspace(tspan[0], tspan[1], 100)
yexact = np.exp(0.25 - (0.5 - t) ** 2)
pl.figure(figsize=(2.5, 1.0))
pl.plot(t, yexact)
pl.xlabel("t")
pl.ylabel("y")
pl.title("Solution exacte.")
pl.savefig("bs23-exact.pdf", pad_inches=0.05, bbox_inches="tight")

# Approximate solution by Ralston
h = 1.0e-1
tout, yout = explicit_method("ralston", f, tspan, y0, h)

# Calcul de l'erreur
n_time_steps = len(tout)
print("Nombre de pas de temps : ", n_time_steps)
absolute_error = np.zeros(n_time_steps)
for i in range(n_time_steps):
    yexact_i = np.exp(0.25 - (0.5 - tout[i]) ** 2)
    absolute_error[i] = np.abs(yexact_i - yout[i, 0])

# Erreur absolue
pl.figure(figsize=(2.5, 1.0))
pl.plot(tout, absolute_error, "-+")
pl.xlabel("Temps (s)")
pl.ylabel("Erreur absolue.")
pl.yscale("log")
pl.title("Méthode de Ralston. h = %.1e" % (h))

# Approximate solution by Bogacki-Shampine(2,3)
atol = 1.0e-4
tout, yout = bogacki_shampine(f, tspan, y0, atol=atol, verbose=False)

# Plot t, y(t)
pl.figure(figsize=(2.0, 1.0))
pl.plot(t, yexact, label="Exacte.")
pl.plot(tout, yout[:, 0], label="Approx.")
pl.xlabel("t")
pl.ylabel("y")
pl.legend(bbox_to_anchor=(1.0, 1.0, 0.0, 0.0))
pl.savefig("bs23-approx.pdf", pad_inches=0.05, bbox_inches="tight")

# Calcul de l'erreur
n_time_steps = len(tout)
print("Nombre de pas de temps : ", n_time_steps)
absolute_error = np.zeros(n_time_steps)
for i in range(n_time_steps):
    yexact_i = np.exp(0.25 - (0.5 - tout[i]) ** 2)
    absolute_error[i] = np.abs(yexact_i - yout[i, 0])

# Erreur absolue
pl.figure(figsize=(2.5, 1.0))
pl.plot(tout, absolute_error, "-+")
pl.xlabel("Temps (s)")
pl.ylabel("Erreur absolue")
pl.yscale("log")
pl.title("BS23. Tol. abs. = %.1e" % (atol))
pl.savefig("bs23-err-abs.pdf", pad_inches=0.05, bbox_inches="tight")

# Calcul de la longueur du pas
step_length = np.diff(tout)

# Longueur du pas
pl.figure(figsize=(2.5, 1.5))
pl.plot(tout[0:-1], step_length, "-+")
pl.xlabel("Temps (s)")
pl.ylabel("$h_n$")
pl.title("BS23. Tol. abs. = %.1e" % (atol))
pl.tight_layout()
pl.savefig("bs23-step-len.pdf", pad_inches=0.05, bbox_inches="tight")
