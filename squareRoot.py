def average(a, b):
    return (a + b) / 2

def squareRoot(num, low, high):
    """'low'から'high'までの範囲内で数当てゲームの戦略を応用することにより、指定された数字の平方根を見つける"""
    for i in range(20):
        guess = average(low, high)
        if guess ** 2 == num:
            break
        elif guess ** 2 > num: #"小さい数を予想すべき"
            high = guess
        else: #"大きい数を予想すべき"
            low = guess
    print(guess)

squareRoot(60, 7, 8)
