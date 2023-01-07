# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
A collection of functions for linear algebra.
"""
from numpy import zeros, argmax, tril, triu, array, eye, outer


def backward_substitution(U, b):
    """
    Solves U @ x = b, where U is upper triangular.

    Uses backward substitution.

    Parameters
    ----------
    U : np.array((n, n))
        An upper triangular matrix
    b : np.array(n)
        The right hand side

    Returns
    -------
    x : np.array(n)
        The solution

    Example
    -------
    >>> from linalg import backward_substitution
    >>> from numpy import array
    >>> U=array([[1.0, 2.0, 3.0, 4.0],
    >>>          [0.0, 5.0, 6.0, 7.0],
    >>>          [0.0, 0.0, 8.0, 9.0],
    >>>          [0.0, 0.0, 0.0, 10.0]])
    >>> e = array([1.0, 2.0, 3.0, 4.0])
    >>> b = U @ e
    >>> x = backward_substitution(U, b)

    Bibliography
    ------------
    Numerical Computing with Matlab, Cleve Moler, 2008
    """
    n = U.shape[0]
    x = zeros((n))
    for k in range(n - 1, -1, -1):
        x[k] = b[k] / U[k, k]
        b[0:k] = b[0:k] - U[0:k, k] * x[k]
    return x


def forward_elimination(L, b):
    """
    Solves L @ x = b, where L is lower triangular.

    Uses forward elimination.

    Parameters
    ----------
    U : np.array((n, n))
        A lower triangular matrix
    b : np.array(n)
        The right hand side

    Returns
    -------
    x : np.array(n)
        The solution

    Example
    -------
    >>> from linalg import forward_elimination
    >>> from numpy import array
    >>> L = array([[1.0, 0.0, 0.0, 0.0],
    >>>            [2.0, 3.0, 0.0, 0.0],
    >>>            [4.0, 5.0, 6.0, 0.0],
    >>>            [7.0, 8.0, 9.0, 10.0]])
    >>> e = array([1.0, 2.0, 3.0, 4.0])
    >>> b = L @ e
    >>> x = forward_elimination(L, b)

    Bibliography
    ------------
    Numerical Computing with Matlab, Cleve Moler, 2008
    """
    n = L.shape[0]
    x = zeros((n))
    for k in range(n):
        x[k] = b[k] / L[k, k]
        b[k + 1 : n] = b[k + 1 : n] - L[k + 1 : n, k] * x[k]
    return x


def lu_decomposition(A):
    """
    Computes the LU decomposition of A, with row permutation.

    This function produces a unit lower triangular matrix L,
    an upper triangular matrix U, and a permutation vector p, such that

    L @ U = A[p, :]

    Parameters
    ----------
    A : np.array((n, n))
        The matrix.

    Returns
    -------
    L : np.array((n, n))
        A lower triangular matrix.
    U : np.array((n, n))
        An upper triangular matrix.
    p : list of int
        A permutation vector representing the permutation of rows of A.

    Example
    -------
    >>> from linalg import lu_decomposition
    >>> from numpy import array
    >>> A = array([[-2.0, 9.2, 3.8],
    >>>            [-0.6, 2.7, 2.4],
    >>>            [-1.0, 4.9, -4.9]])
    >>> L, U, p = lu_decomposition(A)
    >>> b = array([15.0, 5.7, 1.0])
    >>> c = b[p]
    >>> y = forward_elimination(L, c)
    >>> x = backward_substitution(U, y)

    Bibliography
    ------------
    Numerical Computing with Matlab, Cleve Moler, 2008
    """
    n = A.shape[0]
    p = list(range(n))
    for k in range(n - 1):
        # Find largest element below diagonal in k-th column
        m = argmax(abs(A[k:n, k]))
        m = m + k
        # Swap pivot row
        if m != k:
            A[[k, m], :] = A[[m, k], :]
            p[m], p[k] = p[k], p[m]
        # Skip elimination if pivot is zero
        if A[k, k] == 0.0:
            raise ValueError("Error : zero pivot !")
        # Compute multipliers
        A[k + 1 : n, k] = A[k + 1 : n, k] / A[k, k]
        # Update the remainder of the matrix
        A[k + 1 : n, k + 1 : n] = A[k + 1 : n, k + 1 : n] - outer(
            A[k + 1 : n, k], A[k, k + 1 : n]
        )
    # Separate result
    L = tril(A, -1) + eye(n)
    U = triu(A)
    return L, U, p


def lu_no_pivoting(A):
    """
    Computes the LU decomposition of A, without row pivoting.

    This function produces a unit lower triangular
    matrix L, an upper triangular matrix U, such that

    L @ U = A.

    Parameters
    ----------
    A : np.array((n, n))
        The matrix.

    Returns
    -------
    L : np.array((n, n))
        A lower triangular matrix.
    U : np.array((n, n))
        An upper triangular matrix.

    Example
    -------
    >>> from linalg import lu_no_pivoting
    >>> from numpy import array
    >>> A = array([[-2.0, 9.2, 3.8],
    >>>            [-0.6, 2.7, 2.4],
    >>>            [-1.0, 4.9, -4.9]])
    >>> L, U = lu_no_pivoting(A)
    """
    n = A.shape[0]
    for k in range(n - 1):
        # Skip elimination if column is zero
        if A[k, k] == 0.0:
            raise ValueError("Error : zero pivot !")
        # Compute multipliers
        A[k + 1 : n, k] = A[k + 1 : n, k] / A[k, k]
        # Update the remainder of the matrix
        A[k + 1 : n, k + 1 : n] = A[k + 1 : n, k + 1 : n] - outer(
            A[k + 1 : n, k], A[k, k + 1 : n]
        )
    # Separate result
    L = tril(A, -1) + eye(n)
    U = triu(A)
    return L, U


if __name__ == "__main__":
    import numpy as np

    # backward_substitution
    print(u"")
    print(u"backward_substitution")
    U = array(
        [
            [1.0, 2.0, 3.0, 4.0],
            [0.0, 5.0, 6.0, 7.0],
            [0.0, 0.0, 8.0, 9.0],
            [0.0, 0.0, 0.0, 10.0],
        ]
    )
    e = array([1.0, 2.0, 3.0, 4.0])
    b = U @ e
    x = backward_substitution(U, b)
    print(u"x=")
    print(x)
    np.testing.assert_array_almost_equal(x, e)

    # forward_elimination
    print(u"")
    print(u"forward_elimination")
    L = array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [2.0, 3.0, 0.0, 0.0],
            [4.0, 5.0, 6.0, 0.0],
            [7.0, 8.0, 9.0, 10.0],
        ]
    )
    e = array([1.0, 2.0, 3.0, 4.0])
    b = L @ e
    x = forward_elimination(L, b)
    print(u"x=")
    print(x)
    np.testing.assert_array_almost_equal(x, e)

    # linalg
    print(u"")
    print(u"linalg")
    A = array([[10.0, -7.0, 0.0], [-3.0, 2.0, 6.0], [5.0, -1.0, 5.0]])
    print(u"A=")
    print(A)
    L, U, p = lu_decomposition(A)
    print(u"L=")
    print(L)
    print(u"U=")
    print(U)
    print(u"p=", p)
    np.testing.assert_array_almost_equal(p, [0, 2, 1])
    Lexpected = array([[1.0, 0.0, 0.0], [0.5, 1.0, 0.0], [-0.3, -0.04, 1.0]])
    np.testing.assert_array_almost_equal(L, Lexpected)
    Uexpected = array([[10.0, -7.0, 0.0], [0.0, 2.5, 5.0], [0.0, 0.0, 6.2]])
    np.testing.assert_array_almost_equal(U, Uexpected)

    # linalg
    print(u"")
    print(u"linalg")
    A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
    print(u"A=")
    print(A)
    L, U, p = lu_decomposition(A)
    print(u"L=")
    print(L)
    print(u"U=")
    print(U)
    print(u"p=", p)
    np.testing.assert_array_almost_equal(p, [0, 2, 1])
    Lexpected = array([[1.0, 0.0, 0.0], [0.5, 1.0, 0.0], [0.3, -0.2, 1.0]])
    np.testing.assert_array_almost_equal(L, Lexpected)
    Uexpected = array([[-2.0, 9.2, 3.8], [0.0, 0.3, -6.8], [0.0, 0.0, -0.1]])
    np.testing.assert_array_almost_equal(U, Uexpected)

    # lu_no_pivoting
    print(u"")
    print(u"lu_no_pivoting")
    import sys
    from numpy.linalg import cond

    eps = sys.float_info.epsilon
    A = array([[2 * eps, 1.0], [1.0, 1.0]])
    L, U = lu_no_pivoting(A.copy())
    print(u"L=")
    print(L)
    print(u"cond(L)=", cond(L))
    print(u"U=")
    print(U)
    print(u"cond(U)=", cond(U))

    # lu_no_pivoting
    print(u"")
    print(u"lu_no_pivoting")
    A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
    print(u"A=")
    print(A)
    L, U = lu_no_pivoting(A.copy())
    print(u"L=")
    print(L)
    print(u"U=")
    print(U)
    np.testing.assert_array_almost_equal(L @ U, A)
    Lexpected = array([[1.0, 0.0, 0.0], [0.3, 1.0, 0.0], [0.5, -5.0, 1.0]])
    np.testing.assert_array_almost_equal(L, Lexpected)
    Uexpected = array([[-2.0, 9.2, 3.8], [0.0, 0.0 - 0.06, 1.26], [0.0, 0.0, -0.5]])
    np.testing.assert_array_almost_equal(U, Uexpected)

    # Combine linalg, forward_elimination and backward_substitution
    A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
    print(u"A=")
    print(A)
    b = array([15.0, 5.7, 1.0])
    print(u"b=")
    print(b)
    # 1) Decompose
    L, U, p = lu_decomposition(A)
    # Observer que A est changee
    # print A
    # 2) Permute les lignes de b
    c = b[p]
    # 3) Resout Ly=c
    y = forward_elimination(L, c)
    print(u"y=")
    print(y)
    # 4) Resout Ux=y
    x = backward_substitution(U, y)
    print(u"x=")
    print(x)
    expected = array([-1.0, 1.0, 1.0])
    np.testing.assert_array_almost_equal(x, expected)

    # Combine lu_no_pivoting, forward_elimination and backward_substitution
    A = array([[-2.0, 9.2, 3.8], [-0.6, 2.7, 2.4], [-1.0, 4.9, -4.9]])
    print(u"A=")
    print(A)
    b = array([15.0, 5.7, 1.0])
    print(u"b=")
    print(b)
    # 1) Decompose
    L, U = lu_no_pivoting(A)
    # Observer que A est changee
    # print A
    # 2) Resout Ly=b
    y = forward_elimination(L, b)
    print(u"y=")
    print(y)
    # 3) Resout Ux=y
    x = backward_substitution(U, y)
    print(u"x=")
    print(x)
    expected = array([-1.0, 1.0, 1.0])
    np.testing.assert_array_almost_equal(x, expected)
