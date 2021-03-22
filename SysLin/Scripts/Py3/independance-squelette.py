# Copyright (C) 2013 - 2021 - Michael Baudin

from numpy import array
from numpy.linalg import matrix_rank
from pylab import plot, text, xlabel, ylabel, title, axis, figure


#
# 1. Deux vecteurs independants
print(u"")
print(u"1. Deux vecteurs independants")
A = TODO
print(u"A=")
print(A)
print(u"Rank=", TODO)
#
# 2. Graphique
delta = 0.3
figure()
plot([0.0, A[0, 0]], [0.0, A[1, 0]], "r-")
text(A[0, 0] - delta, A[1, 0], "a1")
plot([0.0, A[0, 1]], [0.0, A[1, 1]], "b--")
text(A[0, 1] + delta, A[1, 1] - delta, "a2")
xlabel(TODO)
ylabel(TODO)
title(TODO)
axis(TODO)

#
# 3. Deux vecteurs independants
print(u"2. Deux vecteurs independants")
A = TODO
print(u"A=")
print(A)
print(u"Rank=", TODO)
#
# 4. Graphique
TODO
