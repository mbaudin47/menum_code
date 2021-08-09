#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
On considère la fonction log(x) pour x dans [0.5, 1.5]. 
Dessine le conditionnement de la fonction log. 
"""
import pylab as pl
from numpy import log, linspace
from floats import logCond
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 2. Plot
N = 1000
x = linspace(0.5, 1.5, N)
y = log(x)
c = logCond(x)
#
pl.figure(figsize=(2.5, 2.5))
#
pl.subplot(2, 1, 1)
pl.suptitle(u"Conditionnement de la fonction log")
pl.plot(x, y, "-")
pl.ylim(bottom=-1.0, top=0.5)
pl.ylabel(u"$\log(x)$")
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.yscale("log")
pl.xlabel(u"x")
pl.ylabel(u"Cond. de log")
pl.ylim(bottom=1.0e0, top=1.0e4)
pl.subplots_adjust(hspace=0.3)
pl.savefig("condition-log.pdf", bbox_inches="tight")
