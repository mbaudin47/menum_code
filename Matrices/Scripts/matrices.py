#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre comment utiliser numpy pour définir des matrices : 
transposée, multiplication par un scalaire, produit matrice-vecteur, 
produit matrice-matrice.
"""
from numpy import array

#
# 1. Matrices : additions
print(u"1. Matrices : addition")
A = array([[1.0, 2.0], [3.0, 4.0], [0.0, 1.0]])
B = array([[5.0, 6.0], [7.0, 8.0], [-1.0, 1.0]])
print(u"A=")
print(A)
print(u"B=")
print(B)
print(u"A+B=")
print(A + B)
#
# 2. Matrices : transposee
print(u"")
print(u"2. Matrices : transposee")
print(u"A=")
print(A)
print(u"A^T=")
print(A.T)
#
# 3. Matrices : multiplication par un scalaire
print(u"")
print(u"3. Matrices : multiplication par un scalaire")
alpha = 2
print(u"A=")
print(A)
print(u"alpha*A=")
print(alpha * A)
#
# 4. Produit matrice-vecteur
print(u"")
print(u"4. Produit matrice-vecteur")
x = array([1.0, 2.0])
print(u"A=")
print(A)
print(u"x=")
print(x)
print(u"A@x=")
print(A @ x)
#
# 5. Produit matrice-matrice
print(u"")
print(u"5. Produit matrice-matrice")
C = array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])
print(u"A=")
print(A)
print(u"C=")
print(C)
print(u"A@C=")
print(A @ C)
