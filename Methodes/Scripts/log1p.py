#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre la fonction log1p sur des exemples choisis.
Dessine le conditionnement de la fonction log1p en fonction de x.
"""
from floats import computeDigits, relativeError, logCond, log1pCond
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# Analyse de log1p
#
# 1. log(x) est mal conditionne
# quand x->1
print(u"")
print(u"1. log(x) est mal conditionne")
print(u"quand x->1")
x = 1.0 + 1.0e-6
c = logCond(x)
print(u"x=", x)
print(u"Condition number :", c)


def printLog1pError(x, exact):
    computed = np.log(1.0 + x)
    print(u"")
    print(u"x=", x)
    print(u"    Exact=", exact)
    print(u"With log(1+", x, ")")
    print(u"    Computed=", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    computed = np.log1p(x)
    print(u"With log1p(", x, ")")
    print(u"    Computed =", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    return None


#
# 2. Comparer log(1+x) vs log1p(x)
print(u"")
print(u"2. Comparer log(1+x) vs log1p(x)")
# Obtenu avec http://www.wolframalpha.com/


# Exemple #1
exact = 9.99999999950000000003e-11
printLog1pError(1.0e-10, exact)
#
# Exemple #2
exact = 9.99999999999999999995e-21
printLog1pError(1.0e-20, exact)
#
# 3. Evolution du conditionnement de log1p
print(u"")
print(u"3. Evolution du conditionnement de log1p")
N = 1000
x = np.linspace(-0.5, 0.5, N)
y = np.log1p(x)
c = log1pCond(x)
#
pl.figure(figsize=(2.5, 2.5))
#
pl.subplot(2, 1, 1)
pl.suptitle(u"Cond. de la fonction log1p")
pl.plot(x, y, "-")
pl.ylim(bottom=-1.0, top=0.5)
pl.ylabel(u"log1p(x)")
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.xlabel(u"x")
pl.ylabel(u"Cond. de log1p")
pl.subplots_adjust(hspace=0.3)
pl.savefig("log1p.pdf", bbox_inches="tight")
