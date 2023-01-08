# Copyright (C) 2013 - 2023 - Michaël Baudin
"""
Functions for polynomial interpolation.

Reference
---------
Michaël Baudin, "Introduction aux méthodes numériques". 
Dunod. Collection Sciences Sup. (2023)
"""

import numpy as np


def polynomial_interpolation(x, y, u):
    """
    Polynomial interpolation.

    Create a global polynomial of degree d = len(x)
    such that P(x[i]) = y[i] for i = 0, ..., len(x) - 1.

    Computes v[k] = P(u[k]) for k = 0, ..., len(u) - 1 using Lagrange
    formula.

    Parameters
    ----------
    x : numpy.array(n)
        The x observations
    y : numpy.array(n)
        The y observations
    u : numpy.array(m)
        The evaluation points
    v : numpy.array(m)
        The value of the polynomial at point u

    Examples
    --------
    >>> import numpy as np
    >>> x = np.arange(0.0, 6.0)
    >>> y = np.array([5.0, 4.0, 2.0, -2.0, 1.0, 3.0])
    >>> u = np.linspace(-0.25, 5.25, 100)
    >>> v = polynomial_interpolation(x, y, u)

    References
    ----------
    Numerical Computing in Matlab, Cleve Moler, 2008, p.93.

    Dahlquist, Germund, and Åke Björck.
    Numerical methods in scientific computing, volume I.
    Society for Industrial and Applied Mathematics, 2008.
    p.351.

    Quarteroni, Alfio, Riccardo Sacco, and Fausto Saleri.
    Numerical mathematics. Vol. 37. Springer Science & Business Media, 2010.
    p.333 and p.340.
    """
    n = np.size(x)
    v = np.zeros(np.size(u))
    for k in range(n):
        w = np.ones(np.size(u))
        # j=0,...,k-1,k+1,...,n-1
        for j in list(range(k)) + list(range(k + 1, n)):
            # Elementwise product
            w = w * (u - x[j]) / (x[k] - x[j])
        v = v + w * y[k]
    return v


def piecewise_linear(x, y, u):
    """
    Piecewise linear interpolation.

    Create the piecewise linear polynomial L(x)
    with L(x[i]) = y[i] for j = 0, ..., len(x) - 1.

    Computes v[k] = L(u[k]) for k = 0, ..., len(u) - 1.
    Uses first divided differences.

    Parameters
    ----------
    x : numpy.array(n)
        The x observations
    y : numpy.array(n)
        The y observations
    u : numpy.array(m)
        The evaluation points
    v : numpy.array(m)
        The value of the polynomial at point u

    Examples
    --------
    >>> import numpy as np
    >>> x = np.arange(0.0, 6.0)
    >>> y = np.array([5.0, 4.0, 2.0, -2.0, 1.0, 3.0])
    >>> u = np.linspace(-0.25, 5.25, 100)
    >>> v = piecewise_linear(x, y, u)

    References
    ----------
    Numerical Computing in Matlab, Cleve Moler, 2008. p.98.
    """
    delta = np.diff(y) / np.diff(x)
    # Find subinterval indices k so
    # that x[k] <= u < x[k + 1]
    n = np.size(x)
    k = np.zeros(np.size(u), dtype=int)
    for j in range(1, n - 1):
        k[x[j] <= u] = j
    # Evaluate interpolant
    s = u - x[k]
    v = y[k] + s * delta[k]
    return v


