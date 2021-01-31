class Solution:
    def solve(self, n, k):
        if k == 1:
            result = 1

        elif k >= n:
            result = k // n
            if k % n != 0:
                result += 1

        elif n % k == 0:
            result = 1
        
        else:
            result = 2

        print(result)

if __name__ == "__main__":
    sol = Solution()

    tests = int(input())
    for i in range(tests):
        n, k = list(map(int, input().split()))
        sol.solve(n, k)
