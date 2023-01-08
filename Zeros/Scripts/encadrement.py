#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dans une méthode de recherche de zéro, on doit parfois identifier un intervalle 
[a,b] contenant le zéro. 
Montre que le test d'encadrement ne doit PAS etre implémenté avec l'instruction 
f(a) * f(b).

Shows that bracketting test must NOT be implemented as f(a) * f(b).

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np

# A difficult test case if bracketting is implemented as product.
# In this case, the evaluation produces an overflow. (M.Baudin)
print("+ Cas 1")


def f(x):
    y = np.exp(x) - 5.221469689764144e173
    return y


a = 350.0
b = 450.0
x = 400.0

fa = f(a)
fb = f(b)
fx = f(x)
p = fa * fb
print("fa = %.3e" % (fa))
print("fb = %.3e" % (fb))
print("fx = %.3e" % (fx))
print("p = %.3e" % (p))

# Bad, very bad!
print(fa * fb < 0.0)

# Good implementation
print(np.sign(fa) != np.sign(fb))

# A difficult test case if bracketting is implemented as product
# In this case, the evaluation produces an underflow. (M.Baudin)
# https://github.com/scipy/scipy/issues/13737
print("+ Cas 2")


def f(x):
    y = np.exp(x) - 1.9151695967140057e-174
    return y


a = -450.0
b = -350.0
x = -400.0

fa = f(a)
fb = f(b)
fx = f(x)
p = fa * fb
print("fa = %.3e" % (fa))
print("fb = %.3e" % (fb))
print("fx = %.3e" % (fx))
print("p = %.3e" % (p))
# Bad, very bad!
print(fa * fb < 0.0)

# Good implementation
print(np.sign(fa) != np.sign(fb))
