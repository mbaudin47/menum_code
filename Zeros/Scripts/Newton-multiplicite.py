#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Montre la lente convergence de la méthode de Newton si la multiplicité est 
supérieure à 1.
On considère la fonction 

f(x) = (x - a) ** m 

où m est un entier représentant la multiplicité de la racine réelle a. 
On utilise a = 1 et m = 1, 3, 5 et 7. 
On observe que la méthode de Newton est plus lente lorsque m est grand. 

Dans la seconde partie, on considère la fonction 

f(x) = (x - a) * exp(alpha * (x - a) ^ 2)

Références
----------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from fzero import newtongui, newton
import pylab as pl
import numpy as np
import matplotlibpreferences

matplotlibpreferences.load_preferences()


def check_derivative(x, fonction, derivee, h, relative_error_max=1.0e-4):
    x1 = x + h
    y1 = fonction(x1)
    x2 = x - h
    y2 = fonction(x2)
    y_prime_fd = (y1 - y2) / (x1 - x2)
    print("Derivative from F.D.=", y_prime_fd)
    y_prime_exacte = derivee(x)
    print("Derivative exact=", y_prime_exacte)
    relative_error = abs(y_prime_fd - y_prime_exacte) / abs(y_prime_exacte)
    if relative_error > relative_error_max:
        raise ValueError("Derivee incorrecte")
    return relative_error


def fonction_multiplicite_m(x, a, m):
    """
    Retourne la valeur de f(x) = (x - a) ** m.

    Alors :

    f'(x) = m * (x - a) ** (m - 1)
    f''(x) = m * (m - 1) * (x - a) ** (m - 2)
    ...
    f^(m)(x) = m !

    Par conséquent, f'(a) = ... = f^(m - 1)(a) = 0.

    Par définition, le réel a est une racine de multiplicité m.

    Parameters
    ----------
    x : float
        L'entrée.
    a : float
        La racine multiple.
    m : int
        La multiplicité de la racine.

    Returns
    -------
    y : float
        La valeur de la fonction.
    """
    y = (x - a) ** m
    return y


def derivee_multiplicite_m(x, a, m):
    """
    Retourne valeur de  f'(x) = m * (x - a) ** (m - 1).

    Parameters
    ----------
    x : float
        L'entrée.
    a : float
        La racine multiple.
    m : int
        La multiplicité de la racine.

    Returns
    -------
    y : float
        La valeur de la fonction.
    """
    y = m * (x - a) ** (m - 1)
    return y


def fonction_multiplicite_1(x):
    a = 1.0
    m = 1
    y = fonction_multiplicite_m(x, a, m)
    return y


def derivee_multiplicite_1(x):
    a = 1.0
    m = 1
    y = derivee_multiplicite_m(x, a, m)
    return y


def fonction_multiplicite_3(x):
    a = 1.0
    m = 3
    y = fonction_multiplicite_m(x, a, m)
    return y


def derivee_multiplicite_3(x):
    a = 1.0
    m = 3
    y = derivee_multiplicite_m(x, a, m)
    return y


def fonction_multiplicite_5(x):
    a = 1.0
    m = 5
    y = fonction_multiplicite_m(x, a, m)
    return y


def derivee_multiplicite_5(x):
    a = 1.0
    m = 5
    y = derivee_multiplicite_m(x, a, m)
    return y


def fonction_multiplicite_7(x):
    a = 1.0
    m = 7
    y = fonction_multiplicite_m(x, a, m)
    return y


def derivee_multiplicite_7(x):
    a = 1.0
    m = 7
    y = derivee_multiplicite_m(x, a, m)
    return y


# Check derivative
x = 3.0
h = 1.0e-4
check_derivative(
    x, fonction_multiplicite_1, derivee_multiplicite_1, h, relative_error_max=1.0e-4
)


# Setup experiment
N = 100

# Utilise la méthode de Newton
x = np.linspace(0.5, 1.5, N)
pl.figure()
pl.xlabel(u"x")
pl.ylabel(u"f(x)")
pl.legend()
#
x0 = 1.5
reltolx = 1.0e-9
# m = 1
y = fonction_multiplicite_1(x)
pl.plot(x, y, "-", label="$m=1$")
xs, history = newtongui(
    fonction_multiplicite_1, x0, derivee_multiplicite_1, reltolx=reltolx
)
# m = 3
y = fonction_multiplicite_3(x)
pl.plot(x, y, "-", label="$m=3$")
xs, history = newtongui(
    fonction_multiplicite_3, x0, derivee_multiplicite_3, reltolx=reltolx
)
# m = 5
y = fonction_multiplicite_5(x)
pl.plot(x, y, "-", label="$m=5$")
xs, history = newtongui(
    fonction_multiplicite_5, x0, derivee_multiplicite_5, reltolx=reltolx
)


