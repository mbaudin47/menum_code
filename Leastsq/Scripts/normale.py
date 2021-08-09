#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Considère l'évolution du transport mondial de passager entre 1971 et 2019. 
Approche cette courbe par un polynôme de degré 2, puis prédit 
la valeur du nombre de passagers en 2030, sous l'hypothèse d'une évolution 
future similaire à l'évolution passée.
Utilise un polynôme de degré 1, 2 ou 3 et compare le résultat. 
Pour résoudre le problème, on évalue la matrice de Vandermonde et on 
utilise la méthode des équations normales. 
"""

from numpy import array, size, linspace, vander
from numpy.linalg import solve, cond
import pylab as pl
from leastsq import polynomial_fit_normal_equations, polynomial_value
from math import log10
from numpy.linalg import cholesky
import matplotlibpreferences


matplotlibpreferences.load_preferences()

#
# 1. Transport mondial de passagers
print(u"")
print(u"1. Transport mondial de passagers")
t = array(
    [
        1971.0,
        1975.0,
        1980.0,
        1985.0,
        1990.0,
        1995.0,
        2000.0,
        2005.0,
        2010.0,
        2015.0,
        2019.0,
    ]
)
y = array(
    [0.3104, 0.4211, 0.6484, 0.7324, 0.9832, 1.233, 1.562, 1.889, 2.245, 3.227, 4.233]
)
m = size(y)
print(u"Nombre d'observations=", m)
# Le nombre d'inconnues
n = 3
print(u"Nombre d'inconnues=", n)
print(u"Degré du polynôme=", n - 1)
# Calcule la matrice X
X = vander(t, n)
print(u"X=")
print(X)
print(u"log10(cond(X))=", log10(cond(X)))
# Résout les équations normales
A = X.T @ X
print(u"A=")
print(A)
print(u"log10(cond(A))=", log10(cond(A)))
b = X.T @ y
print(u"b=")
print(b)
beta = solve(A, b)
print(u"beta=", beta)
# Evalue le polynôme
m = 100
u = linspace(1970, 2040, m)
X = vander(u, n)
v = X @ beta
# Nombre de passagers en 2030
u2030 = array([2030.0])
X = vander(u2030, n)
v2030 = X @ beta

# Make a plot
fig = pl.figure(figsize=(2.0, 1.0))
pl.plot(t, y, "o")
pl.plot(u, v, "-")
pl.plot(u2030, v2030, "s")
pl.xlabel(u"")
pl.ylabel(u"Milliards")
pl.title(u"Ajustement par moindres carrés.")
pl.text(u2030 - 20.0, v2030, "%.3f" % (v2030[0]))
pl.savefig("normale-transport.pdf", bbox_inches="tight")

#
# 2. La fonction polynomial_fit_normal_equations
print(u"")
print(u"2. La fonction polynomial_fit_normal_equations")
beta = polynomial_fit_normal_equations(t, y, 3)
print(u"beta=", beta)
u = linspace(1970, 2020, 100)
v = polynomial_value(beta, u)

# Make a plot
pl.figure(figsize=(2.0, 1.0))
pl.plot(t, y, "o")
pl.plot(u, v, "-")
pl.xlabel(u"")
pl.ylabel(u"Milliards")
pl.title(u"Ajustement par moindres carrés.")

#
# 3. Prédire le nombre de passagers en 2030
print(u"")
print(u"3. Prédire le nombre de passagers en 2030")
beta = polynomial_fit_normal_equations(t, y, 3)
u = array([2030.0])
pop = polynomial_value(beta, u)
print(u"Nombre de passagers en 2030=", pop)

#########################################
#
# Optionnel
#
print(u"")
print(u"##################################")
print(u"Optionnel")

#
# 4. Teste d'autres degrés
# Observons le conditionnement qui augmente quand le degré augmente
print(u"")
print(u"4. Teste d'autres degrés polynomiaux.")
u = linspace(1970, 2020, 100)
# Degree 1
beta = polynomial_fit_normal_equations(t, y, 1)
v2 = polynomial_value(beta, u)
# Degree 2
beta = polynomial_fit_normal_equations(t, y, 2)
v3 = polynomial_value(beta, u)
# Degree 3
beta = polynomial_fit_normal_equations(t, y, 3)
v4 = polynomial_value(beta, u)
# Make a plot
pl.figure(figsize=(2.0, 1.0))
pl.plot(t, y, "o")
pl.plot(u, v2, "-", label="Degré 1")
pl.plot(u, v3, "--", label="Degré 2")
pl.plot(u, v4, "-.", label="Degré 3")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.xlabel(u"")
pl.ylabel(u"Milliards")
pl.title(u"Ajustement par moindres carrés.")
pl.savefig("normale-ajustement.pdf", bbox_inches="tight")

# 5. Normaliser les données
# Voir le conditionnement
print(u"")
print(u"5. Normaliser les données")
print(u"Avec des données non normalisées")
print(u"Degré 1")
beta = polynomial_fit_normal_equations(t, y, 1)
print(beta)
print(u"Degré 2")
beta = polynomial_fit_normal_equations(t, y, 2)
print(beta)
print(u"Degré 3")
beta = polynomial_fit_normal_equations(t, y, 3)
print(beta)
# Normaliser les données
print(u"Avec des données normalisées")
tmin = t.min()
tmax = t.max()
delta = (tmax - tmin) / 2.0
tcentre = tmin + delta
s = (t - tcentre) / delta
print(u"s=", s)
print(u"Degré 1")
beta = polynomial_fit_normal_equations(s, y, 1)
print(beta)
print(u"Degré 2")
beta = polynomial_fit_normal_equations(s, y, 2)
print(beta)
print(u"Degré 3")
beta = polynomial_fit_normal_equations(s, y, 3)
print(beta)
#
# 6. Prédire le nombre de passagers en 2030
# avec des données normalisées
print(u"6. Prédire le nombre de passagers en 2030")
print(u"avec des données normalisées.")
print(u"With scaled data")
s = (t - tcentre) / delta
beta = polynomial_fit_normal_equations(s, y, 2)
u = array([2030.0])
s = (u - tcentre) / delta
pop = polynomial_value(beta, s)
print(u"Nombre de passagers en 2030=", pop)

# 7. Cholesky
print(u"7. Cholesky")

n = 3
X = vander(t, n)
A = X.T @ X
b = X.T @ y
L = cholesky(A)
z = solve(L, b)
betabis = solve(L.T, z)
print(betabis)
