class Solution:
    def solve(self, n):
        if n == 1:
            return 'NO'

        end = self.nth_root(n)
        for i in range(1, end):
            num = n - (i ** 3)
            if self.is_perfect_cube(num):
                return 'YES'

        return 'NO'

    def nth_root(self, n, k=3):
        x = n**(1./k)
        y = int(x)
        return y + 1 if y != x else y

    def is_perfect_cube(self, x):
        x = abs(x)
        return int(round(x ** (1. / 3))) ** 3 == x


if __name__ == '__main__':
    sol = Solution()
    tests = int(input())
    results = []
    for test in range(tests):
        n = int(input())
        result = sol.solve(n)
        results.append(result)

    for result in results:
        print(result)
