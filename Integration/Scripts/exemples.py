#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

from math import pi
from scipy import special
from quadrature import adaptsim
from floats import computeDigits
import numpy as np
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
# Exemple A : Singularite non integrable
#
print(u"")
print(u"Exemple A : Singularite non integrable")


def myfunA(x):
    y = 1.0 / (2.0 * x - 1.0)
    return y


# Make a plot
x = np.linspace(0.0, 0.9, 100)
y = myfunA(x)
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"$1/(2x-1)$")
pl.savefig("exemples-inv2x.pdf", bbox_inches="tight")

if False:
    Q, fcount = adaptsim(myfunA, 0.0, 0.9)

#
# Exemple B : Sans probleme
#
print(u"")
print(u"Exemple B : Sans probleme")


def myfunB(x):
    y = 1.0 / np.sqrt(1.0 + x ** 4)
    return y


# Make a plot
x = np.linspace(0.0, 1.0, 100)
y = myfunB(x)
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"$1/\sqrt{1+x^4}$")
pl.savefig("exemples-invsqrt.pdf", bbox_inches="tight")

# http://www.wolframalpha.com/
# integral from 0 to 1 1/sqrt(1+x^4)
Q, fcount = adaptsim(myfunB, 0.0, 1.0)
expected = 0.927037338650685959
print(u"expected=", expected)
print(u"Q=", Q)
digits = computeDigits(expected, Q, 10)
print(u"Digits=", digits)
print(u"fcount=", fcount)
# Q,fcount=adaptsim_gui(myfunB,0.,2./3.)

#
# Exemple C : Singularite apparente
#
print(u"")
print(u"Exemple C : Singularite apparente")


def mysinc(x):
    y = np.sin(x) / x
    return y


# Make a plot
x = np.linspace(0.0, pi, 100)
y = mysinc(x)
pl.figure(figsize=(2.0, 1.0))
pl.plot(x, y, "-")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.title(u"$\sin(x)/x$")
pl.savefig("exemples-sinc.pdf", bbox_inches="tight")

# integral from 0 to pi sin(x)/x
if False:
    # ZeroDivisionError: float division
    Q, fcount = adaptsim(mysinc, 0.0, pi)
    expected = 1.85193705198246617036
    print(u"expected=", expected)
    print(u"Q=", Q)
    digits = computeDigits(expected, Q, 10)
    print(u"Digits=", digits)
    print(u"fcount=", fcount)

#
# Exemple D : Gerer une singularite apparente I
#
print(u"")
print(u"Exemple D : Gerer une singularite apparente I")
# integral from 0 to pi sin(x)/x
afterzero = np.nextafter(0.0, pi)
print(u"afterzero=", afterzero)
Q, fcount = adaptsim(mysinc, afterzero, pi)
expected = 1.85193705198246617036
print(u"expected=", expected)
print(u"Q=", Q)
digits = computeDigits(expected, Q, 10)
print(u"Digits=", digits)
print(u"fcount=", fcount)
# Q,fcount=adaptsim_gui(mysinc,afterzero,pi)

#
# Exemple E : Gerer une singularite apparente II
#
print(u"")
print(u"Exemple E : Gerer une singularite apparente II")


def mysincbis(x):
    if x == 0:
        y = 1.0
    else:
        y = np.sin(x) / x
    return y


# integral from 0 to pi sin(x)/x
Q, fcount = adaptsim(mysincbis, 0.0, pi)
expected = 1.85193705198246617036
print(u"expected=", expected)
print(u"Q=", Q)
digits = computeDigits(expected, Q, 10)
print(u"Digits=", digits)
print(u"fcount=", fcount)

#
# Exemple F : Arguments supplementaires
#
print(u"")
print(u"Exemple F : Arguments supplementaires")


def betafun(t, z, w):
    y = t ** (z - 1) * (1.0 - t) ** (w - 1)
    return y


z = 8.0 / 3.0
w = 10.0 / 3.0
tol = 1.0e-6
Q, fcount = adaptsim(betafun, 0.0, 1.0, tol, z, w)
expected = 0.0348329096012058297782
print(u"expected=", expected)
print(u"from scipy/special=", special.beta(z, w))
print(u"Q=", Q)
digits = computeDigits(expected, Q, 10)
print(u"Digits=", digits)
print(u"fcount=", fcount)

##############################
#
# Optionnel
#
print(u"")
print(u"Optionnel")
#
# Extra-arguments of callbacks
print(u"Extra-arguments of callbacks")


def midpoint(f, a, b, *args):
    """
    M = midpoint(f,a,b) returns the value of
    f(c), where c=(a+b)/2.
    M = midpoint(f,a,b,a1,a2,...) returns the
    value of f(c,a1,a2,...), where c=(a+b)/2,
    and a1, a2,... are extra-arguments of f.
    """
    c = (a + b) / 2
    y = f(c, *args)
    return y


print(u"midpoint(myfunB,0,1)=", midpoint(myfunB, 0, 1))


def myfunBbis(x, a, b, c):
    y = a / np.sqrt(b + c * x ** 4)
    return y


print(u"midpoint(myfunBbis,0,1,1.,1.,1.)=", midpoint(myfunBbis, 0, 1, 1.0, 1.0, 1.0))
