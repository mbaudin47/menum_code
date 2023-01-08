# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
A collection of functions to perform numerical differentiation with 
finite difference formulas.

Reference
---------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import sys
import numpy as np
import pylab as pl


def first_derivative(f, x, h=None, p=2, *args):
    """
    Computes the f'(x) from finite differences.

    Assumes that x is a float and y=f(x) is a float.

    Use finite differences with order p.

    The step size is computed according to the
    optimal value, when f(x)/f''(x) approx 1.

    The function f is supposed to have the
    calling sequence

        y=f(x)

    where x is a float and y is a float.
    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y=f(x,*args)

    Uses the trick from (Dumontet, Vignes, 1977) to compute the
    step as accurately as possible: see. eq.14, p.16.

    Parameters
    ----------
    f : function
        The function to derivate.
    x : float
        The point where the gradient is to be computed.
    h : float
        The step size.
    p : int
        The order of the formula, p=1, 2 or 4.
    args : list
        The optional arguments of f.

    Returns
    -------
    g : array
        The gradient.
    fcount : int
        The number of function evaluations of f.

    Examples
    --------
    >>> from numpy import sin
    >>> x = 1.0
    >>> g, fcount = first_derivative(sin, x)
    >>> h = 1.0e-4
    >>> g, fcount = first_derivative(sin, x, h)
    >>> g, fcount = first_derivative(sin, x, h, p=1)

    References
    ----------
    J. Dumontet et J. Vignes. « Détermination du pas optimal
    dans le calcul des dérivées sur ordinateur ». In : R.A.I.R.O
    Analyse numérique 11.1 (1977), p. 13-25.
    """

    def first_derivative_forward(f, x, h, *args):
        """Apply forward_elimination finite difference for gradient."""
        fcount = 2
        fx = f(x, *args)
        xp = x + h
        h_exact = xp - x
        fxp = f(xp, *args)
        g = (fxp - fx) / h_exact
        return g, fcount

    def first_derivative_centered(f, x, h, *args):
        """Apply centered finite difference for gradient."""
        fcount = 2
        xp = x + h
        xm = x - h
        h_exact = xp - xm
        fxp = f(xp, *args)
        fxm = f(xm, *args)
        g = (fxp - fxm) / h_exact
        return g, fcount

    eps = sys.float_info.epsilon
    if h == None:
        h = eps ** (1.0 / (p + 1))
    if p == 1:
        g, fcount = first_derivative_forward(f, x, h, *args)
    elif p == 2:
        g, fcount = first_derivative_centered(f, x, h, *args)
    elif p == 4:
        g1, fcount1 = first_derivative_centered(f, x, h, *args)
        g2, fcount2 = first_derivative_centered(f, x, 2.0 * h, *args)
        fcount = fcount1 + fcount2
        g = (4.0 * g1 - g2) / 3.0
    else:
        print(u"Error ! Unknown p=", p)
        return None
    return g, fcount


