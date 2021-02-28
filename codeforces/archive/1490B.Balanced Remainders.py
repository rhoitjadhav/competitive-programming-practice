class Solution:
    def solve(self, n, arr):
        lst = [0, 0, 0]
        c = n // 3
        result = 0

        for a in arr:
            mod = a % 3
            if mod == 0:
                lst[0] += 1
            elif mod == 1:
                lst[1] += 1
            else:
                lst[2] += 1

        while True:
            if self.is_same(c, lst) is True:
                return result

            minn = self.min_(lst)
            lst[minn] += 1
            lst[minn - 1] -= 1
            result += 1

    def is_same(self, c, arr):
        for a in arr:
            if a != c:
                return False

        return True

    def min_(self, arr):
        index = 0
        minn = arr[0]

        for i in range(1, 3):
            if arr[i] < minn:
                index = i
                minn = arr[i]

        return index


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
