# Drawing Book 

def pageCount1(n, p):
    return min(p//2, n//2-p//2)

def pageCount(n, p):
    # Median
    median = int(n/2)

    if p <= median:
        # Start
        start = 1
        stop = n
        step = 2
    
    else:
        # End
        if (n % 2) == 0:
            start = n + 1
        else:
            start = n
        
        stop = 1
        step = -2
    
    count = 0
    for i in range(start, stop, step):
        if (i == p) or (i-1 == p):
            return count 
        count += 1

    return count

n = 7
p = 3
result = pageCount(n, p)
print(result)

result1 = pageCount1(n, p)

print(result1)

