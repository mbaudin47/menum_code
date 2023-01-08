# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
A collection of functions to compute the solution of non linear equations.

Reference
---------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import sys
import pylab as pl
import numpy as np
from interp import polynomial_interpolation


def _compute_and_plot(x, f, *args):
    """
    Plots (x, 0.0) and computes y=f(x).

    This function is used in the bisection to see where the function
    is evaluated.

    Parameters
    ----------
    x : float
        The abscissa of the point to plot.
    f : function
        The function
    *args : a list
        The extra input arguments for f.

    Returns
    -------
    y : float
        The value of f(x).
    """
    pl.plot(x, 0.0, "b|")
    print(u"x=%.17e" % (x))
    y = f(x, *args)
    return y


def _function_plot(f, a, b, N=100, *args):
    """
    Plot the function f on interval [a, b].

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The left boundary
    b : float
        The right boundary
    N : int
        The number of points.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    None.

    """
    x = np.linspace(min([a, b]), max([a, b]), N)
    y = np.zeros((N, 1))
    for i in range(N):
        y[i] = f(x[i], *args)
    pl.figure()
    pl.plot(x, y, "-")
    pl.xlabel(u"x")
    pl.ylabel(u"f(x)")
    return None


def bisection(f, a, b, reltolx=None, abstolx=0.0, verbose=False, *args):
    """
    Solves f(x)=0 by bisection.

    This function solves the equation

    f(x)=0

    for the real variable x.

    The root must be bracketed in (a,b), i.e.
    we must have the mathematical condition:

    f(a) * f(b) < 0.

    On output we have abs(b-a)<=reltolx*max(abs(c),1.).

    The function f must have the calling sequence

    y=f(x)

    where x and y are floats.

    The calling sequence of f must be

    y=f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y=f(x,*args)

    In order to avoid unnecessary underflow / overflow, we
    do not use the naive statement:

        f(a) * f(b) < 0

    but rather:

        if np.sign(fa) != np.sign(fb)

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The left boundary
    b : float
        The right boundary
    reltolx : float
        The relative tolerance on x.
        We must have reltolx > 0.
        Default is twice the machine epsilon.
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    verbose : bool
        If True, print intermediate messages.

    Returns
    -------
    c : float
        The approximate root.
    history : list of floats
        The approximate roots computed
        of the iterations of the algorithm

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = bisection(myFunction, 1.0, 2.0)

    Bibliography
    ------------
    Malcolm, Michael A., Cleve B. Moler, and George Elmer Forsythe.
    Computer methods for mathematical computations. Prentice-Hall, 1977.
    """
    if reltolx == None:
        reltolx = 2.0 * sys.float_info.epsilon
    history = []
    history.append(a)
    fa = f(a, *args)
    if fa == 0.0:
        return a, history
    history.append(b)
    fb = f(b, *args)
    if fb == 0.0:
        return b, history
    if verbose:
        print("a=%.3e, fa=%.3e" % (a, fa))
        print("b=%.3e, fb=%.3e" % (b, fb))
    if np.sign(fa) == np.sign(fb):
        raise ValueError(u"The interval (a,b) does not bracket a root")
    k = 0
    while abs(b - a) > reltolx * abs(b) + abstolx:
        c = (a + b) / 2.0
        fc = f(c, *args)
        history.append(c)
        if fc == 0:
            break
        elif np.sign(fa) != np.sign(fc):
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        if verbose:
            print("In [%.3e, %.3e] @ [%.3e, %.3e]" % (a, b, fa, fb))
        k = k + 1
        if k > 100:
            raise ValueError(u"Warning : maximum number of iterations reached!")
    return c, history


def bisectiongui(f, a, b, reltolx=None, abstolx=0.0, *args):
    """
    Solves f(x)=0 by bisection and plots the intermediate approximate roots.

    Same as bisection, with plot.

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The left boundary
    b : float
        The right boundary
    reltolx : float
        The relative tolerance on x.
        We must have reltolx>0.
        Default is twice the machine epsilon.
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    c : float
        The approximate root.
    history : list of floats
        The approximate roots computed
        of the iterations of the algorithm

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = bisectiongui(myFunction, 1.0, 2.0)
    """
    N = 100
    _function_plot(f, a, b, N, *args)
    verbose = False
    c, history = bisection(_compute_and_plot, a, b, reltolx, abstolx, verbose, f, *args)
    return c, history


