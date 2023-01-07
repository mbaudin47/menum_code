from pylab import plot, yscale, figure, title, xlabel, ylabel
from numpy import log, linspace
from floats import logCond

# 1. Conditionnement de log
x = TODO
print(u"log(", x, ")=", log(x), ", clog(", x, ")=", logCond(x))
# 2. Plot
x = linspace(TODO)
y = TODO
c = TODO
#
figure()
title(TODO)
plot(x, y, "r-")
xlabel(TODO)
ylabel(TODO)
#
figure()
title(TODO)
plot(x, c, "r-")
yscale(TODO)
xlabel(TODO)
ylabel(TODO)
