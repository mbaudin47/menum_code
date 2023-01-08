# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
A collection of functions for numerical optimization.

Reference
---------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

from math import sqrt
from sys import float_info
import pylab as pl
import numpy as np


def goldensection(f, a, b, reltolx=None, *args):
    """
    Minimizes a one-variable function with golden section search.

    This function uses the golden section search algorithm in
    order to find an approximate x which minimizes the function f
    in the interval [a,b].

    Parameters
    ----------
    f : function
        The function to minimize.
    a : float
        The lower bound for the optimum
    b : float, the upper bound for the optimum
    reltolx : float
        The relative tolerance on x.
        Default = 2 * sqrt(eps) where eps is the machine epsilon.
    args : list
        Extra-arguments for f

    Returns
    -------
    xopt : float
        The approximate solution in [a,b]
    fopt : float
        The function value at xopt

    Examples
    --------
    >>> def conductivity(x):
    >>>     a = 0.034
    >>>     b = 4.739e-06
    >>>     c = 0.03815
    >>>     y = a + b * x + c / x
    >>>     return y
    >>>
    >>> import numpy as np
    >>> from optim import goldensection
    >>> a = 0.034
    >>> b = 4.739e-06
    >>> c = 0.03815
    >>> xexact = np.sqrt(c / b)
    >>> fexact = conductivity(xexact)
    >>> reltolx = 1.0e-8
    >>> xopt, fopt = goldensection(conductivity, 30.0, 200.0, reltolx)

    References
    -----------
    http://en.wikipedia.org/wiki/Golden_section_search

    Kiefer, J. (1953), "Sequential minimax search for a maximum",
    Proceedings of the American Mathematical
    Society 4 (3): 502-506
    """
    if reltolx == None:
        reltolx = 2.0 * sqrt(float_info.epsilon)
    phi = (1.0 + sqrt(5.0)) / 2.0
    rho = 2.0 - phi
    fa = f(a, *args)
    fb = f(b, *args)
    x1 = (1.0 - rho) * a + rho * b
    f1 = f(x1, *args)
    x2 = rho * a + (1.0 - rho) * b
    f2 = f(x2, *args)
    while abs(b - a) > reltolx * max([abs(b), 1.0]):
        if f1 <= f2:  # x* in [a,x2]
            b = x2
            fb = f2
            x2 = x1
            f2 = f1
            x1 = (1.0 - rho) * a + rho * b
            f1 = f(x1, *args)
        else:  # x* in [x1,b]
            a = x1
            fa = f1
            x1 = x2
            f1 = f2
            x2 = rho * a + (1.0 - rho) * b
            f2 = f(x2, *args)
    if fa < fb:
        xopt = a
        fopt = fa
    else:
        xopt = b
        fopt = fb
    return xopt, fopt


