#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Un modèle de frasil simplifié à 3 paramètres.

Références
Urban Svensson et Anders Omstedt. « Report on frazil ice ». In : Cold
Regions Science and Technology 22.3 (1994), p. 221-233.

Urban Svensson et Anders Omstedt. « Simulation of supercooling and
size distribution in frazil ice dynamics ». In : Cold Regions Science and
Technology 22.3 (1994), p. 221-233.

Fabien Souillé, Florent Taccone et Chaymae El Mertahi. « A Multi-
class Frazil Ice Model for Shallow Water Flows ». In : Online proceedings
of the papers submitted to the 2020 TELEMAC-MASCARET User Confe-
rence October 2020. 2020, p. 122-129.

Torkild Carstens. « Experiments with supercooling and ice formation
in flowing water ». 1966.

"""

import numpy as np
from odes import bogacki_shampine
import pylab as pl
import scipy.special as scp
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def frasil(y, t):
    T, C = y
    dTdt = -phi - alpha * T * C
    dCdt = -beta * T * C
    dydt = np.array((dTdt, dCdt))
    return dydt


# Paramètres
phi = 4.0e-4
alpha = 66.87
beta = 0.9177

# Intervalle de temps
t_min = 0.0
t_max = 600.0
tspan = [t_min, t_max]

# Condition initiale
T0 = 0.0
C0 = 1.0e-8

# Resoudre l'ODE
y0 = [T0, C0]
t, y = bogacki_shampine(frasil, tspan, y0)

###########################################################
# Calcul de la date critique

# Approché
C0 = 1.0e-8
a = 1.0 / (C0 * alpha)
w = scp.lambertw(beta * phi * a ** 2)
tc = np.sqrt(w.real / (beta * phi))
Tc = -phi * tc
Cc = C0 * np.exp(0.5 * beta * phi * tc ** 2)
print(u"tc=", tc, "Tc=", Tc, "Cc=", Cc)

# Trajectoire
pl.figure(figsize=(3.0, 2.5))
pl.suptitle(u"Dynamique du frasil.")
#
pl.subplot(2, 1, 1)
pl.plot(t, y[:, 0], "-")
pl.plot(tc, Tc, "o")
pl.xlabel(u"")
pl.ylabel(u"T (°C)")
#
pl.subplot(2, 1, 2)
pl.plot(t, y[:, 1], "-")
pl.plot(tc, Cc, "o")
pl.xlabel(u"t (s)")
pl.ylabel(u"C")
pl.subplots_adjust(hspace=0.3)
pl.savefig("frasil-dynamique.pdf", bbox_inches="tight")

########################################################
# Plusieurs conditions initiales
#
pl.figure(figsize=(2.0, 2.5))
pl.suptitle(u"Sensibilité à la condition initiale $y_0=(T_0, C_0)$.")
ax1 = pl.subplot(2, 1, 1)
pl.xlabel(u"")
pl.ylabel(u"T (°C)")
ax2 = pl.subplot(2, 1, 2)
pl.xlabel(u"t (s)")
pl.ylabel(u"C")
#
index = 0
line_style = ["-", "--", "-.", ":"]
for T0 in [-0.1, 0.1]:
    for C0_exponent in [-7, -9]:
        C0 = 10.0 ** C0_exponent
        y0 = [T0, C0]
        t, y = bogacki_shampine(frasil, tspan, y0)
        ax1.plot(
            t, y[:, 0], line_style[index], label="$(%.1f,10^{%d})$" % (T0, C0_exponent)
        )
        ax2.plot(
            t, y[:, 1], line_style[index], label="$(%.1f,10^{%d})$" % (T0, C0_exponent)
        )
        index += 1

_ = ax1.legend(bbox_to_anchor=(1.0, 1.0))
_ = ax2.legend(bbox_to_anchor=(1.0, 1.0))
pl.subplots_adjust(wspace=0.4, hspace=0.3)
pl.savefig("frasil-dynamique-sensibilite.pdf", bbox_inches="tight")

########################################################
# Plusieurs conditions initiales dans l'espace des phases
#
pl.figure(figsize=(2.5, 1.5))
pl.title(u"Sensibilité à la condition initiale $y_0=(T_0, C_0)$.")
pl.xlabel(u"T (°C)")
pl.ylabel(u"C")
index = 0
line_style = ["-", "--", "-.", ":"]
for T0 in [-0.1, 0.1]:
    for C0_exponent in [-7, -9]:
        C0 = 10.0 ** C0_exponent
        y0 = [T0, C0]
        t, y = bogacki_shampine(frasil, tspan, y0)
        pl.plot(
            y[:, 0],
            y[:, 1],
            line_style[index],
            label="$(%.1f,10^{%d})$" % (T0, C0_exponent),
        )
        index += 1
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("frasil-phases-sensibilite.pdf", bbox_inches="tight")
