#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
On considère (voir (Lemaire, 2005), p.88) la fonction qui transforme 
l'indice de fiabilité beta en probabilité Pf par la relation :

Pf = Phi (-beta)

où Phi est la fonction de répartition de la loi Gaussienne centrée 
réduite. 
On souhaite interpoler une table de 5 points sur la courbe :

log10(Pf) = log10(Phi (-beta))
    
Référence
---------
Lemaire, Maurice. Fiabilité des structures. 2005. Lavoisier, 
Hermès Science Publications
"""

import numpy as np
from scipy.stats import norm
import pylab as pl
import interp
import matplotlibpreferences

matplotlibpreferences.load_preferences()

# 1. Calcule les données du problème


def probabilite_defaillance(beta):
    """
    Retourne le logarithme en base 10 de la probabilité.

    Parameters
    ----------
    beta : float
        L'indice de fiabilité.

    Returns
    -------
    pflog_log : float
        Le logarithme en base 10 de la probabilité.

    """
    pflog_log10 = norm.logcdf(-beta) / np.log(10.0)
    return pflog_log10


# Génère des observations
if False:
    number_of_data_points = 8
    beta_data = np.linspace(0.0, 5.0, number_of_data_points)
    pflog_data = probabilite_defaillance(beta_data)
else:
    # Observations
    beta_data = np.array([0.0, 0.7143, 1.429, 2.143, 2.857, 3.571, 4.286, 5.0])
    pflog_data = np.array(
        [-0.3010, -0.6242, -1.116, -1.794, -2.670, -3.751, -5.040, -6.543]
    )
    number_of_data_points = len(beta_data)
print("+ Beta=", beta_data)
print("pflog_log=", pflog_data)

# Point où on veut la valeur
beta_cible = 4.5
pflog_exact = probabilite_defaillance(beta_cible)
print("+ beta_cible=", beta_cible)
print("pflog_exact=%.3f" % (pflog_exact))

# Courbe
number_of_points = 201
beta_array = np.linspace(0.0, 5.0, number_of_points)
pflog_exact_array = probabilite_defaillance(beta_array)

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_data, pflog_data, "o")
pl.plot(beta_array, pflog_exact_array, "-")
pl.xlabel(u"$\\beta$")
pl.ylabel(u"$\log_{10}(P_f)$")
pl.savefig("fiabilite-donnees.pdf", bbox_inches="tight")

# 2. Interpolation linéaire
v = interp.piecewise_linear(beta_data, pflog_data, beta_array)

# Point où on veut la valeur
pflog_piecelin = interp.piecewise_linear(beta_data, pflog_data, beta_cible)
pflog_erreur = np.abs(pflog_exact - pflog_piecelin)
print("+ (Interp. Lin.) pf=%.3f, Erreur=%.3e" % (pflog_piecelin, pflog_erreur))

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_data, pflog_data, "o", label="Data")
pl.plot(beta_array, pflog_exact_array, "-", label="Exact")
pl.plot(beta_array, v, "-", label="Lin. p. m.")
pl.xlabel(u"$\\beta$")
pl.ylabel(u"$\log_{10}(P_f)$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.title("Interp. linéaire par morceaux.")

# Calcul de l'erreur par l'interpolation linéaire par morceaux
error_piecewise = np.abs(v - pflog_exact_array)
# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_array, error_piecewise, "-")
pl.plot(beta_array, 1.0e-3 * np.ones(number_of_points))
pl.xlabel(u"$\\beta$")
pl.ylabel(u"Erreur abs.")
pl.title("Interp. linéaire par morceaux.")

# 3. Interpolation polynomiale
v = interp.polynomial_interpolation(beta_data, pflog_data, beta_array)

# Point où on veut la valeur
pflog_interp = interp.polynomial_interpolation(beta_data, pflog_data, beta_cible)
pflog_erreur = np.abs(pflog_exact - pflog_interp)
print("+ (Interp. globale) pf=%.3f, Erreur=%.3e" % (pflog_interp, pflog_erreur))

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_data, pflog_data, "o", label="Data")
pl.plot(beta_array, pflog_exact_array, "-", label="Exact")
pl.plot(beta_array, v, "-", label="Global")
pl.xlabel(u"$\\beta$")
pl.ylabel(u"$\log_{10}(P_f)$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.title("Interp. polynomiale.")

# Calcul de l'erreur par l'interpolation polynomiale
error_global = np.abs(v - pflog_exact_array)
# Figure
pl.figure(figsize=(2.5, 1.0))
pl.plot(beta_array, error_global, "-")
pl.plot(beta_array, 1.0e-3 * np.ones(number_of_points))
pl.xlabel(u"$\\beta$")
pl.ylabel(u"Erreur abs.")
pl.title("Interp. polyn.")

# 4. Interpolation par spline
v = interp.spline_interpolation(beta_data, pflog_data, beta_array)

# Point où on veut la valeur
pflog_spline = interp.spline_interpolation(beta_data, pflog_data, beta_cible)
pflog_erreur = np.abs(pflog_exact - pflog_spline)
print("+ (Spline) pf=%.3f, Erreur=%.3e" % (pflog_spline, pflog_erreur))

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_data, pflog_data, "o", label="Data")
pl.plot(beta_array, pflog_exact_array, "-", label="Exact")
pl.plot(beta_array, v, "-", label="Spline")
pl.xlabel(u"$\\beta$")
pl.ylabel(u"$\log_{10}(P_f)$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.title("Spline.")

# Calcul de l'erreur par spline
error_spline = np.abs(v - pflog_exact_array)
# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_array, error_spline, "-")
pl.plot(beta_array, 1.0e-3 * np.ones(number_of_points))
pl.xlabel(u"$\\beta$")
pl.ylabel(u"Erreur abs.")
pl.title("Spline.")

# 5. Utilisation des points de Chebyshev

# Observations
if False:
    beta_data = interp.compute_Chebyshev_roots(number_of_data_points, 0.0, 5.0)
    pflog_data = probabilite_defaillance(beta_data)
else:
    beta_data = np.array([0.048, 0.4213, 1.111, 2.012, 2.988, 3.889, 4.579, 4.952])
    pflog_data = np.array(
        [-0.3180, -0.4727, -0.8753, -1.656, -2.852, -4.298, -5.631, -6.435]
    )
print("Beta=", beta_data)
print("Pf_log=", pflog_data)

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_data, pflog_data, "o")
pl.plot(beta_array, pflog_exact_array, "-")
pl.xlabel(u"$\\beta$")
pl.ylabel(u"$\log_{10}(P_f)$")
pl.title("Avec noeuds de Chebyshev.")

# Interpolation polynomiale
v = interp.polynomial_interpolation(beta_data, pflog_data, beta_array)

# Point où on veut la valeur
pflog_interp = interp.polynomial_interpolation(beta_data, pflog_data, beta_cible)
pflog_erreur = np.abs(pflog_exact - pflog_interp)
print("+ (Interp. globale) pf=%.3f, Erreur=%.3e" % (pflog_interp, pflog_erreur))

# Figure
pl.figure(figsize=(1.5, 1.0))
pl.plot(beta_data, pflog_data, "o", label="Data")
pl.plot(beta_array, pflog_exact_array, "-", label="Exact")
pl.plot(beta_array, v, "-", label="Global")
pl.xlabel(u"$\\beta$")
pl.ylabel(u"$\log_{10}(P_f)$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.title("Interp. polynomiale (Chebyshev).")

# Calcul de l'erreur par l'interpolation polynomiale
error_cheby = np.abs(v - pflog_exact_array)
# Figure
pl.figure(figsize=(3.0, 1.0))
pl.plot(beta_array, error_cheby, "-", label="Lin. p. m.")
pl.plot(beta_array, 1.0e-3 * np.ones(number_of_points))
pl.xlabel(u"$\\beta$")
pl.ylabel(u"Erreur abs.")
pl.title("Interp. Chebyshev.")

# Compare les erreurs des 4 méthodes
# 1. Observations
beta_data = np.array([0.0, 0.7143, 1.429, 2.143, 2.857, 3.571, 4.286, 5.0])
pflog_data = np.array(
    [-0.3010, -0.6242, -1.116, -1.794, -2.670, -3.751, -5.040, -6.543]
)
number_of_data_points = len(beta_data)
u = np.linspace(0.0, 5.0, number_of_points)
# 2. Interpolation lin.p.morceaux
pflog_piecelin = interp.piecewise_linear(beta_data, pflog_data, beta_array)
erreur_piecelin = np.abs(pflog_exact_array - pflog_piecelin)
# 3. Interpolation polynomiale
pflog_global = interp.polynomial_interpolation(beta_data, pflog_data, beta_array)
erreur_global = np.abs(pflog_exact_array - pflog_global)
# 4. Spline
pflog_global = interp.spline_interpolation(beta_data, pflog_data, beta_array)
erreur_spline = np.abs(pflog_exact_array - pflog_global)
# 5. Polynôme de Chebyshev
beta_data = np.array([0.048, 0.4213, 1.111, 2.012, 2.988, 3.889, 4.579, 4.952])
pflog_data = np.array(
    [-0.3180, -0.4727, -0.8753, -1.656, -2.852, -4.298, -5.631, -6.435]
)
pflog_cheby = interp.polynomial_interpolation(beta_data, pflog_data, beta_array)
erreur_cheby = np.abs(pflog_exact_array - pflog_cheby)
#
pl.figure(figsize=(2.5, 1.5))
pl.plot(beta_array, erreur_piecelin, "-", label="Lin. p. m.")
pl.plot(beta_array, erreur_global, "--", label="Equidistant")
pl.plot(beta_array, erreur_cheby, "-.", label="Chebyshev")
pl.plot(beta_array, erreur_spline, ":", label="Spline")
pl.xlabel(u"$\\beta$")
pl.ylabel(u"Erreur abs.")
pl.title("Interpolation.")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.yscale("log")
pl.ylim(1.0e-4, 0.5e-1)
pl.savefig("fiabilite-interpolation.pdf", bbox_inches="tight")

# Analyse de convergence

number_of_points_array = list(range(2, 30))
number_of_experiments = len(number_of_points_array)
error_piecewise = np.zeros(number_of_experiments)
error_spline = np.zeros(number_of_experiments)
error_equi = np.zeros(number_of_experiments)
error_cheby = np.zeros(number_of_experiments)
for index in range(number_of_experiments):
    number_of_data_points = number_of_points_array[index]
    number_of_points = 100 * number_of_data_points
    # Generate data
    beta_data = np.linspace(0.0, 5.0, number_of_data_points)
    pflog_data = probabilite_defaillance(beta_data)
    # Compute exact pflog
    beta_array = np.linspace(0.0, 5.0, number_of_points)
    pflog_exact_array = probabilite_defaillance(beta_array)
    # Compute error for piecewise linear interpolation
    v = interp.piecewise_linear(beta_data, pflog_data, beta_array)
    error_piecewise[index] = max(abs(v - pflog_exact_array))
    # Compute error for polynomial interpolation
    v = interp.polynomial_interpolation(beta_data, pflog_data, beta_array)
    error_equi[index] = max(abs(v - pflog_exact_array))
    # Compute error for spline interpolation
    v = interp.spline_interpolation(beta_data, pflog_data, beta_array)
    error_spline[index] = max(abs(v - pflog_exact_array))
    # Compute error for Chebyshev interpolation
    beta_data = interp.compute_Chebyshev_roots(number_of_data_points, 0.0, 5.0)
    pflog_data = probabilite_defaillance(beta_data)
    v = interp.polynomial_interpolation(beta_data, pflog_data, beta_array)
    error_cheby[index] = max(abs(v - pflog_exact_array))

pl.figure(figsize=(2.5, 1.5))
pl.plot(number_of_points_array, error_piecewise, "-", label="Linéaire p.m.")
pl.plot(number_of_points_array, error_equi, "--", label="Equidistant")
pl.plot(number_of_points_array, error_cheby, "-.", label="Chebyshev")
pl.plot(number_of_points_array, error_spline, ":", label="Spline")
pl.yscale("log")
pl.xlabel("$n$")
pl.ylabel(u"$\|f - P\|_{\infty}$")
pl.legend(bbox_to_anchor=(1.0, 1.0))
pl.savefig("fiabilite-convergence.pdf", bbox_inches="tight")
