class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()
        n = len(string)
        if (n < 1) or (n == 1 and not string[0].isdigit()):
            return 0

        plusminus = False
        neg = False
        if n > 1:
            if not string[0].isdigit() and not string[1].isdigit():
                return 0

            if string[0] in '-+' and string[1].isdigit():
                plusminus = True

        digits = ''

        start = 0
        if plusminus:
            start = 1
            if string[0] == '-':
                neg = True

        for i in range(start, n):
            if string[i].isdigit():
                digits += string[i]

            if not string[i].isdigit():
                break

        if digits == '':
            return 0

        digits = int(digits)
        if neg:
            digits *= -1

        rangee = 2 ** 31
        if digits >= rangee:
            return rangee - 1

        if digits < rangee * -1:
            return rangee * -1

        return digits


sol = Solution()
string = "2147483648"
result = sol.myAtoi(string)
print(result)
