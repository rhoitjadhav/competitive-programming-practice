start_vertex = int(input())
n = int(input())

edges = {}

for i in range(n-1):
    edges[i+1] = input().split()

print(edges)


