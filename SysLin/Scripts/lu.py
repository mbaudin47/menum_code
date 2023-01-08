#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Utilise numpy pour calculer la solution d'un système d'équations 
linéaires. 
Montre la décomposition LU, résout un système triangulaire supérieur, 
résout un système triangulaire inférieur. 
Montre comment rechercher les pivots dans une matrice avec argmax. 
Extraire les matrices L et U d'une décomposition LU.
Voir les matrices intermediaires.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from numpy import array, argmax, tril, triu
from numpy.linalg import solve
from linalg import lu_decomposition, forward_elimination, backward_substitution

#
# 1. Verifier PA=LU
print(u"")
print(u"1. Verifier PA=LU")
#
A = array([[10.0, -7.0, 0.0], [-3.0, 2.0, 6.0], [5.0, -1.0, 5.0]])
print(u"A=")
print(A)
L = array([[1.0, 0.0, 0.0], [0.5, 1.0, 0.0], [-0.3, -0.04, 1.0]])
print(u"L=")
print(L)
U = array([[10.0, -7.0, 0.0], [0.0, 2.5, 5.0], [0.0, 0.0, 6.2]])
print(u"U=")
print(U)
P = array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]])
print(u"P=")
print(P)
print(u"P@A=")
print(P @ A)
print(u"L@U=")
print(L @ U)
#
# 2. Resoudre Ux=b
U = array(
    [
        [1.0, 2.0, 3.0, 4.0],
        [0.0, 5.0, 6.0, 7.0],
        [0.0, 0.0, 8.0, 9.0],
        [0.0, 0.0, 0.0, 10.0],
    ]
)
print(u"U=")
print(U)
e = array([1.0, 2.0, 3.0, 4.0])
print(u"exact=")
print(e)
b = U @ e
print(u"b=")
print(b)
x = solve(U, b)
print(u"x=")
print(x)
x = backward_substitution(U, b)
print(u"backward_substitution(U,x)=")
print(x)

# 3. Resoudre Lx=b
L = array(
    [
        [1.0, 0.0, 0.0, 0.0],
        [2.0, 3.0, 0.0, 0.0],
        [4.0, 5.0, 6.0, 0.0],
        [7.0, 8.0, 9.0, 10.0],
    ]
)
print(u"L=")
print(L)
e = array([1.0, 2.0, 3.0, 4.0])
print(u"exact=")
print(e)
b = L @ e
print(u"b=")
print(b)
x = solve(L, b)
print(u"x=")
print(x)
x = forward_elimination(L, b)
print(u"forward_elimination(L,b)=")
print(x)
#
# 4. Rechercher les pivots dans une matrice
print(u"")
print(u"4. Rechercher les pivots dans une matrice")
A = array([[-3.0, 2.0, 6.0], [5.0, -1.0, 5.0], [10.0, -7.0, 0.0]])
print(u"A=")
print(A)
n = A.shape[0]
print(u"n=", n)
# Rechercher les pivots dans la colonne #k
print(u"Rechercher les pivots dans la colonne #k")
k = 1
print(u"k=", k)
m = argmax(abs(A[k:n, k]))
print(u"m=", m)
print(u"m+k=", m + k)
#
# 5. Extraire les parties U et L
print(u"")
print(u"5. Extraire les parties U et L")
A = array([[-3.0, 2.0, 6.0], [5.0, -1.0, 5.0], [10.0, -7.0, 0.0]])
print(u"A=")
print(A)
print(u"triu(U)=")
print(triu(A))
print(u"tril(U)=")
print(tril(A))
#
# 6. Factoriser PA=LU
print(u"")
print(u"6. Factoriser PA=LU")
A = array([[10.0, -7.0, 0.0], [-3.0, 2.0, 6.0], [5.0, -1.0, 5.0]])
print(u"A=", A)
L, U, p = lu_decomposition(A)
print(u"L=")
print(L)
print(u"U=")
print(U)
print(u"p=", p)
#
# 7. Voir les matrices intermediaires
print(u"")
print(u"7. Voir les matrices intermediaires")
A = array([[10.0, -7.0, 0.0], [-3.0, 2.0, 6.0], [5.0, -1.0, 5.0]])
print(u"A=")
print(A)
L1 = array([[1.0, 0.0, 0.0], [0.5, 1.0, 0.0], [-0.3, 0.0, 1.0]])
print(u"L1=")
print(L1)
L2 = array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, -0.04, 1.0]])
print(u"L2=")
print(L2)
P1 = array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
print(u"P1=")
print(P1)
P2 = array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]])
print(u"P2=")
print(P2)
print(u"L1@L2=")
print(L1 @ L2)
print(u"P2@P1=")
print(P2 @ P1)
M1 = array([[1.0, 0.0, 0.0], [0.3, 1.0, 0.0], [-0.5, 0.0, 1.0]])
print(u"M1=")
print(M1)
M2 = array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.04, 1.0]])
print(u"M2=")
print(M2)
