#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Présente les formats en Python.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
#
# Formats
print(u"Formats")
a = 1234.56789
n = 9876
print(u"n = %6d" % n)  # Pad with spaces
print(u"a = %f" % a)
print(u"a = %e" % a)
print(u"a = %6.2f" % a)
print(u"a = %6.2e" % a)
