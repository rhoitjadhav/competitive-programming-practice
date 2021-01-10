def longestDigitsPrefix(string: str):
    if string[0].isdigit is False: return ""

    result = ""

    for s in string:
        if s.isdigit():
            result += s
        else:
            break

    return result


s = "12abc34"

result = longestDigitsPrefix(s)
print(result)
