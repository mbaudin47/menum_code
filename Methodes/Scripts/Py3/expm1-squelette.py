# Copyright (C) 2013 - 2021 - Michaël Baudin

from floats import computeDigits, relativeError, expm1Cond, logCond, log1pCond
from numpy import linspace
from pylab import plot, figure, title, xlabel, ylabel, yscale
from math import log, log1p, exp, expm1

#
# Analyse de expm1
#

# 1. Calcule une table de exp(x)
print(u"x    exp(x)")
for i in range(0, -20, -2):
    x = 10 ** i
    print(u"%.17e, %.17e" % (x, exp(x)))

# 2. Comparer exp(x)-1 vs expm1(x)
def printExpm1Error(x, exact):
    computed = exp(x) - 1.0
    print(u"")
    print(u"x=", x)
    print(u"Exact=", exact)
    print(u"With exp(", x, ")-1")
    print(u"    Computed=", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    computed = expm1(x)
    print(u"With expm1(", x, ")")
    print(u"    Computed =", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    return None


exact = TODO
printExpm1Error(TODO)

#
# 3. Evolution du conditionnement de exp(x)-1
x = linspace(TODO)
c = expm1Cond(x)
figure()
plot(TODO)
xlabel(TODO)
ylabel(TODO)
title(TODO)