def spline_interpolation(x, y, u, siderule="natural"):
    """
    Spline function.

    Creates the piecewise cubic interpolatory
    spline S(x), with S(x[i]) = y[i] for i = 0, ..., len(x) - 1.

    Compute v[k] = S(u[k]) for k = 0, ..., len(u) - 1.

    * if siderule=="not-a-knot" (default),
        uses not-a-knot end conditions.
    * if siderule=="natural",
        uses natural end conditions.

    Parameters
    ----------
    x : numpy.array(n)
        The x observations
    y : numpy.array(n)
        The y observations
    u : numpy.array(m)
        The evaluation points
    siderule : str
        "natural" for a natural spline, or "not-a-knot" for
        a smoother spline

    Returns
    -------
    v : a numpy array with m entries,
        The value of the spline at point u

    Examples
    --------
    >>> import numpy as np
    >>> x = np.arange(0.0, 6.0)
    >>> y = np.array([5.0, 4.0, 2.0, -2.0, 1.0, 3.0])
    >>> u = np.linspace(-0.25, 5.25, 100)
    >>> v = spline_interpolation(x, y, u)

    References
    ----------
    Numerical Computing in Matlab, Cleve Moler, 2008

    Carl De Boor. A practical guide to splines. Springer, 2001.
    """
    #  First derivatives
    h = np.diff(x)
    delta = np.diff(y) / h
    if siderule == "not-a-knot":
        d = spline_slopes_not_a_knot(h, delta)
    else:
        d = spline_slopes_natural(h, delta)
    #  Piecewise polynomial coefficients
    n = np.size(x)
    c = (3 * delta - 2 * d[0 : n - 1] - d[1:n]) / h
    b = (d[0 : n - 1] - 2 * delta + d[1:n]) / h ** 2
    #  Find subinterval indices k
    # so that x(k) <= u < x(k+1)
    k = np.zeros(np.size(u), dtype=int)
    for j in range(1, n - 1):
        k[x[j] <= u] = j
    #  Evaluate spline
    s = u - x[k]
    v = y[k] + s * (d[k] + s * (c[k] + s * b[k]))
    return v


def spline_slopes_not_a_knot(h, delta):
    """
    Slopes for cubic spline interpolation.

    Computes the slopes of the spline:

        d[j]= S'(x[j]) for j = 0, ..., len(u) - 1.

    Not-a-knot end points.
    Usually :

    * h = np.diff(x)
    * delta = np.diff(y)/h

    where x and y are the X and Y observations.

    Parameters
    ----------
    h : np.array(n - 1)
        Differences of x nodes values.
    delta : np.array(n - 1)
        Ratio of the difference of y values to h.

    Returns
    -------
    d : np.array(n)
        Coefficients of the splines.

    References
    ----------
    Numerical Computing in Matlab, Cleve Moler, 2008. p.102

    Carl De Boor. A practical guide to splines. Springer, 2001.

    Dahlquist, Germund, and Åke Björck.
    Numerical methods in scientific computing, volume I.
    Society for Industrial and Applied Mathematics, 2008.
    p.417.
    """
    # Diagonals of tridiagonal system
    n = np.size(h) + 1
    a = np.zeros(n - 1)
    b = np.zeros(n)
    c = np.zeros(n - 1)
    r = np.zeros(n)
    a[0 : n - 2] = h[1 : n - 1]
    a[n - 2] = h[n - 3] + h[n - 2]
    b[0] = h[1]
    b[1 : n - 1] = 2 * (h[1 : n - 1] + h[0 : n - 2])
    b[n - 1] = h[n - 3]
    c[0] = h[0] + h[1]
    c[1 : n - 1] = h[0 : n - 2]
    # Right-hand side
    r[0] = ((h[0] + 2 * c[0]) * h[1] * delta[0] + h[0] ** 2 * delta[1]) / c[0]
    r[1 : n - 1] = 3 * (
        h[1 : n - 1] * delta[0 : n - 2] + h[0 : n - 2] * delta[1 : n - 1]
    )
    r[n - 1] = (
        h[n - 2] ** 2 * delta[n - 3]
        + (2 * a[n - 2] + h[n - 2]) * h[n - 3] * delta[n - 2]
    ) / a[n - 2]
    # Solve tridiagonal linear system
    d = tridiagonal_solve(a, b, c, r)
    return d