def gradient(f, x, h=None, p=2, *args):
    """
    Computes the gradient of a function f(x).

    Assumes that x is a vector of size n and
    y=f(x) is a float.

    Use finite differences with order p.

    The step size is computed according to the
    optimal value, when f(x)/f''(x) approx 1.

    The function f is supposed to have the
    calling sequence

        y=f(x)

    where x is a vector of size n and y is a float.
    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y=f(x,*args)

    Uses the trick from (Dumontet, Vignes, 1977) to compute the
    step as accurately as possible: see. eq.14, p.16.

    Parameters
    ----------
    f : function
        The function to derivate.
    x : array
        The point where the gradient is to be computed.
    h : float
        The step size.
    p : int
        The order of the formula, p=1, 2 or 4.
    args : list
        The optional arguments of f.

    Returns
    -------
    g : array
        The gradient.
    fcount : int
        The number of function evaluations of f.

    Examples
    --------
    >>> def rosenbrockF(x):
    >>>     # Compute the Rosenbrock cost function.
    >>>     # Reference
    >>>     # "An Automatic Method for Finding the Greatest or Least
    >>>     #  Value of a Function"
    >>>     # H. H. Rosenbrock, 1960, The Computer Journal
    >>>     f = 100.0 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    >>>     return f
    >>>
    >>> x = [-1.2, 1.0]
    >>> g, fcount = gradient(rosenbrockF, x)
    >>> h = 1.e-4
    >>> g, fcount = gradient(rosenbrockF, x, h)
    >>> g, fcount = gradient(rosenbrockF, x, p=4)

    References
    ----------
    J. Dumontet et J. Vignes. « Détermination du pas optimal
    dans le calcul des dérivées sur ordinateur ». In : R.A.I.R.O
    Analyse numérique 11.1 (1977), p. 13-25.
    """

    def gradient_forward(f, x, h, *args):
        """Apply forward_elimination finite difference for gradient."""
        n = np.size(x)
        fcount = n + 1
        E = np.identity(n)
        g = np.zeros(n)
        fx = f(x, *args)
        for i in range(n):
            v = h * E[:, i]
            xp = x + v
            h_exact = xp[i] - x[i]
            fxp = f(xp, *args)
            g[i] = (fxp - fx) / h_exact
        return g, fcount

    def gradient_centered(f, x, h, *args):
        """Apply centered finite difference for gradient."""
        n = np.size(x)
        fcount = 2 * n
        E = np.identity(n)
        g = np.zeros(n)
        for i in range(n):
            v = h * E[:, i]
            xp = x + v
            xm = x - v
            h_exact = xp[i] - xm[i]
            fxp = f(xp, *args)
            fxm = f(xm, *args)
            g[i] = (fxp - fxm) / h_exact
        return g, fcount

    eps = sys.float_info.epsilon
    if h == None:
        h = eps ** (1.0 / (p + 1))
    if p == 1:
        g, fcount = gradient_forward(f, x, h, *args)
    elif p == 2:
        g, fcount = gradient_centered(f, x, h, *args)
    elif p == 4:
        g1, fcount1 = gradient_centered(f, x, h, *args)
        g2, fcount2 = gradient_centered(f, x, 2.0 * h, *args)
        fcount = fcount1 + fcount2
        g = (4.0 * g1 - g2) / 3.0
    else:
        print(u"Error ! Unknown p=", p)
        return None
    return g, fcount


def _fonction_plot_x(x, f, *args):
    """
    Computes the y=f(x), and plot the point x.

    Assumes that x is a vector of size n and
    y=f(x) is a float.

    Parameters
    ----------
    x : a vector, the current point
    f : a function
    args : the extra-arguments of f

    Returns
    -------
    y : float
        The output of the function.
    """
    pl.plot(x[0], x[1], "bo")
    y = f(x, *args)
    return y


def gradient_gui(
    f, x, h=None, p=2, limits_factor=4.0, figure=None, plot_ticks=False, *args
):
    """
    Computes the gradient of f(x)

    Same as gradient(), but plots the point x.

    Parameters
    ----------
    f : function
        The function to derivate.
    x : array
        The point where the gradient is to be computed.
    h : float
        The step size.
    p : int
        The order of the finite difference formula, p=1, 2 or 4
    limits_factor : float
        The factor which multiplies the step size to set the limits.
    figure : matplotlib figure
        The figure to fill.
        If not provided, creates a new figure.
    plot_ticks : bool
        If false, hide the x and y ticks.
    args : list
        The optional arguments of f.

    Returns
    -------
    g : array
        The gradient.
    fcount : int
        The number of function evaluations of f.

    Examples
    --------
    >>> def rosenbrockF(x):
    >>>     # Compute the Rosenbrock cost function.
    >>>     # Reference
    >>>     # "An Automatic Method for Finding the Greatest or Least
    >>>     #  Value of a Function"
    >>>     # H. H. Rosenbrock, 1960, The Computer Journal
    >>>     f = 100.0 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    >>>     return f
    >>>
    >>> x = [-1.2, 1.0]
    >>> g, fcount = gradient_gui(rosenbrockF, x)
    >>> g, fcount = gradient_gui(rosenbrockF, x, p=1)
    >>> g, fcount = gradient_gui(rosenbrockF, x, p=2)
    >>> g, fcount = gradient_gui(rosenbrockF, x, p=4)
    """
    if figure is None:
        figure = pl.figure()
    pl.title(u"Gradient d'ordre %d." % (p))
    if h == None:
        eps = sys.float_info.epsilon
        h = eps ** (1.0 / (p + 1))
    g, fcount = gradient(_fonction_plot_x, x, h, p, f, *args)
    pl.xlabel(u"$x_1$")
    pl.ylabel(u"$x_2$")
    # Enlarge the x and y limits
    pl.xlim(x[0] - limits_factor * h, x[0] + limits_factor * h)
    pl.ylim(x[1] - limits_factor * h, x[1] + limits_factor * h)
    #
    if not plot_ticks:
        pl.xticks([])
        pl.yticks([])
    return g, fcount


