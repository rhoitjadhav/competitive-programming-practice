class Solution:
    def solve(self, q, d):
        n = len(q)

        for i in range(n):
            if q[i] >= d * 10:
                print('YES')

            elif d == 1:
                print('YES')
            
            elif q[i] % 10 == d:
                print('YES')

            else:
                result = self.is_lucky(q[i], d)
                print(result)

    def is_lucky(self, num, d):
        while True:
            if num < d:
                return 'NO'

            if num % 10 == d:
                return 'YES'

            num -= d


if __name__ == "__main__":
    sol = Solution()

    tests = int(input())
    for i in range(tests):
        _, d = list(map(int, input().split()))
        q = list(map(int, input().split()))
        sol.solve(q, d)
