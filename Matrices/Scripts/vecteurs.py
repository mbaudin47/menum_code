#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Définit et manipule des vecteurs avec numpy : norme, produit scalaire.
"""
from numpy import array, inf
from numpy.linalg import norm
from math import sqrt
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 1. Normes de vecteurs
print(u"1. Normes de vecteurs")
x = array([1.0, 2.0, 3.0])
print(u"x=")
print(x)
print(x.shape)
print(x.shape[0])
print(u"||x||_2=", norm(x))
print(u"Check=", sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2))
print(u"||x||_INF=", norm(x, inf))
print(u"Check=", max(abs(x)))
print(u"||x||_1=", norm(x, 1))
print(u"Check=", sum(abs(x)))

#
# 2. Produit scalaire
print(u"")
print(u"2. Produit scalaire")


def myDotProduct(x, y):
    """
    Scalar product x^t*y of two column vectors x and y.
    """
    n = x.shape[0]
    nbis = y.shape[0]
    if n != nbis:
        print(u"# rows in x does not match # rows in y")
    p = 0.0
    for i in range(n):
        p = p + x[i] * y[i]
    return p


x = array([1.0, 2.0, 3.0])
y = array([4.0, 5.0, 6.0])
print(u"x=")
print(x)
print(u"y=")
print(y)
print(u"x + y=")
print(x + y)
alpha = 2.0
print(u"alpha=", alpha)
print(u"alpha * x =", alpha * x)
print(u"x@y=")
print(x @ y)
print(u"myDotProduct(x,y)=")
print(myDotProduct(x, y))
