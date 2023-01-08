# Importer les modules
TODO
# 1. Oscillateur Harmonique a la main
def harmosc(y, t):
    ydot = TODO
    return ydot


# 1.1 Methode d'Euler
t0 = 0.0
tfinal = 2 * pi
h = 0.1
y0 = array([1.0, 0.0])
t = t0
y = y0
while t <= tfinal:
    y = TODO
    t = t + h

# 1.2 Solution
print(u"y=", y)
yexact = [cos(tfinal), -sin(tfinal)]
print(u"yexact=", TODO)
print(u"Nombre d'iterations:", TODO)
print(u"Erreur absolue=", TODO)

# 2. Oscillateur Harmonique avec une fonction
tspan = [0.0, 2 * pi]
h = 0.1
y0 = [1, 0]
tout, yout = euler(TODO)
# 2.2 Exact solution
n = 100
t = linspace(0, 2 * pi, n)
yexact = array([cos(t), -sin(t)])
yexact = yexact.T
# 2.3 Phase plot
figure()
plot(TODO)
plot(TODO)
axis("equal")
axis([-1.2, 1.4, -1.4, 1.6])
xlabel(TODO)
ylabel(TODO)
legend(("Euler", "Exact"))
title(TODO)
