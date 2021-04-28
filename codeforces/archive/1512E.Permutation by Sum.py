class Solution:
    def get_n_sum(self, n):
        return (n * (n + 1)) // 2

    def get_last_n_sum(self, n, k):
        return (k * ((2 * n) + 1 - k))//2

    def solve(self, n, l, r, s):
        nsum = self.get_n_sum(n)

        if s > nsum:
            return -1

        k = r - l + 1

        low = self.get_n_sum(k)
        high = self.get_last_n_sum(n, k)

        if s < low or s > high:
            return

        result = [-1 for _ in range(n)]
        lr_set = set()
        
        count = l-1
        for i in range(n, 0, -1):
            if k > 0:
                k_ = k - 1
                high = self.get_last_n_sum(i, k)
                low = self.get_n_sum(k_)
                if (high >= s) and (s - i >= low):
                    result[count] = i
                    lr_set.add(i)
                    count += 1
                    s -= i
                    k -= 1

        count = 1
        for i in range(n):
            if result[i] == -1:
                while True:
                    if count in lr_set:
                        count += 1
                    else:
                        break

                result[i] = count
                count += 1

        return " ".join(str(r) for r in result)

if __name__ == '__main__':
    sol = Solution()

    tests = int(input())
    results = []
    for _ in range(tests):
        n, l, r, s = list(map(int, input().split()))
        result = sol.solve(n, l, r, s)
        results.append(result)

    for result in results:
        print(result)

    # arr = list(map(int, "5 1 4 12".split()))
    # result = sol.solve(*arr)
    # print(result)
