#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre l'algorithme du produit matrice vecteur, fondé sur deux boucles 
imbriquées.
Montre comment utiliser l'opérateur @ avec des array numpy et compare 
les deux méthodes. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy

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
        print(u"# of columns in A does not match # of rows in x")
    y = numpy.zeros(m)
    for i in range(m):
        for j in range(n):
            y[i] = y[i] + A[i, j] * x[j]
    return y


print(u"")
print(u"1. Produit matrice-vecteur : algorithme")
A = numpy.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]])
x = numpy.array([1.0, 2.0])
print(u"A=")
print(A)
print(u"x=")
print(x)
print(u"A@x=")
print(A @ x)
print(u"myMatVecProduct(A,x)=")
print(myMatVecProduct(A, x))

#
# Produit matrice-matrice : algorithme
def myMatMatProduct(A, B):
    """
    Matrix-matrix product A*B.
    """
    m = A.shape[0]
    p = A.shape[1]
    pbis = B.shape[0]
    n = B.shape[1]
    if p != pbis:
        print(u"# of columns in A does not match # of rows in B")
    C = numpy.zeros((m, n))
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i, j] = C[i, j] + A[i, k] * B[k, j]
    return C


print(u"")
print(u"Produit matrice-matrice : algorithme")
A = numpy.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]])
B = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(u"A=")
print(A)
print(u"B=")
print(B)
print(u"A@B=")
print(A @ B)
print(u"myMatMatProduct(A,B)=")
print(myMatMatProduct(A, B))
