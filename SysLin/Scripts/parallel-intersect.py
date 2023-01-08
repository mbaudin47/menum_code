#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine des vecteurs définissant des lignes parallèles, puis des 
lignes possédant une intersection.

Parallel and intersected lines.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import pylab as pl
import numpy as np
import matplotlibpreferences

matplotlibpreferences.load_preferences()

x1 = np.linspace(1.0, 3.0, 100)

ymin = 1.0
ymax = 5.0
figheight = 1.0
figwidth = 1.0

# 1. Parallel lines
pl.figure(figsize=(figwidth, figheight))
# Line 1
x2 = 9.0 - 3.0 * x1
pl.plot(x1, x2, "-", label="$3 x_1 + x_2 = 9$")
# Line 2
x2 = 7.0 - 3.0 * x1
pl.plot(x1, x2, "--", label="$3 x_1 + x_2 = 7$")
#
pl.ylim(ymin, ymax)
pl.xlabel("$x_1$")
pl.ylabel("$x_2$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("parallel-intersect-parallel.pdf", bbox_inches="tight")

# 2. Intersection lines
pl.figure(figsize=(figwidth, figheight))
# Line 1
x2 = 9.0 - 3.0 * x1
pl.plot(x1, x2, "-", label="$3 x_1 + x_2 = 9$")
# Line 2
x2 = 1.0 + x1
pl.plot(x1, x2, "--", label="$x_1 - x_2 = -1$")
# Intersection
pl.plot(2.0, 3.0, "o", label="$(2, 3)$")
#
pl.ylim(ymin, ymax)
pl.xlabel("$x_1$")
pl.ylabel("$x_2$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("parallel-intersect-intersect.pdf", bbox_inches="tight")
