def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_ans = 0
    result = []
    for q in queries:
        query = q[0]
        x = q[1]
        y = q[2]

        seq = (x ^ last_ans) % n

        if query == 1:
            seq_list[seq].append(y)

        else:
            last_ans = seq_list[seq][y % len(seq_list[seq])]
            result.append(last_ans)

    return result

n = 2

que = """
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
"""
queries = []
for q in que.strip().split("\n"):
    queries.append(list(map(int, q.split())))

n = 2
result = dynamicArray(n, queries)
print(result)
