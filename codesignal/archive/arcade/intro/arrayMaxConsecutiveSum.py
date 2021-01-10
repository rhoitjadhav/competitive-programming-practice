def arrayMaxConsecutiveSum(a, k):
    n = len(a)

    window = 0
    for i in range(k):
        window += a[i]

    _max = window   

    for i in range(1, n-k+1):
        window = window - a[i-1] + a[i+k-1]
        _max = max(window, _max)
    
    return _max


a = [3, 2, 1, 1]
k = 1

result = arrayMaxConsecutiveSum(a, k)
print(result)
