#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Présente les boucles while et for.
"""
#
# Boucles
print(u"Boucles")
# Boucles while
nMax = 5
n = 1
a = []  # Create empty list
while n < nMax:
    a.append(1.0 / n)  # Append element to list
    n = n + 1

print(u"a=", a)
# Sortie : [1.0, 0.5, 0.33333333333333331, 0.25]
#
# Fonction range
start = 1
stop = 5
step = 2
print(u"range(stop)=", list(range(stop)))
print(u"range(start,stop)=", list(range(start, stop)))
print(u"range(start,stop,step)=", list(range(start, stop, step)))
#
# Boucles for
nMax = 5
a = []  # Create empty list
for n in range(1, nMax):
    a.append(1.0 / n)

print(a)
