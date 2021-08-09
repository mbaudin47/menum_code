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
utilise la méthode QR. 
"""
from numpy import array, linspace, vander, set_printoptions
from numpy.linalg import qr, norm, solve, cond
from pylab import plot, title, figure, xlabel, ylabel
from leastsq import polynomial_fit, polynomial_value
from math import log10

#
# 1. Ajustement polynomial par la décomposition QR
print(u"")
print(u"1. Ajustement polynomial par la décomposition QR")
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
#
# Résoudre par QR
print(u"")
print(u"Résoudre par QR")
n = 3
X = vander(t, n)
Q, R = qr(X)
print(u"Q=")
print(Q)
print(u"R=")
print(R)
print(u"log10(cond(R))=", log10(cond(R)))
z = Q.T @ y
beta = solve(R, z)
print(u"beta=")
print(beta)

#
# 2. Utiliser polynomial_fit et polynomial_value
print(u"")
print(u"2. Utiliser polynomial_fit et polynomial_value")
beta = polynomial_fit(t, y, 3)
print(u"beta=", beta)
u = linspace(1970, 2040, 100)
v = polynomial_value(beta, u)
# Faire un dessin
figure()
plot(t, y, "o")
plot(u, v, "r-")
xlabel(u"")
ylabel(u"Milliards")
title(u"Ajustement polynomial (QR)")

# 3. Prédire le nombre de passagers en 2030
print(u"")
print(u"3. Prédire le nombre de passagers en 2030")
beta = polynomial_fit(t, y, 3)
u = array([2030.0])
pop = polynomial_value(beta, u)
print(u"Passagers en 2030=", pop)

#########################################
#
# Optionnel
#
print(u"")
print(u"##################################")
print(u"Optionnel")

#
# 4. Mettre les données à l'échelle
# Voir le conditionnement
print(u"")
print(u"4. Mettre les données à l'échelle.")
print(u"Degré 1")
beta = polynomial_fit(t, y, 1)
print(u"beta=", beta)
print(u"Degré 2")
beta = polynomial_fit(t, y, 2)
print(u"beta=", beta)
print(u"Degré 3")
beta = polynomial_fit(t, y, 3)
print(u"beta=", beta)
# Mettre les données à l'échelle
print(u"Avec des données normalisées")
tmin = t.min()
tmax = t.max()
delta = (tmax - tmin) / 2.0
tcentre = tmin + delta
s = (t - tcentre) / delta
print(u"s=", s)
print(u"Degré 2")
beta = polynomial_fit(s, y, 1)
print(u"beta=", beta)
print(u"Degré 3")
beta = polynomial_fit(s, y, 2)
print(u"beta=", beta)
print(u"Degré 4")
beta = polynomial_fit(s, y, 3)
print(u"beta=", beta)

#
# 5. Vérifier les propriétés de QR
print(u"")
print(u"5. Vérifier les propriétés de QR")
n = 3
X = vander(t, n)
Q, R = qr(X)
set_printoptions(precision=5)
print(u"Q=")
print(Q)
print(u"R=")
print(R)
print(u"Q[:,0] @ Q[:,1]=", Q[:, 0] @ Q[:, 1])
print(u"Q[:,0] @ Q[:,2]=", Q[:, 0] @ Q[:, 2])
print(u"Q[:,1] @ Q[:,2]=", Q[:, 1] @ Q[:, 2])
print(u"norm(Q[:,0])=", norm(Q[:, 0]))
print(u"norm(Q[:,1])=", norm(Q[:, 1]))
print(u"norm(Q[:,2])=", norm(Q[:, 2]))
#
# 6. Prédire le nombre de passagers en 2030
# avec des données normalisées
print(u"")
print(u"6. Prédire le nombre de passagers en 2030")
print(u"avec des données normalisées")
tmin = t.min()
tmax = t.max()
delta = (tmax - tmin) / 2.0
tcentre = tmin + delta
s = (t - tcentre) / delta
beta = polynomial_fit(s, y, 2)
u = array([2030.0])
s = (u - tcentre) / delta
pop = polynomial_value(beta, s)
print(u"Passagers en 2030=", pop)
