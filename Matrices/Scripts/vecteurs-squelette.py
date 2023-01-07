from numpy import array, inf
from numpy.linalg import norm
from math import sqrt

#
# 1. Normes de vecteurs
x = array([1.0, 2.0, 3.0])
print(u"x=", x)
print(u"||x||_2=", norm(TODO))
print(u"Check=", sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2))
print(u"||x||_INF=", norm(TODO))
print(u"Check=", max(abs(x)))
print(u"||x||_1=", norm(TODO))
print(u"Check=", sum(abs(x)))

#
# 2. Produit scalaire
def myDotProduct(x, y):
    n = x.shape[0]
    p = 0.0
    for i in range(n):
        p = TODO
    return p


x = array([1.0, 2.0, 3.0])
y = array([4.0, 5.0, 6.0])
print(u"x=")
print(x)
print(u"y=")
print(y)
print(u"x@y=")
print(x @ y)
print(u"myDotProduct=")
print(myDotProduct(TODO))
