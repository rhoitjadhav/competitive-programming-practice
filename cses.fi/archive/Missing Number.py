class Solution:
    def solve(self, n, arr):
        result = 0
        for i in range(n):
            result += i + 1

        for a in arr:
            result -= a

        return result


if __name__ == "__main__":
    sol = Solution()

    n = int(input())
    arr = list(map(int, input().split()))

    result = sol.solve(n, arr)
    print(result)
