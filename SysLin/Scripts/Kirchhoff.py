#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Utilise numpy pour calculer les tensions dans un circuit électrique par 
la loi de Kirchoff par résolution d'un système d'équations linéaires.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
from linalg import lu_decomposition, forward_elimination, backward_substitution

# Donnees du probleme
R = 1.0
vs = 10.0

print(u"")
print(u"1. Creer la matrice")
A = np.array([[3.0 * R, -R, 0.0], [-R, 4.0 * R, -R], [0.0, -R, 4.0 * R]])
print(u"A=")
print(A)
print(u"cond(A)=", np.linalg.cond(A))
print(u"Perdus=", np.log10(np.linalg.cond(A)))

print(u"")
print(u"2. Creer le second membre")
b = np.array([vs, 0.0, 0.0])
print(u"b=")
print(b)

print(u"")
print(u"3. Utiliser PA=LU")
L, U, p = lu_decomposition(A.copy())  # 1) Decompose
c = b[p]  # 2) Permute
y = forward_elimination(L, c)  # 3) Resout Ly=c
i = backward_substitution(U, y)  # 4) Resout Ui=y
print(u"i=")
print(i)
