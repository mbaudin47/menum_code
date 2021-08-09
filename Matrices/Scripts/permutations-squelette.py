from numpy import array, eye

# 1. Matrice de permutation
p = [TODO]
# Convertit en matrice de permutation
I = eye(4)
print(I)
P = I[TODO]
print(P)

# 2. Produit P@A
A = array(list(range(16)))
A = A.reshape((4, 4))
print(A)
print(P @ A)

# 3. Tableau de permutations
p = [TODO]
A = array(TODO)
print(A)
print(A[p, :])
