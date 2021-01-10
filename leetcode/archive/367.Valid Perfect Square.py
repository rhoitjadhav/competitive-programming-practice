# Valid Perfect Square
import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = int(math.sqrt(num))
        return (n * n) == num
            

    # O(log n) solution
    def isPerfectSquare1(self, num: int) -> bool:
        l,h=0,num
        while(l<=h):
            m=(l+h)//2
            if (m*m ==num):
                return True
            elif (m*m < num):
                l=m+1
            else:
                h=m-1
        return False 

s = Solution()
num = 16
s.isPerfectSquare(num)
