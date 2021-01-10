# Picking Numbers

def pickingNumbers(a):
    maxx = 0
    n = len(a)
    a.sort()
    for i in range(n):
        count = 0
        for j in range(i, n):
            diff = abs(a[i] - a[j])
            if diff == 1 or diff == 0:
                count += 1

        maxx = max(count, maxx)

    return maxx


a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
result = pickingNumbers(a)
print(result)
