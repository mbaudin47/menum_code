#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre le produit tensoriel de deux vecteurs avec la fonction outer du module 
numpy.

Shows outer product for LU pivoting
"""

from numpy import array, outer

A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
n = A.shape[0]
k = 0
m = 0
A[k + 1 : n, k] = A[k + 1 : n, k] / A[k, k]
print(A)
A[k + 1 : n, k]
A[k, k + 1 : n]
print(outer(A[k + 1 : n, k], A[k, k + 1 : n]))
