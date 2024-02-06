# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        count = 0
        l = 0
        r = 1
        for i in range(1, n):
            temp = s[l:r]
            if s[i] in temp:
                count = max(count, abs(l-r))
                l += temp.find(s[r]) + 1

            r += 1

        count = max(count, abs(l-r))

        return count


s = "ohomm"

sol = Solution()

result = sol.lengthOfLongestSubstring(s)
print(result)
