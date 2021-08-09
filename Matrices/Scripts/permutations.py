#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Définit une matrice de permutation avec numpy : utilisation d'une liste, 
convertit en matrice, produit matrice-matrice avec une matrice de permutation, 
utilisation d'une liste pour permuter les lignes de la matrice sans produit.
"""
from numpy import array, eye

#
# 1. Matrice de permutation
print(u"1. Matrice de permutation")
p = [3, 0, 2, 1]
print(u"p=", p)
# Convertit en matrice de permutation
I = eye(4)
print(u"I=")
print(I)
P = I[p, :]
print(u"P=")
print(P)
#
# 2. Produit P@A
print(u"")
print(u"2. Produit P@A")
A = array(range(16))
A = A.reshape((4, 4))
print(u"A=")
print(A)
print(u"P@A=")
print(P @ A)
#
# 3. Tableau de permutations
print(u"")
print(u"3. Tableau de permutations")
p = [0, 2, 1]
print(u"p=", p)
A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
print(u"A=")
print(A)
print(u"A[p,:]=")
print(A[p, :])
