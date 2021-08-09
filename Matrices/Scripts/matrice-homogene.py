#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Le script illustre comment utiliser produit matrice-vecteur pour déterminer 
la géométrie d'un robot en utilisant les coordonnées homogènes. 
On considère un robot à deux bras A et B. 
En fonction des angles associés à A et B et de la longueur des deux bras, 
on analyse la position des deux points au bout des bras A et B.
On calcule la position du robot en utilisant une grille régulière de 7 points 
entre 0 et 2pi pour les deux angles des bras et on affiche les positions 
associées, ce qui montre la portée du robot. 

Références
2D Kinematics, SI 475  : Intelligent Robotics
Gavin Taylor,   USNA CS
"""

from numpy import array, linspace
from numpy import pi, sin, cos, sqrt
from math import atan
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

x0 = 3.0
y0 = -1.0
theta = pi / 4.0
lx = 1.0
ly = 2.0
#
T = array(
    [[cos(theta), -sin(theta), lx], [sin(theta), cos(theta), ly], [0.0, 0.0, 1.0]]
)
x = array([[x0], [y0], [1.0]])
y = T @ x
x1 = y[0, 0]
y1 = y[1, 0]
pl.figure(figsize=(2.0, 1.5))
pl.plot(0, 0, "x")
pl.plot(x0, y0, "x")
# pl.plot([x0,x1],[y0,y1],"b-")
pl.plot(x1, y1, "^")
# Plot transformation
t0 = atan(y0 / x0)
t = linspace(t0, t0 + theta)
r = sqrt(x0 ** 2 + y0 ** 2)
pl.plot(r * cos(t), r * sin(t), "--", color="tab:blue")
px = r * cos(t0 + theta)
py = r * sin(t0 + theta)
pl.plot(px, py, "o")
pl.plot([px, x1], [py, y1], "--", color="tab:blue")
pl.axis("equal")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.savefig("matrice-homogene-translrotat.pdf", bbox_inches="tight")

#
"""
First arm : angle theta, length l1
Second arm : angle phi, length l2
"""
#
# 1. Define the matrices
l1 = 1.0
theta = pi / 4
R1 = array(
    [[cos(theta), -sin(theta), 0.0], [sin(theta), cos(theta), 0.0], [0.0, 0.0, 1.0]]
)
T1 = array([[0.0, 1.0, l1], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

# 2.
x = array([[0.0], [0.0], [1.0]])
print(u"x=")
print(x)
y = R1 @ T1 @ x
print(u"y=")
print(y)


def plotArm(p1, p2, c1, c2, cline):
    pl.plot(p1[0], p1[0], c1)
    pl.plot([p1[0], p2[0]], [p1[1], p2[1]], cline)
    pl.plot(p2[0], p2[1], c2)
    return


# 3.
def singleArm(theta, l):
    R1 = array(
        [[cos(theta), -sin(theta), 0.0], [sin(theta), cos(theta), 0.0], [0.0, 0.0, 1.0]]
    )
    T1 = array([[0.0, 1.0, l], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    x = array([[0.0], [0.0], [1.0]])
    y = R1 @ T1 @ x
    #
    plotArm([0.0, 0.0], [y[0, 0], y[1, 0]], "bo", "ro", "b-")
    return


pl.figure()
for theta in linspace(0.0, 2 * pi, 10):
    singleArm(theta, 4.0)
pl.axis("equal")

# 3.
def plotRobot(theta, phi, l1, l2):
    T1 = array([[1.0, 0.0, l1], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    R1 = array(
        [[cos(theta), -sin(theta), 0.0], [sin(theta), cos(theta), 0.0], [0.0, 0.0, 1.0]]
    )
    T2 = array([[1.0, 0.0, l2], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    R2 = array([[cos(phi), -sin(phi), 0.0], [sin(phi), cos(phi), 0.0], [0.0, 0.0, 1.0]])
    # Premier bras
    x = array([[0.0], [0.0], [1.0]])
    y1 = R1 @ T1 @ x
    plotArm([0.0, 0.0], [y1[0, 0], y1[1, 0]], "o", "x", "-")
    # Deuxième bras
    y2 = R1 @ T1 @ R2 @ T2 @ x
    plotArm([y1[0, 0], y1[1, 0]], [y2[0, 0], y2[1, 0]], "x", "^", "-")
    return


theta = pi / 4
phi = pi / 3
l1 = 2.0
l2 = 3.0
pl.figure(figsize=(2.0, 1.5))
plotRobot(theta, phi, l1, l2)
pl.text(0.5, 1, "A")
pl.text(1.2, 3, "B")
pl.xlabel(u"x")
pl.ylabel(u"y")
pl.axis("equal")
pl.savefig("matrice-homogene-2bras.pdf", bbox_inches="tight")

#
pl.figure()
for theta in linspace(0.0, 2 * pi, 7):
    for phi in linspace(0.0, 2 * pi, 7):
        plotRobot(theta, phi, 2.0, 3.0)
pl.axis("equal")
