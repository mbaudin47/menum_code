# Copyright (C) 2013 - 2023 - Michael Baudin
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Etude du comportement du pas optimal et de l'erreur absolue optimale en 
fonction du degré d et de l'ordre de précision p.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import pylab as pl
import numpy as np
import sys
import matplotlibpreferences
from matplotlib.ticker import MaxNLocator

matplotlibpreferences.load_preferences()

eps = sys.float_info.epsilon

styles = ["-", "--", ".-", ":", "+-"]

# Etude du pas optimal
pl.figure(figsize=(4.0, 1.2))
ax = pl.subplot(1, 2, 1)
pl.title(u"Pas optimal")
pl.xlabel(u"$p$")
pl.ylabel(u"$h^\star$")
index = 0
list_of_derivative_orders = range(1, 10, 2)
for d in list_of_derivative_orders:
    p = np.array([float(i) for i in range(1, 10)])
    h = eps ** (1.0 / (d + p))
    pl.plot(p, h, styles[index], label="$d=%d$" % (d))
    index += 1
pl.yscale("log")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#pl.legend(bbox_to_anchor=(1.0, 1.0))
# Etude de l'erreur absolue optimale
#pl.figure(figsize=(2.0, 1.2))
ax = pl.subplot(1, 2, 2)
pl.title(u"Erreur optimale")
pl.xlabel(u"$p$")
pl.ylabel(u"$e_{abs}^\star$")
index = 0
for d in list_of_derivative_orders:
    p = np.array([float(i) for i in range(1, 10)])
    e = eps ** (p / (d + p))
    pl.plot(p, e, styles[index], label="$d=%d$" % (d))
    index += 1
pl.yscale("log")
pl.legend(bbox_to_anchor=(1.0, 1.0))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
pl.subplots_adjust(wspace=0.6)
pl.savefig("precision-degre-eabs.pdf", bbox_inches="tight")

# Etude du terme multiplicatif de epsilon
fig = pl.figure(figsize=(1.5, 1.0))
pl.title(
    u"Sensibilité de $\\frac{d + p}{p} \\left(\\frac{p}{d}\\right)^{\\frac{d}{d+p}}$"
)
pl.xlabel(u"$p$")
pl.ylabel(u"$y$")
index = 0
for d in range(1, 10, 2):
    p = np.array([float(i) for i in range(1, 10)])
    e = ((d + p) / d) * (p / d) ** (d / (d + p))
    pl.plot(p, e, styles[index], label="$d=%d$" % (d))
    index += 1
ax = fig.get_axes()[0]
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("precision-degre-facteur.pdf", bbox_inches="tight")
