# Import des modules
TODO
# 1.1 Define the function
def harmosc(y, t):
    ydot = TODO
    return ydot


# 1.2 Solve the ode
y0 = [TODO]
t = linspace(0, 2 * pi, 100)
y = odeint(TODO)
# 1.3 Phase plot
plot(TODO)
axis("equal")
axis([-1.2, 1.2, -1.2, 1.2])
xlabel(TODO)
ylabel(TODO)
title(TODO)
# 1.4 Regular plot
ode_plot(t, y, "Harmonic oscillator", "-")
