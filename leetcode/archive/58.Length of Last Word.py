# Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])            

s = Solution()
w = "a "
print(s.lengthOfLastWord(w))
