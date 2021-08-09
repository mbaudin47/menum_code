from numpy import array, zeros, outer

#
# 1. Produit matrice-vecteur : algorithme
def myMatVecProduct(A, x):
    m = A.shape[0]
    n = A.shape[1]
    xrows = x.shape[0]
    if n != xrows:
        print(u"# columns A does not match # rows x")
    y = zeros(m)
    for i in range(m):
        for j in range(n):
            y[i] = TODO
    return y


A = array(TODO)
x = array(TODO)
print(u"A=")
print(A)
print(u"x=")
print(x)
print(u"A@x=")
print(A @ x)
print(u"myMatVecProduct(A,x)=")
print(myMatVecProduct(A, x))

#
# 2. Produit matrice-matrice : algorithme
def myMatMatProduct(A, B):
    m = A.shape[0]
    p = A.shape[1]
    pbis = B.shape[0]
    n = B.shape[1]
    if p != pbis:
        print(u"# columns A does not match # rows B")
    C = zeros((m, n))
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i, j] = TODO
    return C


A = array(TODO)
B = array(TODO)
print(u"A=")
print(A)
print(u"B=")
print(B)
print(u"A@B=")
print(A @ B)
print(u"myMatMatProduct(A,B)=")
print(myMatMatProduct(A, B))

# 3. Produit tensoriel
x = array(TODO)
print(u"x=")
print(x)
y = array(TODO)
print(u"y=")
print(y)
print(u"outer(x,y)=")
print(outer(x, y))
