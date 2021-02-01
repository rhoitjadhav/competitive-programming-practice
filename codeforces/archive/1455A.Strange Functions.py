class Solution:
    def solve(self, n):
        count = 0
        while n != 0:
            n //= 10
            count += 1

        print(count)
    


if __name__ == "__main__":
    sol = Solution()

    tests = int(input())
    for i in range(tests):
        n = int(input())
        sol.solve(n)
