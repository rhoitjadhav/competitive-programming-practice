def makeAnagram(a, b):
    str1 = []
    for s in a:
        if s in b:
            find = b.find(s)
            b = b[:find] + b[find+1:]
            str1.append(s)
    
    for s in str1:
        find = a.find(s)
        a = a[:find] + a[find+1:]

    return len(a) + len(b)

a = 'cde'
b = 'dcf'
result = makeAnagram(a, b)
print(result)
