# Sales by Match

def sockMerchant(n, ar):
    count = 0
    sock_set = set()
    for i in range(n):
        if ar[i] in sock_set:
            count += 1
            sock_set.remove(ar[i])

        else:
            sock_set.add(ar[i])

    return count


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(n, ar)
print(result)
