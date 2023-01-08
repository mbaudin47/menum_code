#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Compare les implémentations naïves et robustes d'une 
formule de différences finies.

Références
----------
Jacques Dumontet. « Algorithme de dérivation numérique : étude théo-
rique et mise en œuvre sur ordinateur ». Thèse de doct. Université de
Béjaia-Abderrahmane Mira, 1973.

J. Dumontet et J. Vignes. « Détermination du pas optimal dans le
calcul des dérivées sur ordinateur ». In : R.A.I.R.O Analyse numérique
11.1 (1977), p. 13-25.

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def f(x):
    return np.sin(x)


def df(x):
    return np.cos(x)


def dff(x):
    return -np.sin(x)


def relative_error(computed, reference):
    # https://nhigham.com/2017/08/14/how-and-how-not-to-compute-a-relative-error/
    return np.abs((computed - reference) / reference)


def absolute_error(computed, reference):
    return np.abs(computed - reference)


# Partie 1: Formule décentrée
def numdiff_forward_no_trick(x, h, f):
    xp = x + h
    approximate_diff = (f(xp) - f(x)) / h
    return approximate_diff


def numdiff_forward_trick(x, h, f):
    xp = x + h
    h_exact = xp - x
    approximate_diff = (f(xp) - f(x)) / h_exact
    return approximate_diff


number_of_steps = 500
h = np.logspace(-1, -12, number_of_steps)
err_with_trick = list()
err_with_no_trick = list()
x = 1e4
for n in range(number_of_steps):
    # 1. No trick
    approximate_diff = numdiff_forward_no_trick(x, h[n], f)
    err_with_no_trick.append(absolute_error(approximate_diff, df(x)))
    # 2. Trick
    approximate_diff = numdiff_forward_trick(x, h[n], f)
    err_with_trick.append(absolute_error(approximate_diff, df(x)))


fig = plt.figure()
plt.plot(h, err_with_trick, "-", label="Astuce magique")
plt.plot(h, err_with_no_trick, ":", label="Sans astuce")
plt.yscale("log")
plt.xscale("log")
plt.xlabel(r"$h$")
plt.ylabel(r"$e_{abs}$")
plt.title(r"Erreur absolue en $x=10^4$ (décentrée)")
plt.legend(bbox_to_anchor=(1.0, 1.0))
fig.set_figwidth(2.0)
fig.set_figheight(1.2)
plt.savefig("astuce-decentree.pdf", bbox_inches="tight")

# Calcul du pas optimal dans ce cas particulier
h_opt = np.sqrt(2.0 * abs(f(x)) * sys.float_info.epsilon / abs(dff(x)))
print("Pas optimal:%.3e" % (h_opt))
e_opt = np.sqrt(2.0 * abs(f(x)) * abs(dff(x)) * sys.float_info.epsilon)
print("Erreur optimale:%.3e" % (e_opt))

# Partie 2 : formule centrée
def numdiff_centered_no_trick(x, h, f):
    xp = x + h
    xm = x - h
    approximate_diff = (f(xp) - f(xm)) / (2.0 * h)
    return approximate_diff


def numdiff_centered_trick(x, h, f):
    xp = x + h
    xm = x - h
    h_exact = xp - xm
    approximate_diff = (f(xp) - f(xm)) / h_exact
    return approximate_diff


number_of_steps = 500
h = np.logspace(-1, -12, number_of_steps)
err_with_trick = list()
err_with_no_trick = list()
x = 1e4
for n in range(number_of_steps):
    # 1. No trick
    approximate_diff = numdiff_centered_no_trick(x, h[n], f)
    err_with_no_trick.append(absolute_error(approximate_diff, df(x)))
    # 2. Trick
    approximate_diff = numdiff_centered_trick(x, h[n], f)
    err_with_trick.append(absolute_error(approximate_diff, df(x)))


fig = plt.figure()
plt.plot(h, err_with_trick, "-", label="Astuce magique")
plt.plot(h, err_with_no_trick, ":", label="Sans astuce")
plt.yscale("log")
plt.xscale("log")
plt.xlabel(r"$h$")
plt.ylabel(r"$e_{abs}$")
plt.title(r"Erreur absolue en $x=10^4$ (centrée)")
plt.legend(bbox_to_anchor=(1.0, 1.0))
fig.set_figwidth(2.0)
fig.set_figheight(1.2)
plt.savefig("astuce-centree.pdf", bbox_inches="tight")
