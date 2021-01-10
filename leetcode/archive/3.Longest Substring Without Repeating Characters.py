# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        count = 0
        l = 0
        r = 1
        for i in range(1, len(s)):
            temp = s[l:r]
            if s[i] in temp:
                if count < abs(l - r):
                    count = abs(l - r)
                l += temp.find(s[r]) + 1

            r += 1

        if count < abs(l - r):
            count = abs(l - r)

        return count


s = "ohomm"

sol = Solution()

result = sol.lengthOfLongestSubstring(s)
print(result)
