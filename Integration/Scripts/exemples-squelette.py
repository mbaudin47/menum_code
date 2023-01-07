# Import des modules
TODO

#
# Exemple A : Singularite non integrable
#
def myfunA(x):
    y = TODO
    return y


# Dessine
x = linspace(0.0, 2.0 / 3.0, 101)
y = TODO
figure()
plot(TODO)
xlabel(TODO)
ylabel(TODO)
title(TODO)

# Division par zero
Q, fcount = adaptsim(myfunA, 0.0, 2.0 / 3.0)

#
# Exemple B : Sans probleme
#
def myfunB(x):
    y = TODO
    return y


# Dessine
TODO
# Calcule
Q, fcount = TODO
expected = TODO
print(u"expected=", expected)
print(u"Q=", Q)
digits = TODO
print(u"Digits=", digits)
print(u"fcount=", fcount)
# Test de adaptsim_gui
Q, fcount = adaptsim_gui(myfunB, 0.0, 2.0 / 3.0)

#
# Exemple C : Singularite apparente
def mysinc(x):
    y = TODO
    return y


# Dessine
TODO

# ZeroDivisionError: float division
Q, fcount = TODO
expected = TODO
digits = TODO

#
# Exemple D : Gerer une singularite apparente I
afterzero = nextafter(0.0, pi)
print(u"afterzero=", afterzero)
Q, fcount = TODO
expected = TODO
digits = TODO
print(u"Digits=", digits)

#
# Exemple E : Gerer une singularite apparente II
def mysincbis(x):
    if x == 0:
        y = 1.0
    else:
        y = sin(x) / x
    return y


Q, fcount = TODO
expected = TODO
digits = TODO
print(u"Digits=", digits)

#
# Exemple F : Arguments supplementaires
def betafun(t, z, w):
    y = TODO
    return y


z = TODO
w = TODO
tol = 1.0e-6
Q, fcount = adaptsim(betafun, 0.0, 1.0, tol, z, w)
expected = TODO
digits = TODO
print(u"Digits=", digits)
