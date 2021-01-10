# Check Palindrome

string = "abca"

def checkPalindrome(inputString):
    n = len(string)
    for i in range(n//2):
        start = inputString[i]
        end = inputString[(n - 1) - i]

        if start != end:
            return False

    return True
