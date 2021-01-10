def prod(n):
    p = 1
    while n != 0:
        p *= n % 10
        n //= 10
    
    return p

def digitsProduct(product):
    for i in range(1, 100000):
        if prod(i) == product:
            return i 

    return -1

n = 26
res = digitsProduct(n)

print(res)

