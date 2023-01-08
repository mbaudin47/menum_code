#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin

"""
Pour un gaz réel, l'équation PV = nRT ne modélise pas correctement 
l'équilibre thermodynamique. 
On peut utiliser alors l'équation de Van Der Waals pour calculer la 
pression par résolution d'une équation non linéaire. 

For a mole of a perfect gas, the state equation
Pv = RT
establishes a relation between the pressure P of the 
gas (in Pascals [Pa]), the specific volume 
v (in cubic meters per kilogram [m3 Kg-1]) and 
its temperature T (in Kelvin [K]), R being the universal 
gas constant, expressed in [JKg-1K-1]
(joules per kilogram per Kelvin).
For a real gas, the deviation from the state equation of perfect gases is
due to van der Waals and takes into account the intermolecular interaction
and the space occupied by molecules of finite size.
Denoting by a and b the gas constants according to the van der Waals
model, in order to determine the specific volume v of the gas, once P and
T are known, we must solve a nonlinear equation.

Références
----------
Numerical Mathematics, Alfio Quarteroni, Riccardo Sacco, Fausto Saleri, 
Springer, Texts in Applied Mathematics, Volume 37, 2007, Chapitre 6, 
"6.7.1 Analysis of the State Equation for a Real Gas", p.276

Redlich–Kwong equation of state
Dieterici model
Clausius model
Virial model
Peng–Robinson model
Wohl model
Beattie–Bridgman model
http://en.wikipedia.org/wiki/Real_gas

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from sys import float_info
from fzero import zeroin, bisection, newton
from numpy import linspace, zeros
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def calculeVolume(n, T, P):
    print(u"Nombre de moles:", n)
    print(u"Temperature:", T, "(K), ", kelvinToCelsius(T), " (C)")
    print(u"Pression=", P, " (Pa)", " = ", pascalToPatm(P), " (atm)")
    # Ideal
    V = (n * R * T) / P
    print(u"Idéal")
    afficheVolume(V, M)
    # Van Der Waals - zeroin
    Vmin = V / 10.0
    Vmax = V * 10.0
    reltolx = None
    abstolx = 0.0
    verbose = False
    V, history = zeroin(
        vanderwaalsSolve, Vmin, Vmax, reltolx, abstolx, verbose, a, b, n, R, T, P
    )
    print(u"Van Der Waals - zeroin")
    print(u"    Iterations:", len(history))
    print(u"    P(V)-p:", vanderwaalsSolve(V, a, b, n, R, T, P))
    afficheVolume(V, M)
    # Van Der Waals - bisection
    Vmin = 0.001
    Vmax = 0.1
    reltolx = None
    V, history = bisection(
        vanderwaalsSolve, Vmin, Vmax, reltolx, abstolx, verbose, a, b, n, R, T, P
    )
    print(u"Van Der Waals - bisection")
    print(u"    Iterations:", len(history))
    print(u"    P(V)-p:", vanderwaalsSolve(V, a, b, n, R, T, P))
    afficheVolume(V, M)
    # Van Der Waals - newton
    V0 = V
    reltolx = None
    V, history = newton(
        vanderwaalsSolve, V0, vanderwaalsSolvePrime, reltolx, abstolx, verbose, a, b, n, R, T, P
    )
    print(u"Van Der Waals - newton")
    print(u"    Iterations:", len(history))
    print(u"    P(V)-p:", vanderwaalsSolve(V, a, b, n, R, T, P))
    afficheVolume(V, M)
    return None


def afficheVolume(V, M):
    """
    V : volume (m3)
    M : masse molaire (kg/mol)
    """
    print(u"    Volume =%.17e(m3)" % V)
    rho = density(M, V)
    print(u"    Density=", rho, "(kg/m3)")
    v = 1.0 / rho
    print(u"    Specific Volume=", v, "(m3/kg)")
    return None


def calculePression(n, T, V):
    """
    n : Nombre de moles
    V : Volume (m3)
    T : Temperature (K)
    """
    print(u"Nombre de moles:", n)
    print(u"Temperature:", T, "(K), ", kelvinToCelsius(T), " (C)")
    print(u"Volume:", V, " (m3), ", 1000 * V, "(L)")
    P = pressionGazIdeal(n, R, T, V)
    patm = pascalToPatm(P)
    print(u"Idéal")
    print(u"    Pression=", P, " (Pa)", " = ", patm, " (atm)")
    P = pressionVanDerWaals(V, a, b, n, R, T)
    patm = pascalToPatm(P)
    print(u"Van Der Waals")
    print(u"    Pression=", P, " (Pa)", " = ", patm, " (atm)")
    return None


def pressionGazIdeal(n, R, T, V):
    """
    V : volume (m3)
    P : pression (Pa)
    R : constante universelle des gaz parfaits
    T : température (K)
    """
    P = n * R * T / V
    return P


def pressionVanDerWaals(V, a, b, n, R, T):
    """
    V : volume (m3)
    P : pression (Pa)
    a,b : constantes
    R : constante universelle des gaz parfaits
    T : température (K)
    """
    P = n * R * T / (V - n * b) - a * (n / V) ** 2
    return P


def celsiusToKelvin(Tcelsius):
    C2K = -273.15  # Celsius to Kelvin
    Tkelvin = Tcelsius - C2K  # temperature (Kelvin)
    return Tkelvin


def kelvinToCelsius(Tkelvin):
    C2K = -273.15  # Celsius to Kelvin
    Tcelsius = Tkelvin + C2K  # temperature (Kelvin)
    return Tcelsius


def patmToPascal(patm):
    oneatm = 101325.0  # Pa (Pa)
    Ppascal = patm * oneatm
    return Ppascal


def pascalToPatm(Ppascal):
    oneatm = 101325.0  # Pa (Pa)
    patm = Ppascal / oneatm
    return patm


def volume(molarMass, density):
    V = molarMass / density
    return V


def density(molarMass, volume):
    rho = molarMass / volume
    return rho


def vanderwaalsSolve(V, a, b, n, R, T, P):
    """
    V : volume (m3)
    P : pression (Pa)
    a,b : constantes
    R : constante universelle des gaz parfaits
    T : température (K)
    """
    y = P - pressionVanDerWaals(V, a, b, n, R, T)
    return y


def vanderwaalsSolvePrime(V, a, b, n, R, T, P):
    """
    Calcule la dérivée de vanderwaalsSolve.
    """
    h = (float_info.epsilon) ** (1.0 / 3.0)
    y1 = vanderwaalsSolve(V + h, a, b, n, R, T, P)
    y2 = vanderwaalsSolve(V - h, a, b, n, R, T, P)
    yp = (y1 - y2) / (2 * h)
    return yp


print(u"CO2")

kB = 1.380648813e-23  # Boltzman constant
NA = 6.0221412927e23  # Avogadro constant

M = 0.04401  # Molar mass of CO2 (kg/mol)
P = 1013250.0  # (Pa) = 10 atm
T = 300.0  # (K)
a = 188.33  # (Pam6Kg-2)
b = 9.77e-4  # (m3Kg-1)
R = 8.314472  # (J.K-1.mol-1) Universal gas constant
RCO2 = 188.9  # (J.kg-1.K-1)


######################################################


T = 300.0  # (K)
n = 1
a = 0.364
b = 4.267e-5
npoints = 1000
Vmin = 1.0e-4
Vmax = 0.1
V = linspace(Vmin, Vmax, npoints)
PGP = zeros(npoints)
PVDW = zeros(npoints)
for i in range(npoints):
    PGP[i] = pressionGazIdeal(n, R, T, V[i])
    PVDW[i] = pressionVanDerWaals(V[i], a, b, n, R, T)

patmGP = pascalToPatm(PGP)
patmVDW = pascalToPatm(PVDW)
rho = density(M, V)

pl.figure(figsize=(3.0, 2.0))
pl.title(u"Température =300 (K)")
pl.xlabel(u"Densité (kg/m3)")
pl.ylabel(u"Pression (atm)")
pl.plot(rho, patmGP, "-", label="Gaz parfait")
pl.plot(rho, patmVDW, "--", label="Van Der Waals")
pl.legend(loc="best")

pl.figure(figsize=(2.0, 1.0))
pl.title(u"Température =300 (K)")
pl.xlabel(u"Volume ($m^3$)")
pl.ylabel(u"Pression ($10^5$ Pa)")
pl.plot(V, PGP / 1.0e5, "-", label="Gaz parfait")
pl.plot(V, PVDW / 1.0e5, "--", label="Van Der Waals")
pl.xscale("log")
pl.yscale("log")
pl.ylim(top=1.0e3)
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("VanDerWaals.pdf", bbox_inches="tight")

###############################
# http://users.wfu.edu/macoskjc/Courses/HWChpt%201.pdf
"""
At T=300 K, 1.00 mol of CO2 occupies a volume of 1.50 L. 
Calculate the pressures given by the ideal gas equation 
and the van der Waals equation.
Ideal gas :     p = 16.4 atm
Van der Waals : p = 15.3 atm
"""
print(u"------------------")
n = 1  # Nombre de moles
V = 1.5e-3  # Volume (m3)
T = 300  # Temperature (K)
calculePression(n, T, V)

###############################


###############################
#
"""
http://physics.ucsc.edu/~joel/Phys5D/13Phys5D-Lecture7.pdf
At T = 273K, applying the ideal gas law to 1 mole of CO2 in V = 22.4 L 
we get P = 1 atm (STP).
Using the van der Waals equation, we find 
P = 0.995 atm, so indeed P is slightly less.
"""
print(u"------------------")
n = 1
T = 273.0
V = 22.4 / 1000.0
calculePression(n, T, V)

"""
But the situation reverses at high density, where the RT/(V-b) term 
becomes more important.
For example, if we compress the CO2 from V = 22.4 L to V = 0.05 L, 
the ideal gas law gives P = 448 atm while the van der Waals 
equation gives 1620 atm, so at high density the pressure P is greater 
than that predicted by the ideal gas law.
"""
print(u"------------------")
n = 1
T = 273.0
V = 0.05 / 1000.0
calculePression(n, T, V)

#################################################
# http://en.wikipedia.org/wiki/Carbon_dioxide
print(u"------------------")
print(u"Calcule volume de CO2")
n = 1  # Number of moles
T = 300.0  # Temperature (Degre Celsius)
P = 2.0e5
calculeVolume(n, T, P)

"""
Attention
Si P>6 atm, le CO2 est liquide et 
l'équation de VDW ne s'applique plus.

"Screening and ranking of sedimentary basins for sequestration of CO2
in geological media in response to climate change"
Stefan Bachu, Environmental Geology (2003) 44:277–289
"""
