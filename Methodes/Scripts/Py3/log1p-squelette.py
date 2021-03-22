# Copyright (C) 2013 - 2021 - Michaël Baudin

from floats import computeDigits, relativeError, expm1Cond, logCond, log1pCond
from numpy import linspace
from pylab import plot, figure, title, xlabel, ylabel, yscale
from math import log, log1p, exp, expm1

#
# 1. log(x) est mal conditionne
# quand x->1
x = 1.0 + 1.0e-6
c = TODO
print(u"x=", x)
print(u"Condition number :", c)


def printLog1pError(x, exact):
    computed = log(1.0 + x)
    print(u"")
    print(u"x=", x)
    print(u"    Exact=", exact)
    print(u"With log(1+", x, ")")
    print(u"    Computed=", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    computed = log1p(x)
    print(u"With log1p(", x, ")")
    print(u"    Computed =", computed)
    print(u"    Relative Error=", relativeError(exact, computed))
    print(u"    Number of Signif. Digits=", computeDigits(exact, computed, 10))
    return None


#
# 2. Comparer log(1+x) vs log1p(x)

exact = TODO
printLog1pError(TODO)

#
# 3. Evolution du conditionnement de log1p
x = linspace(TODO)
c = log1pCond(x)
figure()
plot(TODO)
xlabel(TODO)
ylabel(TODO)
title(TODO)
