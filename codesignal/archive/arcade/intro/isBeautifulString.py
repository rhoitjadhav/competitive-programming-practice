def isBeautifulString(string: str):
    d = {}

    alphabets = list(map(chr, range(97, 123))) 
    
    for a in alphabets:
        d[a] = 0

    for s in string:        
        d[s] += 1

    chars = sorted(d.keys())
    n = len(chars)

    for i in range(n-1):
        if d[chars[i]] < d[chars[i+1]]:
            return False

    return True

string = "bbbb"
result = isBeautifulString(string)
print(result)