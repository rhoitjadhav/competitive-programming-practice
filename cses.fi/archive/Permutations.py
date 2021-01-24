from itertools import permutations


class Solution:
    def solve(self, *args):
        n = args[0]

        if n <= 1:
            return n

        if n <= 3:
            return 'NO SOLUTION'

        result = []

        for i in range(2, n+1, 2):
            result.append(str(i))

        for i in range(1, n+1, 2):
            result.append(str(i))

        return " ".join(result)


if __name__ == "__main__":
    sol = Solution()

    n = int(input())
    result = sol.solve(n)
    print(result)
