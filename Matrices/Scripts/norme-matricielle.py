#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
On considère une matrice A de taille 2-par-2.
Soit C le cercle unité, de centre l'origine du repère et de rayon égal à 1.
Les points x sont choisis en utilisant les coordonnées polaires :
    x1 = cos(theta)
    x2 = cos(theta)
où theta est dans l'intervalle [0, 2pi]. 
Alors x est dans C.
On choisit un ensemble d'angles theta sur une grille régulière 
de n = 1000 points entre 0 et 2pi. 
Le script dessine le point y = A * x pour une 
collection de points x dans C. 
C'est une ellipse, dont les demi-axes dépendent des valeurs et vecteurs 
singuliers de la matrice. 

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from numpy import linspace, cos, sin, array, argmax, inf
from numpy.linalg import norm
from math import pi
import pylab as pl
from numpy import zeros
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# Plot A*x
A = array([[1.0, 2.0], [3.0, 4.0]])
r = 1
m = 1000
t = linspace(0, 2 * pi, m)
# Plot the unit circle
x = zeros((2, m))
x[0, :] = r * cos(t)
x[1, :] = r * sin(t)
pl.figure(figsize=(2.5, 1.0))
pl.plot(x[0, :], x[1, :], "-", label="$x$")
pl.xlabel(u"$x_1$")
pl.ylabel(u"$x_2$")
pl.axis("equal")
# Plot the image ellipse
b = A @ x
pl.plot(b[0, :], b[1, :], "--", label="$Ax$")
pl.legend()
pl.savefig("norme-matricielle.pdf", bbox_inches="tight")


def vectorMaxNorm1(A):
    """
    Calcule le vecteur x qui maximise
    la norme 1 de ||A*x||/||x||
    """
    k = argmax(sum(abs(A), 0))
    n = A.shape[1]
    x = zeros(n)
    x[k] = 1.0
    return x


A = array([[1.0, 2.0], [3.0, 4.0]])
x = vectorMaxNorm1(A)
print(u"Max norm-1 vector:")
print(x)
print(u"Max :")
print(x)
b = A @ x
ratio = norm(b, 1) / norm(x, 1)
print(u"(%.2f,%.2f), ratio=%.2f" % (x[0], x[1], ratio))

# Brute-force search !
print(u"Brute-force search !")
r = 1
m = 21
t = linspace(0, 2 * pi, m)
x = zeros((2, m))
x[0, :] = r * cos(t)
x[1, :] = r * sin(t)
b = A @ x
for i in range(m):
    ratio = norm(b[:, i], 1) / norm(x[:, i], 1)
    print(u"(%.2f,%.2f), ratio=%.2f" % (x[0, i], x[1, i], ratio))


def vectorMaxNormInf(A):
    """
    Calcule le vecteur x qui maximise
    la norme infinie de ||A*x||/||x||
    """
    k = argmax(sum(abs(A), 1))
    n = A.shape[1]
    x = zeros(n)
    for j in range(n):
        if A[k, j] > 0:
            x[j] = 1.0
        elif A[k, j] < 0:
            x[j] = -1.0
    return x


A = array([[1.0, 2.0], [3.0, 4.0]])
x = vectorMaxNormInf(A)
print(u"Max norm-inf vector:")
print(x)
print(u"Max :")
print(x)
b = A * x
ratio = norm(b, inf) / norm(x, inf)
print(u"(%.2f,%.2f), ratio=%.2f" % (x[0], x[1], ratio))

# Brute-force search !
print(u"Brute-force search !")
r = 1
m = 101
t = linspace(0, 2 * pi, m)
x = zeros((2, m))
x[0, :] = r * cos(t)
x[1, :] = r * sin(t)
b = A @ x
for i in range(m):
    ratio = norm(b[:, i], inf) / norm(x[:, i], inf)
    print(u"(%.2f,%.2f), ratio=%.2f" % (x[0, i], x[1, i], ratio))
