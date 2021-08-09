#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Calcule la probabilité d'avoir une taille inférieure ou supérieure à 2 mètres, 
sous l'hypothèse que la distribution de la taille des hommes suit une loi 
Gaussienne.
On pourrait utiliser le module scipy.stats pour faire le calcul, mais 
on utilise une méthode d'intégration numérique.

Référence
---------
Statistical Abstract of the United States U.S. Census Bureau. 
Table 209. cumulative percent distribution of population 
by height and sex : 2007-2008
2012
https://www.census.gov/compendia/statab/2012/tables/12s0209.pdf.
"""
import numpy as np
import pylab as pl
from quadrature import adaptsim
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def gausspdf(x, mu, sigma):
    z = (x - mu) / sigma
    y = np.exp(-(z ** 2) / 2.0) / (sigma * np.sqrt(2 * np.pi))
    return y


mu = 1.7633
sigma = 0.0680
n = 100
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, n)
y = gausspdf(x, mu, sigma)
#
fig = pl.figure(figsize=(3.0, 2.0))
pl.plot(x, y)
pl.xlabel(u"Taille (m)")
pl.ylabel(u"Densité")
pl.title(u"Hommes de 20 à 79 ans")
pl.savefig("taille.pdf", bbox_inches="tight")

# Probabilité d'avoir une taille inférieure à 2 (m)
a = mu - 40 * sigma
b = 2.0
tol = 1.0e-7
Q, fcount = adaptsim(gausspdf, a, b, tol, mu, sigma)
print(u"P(T<2)=", Q)
print(u"fcount=", fcount)

# Probabilité complémentaire d'avoir une taille inférieure à 2 (m)
a = 2.0
b = mu + 40 * sigma
tol = 1.0e-7
Q, fcount = adaptsim(gausspdf, a, b, tol, mu, sigma)
print(u"P(T>2)=", Q)
print(u"fcount=", fcount)
