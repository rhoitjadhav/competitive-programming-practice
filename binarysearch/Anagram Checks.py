from collections import Counter 

class Solution:
    def solve(self, s0, s1):
        s0_count = Counter(s0)
        s1_count = Counter(s1)
        
        if len(s0_count) != len(s1_count):
            return False

        for key in s0_count:
            if s0_count[key] != s1_count.get(key):
                return False
            
        return True

s = Solution()
s0 = 'silnt'
s1 = 'liste'
result = s.solve(s0, s1)
print(result)
