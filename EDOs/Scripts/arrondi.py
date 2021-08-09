#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Analyse de la longueur optimale du pas de discrétisation h pour une méthode 
d'ordre p pour la résolution d'une équation différentielle ordinaire.
Calcule le nombre d'itérations N correspondant. 
On suppose que l'intervalle d'intégration est de longueur L = t[final] - t[0] 
et que la constante correspondant à l'ordre de précision est C.
On fait l'hypothèse que l'erreur globale est inférieure ou égale à la 
somme des erreurs locales. 
"""

from sys import float_info
from math import floor

#
# Prise en compte des arrondis
print(u"Prise en compte des arrondis")
#
L = 20.0
C = 100.0
for p in [1, 3, 5, 10]:
    eps = float_info.epsilon
    h = (eps / C / p) ** (1.0 / (p + 1))
    N = L * (p * C / eps) ** (1.0 / (p + 1))
    N = floor(N)
    print(u"p=%d h=%g N=%d" % (p, h, N))
