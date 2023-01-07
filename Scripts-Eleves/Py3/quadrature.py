# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
A collection of functions for quadrature.
"""

import numpy as np
import pylab as pl


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


def adaptsim(f, a, b, atol=1.0e-6, *args):
    """
    Evaluate definite integral with adaptive quadrature.

    The algorithm is based on adaptive Simpson's quadrature.
    It is a simplified version of (Gander, Gautschi, 2000).

    This function approximates the integral of f(x)
    from a to b to within an absolute tolerance.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    atol : float
        The absolute tolerance on the integral
        atol>0
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).

    Examples
    --------
    >>> def test_f(x):
    >>>     y = 1.0 / (1.0 + x ** 4)
    >>>     return y
    >>>
    >>> integral, fcount = adaptsim(test_f, 0.0, 1.0)

    Bibliography
    ------------
    Walter Gander and Walter Gautschi. "Adaptive quadrature—revisited."
    BIT Numerical Mathematics 40.1 (2000): 84-101.

    Numerical Computing with Matlab, Cleve Moler, 2008
    """
    # Initialization
    c = (a + b) / 2.0
    fa = f(a, *args)
    fc = f(c, *args)
    fb = f(b, *args)
    # Recursive call
    integral, fcount_step = _adaptsim_step(f, a, c, b, atol, fa, fc, fb, *args)
    fcount = fcount_step + 3
    return integral, fcount


def _adaptsim_step(f, a, c, b, atol, fa, fc, fb, *args):
    """
    Recursive subfunction used by adaptsim.
    """
    h = b - a
    d = (a + c) / 2
    e = (c + b) / 2
    fd = f(d, *args)
    fe = f(e, *args)
    S = h / 6.0 * (fa + 4.0 * fc + fb)
    S2 = h / 12.0 * (fa + 4.0 * fd + 2.0 * fc + 4.0 * fe + fb)
    if abs(S2 - S) <= atol:
        integral = S2 + (S2 - S) / 15.0
        fcount = 2
    else:
        integral_a, fcount_a = _adaptsim_step(f, a, d, c, atol, fa, fd, fc, *args)
        integral_b, fcount_b = _adaptsim_step(f, c, e, b, atol, fc, fe, fb, *args)
        integral = integral_a + integral_b
        fcount = fcount_a + fcount_b + 2
    return integral, fcount


def adaptsim_gui(f, a, b, atol=1.0e-6, *args):
    """
    Evaluate definite integral with adaptive quadrature.

    The algorithm is based on adaptive Simpson's quadrature.
    It is a simplified version of (Gander, Gautschi, 2000).

    Plot the function, and the evaluation points.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    atol : float
        The absolute tolerance on the integral
        atol>0
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).

    Examples
    --------
    >>> def test_f(x):
    >>>     y = 1.0 / (1.0 + x ** 4)
    >>>     return y
    >>>
    >>> integral, fcount = adaptsim_gui(test_f, 0.0, 1.0)

    Bibliography
    ------------
    Walter Gander and Walter Gautschi. "Adaptive quadrature—revisited."
    BIT Numerical Mathematics 40.1 (2000): 84-101.

    Numerical Computing with Matlab, Cleve Moler, 2008
    """
    # Create initial plot
    n = 100
    x = np.linspace(a, b, n)
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    pl.figure()
    pl.plot(x, y, "-")
    pl.xlabel(u"x")
    pl.ylabel(u"y")
    # Quadrature with plot
    integral, fcount = adaptsim(_compute_and_plot, a, b, atol, f, *args)
    # Finalize plot
    pl.title(u"integral=%.4f, Fcount:%d" % (integral, fcount))
    return integral, fcount


def midpoint_rule(f, a, b, *args):
    """
    Evaluate definite integral with midpoint rule.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).

    Examples
    --------
    >>> def test_f(x):
    >>>     y = 1.0 / (1.0 + x ** 4)
    >>>     return y
    >>>
    >>> integral, fcount = midpoint_rule(test_f, 0.0, 1.0)
    """
    c = (a + b) / 2.0
    fc = f(c, *args)
    fcount = 1
    h = b - a
    integral = h * fc
    return integral, fcount


def trapezoidal_rule(f, a, b, *args):
    """
    Evaluate definite integral with trapezoidal rule.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).
    """
    fa = f(a, *args)
    fb = f(b, *args)
    fcount = 2
    h = b - a
    integral = h * (fa + fb) / 2.0
    return integral, fcount


def simpson_rule(f, a, b, *args):
    """
    Evaluate definite integral with Simpson's rule.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).
    """
    c = (a + b) / 2.0
    fa = f(a, *args)
    fb = f(b, *args)
    fc = f(c, *args)
    fcount = 3
    h = b - a
    integral = h * (fa + 4 * fc + fb) / 6.0
    return integral, fcount


def compositesimpson_rule(f, a, b, *args):
    """
    Evaluate definite integral with composite Simpson's rule.

    Uses 2 sub-intervals.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).
    """
    c = (a + b) / 2.0
    integral1, fcount1 = simpson_rule(f, a, c, *args)
    integral2, fcount2 = simpson_rule(f, c, b, *args)
    integral = integral1 + integral2
    fcount = fcount1 + fcount2
    return integral, fcount


def boole_rule(f, a, b, *args):
    """
    Evaluate definite integral with Boole's rule.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).
    """
    integral1, fcount1 = simpson_rule(f, a, b, *args)
    integral2, fcount2 = compositesimpson_rule(f, a, b, *args)
    integral = integral2 + (integral2 - integral1) / 15
    fcount = fcount1 + fcount2
    return integral, fcount


def composite_midpoint(f, a, b, n, *args):
    """
    Evaluate definite integral with composite midpoint rule.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    n : int
        The number of nodes
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).
    """
    if type(n) is not int:
        raise ValueError("The number %s of subintervals is not an integer" % (n))
    h = (b - a) / (n - 1)
    x = [a + i * h for i in range(n)]
    y_sum = 0.0
    for i in range(n - 1):
        x_midpoint = (x[i] + x[i + 1]) / 2.0
        yi = f(x_midpoint, *args)
        y_sum += yi
    integral = y_sum * h
    fcount = n - 1
    return integral, fcount


def composite_trapezoidal(f, a, b, n, *args):
    """
    Evaluate definite integral with composite trapezoidal rule.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    n : int
        The number of nodes
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).
    """
    if type(n) is not int:
        raise ValueError("The number %s of subintervals is not an integer" % (n))
    h = (b - a) / (n - 1)
    x = [a + i * h for i in range(n)]
    y_sum = f(x[0], *args)
    for i in range(1, n - 1):
        y_sum += 2.0 * f(x[i], *args)
    y_sum += f(x[n - 1], *args)
    integral = y_sum * h / 2.0
    fcount = n
    return integral, fcount


def composite_simpson(f, a, b, n, *args):
    """
    Evaluate definite integral with composite Simpson rule.

    The first argument, f, is a function that defines f(x).
    The calling sequence of f must be

        y = f(x)

    If extra-arguments are provided in the args input
    argument, the function f is supposed to have the calling
    sequence

        y = f(x,*args)

    Parameters
    ----------
    f : function
        The function to integrate
    a : float
        The lower end of the interval
    b : float
        The upper end of the interval
    n : int
        The number of nodes
    args : list
        The extra-arguments for f

    Returns
    -------
    integral : float
        The approximate value of the integral.
    fcount : int
        The number of evaluations of f(x).
    """
    integral_Mc, fcount_Mc = composite_midpoint(f, a, b, n, *args)
    integral_Tc, fcount_Tc = composite_trapezoidal(f, a, b, n, *args)
    fcount = fcount_Mc + fcount_Tc
    integral = 2.0 * integral_Mc / 3.0 + integral_Tc / 3.0
    return integral, fcount


def test_problems():
    """
    Create a collection of integration test problems.

    Each problem is a dictionnary with the following fields:
        * function: function, the test function
        * a : float, the lower bound
        * b : float, the upper bound
        * integral : float, the integral

    Returns
    -------
    test_collection: list of dict
        Each item in the list is a test problem.

    Examples
    --------
    test_collection = test_problems()
    >>> for problem in test_collection:
    >>>     integral, fcount = adaptsim(problem["function"], problem["a"], problem["b"])
    >>>     absolute_error = abs(integral - problem["integral"])

    """
    test_collection = []

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.43
    # Property: very easy
    def test_f(x):
        y = x
        return y

    a = 0.0
    b = 1.0
    integral = 0.5
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "X"}
    test_collection.append(problem)

    # Property : integrates exactly with a rule with exact degree 2
    def test_f(x):
        y = x ** 2
        return y

    a = 0.0
    b = 1.0
    integral = 0.33333333333333333  # 1 / 3
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "X^2"}
    test_collection.append(problem)

    # Property : integrates exactly with a rule with exact degree 3
    def test_f(x):
        y = x ** 3
        return y

    a = 0.0
    b = 1.0
    integral = 0.25  # 1 / 4
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "X^3"}
    test_collection.append(problem)

    # Property : integrates exactly with a rule with exact degree 5
    def test_f(x):
        y = x ** 5
        return y

    a = 0.0
    b = 1.0
    integral = 0.166666666666666667  # 1 / 6
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "X^5"}
    test_collection.append(problem)

    # Property : integrates exactly with a rule with exact degree 7
    def test_f(x):
        y = x ** 7
        return y

    a = 0.0
    b = 1.0
    integral = 0.125  # 1 / 8
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "X^7"}
    test_collection.append(problem)

    # Property : integrates exactly with a rule with exact degree 9
    def test_f(x):
        y = x ** 9
        return y

    a = 0.0
    b = 1.0
    integral = 0.1
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "X^9"}
    test_collection.append(problem)

    # Property: easy
    # Ref: Numerical Computing with Matlab, Cleve Moler, 2008, p.171
    def test_f(x):
        y = 1.0 / sqrt(1.0 + x ** 4)
        return y

    a = 0.0
    b = 1.0
    integral = 0.927037338650685959
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "InvSqrt",
    }
    test_collection.append(problem)

    # Property: easy
    def test_f(t):
        z = 8.0 / 3.0
        w = 10.0 / 3.0
        y = t ** (z - 1) * (1.0 - t) ** (w - 1)
        return y

    a = 0.0
    b = 1.0
    integral = 0.0348329096012058297782
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "Beta"}
    test_collection.append(problem)

    # Property: a division by zero may occur at x=0
    # Trick: consider x = 0 separately
    def test_f(x):
        use_trick = False
        if use_trick:
            if x == 0.0:
                y = 1.0
            else:
                y = sin(x) / x
        else:
            y = sin(x) / x
        return y

    a = 0.0
    b = pi
    integral = 1.85193705198246617036
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "Sinc"}
    test_collection.append(problem)

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.43
    # Property: very easy
    def test_f(x):
        y = sin(pi * x)
        return y

    a = 0.0
    b = 1.0
    integral = 0.6366197723675813  # 2 / pi
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "SinPi",
    }
    test_collection.append(problem)

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.46
    # Property: very easy
    def test_f(x):
        y = 1.0 / (1.0 + x)
        return y

    a = 0.0
    b = 1.0
    integral = 0.69314718055994531  # log(2)
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Inv1PX",
    }
    test_collection.append(problem)

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.46
    # Property: false singularity in x=0
    # Trick: consider x = 0 separately
    def test_f(x):
        use_trick = False
        if use_trick:
            if x == 0.0:
                y = 1.0
            else:
                y = x / np.expm1(x)
        else:
            y = x / np.expm1(x)
        return y

    a = 0.0
    b = 1.0
    integral = 0.777504634112248276
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "XDivExpm1",
    }
    test_collection.append(problem)

    # Property: a relative error stopping rule fail
    # The function has no bounded derivative in [0, 1].
    # Ref.: Walter Gander and Walter Gautschi. "Adaptive quadrature—revisited."
    # BIT Numerical Mathematics 40.1 (2000): 84-101.
    # p.4
    def test_f(x):
        y = np.sqrt(x)
        return y

    a = 0.0
    b = 1.0
    integral = 0.66666666666666666
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Pow1/2",
    }
    test_collection.append(problem)

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.46
    # Property: no third derivative at x=0
    def test_f(x):
        y = x ** 1.5
        return y

    a = 0.0
    b = 1.0
    integral = 0.4
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Pow3/2",
    }
    test_collection.append(problem)

    # Property: not derivable at x=1 (corner), non continuous at x = 3.0
    # Ref.: Walter Gander and Walter Gautschi. "Adaptive quadrature—revisited."
    # BIT Numerical Mathematics 40.1 (2000): 84-101.
    # p.7
    def test_f(x):
        if x < 1.0:
            y = x + 1.0
        elif x < 3.0:
            y = 3.0 - x
        else:
            y = 2.0
        return y

    a = 0.0
    b = 5.0
    integral = 7.5
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Discontinuous",
    }
    test_collection.append(problem)

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.2 and p.325
    # Property : easy
    def test_f(x):
        y = 1.0 / (1.0 + x ** 4)
        return y

    a = 0.0
    b = 1.0
    integral = 0.8669729873399110
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "InvPow4",
    }
    test_collection.append(problem)

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.325
    # Property : easy
    def test_f(x):
        y = 1.0 / (1.0 + np.exp(x))
        return y

    a = 0.0
    b = 1.0
    integral = 0.37988549304172248
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "InvExp",
    }
    test_collection.append(problem)

    # Ref.:Davis, Philip J., and Philip Rabinowitz.
    # "Methods of numerical integration." (1975). p.325
    # Property : oscillates 5 times in the interval
    def test_f(x):
        y = 2.0 / (2.0 + np.sin(10.0 * np.pi * x))
        return y

    a = 0.0
    b = 1.0
    integral = 1.15470053837925153
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "2InvSin",
    }
    test_collection.append(problem)

    # Property: not a polynomial
    def test_f(x):
        y = np.sin(2.5 * x) ** 2
        return y

    a = 0.0
    b = 1.0
    integral = 0.59589242746631385  # (5 - sin(5)) / 10
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "SquareSin",
    }
    test_collection.append(problem)

    # Property: a needle in a haystack, i.e. a spiky function
    # Ref.:Baudin, 2021
    def test_f(x):
        a = 10000.0
        b = 0.5
        y = 1.0 / (1.0 + a * (x - b) ** 2)
        return y

    a = -1.0
    b = 1.0
    integral = 0.031015979856434922  # 1/50 tan^(-1)(50)
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Needle",
    }
    test_collection.append(problem)

    # Property: exact integral is 1, but interval is very large.
    # Ref.: Gauss
    def test_f(x):
        y = np.exp(-0.5 * x ** 2) / np.sqrt(2.0 * np.pi)
        return y

    a = -40.0
    b = 40.0
    integral = 1.0
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Gauss",
    }
    test_collection.append(problem)

    # Property: integral is zero, ill-conditionned
    def test_f(x):
        y = np.sin(x)
        return y

    a = 0.0
    b = 2.0 * np.pi
    integral = 0.0
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "Sin0"}
    test_collection.append(problem)

    # Property: easy, exact integral is 1, but interval is small.
    # Ref.: Richard, L. "Burden and J. Douglas Faires.
    # Numerical analysis. Brooks." Cole Publishing Company, Pacific Grove,
    # California 93950 (1997): 78.
    # p.142
    def test_f(x):
        y = np.sin(x)
        return y

    a = 0.0
    b = np.pi / 2.0
    integral = 1.0
    problem = {"function": test_f, "integral": integral, "a": a, "b": b, "name": "Sin1"}
    test_collection.append(problem)

    # Property: easy, but has large curvature at 1.25, and moderate at x=2.0
    # Ref.: Richard, L. "Burden and J. Douglas Faires.
    # Numerical analysis. Brooks." Cole Publishing Company, Pacific Grove,
    # California 93950 (1997): 78.
    # p.143
    def test_f(x):
        y = (100.0 / x ** 2) * np.sin(10.0 / x)
        return y

    a = 1.0
    b = 3.0
    integral = -1.42602475634626612
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "FairesBurden",
    }
    test_collection.append(problem)

    # Ref.: Espelid, T.O. Doubly Adaptive Quadrature Routines Based on
    # Newton–Cotes Rules. BIT Numerical Mathematics 43, 319–337 (2003).
    # https://doi.org/10.1023/A:1026087703168
    # p.334, problem 2.
    # Property: discontinuous
    def test_f(x):
        if x > 0.3:
            y = 1.0
        else:
            y = 0.0
        return y

    a = 0.0
    b = 1.0
    integral = 0.7
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Espelid2",
    }
    test_collection.append(problem)

    # Ref.: Espelid, T.O. Doubly Adaptive Quadrature Routines Based on
    # Newton–Cotes Rules. BIT Numerical Mathematics 43, 319–337 (2003).
    # https://doi.org/10.1023/A:1026087703168
    # p.334, problem 4.
    # Property: TODO
    def test_f(x):
        y = 23.0 / 25.0 * np.cosh(x) - np.cos(x)
        return y

    a = -1.0
    b = 1.0
    integral = 0.47942822668880167
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Espelid4",
    }
    test_collection.append(problem)

    # Ref.: Espelid, T.O. Doubly Adaptive Quadrature Routines Based on
    # Newton–Cotes Rules. BIT Numerical Mathematics 43, 319–337 (2003).
    # https://doi.org/10.1023/A:1026087703168
    # p.334, problem 5.
    # Property: hard with symbolic computation
    def test_f(x):
        y = 1.0 / (x ** 4 + x ** 2 + 0.9)
        return y

    a = -1.0
    b = 1.0
    # Symbolic calculation failed to produce more digits
    integral = 1.58223
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Espelid5",
    }
    test_collection.append(problem)

    # Ref.: Espelid, T.O. Doubly Adaptive Quadrature Routines Based on
    # Newton–Cotes Rules. BIT Numerical Mathematics 43, 319–337 (2003).
    # https://doi.org/10.1023/A:1026087703168
    # p.334, problem 7.
    # Property: hard, adaptive quadrature fails on division by zero.
    def test_f(x):
        y = 1.0 / np.sqrt(x)
        return y

    a = 0.0
    b = 1.0
    integral = 2.0
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Espelid7",
    }
    test_collection.append(problem)

    # Ref.: Espelid, T.O. Doubly Adaptive Quadrature Routines Based on
    # Newton–Cotes Rules. BIT Numerical Mathematics 43, 319–337 (2003).
    # https://doi.org/10.1023/A:1026087703168
    # p.334, problem 13.
    # Property: hard, highly oscillatory
    def test_f(x):
        y = np.sin(100.0 * np.pi * x) / (np.pi * x)
        return y

    a = 0.1
    b = 1.0
    integral = 0.0090986375391668429
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Espelid13",
    }
    test_collection.append(problem)

    # Ref.: Espelid, T.O. Doubly Adaptive Quadrature Routines Based on
    # Newton–Cotes Rules. BIT Numerical Mathematics 43, 319–337 (2003).
    # https://doi.org/10.1023/A:1026087703168
    # p.334, problem 14.
    # Property: fast decrease, the mass is very near 0
    def test_f(x):
        y = np.sqrt(5.0) * np.exp(-50.0 * np.pi * x ** 2)
        return y

    a = 0.0
    b = 10.0
    integral = 0.158113883008418967  # erf(50 sqrt(2 π))/(2 sqrt(10))
    problem = {
        "function": test_f,
        "integral": integral,
        "a": a,
        "b": b,
        "name": "Espelid14",
    }
    test_collection.append(problem)
    return test_collection


if __name__ == "__main__":
    from math import pi
    from floats import computeDigits
    from numpy import nextafter, sqrt, sin

    def myfunB(x):
        y = 1.0 / (1.0 + x ** 4)
        return y

    expected = 0.8669729873399110

    # adaptsim
    integral, fcount = adaptsim(myfunB, 0.0, 1.0)
    np.testing.assert_almost_equal(integral, expected)

    # composite_midpoint
    integral, fcount = composite_midpoint(myfunB, 0.0, 1.0, 10000)
    np.testing.assert_almost_equal(integral, expected)

    # composite_trapezoidal
    integral, fcount = composite_trapezoidal(myfunB, 0.0, 1.0, 10000)
    np.testing.assert_almost_equal(integral, expected)

    # composite_simpson
    integral, fcount = composite_midpoint(myfunB, 0.0, 1.0, 10000)
    np.testing.assert_almost_equal(integral, expected)

    runGraphics = True
    if runGraphics:
        integral, fcount = adaptsim_gui(myfunB, 0.0, 1.0)

    #
    print(u"Singularity: Solution 1 is to change a")

    def mysinc(x):
        y = sin(x) / x
        return y

    afterzero = nextafter(0.0, pi)
    print(u"afterzero=", afterzero)
    integral, fcount = adaptsim(mysinc, afterzero, pi)
    expected = 1.85193705198246617036
    np.testing.assert_almost_equal(integral, expected)

    #
    print(u"Solution 2 : change f")

    def mysincbis(x):
        if x == 0.0:
            y = 1.0
        else:
            y = np.sin(x) / x
        return y

    # integral from 0 to pi sin(x)/x
    integral, fcount = adaptsim(mysincbis, 0.0, pi)
    expected = 1.85193705198246617036
    np.testing.assert_almost_equal(integral, expected)
    #
    integral, fcount = composite_midpoint(mysincbis, 0.0, pi, 10000)
    np.testing.assert_almost_equal(integral, expected)
    #
    integral, fcount = composite_trapezoidal(mysincbis, 0.0, pi, 10000)
    np.testing.assert_almost_equal(integral, expected)

    #
    print(u"Extra args")

    def betafun(t, z, w):
        y = t ** (z - 1) * (1.0 - t) ** (w - 1)
        return y

    z = 8.0 / 3.0
    w = 10.0 / 3.0
    atol = 1.0e-15
    integral, fcount = adaptsim(betafun, 0.0, 1.0, atol, z, w)
    expected = 0.0348329096012058297782
    np.testing.assert_almost_equal(integral, expected)

    # Benchmark
    test_collection = test_problems()
    for problem in test_collection:
        # adaptive quadrature
        try:
            integral, fcount = adaptsim(problem["function"], problem["a"], problem["b"])
            digits = computeDigits(integral, problem["integral"], 10.0)
            abs_error = abs(integral - problem["integral"])
        except RecursionError:
            digits = 0.0
            abs_error = np.inf
            print("    adaptsim fails!")
        print(
            "%-15s, Ad.Quad. Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, fcount, abs_error)
        )
        # Composite Midpoint
        integral, fcount = composite_midpoint(
            problem["function"], problem["a"], problem["b"], 10000
        )
        digits = computeDigits(integral, problem["integral"], 10.0)
        abs_error = abs(integral - problem["integral"])
        print(
            "%-15s, Comp. M. Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, fcount, abs_error)
        )
        # Composite Trapezoidal
        integral, fcount = composite_trapezoidal(
            problem["function"], problem["a"], problem["b"], 10000
        )
        digits = computeDigits(integral, problem["integral"], 10.0)
        abs_error = abs(integral - problem["integral"])
        print(
            "%-15s, Comp. T. Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, fcount, abs_error)
        )
        # Composite Simpson
        integral, fcount = composite_simpson(
            problem["function"], problem["a"], problem["b"], 10000
        )
        digits = computeDigits(integral, problem["integral"], 10.0)
        abs_error = abs(integral - problem["integral"])
        print(
            "%-15s, Comp. S. Digits: %.2f, Iter: %d, A.E.=%.3e"
            % (problem["name"], digits, fcount, abs_error)
        )
