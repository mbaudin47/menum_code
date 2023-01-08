#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Conditionnement de la fonction erf.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import pylab as pl
import numpy as np
from scipy.special import erf
from floats import erfCond
import matplotlibpreferences

matplotlibpreferences.load_preferences()


#
# 2. Plot
N = 1000
x = np.linspace(-6.0, 6.0, N)
y = erf(x)
c = erfCond(x)
#
pl.figure(figsize=(1.5, 1.5))
#
pl.subplot(2, 1, 1)
pl.suptitle(u"Cond. de la fonction erf")
pl.plot(x, y, "-")
pl.ylim(bottom=-1.2, top=1.2)
pl.ylabel(u"$\\textrm{erf}(x)$")
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.yscale("log")
pl.xlabel(u"$x$")
pl.ylabel(u"Cond. de erf")
pl.ylim(bottom=1.0e-15, top=1.0e2)
pl.subplots_adjust(hspace=0.5)
pl.savefig("condition-erf.pdf", bbox_inches="tight")
