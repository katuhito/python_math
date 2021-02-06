def factors(num):
    """numの約数リストを返す"""
    factorList = []
    for i in range(1, num + 1):
        if num % 1 == 0:
            factorList.append(i)
    return factorList
        
