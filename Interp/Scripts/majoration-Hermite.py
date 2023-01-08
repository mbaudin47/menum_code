#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine le polynôme impliqué dans la majoration pour le calcul 
de l'erreur d'interpolation par spline cubique d'Hermite :

    f(t) = t^2 (1 - t)^2

pour t dans [0, 1].

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

t = np.linspace(0.0, 1.0, 100)
y = t ** 2 * (t - 1.0) ** 2
pl.figure(figsize=(2.0, 1.0))
pl.plot(t, y)
pl.xlabel(u"$t$")
pl.ylabel(r"$t^2 (t-1)^2$")
pl.savefig("majoration-Hermite.pdf", bbox_inches="tight")
