#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Dessine les pentes utilisées dans les méthodes numériques.

Le problème test est :
    
y'(t) = a * y(t)
y(0) = 1

La solution est 

y(t) = y0 * exp(a * t)

pour tout t >= 0.

On utilise a = 1.

Références
----------
Cleve Moler. Numerical Computing with Matlab. Society for
Industrial Mathematics, 2004.

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from numpy import linspace, exp
import pylab as pl
import matplotlibpreferences


matplotlibpreferences.load_preferences()


def f(y, t):
    a = 1.0
    ydot = a * y
    return ydot


def plotslope(t0, y0, s, slopetext, deltat=-0.05, deltay=0.2):
    """
    Dessine la pente s au point (t0,y0) avec le texte slopetext.
    Par défaut, affiche le texte au dessus de la pente,
    légèrement à gauche (pour centrer)

    t0 : un flottant, la date
    y0 : un flottant, la valeur à la date t0
    s : un flottant, la pente
    slopetext : une chaîne de caractères, le texte
    deltat : un flottant, le décalage horizontal pour le texte
    deltay : un flottant, le décalage vertical pour le texte
    """
    t = linspace(t0 - 0.2, t0 + 0.2)
    y = s * (t - t0) + y0
    pl.plot(t, y, "-", color="tab:blue")
    pl.plot(t0, y0, "o", color="tab:blue")
    pl.text(t0 + deltat, y0 + deltay, slopetext)
    return


def plotdottedline(
    tleft, t, y, ttext, ytext, plothorizontal=True, pointSymbol="o", delta_y_at_t=0.0
):
    """
    Dessine une ligne pointillé verticale.

    Si plothorizontal est True, dessine un trait horizontal.
    Dessine un rond bleu à (t,y).
    Si ttext n'est pas vide, dessine le texte à l'abscisse t.
    Si ytext n'est pas vide, dessine le texte à l'ordonnée y.

    Parameters
    ----------
    tleft : float
        La borne inférieure de temps du trait pointillé.
    t : float
        L'abscisse de la date.
    y : float
        L'ordonnée du trait, si plothorizontal est True.
    ttext : str
        Le texte à la date t.
    ytext : str
        lL texte à l'ordonnée y.
    plothorizontal : bool, optional
        Si True, dessine un trait pointillé horizontal. The default is True.
    pointSymbol : str, optional
        Le symbol pour le point. The default is "o".
    delta_y_at_t : float, optional
        L'incrément vertical pour la position de ttext. The default is 0.0.

    Returns
    -------
    None.
    """
    pl.plot([t, t], [0.6, y], "k:")  # y0 : Vertical
    if plothorizontal:
        pl.plot([tleft, t], [y, y], "k:")  # y0 : Horizontal
    pl.plot(t, y, pointSymbol, color="tab:blue")
    if ttext != "":
        pl.text(t, delta_y_at_t, ttext)
    if ytext != "":
        pl.text(tleft - 0.3, y, ytext)
    return


def decorateaxis(tleft, t0, tf, h):
    """
    Dessine les axes des absices et des ordonnées.

    Parameters
    ----------
    tleft : float
        La borne inférieure de temps du trait pointillé.
    t0 : float
        La date initiale.
    tf : float
        La date maximale pour la solution exacte à la date finale.
    h : float
        Le pas d'intégration.

    Returns
    -------
    None.
    """
    pl.axis("off")
    pl.arrow(
        tleft + 0.1,
        y0 - 0.2,
        tf + 0.3,
        0,
        head_width=0.1,
        head_length=0.05,
        fc="k",
        ec="k",
    )
    yf = y0 * exp(a * (t0 + h))
    pl.arrow(
        tleft + 0.1,
        y0 - 0.2,
        0.0,
        yf + 0.1,
        head_width=0.05,
        head_length=0.1,
        fc="k",
        ec="k",
    )
    pl.xlim([tleft, 1.3])
    yright = y0 * exp(a * (tf + 0.2))
    pl.ylim([tleft, yright + 0.5])
    return