def spline_slopes_natural(h, delta):
    """
    Slopes for cubic spline interpolation.

    Computes the slopes of the spline:

        d[j]= S'(x[j]) for j = 0, ..., len(u) - 1.

    Natural zero curvature at end points i.e. S''(x)=0 at end points.

    Usually :

    * h = np.diff(x)
    * delta = np.diff(y) / h

    where x and y are the X and Y observations.

    Parameters
    ----------
    h : np.array(n - 1)
        Differences of x nodes values.
    delta : np.array(n - 1)
        Ratio of the difference of y values to h.

    Returns
    -------
    d : np.array(n)
        Coefficients of the splines.

    References
    ----------
    Numerical Computing in Matlab, Cleve Moler, 2008. p.102

    Carl De Boor. A practical guide to splines. Springer, 2001.

    Dahlquist, Germund, and Åke Björck.
    Numerical methods in scientific computing, volume I.
    Society for Industrial and Applied Mathematics, 2008.
    p.417.
    """
    # Diagonals of tridiagonal system
    n = np.size(h) + 1
    a = np.zeros(n - 1)
    b = np.zeros(n)
    c = np.zeros(n - 1)
    r = np.zeros(n)
    a[0 : n - 2] = h[1 : n - 1]
    a[n - 2] = 1
    b[0] = 2
    b[1 : n - 1] = 2 * (h[1 : n - 1] + h[0 : n - 2])
    b[n - 1] = 2
    c[0] = 1
    c[1 : n - 1] = h[0 : n - 2]
    # Right-hand side
    r[0] = 3 * delta[0]
    r[1 : n - 1] = 3 * (
        h[1 : n - 1] * delta[0 : n - 2] + h[0 : n - 2] * delta[1 : n - 1]
    )
    r[n - 1] = 3 * delta[n - 2]
    # Solve tridiagonal linear system
    d = tridiagonal_solve(a, b, c, r)
    return d


def tridiagonal_solve(a, b, c, d):
    """
    Solve the tridiagonal problem A * x = d.

    Solves the equation A * x = d, where
    A is a tridiagonal n-by-n matrix (a,b,c) and d is the right
    hand side.
    More precisely, the matrix is:

    A =
    [b[0] c[0] 0    ... 0]
    [a[0] b[1] c[1] ... 0]
    [...]
    [0 ... a[n - 3] b[n - 2] c[n - 2]]
    [0 ... 0        a[n - 2] b[n - 1]]

    This algorithm is known as Thomas' algorithm.

    Caution: the function also modifies b and d parameters when solving.

    Parameters
    ----------
    a : numpy.array(n - 1)
        The sub-diagonal.
    b : numpy.array(n)
        The diagonal.
    c : numpy.array(n - 1)
        The super-diagonal

    Returns
    -------
    x : numpy.array(n)
        The solution of A * x = d

    References
    ----------
    Wikipedia : Tridiagonal matrix algorithm

    Kiusalaas, Jaan. Numerical methods in engineering with Python 3.
    Cambridge university press, 2013. p.60

    Higham, Nicholas J. Accuracy and stability of numerical algorithms.
    Society for industrial and applied mathematics, 2002. p.174.
    """
    n = len(d)
    for i in range(n - 1):
        d[i + 1] -= d[i] * a[i] / b[i]
        b[i + 1] -= c[i] * a[i] / b[i]
    for i in list(range(n - 2, -1, -1)):
        d[i] -= d[i + 1] * c[i] / b[i + 1]
    x = d / b
    return x


def compute_Chebyshev_roots(n, a=-1.0, b=1.0):
    """
    Return the list of Chebyshev roots of the polynomial of degree n.

    The roots are sorted in increasing order.

    Parameters
    ----------
    n : int
        The number of roots.
    a : float
        The lower bound.
    b : float
        The upper bound.

    Returns
    -------
    roots : np.array(n) of floats
        The list of roots.
    """
    k = np.array(range(n))
    roots = -np.cos((2 * (k + 1) - 1) * np.pi / (2 * n))
    roots_array = np.array(roots)
    scaled_roots = 0.5 * ((b - a) * roots_array + a + b)
    return scaled_roots


def compute_Chebyshev_polynomial(n, x_scaled):
    """
    Return the value of Chebyshev polynomials of degree n.

    Parameters
    ----------
    n : int
        The polynomial degree.
    x_scaled : float
        The point in [-1.0, 1.0].

    Returns
    -------
    y : float or np.array(n)
        The polynomial value.
    """
    if len(x_scaled[x_scaled < -1.0]) > 0 or len(x_scaled[x_scaled > 1.0] > 0):
        raise ValueError("x must be in [-1, 1]")
    y = np.cos(n * np.arccos(x_scaled))
    return y


