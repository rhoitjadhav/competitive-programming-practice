# Number Line Jumps

def kangaroo(x1, v1, x2, v2):
    if x2 > x1:
        if v2 > v1:
            return "NO"

    if x1 > x2:
        if v1 > v2:
            return "NO"

    for _ in range(10000):
        x1 = x1 + v1
        x2 = x2 + v2

        if x1 == x2:
            return "YES"

    return "NO"


x1, v1, x2, v2 = tuple(map(int, "0 3 4 2".split()))
result = kangaroo(x1, v1, x2, v2)
print(result)
