class Solution:
    def solve(self, n):
        if n <= 2:
            return 1
        
        first = 0
        second = 1

        for i in range(n-1):
            third = first + second
            first = second
            second = third
        
        return second

s = Solution()
n = 7
result = s.solve(n)
print(result)
