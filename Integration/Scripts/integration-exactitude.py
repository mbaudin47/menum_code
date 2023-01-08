#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Draw the four rules of numerical integration: midpoint, trapezoidal, 
Simpson and Boole. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from quadrature import (
    adaptsim,
    midpoint_rule,
    trapezoidal_rule,
    simpson_rule,
    boole_rule,
)


def polynomial(x, p):
    y = x ** p
    return y


# Verifie le degre d'exactitude
a = 0.0
b = 1.0
pmax = 10
tol = 1.0e-15
for p in range(pmax):
    exacte, fcount = adaptsim(polynomial, a, b, tol, p)
    # I,fcount=midpoint_rule(polynomial,a,b,p)
    # I,fcount=trapezoidal_rule(polynomial,a,b,p)
    # I,fcount=simpson_rule(polynomial,a,b,p)
    # I,fcount=compositesimpson_rule(polynomial,a,b,p)
    I, fcount = boole_rule(polynomial, a, b, p)
    print(u"p=", p, "Exacte=", exacte, ", I=", I, ", Err.abs.", abs(exacte - I))
    if abs(exacte - I) > tol:
        p = p - 1
        break

print(u"Degré d'exactitude=", p)
print(u"Ordre de précision=", p + 1)

# Verifie le degre d'exactitude
a = 0.0
b = 1.0
pmax = 7
tol = 1.0e-15
for p in range(pmax):
    exacte, fcount = adaptsim(polynomial, a, b, tol, p)
    I1, fcount = midpoint_rule(polynomial, a, b, p)
    I2, fcount = trapezoidal_rule(polynomial, a, b, p)
    I3, fcount = simpson_rule(polynomial, a, b, p)
    I4, fcount = boole_rule(polynomial, a, b, p)
    # print "p=",p, "Exacte=",exacte,", Milieu=", I1, "Trapeze=", I2, "Simpson=", I3, "boole=", I4
    print(p, "&", exacte, "&", I1, "&", I2, "&", I3, "&", I4)
