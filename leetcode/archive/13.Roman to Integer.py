# Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = dct[s[0]]

        for i in range(1, len(s)):
            prev = s[i - 1]
            if ("X" == s[i] or "V" == s[i]) and prev == "I":
                res += dct[s[i]] - 2

            elif ("L" == s[i] or "C" == s[i]) and prev == "X":
                res += dct[s[i]] - 20

            elif ("D" == s[i] or "M" == s[i]) and prev == "C":
                res += dct[s[i]] - 200

            else:
                res += dct[s[i]]

        return res


s = Solution()
print(s.romanToInt("MCMXCIV"))