def newton(f, x0, fprime, reltolx=None, abstolx=0.0, verbose=False, *args):
    """
    Solves f(x)=0 by Newton-Raphson.

    This function solves the equation

    f(x)=0

    for the real variable x.

    The derivative can be computed
    from finite differences if required.

    On output we have abs(x - xprev) <= reltolx * max(abs(x), 1.0)
    where xprev is the previous value of x in the algorithm.

    The function f must have the calling sequence

    y=f(x)

    where x and y are floats.

    The calling sequence of fprime must be

    y=fprime(x)

    where x and y are floats.

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y=f(x,*args)

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    x0 : float
        The initial guess
    fprime : function
        The first derivative of f
    reltolx : float
        The relative tolerance on x.
        Default is twice the machine epsilon.
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    verbose : bool
        If True, print intermediate messages.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    x : float
        The approximate root.
    history : list of floats
        The approximate root
        computed during the iterations of the algorithm

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> def myFunctionPrime(x):
    >>>     y = 2 * x
    >>>     return y
    >>>
    >>> xs, history = newton(myFunction, 1.0, myFunctionPrime)
    """
    if reltolx == None:
        reltolx = 2.0 * sys.float_info.epsilon
    xprev = float("inf")
    x = x0
    history = [x0]
    k = 0
    while abs(x - xprev) > reltolx * abs(x) + abstolx:
        xprev = x
        fx = f(x, *args)
        if verbose:
            print("x=%.3e, fx=%.3e" % (x, fx))
        if fx == 0.0:
            break
        s = fprime(x, *args)
        x = x - fx / s
        history.append(x)
        k = k + 1
        if k > 100:
            raise ValueError(u"Maximum number of iterations reached!")
    return x, history


def newtongui(f, x0, fprime, reltolx=None, abstolx=0.0, *args):
    """
    Solves f(x)=0 by newton and
    plots the intermediate approximate roots computed
    during the algorithm.

    Same as newton, with a plot.

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    x0 : float
        The initial guess
    fprime : function
        The first derivative of f
    reltolx : float
        The relative tolerance on x.
        Default is twice the machine epsilon.
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    x : float
        The approximate root.
    history : list of floats
        The approximate root
        computed during the iterations of the algorithm

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> def myFunctionPrime(x):
    >>>     y = 2 * x
    >>>     return y
    >>>
    >>> xs, history = newtongui(myFunction, 1.0, myFunctionPrime)
    """
    verbose = False
    c, history = newton(
        _newton_fplot, x0, _newton_fprime_plot, reltolx, abstolx, verbose, f, fprime, *args
    )
    return c, history


def _newton_fplot(x, f, fprime, *args):
    """
    Plots a blue bar at abscissa x, and computes y=f(x).

    This function is used by newtongui.

    Parameters
    ----------
    x : float
        The function where the function must be plotted.
    f : function
        The function involved in the non linear equation.
    fprime : function
        The first derivative of f.
    args : list
        The extra input arguments for f.

    Returns
    -------
    y : float
        The value of f(x)
    """
    y = _compute_and_plot(x, f, *args)
    return y


def _newton_fprime_plot(x, f, fprime, *args):
    """
    Computes y=f'(x).

    This function is used by newtongui.

    Parameters
    ----------
    x : float
        The point where the first derivative must be evaluated.
    f : function
        The function involved in the non linear equation.
    fprime : function
        The derivative of f
    *args : list
        The extra input arguments for f.

    Returns
    -------
    y : float
        The value of fprime(x)
    """
    y = fprime(x, *args)
    return y


