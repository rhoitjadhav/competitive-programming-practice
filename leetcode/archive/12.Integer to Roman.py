class Solution:
    def __init__(self) -> None:
        pass
        
    def intToRoman(self, num: int) -> str:
        symbols = {
            1000: 'M',
            900: 'CM',
            500: 'D', 
            400: 'CD',
            100: 'C',
            90: 'XC', 
            50: 'L',
            40: 'XL', 
            10: 'X',
            9: 'IX',
            5: 'V', 
            4: 'IV',
            1: 'I', 
        }

        if num in symbols:
            return symbols[num]

        result = ''
        for s in symbols:
            nsymbol = num // s
            if nsymbol != 0:
                result += symbols[s] * nsymbol
            
            num %= s

        return result

sol = Solution()
num = 888
result = sol.intToRoman(num)
print(result)

"""

1.  888 // 500 = 1
    888 % 500 = 388
    500 => 'D' * 1
    D

2.  388 // 100 = 3
    388 % 100 = 88
    100 => 'C' * 3
    DCCC

3.  88 // 50 = 1
    88 % 50 = 38
    50 => 'L' * 1
    DCCCL

4.  38 // 10 = 3
    38 % 10 = 8
    10 => 'X' * 3
    DCCCLXXX

5.  8 // 5 = 1
    8 % 5 = 3
    5 => 'V' * 1
    DCCCLXXXV

6.  3 // 1 = 3
    3 % 1 = 1
    1 => 'I' * 3
    DCCCLXXXVIII

DCCCLXXXVIII

"""
