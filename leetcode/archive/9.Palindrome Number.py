# Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        return string == string[::-1]


x = 121
s = Solution()
result = s.isPalindrome(x)
print(result)
