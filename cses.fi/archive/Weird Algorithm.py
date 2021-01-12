class Solution:
    def solve(self, n):
        print(n, end=" ")

        while n != 1:
            if self.is_odd(n):
                n = (n * 3) + 1
            else:
                n //= 2

            print(n, end=" ")

    def is_odd(self, num):
        if num % 2 != 0:
            return True

        return False


if __name__ == "__main__":
    sol = Solution()

    n = int(input())
    sol.solve(n)
