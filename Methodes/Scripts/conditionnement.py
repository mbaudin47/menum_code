#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre le conditionnement de log(x) quand x~1. 
Dessine le conditionnement de log en fonction de x.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
#
# Conditionnement de log(x) quand x~1
#
import pylab as pl
from numpy import log, linspace
from floats import logCond
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 1. Conditionnement de log
print(u"")
print(u"1. Conditionnement de log")
x = 1.01
print(u"x=", x)
print(u"    log(x)=", log(x))
print(u"    logCond(x)=", logCond(x))
#
x = 1.0001
print(u"x=", x)
print(u"    log(x)=", log(x))
print(u"    logCond(x)=", logCond(x))
#
x = 1.000001
print(u"x=", x)
print(u"    log(x)=", log(x))
print(u"    logCond(x)=", logCond(x))
#
# 2. Plot
print(u"")
print(u"2. Plot")
x = linspace(0.5, 1.5, 1000)
y = log(x)
c = logCond(x)
#
pl.figure(figsize=(4, 3))
pl.title(u"log")
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"log(x)")
pl.ylim(top=0.5)
pl.savefig("conditionnement-log.pdf", bbox_inches="tight")

#
pl.figure(figsize=(4, 3))
pl.title(u"Conditionnement de log")
pl.plot(x, c, "-")
pl.yscale("log")
pl.xlabel(u"x")
pl.ylabel(u"Condition-Log(x)")
pl.savefig("conditionnement-condlog.pdf", bbox_inches="tight")
