# 1. Variables
b = 2  # b est entier
print(u"b=", b)
print(u"type(b)=", type(b))
b = TODO
TODO
del b  # efface la variable b
print(b)  # erreur !
#
# 2. Listes
a = [1.0, 2.0, 3.0]  # Create a list
print(u"a=", a)
print(u"a[0]=", a[0])
print(u"a[TODO]=", a[TODO])
print(u"len(a)=", len(a))  # Determine length of list
a[1:3] = TODO
TODO
#
# 3. Operateurs arithmetiques
# + : addition
# - : soustraction
# * : multiplication
# / : division
# ** : exponentiation
# % : division modulaire
a = 2.0
b = 3.0
print(u"a + b=", a + b)
# TODO : les autres
#
# 4. Operateurs de comparaison
# <, >, <=, >=, ==, !=
a = 2  # Integer
b = 1.99  # Floating point
print(a > b)
# TODO : les autres
#
# 5. Conditions
a = 1.5
if a < 0.0:
    sign = "negative"
elif a > 0.0:
    sign = "positive"
else:
    sign = "zero"

print(u"a is ", sign)

#
# 6. Boucles
# Boucles while
nMax = 5
n = 1
a = []  # Create empty list
while n < nMax:
    a.append(1.0 / n)  # Append element to list
    n = n + 1

print(u"a=", a)
# Sortie : [1.0, 0.5, 0.33333333333333331, 0.25]
#
# Fonction range
start = 1
stop = 5
step = 2
print(u"range(stop)=", list(range(stop)))
print(u"range(start,stop)=", list(range(start, stop)))
print(u"range(start,stop,step)=", list(range(start, stop, step)))
#
# Boucles for
nMax = 5
a = []  # Create empty list
for n in range(1, nMax):
    a.append(1.0 / n)

print(a)
#
# 7. Fonctions maths communes
# abs(a) : |a|
# max(sequence)
# min(sequence)
print(u"abs(-5)=", abs(-5))
print(u"max([2,-2,3])=", max([2, -2, 3]))  # max d'une liste
#
# 8. Formats
a = 1234.56789
n = 9876
print(u"%7.2f" % a)
print(u"n = %6d" % n)  # Pad with spaces
print(u"a = %f" % a)
print(u"a = %e" % a)
print(u"a = %6.2f" % a)
print(u"a = %6.2e" % a)
