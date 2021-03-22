#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre la différence entre erreur absolue et erreur relative sur des 
exemples choisis.
"""
from floats import computeDigits, relativeError

#
# Erreur absolue, relative


def computeError(exact, computed, basis):
    """
    Compute and print the absolute and relative errors.
    """
    abserr = abs(computed - exact)
    relerr = relativeError(exact, computed)
    d = computeDigits(exact, computed, basis)
    print(u"")
    print(u"computed=", computed, ", exact=", exact)
    print(u"Absolute error:", abserr)
    print(u"Relative error:", relerr)
    print(u"Correct base-", basis, " digits:", d)


a = 1.0
b = 1.0
computeError(a, b, 10)
computeError(a, b, 2)
#
a = 1.0
b = 2.0
computeError(a, b, 10)
computeError(a, b, 2)
#
a = 1.0
b = 1.000001
computeError(a, b, 10)
computeError(a, b, 2)
#
a = 1.0e100
b = 1.000001e100
computeError(a, b, 10)
computeError(a, b, 2)
#
a = 0.0
b = 1.0e-100
computeError(a, b, 10)
computeError(a, b, 2)
#
# Invariance par changement d'echelle
a = 1.0
b = 1.000001
computeError(a, b, 10)
alpha = 1.0e100
computeError(a * alpha, b * alpha, 10)
#
