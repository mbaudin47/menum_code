# Import des modules
TODO


def humps(x):
    y = TODO
    return y


# 1. Integrate the function humps
Q, fcount = adaptsim_gui(TODO)
expected = 35.85832539549867
print(u"expected=", expected)
print(u"Q=", Q)
digits = computeDigits(TODO)
print(u"Digits=", digits)
print(u"fcount=", fcount)
# 2. See convergence
err = zeros(13)
fcount = zeros(13)
for k in range(13):
    tol = 10 ** -k
    Q, fcount[k] = adaptsim(TODO)
    err[k] = TODO
    ratio = err[k] / tol
    print(u"%8.0e %7d %13.3e %9.3f" % (tol, fcount[k], err[k], ratio))
# Make a plot
plot(fcount, err, "bo")
xscale("log")
yscale("log")
# TODO : labels, titles
