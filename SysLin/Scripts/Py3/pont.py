#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Calcule les efforts dans un pont à base de poutres. 
"""

import numpy as np
from linalg import lu_decomposition, forward_elimination, backward_substitution

#
# 1. Calcul de la force
print(u"1. Calcul de la force")
unnewton = 9.807
M = 10000
print(u"M=", M, " (kg)")
F = unnewton * M
print(u"F=", F, " (N)")

# Donnees du probleme
alpha = np.sqrt(2.0) / 2.0

# 2. Matrice
A = np.zeros((5, 5))
A[0, :] = [0.0, 1.0, 0.0, -1.0, 0.0]
A[1, :] = [0.0, 0.0, 1.0, 0.0, 0.0]
A[2, :] = [alpha, 0.0, 0.0, 0.0, -alpha]
A[3, :] = [alpha, 0.0, 1.0, 0.0, alpha]
A[4, :] = [0.0, 0.0, 0.0, 1.0, alpha]
print(u"A=")
print(A)

# 4. Calculer le conditionnement
print(u"cond(A)=", np.linalg.cond(A))
print(u"Perdus=", np.log10(np.linalg.cond(A)))
print(u"Restants=", np.log10(2 ** 53 / np.linalg.cond(A)))

# 5. Creer le second membre
b = np.array([0.0, F, 0.0, 0.0, 0.0])
print(u"b=")
print(b)

# 6. Utiliser PA=LU
L, U, p = lu_decomposition(A.copy())  # 1) Decompose
y = forward_elimination(L, b[p])  # 2) Resout Ly=Pb
x = backward_substitution(U, y)  # 3) Resout Ux=y
print(u"x=")
print(x)
for i in range(5):
    print("x[%d] = %.3e" % (i, x[i]))

# 7. Utiliser solve
x = np.linalg.solve(A, b)
print(u"solve(A,b)=")
print(x)
