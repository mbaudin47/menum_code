# Importer les modules
TODO
# 1. Transport mondial de passagers
t = array([1971.0, TODO, 2019.0])
y = array([0.3104, TODO, 4.233])
m = TODO
# Le nombre d'inconnues
n = 3
# Calculer la matrice X
X = TODO
print(u"cond(X)=", TODO)
# Résoudre les équations normales
A = TODO
print(u"cond(A)=", TODO)
b = TODO
beta = TODO
# Evaluer le polynôme
m = 100
u = linspace(1890, 2020, m)
X = vander(u, n)
v = X @ beta
# Faire un dessin
TODO
# 2. La fonction polynomial_fit_normal_equations
beta = polynomial_fit_normal_equations(t, y, 3)
u = linspace(1970, 2020, 100)
v = polynomial_value(beta, u)
# Faire un dessin
TODO
# 3. Prédire le nombre de passagers en 2030
beta = polynomial_fit_normal_equations(t, y, 3)
u = array([2030.0])
pop = polynomial_value(beta, u)