def compute_Chebyshev_extremas(n):
    """
    Return the list of Chebyshev extremas of the polynomial of degree n.

    The extremas are sorted in increasing order.

    Parameters
    ----------
    n : int
        The number of roots.

    Returns
    -------
    roots : list(n) of floats
        The list of roots.
    """
    k = np.array(range(n + 1))
    roots = np.cos((k) * np.pi / n)
    return roots


if __name__ == "__main__":
    runGraphics = True
    import pylab as pl

    # Data
    x = np.arange(0.0, 6.0)
    y = np.array([5.0, 4.0, 2.0, -2.0, 1.0, 3.0])

    # Linear Interpolation
    nu = 100
    u = np.linspace(-0.25, 5.25, nu)
    v = piecewise_linear(x, y, u)

    if runGraphics:
        pl.figure()
        pl.plot(x, y, "o")
        pl.plot(u, v, "-")
        pl.title(u"Piecewise linear interpolation")

    # Check 1
    u = np.array(x)
    v = piecewise_linear(x, y, u)
    np.testing.assert_almost_equal(v, y)

    # Check 2
    u = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
    v = piecewise_linear(x, y, u)
    exact = np.array([5.0, 4.5, 4.0, 3.0, 2.0])
    np.testing.assert_almost_equal(v, exact)

    # Polynomial Interpolation: (time, P)
    nu = 100
    u = np.linspace(-0.25, 5.25, nu)
    v = polynomial_interpolation(x, y, u)

    if runGraphics:
        pl.figure()
        pl.plot(x, y, "o")
        pl.plot(u, v, "-")
        pl.title(u"Polynomial interpolation")

    # Spline naturelle
    nu = 100
    u = np.linspace(-0.25, 5.25, nu)
    v = spline_interpolation(x, y, u)

    if runGraphics:
        pl.figure()
        pl.plot(x, y, "o")
        pl.plot(u, v, "-")
        pl.title(u"Spline interpolation : natural")

    # Spline not-a-knot :
    nu = 100
    u = np.linspace(-0.25, 5.25, nu)
    v = spline_interpolation(x, y, u, "not-a-knot")

    if runGraphics:
        pl.figure()
        pl.plot(x, y, "o")
        pl.plot(u, v, "-")
        pl.title(u"Spline interpolation : not-a-knot")

    # Test Thomas' algorithm
    a = [1.0, 1.0, 1.0]
    b = [4.0, 5.0, 6.0, 7.0]
    c = [1.0, 1.0, 1.0]
    matrix = np.diag(a, -1) + np.diag(b) + np.diag(c, 1)
    exact = np.array([1.0, 2.0, 3.0, 4.0])
    d = matrix @ exact
    computed = tridiagonal_solve(a, b, c, d)
    np.testing.assert_array_almost_equal(computed, exact)

    # Accuracy testing : Linear Interpolation
    x = np.linspace(0.0, 1.5, 100)
    y = np.sin(x)
    u = np.linspace(0.5, 1.5, 400)
    exact = np.sin(u)
    computed = piecewise_linear(x, y, u)
    np.testing.assert_array_almost_equal(computed, exact, decimal=4)
    print("Linear interpolation: maximum absolute error")
    print(np.linalg.norm(computed - exact, np.inf))

    # Accuracy testing : Polynomial Interpolation
    x = np.linspace(0.0, 1.5, 7)
    y = np.sin(x)
    u = np.linspace(0.5, 1.5, 10)
    exact = np.sin(u)
    computed = polynomial_interpolation(x, y, u)
    np.testing.assert_array_almost_equal(computed, exact, decimal=4)
    print("Polynomial interpolation: maximum absolute error")
    print(np.linalg.norm(computed - exact, np.inf))

    # Accuracy testing : Spline Interpolation
    x = np.linspace(0.0, 1.5, 100)
    y = np.sin(x)
    u = np.linspace(0.5, 1.5, 400)
    exact = np.sin(u)
    computed = spline_interpolation(x, y, u)
    np.testing.assert_array_almost_equal(computed, exact, decimal=4)
    print("Spline interpolation: maximum absolute error")
    print(np.linalg.norm(computed - exact, np.inf))
