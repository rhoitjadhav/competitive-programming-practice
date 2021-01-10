def digitDegree(n):
    count = 0
    while True:
        if n // 10 == 0:
            return count

        n = get_sum(n)
        count += 1

def get_sum(num):
    _sum = 0
    while num != 0:
        rem = num % 10
        num //= 10
        _sum += rem

    return _sum

num = 91

result = digitDegree(num)
print(result)
