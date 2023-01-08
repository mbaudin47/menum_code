#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Calcule le conditionnement des fonctions sin, cos et tan.

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
import pylab as pl
import numpy as np
import matplotlibpreferences

matplotlibpreferences.load_preferences()

figwidth = 1.0
figheight = 1.5

# Sinus
def sinCond(x):
    n = x.shape[0]
    y = np.ones((n, 1))
    indices = np.where(x != 0)[0]
    y = abs(x[indices] * np.cos(x[indices]) / np.sin(x[indices]))
    return y

N = 1000
x = np.linspace(-2 * np.pi, 2 * np.pi, N)
y = np.sin(x)
c = sinCond(x)
#
pl.figure(figsize=(figwidth, figheight))
pl.subplot(2, 1, 1)
pl.plot(x, y, "-")
pl.ylabel(u"$\sin$")
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.ylim([1.0e-3, 1.0e3])
pl.yscale("log")
pl.xlabel(u"$x$")
pl.ylabel(u"Cond. de sin")
pl.subplots_adjust(hspace=0.6, top=0.85)
pl.savefig("condition-trigonometrie-sin.pdf", bbox_inches="tight")

# Cosinus


def cosCond(x):
    y = abs(x * np.sin(x) / np.cos(x))
    return y


N = 1000
x = np.linspace(-2 * np.pi, 2 * np.pi, N)
y = np.cos(x)
c = cosCond(x)
#
pl.figure(figsize=(figwidth, figheight))
pl.subplot(2, 1, 1)
pl.plot(x, y, "-")
pl.ylabel(u"$\cos$")
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.ylim([1.0e-3, 1.0e3])
pl.yscale("log")
pl.xlabel(u"$x$")
pl.ylabel(u"Cond. de cos")
pl.subplots_adjust(hspace=0.6, top=0.85)
pl.savefig("condition-trigonometrie-cos.pdf", bbox_inches="tight")

# Tan


def tanCond(x):
    y = abs(x / np.sin(x) / np.cos(x))
    return y


N = 1000
x = np.linspace(-2 * np.pi, 2 * np.pi, N)
y = np.tan(x)
c = tanCond(x)
#
pl.figure(figsize=(figwidth, figheight))
pl.subplot(2, 1, 1)
pl.plot(x, y, "-")
pl.ylabel(u"$\\tan$")
pl.ylim([-10, 10])
#
pl.subplot(2, 1, 2)
pl.plot(x, c, "-")
pl.ylim([1.0e-0, 1.0e3])
pl.yscale("log")
pl.xlabel(u"$x$")
pl.ylabel(u"Cond. de tan")
pl.ylim(top=1.0e3)
pl.subplots_adjust(hspace=0.6, top=0.85)
pl.savefig("condition-trigonometrie-tan.pdf", bbox_inches="tight")
