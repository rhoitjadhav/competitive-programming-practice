def countTriplets1(arr, r):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] * r == arr[j] and arr[j] * r == arr[k]:
                    count += 1

    return count


def countTriplets(arr, r):
    count = 0
    before = {}
    after = {}

    for a in arr:
        if after.get(a):
            after[a] += 1
        else:
            after[a] = 1

    for i in range(len(arr)):
        after[arr[i]] -= 1

        if (arr[i] % r == 0) and (arr[i] // r in before) and (arr[i] * r in after):
            count += before[arr[i] // r] * after[arr[i] * r]

        if before.get(arr[i]):
            before[arr[i]] += 1
        else:
            before[arr[i]] = 1
    
    return count

arr = list(map(int, "1 2 2 4".split()))
r = 2

result1 = countTriplets1(arr, r)
result = countTriplets(arr, r)

print(result1, result)
