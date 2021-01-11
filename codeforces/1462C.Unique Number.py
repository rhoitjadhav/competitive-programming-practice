class Solution:
    def solve(self, num):
        if num > 45:
            return -1

        if num < 10:
            return num

        result = ''
        i = 9
        while True:
            if num <= i:
                result += str(num)
                break

            num = num - i
            result += str(i)
            i -= 1

        return int((result[::-1]))


if __name__ == "__main__":
    s = Solution()

    tests = int(input())
    for i in range(tests):
        result = s.solve(int(input()))
        print(result)
