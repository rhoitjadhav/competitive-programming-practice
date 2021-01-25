class Solution:
    def solve(self, case, digits):
        result = ''
        brackets = 0

        for digit in digits:
            num = int(digit)

            if num > brackets:
                result += '(' * (num - brackets)
                brackets = num

            if num < brackets:
                result += ')' * (brackets - num)
                brackets = num

            result += str(num)

        result += ')' * brackets

        print(f'Case #{case+1}: {result}')


if __name__ == '__main__':
    sol = Solution()
    tests = int(input())

    for i in range(tests):
        digits = input()
        sol.solve(i, digits)
