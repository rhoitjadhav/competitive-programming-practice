# Find Digits
def findDigits(n):
    if n == 0:
        return 1

    count = 0
    num = n

    while n != 0:
        rem = n % 10
        n //= 10

        if rem != 0 and num % rem == 0:
            count += 1

    return count


n = 1012
result = findDigits(n)
print(result)
