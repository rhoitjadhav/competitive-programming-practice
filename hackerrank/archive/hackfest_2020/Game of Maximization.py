def maximumStones(a):
    n = len(a)
    even_sum = 0
    odd_sum = 0

    for i in range(0, n, 2):
        even_sum += a[i]

    for j in range(1, n, 2):
        odd_sum += a[j]

    
    diff = abs(even_sum - odd_sum)

    return even_sum + odd_sum - diff

arr = list(map(int, "5 1 1 4".split()))

result = maximumStones(arr)

print(result)


