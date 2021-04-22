class Solution:
    def solve(self, n, b):
        m = n + 2
        b.sort()

        summ = sum(b[:m-1])
        largest = b[m-1]
        largest2 = b[m-2]

        for i in range(m-1):
            if summ - b[i] == largest:
                return self.return_arr(i, b, 1, m)

        if summ - largest2 == largest2:
            return " ".join([str(b[i]) for i in range(m-2)])

        return -1

    def return_arr(self, i, b, k, m):
        return " ".join([str(b[j]) for j in range(m-k) if j != i])


if __name__ == '__main__':
    sol = Solution()
    tests = int(input())
    results = []
    for _ in range(tests):
        n = int(input())
        b = list(map(int, input().split()))
        result = sol.solve(n, b)
        results.append(result)

    for result in results:
        print(result)
