#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Dessine la fonction :

    f(x) = exp(-1 / x ^ 2)

pour x dans [-5, 5]. 
Cette fonction possède un minimum global en x = 0. 
Pourtant, toutes les dérivées de f sont nulles en ce point :

    f'(0) = f''(0) = ... = 0

C'est donc un "contre-exemple" pour lequel le théorème ne s'applique pas. 
"""

from numpy import exp, linspace
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()

x = linspace(-5, 5, 100)
y = exp(-1.0 / x ** 2)

pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"f(x)")
pl.title(u"$f(x)=\exp(-1/x^2)$")
pl.savefig("fonction-plate.pdf", bbox_inches="tight")
