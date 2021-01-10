import math


def gcd(arr):
    result = arr[0]

    for i in range(1, len(arr)):
        result = math.gcd(result, arr[i])

    return result


def maximumValue(a):
    n = len(a)
    gmax = 0
    for i in range(n):
        for j in range(i, n):
            arr = a[i:j+1]
            # gcd
            _gcd = gcd(arr)
            # sum
            _sum = sum(arr)
            # max
            _max = max(arr)
            # f(l, r)
            gmax = max(gmax, _gcd * (_sum - _max))
            print(i+1, j+1, _gcd, _sum, _max)
            # print(i+1, j+1)

    return gmax


a = list(map(int, "7 12 24 6 5".split()))

result = maximumValue(a)
# result = math.gcd(5, 20)

print(result)
