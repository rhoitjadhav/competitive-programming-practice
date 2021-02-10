class Solution:
    def solve(self, n):
        if (n % 2020 == 0) or (n % 2021 == 0):
            return 'YES'
        
        q = n // 2020
        r = n % 2020

        if q < r:
            return 'NO'
        
        return 'YES'


if __name__ == "__main__":
    s = Solution()

    tests = int(input())
    for i in range(tests):
        result = s.solve(int(input()))
        print(result)