def second_derivative(f, x, h=None, p=2, *args):
    """
    Computes f''(x) with finite differences.

    Assumes that x is a vector of size n and
    y=f(x) is a float.

    Function f : same specifications as in gradient.

    Parameters
    ----------
    f : function
        The function to derivate.
    x : point
        The point where the second derivative is to be computed.
    h : float
        The step size.
    p : int
        The order of the finite difference formula, p=1, 2 or 4
    args : list
        The optional arguments of f.

    Returns
    -------
    H : float
        The second derivative.
    fcount : int
        The number of function evaluations of f.

        def mysquare(x):
        y = x ** 2
        return y

    Examples
    --------
    >>> x = 1.0
    >>> h = 1.0e-3
    >>> H, fcount = second_derivative(mysquare, x, h, p=1)
    """

    def second_derivative_forward(f, x, h, *args):
        """Apply forward_elimination finite difference for second derivative."""
        fcount = 4
        fx = f(x, *args)
        xpi = x + h
        fxi = f(xpi, *args)
        xpj = x + h
        fxj = fxi
        xpij = x + 2.0 * h
        fxij = f(xpij, *args)
        h_exact = xpj - x
        g1 = (fxj - fx) / h_exact
        h_exact = xpij - xpi
        g2 = (fxij - fxi) / h_exact
        H = (g2 - g1) / h
        return H, fcount

    def second_derivative_centered(f, x, h, *args):
        """Apply centered finite difference for second derivative."""
        fcount = 3
        xpp = x + 2.0 * h
        fpp = f(xpp, *args)
        xmp = x
        fmp = f(x, *args)
        xpm = x
        fpm = fmp
        xmm = x - 2.0 * h
        fmm = f(xmm, *args)
        h_exact = xpp - xmp
        g2 = (fpp - fmp) / h_exact
        h_exact = xpm - xmm
        g1 = (fpm - fmm) / h_exact
        H = (g2 - g1) / (2.0 * h)
        return H, fcount

    if h == None:
        eps = sys.float_info.epsilon
        h = eps ** (1.0 / (p + 2))
    if p == 1:
        H, fcount = second_derivative_forward(f, x, h, *args)
    elif p == 2:
        H, fcount = second_derivative_centered(f, x, h, *args)
    elif p == 4:
        H1, fcount1 = second_derivative_centered(f, x, h, *args)
        H2, fcount2 = second_derivative_centered(f, x, 2.0 * h, *args)
        fcount = fcount1 + fcount2
        H = (4.0 * H1 - H2) / 3.0
    else:
        print(u"Error ! Unknown p=", p)
        return None
    return H, fcount


