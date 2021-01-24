class Solution:
    def solve(self, string):
        n = len(string)
        if n <= 1:
            return n

        result = 1
        count = 1
        for i in range(1, n):
            if string[i] == string[i-1]:
                count += 1
            else:
                result = max(result, count)
                count = 1

        return max(result, count)


if __name__ == "__main__":
    sol = Solution()

    string = input()
    result = sol.solve(string)
    print(result)
