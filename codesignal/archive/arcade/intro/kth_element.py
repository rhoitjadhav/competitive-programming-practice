def remove(a, k):
    n = len(a)
    if k >= n or n < 1:
        return a
    num = a[k - 1]

    output = []
    for i in range(n):
        if (i + 1) % num != 0:
            output.append(a[i])
    
    return output

a = [2, 4, 6, 8, 10]
k = 2
print(remove(a, k))
