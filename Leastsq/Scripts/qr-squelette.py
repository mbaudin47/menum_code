# Import des modules
TODO
# 1. Ajustement polynomial avec QR
t = array([1971.0, TODO, 2019.0])
y = array([0.3104, TODO, 4.233])
#
# Résoudre avec QR
n = 3
X = TODO
Q, R = TODO
z = TODO
beta = TODO
# 2. Utiliser polynomial_fit et polynomial_value
beta = polynomial_fit(t, y, 3)
u = linspace(1970, 2020, 100)
v = polynomial_value(beta, u)
# Faire un dessin
TODO
# 3. Prédire le nombre de passagers en 2030
beta = polynomial_fit(t, y, 2)
u = array([2030.0])
pop = polynomial_value(beta, u)