def goldensectiongui(f, a, b, reltolx=None, *args):
    """
    Minimizes a one-variable function with golden section search.

    This function uses the golden section search algorithm in
    order to find an approximate x which minimizes the function f
    in the interval [a,b].

    Moreover, plots the intermediate points during the search.

    * red : a
    * blue : b
    * green : x1
    * yellow : x2

    Parameters
    ----------
    f : function
        The function to minimize.
    a : float
        The lower bound for the optimum
    b : float, the upper bound for the optimum
    reltolx : float
        The relative tolerance on x.
        Default = 2 * sqrt(eps) where eps is the machine epsilon.
    args : list
        Extra-arguments for f

    Returns
    -------
    xopt : float
        The approximate solution in [a,b]
    fopt : float
        The function value at xopt

    Examples
    --------
    >>> def conductivity(x):
    >>>     a = 0.034
    >>>     b = 4.739e-06
    >>>     c = 0.03815
    >>>     y = a + b * x + c / x
    >>>     return y
    >>>
    >>> import numpy as np
    >>> from optim import goldensectiongui
    >>> a = 0.034
    >>> b = 4.739e-06
    >>> c = 0.03815
    >>> xexact = np.sqrt(c / b)
    >>> fexact = conductivity(xexact)
    >>> reltolx = 1.0e-8
    >>> xopt, fopt = goldensectiongui(conductivity, 30.0, 200.0, reltolx)

    References
    ----------
    http://en.wikipedia.org/wiki/Golden_section_search

    Kiefer, J. (1953), "Sequential minimax search for a maximum",
    Proceedings of the American Mathematical
    Society 4 (3): 502-506
    """
    # Plot the function
    N = 100
    x = np.linspace(min([a, b]), max([a, b]), N)
    y = np.zeros((N, 1))
    for i in range(N):
        y[i] = f(x[i], *args)
    pl.plot(x, y, "-")
    pl.xlabel(u"x")
    pl.ylabel(u"f(x)")

    if reltolx == None:
        reltolx = 2 * sqrt(float_info.epsilon)
    phi = (1.0 + sqrt(5.0)) / 2.0
    rho = 2.0 - phi
    print(u"iter, x, f(x)")
    fa = f(a, *args)
    fb = f(b, *args)
    x1 = a + rho * (b - a)
    f1 = f(x1, *args)
    x2 = b - rho * (b - a)
    f2 = f(x2, *args)
    pl.plot(a, fa, "ro")
    pl.plot(b, fb, "bo")
    pl.plot(x1, f1, "go")
    pl.plot(x2, f2, "yo")
    print(u"0, %f, %f" % (a, fa))
    print(u"0, %f, %f" % (b, fb))
    print(u"0, %f, %f" % (x1, f1))
    print(u"0, %f, %f" % (x2, f2))
    i = 0
    while abs(b - a) > reltolx * max([abs(b), 1.0]):
        i = i + 1
        if f1 <= f2:
            b = x2
            fb = f2
            x2 = x1
            f2 = f1
            x1 = a + rho * (b - a)
            f1 = f(x1, *args)
            pl.plot(x1, f1, "go")
            print(u"%d, %f, %f" % (i, x1, f1))
        else:
            a = x1
            fa = f1
            x1 = x2
            f1 = f2
            x2 = b - rho * (b - a)
            f2 = f(x2, *args)
            pl.plot(x2, f2, "yo")
            print(u"%d, %f, %f" % (i, x2, f2))
    if fa < fb:
        xopt = a
        fopt = fa
    else:
        xopt = b
        fopt = fb
    return xopt, fopt


if __name__ == "__main__":
    from floats import computeDigits

    # 1. goldensectiongui

    def conductivity(x):
        a = 0.034
        b = 4.739e-06
        c = 0.03815
        y = a + b * x + c / x
        return y

    a = 0.034
    b = 4.739e-06
    c = 0.03815
    xexact = 89.72302695368212  # np.sqrt(c / b)
    fexact = conductivity(xexact)
    reltolx = 1.0e-8

    runGraphics = True
    if runGraphics:
        xopt, fopt = goldensectiongui(conductivity, 30.0, 200.0, reltolx)
        print(u"xopt=", xopt)
        print(u"fopt=", fopt)
        print(u"X Digits:", computeDigits(xopt, xexact, 10), " (must be >6)")
        print(u"F Digits:", computeDigits(fopt, fexact, 10), " (must be >15)")
        np.testing.assert_almost_equal(xopt, xexact, decimal=5)
        np.testing.assert_almost_equal(fopt, fexact, decimal=14)

    # 2. goldensection
    xopt, fopt = goldensection(conductivity, 30.0, 200.0, reltolx)
    print(u"xopt=", xopt)
    print(u"fopt=", fopt)
    print(u"X Digits:", computeDigits(xopt, xexact, 10), " (must be >6)")
    print(u"F Digits:", computeDigits(fopt, fexact, 10), " (must be >15)")
    np.testing.assert_almost_equal(xopt, xexact, decimal=5)
    np.testing.assert_almost_equal(fopt, fexact, decimal=14)

    # With parameters
    def conductivity_param(x, a, b, c):
        y = a + b * x + c / x
        return y

    xopt, fopt = goldensection(conductivity_param, 30.0, 200.0, reltolx, a, b, c)
    np.testing.assert_almost_equal(xopt, xexact, decimal=5)
    np.testing.assert_almost_equal(fopt, fexact, decimal=14)
