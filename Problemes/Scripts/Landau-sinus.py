#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Application de la notation de Landau pour sinus au voisinage de zéro

L'objectif de cet exemple est de montrer comment se comporte 
la fonction sinus au voisinage de zéro. 
En particulier, nous illustrons que :

sin(x) = O(x) quand x -> 0

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import pylab as pl
import numpy as np
import matplotlibpreferences


matplotlibpreferences.load_preferences()

x = np.linspace(-2, 2, 101)
absx = np.abs(x)
abssin = np.abs(np.sin(x))

delta = 1.0

pl.figure(figsize=(1.5, 1.0))
pl.plot(x, abssin, "-", label="$|\sin(x)|$")
pl.plot(x, absx, "--", label="$|x|$")
pl.plot([-delta, -delta], [0.0, delta], "k:")
pl.plot([delta, delta], [0.0, delta], "k:")
pl.text(-delta - 0.2, -0.67, "$-\delta$")
pl.text(delta - 0.1, -0.67, "$\delta$")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
#pl.title(r"Notation de Landau quand $x\rightarrow 0$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("Landau-sinus.pdf", bbox_inches="tight")
