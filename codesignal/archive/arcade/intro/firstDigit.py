def firstDigit(string: str):
    for s in string:
        if s.isdigit():
            return s

string = "abc1"
result = firstDigit(string)
print(result)
