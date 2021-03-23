class Solution:
    def solve(self, n, arr):
        if n == 1:
            return arr

        arr.sort()
        duplicate = []
        s = set([arr[0]])
        output = [arr[0]]

        for i in range(1, n):
            if arr[i] in s:
                duplicate.append(arr[i])
            else:
                output.append(arr[i])
                s.add(arr[i])

        output.extend(duplicate)
        return output


if __name__ == "__main__":
    sol = Solution()
    tests = int(input())
    results = []
    for test in range(tests):
        n = int(input())
        arr = list(map(int, input().split()))
        result = sol.solve(n, arr)
        results.append(result)

    for result in results:
        for r in result:
            print(r, end=" ")

        print()
