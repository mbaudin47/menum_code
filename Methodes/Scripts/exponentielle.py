#!/usr/bin/python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Montre l'utilité de la fonction expm1 sur un exemple concret de 
calcul de probabilité.
Evalue la fonction de répartition de la loi exponentielle.

Soit X la durée de vie d'une batterie de voiture en km. 
Supposons que X suit une loi exponentielle de moyenne 20 000. 
En d'autres termes, la durée de vie moyenne d'une telle batterie 
est de 20 000 km. 
* Quelle est la probabilité que la durée de vie soit inférieure 
à 10^-12 km = 1 nano mètre ?

Reference 
---------
Introduction to Probability and Statistics for Engineers 
and Scientists 3rd ed 
Section 5.6 - Exponentials Random Variables
S. Ross (Elsevier, 2004)

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from math import exp, log, expm1, log1p


#
# 1. Fonction de repartition naive
def expcdfNaive(x, mu):
    """
    Fonction de repartition de
    la loi exponentielle de moyenne mu.
    Implementation naive.

    Calling Sequence
    p=expcdfNaive(x,mu)

    Parametres
    x : un reel positif >=0
    mu : un reel positif >0, la moyenne
    p : un reel, la probabilite que X<=x
    """
    p = 1.0 - exp(-x / mu)
    return p


def expcdfRobust(x, mu):
    """
    Fonction de repartition de
    la loi exponentielle de moyenne mu.
    Implementation robuste.

    Calling Sequence
    p=expcdfRobust(x,mu)

    Parametres
    x : un reel positif >=0
    mu : un reel positif >0, la moyenne
    p : un reel, la probabilite que X<=x
    """
    p = -expm1(-x / mu)
    return p


mu = 20000.0
#
print(u"Cas #1")
x = 10000
print(u"x=", x, ", mu=", mu)
print(u"exact : P(X<x)=0.3934693")
print(u"Naive=", expcdfNaive(x, mu))
print(u"Robust=", expcdfRobust(x, mu))
#
print(u"")
print(u"Cas #2")
x = 1.0e-12
print(u"x=", x, ", mu=", mu)
print(u"exact : P(X<x)=5.D-17")
print(u"Naive=", expcdfNaive(x, mu))
print(u"Robust=", expcdfRobust(x, mu))

#
# 2. Quantile
def expinvNaive(p, mu):
    """
    Fonction de repartition inverse (quantile) de
    la loi exponentielle de moyenne mu.
    Implementation naive.

    Calling Sequence
    x=expinvNaive(p,mu)

    Parametres
    p : un reel, dans l'intervalle [0,1]
    mu : un reel positif >0, la moyenne
    x : un reel positif >=0
    """
    if p == 1.0:
        x = float("inf")
    else:
        x = -mu * log(1.0 - p)
    return x


def expinvRobust(p, mu):
    """
    Fonction de repartition inverse (quantile) de
    la loi exponentielle de moyenne mu.
    Implementation robuste.

    Calling Sequence
    x=expinvNaive(p,mu)

    Parametres
    p : un reel, dans l'intervalle [0,1]
    mu : un reel positif >0, la moyenne
    x : un reel positif >=0
    """
    if p == 1.0:
        x = float("inf")
    else:
        x = -mu * log1p(-p)
    return x


#
mu = 20000.0
print(u"")
print(u"Cas #1")
p = 1.0
print(u"p=", p, ", mu=", mu)
print(u"exact : x=INF")
print(u"Naive(x,mu)=", expinvNaive(p, mu))
print(u"Robust(x,mu)=", expinvRobust(p, mu))
#
print(u"")
print(u"Cas #2")
p = 0.5
print(u"p=", p, ", mu=", mu)
print(u"exact : x=0.6931472")
print(u"Naive(x,mu)=", expinvNaive(p, mu))
print(u"Robust(x,mu)=", expinvRobust(p, mu))
#
print(u"")
p = 5.0e-17
print(u"Cas #3")
print(u"exact : x=1.e-12")
print(u"Naive(x,mu)=", expinvNaive(p, mu))
print(u"Robust(x,mu)=", expinvRobust(p, mu))
