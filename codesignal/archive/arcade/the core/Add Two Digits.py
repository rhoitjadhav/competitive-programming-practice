def addTwoDigits(n):
    add = 0
    while n != 0:
        add += n % 10
        n //= 10
    
    return add

n = 29
result = addTwoDigits(n)
print(result)
