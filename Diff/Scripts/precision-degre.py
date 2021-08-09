# Copyright (C) 2013 - 2021 - Michael Baudin
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Etude du comportement du pas optimal et de l'erreur absolue optimale en 
fonction du degré d et de l'ordre de précision p.
"""
import pylab as pl
import numpy as np
import sys
import matplotlibpreferences


matplotlibpreferences.load_preferences()

eps = sys.float_info.epsilon

styles = ["-", "--", ".-", ":", "+-"]

# Etude du pas optimal
pl.figure(figsize=(2.0, 1.2))
pl.title(u"Sensibilité du pas optimal.")
pl.xlabel(u"p")
pl.ylabel(u"$h^\star$")
index = 0
for d in range(1, 10, 2):
    p = np.array([float(i) for i in range(1, 10)])
    h = eps ** (1.0 / (d + p))
    pl.plot(p, h, styles[index], label="d=%d" % (d))
    index += 1
pl.yscale("log")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("precision-degre-hopt.pdf", bbox_inches="tight")

# Etude de l'erreur absolue optimale
pl.figure(figsize=(2.0, 1.2))
pl.title(u"Sensibilité de l'erreur optimale.")
pl.xlabel(u"p")
pl.ylabel(u"$e_{abs}^\star$")
index = 0
for d in range(1, 10, 2):
    p = np.array([float(i) for i in range(1, 10)])
    e = eps ** (p / (d + p))
    pl.plot(p, e, styles[index], label="d=%d" % (d))
    index += 1
pl.yscale("log")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("precision-degre-eabs.pdf", bbox_inches="tight")

# Etude du terme multiplicatif de epsilon
pl.figure(figsize=(2.0, 1.0))
pl.title(
    u"Sensibilité de $\\frac{d + p}{p} \\left(\\frac{p}{d}\\right)^{\\frac{d}{d+p}}$."
)
pl.xlabel(u"p")
pl.ylabel(u"y")
index = 0
for d in range(1, 10, 2):
    p = np.array([float(i) for i in range(1, 10)])
    e = ((d + p) / d) * (p / d) ** (d / (d + p))
    pl.plot(p, e, styles[index], label="d=%d" % (d))
    index += 1
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("precision-degre-facteur.pdf", bbox_inches="tight")
