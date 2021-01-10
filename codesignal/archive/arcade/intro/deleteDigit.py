def deleteDigit(n):
    gmax = 0
    count = 0
    num = 0
    while n != 0:
        rem = n % 10
        n //= 10
        val = n * 10 ** count + num
        num = rem * 10 ** count + num
        gmax = max(gmax, val)
        count += 1

    return gmax

n = 2
result = deleteDigit(n)

print(result)
