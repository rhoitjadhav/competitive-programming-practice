import math


class Solution:
    def solve(self, n):
        if n & (n-1):
            return 'YES'

        else:
            return 'NO'


if __name__ == "__main__":
    sol = Solution()

    tests = int(input())
    for i in range(tests):
        n = int(input())
        result = sol.solve(n)
        print(result)
