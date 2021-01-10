def buildPalindrome(st: str):
    n = len(st)
    substrings = []
    substring = ""
    for i in range(n-1, -1, -1):
        substring += st[i]
        substrings.append(substring)

    index = None
    for s in reversed(substrings):
        if isPalindrome(s):
            if st.rfind(s) == 0:
                return st
            else:
                index = st.rfind(s)
                break

    if index is not None:
        result = st + st[index - 1::-1]
    else:
        result = st + st[-2::-1]

    return result


def isPalindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n-1-i]:
            return False

    return True


st = "abcd"

result = buildPalindrome(st)

print(result)