def hessian(f, x, h=None, p=2, *args):
    """
    Computes the Hessian matrix of f(x)

    Assumes that x is a vector of size n and
    y=f(x) is a float.

    Function f : same specifications as in gradient.

    Parameters
    ----------
    f : function
        The function to derivate.
    x : array
        The point where the Hessian is to be computed.
    h : float
        The step size.
    p : int
        The order of the finite difference formula, p=1, 2 or 4
    args : list
        The optional arguments of f.

    Returns
    -------
    H : array
        The Hessian matrix.
    fcount : int
        The number of function evaluations of f.

    Examples
    --------
    >>> def rosenbrockF(x):
    >>>     # Compute the Rosenbrock cost function.
    >>>     # Reference
    >>>     # "An Automatic Method for Finding the Greatest or Least
    >>>     #  Value of a Function"
    >>>     # H. H. Rosenbrock, 1960, The Computer Journal
    >>>     f = 100.0 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    >>>     return f
    >>>
    >>> x = [-1.2, 1.0]
    >>> g, fcount = hessian(rosenbrockF, x)
    >>> h = 1.e-4
    >>> g, fcount = hessian(rosenbrockF, x, h)
    >>> g, fcount = hessian(rosenbrockF, x, p=4)
    """

    def hessian_forward(f, x, h, *args):
        """Apply forward_elimination finite difference for Hessian matrix."""
        n = np.size(x)
        fcount = (n + 1) ** 2
        E = np.identity(n)
        H = np.zeros((n, n))
        fx = f(x, *args)
        for i in range(n):
            vi = h * E[:, i]
            xpi = x + vi
            fxi = f(xpi, *args)
            for j in range(i + 1):
                vj = h * E[:, j]
                if j != i:
                    xpj = x + vj
                    fxj = f(xpj, *args)
                else:
                    xpj = x + vi
                    fxj = fxi
                xpij = x + vi + vj
                fxij = f(xpij, *args)
                h_exact = xpj[j] - x[j]
                g1 = (fxj - fx) / h_exact
                h_exact = xpij[j] - xpi[j]
                g2 = (fxij - fxi) / h_exact
                H[i, j] = (g2 - g1) / h
        for i in range(n):
            for j in range(i + 1, n):
                H[i, j] = H[j, i]
        return H, fcount

    def hessian_centered(f, x, h, *args):
        """Apply centered finite difference for Hessian matrix."""
        n = np.size(x)
        fcount = 0
        E = np.identity(n)
        H = np.zeros((n, n))
        for i in range(n):
            vi = h * E[:, i]
            for j in range(i + 1):
                vj = h * E[:, j]
                xpp = x + vi + vj
                fpp = f(xpp, *args)
                if j != i:
                    xmp = x - vi + vj
                    fmp = f(xmp, *args)
                    xpm = x + vi - vj
                    fpm = f(xpm, *args)
                    fcount += 2
                else:
                    xmp = x
                    fmp = f(x, *args)
                    fcount += 1
                    xpm = x
                    fpm = fmp
                xmm = x - vi - vj
                fmm = f(xmm, *args)
                fcount += 1
                h_exact = xpp[i] - xmp[i]
                g2 = (fpp - fmp) / h_exact
                h_exact = xpm[i] - xmm[i]
                g1 = (fpm - fmm) / h_exact
                H[i, j] = (g2 - g1) / (2 * h)
        for i in range(n):
            for j in range(i + 1, n):
                H[i, j] = H[j, i]
        return H, fcount

    if h == None:
        eps = sys.float_info.epsilon
        h = eps ** (1.0 / (p + 2))
    if p == 1:
        H, fcount = hessian_forward(f, x, h, *args)
    elif p == 2:
        H, fcount = hessian_centered(f, x, h, *args)
    elif p == 4:
        H1, fcount1 = hessian_centered(f, x, h, *args)
        H2, fcount2 = hessian_centered(f, x, 2.0 * h, *args)
        fcount = fcount1 + fcount2
        H = (4.0 * H1 - H2) / 3.0
    else:
        print(u"Error ! Unknown p=", p)
        return None
    return H, fcount


def hessian_gui(f, x, h=None, p=2, limits_factor=6.0, *args):
    """
    Computes the Hessian matrix of f and points the points where f is evaluated.

    Same as hessian, but plots the point x.

    Parameters
    ----------
    f : function
        The function to derivate.
    x : array
        The point where the Hessian is to be computed.
    h : float
        The step size.
    p : int
        The order of the finite difference formula, p=1, 2 or 4
    limits_factor : float
        The factor which multiplies the step size to set the limits.
    args : list
        The optional arguments of f.

    Returns
    -------
    H : array
        The Hessian matrix.
    fcount : int
        The number of function evaluations of f.

    Examples
    --------
    >>> def rosenbrockF(x):
    >>>     # Compute the Rosenbrock cost function.
    >>>     # Reference
    >>>     # "An Automatic Method for Finding the Greatest or Least
    >>>     #  Value of a Function"
    >>>     # H. H. Rosenbrock, 1960, The Computer Journal
    >>>     f = 100.0 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
    >>>     return f
    >>>
    >>> x = [-1.2, 1.0]
    >>> g, fcount = hessian_gui(rosenbrockF, x)
    >>> h = 1.e-4
    >>> g, fcount = hessian_gui(rosenbrockF, x, h)
    >>> g, fcount = hessian_gui(rosenbrockF, x, p=4)
    """
    pl.figure()
    pl.title(u"Hessienne d'ordre %d." % (p))
    if h == None:
        eps = sys.float_info.epsilon
        h = eps ** (1.0 / (p + 2))
    H, fcount = hessian(_fonction_plot_x, x, h, p, f, *args)
    # Enlarge the x and y limits
    pl.xlim(x[0] - limits_factor * h, x[0] + limits_factor * h)
    pl.ylim(x[1] - limits_factor * h, x[1] + limits_factor * h)
    return H, fcount