def plotexact(tleft, tf, y0):
    """
    Dessine la solution exacte.

    Parameters
    ----------
    tleft : float
        La date minimale pour la solution exacte à la date initiale.
    tf : float
        La date maximale pour la solution exacte à la date finale.
    y0 : float
        L'état initial.

    Returns
    -------
    None.
    """
    t = linspace(tleft, tf + 0.2)
    y = y0 * exp(a * t)
    pl.plot(t, y, "-", color="tab:orange")
    return


def plotinitial(tleft, t0, y0, delta_y_at_t0=0.0):
    """
    Dessine la ligne pointillée à la date initiale.

    Parameters
    ----------
    t0 : float
        La date initiale.
    y0 : float
        L'état initial.
    tleft : float
        La date minimale pour la solution exacte à la date initiale.
    delta_y_at_t0 : float, optional
        L'incrément en y pour l'affichage de la date initiale. The default is 0.0.

    Returns
    -------
    None.
    """
    plotdottedline(tleft, t0, y0, "$t_n$", "$y_n$", delta_y_at_t=delta_y_at_t0)
    return


def plotfinal(t0, h, y0, tleft, afficheTnPlus1=True, delta_y_at_t0=0.0):
    """
    Dessine la ligne pointillée à la date finale.

    Parameters
    ----------
    t0 : float
        La date initiale.
    h : float
        Le pas d'intégration.
    y0 : float
        L'état initial.
    tleft : float
        La date minimale pour la solution exacte à la date initiale.
    afficheTnPlus1 : bool, optional
        Si vrai, affiche t(n+h). The default is True.
    delta_y_at_t0 : float, optional
        L'incrément en y pour l'affichage de la date initiale. The default is 0.0.

    Returns
    -------
    None.
    """
    yf = y0 * exp(a * (t0 + h))
    if afficheTnPlus1:
        plotdottedline(
            tleft,
            t0 + h,
            yf,
            "$t_{n+1}$",
            "",
            plothorizontal=False,
            pointSymbol="+",
            delta_y_at_t=delta_y_at_t0,
        )
    else:
        plotdottedline(
            tleft,
            t0 + h,
            yf,
            "",
            "",
            plothorizontal=False,
            pointSymbol="+",
            delta_y_at_t=delta_y_at_t0,
        )
    return


def plotexactinitialfinal(tleft, t0, tf, y0, h, afficheTnPlus1=True, delta_y_at_t0=0.0):
    """
    Dessine la solution exacte, et les pointillés aux dates t(n) et t(n+h).

    Parameters
    ----------
    tleft : float
        La date minimale pour la solution exacte à la date initiale.
    t0 : float
        La date initiale.
    tf : float
        La date maximale pour la solution exacte à la date finale.
    y0 : float
        L'état initial.
    h : float
        Le pas d'intégration.
    afficheTnPlus1 : bool, optional
        Si vrai, affiche t(n+h). The default is True.
    delta_y_at_t0 : float, optional
        L'incrément en y pour l'affichage de la date initiale. The default is 0.0.

    Returns
    -------
    None.
    """
    plotexact(tleft, tf, y0)  # Solution exacte
    plotinitial(tleft, t0, y0, delta_y_at_t0)  # Initial
    plotfinal(t0, h, y0, tleft, afficheTnPlus1, delta_y_at_t0)  # Final
    return


tspan = [0.0, 1.0]
a = 1.0
y0 = 1
t0 = tspan[0]
tf = tspan[1]
h = 1.0
tleft = t0 - 0.2

###################################################
#
# Méthode d'Euler

