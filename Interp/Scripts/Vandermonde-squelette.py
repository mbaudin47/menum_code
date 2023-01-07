# Import des modules
TODO
# 1. Compute and use Vandermonde matrix
x = np.array([-1.0, 0.0, 1.0, 2.0])
V = vander(x)
y = array([TODO])
c = TODO
exact = array([TODO])
# Compute matrix "by hand"
n = x.shape[0]
V = zeros((n, n))
for i in range(n):
    for j in range(n):
        V[i, j] = TODO

# 2. Interpolation de Lagrange
# Number of points where to interpolate
nu = 100
x = arange(0, 4)
y = array([TODO])
u = np.linspace(-1.25, 2.25, nu)
v = polynomial_interpolation(x, y, u)
# Plot
TODO
