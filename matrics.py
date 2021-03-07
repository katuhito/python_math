# 行列の計算
A = [[2,3], [5,-8]]
B = [[1,-4], [8,-6]]

def addMatrics(a, b):
    """2つの2×2行列を加算する"""
    C = [[a[0][0] + b[0][0], a[0][1] + b[0][1]], [a[1][0] + b[1][0], a[1][1] + B[1][1]]]
    return C

C = addMatrics(A, B)
print(C)

# 行列のかけ算
def multMatrix(a, b):
    # 行列aと行列ｂを掛けた結果を返す
    m = len(a) #1番目の行列の行数
    n = len(b[0]) #2番目の行列の列数
    newmatrix = []
    for i in range(m):
        row = []
        # bの全ての列を処理
        for j in range(n):
            sum1 = 0
            # 現在の列にある全ての要素を処理
            for k in range(len(b)):
                sum1 += a[i][k] * b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix


