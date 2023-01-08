#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Créer une liste en Python, déterminer sa longueur ; slicing.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
#
# Listes
print(u"Listes")
a = [1.0, 2.0, 3.0]  # Create a list
print(u"a=", a)
print(u"a[0]=", a[0])
print(u"a[1]=", a[1])
print(u"a[2]=", a[2])
print(u"len(a)=", len(a))  # Determine length of list
a[1:3] = [12.0, 13.0]  # Modify selected elements
print(u"a=", a)
print(u"len(a)=", len(a))  # Determine length of list