def secant(f, a, b, reltolx=None, abstolx=0.0, verbose=False, *args):
    """
    Solves f(x)=0 by secant's method.

    This function solves the equation

    f(x)=0

    for the real variable x.

    The root must be bracketed in (a,b), i.e.
    we must have the mathematical condition:

    f(a) * f(b)<0.

    On output we have abs(b - a) <= reltolx * max(abs(c), 1.0).

    The function f must have the calling sequence

    y=f(x)

    where x and y are floats.

    The calling sequence of f must be

    y=f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y=f(x,*args)

    The implementation avoids the naive update:

        b = (fc * b - fb * c) / (fc - fb)

    so as to avoid unnecessary overflows / underflows.

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The left boundary
    b : float
        The right boundary
    reltolx : float
        The relative tolerance on x, reltolx>0.
        Default is twice the machine epsilon
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    verbose : bool
        If True, print intermediate messages.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    c : float
        The approximate root
    history : list of floats
        The approximate roots computed
        during the iterations of the algorithm.

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = secant(myFunction, 1.0, 2.0)
    """
    if reltolx == None:
        reltolx = 2.0 * sys.float_info.epsilon
    history = []
    history.append(a)
    fa = f(a, *args)
    if fa == 0.0:
        return a, history
    history.append(b)
    fb = f(b, *args)
    if fb == 0.0:
        return b, history
    if verbose:
        print("a=%.3e, fa=%.3e" % (a, fa))
        print("b=%.3e, fb=%.3e" % (b, fb))
    if np.sign(fa) == np.sign(fb):
        raise ValueError(u"The interval (a,b) does not bracket a root")
    k = 0
    while abs(b - a) > reltolx * abs(b) + abstolx:
        c = a  # c=x(n-1)
        fc = fa
        a = b  # a=x(n)
        fa = fb
        t = fc / fb
        b = b + (b - c) / (t - 1.0)
        fb = f(b, *args)
        history.append(b)
        if fb == 0.0:
            break
        if verbose:
            print("b=%.3e, fb=%.3e" % (b, fb))
        k = k + 1
        if k > 100:
            raise ValueError(u"Maximum number of iterations reached!")
    return b, history


def secantgui(f, a, b, reltolx=None, abstolx=0.0, *args):
    """
    Solves f(x)=0 by secant and plots the intermediate approximate roots.

    Same as secant with a plot.

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The left boundary
    b : float
        The right boundary
    reltolx : float
        The relative tolerance on x, reltolx>0.
        Default is twice the machine epsilon
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    c : float
        The approximate root
    history : list of floats
        The approximate roots computed
        during the iterations of the algorithm.

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = secant(myFunction, 1.0, 2.0)
    """
    N = 100
    _function_plot(f, a, b, N, *args)
    verbose = False
    c, history = secant(_compute_and_plot, a, b, reltolx, abstolx, verbose, f, *args)
    return c, history


