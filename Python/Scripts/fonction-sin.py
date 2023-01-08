#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine la fonction sinus.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

x = np.linspace(0.0, 2.0 * np.pi)
y = np.sin(x)
pl.figure(figsize=(2.0, 1.0))
pl.title(u"La fonction sin")
pl.plot(x, y, "-")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.savefig("fonction-sin.pdf", bbox_inches="tight")
