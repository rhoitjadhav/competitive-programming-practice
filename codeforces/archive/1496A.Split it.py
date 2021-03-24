class Solution:
    def solve(self, n, k, string):
        if (n == 0) or (n / 2 == k):
            return "NO"

        if k == 0:
            return "YES"

        for i in range(k):
            if string[i] != string[n - i - 1]:
                return "NO"

        return "YES"


if __name__ == "__main__":
    sol = Solution()
    tests = int(input())
    results = []
    for test in range(tests):
        n, k = list(map(int, input().split()))
        string = input()
        result = sol.solve(n, k, string)
        results.append(result)

    for result in results:
        print(result)