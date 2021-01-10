# Beautiful Days at the Movies
def beautifulDays(s, e, k):
    beautiful = 0
    for i in range(s, e + 1):
        if abs(i - (int(str(i)[::-1]))) % k == 0:
            beautiful += 1

    return beautiful


a = list(map(int, "13 45 3".split()))
result = beautifulDays(a[0], a[1], a[2])
print(result)
