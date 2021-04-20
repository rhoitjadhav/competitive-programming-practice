class Solution:
    def solve(self, n, arr):
        map = {}
        for i, a in enumerate(arr):
            if map.get(a):
                map[a][0] += 1
                map[a][1] = i                
            else:
                map[a] = [1, i]

        for key in map:
            if map[key][0] == 1:
                return map[key][1] + 1

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
