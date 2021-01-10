# Two Strings

def twoStrings(s1, s2):
    hash_set = set()
    for s in s2:
        hash_set.add(s)
    
    for s in s1:
        if s in hash_set:
            return "YES"
    
    return "NO"

s1 = "hello"
s2 = "world"

print(twoStrings(s1, s2))