#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Interpolation d'une table de 6 observations par une spline cubique par 
morceaux.
On utilise une spline naturelle, puis une spline not-a-knot.
Cette dernière utilise d'autres conditions aux bords, ce qui change 
un peu le comportement de la spline sur les extrémités.

Examples of spline interpolation.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from numpy import linspace, arange, array
from pylab import plot, title, figure
from interp import spline_interpolation

#
# 1. Spline naturelle
print(u"1. Spline naturelle")

x = arange(1, 7)
y = array([16, 18, 21, 17, 15, 12])
nu = 100
u = linspace(0.75, 6.25, nu)
v = spline_interpolation(x, y, u)
figure()
plot(x, y, "o")
plot(u, v, "-")
title(u"Spline interpolation : natural")

#
# 2. Spline not-a-knot :
# a different boundary condition
print(u"")
print(u"2. Spline not-a-knot")
x = arange(1, 7)
y = array([16, 18, 21, 17, 15, 12])
nu = 100
u = linspace(0.75, 6.25, nu)
v = spline_interpolation(x, y, u, "not-a-knot")
figure()
plot(x, y, "o")
plot(u, v, "-")
title(u"Spline interpolation : not-a-knot")
