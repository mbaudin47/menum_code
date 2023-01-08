#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
On considère la durée de vie d'un composant électronique en fonction de 
la température :
    
    MTTF = C exp(T0/T)

où T est la température et C et T0 sont des constantes. 
En utilisant le logarithme, on obtient :

log(MTTF) = log(C) + T0/T

On utilise la méthode des moindres carrés linéaires pour déterminer 
les coefficients d'un polynôme de degré 1 s'ajustant aux observations. 
On en déduit C et T0.

The mean time to failure of an integrated circuit 
obeys to the law :

    MTTF = C exp(T0/T)

where T is the operating temperature and 
C and T0 are constants.

log(MTTF) = log(C) + T0/T

Références
----------
Alan S. Morris, Reza Langari. 
Measurement and Instrumentation: Theory and Application, p.205
https://books.google.fr/books?id=arw7FIVkVb4C&pg=PA205

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import pylab as pl
from numpy import array, linspace
from leastsq import polynomial_fit_normal_equations
from numpy import log, exp
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# Temperature (K)
temp = array([600.0, 580.0, 560.0, 540.0, 520.0, 500.0])
# hours
MTTF = array([54.0, 105.0, 206.0, 411.0, 941.0, 2145.0])

print(array([1.0 / temp, log(MTTF)]).T)

degre = 1
bet = polynomial_fit_normal_equations(1.0 / temp, log(MTTF), degre)

t = linspace(500.0, 600.0)
l = bet[0] / t + bet[1]

# Plot data and fit
pl.figure(figsize=(1.5, 1.0))
pl.plot(1000 * 1.0 / temp, log(MTTF), "o", label=u"Données")
pl.xlabel(u"$1000 / T$ (1/K)")
pl.ylabel(u"$\\log(MTTF)$")
pl.plot(1000 * 1.0 / t, l, "-", label="Droite")
pl.savefig("mttf-log.pdf", bbox_inches="tight")

print(u"bet=", bet)
T0 = bet[0]
print(u"T0=", T0)
C = exp(bet[1])
print(u"C=", C)

pl.figure(figsize=(1.5, 1.0))
pl.plot(temp, MTTF, "o", label=u"Données")
pl.plot(t, C * exp(T0 / t), "-", label=u"Droite")
pl.xlabel(u"$T$ (K)")
pl.ylabel(u"$MTTF$ (heures)")
pl.savefig("mttf-exp.pdf", bbox_inches="tight")
