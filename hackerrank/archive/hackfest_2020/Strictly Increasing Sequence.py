def whoIsTheWinner(a):
    n = len(a)
    if n == 1: return "First"

    misplaced = 0
    for i in range(n-1):
        if a[i] >= a[i+1]:
            misplaced += 1 

    if misplaced == 0:
        return "First"
    
    if n % 2 == 0:
        return "Second"
    else:
        return "First"



a = list(map(int, "2 3".split()))

result = whoIsTheWinner(a)
print(result)
