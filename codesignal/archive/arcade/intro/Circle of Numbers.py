def circleOfNumbers(n, s):
    summ = s + (n // 2)
    if summ >= n:
        return summ - n
    return summ

n = 6
s = 3

result = circleOfNumbers(n, s)
print(result)
