#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilise plusieurs règles d'intégration sur une fonction
test dont l'intégrale exacte est connue.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np
from quadrature import (
    midpoint_rule,
    trapezoidal_rule,
    simpson_rule,
    compositesimpson_rule,
    boole_rule,
)


def myfunc(x):
    y = np.sin(2.5 * x) ** 2
    return y

a = 0.0
b = 1.0

I_exacte = (5.0 - np.sin(5.0)) / 10.0
print("I = %.4f" % (I_exacte))

h = b - a

# Règle du point milieu (A)
c = (a + b) / 2.0
fc = myfunc(c)
M = h * fc
print("M = %.4f" % (M))

# Règle du point milieu (B)
M, fcount = midpoint_rule(myfunc, a, b)
print("M = %.4f (B)" % (M))
print("fcount = ", fcount)

# Règle du trapèze
fa = myfunc(a)
fb = myfunc(b)
T = h * (fa + fb) / 2.0
print("T = %.4f" % (T))

# Règle du trapèze (B)
T, fcount = trapezoidal_rule(myfunc, a, b)
print("T = %.4f (B)" % (T))
print("fcount = ", fcount)

# Règle de Simpson (A)
S = h * (fa + 4 * fc + fb) / 6.0
print("S = %.4f" % (S))

# Règle de Simpson (B)
S = 2.0 * M / 3.0 + T / 3.0
print("S = %.4f (B)" % (S))

# Règle de Simpson (C)
S, fcount = simpson_rule(myfunc, a, b)
print("S = %.4f (C)" % (S))
print("fcount = ", fcount)

# Règle de Simpson composite à deux sous-intervalles (A)
integral1, fcount1 = simpson_rule(myfunc, a, c)
integral2, fcount2 = simpson_rule(myfunc, c, b)
S2 = integral1 + integral2
print("S2 = %.4f" % (S2))

# Règle de Simpson composite à deux sous-intervalles (B)
d = (a + c) / 2.0
e = (c + b) / 2.0
fd = myfunc(d)
fe = myfunc(e)
S2 = h * (fa + 4.0 * fd + 2.0 * fc + 4.0 * fe + fb) / 12.0
print("S2 = %.4f (B)" % (S2))

# Règle de Simpson composite à deux sous-intervalles (C)
S2, fcount = compositesimpson_rule(myfunc, a, b)
print("S2 = %.4f (C)" % (S2))
print("fcount = ", fcount)

# Règle de Boole (A)
w1 = 7.0 / 6.0
w2 = 16.0 / 3.0
w3 = 2.0
w4 = 16.0 / 3.0
w5 = 7.0 / 6.0
B = h * (w1 * fa + w2 * fd + w3 * fc + w4 * fe + w5 * fb) / 15.0
print("B = %.4f" % (B))

# Règle de Boole (B)
B = S2 + (S2 - S) / 15.0
print("B = %.4f (B)" % (B))

# Règle de Boole (C)
B, fcount = boole_rule(myfunc, a, b)
print("B = %.4f (C)" % (B))
print("fcount = ", fcount)