def zeroin(f, a, b, reltolx=None, abstolx=0.0, verbose=False, *args):
    """
    Solves f(x)=0 by Dekker-Brent algorithm.

    This function solves the equation

    f(x)=0

    for the real variable x.

    The algorithm combines three methods : bisection,
    secant and inverse quadratic interpolation (IQI).

    The root must be bracketed in (a,b), i.e.
    we must have:

    f(a) * f(b) < 0.

    zeroin returns one end point of a small subinterval
    of [a,b] where f changes sign.

    On output we have abs(b - a) / 2 <= reltolx * max(abs(c), 1.0).

    The function f must have the calling sequence

    y=f(x)

    where x and y are floats.

    The calling sequence of f must be

    y=f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y=f(x,*args)

    The three abscissas, a, b, and c, satisfy:

    * f(x) changes sign between a and b, i.e. the zero is in [a, b],
    * b is the closest approximation of the zero, i.e.
    abs(f(b)) <= abs(f(a)).
    * c is the previous or older iterate.

    The next point is chosen from a combination of three methods:

    * bisection,
    * interpolation,
    * a small increment if other methods are unsafe.

    Interpolation step can be performed based on two methods:
    * if a=c, linear interpolation (secant) based on b and c,
    * otherwise inverse quadratic interpolation point based on
    a, b, and c (they are distinct).

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The lower end point
    b : float
        The upper end point
    reltolx : float
        The relative tolerance on x, reltolx > 0.
        Default is twice the machine epsilon
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    verbose : bool
        If True, print intermediate messages.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    c : float
        The approximate root
    history : list of floats
        The approximate roots computed
        during the iterations of the algorithm.

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = zeroin(myFunction, 1.0, 2.0)

    Bibliography
    ------------
    Dekker, T. J. (1969), "Finding a zero by means of successive linear
    interpolation", in Dejon, B.; Henrici, P. (eds.), Constructive Aspects of
    the Fundamental Theorem of Algebra, London: Wiley-Interscience.

    Brent, Richard P. "An algorithm with guaranteed convergence for finding
    a zero of a function." The Computer Journal 14.4 (1971): 422-425.

    Brent, Richard P. Algorithms for minimization without derivatives.
    Englewood Cliffs, N.J.Prentice-Hall, 1973.

    Malcolm, Michael A., Cleve B. Moler, and George Elmer Forsythe.
    Computer methods for mathematical computations. Prentice-Hall, 1977.

    Numerical Computing with Matlab, Cleve Moler, 2008
    """
    # Initialize.
    if reltolx == None:
        reltolx = 2.0 * sys.float_info.epsilon
    fa = f(a, *args)
    fb = f(b, *args)
    if verbose:
        step_name = "Start "
        print("%s. In [%.3e, %.3e]" % (step_name, a, b))
    if np.sign(fa) == np.sign(fb):
        raise ValueError(u"Function must change sign on the interval")
    c = a
    fc = fa
    d = b - c
    e = d
    history = list()
    k = 0
    while fb != 0:
        if np.sign(fa) == np.sign(fb):
            a = c
            fa = fc
            d = b - c
            e = d
        if abs(fa) < abs(fb):
            c = b
            b = a
            a = c
            fc = fb
            fb = fa
            fa = fc
        # Test convergence
        m = 0.5 * (a - b)
        tol = reltolx * abs(b) + abstolx
        if abs(m) <= tol or fb == 0.0:
            break
        # Choose bisection or interpolation
        # Is bisection necessary?
        if abs(e) < tol or abs(fc) <= abs(fb):
            # Bisection
            d = m
            e = m
        else:
            # Interpolation
            if a == c:
                # Linear interpolation (secant)
                s = fb / fc
                p = 2.0 * m * s
                q = 1.0 - s
                step_name = "Secant"
            else:
                # Inverse quadratic interpolation
                q = fc / fa
                r = fb / fa
                s = fb / fc
                p = s * (2.0 * m * q * (q - r) - (b - c) * (r - 1.0))
                q = (q - 1.0) * (r - 1.0) * (s - 1.0)
                step_name = "IQI   "
            # Adjust signs
            if p > 0:
                q = -q
            else:
                p = -p
            # Is interpolated point acceptable
            if 2.0 * p < min(3.0 * m * q - abs(tol * q), abs(e * q)):
                # Interpolation accepted
                e = d
                d = p / q
            else:
                # Otherwise, bisection.
                d = m
                e = m
                step_name = "Bisect"
        # Next point
        c = b
        fc = fb
        if abs(d) > tol:
            b = b + d
        else:
            b = b - np.sign(b - a) * tol
            step_name = "Small "
        history.append(b)
        fb = f(b, *args)
        if verbose:
            print("%s. In [%.3e, %.3e]" % (step_name, a, b))
        k = k + 1
        if k > 100:
            raise ValueError(u"Maximum number of iterations reached!")
    return b, history


def zeroingui(f, a, b, reltolx=None, abstolx=0.0, verbose=False, *args):
    """
    Solves f(x)=0 by a combination of bisection, secant and IQI, and plot.

    Same as zeroin with a plot.

    A the end of each step, the user is asked to click
    on the graph to go to the next step.
    See fzeroplot for the description of the symbols.

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The lower end point
    b : float
        The upper end point
    reltolx : float
        The relative tolerance on x, reltolx > 0.
        Default is twice the machine epsilon
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    verbose : bool
        If True, print intermediate messages.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    c : float
        The approximate root
    history : list of floats
        The approximate roots computed
        during the iterations of the algorithm.

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = zeroingui(myFunction, 1.0, 2.0)

    Bibliography
    ------------
    Numerical Computing with Matlab, Cleve Moler, 2008
    """
    N = 100
    _function_plot(f, a, b, N, *args)
    b, history = zeroin(_compute_and_plot, a, b, reltolx, abstolx, verbose, f, *args)
    return b, history


