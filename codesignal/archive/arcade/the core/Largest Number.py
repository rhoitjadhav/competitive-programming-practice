def largestNumber(n):
    result = 0
    n -= 1
    while n != -1:
        result += 9 * 10 ** n
        n -= 1
    
    return result

def largestNumber1(n):
    return 10 ** n - 1

n = 3

result = largestNumber(n)
print(result)
