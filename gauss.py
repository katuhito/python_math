# divisor = 2
# row = [1,2,3,4,5]
# for i, term in enumerate(row):
#     row[i] = term / divisor
# print(row)

def gauss(A):
    """ガウスの消去法を使って行列を単位行列に変換し、最終列にそれぞれの変数の解を持った行列に変換する"""
    m = len(A)
    n = len(A[0])
    for j, row in enumerate(A):
        # 対角線上にある要素で割ることにより
        # 対角線上の要素の値が1になるようにする
        if row[j] != 0:  #対角線上の要素は0にならない
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term / divisor
        # それぞれの行に対して、他の行を反数に足す
        for i in range(m):
            if i != j: #j行目は処理しない
                # 反数を計算
                addinv = -1 * A[i][j]
                # i番目の列を全て処理
                for ind in range(n):
                    # i行目にある要素に反数を掛けた値とj行目の要素を足す
                    A[i][ind] += addinv * A[j][ind]
    return A

# 例えば
B = [[2,1,-1,8],[-3,-1,2,-1],[-2,1,2,-3]]
print(gauss(B))



