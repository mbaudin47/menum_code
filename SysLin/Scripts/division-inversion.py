#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Comparaison entre la division et l'inversion pour la résolution 
d'une équation linéaire à une inconnue.

Références
----------
George E. Forsythe, Michael A. Malcolm et Cleve Moler. Computer
methods for mathematical computations. Prentice-Hall Series in 
Automatic Computation, 1977.
Page 31.

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np

a = 6.0
b = 8.0

# Method #1 : division
x1 = b / a
x1 = np.around(x1, decimals=3)
print("x1=", x1)

# Method #2 : inversion
a_inverse = 1.0 / a
a_inverse = np.around(a_inverse, decimals=3)
print("a_inverse=", a_inverse)
x2 = a_inverse * b
x2 = np.around(x2, decimals=3)
print("x2=", x2)


def compute_error(a, b, verbose=False):
    """
    Compute the absolute error between the two methods.
    """
    # Method #1 : division
    x1 = b / a
    x1 = np.around(x1, decimals=3)
    if verbose:
        print("x1=", x1)

    # Method #2 : inversion
    a_inverse = 1.0 / a
    a_inverse = np.around(a_inverse, decimals=3)
    if verbose:
        print("a_inverse=", a_inverse)
    x2 = a_inverse * b
    x2 = np.around(x2, decimals=3)
    if verbose:
        print("x2=", x2)

    error = abs(x1 - x2)
    return error


# Boucle de recherche
maximum_error = 0.0
worst_a = 0.0
worst_b = 0.0
number_of_trials = 1000
for i in range(number_of_trials):
    a = float(np.random.randint(1, 10))
    if a == 0.0:
        continue
    b = float(np.random.randint(1, 10))
    if b == 0.0:
        continue
    error = compute_error(a, b)
    if error > maximum_error:
        maximum_error = error
        worst_a = a
        worst_b = b

print("+ Worst case:")
print("a=", worst_a)
print("b=", worst_b)
relative_error = compute_error(worst_a, worst_b, True)
print("Max. error=", maximum_error)
