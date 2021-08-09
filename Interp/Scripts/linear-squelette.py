# Import des modules
TODO
# 1. Un exemple d'interpolation lineaire
x = arange(1, 7)
y = array([16, 18, 21, 17, 15, 12])
# Plot
TODO
# 2. Une fonction d'interpolation lineaire
x = arange(1, 7)
y = array([16, 18, 21, 17, 15, 12])
nu = 100
u = linspace(0.75, 6.25, nu)
v = piecewise_linear(x, y, u)
# Plot
TODO
