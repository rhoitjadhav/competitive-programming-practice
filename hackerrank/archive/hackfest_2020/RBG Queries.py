def mixColors(c, q):
    n = len(q)
    m = len(c)
    res = []

    colors_set = set()
    gmax_set = set()

    for i in range(m):
        colors_set.add(tuple(c[i]))

    gmax = [c[0]]
    for j in range(1, m):
        gmax.append([max(gmax[j-1][0], c[j][0]), max(gmax[j-1][1], c[j][1]), max(gmax[j-1][2], c[j][2])])

    for g in gmax:
        gmax_set.add(tuple(g))

    print(colors_set)
    print(gmax_set)
    
    for i in range(n):
        # Search
        if tuple(q[i]) in colors_set:
            res.append("YES")
            continue

        # Max of colors
        if tuple(q[i]) in gmax_set:
            res.append("YES")
            continue

        res.append("NO")

    return res


c = [[1, 1, 1],
     [0, 0, 2],
     [5, 0, 0],
     [5, 2, 2]]

q = [[0, 0, 2], [5, 1, 2], [5, 3, 2]]
result = mixColors(c, q)
print("\n".join(result))
