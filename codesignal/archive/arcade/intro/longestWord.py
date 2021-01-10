import re


def longestWord(text):
    matches = re.findall('[a-zA-Z]*', text)
    gmax = 0
    result = ""
    for m in matches:
        if len(m) > gmax:
            gmax = len(m)
            result = m
    
    return result

text = "1!"
result = longestWord(text)

print(result)
