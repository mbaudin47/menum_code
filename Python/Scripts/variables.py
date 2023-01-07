#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Affecter, lire, imprimer et effacer une variable en Python.
"""
#
# Variables
print(u"Variables")
b = 2  # b est entier
print(u"b=", b)
print(u"type(b)=", type(b))
b = b * 2.0  # b est flottant
print(u"b=", b)
print(u"type(b)=", type(b))
del b  # efface la variable b
# print b # erreur !
