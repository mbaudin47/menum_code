#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre deux algorithmes qui calculent le plus grand normal, le plus petit 
dénormalisé.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
#
# Approximation du plus grand normal
print(u"")
print(u"Approximation du plus grand normal")
M = 1.0
emax = 0
while True:
    t = M * 2
    if t / 2 != M:
        break
    M = t
    emax = emax + 1

print(u"M=", M)
print(u"emax=", emax)
print(u"2*M=", 2 * M)
#
# Plus petit denormalise
print(u"")
print(u"Plus petit denormalise")
m = 1.0
emin = 0
while True:
    t = m / 2
    if t * 2 != m:
        break
    m = t
    emin = emin - 1

print(u"m=", m)
print(u"emin=", emin)
print(u"m/2=", m / 2)
