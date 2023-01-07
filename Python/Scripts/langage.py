#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Utiliser les instructions de base en Python: variables, listes, opérateurs, 
condition if, boucle for, range, fonctions maths
"""
#
# 1. Variables
print(u"1. Variables")
b = 2  # b est entier
print(u"b=", b)
print(u"type(b)=", type(b))
b = b * 2.0  # b est flottant
print(u"b=", b)
print(u"type(b)=", type(b))
del b  # efface la variable b
# print b # erreur !
#
# 2. Listes
print(u"2. Listes")
a = [1.0, 2.0, 3.0]  # Create a list
print(u"a=", a)
print(u"a[0]=", a[0])
print(u"a[1]=", a[1])
print(u"a[2]=", a[2])
print(u"len(a)=", len(a))  # Determine length of list
a[1:3] = [12.0, 13.0]  # Modify selected elements
print(u"a=", a)
print(u"len(a)=", len(a))  # Determine length of list
#
# 3. Operateurs arithmetiques
print(u"3. Operateurs arithmetiques")
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
#
# 4. Operateurs de comparaison
print(u"4. Operateurs de comparaison")
# <, >, <=, >=, ==, !=
a = 2  # Integer
b = 1.99  # Floating point
c = "2"  # String
print(a > b)
print(a == c)
print((a > b) and (a != c))
print((a > b) or (a == b))
#
# 5. Conditions
print(u"5. Conditions")
a = 1.5
if a < 0.0:
    sign = "negative"
elif a > 0.0:
    sign = "positive"
else:
    sign = "zero"

print(u"a is ", sign)

#
# 6. Boucles
print(u"6. Boucles")
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
#
# 7. Fonctions maths communes
print(u"7. Fonctions maths communes")
# abs(a) : |a|
# max(sequence)
# min(sequence)
print(u"abs(-5)=", abs(-5))
print(u"max([2,-2,3])=", max([2, -2, 3]))  # max d'une liste
#
# 8. Formats
print(u"8. Formats")
# wd : entier sur w characteres
# w.df : flottant sur w characteres,
#        dont d apres la virgule
# w.de : Notation exponentielle
#        sur w characteres,
#        dont d apres la virgule.
a = 1234.56789
n = 9876
print(u"n = %6d" % n)  # Pad with spaces
print(u"a = %f" % a)
print(u"a = %e" % a)
print(u"a = %6.2f" % a)
print(u"a = %6.2e" % a)
