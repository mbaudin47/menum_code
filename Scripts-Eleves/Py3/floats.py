# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
A collection of functions to manage floating point numbers.
"""

import numpy as np
import pylab as pl
from scipy.special import erf


def computeDigits(expected, computed, basis=2.0):
    """
    Compute the number of base-b digits common in expected and computed.

    Compute the number of common base-b digits
    between expected and computed.

    Parameters
    ----------
    expected : float
        The expected value
    computed : float
        The computed value
    basis : float
        The basis
    d : float
        The number of common digits

    Examples
    --------
    >>> exact = 1.0
    >>> computed = 1.0
    >>> d = computeDigits(exact, computed)

    We can se the basis if required.

    >>> exact = 1.0
    >>> computed = 1.0
    >>> basis = 10.0
    >>> d = computeDigits(exact, computed, basis)
    """
    relerr = relativeError(expected, computed)
    dmin = 0
    dmax = -np.log(2 ** (-53)) / np.log(basis)
    if relerr == 0.0:
        d = dmax
    else:
        d = -np.log(relerr) / np.log(basis)
        d = max(dmin, d)
    return d


def relativeError(expected, computed):
    """
    Compute the relative error between expected and computed.

    Compute the relative error
    between expected and computed.
    If expected is zero, the relative error in infinite.

    Parameters
    ----------
    expected : float
        The expected value.
    computed : float
        The computed value.

    Examples
    --------
    >>> exact = 1.0
    >>> computed = 1.0
    >>> relerr = relativeError(exact, computed)
    """
    if (expected == 0.0) & (computed == 0):
        e = 0
    elif expected == 0.0:
        e = float("inf")
    else:
        e = abs(computed - expected) / abs(expected)
    return e


def absoluteError(expected, computed):
    """
    Compute the absolute error between expected and computed.

    Parameters
    ----------
    expected : float
        The expected value.
    computed : float
        The computed value.

    Examples
    --------
    >>> exact = 1.0
    >>> computed = 1.0
    >>> relerr = absoluteError(exact, computed)
    """
    e = abs(computed - expected)
    return e


def computeDigits2Darray(expected, computed, basis=2.0):
    """
    Compute the number of base-b digits common in expected and computed.

    Parameters
    ----------
    expected : np.array
        The expected value
    computed : np.array
        The computed value
    basis : float
        The basis
    d : np.array
        The number of common digits

    Examples
    --------
    >>> expected = np.array([[1.0], [2.0], [3.0]])
    >>> computed = np.array([[1.01], [2.01], [3.01]])
    >>> digits = computeDigits2Darray(expected, computed, basis=2)
    """
    nrows = expected.shape[0]
    ncols = expected.shape[1]
    if computed.shape[0] != nrows:
        print(u"Error ! Number of rows do not match")
        return None
    if computed.shape[1] != ncols:
        print(u"Error ! Number of columns do not match")
        return None
    digits = np.zeros((nrows, ncols))
    for i in range(nrows):
        for j in range(ncols):
            digits[i, j] = computeDigits(expected[i, j], computed[i, j], 10)
    return digits


def fCond(f, x, dx=1.0e-8):
    """
    Compute the condition number of f.

    The condition number is

        c=abs(x*f'(x)/f(x))

    Uses a finite difference of order one to approximate
    f'(x).

    Parameters
    ----------
    f : a function
        The function y=f(x) which condition number is to be computed.
    x : float
        The point where the condition number should be computed.
    dx : float
        The step used for the finite difference

    Returns
    -------
    c : float
        The condition number of f(x)

    Examples
    --------
    >>> x = 2.0
    >>> c = fCond(np.log, x)
    """
    y = f(x)
    yh = f(x + dx)
    c = (abs(yh - y) / abs(y)) / (abs(dx) / x)
    return c


def logCond(x):
    """
    The condition number of log(x).

    Computes the condition number of log(x),
    from the formula :

        c = abs(1/y)

    where y=log(x).

    Parameters
    ----------
    x : float
        The point where the condition number should be computed.

    Returns
    -------
    c : float
        The condition number, c>=0.

    Examples
    --------
    >>> x = 2.0
    >>> c = logCond(x)
    """
    y = np.log(x)
    c = abs(1.0 / y)
    return c


def log1pCond(x):
    """
    The condition number of log(1+x).

    Computes the condition number of log(1+x),
    from the formula :

        c = abs(x/(1+x)/y)

    where y=log(1+x).

    Parameters
    ----------
    x : float
        The point where the condition number should be computed.

    Returns
    -------
    c : float
        The condition number, c>=0.
    """
    y = np.log1p(x)
    c = abs(x / (1.0 + x) / y)
    return c


def expm1Cond(x):
    """
    The condition number of exp(x)-1.

    Computes the condition number of exp(x)-1,
    from the formula :

        c = abs(x*exp(x)/y)

    where y=exp(x)-1.

    Parameters
    ----------
    x : float
        The point where the condition number should be computed.

    Returns
    -------
    c : float
        The condition number, c>=0.

    Examples
    --------
    >>> x = 2.0
    >>> c = expm1Cond(x)
    """
    expx = np.exp(x)
    y = np.expm1(x)
    c = abs(x * expx / y)
    return c


def expCond(x):
    """
    The condition number of exp(x).

    Computes the condition number of exp(x),
    from the formula :

        c = abs(x)

    Parameters
    ----------
    x : float
        The point where the condition number should be computed.

    Returns
    -------
    c : float
        The condition number, c>=0.

    Examples
    --------
    >>> x = 2.0
    >>> c = expCond(x)
    """
    c = abs(x)
    return c


def erfCond(x):
    """
    Retourne le conditionnement de erf.

    Parameters
    ----------
    x : float
        L'entrée.

    Returns
    -------
    c : float
        Le conditionnement.

    Examples
    --------
    >>> x = 2.0
    >>> c = erfCond(x)
    """
    c = 2.0 / np.sqrt(np.pi) * np.abs(x * np.exp(-(x ** 2)) / erf(x))
    return c


def computefloats(
    p=3, emin=-2, emax=3, logscale=False, allpositive=True, withdenormals=False
):
    """
    Computes all floating point numbers in a system.

    Compute all floating point numbers
    from the formula :

        x=M*2**(e-p+1)

    Parameters
    ----------
    p : int
        The precision (default=3).
    emin : int
        The minimum exponent (default=-2)
    emax : int
        The maximum exponent (default=3)
    logscale : bool
        Set to True to enable log2-scale (default=False)
    allpositive : bool
        Set to False to compute negative numbers  (default=True)
    withdenormals : bool
        Set to True to compute subnormal numbers
        (default=False)

    Returns
    -------
    allfloats: list of floats
        The list of required floating point numbers.

    Examples
    --------
    >>> allfloats = computefloats()
    >>> allfloats = computefloats(logscale=True)
    >>> allfloats = computefloats(allpositive=False)
    >>> allfloats = computefloats(withdenormals=True)
    """
    if (not allpositive) & logscale:
        print(u"Error : Cannot enable both logscale" + "and compute negative numbers !")
        return
    # 1. Compute
    allfloats = []
    for e in range(emin, emax + 1):
        for M in range(2 ** (p - 1), 2 ** p):
            x = M * 2 ** (e - p + 1)
            if logscale:
                x = np.log2(x)
            allfloats.append(x)
            if not allpositive:
                allfloats.append(-x)
    if withdenormals:
        for M in range(0, 2 ** (p - 1)):
            x = M * 2 ** (emin - p + 1)
            if logscale:
                x = np.log2(x)
            allfloats.append(x)
            if not allpositive:
                allfloats.append(-x)
    allfloats = sorted(allfloats)
    return allfloats


def floatgui(
    p=3, emin=-2, emax=3, logscale=False, allpositive=True, withdenormals=False
):
    """
    Computes and plot all floating point numbers in a system.

    Compute all floating point numbers from the formula :

        x=M*2**(e-p+1)

    Parameters
    ----------
    p : int
        The precision (default=3)
    emin : int
        The minimum exponent (default=-2)
    emax : int
        The maximum exponent (default=3)
    logscale : bool
        Set to true to enable log2-scale (default=False)
    allpositive : bool
        Set to False to compute negative numbers
        (default=True)
    withdenormals : bool
        Set to True to compute subnormal numbers
        (default=False)

    Returns
    -------
    allfloats: list of floats
        The list of required floating point numbers.

    Examples
    --------
    >>> allfloats = floatgui()
    >>> allfloats = floatgui(logscale=True)
    >>> allfloats = floatgui(allpositive=False)
    >>> allfloats = floatgui(withdenormals=True)
    """
    if (not allpositive) & logscale:
        print(u"Error : Cannot enable both logscale" + "and compute negative numbers !")
        return
    # 1. Compute
    allfloats = computefloats(p, emin, emax, logscale, allpositive, withdenormals)
    # 2. Plot
    _ = pl.figure(figsize=(6, 1))
    if logscale:
        pl.xlabel(u"log2(x)")
    else:
        pl.xlabel(u"x")
    stitle = "Système flottant, p=%d, emin=%d, emax=%d" % (p, emin, emax)
    pl.title(stitle)
    for x in allfloats:
        pl.plot([x, x], [-0.1, 0.1], "-", color="tab:blue", linewidth=0.5)
    xmin = min(allfloats)
    xmax = max(allfloats)
    delta_x = 1.0
    pl.axis([xmin - delta_x, xmax + delta_x, -1, 1])
    frame1 = pl.gca()
    frame1.axes.get_yaxis().set_visible(False)
    return allfloats


if __name__ == "__main__":
    allfloats = computefloats()
    print(allfloats)
    allfloats = computefloats(logscale=True)
    print(allfloats)
    allfloats = computefloats(allpositive=False)
    print(allfloats)
    allfloats = computefloats(withdenormals=True)
    print(allfloats)
    # Graphique - necessite de fermer la fenetre
    runGraphics = False
    if runGraphics:
        allfloats = floatgui()

    exact = 1.0
    computed = 1.0
    basis = 2
    abserr = absoluteError(exact, computed)
    relerr = relativeError(exact, computed)
    d = computeDigits(exact, computed, basis)
    print(u"")
    print(u"computed=", computed, ", exact=", exact)
    print(u"Relative error:", relerr, " Relative error:", abserr)
    print(u"Correct base-", basis, " digits:", d)

    # Vérification de erfCond
    x = 1.0
    cond_approche = fCond(erf, x)
    cond_exact = erfCond(x)
    print(u"Verification erfCond")
    print(u"x=", x)
    print(u"cond_approche=", cond_approche)
    print(u"cond_exact=", cond_exact)
    np.testing.assert_almost_equal(cond_approche, cond_exact, decimal=4)

    # Vérification de logCond
    x = 2.0
    cond_approche = fCond(np.log, x)
    cond_exact = logCond(x)
    print(u"Verification logCond")
    print(u"x=", x)
    print(u"cond_approche=", cond_approche)
    print(u"cond_exact=", cond_exact)
    np.testing.assert_almost_equal(cond_approche, cond_exact, decimal=4)

    # Vérification de log1pCond
    x = 2.0
    cond_approche = fCond(np.log1p, x)
    cond_exact = log1pCond(x)
    print(u"Verification log1pCond")
    print(u"x=", x)
    print(u"cond_approche=", cond_approche)
    print(u"cond_exact=", cond_exact)
    np.testing.assert_almost_equal(cond_approche, cond_exact, decimal=4)

    # Vérification de expm1Cond
    x = 2.0
    cond_approche = fCond(np.expm1, x)
    cond_exact = expm1Cond(x)
    print(u"Verification expm1Cond")
    print(u"x=", x)
    print(u"cond_approche=", cond_approche)
    print(u"cond_exact=", cond_exact)
    np.testing.assert_almost_equal(cond_approche, cond_exact, decimal=4)

    # Verif computeDigits2Darray
    expected = np.array([[1.0], [2.0], [3.0]])
    computed = np.array([[1.01], [2.01], [3.01]])
    digits = computeDigits2Darray(expected, computed, basis=2)
    print("digits=", digits)
    digits_exact = np.array([[2.0], [2.301], [2.477]])
    np.testing.assert_almost_equal(digits, digits_exact, decimal=4)