pl.figure()
xs, history = newton(fonction_multiplicite_1, x0, derivee_multiplicite_1)


def calcule_erreur_absolue(xexact, history):
    n = len(history)
    absolute_error = np.zeros(n)
    for i in range(n):
        absolute_error[i] = abs(xexact - history[i])
    iteration_indices = list(range(n))
    return iteration_indices, absolute_error


def plot_convergence(xexact, function, derivative, x0, reltolx=1.0e-7, line_style="-"):
    xs, history = newton(function, x0, derivative, reltolx=reltolx)
    iteration_indices, absolute_error = calcule_erreur_absolue(xexact, history)
    pl.plot(iteration_indices, absolute_error, line_style)
    pl.xlabel(u"Itérations")
    pl.ylabel(u"Erreur absolue")
    return


# Convergence de la methode
xexact = 1.0
pl.figure(figsize=(2.5, 1.5))
# m = 1
plot_convergence(
    xexact, fonction_multiplicite_1, derivee_multiplicite_1, x0, line_style="-"
)
# m = 3
plot_convergence(
    xexact, fonction_multiplicite_3, derivee_multiplicite_3, x0, line_style="-."
)
# m = 5
plot_convergence(
    xexact, fonction_multiplicite_5, derivee_multiplicite_5, x0, line_style=":"
)
# m = 7
plot_convergence(
    xexact, fonction_multiplicite_7, derivee_multiplicite_7, x0, line_style="--"
)
pl.legend(["$m=1$", "$m=3$", "$m=5$", "$m=7$"], bbox_to_anchor=(1.0, 1.0))
pl.yscale("log")
pl.title("$f(x) = (x - 1)^m$")
pl.savefig("Newton-multiplicite.pdf", bbox_inches="tight")


def exponentielle_parametrique(x, a, alpha):
    y = (x - a) * np.exp(alpha * (x - a) ** 2)
    return y


def derivee_exponentielle(x, a, alpha):
    y = (2.0 * alpha * (x - a) ** 2 + 1.0) * np.exp(alpha * (x - a) ** 2)
    return y


def exponentielle_parametrique_1(x):
    a = 1.0
    alpha = 1.0
    y = exponentielle_parametrique(x, a, alpha)
    return y


def derivee_exponentielle_1(x):
    a = 1.0
    alpha = 1.0
    y = derivee_exponentielle(x, a, alpha)
    return y


def exponentielle_parametrique_2(x):
    a = 1.0
    alpha = 2.0
    y = exponentielle_parametrique(x, a, alpha)
    return y


def derivee_exponentielle_2(x):
    a = 1.0
    alpha = 2.0
    y = derivee_exponentielle(x, a, alpha)
    return y


def exponentielle_parametrique_3(x):
    a = 1.0
    alpha = 10.0
    y = exponentielle_parametrique(x, a, alpha)
    return y


def derivee_exponentielle_3(x):
    a = 1.0
    alpha = 10.0
    y = derivee_exponentielle(x, a, alpha)
    return y


# Check derivative
x = 3.0
h = 1.0e-4
check_derivative(
    x,
    exponentielle_parametrique_1,
    derivee_exponentielle_1,
    h,
    relative_error_max=1.0e-4,
)

# Setup experiment
N = 100
x0 = 1.5

# Utilise la méthode de Newton
x = np.linspace(0.5, 1.5, N)
pl.figure()
pl.xlabel(u"$x$")
pl.ylabel(u"$f(x)$")
pl.legend()
# m = 1
y = fonction_multiplicite_3(x)
pl.plot(x, y, "-", label="$\\alpha=10$")
pl.legend()
xs, history = newtongui(exponentielle_parametrique_3, x0, derivee_exponentielle_3)

#
# Convergence de la methode
xexact = 1.0
x0 = 2.0
pl.figure()
plot_convergence(xexact, exponentielle_parametrique_1, derivee_exponentielle_1, x0)
plot_convergence(xexact, exponentielle_parametrique_2, derivee_exponentielle_2, x0)
plot_convergence(xexact, exponentielle_parametrique_3, derivee_exponentielle_3, x0)
pl.legend([u"$\\alpha=1$", u"$\\alpha=2$", u"$\\alpha=10$"])
pl.yscale("log")
pl.title(u"$f(x) = (x - a) \exp(\\alpha (x - a)^2)$")
