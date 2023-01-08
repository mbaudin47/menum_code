#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Permute les lignes d'un vecteur. 
Pour cela, utilise un tableau d'indice et utilise l'opération de slicing 
en Python avec un array numpy. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from numpy import array

p = [0, 2, 1]
print(p)
b = array([15.0, 5.7, 1.0])
print(b)
c = b[p]
print(c)
