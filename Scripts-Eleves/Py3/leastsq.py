# Copyright (C) 2013 - 2021 - Michaël Baudin

"""
A collection of functions for least squares.
"""
import numpy as np


def polynomial_fit_normal_equations(t, y, n):
    """
    Polynomial curve fitting from normal equations.

    Finds the coefficients of
    a polynomial p(x) of degree n that fits the data,

    p(t[i]) ~ y[i],

    in a least-squares sense.

    These coefficients are ordered with powers
    in decreasing order:

    p(t) = bet[0] * t^n + bet[1] * t^{n-1} + ... + bet[n - 1] * t + bet[n].

    Parameters
    ----------
    t : np.array(m)
        The x observations.
    y : np.array(m)
        The y observations
    n : int, n>=0,
        The degree of the polynomial
    bet : np.array(n + 1)
        The coefficients of the polynomial

    Examples
    --------
    >>> import numpy as np
    >>> t = np.array([1971.0, 1980.0, 1990.0, 2000.0, 2010.0, 2019.0])
    >>> y = np.array([0.3104, 0.6484, 0.9832, 1.562, 2.245, 4.233])
    >>> # Scale data
    >>> s = (t - min(t)) / (max(t) - min(t))
    >>> m = np.size(y)
    >>> bet = polynomial_fit_normal_equations(s, y, 3)

    References
    ----------
    Numerical Computing with Matlab, Cleve Moler, 2008. p.145.

    Allaire, Grégoire, et al. Numerical linear algebra. Vol. 55.
    New York: Springer, 2008. p.131.

    Björck, Åke. Numerical methods for least squares problems.
    Society for Industrial and Applied Mathematics, 1996.
    p.7.
    """
    X = np.vander(t, n + 1)
    A = X.T @ X
    b = X.T @ y
    bet = np.linalg.solve(A, b)
    return bet


def polynomial_value(bet, u):
    """
    Polynomial evaluation.

    Computes the value of the polynomial at point u defined by its
    coefficients bet.

    These coefficients are ordered with powers in
    decreasing order:

    p(t) = bet[0] * t^n + bet[1] * t^{n-1} + ... + bet[n - 1] * t + bet[n].

    Parameters
    ----------
    bet : np.array(n + 1)
        The coefficients of the polynomial in decreasing power order.
    u : np.array(m)
        The points where to evaluate the polynomial
    v : np.array(m)
        The value of the polynomial at u

    Examples
    --------
    >>> import numpy as np
    >>> bet = np.array([7.961, -7.624, 3.565, 0.2755])
    >>> u = np.linspace(1970.0, 2020.0, 100)
    >>> v = polynomial_value(bet, u)
    """
    n = np.size(bet)
    X = np.vander(u, n)
    v = np.dot(X, bet)
    return v


def polynomial_fit(t, y, n):
    """
    Polynomial curve fitting.

    Computes the coefficients of a
    polynomial p(x) of degree n that fits the data:

    p(t[i]) ~ y[i]

    in a least-squares sense.

    These coefficients are ordered with powers in
    decreasing order:

    p(t) = bet[0] * t^n + bet[1] * t^{n-1} + ... + bet[n - 1] * t + bet[n].

    Uses the QR decomposition.

    Parameters
    ----------
    t : np.array(m)
        The x observations
    y : np.array(m)
        The y observations
    n : int, n>=0,
        The degree of the polynomial
    bet : np.array(n + 1)
        The coefficients of the polynomial

    Examples
    --------
    >>> import numpy as np
    >>> t = np.array([1971.0, 1980.0, 1990.0, 2000.0, 2010.0, 2019.0])
    >>> y = np.array([0.3104, 0.6484, 0.9832, 1.562, 2.245, 4.233])
    >>> # Scale data
    >>> s = (t - min(t)) / (max(t) - min(t))
    >>> m = np.size(y)
    >>> bet = polynomial_fit(s, y, 3)

    References
    ----------
    Numerical Computing with Matlab, Cleve Moler, 2008. p.147.

    Allaire, Grégoire, et al. Numerical linear algebra. Vol. 55.
    New York: Springer, 2008. p.132

    Björck, Åke. Numerical methods for least squares problems.
    Society for Industrial and Applied Mathematics, 1996.
    p.21.
    """
    X = np.vander(t, n + 1)
    Q, R = np.linalg.qr(X)
    z = np.dot(np.transpose(Q), y)
    bet = np.linalg.solve(R, z)
    return bet


if __name__ == "__main__":
    runGraphics = False
    import pylab as pl

    # Source:
    # Air transport, passengers carried
    # International Civil Aviation Organization, Civil Aviation Statistics
    # of the World and ICAO staff estimates
    # The World Bank. IS.AIR.PSGR. 2020.
    t = np.array(
        [
            1971.0,
            1975.0,
            1980.0,
            1985.0,
            1990.0,
            1995.0,
            2000.0,
            2005.0,
            2010.0,
            2015.0,
            2019.0,
        ]
    )
    y = np.array(
        [
            0.3104,
            0.4211,
            0.6484,
            0.7324,
            0.9832,
            1.233,
            1.562,
            1.889,
            2.245,
            3.227,
            4.233,
        ]
    )
    # Scale data
    s = (t - min(t)) / (max(t) - min(t))
    m = np.size(y)
    bet = polynomial_fit_normal_equations(s, y, 3)
    print(u"bet=", bet)
    beta_reference = np.array([6.906, -6.222, 3.208, 0.2450])
    np.testing.assert_allclose(bet, beta_reference, 1.0e-3)

    # Evaluate and plot
    u = np.linspace(1970.0, 2020.0, 100)
    v = polynomial_value(bet, u)

    # Make a plot
    if runGraphics:
        pl.figure()
        pl.plot(t, y, "o")
        pl.plot(u, v, "-")
        pl.xlabel(u"Year")
        pl.ylabel(u"Billions")
        pl.title(u"Polynomial least squares (Normal Equations)")

    # Degree 3 with polynomial_fit
    bet = polynomial_fit(s, y, 3)
    print(u"bet=", bet)
    np.testing.assert_allclose(bet, beta_reference, 1.0e-3)

    # polynomial_value
    u = np.array([1990.0, 2000.0, 2010.0])
    u_scaled = (u - min(t)) / (max(t) - min(t))
    y = polynomial_value(bet, u_scaled)
    print(u"y=", y)
    y_reference = np.array([0.9683, 1.435, 2.448])
    np.testing.assert_allclose(y, y_reference, 1.0e-3)
