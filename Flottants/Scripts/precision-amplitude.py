#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Montre les champs de sys.float_info. 
Montre le comportement des nombres avec overflow, underflow. 
Calcule le epsilon machine avec un algorithme "historique". 
"""

#
# 1. La fonction sys.float_info
print(u"")
print(u"1. La fonction sys.float_info")
import sys

print(u"max:", sys.float_info.max)
print(u"max_exp:", sys.float_info.max_exp)
print(u"min:", sys.float_info.min)
print(u"min_exp:", sys.float_info.min_exp)
print(u"mant_dig:", sys.float_info.mant_dig)
print(u"epsilon:", sys.float_info.epsilon)
print(u"radix:", sys.float_info.radix)
#
# Heureusement, on ne peut pas changer ces attributs :
# sys.float_info.max=2 # TypeError: readonly attribute

#
# 2. Nombre extremes
print(u"")
print(u"2. Nombre extremes")
print(u"1.e1000=", 1.0e1000)
print(u"-1.e1000=", -1.0e1000)
print(u"1.e-1000=", 1.0e-1000)
print(u"-1.e-1000=", -1.0e-1000)

#
# 3. Epsilon machine
print(u"")
print(u"3. Epsilon machine")
eps = 1.0
n = 1
while 1.0 + eps > 1.0:
    eps = eps / 2.0
    print(u"n=", n, ", eps=", eps)
    n = n + 1
