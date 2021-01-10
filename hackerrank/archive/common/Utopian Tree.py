# Utopian Tree

def utopianTree(n):
    if n == 0:
        return 1
    if n == 1:
        return 2

    height = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2

    return height


n = 2
result = utopianTree(n)
print(result)
