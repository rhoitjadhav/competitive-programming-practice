def alphabeticShift(s):
    output = ''

    for c in s:
        if c == 'z':
            output += 'a'
        else:
            output += chr(ord(c) + 1)
    
    return output

string = 'crazy'
result = alphabeticShift(string)

print(result)
