#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre les nombres extrêmes en Python: INF, NAN, division par zéro. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

#
# 1. Nombres extremes : INF, -INF
print(u"")
print(u"1. Nombres extremes : INF, -INF")
x = float("inf")
print(u"x=", x)
print(u"1+x=", 1 + x)
print(u"2*x=", 2 * x)
print(u"x/2=", x / 2)
print(u"1/x=", 1 / x)
#
x = float("-inf")
print(u"x=", x)
print(u"1+x=", 1 + x)
print(u"2*x=", 2 * x)
print(u"x/2=", x / 2)
print(u"1/x=", 1 / x)
#
# 2. NAN
print(u"")
print(u"2. NAN")
x = float("nan")
print(u"x=", x)
print(u"1+x=", 1 + x)
print(u"2*x=", 2 * x)
print(u"x/2=", x / 2)
print(u"1/x=", 1 / x)
#
# 3. Comment produire NAN ?
print(u"")
print(u"3. Comment produire NAN ?")
x = float("inf")
print(u"x-x", x - x)
print(u"0*x", 0 * x)
print(u"x/x", x / x)
#
#
# 4. Division par zero
# Produce a ZeroDivisionError
print(u"")
print(u"4. Division par zero")
x = +0.0
print(u"x=", x)
# print(u"1.0/x=",1.0/x) # ZeroDivisionError
#
x = -0.0
print(u"x=", x)
# print(u"1.0/x=",1.0/x) # ZeroDivisionError
