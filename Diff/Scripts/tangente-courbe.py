#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine la tangente à la courbe y = sin(x).

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
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
# Limites du graphique
ymin = -1.2
# Graphique
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-", label="$f(x)=\sin(x)$")
pl.plot(x, t, "--", label="$f(a)+(x-a)f'(a)$")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.ylim(bottom=ymin)
pl.title(u"Tangente de $\sin$ au point $a=2$")
pl.savefig("tangente-courbe.pdf", bbox_inches="tight")
