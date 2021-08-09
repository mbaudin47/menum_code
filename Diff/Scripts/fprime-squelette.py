# Import des modules
TODO
# Definir la fonction
def myfunc(x):
    y = TODO
    return y


# 1. Compute a derivative with 3 methods
x = 1
expected = TODO
h = 1.0e-4
g = (myfunc(x + h) - myfunc(x)) / h
d = computeDigits(expected, g, 10)
print(TODO)
g = (myfunc(x + h) - myfunc(x - h)) / (2 * h)
d = computeDigits(TODO)
print(TODO)
# 2. Use various step sizes
# 2.1 See absolute error.
x = 1
expected = TODO
n = 16
e = zeros(n)
h = logspace(0, -15, n)
for i in range(n):
    g = (myfunc(x + h[i]) - myfunc(x)) / h[i]
    e[i] = TODO
    print(u"h=", h[i], ", g=", g, ", AE=", e[i])

# 2.2 Plot absolute error
n = 100
e = zeros(n)
h = logspace(0, -15, n)
for i in range(n):
    g = (myfunc(x + h[i]) - myfunc(x)) / h[i]
    e[i] = TODO

# Plot
TODO


x = 1.0
expected = TODO
n = 100
d1 = zeros(n)
d2 = zeros(n)
h = logspace(2, -15, n)
for i in range(n):
    g = (myfunc(x + h[i]) - myfunc(x)) / h[i]
    d1[i] = computeDigits(TODO)
    g = (myfunc(x + h[i]) - myfunc(x - h[i])) / (2 * h[i])
    d2[i] = computeDigits(TODO)

# Plot
TODO
