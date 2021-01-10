# Happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        result = 0
        dct = dict()
        while result != 1:
            result = 0
            if dct.get(n, False):
                return False
            else:
                dct[n] = True
            while n != 0:
                b = n % 10
                n = n // 10
                result = (b ** 2) + result 
            n = result
            
        return True


s = Solution()
print(s.isHappy(19))