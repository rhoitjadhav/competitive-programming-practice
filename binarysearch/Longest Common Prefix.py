class Solution:
    def solve(self, words):
        n = len(words)
        result = ''
        for i, char in enumerate(min(words)):
            for j in range(len(words)):
                if char != words[j][i]:
                    return result
            result += char

        return result


sol = Solution()
words = ["anthony", "ant", "antigravity"]
result = sol.solve(words)
print(result)
