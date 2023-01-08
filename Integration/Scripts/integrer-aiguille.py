#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine une fonction pour laquelle une méthode d'intégration 
numérique peut être en difficulté.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def mafonction(x):
    a = 10000
    b = 0.5
    y = 1.0 / (1.0 + a * (x - b) ** 2)
    return y


x = np.linspace(-1.0, 1.0, 101)
y = mafonction(x)
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-")
pl.xlabel(u"$x$")
pl.ylabel(u"$y$")
pl.title(u"Une aiguille dans une botte de foin.")
pl.savefig("integrer-aiguille.pdf", bbox_inches="tight")
