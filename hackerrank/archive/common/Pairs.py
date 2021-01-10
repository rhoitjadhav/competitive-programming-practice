def pairs(k, arr):
    count = 0
    sets = set(arr)
    n = len(arr)

    for i in range(n):
        key = (arr[i] - k)
        if key in sets:
            print(key, arr[i])
            count += 1

    return count


k = 2
arr = list(map(int, "1 5 3 4 2".split()))

result = pairs(k, arr)
print(result)
