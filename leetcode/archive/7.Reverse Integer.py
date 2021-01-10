# Reverse Integer
class Solution:
    def reverse1(self, x: int) -> int:
        if abs(x) > (2 ** 31 - 1):
            return 0

        is_neg = False
        string = str(x)
        if x < 0:
            is_neg = True

        if is_neg:
            string = str(string[1:])
            y = -int(string[::-1])
            if y < -(2 ** 31 - 1):
                return 0
            return y

        else:
            y = int(string[::-1])
            if abs(y) > (2 ** 31 - 1):
                return 0
            return y

    def reverse(self, x: int) -> int:
        sign = 1
        digits = []

        if x % 10 == 0:
            x = x // 10

        if x < 0:
            sign = -1
            x = abs(x)
        while True:
            digit = x % 10
            x = x // 10
            digits.append(digit)
            if x == 0:
                break

        res = 0
        for i in digits:
            res *= 10
            res += i

        if res > 0x7FFFFFFF:
            return 0

        res *= sign
        return res


s = Solution()
print(s.reverse(123))
