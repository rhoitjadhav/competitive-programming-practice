def arrayManipulation(n, queries):
    arr = [0 for _ in range(n + 2)]

    for a,b,k in queries:
        arr[a] += k
        arr[b+1] -= k
    
    gmax = cmax = 0
    for a in arr:
        cmax += a
        gmax = max(cmax, gmax)

    return gmax

n = 5
q = """
1 2 100
2 5 100
3 4 100
"""

queries = []

for qu in q.strip().split("\n"):
    queries.append(list(map(int, qu.split())))

result = arrayManipulation(n, queries)
print(result)