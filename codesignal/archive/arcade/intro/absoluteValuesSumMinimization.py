def absoluteValuesSumMinimization(a):
    n = len(a)
    if n == 1: return a[0]

    _sum = float("inf")
    _num = a[0]
    for i in range(n):
        summ = 0
        for j in range(n):
            summ += abs(a[i] - a[j])
        
        if summ == _sum:
            _num = min(_num, a[i])
        
        elif summ < _sum:
            _num = a[i]
            _sum = summ
        
        else:
            pass


    return _num

a =[-10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

result = absoluteValuesSumMinimization(a)
print(result)
