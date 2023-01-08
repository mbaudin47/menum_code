#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine la fonction :

    f(x) = exp(-1 / x ^ 2)

pour x dans [-5, 5]. 
Cette fonction possède un minimum global en x = 0. 
Pourtant, toutes les dérivées de f sont nulles en ce point :

    f'(0) = f''(0) = ... = 0

C'est donc un "contre-exemple" pour lequel le théorème ne s'applique pas. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from numpy import exp, linspace
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

x = linspace(-5, 5, 100)
y = exp(-1.0 / x ** 2)

pl.figure(figsize=(1.5, 0.5))
pl.plot(x, y, "-")
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
pl.savefig("fonction-plate.pdf", bbox_inches="tight")
