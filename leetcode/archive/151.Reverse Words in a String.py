# Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        return " ".join(str_list[::-1])


s = 'abc'
sol = Solution()
result = sol.reverseWords(s)
print(result)