def derivative_centered(f, x, d, h=None, *args):
    """
    Computes the degree d derivative of f at point x.

    Uses a method based on a centered finite difference formula with order 2.
    If the step is not provided, uses the approximately optimal
    step size.

    Parameters
    ----------
    f : function
        The function.
    x : float
        The point where the derivative is to be evaluated.
    h : float
        The step.
    d : int
        The degree of the derivative of f.
    *args : list
        The optional arguments of f.

    Returns
    -------
    y : float
        A approximation of the d-th derivative of f at point x.

    """
    if h is None:
        eps = sys.float_info.epsilon
        h = eps ** (1.0 / (2 + d))
    y = np.zeros((d + 1))
    for i in range(d + 1):
        y[i] = f(x + i * 2.0 * h - d * h, *args)
    for k in range(d, 0, -1):
        for i in range(k):
            y[i] = (y[i + 1] - y[i]) / (2.0 * h)
    return y[0]


def derivative_forward(f, x, order, h=None, *args):
    """
    Computes the order d derivative of f at point x.

    Uses a method based on a forward_elimination finite difference formula
    with precision order 1.
    If the step is not provided, uses the approximately optimal
    step size.

    Parameters
    ----------
    f : function
        The function.
    x : float
        The point where the derivative is to be evaluated.
    h : float
        The step.
    order : int
        The order of the derivative of f.
    *args : list
        The optional arguments of f.

    Returns
    -------
    y : float
        A approximation of the d-th derivative of f at point x.

    Examples
    --------
    >>> import numpy as np
    >>> x = 1.0
    >>> order = 3  # Compute f'''
    >>> y = derivative_forward(np.sin, x, order)
    """
    if h is None:
        eps = sys.float_info.epsilon
        h = eps ** (1.0 / (1 + order))
    y = np.zeros((order + 1))
    for i in range(order + 1):
        y[i] = f(x + i * h, *args)
    for k in range(order, 0, -1):
        for i in range(k):
            y[i] = (y[i + 1] - y[i]) / h
    return y[0]


def compute_indices(order, p, direction="centered"):
    """
    Computes the min and max indices for a finite difference formula.

    This function is used by compute_coefficients() to compute the
    derivative of arbitrary order and arbitrary order of accuracy.

    Parameters
    ----------
    order : int
        The order of the derivative.
    p : int
        The order of precision of the formula.
    direction : str, optional
        The direction of the formula.
        The direction can be "forward", "backward" or "centered".
        The default is "centered".

    Raises
    ------
    ValueError
        If direction is "centered", d + p must be odd.

    Returns
    -------
    imin : int
        The minimum indice of the f.d. formula.
    imax : int
        The maximum indice of the f.d. formula.

    Examples
    --------
    >>> order = 3  # Compute f'''
    >>> p = 6  # Use order 6 formula
    >>> imin, imax = compute_indices(order, p)
    >>> imin, imax = compute_indices(order, p, "forward")
    >>> imin, imax = compute_indices(order, p, "backward")
    >>> imin, imax = compute_indices(order, p, "centered")
    """
    if direction == "forward":
        imin = 0
        imax = order + p - 1
    elif direction == "backward":
        imin = -(order + p - 1)
        imax = 0
    elif direction == "centered":
        if (order + p) % 2 == 0:
            raise ValueError("d+p must be odd for a centered formula.")
        imax = (order + p - 1) // 2
        imin = -imax
    else:
        raise ValueError("Invalid direction = %s" % (direction))
    return (imin, imax)


