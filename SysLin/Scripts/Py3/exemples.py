#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Utilise numpy pour résoudre un système d'équations linéaires. 
Résout un système d'équations linéaires par décomposition PA = LU. 
Montre un exemple de résolution avec un pivot nécessaire.
Montre un exemple de matrice mal conditionnée.
Résout plusieurs problèmes avec un seul appel à solve().
"""
from numpy import array, inf
from numpy.linalg import solve, cond
from linalg import lu_decomposition, forward_elimination, backward_substitution

#
# 1. Exemple simple
print(u"1. Exemple simple")
A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
print(u"A=")
print(A)
# Calcule le conditionnement
print(u"cond(A)=", cond(A, inf))
b = array([15.0, 5.7, 1.0])
print(u"b=")
print(b)
# 1) Decompose
L, U, p = lu_decomposition(A)
# Observer que A est changee
# print A
# 2) Permute les lignes de b
c = b[p]
# 3) Resout Ly=c
y = forward_elimination(L, c)
print(u"y=")
print(y)
# 4) Resout Ux=y
x = backward_substitution(U, y)
print(u"x=")
print(x)
# Resout avec solve
A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
b = array([15.0, 5.7, 1.0])
x = solve(A, b)
print(u"solve(A,b)=")
print(x)

################################################
#
# Optionnel
#

import sys
from linalg import lu_no_pivoting
from numpy.linalg import norm
from scipy.linalg import hilbert
from math import log10
from numpy import ones

print(u"")
print(u"Optionnel")
#
# 2. Exemple avec pivot necessaire
print(u"")
print(u"2. Exemple avec pivot necessaire")
eps = sys.float_info.epsilon
A = array([[2 * eps, 1.0], [1.0, 1.0]])
print(u"A=")
print(A)
print(u"cond(A)=", cond(A))
# 1) Decompose PA=LU
print(u"Decompose PA=LU")
L, U, p = lu_decomposition(A.copy())
# 2) Affiche les matrices
print(u"L=")
print(L)
print(u"cond(L)=", cond(L))
print(u"U=")
print(U)
print(u"cond(U)=", cond(U))
# 3) Decompose A=LU
print(u"Decompose A=LU")
L, U = lu_no_pivoting(A.copy())
# 4) Affiche les matrices
print(u"L=")
print(L)
print(u"cond(L)=", cond(L))
print(u"U=")
print(U)
print(u"cond(U)=", cond(U))

#
# 3. Exemple matrice mal conditionnee

print(u"")
print(u"3. Exemple matrice mal conditionnee")
n = 4
A = hilbert(n)
print(u"A=")
print(A)
print(u"cond(A)=", cond(A))
e = ones((n, 1))
b = A @ e
print(u"b=")
print(b)
x = solve(A, b)
print(u"solve(A,b)=")
print(solve(A, b))
lre = -log10(norm(x - e) / norm(e))
print(u"solve : LRE=", lre)


#
# 4. Resoudre plusieurs systemes
print(u"")
print(u"4. Resoudre plusieurs systemes")
#
A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
print(u"A=")
print(A)
B = array([[15.0, -5.4], [5.7, -0.3], [1.0, -9.8]])
print(u"B=", end=" ")
print(B)
x = solve(A, B)
print(u"x=")
print(x)
