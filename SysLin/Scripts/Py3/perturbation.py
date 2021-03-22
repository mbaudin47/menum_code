#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
Pour une matrice donnée, calcule le second 
membre b et la perturbation Delta b qui réalise 
la borne maximale liée au conditionnement de la matrice. 
En d'autres termes, calcule b et delta b tels que 

norm(delta x) / norm(x) = cond(A) * norm(delta b) / norm(b)

Références
[1] Regularization of Least Squares Problems
Heinrich Voss
voss@tu-harburg.de
Hamburg University of Technology
Institute of Numerical Simulation
https://www.mat.tuhh.de/lehre/material/RegLS.pdf

[2]
Discrete Least-squares Approximations
Biswa Nath Datta
Distinguished Research Professor
Northern Illinois University
De Kalb
Illinois 60115, USA
E-mail : dattab@math.niu.edu
http://www.math.niu.edu/~dattab/math435.2009/CHAPTER_LEASTSQURES.pdf

"""

# Copyright (C) 2013 - 2021 - Michaël Baudin

import numpy as np
import scipy
import scipy.linalg
import pylab as pl
import matplotlibpreferences

matplotlibpreferences.load_preferences()

#
#


def vectorMaxNorm1(A):
    """
    Calcule le vecteur x qui maximise
    la norme 1 de ||A*x||/||x||
    """
    k = np.argmax(np.sum(np.abs(A), 0))
    n = A.shape[1]
    x = np.zeros((n, 1))
    x[k] = 1.0
    return x


def vectorMaxNormInf(A):
    """
    Calcule le vecteur x qui maximise
    la norme infinie de ||A*x||/||x||
    """
    if type(A) != np.ndarray:
        raise TypeError("A numpy array is expected.")
    k = np.argmax(np.sum(np.abs(A), 1))
    n = A.shape[1]
    x = np.zeros((n, 1))
    #
    indices = np.where(A[k, :] > 0)[0]
    x[indices] = 1.0
    #
    indices = np.where(A[k, :] < 0)[0]
    x[indices] = -1.0
    return x


def randomGaussianMatrix(n):
    mean = np.zeros((n,))
    cov = np.identity(n)
    A = np.random.multivariate_normal(mean, cov, n)
    return A


def worstCaseRHSNorm1(A):
    """
    Pour une matrice donnée, calcule le second
    membre b et la perturbation Delta b qui réalise
    la borne maximale liée au conditionnement de la matrice
    en norme 1.
    En d'autres termes, calcule b et delta b tels que

    norm(delta x) / norm(x) = cond(A) * norm(delta b) / norm(b)
    """
    if type(A) != np.ndarray:
        raise TypeError("A numpy array is expected.")
    x = vectorMaxNorm1(A)
    b = np.dot(A, x)
    invA = np.linalg.inv(A)
    deltaB = vectorMaxNorm1(invA)
    deltaX = np.linalg.solve(A, deltaB)
    return (x, deltaX, b, deltaB)


def worstCaseRHSNormINF(A):
    """
    Pour une matrice donnée, calcule le second
    membre b et la perturbation Delta b qui réalise
    la borne maximale liée au conditionnement de la matrice
    en norme infinie.
    En d'autres termes, calcule b et delta b tels que

    norm(delta x) / norm(x) = cond(A) * norm(delta b) / norm(b)
    """
    if type(A) != np.ndarray:
        raise TypeError("A numpy array is expected.")
    x = vectorMaxNormInf(A)
    b = np.dot(A, x)
    invA = np.linalg.inv(A)
    deltaB = vectorMaxNormInf(invA)
    deltaX = np.linalg.solve(A, deltaB)
    return (x, deltaX, b, deltaB)


# A=np.matrix([[1.,-1.],[1.,1.]])
# A=np.matrix([[1.,2.],[3.,4.]])
# B = randomGaussianMatrix(5) * 10
# A = B.round()
A = scipy.linalg.hilbert(6)
print(u"A")
print(A)
x = vectorMaxNorm1(A)
print(u"x1")
print(x)
x = vectorMaxNormInf(A)
print(u"xINF")
print(x)


def printAnalysis(x, deltaX, b, deltaB, normindex=1):
    print(u"b")
    print(b)
    print(u"deltaB")
    print(deltaB)
    print(u"x")
    print(x)
    print(u"deltaX")
    print(deltaX)
    print(u"Cond(A,%s) = %.3e" % (str(normindex), np.linalg.cond(A, normindex)))
    leftRatio = np.linalg.norm(deltaX, normindex) / np.linalg.norm(x, normindex)
    rightRatio = np.linalg.norm(deltaB, normindex) / np.linalg.norm(b, normindex)
    print(u"|Delta x|/|x| : %.3e" % (leftRatio))
    print(u"|Delta b|/|b| : %.3e" % (rightRatio))
    print(u"%f = %f" % (leftRatio, np.linalg.cond(A, normindex) * rightRatio))
    print(u"|Delta b| = %.3e" % (np.linalg.norm(deltaB, normindex)))
    print(u"|Delta x| = %.3e" % (np.linalg.norm(deltaX, normindex)))
    return None


x, deltaX, b, deltaB = worstCaseRHSNorm1(A)
printAnalysis(x, deltaX, b, deltaB, 1)
x, deltaX, b, deltaB = worstCaseRHSNormINF(A)
printAnalysis(x, deltaX, b, deltaB, np.inf)

"""
Montrons le conditionnement de la matrice de Hilbert.
"""
nmatrices = 15
cond1 = np.zeros((nmatrices - 1,))
cond2 = np.zeros((nmatrices - 1,))
condi = np.zeros((nmatrices - 1,))
matricessize = range(1, nmatrices)
for n in matricessize:
    A = scipy.linalg.hilbert(n)
    cond1[n - 1] = np.linalg.cond(A, 1)
    cond2[n - 1] = np.linalg.cond(A, 2)
    condi[n - 1] = np.linalg.cond(A, np.inf)

pl.figure(figsize=(2.5, 1.5))
pl.plot(matricessize, cond1, ".", label=r"$1$")
pl.plot(matricessize, cond2, ".", label=r"$2$")
pl.plot(matricessize, condi, ".", label=r"$\infty$")
pl.yscale("log")
pl.xlabel(u"Taille de la matrice")
pl.ylabel(u"Conditionnement")
pl.title(u"Matrice de Hilbert")
pl.legend()
pl.savefig("hilbert-cond.pdf", bbox_inches="tight")
