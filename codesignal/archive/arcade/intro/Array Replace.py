def arrayReplace(a, r, s):
    n = len(a)
    for i in range(n):
        if a[i] == r:
            a[i] = s

    return a