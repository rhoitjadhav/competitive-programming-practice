arr = [-23, 4, -3, 8, -12]
n = len(arr)
max = arr[0] * arr[1]
for i in range(1, n):
    if i + 1 == n:
        break
    product = arr[i] * arr[i + 1]

    if product > max:
        max = product

print(max)

