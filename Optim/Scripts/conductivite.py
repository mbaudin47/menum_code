#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
On cherche à déterminer la conductivité optimale d'une laine de verre. 
Cela revient à déterminer le minimum de la fonction 

y = a + b * x + c / x

où a, b, c sont des constantes. 
On utilise la méthode du nombre d'or.

On a fixé :

rhoopt = 89.73245971

On peut calculer b et c en fonction de rhoopt par l'équation :

b = 0.001 / (50 + rhoopt ** 2 / 50)
c = rhoopt ** 2 * b

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import numpy as np
import pylab as pl
from optim import goldensection, goldensectiongui
import matplotlibpreferences


matplotlibpreferences.load_preferences()

lambda50 = 0.037  # Lambda(rho=50) Lu sur le graphique
lambdaopt = 0.036  # Lu sur le graphique


def conduc(x, a, b, c):
    y = a + b * x + c / x
    return y


a = 0.034
b = 4.739e-6
c = 0.03815

rhoopt_exact = np.sqrt(c / b)
print(u"xopt (exact)=", rhoopt_exact)

# Solve
reltolx = 1.0e-8
xopt, fopt = goldensection(conduc, 30.0, 200.0, reltolx, a, b, c)
print(u"xopt=", xopt)
print(u"fopt=", fopt)
absolute_error = abs(rhoopt_exact - xopt)
print(u"Abs. error=", absolute_error)
relative_error = absolute_error / abs(rhoopt_exact)
print(u"Rel. error=", relative_error)


print(u"a=", a)
print(u"b=", b)
print(u"c=", c)
x = np.linspace(30, 200)
y = conduc(x, a, b, c)

pl.figure(figsize=(2.0, 1.0))

# Solve with gui
reltolx = 1.0e-8
xopt, fopt = goldensectiongui(conduc, 30.0, 200.0, reltolx, a, b, c)
pl.plot(xopt, fopt, "*")
#pl.ylabel(u"Conductivite (W/(m.K)")
#pl.xlabel(u"Densité (kg/$m^3$)")
pl.xlabel(u"$\\rho$")
pl.ylabel(u"$\\lambda(\\rho)$")
pl.savefig("conductivite.pdf", bbox_inches="tight")