if True:
    #
    pl.figure(figsize=(2.0, 1.5))
    pl.suptitle(u"Euler")
    plotexactinitialfinal(tleft, t0, tf, y0, h, delta_y_at_t0=0.2)
    decorateaxis(tleft, t0, tf, h)
    # Pente d'Euler
    s = f(y0, t0)
    plotslope(t0, y0, s, "$s_1$", deltay=0.3)
    # Méthode d'Euler
    y1 = y0 + h * s
    plotdottedline(tleft, t0 + h, y1, "", "$y_{n+1}$")
    #
    pl.savefig("pentes_Euler.pdf", pad_inches=0.05, bbox_inches="tight")

###################################################
#
# Méthode de Runge

if True:
    # 1.
    fig = pl.figure(figsize=(4.0, 1.5))
    pl.suptitle(u"Runge")
    pl.subplot(1, 2, 1)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #1
    s1 = f(y0, t0)
    plotslope(t0, y0, s1, "$s_1$", deltay=0.3)
    #
    # 2.
    pl.subplot(1, 2, 2)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #2
    plotslope(t0, y0, s1, "$s_1$", deltay=0.3)
    s2 = f(y0 + 0.5 * h * s1, t0 + 0.5 * h)
    plotslope(t0 + 0.5 * h, y0 + 0.5 * h * s1, s2, "$s_2$", deltat=0.1, deltay=-0.1)
    plotdottedline(
        tleft,
        t0 + 0.5 * h,
        y0 + 0.5 * h * s1,
        "$t_n+\\frac{h}{2}$",
        "",
        plothorizontal=False,
    )
    # Méthode de Runge
    y1 = y0 + h * s2
    plotdottedline(tleft, t0 + h, y1, "", "$y_{n+1}$")
    #
    fig.tight_layout()
    pl.savefig("pentes_Runge.pdf", pad_inches=0.05, bbox_inches="tight")

###################################################
#
# Méthode de Heun

if True:
    # 1.
    fig = pl.figure(figsize=(4.0, 1.5))
    pl.suptitle(u"Heun")
    pl.subplot(1, 2, 1)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #1
    s1 = f(y0, t0)
    plotslope(t0, y0, s1, "$s_1$", deltay=0.3)
    #
    # 2.
    pl.subplot(1, 2, 2)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #2
    plotslope(t0, y0, s1, "$s_1$", deltay=0.3)
    s2 = f(y0 + h * s1, t0 + h)
    plotslope(t0 + h, y0 + h * s1, s2, "$s_2$", deltat=0.1, deltay=-0.1)
    plotdottedline(tleft, t0 + h, y0 + h * s1, "", "", plothorizontal=False)
    # Méthode de Heun
    y1 = y0 + 0.5 * h * (s1 + s2)
    plotdottedline(tleft, t0 + h, y1, "", "$y_{n+1}$")
    fig.tight_layout()
    pl.savefig("pentes_Heun.pdf", pad_inches=0.05, bbox_inches="tight")

