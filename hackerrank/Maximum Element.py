from collections import deque


stack = deque()
n = int(input())
gmax = float('-inf')
for i in range(n):
    query = input().split()

    if query[0] == '1':
        gmax = max(gmax, int(query[1]))
        stack.append(gmax)

    elif query[0] == '2':
        if stack:
            stack.pop()
        
        if stack:
            gmax = stack[-1]
        
        else:
            gmax = float('-inf')
    
    else:
        print(gmax)
