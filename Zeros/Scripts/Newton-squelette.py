# Import des modules
TODO

# 3. Definir myFunction
def myFunction(x):
    y = TODO
    return y


# 4. Definir myFunctionPrime
def myFunctionPrime(x):
    y = TODO
    return y


# 5. Utiliser newtongui
N = 100
x = linspace(1.0, 2.0, N)
y = myFunction(x)
plot(TODO)
xlabel(u"x")
ylabel(u"f(x)")
title(u"TODO")
xs, history = newtongui(TODO)
show()

# 6. Utiliser computeDigits
print(u"xs=", xs)
xexact = TODO
d = computeDigits(TODO)
print(u"Correct decimal digits=", d)
print(u"Iterations=", len(history))

# 7. Convergence de la methode
n = TODO
digits = zeros(n)
for i in range(n):
    xs = TODO
    digits[i] = computeDigits(TODO)

plot(TODO)
xlabel(u"Iterations")
ylabel(u"Number of digits")
title(u"Convergence of Newton")
grid()
show()
