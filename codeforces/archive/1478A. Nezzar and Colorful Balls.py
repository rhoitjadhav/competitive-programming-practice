class Solution:
    def solve(self, n, arr):
        if n <= 1:
            gcount = 1

        else:
            gcount = ccount = 1
            for i in range(1, n):
                if arr[i] == arr[i - 1]:
                    ccount += 1
                    gcount = max(gcount, ccount)
                
                else:
                    ccount = 1

            gcount = max(gcount, ccount)

        print(gcount)


if __name__ == "__main__":
    sol = Solution()

    tests = int(input())
    for i in range(tests):
        n = int(input())
        a = list(map(int, input().split()))
        sol.solve(n, a)
