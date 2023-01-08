#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre l'algorithme du produit matrice-vecteur, l'algorithme du produit 
matrice-matrice.
Montre les fonctions de numpy pour les vecteurs : 
somme, produit tensoriel, multiplication par un scalaire.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from numpy import array, zeros, outer

#
# 1. Produit matrice-vecteur : algorithme
def myMatVecProduct(A, x):
    """
    Matrix-vector product A*x.
    x must be a column vector.
    """
    m = A.shape[0]
    n = A.shape[1]
    xrows = x.shape[0]
    if n != xrows:
        print(u"# columns A does not match # rows x")
    y = zeros(m)
    for i in range(m):
        for j in range(n):
            y[i] = y[i] + A[i, j] * x[j]
    return y


print(u"1. Produit matrice-vecteur : algorithme")
A = array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]])
x = array([1.0, 2.0])
print(u"A=")
print(A)
print(u"x=")
print(x)
print(u"A@x=")
print(A @ x)
print(u"myMatVecProduct(A,x)=")
print(myMatVecProduct(A, x))

#
# 2. Produit matrice-matrice : algorithme
def myMatMatProduct(A, B):
    """
    Matrix-matrix product A*B.
    """
    m = A.shape[0]
    p = A.shape[1]
    pbis = B.shape[0]
    n = B.shape[1]
    if p != pbis:
        print(u"# columns A does not match # rows B")
    C = zeros((m, n))
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i, j] = C[i, j] + A[i, k] * B[k, j]
    return C


print(u"")
print(u"2. Produit matrice-matrice : algorithme")
A = array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]])
B = array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(u"A=")
print(A)
print(u"B=")
print(B)
print(u"A@B=")
print(A @ B)
print(u"myMatMatProduct(A,B)=")
print(myMatMatProduct(A, B))
#
# 3. Produit tensoriel
print(u"")
print(u"3. Produit tensoriel")
x = array([1.0, 2.0])
print(u"x=")
print(x)
y = array([0.0, 1.0, 2.0, 3.0])
print(u"y=")
print(y)
print(u"outer(x,y)=")
print(outer(x, y))
#
# 4. Somme
print(u"")
print(u"4. Somme")
x = array([1.0, 2.0, 3.0])
print(u"x=")
print(x)
y = array([[4.0], [5.0], [6.0]])
print(u"y=")
print(y)
print(u"x+y=")
print(x + y)
#
# 5. Somme, multiplication par un scalaire
print(u"")
print(u"5. Somme, multiplication par un scalaire")
alpha = 2.0
print(u"alpha=")
print(alpha)
x = array([1.0, 2.0, 3.0])
print(u"x=")
print(x)
y = array([4.0, 5.0, 6.0])
print(u"alpha*x=")
print(alpha * x)
