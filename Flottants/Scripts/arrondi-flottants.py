#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2022 - Michaël Baudin
"""
Montre les conséquences des erreurs d'arrondi avec des nombres à virgule 
flottante.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np

print("+ Evaluation de 3.0 - 0.3 / 0.1")
x = 3.0 - 0.3 / 0.1
print("x = ", x)

print("+ Evaluation de sin(pi)")
x = np.sin(np.pi)
print("x = ", x)

def float_repr(x):
    p = 53
    print("x = ", x)
    e = np.floor(np.log2(abs(x)))
    print("e = ", e)
    m = x / 2 ** (e - p + 1)
    print("m = ", m)
    exponent = e - p + 1
    print("x = %d * 2 ^ %d" % (m, exponent))
    return m, e
# 
print("+ Représentation de pi")
x = np.pi
float_repr(x)
# L'erreur d'arrondi est :
# https://www.wolframalpha.com/input?i=7205759403792794+*+2+**+-56+-+0.1

# 
print("+ Représentation de 0.1")
x = 0.1
float_repr(x)
# L'erreur d'arrondi est :
# https://www.wolframalpha.com/input?i=7074237752028440+*+2+%5E+-51+-+pi
