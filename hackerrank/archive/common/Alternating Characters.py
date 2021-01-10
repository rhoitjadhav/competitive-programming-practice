def alternatingCharacters(s):
    n = len(s)
    if len(s) <= 1: return 0
    count = 0

    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1

    return count
    
s = "AAABBB"

result = alternatingCharacters(s)
print(result)

