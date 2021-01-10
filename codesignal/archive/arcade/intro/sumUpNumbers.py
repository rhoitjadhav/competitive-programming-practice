import re

def sumUpNumbers(string: str):
    matches = re.findall(r'\d+', string)

    return sum([int(i) for i in matches])

string = "11 1"
result = sumUpNumbers(string)
print(result)