def compute_coefficients(order, p, direction="centered"):
    """
    Computes the coefficients of the finite difference formula.

    Parameters
    ----------
    order : int
        The order of the derivative.
    p : int
        The order of precision of the formula.
    direction : str, optional
        The direction of the formula.
        The direction can be "forward", "backward" or "centered".
        The default is "centered".

    Raises
    ------
    ValueError
        If direction is "centered", order + p must be odd.

    Returns
    -------
    c : np.array(order + p)
        The coefficicients of the finite difference formula.

    Examples
    --------
    >>> order = 3  # Compute f'''
    >>> p = 6  # Use order 6 formula
    >>> c = compute_coefficients(order, p)
    >>> c = compute_coefficients(order, p, "forward")
    >>> c = compute_coefficients(order, p, "backward")
    >>> c = compute_coefficients(order, p, "centered")
    """
    # Compute matrix
    imin, imax = compute_indices(order, p, direction)
    indices = list(range(imin, imax + 1))
    A = np.vander(indices, increasing=True).T
    # Compute right-hand side
    b = np.zeros((order + p))
    b[order] = 1.0
    # Solve
    c = np.linalg.solve(A, b)
    return c


def finite_differences(f, x, order, p, direction="centered", h=None, *args):
    """
    Computes the degree d derivative of f at point x.

    Uses a finite difference formula with order p.
    If the step is not provided, uses the approximately optimal
    step size.
    If direction is "centered", if d is even and if p is odd,
    then the order of precision is actually p + 1.

    Parameters
    ----------
    f : function
        The function.
    x : float
        The point where the derivative is to be evaluated.
    order : int
        The order of the derivative of f.
    p : int
        The order of precision of the formula.
    direction : str, optional
        The direction of the formula.
        The direction can be "forward", "backward" or "centered".
        The default is "centered".
    h : float
        The step.
    *args : list
        The optional arguments of f.

    Raises
    ------
    ValueError
        If direction is "centered", d + p must be odd.

    Returns
    -------
    z : float
        A approximation of the d-th derivative of f at point x.

    Examples
    --------
    >>> import numpy as np
    >>> x = 1.0
    >>> order = 3  # Compute f'''
    >>> p = 2  # Use order 2 precision
    >>> y = finite_differences(np.sin, x, order, p)
    >>> y = finite_differences(np.sin, x, order, p, "forward")

    """
    # Compute the optimal step size
    if h is None:
        if direction == "centered" and order % 2 == 0 and p % 2 == 1:
            eps = sys.float_info.epsilon
            h = eps ** (1.0 / (order + p + 1))
        else:
            eps = sys.float_info.epsilon
            h = eps ** (1.0 / (order + p))
    # Compute the function values
    imin, imax = compute_indices(order, p, direction)
    y = np.zeros((order + p))
    for i in range(imin, imax + 1):
        y[i - imin] = f(x + i * h, *args)
    # Compute the coefficients
    c = compute_coefficients(order, p, direction)
    # Apply the formula
    z = 0.0
    for i in range(imin, imax + 1):
        z += c[i - imin] * y[i - imin]
    factor = np.math.factorial(order) / h ** order
    z *= factor
    return z


