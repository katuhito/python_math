from math import sqrt

def quad(a, b, c):
    """a*x**2 + b*x + c = 0形式の方程式の解を計算する"""
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2
    
