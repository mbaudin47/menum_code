# Copyright (C) 2013 - 2023 - Michael Baudin
"""
Une librairie pour le modèle de Lorenz.

Références
----------
Morris W. Hirsch, Stephen Smale et Robert. L. Devaney. Differential 
Equations, Dynamical Systems, and an introduction to chaos, Third
Edition. Elsevier, 2013.

Martin Braun. Differential equations and their applications, Fourth Edition. 
Texts in applied mathematics. Springer, 1993.

Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""
from scipy.integrate import odeint
import numpy as np
from pylab import plot, xlabel, ylabel, figure, axis, legend
import pylab


def lorenz(y, t, beta, sigma, rho):
    """
    The right-hand side of the Lorenz attractor.

    Returns f(t,y(t)) in the ODE :

        dy/dt=f(t,y(t))

    for the Lorenz attractor.

    Parameters
    ----------
    y : np.array(3)
        The current point.
    t : float
        The current time
    beta : float
        The first parameter
    sigma : float
        The Prandlt number
    rho : float
        The Rayleigh number

    Returns
    -------
    ydot : np.array(3)
        The derivative of y with respect to t.
    """
    A = lorenz_jacobian(y, t, beta, sigma, rho)
    ydot = A @ y
    return ydot


def lorenz_jacobian(y, t, beta, sigma, rho):
    """
    The Jacobian matrix of the Lorenz attractor.

    Returns the Jacobian of f(t,y(t)) with
    respect to y in the ODE :

        dy/dt=f(t,y(t))

    for the Lorenz attractor.

    Parameters
    ----------
    y : np.array(3)
        The current point.
    t : float
        The current time
    beta : float
        The first parameter
    sigma : float
        The Prandlt number
    rho : float
        The Rayleigh number

    Returns
    -------
    A : np.array((3, 3))
        The Jacobian matrix.
    """
    A = np.array([[-beta, 0.0, y[1]], [0.0, -sigma, sigma], [-y[1], rho, -1.0]])
    return A


def lorenzgui(tfinal, beta=8.0 / 3.0, sigma=10.0, rho=28.0):
    """
    Makes a phase plot of the Lorenz attractor.

    Solves the ODE :

        dy/dt=f(t,y(t))
        y(0)=y0

    for the Lorenz attractor.

    Parameters
    ----------
    tfinal : float
        The final time
    beta : float
        The first parameter
    sigma : float
        The Prandlt number
    rho : float
        The Rayleigh number

    Returns
    -------
    figure : matplotlib figure
        The plot.
    """
    y0 = np.array([1.0, 1.0, 1.0])
    t = np.linspace(0.0, tfinal, 10000)
    y = odeint(lorenz, y0, t, (beta, sigma, rho))
    # Phase plot
    fig = figure()
    plot(y[:, 1], y[:, 2], "-")
    plot(y0[1], y0[2], "*", label="t=0")
    plot(y[-1, 1], y[-1, 2], "o", label="t=%.2f" % (tfinal))
    axis("equal")
    xlabel(u"$y_2$")
    ylabel(u"$y_3$")
    pylab.title(
        r"Attracteur de Lorenz : "
        r"$\rho$=%.1f, $\sigma$=%.1f, $\beta$=%.1f" % (beta, sigma, rho)
    )
    legend()
    return fig
