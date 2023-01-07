#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Dessine la sécante à la courbe y = x ** 2.
"""

import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# Fonction
x = np.linspace(-0.2, 2.0 * np.pi, 100)
y = np.sin(x)
# Tangente
a = 2.0
d = np.cos(a)
t = np.sin(a) + d * (x - a)
# Sécante
h = 1.0
d = (np.sin(a + h) - np.sin(a)) / h
s = np.sin(a) + d * (x - a)
# Limites du graphique
ymin = -2.5
delta = 0.3
# Graphique
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-", label="$f(x)=\sin(x)$")
pl.plot(x, t, "--", label="$f(a)+(x-a)f'(a)$")
pl.plot(x, s, ":", label="$f(a)+(x-a)d$")
pl.plot([a, a], [ymin, np.sin(a)], ":")
pl.text(a - 3.0 * delta, ymin + delta, "a")
pl.plot([a + h, a + h], [ymin, np.sin(a + h)], ":")
pl.text(a + h + delta, ymin + delta, "a + h")
pl.ylim(bottom=ymin)
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.title(u"Sécante de $\sin$ au point a=2 avec h=1.")
pl.savefig("secante-courbe.pdf", bbox_inches="tight")
