#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre la décomposition PA = LU d'une matrice.
"""
from numpy import array
from linalg import lu_decomposition

A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
L, U, p = lu_decomposition(A)
print(L)
print(U)
print(p)
