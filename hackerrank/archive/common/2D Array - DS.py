# 2D Array - DS
def solve(a):
    n = len(a)
    m = len(a[0])
    skipi = [1]
    skipj = [0, 2]
    gmax = float("-inf")
    for i in range(n - 2):
        skipi = [i + 1]
        for j in range(m - 2):
            skipj = [j + 0, j + 2]
            summ = 0
            for k in range(i, 3 + i):
                for l in range(j, 3 + j):
                    if k in skipi and l in skipj:
                        print("-", end=" ")    
                    else:
                        summ += a[k][l]
                        print(a[k][l], end=" ")

                print()
            
            print("sum:", summ)
            gmax = max(summ, gmax)
    
    return gmax

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(solve(arr))
