#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Définir une condition if en Python.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
#
# Conditions
print(u"Conditions")
a = 1.5
if a < 0.0:
    sign = "negative"
elif a > 0.0:
    sign = "positive"
else:
    sign = "zero"

print(u"a is ", sign)
