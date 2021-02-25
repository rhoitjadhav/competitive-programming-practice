class Solution:
    def solve(self, n, arr):
        result = 0
        for i in range(n-1):
            minn = min(arr[i], arr[i+1])
            maxx = max(arr[i], arr[i+1])

            while (maxx / minn) > 2.0:
                minn = minn * 2
                result += 1
        
        return result


if __name__ == '__main__':
    sol = Solution()
    tests = int(input())
    results = []
    for test in range(tests):
        n = int(input())
        arr = list(map(int, input().split()))
        result = sol.solve(n, arr)
        results.append(result)
    
    for result in results:
        print(result)
