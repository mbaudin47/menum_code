#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Considère l'évolution du transport mondial de passager entre 1971 et 2019. 
Calcule la matrice de conception associée à un polynôme de degré 2, égale 
à la matrice de Vandermonde dans ce cas particulier. 
Calcule la décomposition QR de la matrice de conception. 
Vérifie que la matrice Q est orthogonale : 
- évalue les produits scalaires mutuels et montre qu'ils sont 
proches de zéro,
- évalue la norme des vecteurs colonnes de Q est montre qu'elles sont 
proche de un.
"""

from numpy import array, transpose, dot, vander, set_printoptions
from numpy.linalg import qr, norm, solve

#
# Define data
t = array(
    [
        1900.0,
        1910.0,
        1920.0,
        1930.0,
        1940.0,
        1950.0,
        1960.0,
        1970.0,
        1980.0,
        1990.0,
        2000.0,
    ]
)
y = array([76.00, 91.97, 105.7, 123.2, 131.7, 150.7, 179.3, 203.2, 226.5, 249.6, 281.4])

#
# 1. Check QR properties
n = 3
X = vander(t, n)
Q, R = qr(X)
set_printoptions(precision=5)
print(u"Q")
print(Q)
print(u"R")
print(R)
print(u"dot(Q[:,0],Q[:,1])", dot(Q[:, 0], Q[:, 1]))
print(u"dot(Q[:,0],Q[:,2])", dot(Q[:, 0], Q[:, 2]))
print(u"dot(Q[:,1],Q[:,2])", dot(Q[:, 1], Q[:, 2]))
print(u"norm(Q[:,0])", norm(Q[:, 0]))
print(u"norm(Q[:,1])", norm(Q[:, 1]))
print(u"norm(Q[:,2])", norm(Q[:, 2]))
#
# 2. Solve with QR
z = dot(transpose(Q), y)
beta = solve(R, z)
print(u"beta=")
print(beta)
