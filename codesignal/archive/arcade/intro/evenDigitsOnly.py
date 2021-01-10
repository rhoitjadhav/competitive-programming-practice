def evenDigitsOnly(n):
    while n != 0:
        rem = n % 10
        if rem % 2 != 0:
            return False
        n = n // 10

    return True

n = 24246
result = evenDigitsOnly(n)
print(result)
