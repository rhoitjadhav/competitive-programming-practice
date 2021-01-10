# Extra Long Factorials
def extraLongFactorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


n = 25
result = extraLongFactorials(n)
print(result)
