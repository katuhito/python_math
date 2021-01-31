def mySum2(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i ** 2 + 1
    return running_sum