def test_problems():
    """
    Create a collection of nonlinear equation test problems.

    Each problem is a dictionnary with the following fields:
        * function: function, the test function
        * a : float, the lower bound
        * b : float, the upper bound
        * root : float, the root

    Returns
    -------
    test_collection: list of dict
        Each item in the list is a test problem.

    Examples
    --------
    test_collection = test_problems()
    >>> for problem in test_collection:
    >>>     xs, history = bisection(problem["function"], problem["a"], problem["b"])
    >>>     absolute_error = abs(xs - problem["root"])

    """
    test_collection = []

    # Property: easy, but not exact, i.e. abs(f(root)) is small, but nonzero
    def test_f(x):
        y = x ** 2 - 2.0
        return y

    root = 1.4142135623730950488
    a = 1.0
    b = 2.0
    problem = {"function": test_f, "root": root, "a": a, "b": b, "name": "SQRT2"}
    test_collection.append(problem)

    # Property: Root is a, i.e. the lower bound of the interval
    def test_f(x):
        y = (x - 1.0) * (x + 1.0)
        return y

    root = 1.0
    a = root
    b = 2.0
    problem = {"function": test_f, "root": root, "a": a, "b": b, "name": "ROOT-A"}
    test_collection.append(problem)

    # Property: Root is b i.e. the upper bound of the interval
    # and the slope at a is zero (makes Newton's method fail)
    def test_f(x):
        y = (x - 1.0) * (x + 1.0)
        return y

    root = 1.0
    a = 0.0
    b = root
    problem = {"function": test_f, "root": root, "a": a, "b": b, "name": "ROOT-B"}
    test_collection.append(problem)

    # Ref: Walter Gautschi. Numerical Analysis, Second Edition.
    # Birkhäuser, 2012. p.254
    # Property: Make secant fail.
    def test_f(x):
        y = np.cos(x) * np.cosh(x) - 1.0
        return y

    a = 1.0
    b = 5.0
    root = 4.730040744862704026
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Gautschi1",
    }
    test_collection.append(problem)

    # Brent, Richard P. Algorithms for minimization without derivatives.
    # Englewood Cliffs, N.J.Prentice-Hall, 1973. p.54
    # Property: badly conditioned and exact root is zero, which makes impossible
    # to use a relative error.
    def test_f(x):
        y = x ** 9
        return y

    a = -1.0
    b = 4.0
    root = 0.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Brent1",
    }
    test_collection.append(problem)

    # Brent, Richard P. Algorithms for minimization without derivatives.
    # Englewood Cliffs, N.J.Prentice-Hall, 1973. p.54
    # Property: badly conditioned and exact root is zero, which makes impossible
    # to use a relative error.
    def test_f(x):
        y = x ** 19
        return y

    a = -1.0
    b = 4.0
    root = 0.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Brent2",
    }
    test_collection.append(problem)

    # Ref. A modified Brent’s method for finding zeros of functions
    # Gautam Wilkins, Ming Gu. Numer. Math. (2013) 123:177–188
    def test_f(x):
        y = 3.0 * (x + 1.0) * (x - 5.0) * (x - 1.0)
        return y

    a = -2.0
    b = 0.5
    root = -1.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "WilkinsGu2",
    }
    test_collection.append(problem)

    # Ref. A modified Brent’s method for finding zeros of functions
    # Gautam Wilkins, Ming Gu. Numer. Math. (2013) 123:177–188
    def test_f(x):
        y = np.sin(x) - np.exp(-x)
        return y

    a = 0.0
    b = 1.0
    root = 0.588532743981861077
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "WilkinsGu3",
    }
    test_collection.append(problem)

    # A difficult test case if bracketting is implemented as product.
    # In this case, the evaluation produces an overflow. (M.Baudin)
    def test_f(x):
        y = np.exp(x) - 5.221469689764144e173
        return y

    a = 350.0
    b = 450.0
    root = 400.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Baudin1",
    }
    test_collection.append(problem)

    # A difficult test case if bracketting is implemented as product
    # In this case, the evaluation produces an underflow. (M.Baudin)
    # https://github.com/scipy/scipy/issues/13737
    def test_f(x):
        y = np.exp(x) - 1.9151695967140057e-174
        return y

    a = -450.0
    b = -350.0
    root = -400.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Baudin2",
    }
    test_collection.append(problem)

    # Ref: Burden, R.L., Faires, J.D.: Numerical Analysis. Brooks Cole,
    # Pacific Grove (2005). Example 1, p.32.
    def test_f(x):
        y = x ** 3 + 4 * x - 10.0
        return y

    a = 1.0
    b = 2.0
    root = 1.55677326439421146
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "BurdenFaires1",
    }
    test_collection.append(problem)

    # Ref: A modified Brent’s method for finding zeros of functions
    # Gautam Wilkins, Ming Gu. Numer. Math. (2013) 123:177–188
    # Ref: Burden, R.L., Faires, J.D.: Numerical Analysis. Brooks Cole,
    # Pacific Grove (2005). Example 1, p.34, Exercise Set 2.2, 1.
    def test_f(x):
        y = np.sqrt(x) - np.cos(x)
        return y

    a = 0.0
    b = 1.0
    root = 0.641714370872882658
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "BurdenFaires2",
    }
    test_collection.append(problem)

    # Ref: Burden, R.L., Faires, J.D.: Numerical Analysis. Brooks Cole,
    # Pacific Grove (2005). Example 1, p.34, Exercise Set 2.2, 2.
    def test_f(x):
        y = 3.0 * (x + 1.0) * (x - 0.5) * (x - 1.0)
        return y

    a = -2.0
    b = 0.0
    root = -1.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "BurdenFaires3",
    }
    test_collection.append(problem)

    # Ref: Numerical Computing with Matlab, Cleve Moler, 2008. p.121
    # Property: Newton's method in an infinite loop
    def test_f(x):
        a = 2.0  # This is a free parameter
        if x >= a:
            y = sqrt(x - a)
        else:
            y = -sqrt(a - x)
        return y

    a = 0.0
    b = 4.0
    root = 2.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Moler",
    }
    test_collection.append(problem)

    # Ref.Quarteroni, Alfio, Riccardo Sacco, and Fausto Saleri.
    # Numerical mathematics. Vol. 37. Springer Science & Business Media, 2010.
    # Example 6.4, p.256
    def test_f(x):
        y = np.cos(2.0 * x) ** 2 - x ** 2
        return y

    a = 0.0
    b = 1.5
    root = 0.5149332646611294138
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "QuarteroniSaccoSaleri1",
    }
    test_collection.append(problem)

    # Ref.Quarteroni, Alfio, Riccardo Sacco, and Fausto Saleri.
    # Numerical mathematics. Vol. 37. Springer Science & Business Media, 2010.
    # Example 6.3, p.251
    # Property: this is Legendre polynomial of degree 5.
    def test_f(x):
        y = x * (63.0 * x ** 4 - 70.0 * x ** 2 + 15.0) / 8.0
        return y

    a = 0.6
    b = 1.0
    root = 0.9061798459386639928
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "QuarteroniSaccoSaleri2",
    }
    test_collection.append(problem)

    # Ref. Wilkinson, James H. Two algorithms based on successive
    # linear interpolation. Stanford University, 1967.
    # Example 2.8, p.8
    # Property: The function is almost flat at x=1.0. The secant goes to 0.99.
    def test_f(x):
        y = x * (x - 1.0) ** 5
        return y

    a = -0.5
    b = 0.99
    root = 0.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Wilkinson",
    }
    test_collection.append(problem)

    # Ref: unknown
    # Property: Makes Newton diverge
    def test_f(x):
        y = x * np.exp(-(x ** 2))
        return y

    a = -2.0
    b = 2.0
    root = 0.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Unknown1",
    }
    test_collection.append(problem)

    # Ref: unknown
    # Property: Makes Newton divide by zero
    def test_f(x):
        y = (x - 1.0) ** 3
        return y

    a = 0.0
    b = 2.0
    root = 0.0
    problem = {
        "function": test_f,
        "root": root,
        "a": a,
        "b": b,
        "name": "Unknown2",
    }
    test_collection.append(problem)

    return test_collection


