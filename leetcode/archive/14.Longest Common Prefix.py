# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) < 1: return ""
        
        pattern = strs[0]
        output = ''

        for i in range(len(pattern)):
            for word in strs[1:]:
                if i >= len(word) or pattern[i] != word[i]:
                    return output
            
            output += pattern[i]

        return output

if __name__ == "__main__":
    s = Solution()
    st = ["ab", "aa"]
    output = (s.longestCommonPrefix(st))
    print(output)
