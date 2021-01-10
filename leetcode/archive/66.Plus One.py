# Plus One
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert list into integer
        n = len(digits)
        num = 0
        for i in range(n - 1, -1, -1):
            num += digits[i] * 10 ** (n - i - 1)
        
        num += 1

        output = []
        i = 1
        while num != 0:
            mod = num % 10
            num //= 10
            output.append(mod)
            i += 1

        output.reverse()
        return output

s = Solution()
digits = [0]
print(s.plusOne(digits))