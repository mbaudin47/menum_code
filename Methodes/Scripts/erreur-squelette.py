from floats import computeDigits, relativeError

#
# Erreur absolue, relative
def computeError(exact, computed, basis):
    abserr = abs(computed - exact)
    relerr = relativeError(exact, computed)
    d = computeDigits(exact, computed, basis)
    print(u"computed=", computed, ", exact=", exact)
    print(u"Absolute error:", abserr)
    print(u"Relative error:", relerr)
    print(u"Correct base-", basis, " digits:", d)


a = 1.0
b = 1.0
computeError(TODO)
computeError(TODO)
