class Solution:
    def longestPalindrome(self, string: str) -> str:
        substrings = []
        result = ''
        gmax = 0
        n = len(string)
        for i in range(n):
            for j in range(i, n):
                substrings.append(string[i:j+1])

        for s in substrings:
            if self.is_palindrome(s):
                if len(s) > gmax:
                    result = s
                    gmax = len(s)

        return result

    def is_palindrome(self, string):
        n = len(string)
        for i in range(n // 2):
            if string[i] != string[n - 1 - i]:
                return False

        return True

s = Solution()
string = 'cbbd'
result = s.longestPalindrome(string)
# result = s.is_palindrome(string)
print(result)
