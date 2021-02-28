from math import sqrt

def magnitude(z):
    return sqrt(z[0] ** 2 + z[1] ** 2)

def cMult(u, v):
    """2つの複素数の積を返す"""
    return [u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0]]

def cAdd(a, b):
    """2つの複素数を足す"""
    return [a[0] + b[0], a[1] + b[1]]
    

   