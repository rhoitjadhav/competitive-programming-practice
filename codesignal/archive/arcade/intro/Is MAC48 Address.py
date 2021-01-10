import re


def isMAC48Address(string: str):
    patternSt = '^[0-9A-F][0-9A-F][-][0-9A-F][0-9A-F][-][0-9A-F][0-9A-F][-][0-9A-F][0-9A-F][-][0-9A-F][0-9A-F][-][0-9A-F][0-9A-F]$'
    return bool(re.match(patternSt, string))
    
string = 'Z1-1B-63-84-45-E6'
result = isMAC48Address(string)
print(result)