def iqi(f, a, b, c, reltolx=None, abstolx=0.0, verbose=False, *args):
    """
    Solves f(x)=0 by Inverse Quadratic Interpolation.

    This function solves the equation

    f(x)=0

    for the real variable x.

    The root must be bracketed in (a,b), i.e.
    we must have:

    f(a)*f(b)<0.

    On output we have abs(b-a)<=reltolx*max(abs(c),1.).

    The function f must have the calling sequence:

    y=f(x)

    where x and y are floats.

    The calling sequence of f must be:

    y=f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence:

        y=f(x,*args)

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The first point.
    b : float
        The second point.
    c : float
        The third point.
    reltolx : float
        The relative tolerance on x.
        We must have reltolx>0.
        Default is twice the machine epsilon.
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    verbose : bool
        If True, print intermediate messages.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    c : float
        The approximate root.
    history : list of floats
        The approximate roots computed
        of the iterations of the algorithm

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = iqi(myFunction, 1.0, 2.0, 3.0)
    """
    if reltolx == None:
        reltolx = 2.0 * sys.float_info.epsilon
    history = [a, b, c]
    fa = f(a, *args)
    fb = f(b, *args)
    fc = f(c, *args)
    k = 0
    while abs(c - b) > reltolx * abs(c) + abstolx:
        if fa == fb or fa == fc or fb == fc:
            print(u"Warning : Cannot interpolate!")
            print(u"a=", a, ", fa=", fa)
            print(u"b=", b, ", fb=", fb)
            print(u"c=", c, ", fc=", fc)
            break
        x = polynomial_interpolation([fa, fb, fc], [a, b, c], 0.0)
        x = x[0]
        a = b
        fa = fb
        b = c
        fb = fc
        c = x
        fc = f(x, *args)
        history.append(c)
        k = k + 1
        if k > 100:
            print(u"Warning : maximum number of iterations reached!")
            break
    return c, history


