def matchingStrings(strings, queries):
    result = []
    for q in queries:
        count = 0
        for s in strings:
            if q == s:
                count += 1

        result.append(count)

    return result

s = """
abcde
sdaklfj
asdjf
na
basdn
sdaklfj
asdjf
na
asdjf
na
basdn
sdaklfj
asdjf
"""
q = """
abcde
sdaklfj
asdjf
na
basdn
"""
strings = []

for st in s.strip().split("\n"):
    strings.append(st)

queries = []
for qu in q.strip().split("\n"):
    queries.append(qu)

result = matchingStrings(strings, queries)

print(result)
