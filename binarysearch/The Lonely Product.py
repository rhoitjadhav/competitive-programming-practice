class Solution:
    def solve(self, a, b, c):
        if a == b and b == c:
            return 1
        elif a == b:
            return c
        
        elif b == c:
            return a
        
        elif a == c:
            return b
        
        else:
            return a * b * c