def iqigui(f, a, b, c, reltolx=None, abstolx=0.0, verbose=False, *args):
    """
    Solves f(x)=0 by Inverse Quadratic Interpolation
    and plot intermediate points of the iterations the algorithm.

    Parameters
    ----------
    f : function
        The function involved in the non linear equation.
    a : float
        The first point.
    b : float
        The second point.
    c : float
        The third point.
    reltolx : float
        The relative tolerance on x.
        We must have reltolx>0.
        Default is twice the machine epsilon.
    abstolx : float
        The absolute tolerance on x.
        We must have abstolx > 0.
        Default is zero.
    verbose : bool
        If True, print intermediate messages.
    *args : list
        The extra input arguments for f.

    Returns
    -------
    c : float
        The approximate root.
    history : list of floats
        The approximate roots computed
        of the iterations of the algorithm

    Examples
    --------
    >>> def myFunction(x):
    >>>     y = x ** 2 - 2.0
    >>>     return y
    >>>
    >>> xs, history = iqigui(myFunction, 1.0, 2.0, 3.0)
    """
    # Plot the function
    N = 100
    x = np.linspace(min(a, b, c), max(a, b, c), N)
    y = np.zeros((N, 1))
    for i in range(N):
        y[i] = f(x[i], *args)
    pl.plot(x, y, "r-")
    pl.xlabel(u"x")
    pl.ylabel(u"f(x)")
    # Compute
    c, history = iqi(_compute_and_plot, a, b, c, reltolx, abstolx, verbose, f, *args)
    return c, history


