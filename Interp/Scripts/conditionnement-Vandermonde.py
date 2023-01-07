#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Condition number of Vandermonde matrices. 

See (Gautschi, 1974) eq. 6.3 page 345 for equidistant nodes  
on [-1, 1].
See also (Gautschi, 2012) page 24.
See (Higham, 2002) page 418 for other condition numbers.
See (Gautschi, 1974) eq. 6.5 page 346 for Chebyshef nodes 
on [-1, 1].

References
----------
Gautschi, W. (1974). Norm estimates for inverses of Vandermonde matrices. 
Numerische Mathematik, 23(4), 337-347.

Gautschi, W. (2012). _Numerical analysis, Second Edition_. 
Springer Science & Business Media.

Higham, Nicholas J. _Accuracy and stability of numerical algorithms_. 
Society for industrial and applied mathematics, 2002.

"""
import numpy as np

def VandermondeEquidistantConditionAsymptotic(n):
    """
    Asymptotic condition number of Vandermonde matrix in infinite norm.
    With equidistant nodes.
    """
    c = np.exp(-np.pi / 4.0) / np.pi * np.exp(n * (np.pi / 4.0 + 0.5 * np.log(2)))
    return c

def VandermondeEquidistantCondition(n):
    """
    Condition number of Vandermonde matrix in infinite norm.
    With equidistant nodes.
    """
    x = np.linspace(-1.0, 1.0, n)
    V = np.vander(x)
    c = np.linalg.cond(V, np.inf)
    return c
def VandermondeChebyshevConditionAsymptotic(n):
    """
    Asymptotic condition number of Vandermonde matrix in infinite norm.
    With Chebyshev nodes.
    """
    c = 3.0 ** 0.75 / 4 * (1.0 + np.sqrt(2.0)) ** n
    return c

def VandermondeChebyshevCondition(n):
    """
    Condition number of Vandermonde matrix in infinite norm.
    With Chebyshev nodes.
    """
    k = np.array(range(n))
    x = -np.cos((2 * (k + 1) - 1) * np.pi / (2 * n))
    V = np.vander(x)
    c = np.linalg.cond(V, np.inf)
    return c

print("Condition number of Vandermonde matrix in infinite norm")
print("Asymptotic condition number, with equidistant nodes")
for n in [5, 10, 20, 40, 80, 160]:
    c = VandermondeEquidistantConditionAsymptotic(n)
    print("n = %d, c[inf] = %.3e" % (n, c))
    
    
print("Condition number, with equidistant nodes")
for n in [5, 10, 20, 40, 80, 160]:
    c = VandermondeEquidistantCondition(n)
    print("n = %d, c[inf] = %.3e" % (n, c))


print("Asymptotic condition number, with Chebyshev nodes")
for n in [5, 10, 20, 40, 80, 160]:
    c = VandermondeChebyshevConditionAsymptotic(n)
    print("n = %d, c[inf] = %.3e" % (n, c))


print("Condition number, with Chebyshev nodes")
for n in [5, 10, 20, 40, 80, 160]:
    c = VandermondeChebyshevCondition(n)
    print("n = %d, c[inf] = %.3e" % (n, c))

# Compare orders of growth, alpha^n where alpha = 
alpha_equidistant = np.exp(np.pi / 4.0 + 0.5 * np.log(2))
print("Equidistant, alpha = %.3e" % (alpha_equidistant))
alpha_Chebyshev = 1.0 + np.sqrt(2.0)
print("Chebyshev, alpha = %.3e" % (alpha_Chebyshev))