def jacobian(fun, x, h=None, p=2, *args):
    """
    Computes the Jacobian matrix of a vector function f(x)

    Assumes that x is a vector of size n and
    y=f(x) is a vector.

    Use finite differences with order p.

    The step size is computed according to the
    optimal value, when f(x)/f''(x) approx 1.

    The function f is supposed to have the
    calling sequence

        y=f(x)

    where x is a vector of size n and y is a float.
    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y=f(x,*args)

    Parameters
    ----------
    f : function
        The function to derivate.
    x : array
        The point where the gradient is to be computed.
    h : float
        The step size.
    p : int
        The order of precision of the formula, p=1, 2 or 4.
    args : list
        The optional arguments of f.

    Returns
    -------
    g : array
        The gradient.
    fcount : int
        The number of function evaluations of f.

    Examples
    --------
    >>> def test_f(x):
    >>>     A = np.array([[1.0, 2.0], [3.0, 4.0]])
    >>>     y = A @ x
    >>>     return y
    >>>
    >>> x = np.array([1.0, 1.0])
    >>> J = jacobian(test_f, x)
    >>> J = jacobian(test_f, x, p=1)
    >>> J = jacobian(test_f, x, p=4)
    """

    def jacobian_forward(fun, x, h, *args):
        J = np.zeros((x.size, x.size))
        for i in range(x.size):
            dx = np.zeros((x.size))
            dx[i] = h[i]
            xp = x + dx
            h_exact = xp[i] - x[i]
            y1 = fun(xp, *args)
            y2 = fun(x, *args)
            J[:, i] = (y1 - y2) / h_exact
        return J

    def jacobian_centered(fun, x, h, *args):
        J = np.zeros((x.size, x.size))
        for i in range(x.size):
            dx = np.zeros((x.size))
            dx[i] = h[i]
            xp = x + dx
            xm = x - dx
            twice_h = xp[i] - xm[i]
            y1 = fun(xp, *args)
            y2 = fun(xm, *args)
            J[:, i] = (y1 - y2) / twice_h
        return J

    if h == None:
        eps = sys.float_info.epsilon
        h_scalar = eps ** (1.0 / (p + 1))
        h = np.ones((x.size)) * h_scalar
    if p == 1:
        J = jacobian_forward(fun, x, h, *args)
    elif p == 2:
        J = jacobian_centered(fun, x, h, *args)
    elif p == 4:
        # Richardson extrapolation
        J1 = jacobian_centered(fun, x, h, *args)
        J2 = jacobian_centered(fun, x, 2.0 * h, *args)
        J = (4.0 * J1 - J2) / 3.0
    else:
        raise ValueError("Wrong value of p=", p)
    return J