if __name__ == "__main__":
    from math import sqrt
    from floats import computeDigits

    def myFunction(x):
        y = x ** 2 - 2.0
        return y

    def myFunctionPrime(x):
        y = 2 * x
        return y

    # Graphique - necessite de fermer la fenetre
    runGraphics = True

    # newton
    xexact = sqrt(2.0)
    xs, history = newton(myFunction, 1.0, myFunctionPrime)
    np.testing.assert_almost_equal(xs, xexact, decimal=4)
    print(u"Approximate Solution:", xs)
    print(u"history:", history)
    print(u"Number of iterations:", len(history))
    print(u"Digits:", computeDigits(xs, xexact))

    # newtongui
    if runGraphics:
        _function_plot(myFunction, 1.0, 2.0, N=100)
        xs, history = newtongui(myFunction, 1.0, myFunctionPrime)
        np.testing.assert_almost_equal(xs, xexact, decimal=4)
        print(u"Approximate Solution:", xs)
        print(u"history:", history)
        print(u"Number of iterations:", len(history))

    # A function with extra-arguments

    def myFPar(x, a, b):
        y = a * x ** 2 - b
        return y

    def myFPrimePar(x, a, b):
        y = 2 * b * x
        return y

    a = 2.0
    b = 3.0
    reltolx = None
    abstolx = 0.0
    verbose = False
    xs, history = newton(myFPar, 1.0, myFPrimePar, reltolx, abstolx, verbose, a, b)
    xexact = np.sqrt(b / a)
    np.testing.assert_almost_equal(xs, xexact, decimal=4)
    print(u"Approximate Solution:", xs)
    print(u"history:", history)
    print(u"Number of iterations:", len(history))

    # bisection
    xs, history = bisection(myFunction, 1.0, 2.0)
    xexact = np.sqrt(2.0)
    np.testing.assert_almost_equal(xs, xexact, decimal=4)
    print(u"Approximate Solution:", xs)
    print(u"history:", history)
    print(u"Number of iterations:", len(history))
    print(u"Digits:", computeDigits(xs, xexact))
    if runGraphics:
        xs, history = bisectiongui(myFunction, 1.0, 2.0)
        np.testing.assert_almost_equal(xs, xexact, decimal=4)

    # secant
    xs, history = secant(myFunction, 1.0, 2.0)
    xexact = np.sqrt(2.0)
    np.testing.assert_almost_equal(xs, xexact, decimal=4)
    print(u"Approximate Solution:", xs)
    print(u"history:", history)
    print(u"Number of iterations:", len(history))
    print(u"Digits:", computeDigits(xs, xexact))
    if runGraphics:
        xs, history = secantgui(myFunction, 1.0, 2.0)
        np.testing.assert_almost_equal(xs, xexact, decimal=4)

    # zeroin
    xs, history = zeroin(myFunction, 1.0, 2.0)
    xexact = np.sqrt(2.0)
    np.testing.assert_almost_equal(xs, xexact, decimal=4)
    print(u"Approximate Solution:", xs)
    print(u"history:", history)
    print(u"Number of iterations:", len(history))
    print(u"Digits:", computeDigits(xs, xexact))
    if runGraphics:
        xs, history = zeroingui(myFunction, 1.0, 2.0)
        np.testing.assert_almost_equal(xs, xexact, decimal=4)
    # Verbose
    xs, history = zeroin(myFunction, 1.0, 2.0, verbose=True)
    xexact = np.sqrt(2.0)
    np.testing.assert_almost_equal(xs, xexact, decimal=4)

    # IQI
    xs, history = iqi(myFunction, 1.0, 2.0, 3.0)
    xexact = np.sqrt(2.0)
    np.testing.assert_almost_equal(xs, xexact, decimal=4)
    print(u"Approximate Solution:", xs)
    print(u"history:", history)
    print(u"Number of iterations:", len(history))
    print(u"Digits:", computeDigits(xs, xexact))
    if runGraphics:
        xs, history = bisectiongui(myFunction, 1.0, 2.0)
        np.testing.assert_almost_equal(xs, xexact, decimal=4)

    # Benchmark
    test_collection = test_problems()
    for problem in test_collection:
        # bisection
        try:
            xs, history = bisection(problem["function"], problem["a"], problem["b"])
            digits = computeDigits(xs, problem["root"])
            abs_error = abs(xs - problem["root"])
        except ValueError:
            digits = 0.0
            abs_error = np.inf
            print("    Bisection fails!")
        print(
            "%-15s, Bisect. Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, len(history), abs_error)
        )
        # secant
        try:
            xs, history = secant(problem["function"], problem["a"], problem["b"])
            digits = computeDigits(xs, problem["root"])
            abs_error = abs(xs - problem["root"])
        except ZeroDivisionError:
            digits = 0.0
            abs_error = np.inf
            print("    Secant fails!")
        except ValueError:
            digits = 0.0
            abs_error = np.inf
            print("    Secant fails!")
        print(
            "%-15s, Secant. Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, len(history), abs_error)
        )
        # zeroin
        try:
            xs, history = zeroin(problem["function"], problem["a"], problem["b"])
            digits = computeDigits(xs, problem["root"])
            abs_error = abs(xs - problem["root"])
        except ValueError:
            digits = 0.0
            abs_error = np.inf
            print("    zeroin fails!")
        print(
            "%-15s, zeroin Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, len(history), abs_error)
        )
        # newton
        def function_derivative(x):
            h = sys.float_info.epsilon ** (1.0 / 3.0)
            f = problem["function"]
            xp = x + h
            xm = x - h
            twice_h = xp - xm
            y = (f(x + h) - f(x - h)) / twice_h
            return y

        try:
            xs, history = newton(problem["function"], problem["a"], function_derivative)
            digits = computeDigits(xs, problem["root"])
            abs_error = abs(xs - problem["root"])
        except ZeroDivisionError:
            digits = 0.0
            abs_error = np.inf
            print("    Newton fails!")
        except ValueError:
            digits = 0.0
            print("    Newton fails!")
        print(
            "%-15s, Newton. Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, len(history), abs_error)
        )
