#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre la fonction expm1 en action.
Dessine l'evolution du conditionnement de exp(x)-1 en fonction de x.
"""
from floats import computeDigits, relativeError, expm1Cond
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# Analyse de expm1
#
# 1. Calcule une table de exp(x)
print(u"")
print(u"1. Calcule une table de exp(x)")
print(u"pour x -> 0")

print(u"x    exp(x)")
for i in range(0, -20, -2):
    x = 10 ** i
    print(u"%.17e, %.17e" % (x, np.exp(x)))

# 2. Comparer exp(x)-1 vs expm1(x)
print(u"")
print(u"2. Comparer exp(x)-1 vs expm1(x)")


def printExpm1Error(x, exact):
    computed = np.exp(x) - 1.0
    print(u"")
    print(u"x=", x)
    print(u"Exact=", exact)
    print(u"With exp(", x, ")-1")
    print(u"    Computed=", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    computed = np.expm1(x)
    print(u"With expm1(", x, ")")
    print(u"    Computed =", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    return None


# Obtenu avec http://www.wolframalpha.com/
# Exemple #1
exact = 1.000000000050000000002e-10
printExpm1Error(1.0e-10, exact)
#
# Exemple #2
exact = 1.000000000000000000005e-20
printExpm1Error(1.0e-20, exact)

#
# 3. Evolution du conditionnement de exp(x)-1
print(u"")
print(u"3. Evolution du conditionnement de exp(x)-1")
N = 1000
x = np.linspace(-0.5, 0.5, N)
y = np.expm1(x)
c = expm1Cond(x)
#
pl.figure(figsize=(2.5, 2.5))
#
pl.subplot(2, 1, 1)
pl.suptitle(u"Cond. de la fonction expm1")
pl.plot(x, y, "-")
pl.ylabel(u"expm1(x)")
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.xlabel(u"x")
pl.ylabel(u"Cond. de expm1")
pl.subplots_adjust(hspace=0.3)
pl.savefig("expm1.pdf", bbox_inches="tight")