if __name__ == "__main__":
    runGraphics = True
    from numpy import sin, logspace, log10, cos

    def myfunc(x):
        y = sin(x)
        return y

    x = 1.0
    h = 1.0e-4
    g, fcount = first_derivative(myfunc, x, h, p=1)
    np.testing.assert_almost_equal(g, cos(x), decimal=4)
    g, fcount = first_derivative(myfunc, x, h, p=2)
    np.testing.assert_almost_equal(g, cos(x), decimal=6)
    g, fcount = first_derivative(myfunc, x, h, p=4)
    np.testing.assert_almost_equal(g, cos(x), decimal=8)

    # 2.3 Plot digits
    n = 100
    d = np.zeros(n)
    x = [1.0]
    exact = cos(x)
    h = logspace(0, -15, n)
    for i in range(n):
        g, fcount = gradient(myfunc, x, h[i], p=1)
        d[i] = -log10(abs(exact - g) / exact)

    if runGraphics:
        pl.plot(log10(h), d, ".-")
        pl.xlabel(u"Log10(Step size)")
        pl.ylabel(u"Number of digits")
        pl.title(u"Compute f' by finite differences")
        pl.show()

    # 2.3 Plot digits
    n = 100
    d = np.zeros(n)
    x = 1.0
    exact = np.cos(x)
    h = np.logspace(0, -15, n)
    for i in range(n):
        g, fcount = gradient(myfunc, x, h[i], p=2)
        d[i] = -np.log10(abs(exact - g) / exact)

    if runGraphics:
        pl.plot(log10(h), d, ".-")
        pl.xlabel(u"Log10(Step size)")
        pl.ylabel(u"Number of digits")
        pl.title(u"Compute f' by finite differences")
        pl.show()

    def rosenbrockF(x):
        """
        Compute the Rosenbrock cost function.

        Calling sequence
        f=rosenbrockF(x)

        Arguments
        x : a 2-by-1 array, the point where to compute
            the cost function
        f : a double, the value of the cost function

        Reference
        "An Automatic Method for Finding the Greatest or Least
         Value of a Function"
        H. H. Rosenbrock, 1960, The Computer Journal

        Notes:
        Starting point is x0 = [-1.2 1.0]
        f(x0)=   24.2
        Minimum is xopt = [1 1]
        f(x0)=   0.
        """
        f = 100.0 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2
        return f

    # Multivariate function
    # Gradient - order 2
    print(u"Rosenbrock\n")
    x = [-1.2, 1.0]
    g, fcount = gradient(rosenbrockF, x)
    print(u"gradient (order 2)=", g)
    print(u"Function calls=", fcount)
    # Gradient - order 1
    print(u"Order 1\n")
    x = [-1.2, 1.0]
    g, fcount = gradient(rosenbrockF, x, p=1)
    print(u"gradient (order 1)=", g)
    print(u"Function calls=", fcount)
    # Gradient - order 4
    print(u"Order 1\n")
    x = [-1.2, 1.0]
    g, fcount = gradient(rosenbrockF, x, p=4)
    print(u"gradient (order 4)=", g)
    print(u"Function calls=", fcount)
    # Hessian - order 2
    H, fcount = hessian(rosenbrockF, x, p=2)
    print(u"H (order 2)=", H)
    print(u"Function calls=", fcount)
    # Hessian - order 1
    H, fcount = hessian(rosenbrockF, x, p=1)
    print(u"H (order 1)=", H)
    print(u"Function calls=", fcount)
    # Hessian - order 4
    H, fcount = hessian(rosenbrockF, x, p=4)
    print(u"H (order 4)=", H)
    print(u"Function calls=", fcount)

    #
    # Dessine le stencil du gradient
    def fausse_fonction(x):
        y = 1.0
        print(x)
        return y

    x = [0.0, 0.0]
    limits_factor = 2.5
    g, fcount = gradient_gui(fausse_fonction, x, p=1, limits_factor=limits_factor)
    g, fcount = gradient_gui(fausse_fonction, x, p=2, limits_factor=limits_factor)
    g, fcount = gradient_gui(fausse_fonction, x, p=4, limits_factor=limits_factor)
    #
    # Dessine le stencil de la Hessienne
    limits_factor = 5.0
    g, fcount = hessian_gui(fausse_fonction, x, p=1, limits_factor=limits_factor)
    g, fcount = hessian_gui(fausse_fonction, x, p=2, limits_factor=limits_factor)
    g, fcount = hessian_gui(fausse_fonction, x, p=4, limits_factor=limits_factor)
    # Check derivative_centered
    x = 1.0
    order = 3
    expected = -np.cos(x)
    print(u"f(3)(x)=", expected)
    y = derivative_forward(np.sin, x, order)
    np.testing.assert_almost_equal(y, expected, decimal=3)
    y = derivative_centered(np.sin, x, order)
    np.testing.assert_almost_equal(y, expected, decimal=6)

    # Check finite_differences
    # Evalue f'''(x) with f(x)= sin(x)
    x = 1.0
    exact = -np.cos(x)
    order = 3
    direction = "centered"
    for p in [2, 4, 6]:
        y = finite_differences(np.sin, x, order, p, direction=direction)
        np.testing.assert_almost_equal(y, exact, decimal=6)
    for p in range(3, 5):
        for direction in ["forward", "backward"]:
            y = finite_differences(np.sin, x, order, p, direction=direction)
            np.testing.assert_almost_equal(y, exact, decimal=6)
    # Check Jacobian
    def test_f(x):
        A = np.array([[1.0, 2.0], [3.0, 4.0]])
        y = A @ x
        return y

    J_exact = np.array([[1.0, 2.0], [3.0, 4.0]])
    x = np.array([1.0, 1.0])
    for p in [1, 2, 4]:
        J = jacobian(test_f, x, p=p)
        print(u"order=", p, "J=")
        print(J)
        np.testing.assert_almost_equal(J, J_exact, decimal=6)

    def mysquare(x):
        y = x ** 2
        return y

    # Compute second derivative
    x = 1.0
    h = 1.0e-3
    expected = 2.0
    H, fcount = second_derivative(mysquare, x, h, p=1)
    np.testing.assert_almost_equal(H, expected, decimal=6)
    H, fcount = second_derivative(mysquare, x, h, p=2)
    np.testing.assert_almost_equal(H, expected, decimal=6)
    H, fcount = second_derivative(mysquare, x, p=4)
    np.testing.assert_almost_equal(H, expected, decimal=6)

    def mysquare_vector(x):
        y = x[0] ** 2
        return y

    # Compute second derivative
    x = [1.0]
    h = 1.0e-4
    expected = 2.0
    H, fcount = hessian(mysquare_vector, x, h, p=1)
    np.testing.assert_almost_equal(H, expected, decimal=6)
    H, fcount = hessian(mysquare_vector, x, h, p=1)
    np.testing.assert_almost_equal(H, expected, decimal=6)
    H, fcount = hessian(mysquare_vector, x, p=4)
    np.testing.assert_almost_equal(H, expected, decimal=6)
