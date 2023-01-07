#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

from quadrature import adaptsim

#
# Compute integral of (x-c)**p from a to b,
# where c=(a+b)/2
#


def myfun(x, a, b, p):
    c = (a + b) / 2.0
    y = (x - c) ** p
    return y


a = 0.0
b = 1.0
p = 3
tol = 1.0e-6

for p in range(10):
    Q, fcount = adaptsim(myfun, a, b, tol, a, b, p)
    if p % 2 == 0:
        predicted = (b - a) ** (p + 1) / (p + 1) / 2 ** p
    else:
        predicted = 0.0
    print(u"%7d %13.3e %13.3e" % (p, Q, predicted))
