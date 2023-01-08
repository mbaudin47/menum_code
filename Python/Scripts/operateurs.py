#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Présente les opérateurs arithmétiques en Python: +, -, *, /, ** et %.
Présente les opérateurs de comparaison : <, >, <=, >=, ==, !=.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
#
# Operateurs arithmetiques
print(u"Operateurs arithmetiques")
# + : addition
# - : soustraction
# * : multiplication
# / : division
# ** : exponentiation
# % : division modulaire
a = 2.0
b = 3.0
print(u"a+b=", a + b)
print(u"a-b=", a - b)
print(u"a*b=", a * b)
print(u"a/b=", a / b)
print(u"a**2=", a ** 2)
print(u"a%2=", a % 2)
#
# Operateurs de comparaison
print(u"Operateurs de comparaison")
# <, >, <=, >=, ==, !=
a = 2  # Integer
b = 1.99  # Floating point
c = "2"  # String
print(a > b)
print(a == c)
print((a > b) and (a != c))
print((a > b) or (a == b))