###################################################
#
# Méthode de RK4
if True:
    # 1.
    fig = pl.figure(figsize=(3.5, 2.5))
    pl.suptitle(u"RK4")
    pl.subplot(2, 2, 1)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #1
    s1 = f(y0, t0)
    plotslope(t0, y0, s1, "$s_1$", deltay=0.5)
    #
    # 2.
    pl.subplot(2, 2, 2)
    plotexactinitialfinal(tleft, t0, tf, y0, h, afficheTnPlus1=False)
    decorateaxis(tleft, t0, tf, h)
    # Pente #2
    plotslope(t0, y0, s1, "$s_1$", deltay=0.5)
    s2 = f(y0 + 0.5 * h * s1, t0 + 0.5 * h)
    plotslope(t0 + 0.5 * h, y0 + 0.5 * h * s1, s2, "$s_2$", deltat=0.1, deltay=-0.2)
    plotdottedline(
        tleft,
        t0 + 0.5 * h,
        y0 + 0.5 * h * s1,
        "$t_n+\\frac{h}{2}$",
        "",
        plothorizontal=False,
    )
    #
    # 3.
    pl.subplot(2, 2, 3)
    plotexactinitialfinal(tleft, t0, tf, y0, h, afficheTnPlus1=False)
    decorateaxis(tleft, t0, tf, h)
    # Pente #3
    plotslope(t0, y0, s1, "$s_1$", deltay=0.5)
    s3 = f(y0 + 0.5 * h * s2, t0 + 0.5 * h)
    plotslope(t0 + 0.5 * h, y0 + 0.5 * h * s1, s3, "$s_3$", deltat=0.1, deltay=-0.1)
    plotdottedline(
        tleft,
        t0 + 0.5 * h,
        y0 + 0.5 * h * s1,
        "$t_n+\\frac{h}{2}$",
        "",
        plothorizontal=False,
    )
    #
    # 4.
    pl.subplot(2, 2, 4)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #4
    s4 = f(y0 + h * s3, t0 + h)
    plotslope(t0 + h, y0 + h * s3, s4, "$s_4$", deltat=-0.1, deltay=+0.5)
    y1 = y0 + (h / 6.0) * (s1 + 2 * s2 + 2 * s3 + s4)
    plotdottedline(tleft, t0 + h, y1, "", "$y_{n+1}$")
    #
    fig.tight_layout()
    pl.savefig("pentes_RK4.pdf", pad_inches=0.05, bbox_inches="tight")

###################################################
#
# Méthode BS23
if True:
    # 1.
    fig = pl.figure(figsize=(3.5, 2.5))
    pl.suptitle(u"BS23")
    pl.subplot(2, 2, 1)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #1
    s1 = f(y0, t0)
    plotslope(t0, y0, s1, "$s_1$", deltay=0.5)
    #
    # 2.
    pl.subplot(2, 2, 2)
    plotexactinitialfinal(tleft, t0, tf, y0, h, afficheTnPlus1=False)
    decorateaxis(tleft, t0, tf, h)
    # Pente #2
    plotslope(t0, y0, s1, "$s_1$", deltay=0.5)
    s2 = f(y0 + 0.5 * h * s1, t0 + 0.5 * h)
    plotslope(t0 + 0.5 * h, y0 + 0.5 * h * s1, s2, "$s_2$", deltat=0.1, deltay=-0.3)
    plotdottedline(
        tleft,
        t0 + 0.5 * h,
        y0 + 0.5 * h * s1,
        "$t_n+\\frac{h}{2}$",
        "",
        plothorizontal=False,
    )
    #
    # 3.
    pl.subplot(2, 2, 3)
    plotexactinitialfinal(tleft, t0, tf, y0, h, afficheTnPlus1=False)
    decorateaxis(tleft, t0, tf, h)
    # Pente #3
    plotslope(t0, y0, s1, "$s_1$", deltay=0.5)
    s3 = f(y0 + 0.75 * h * s2, t0 + 0.75 * h)
    plotslope(t0 + 0.75 * h, y0 + 0.75 * h * s2, s3, "$s_3$", deltat=0.05, deltay=-0.5)
    plotdottedline(
        tleft,
        t0 + 0.75 * h,
        y0 + 0.75 * h * s2,
        "$t_n+\\frac{3h}{4}$",
        "",
        plothorizontal=False,
    )
    #
    # 4.
    pl.subplot(2, 2, 4)
    plotexactinitialfinal(tleft, t0, tf, y0, h)
    decorateaxis(tleft, t0, tf, h)
    # Pente #4
    y1 = y0 + h / 9.0 * (2.0 * s1 + 3.0 * s2 + 4.0 * s3)
    s4 = f(y1, t0 + h)
    plotslope(t0 + h, y1, s4, "$s_4$", deltat=-0.1, deltay=+0.6)
    plotdottedline(tleft, t0 + h, y1, "", "$y_{n+1}$")
    #
    fig.tight_layout()
    pl.savefig("pentes_BS23.pdf", pad_inches=0.05, bbox_inches="tight")
