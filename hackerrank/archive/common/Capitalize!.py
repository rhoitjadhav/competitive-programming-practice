def solve(strings):
    strings = list(strings)

    strings[0] = strings[0].upper()

    for i in range(1, len(strings)):
        if strings[i - 1] == ' ' and strings[i] != ' ':
            strings[i] = strings[i].upper()

    
    return "".join(strings)

s = "hello world"

result = solve(s)
print(result)