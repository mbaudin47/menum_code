#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Définit des nombres extrêmes en Python avec numpy : division par zéro, zéro 
signé.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
#
# Division par zero avec Numpy
print(u"")
print(u"Division par zero avec Numpy")
import numpy

x = numpy.float64(0.0)
# print 1/x # FloatingPointError
numpy.seterr(all="ignore")
print(1 / x)  # inf
numpy.seterr(all="raise")
# print 1/x # FloatingPointError
#
# Zeros avec signes avec Numpy
print(u"")
print(u"Zeros avec signes avec Numpy")
import numpy

numpy.seterr(all="ignore")
x = numpy.float64(0.0)
print(u"x=", x)
print(u"1/x=", 1 / x)  # inf
x = numpy.float64(-0.0)
print(u"x=", x)
print(u"1/x=", 1 / x)  # -inf
