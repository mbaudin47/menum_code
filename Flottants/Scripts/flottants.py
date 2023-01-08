#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre les nombres à virgule flottante: normalisés, dénormalisés, en 
échelle logarithmique, positifs, négatifs.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from floats import floatgui
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# 1. Afficher les flottants
print(u"1. Afficher les flottants")
p = 3
emin = -2
emax = 3
"""
Pour avoir la liste des normalises
for m in range(2**(p-1), 2**p)
"""
# Pour avoir les normalises et denormalises
allfloats = []
for m in range(1 - 2 ** p, 2 ** p):
    for e in range(emin, emax + 1):
        x = m * 2 ** (e - p + 1)
        print(u"(", m, ",", e, ")=", x)
        allfloats.append(x)

sorted_floats = sorted(set(allfloats))
print(sorted_floats)
print("Nombre de flottants = ", len(sorted_floats))


#
# 2. Un systeme jouet
print(u"")
print(u"2. Un systeme jouet")
allfloats = floatgui()
print(u"Floats=")
for f in allfloats:
    print(f)
#
# 3. En echelle logarithmique
print(u"")
print(u"3. En echelle logarithmique")
allfloats = floatgui(logscale=True)
print(u"Floats=")
for f in allfloats:
    print(f)
#
# 4. Avec les nombres negatifs
print(u"")
print(u"4. Avec les nombres negatifs")
allfloats = floatgui(allpositive=False)
print(u"Floats=")
for f in allfloats:
    print(f)
#
# 5. Avec les denormalises
print(u"")
print(u"5. Avec les denormalises")
allfloats = floatgui(withdenormals=True)
print(u"Floats=")
for f in allfloats:
    print(f)
#
# 6. Avec les denormalises et les négatifs
print(u"")
print(u"5. Avec les denormalises")
p = 3
emin = -2
emax = 3
allfloats = floatgui(p, emin, emax, withdenormals=True, allpositive=False)
print(u"Floats=")
for f in allfloats:
    print(f)
pl.xlabel("$x$")
pl.title("Système flottant, $p=%d$, $e_{min}=%d$, $e_{max}=%d$" % (
    p, emin, emax))
fig = pl.gcf()
fig.set_size_inches(4.0, 0.5)
pl.savefig("flottants.pdf", bbox_inches="tight")

#
# Omega, alpha, mu
omega = (2 - 2 ** (1 - p)) * 2 ** emax
print("omega=", omega)
mu = 2 ** emin
print("mu=", mu)
alpha = 2 ** (emin - p + 1)
print("alpha=", alpha)

#
# Les flottants dénormalisés sont inférieurs (strictement) à m = beta ** (p - 1)
limite_denormal = 2 ** (p - 1)
print("Limite dénormalisés:", limite_denormal)
print("Exposant de beta minmal:", emin - p + 1)
