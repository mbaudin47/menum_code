#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Observe graphiquement la différence entre vecteurs linéairement 
indépendants et dépendants. 
"""

from numpy import array
from numpy.linalg import matrix_rank
from pylab import plot, text, xlabel, ylabel, axis, figure, savefig
import matplotlibpreferences

matplotlibpreferences.load_preferences()


#
# 1. Deux vecteurs independants
print(u"")
print(u"1. Deux vecteurs independants")
A = array([[1.0, 3.0], [2.0, 4.0]])
print(u"A=")
print(A)
print(u"Rank=", matrix_rank(A))
#
# 2. Graphique
print(u"")
print(u"2. Graphique")
delta = 0.3
figure(figsize=(2.0, 1.5))
plot([0.0, A[0, 0]], [0.0, A[1, 0]], "-")
text(A[0, 0] - delta, A[1, 0] + delta, "$\mathbf{a}_1$")
plot([0.0, A[0, 1]], [0.0, A[1, 1]], "--")
text(A[0, 1] + delta, A[1, 1] - delta, "$\mathbf{a}_2$")
xlabel(u"$x_1$")
ylabel(u"$x_2$")
axis("equal")
savefig("independance-vecteurs-independants.pdf", bbox_inches="tight")

#
# 3. Deux vecteurs dependants
print(u"")
print(u"3. Deux vecteurs dependants")
A = array([[1.0, -2.0], [2.0, -4.0]])
print(u"A=")
print(A)
print(u"Rank=", matrix_rank(A))
#
# 4. Graphique
print(u"")
print(u"4. Graphique")
delta = 0.3
figure(figsize=(2.0, 1.5))
plot([0.0, A[0, 0]], [0.0, A[1, 0]], "-")
text(A[0, 0] + delta, A[1, 0] - delta, "$\mathbf{a}_1$")
plot([0.0, A[0, 1]], [0.0, A[1, 1]], "--")
text(A[0, 1] - 3.0 * delta, A[1, 1] + 2.0 * delta, "$\mathbf{a}_2$")
xlabel(u"$x_1$")
ylabel(u"$x_2$")
axis("equal")
savefig("independance-vecteurs-dependants.pdf", bbox_inches="tight")

############################################################
#
# Optionnel
#
from numpy import column_stack

#
# 5. Faire une matrice avec deux vecteurs
print(u"")
print(u"5. Faire une matrice avec deux vecteurs")
a1 = array([1.0, 2.0])
print(u"a1=")
print(a1)
a2 = array([3.0, 4.0])
print(u"a2=")
print(a2)
A = column_stack([a1, a2])
print(u"A=")
print(A)
