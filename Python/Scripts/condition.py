#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Définir une condition if en Python.
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
