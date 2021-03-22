#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2013 - 2021 - Michaël Baudin
"""
Considère une attaque par force brute d'une clé de hash. 
On détermine le nombre d'attaques nécessaires pour provoquer une collision 
avec une probabilité p.
Si p est proche de zéro (ce que l'on souhaite pour garantir la sûreté de 
la clé), on peut utiliser la fonction log1p pour déterminer n avec 
précision.

Références
http://en.wikipedia.org/wiki/Birthday_attack
https://en.wikipedia.org/wiki/Collision_attack
https://crypto.stackexchange.com/questions/9258/birthday-attack
"""

from math import log, log1p, sqrt

p = 1.0e-18
nbits = 512
H = 2 ** nbits
n = sqrt(-2.0 * H * log(1.0 - p))
print(u"Naif=", n)
n = sqrt(-2.0 * H * log1p(-p))
print(u"Correct=", n)
